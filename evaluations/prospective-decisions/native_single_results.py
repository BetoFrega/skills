#!/usr/bin/env python3
"""Collect native standalone results, retaining malformed responses as failures.

This offline adapter preserves the original frozen runner and never repairs or
reruns a model response. It handles a format failure discovered during collection.
"""

import argparse
import json
from pathlib import Path
import re
import time

import native_single as original

from report_validation import validate_schema


def collect(output, root_rollout):
    frozen = original.module(output / "frozen/native_single.py")
    plan, bench = frozen.verify(output)
    cases = {c["case_index"]: c for c in original.get(output / "inputs.json")}
    receipts, threads = {}, {}
    for line in root_rollout.read_text().splitlines():
        event = json.loads(line)
        payload = event.get("payload", {})
        if payload.get("type") == "item_completed":
            item = payload.get("item", {})
            if re.fullmatch(r"/root/sol_single_\d+", item.get("agent_path", "")):
                threads[item["agent_path"]] = item.get("agent_thread_id")
        if payload.get("type") != "agent_message" or not re.fullmatch(
                r"/root/sol_single_\d+", payload.get("author", "")):
            continue
        for content in payload.get("content", []):
            text = content.get("text", "")
            if "Message Type: FINAL_ANSWER" not in text:
                continue
            index = int(payload["author"].rsplit("_", 1)[1])
            if index in receipts:
                raise ValueError("More than one native response for the same case")
            raw = text.split("Payload:\n", 1)[1]
            report, failure = None, None
            try:
                report = json.loads(raw)
                validate_schema(report, original.get(output / "decider-schema.json"))
                bench.validate_report(cases[index]["packet"], report)
            except json.JSONDecodeError as error:
                failure = {"kind": "invalid_json", "detail": str(error)}
            except (ValueError, KeyError, TypeError) as error:
                failure = {"kind": "invalid_report", "detail": str(error)}
            receipts[index] = {"case_index": index, "agent_name": payload["author"],
                "report": report, "raw_report": raw, "failure": failure}
    for index, receipt in receipts.items():
        if not cases[index]["model_assignment_required"]:
            raise ValueError("Unexpected model response for a human gate")
        receipt["agent_thread_id"] = threads.get(receipt["agent_name"])
        if not receipt["agent_thread_id"]:
            raise ValueError("Missing native thread identity")
        job_id = f"c{index:05d}-r0-sol-single"
        job_dir = output / job_id
        job_dir.mkdir(exist_ok=True)
        job = {"job_id": job_id, "decision_id": cases[index]["packet"]["decision_id"],
            "role": "initial_a", "provider": "native_collaboration", "model": plan["model"],
            "effort": plan["effort"], "prompt_file": str(output / "prompts" / f"{index:05d}.txt"),
            "schema_file": str(output / "decider-schema.json"),
            "tool_mode": "assigned_input_loading_then_no_tools"}
        original.put(job_dir / "report.json", receipt["report"])
        (job_dir / "raw-report.txt").write_text(receipt["raw_report"])
        if not (job_dir / "stdout.log").exists():
            original.put(job_dir / "stdout.log", {"structured_output": receipt["report"], "usage": None})
        status = original.get(job_dir / "status.json") if (job_dir / "status.json").exists() else {
            **job, "recorded_finished_at": time.time(), "prompt_sha256": original.sha(Path(job["prompt_file"]))}
        status.update({"state": "failed" if receipt["failure"] else "completed",
            "agent_name": receipt["agent_name"], "agent_thread_id": receipt["agent_thread_id"],
            "failure": receipt["failure"]})
        original.put(job_dir / "status.json", status)
        report = receipt["report"]
        failed = receipt["failure"] is not None
        original.put(output / "outcomes" / f"{index:05d}.json", {"case_index": index,
            "status": "failed" if failed else "escalated" if report["decision"] == "ESCALATE" else "accepted",
            "decision": None if failed else report["decision"], "reports": [] if failed else [report],
            "failure": receipt["failure"], "jobs": [job]})
    original.put(output / "native-receipts.json", list(receipts.values()))
    summary = {"recorded_outcomes": len(receipts) + sum(
        not c["model_assignment_required"] for c in cases.values()), "model_responses": len(receipts),
        "failed": sum(r["failure"] is not None for r in receipts.values()),
        "offline_collector": {"path": str(Path(__file__).resolve()), "sha256": original.sha(Path(__file__)),
            "schema_validator_sha256": original.sha(Path(__file__).with_name("report_validation.py")),
            "reason": "Validate the frozen schema and preserve malformed native output as a failure without repair or new inference."}}
    original.put(output / "run-summary.json", summary)
    print(json.dumps(summary))


def score(output):
    frozen = original.module(output / "frozen/native_single.py")
    original.validate_outcomes(output, [original.get(p) for p in (output / "outcomes").glob("*.json")])
    frozen.score(output)
    result = original.get(output / "scores.json")
    failures = [original.get(p) for p in sorted((output / "outcomes").glob("*.json"))
                if original.get(p)["status"] == "failed"]
    result.update({"failed": len(failures), "failed_case_indices": [r["case_index"] for r in failures],
        "failure_treatment": "Malformed responses are failures; their choices are not accepted, their usage is counted, and they are not rerun."})
    original.put(output / "scores.json", result)
    print(json.dumps({"failed": result["failed"], "failed_case_indices": result["failed_case_indices"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("collect", "score"):
        option = sub.add_parser(name)
        option.add_argument("--output", type=Path, required=True)
        if name == "collect":
            option.add_argument("--root-rollout", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "collect":
        collect(args.output.resolve(), args.root_rollout.resolve())
    else:
        score(args.output.resolve())
