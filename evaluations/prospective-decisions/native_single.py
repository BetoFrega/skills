#!/usr/bin/env python3
"""Prepare and score one native Sol decider per case on the original frozen inputs."""

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import time


def get(path):
    return json.loads(path.read_text())


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(path):
    spec = importlib.util.spec_from_file_location("original_benchmark", path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def prepare(suite, original, output):
    bench = module(suite / "frozen/benchmark.py")
    source = bench.check_suite(suite)
    if get(original / "suite-reference.json")["manifest_sha256"] != sha(suite / "manifest.json"):
        raise ValueError("Original run belongs to a different suite")
    output.mkdir(parents=True, exist_ok=False)
    os.chmod(output, 0o700)
    (output / "frozen").mkdir()
    shutil.copyfile(Path(__file__), output / "frozen/native_single.py")
    shutil.copyfile(suite / "frozen/benchmark.py", output / "frozen/benchmark.py")
    put(output / "decider-schema.json", bench.schema())
    cases = []
    for index in range(source["case_count"]):
        packet = get(suite / "packets" / f"{index:05d}.json")
        old = get(original / "outcomes" / f"c{index:05d}-r0-luna-single.json")
        if bench.facts(packet)["user_gate"]["required"]:
            prompt = None
            put(output / "outcomes" / f"{index:05d}.json", {"case_index": index,
                "status": "escalated", "decision": "ESCALATE", "route": "explicit_user_gate", "jobs": []})
        else:
            if len(old["jobs"]) != 1:
                raise ValueError("Expected exactly one original standalone decider")
            job = old["jobs"][0]
            prompt = Path(job["prompt_file"]).read_text()
            expected = bench.DECIDER + "\n" + bench.encoded({"packet": packet}).decode()
            if prompt != expected or hashlib.sha256(prompt.encode()).hexdigest() != get(
                    original / job["job_id"] / "status.json")["prompt_sha256"]:
                raise ValueError("Original standalone input integrity mismatch")
            path = output / "prompts" / f"{index:05d}.txt"
            path.parent.mkdir(exist_ok=True)
            path.write_text(prompt)
        cases.append({"case_index": index, "packet": packet, "model_assignment_required": prompt is not None})
    put(output / "inputs.json", cases)
    plan = {"version": "posthoc-native-single-v1", "evaluation_kind": "One standalone Sol round on reused cases",
        "source_suite": str(suite), "source_run": str(original), "source_manifest_sha256": sha(suite / "manifest.json"),
        "case_count": len(cases), "repetitions": 1, "max_live_native_agents": 3,
        "model": "gpt-6.1-sol", "effort": "high", "provider": "native_collaboration",
        "selection_rationale": "Requested standalone Sol comparator. High effort is justified by comparing competing schedules across dependency, retry, deadline, and capacity constraints; a reasoning error would directly become a wrong accepted recommendation. No peer reports or judge are supplied.",
        "confidence_level": source["confidence_level"], "max_wrong_accepted_rate": source["max_wrong_accepted_rate"],
        "minimum_eligible_coverage": source["minimum_eligible_coverage"],
        "rates": {"input": 2.0, "cached_input": 0.1, "output": 10.0},
        "price_source": "https://developers.openai.com/api/docs/models/gpt-6.1-sol",
        "limits": ["The same cases have already informed model comparisons; this is exploratory, not untouched confirmation.",
                   "Native input loading differs from the original CLI standalone transport.",
                   "Hosted aliases and inference outputs are not immutable or deterministic."]}
    put(output / "frozen/plan.json", plan)
    files = [*sorted((output / "frozen").iterdir()), output / "inputs.json", output / "decider-schema.json",
             *sorted((output / "prompts").glob("*.txt"))]
    put(output / "freeze.json", {"frozen_at": time.time(),
        "files": {p.relative_to(output).as_posix(): sha(p) for p in files}})
    print(json.dumps({"round": str(output), "case_count": len(cases),
        "required_assignments": sum(c["model_assignment_required"] for c in cases),
        "model": plan["model"], "effort": plan["effort"], "model_calls": 0}))


def verify(output):
    freeze = get(output / "freeze.json")
    for name, expected in freeze["files"].items():
        if sha(output / name) != expected:
            raise ValueError("Frozen standalone artifact changed: " + name)
    if sha(Path(__file__)) != freeze["files"]["frozen/native_single.py"]:
        raise ValueError("Use this round's frozen native_single.py")
    plan = get(output / "frozen/plan.json")
    suite = Path(plan["source_suite"])
    if sha(suite / "manifest.json") != plan["source_manifest_sha256"]:
        raise ValueError("Source suite changed")
    bench = module(suite / "frozen/benchmark.py")
    bench.check_suite(suite)
    return plan, bench


def collect(output, root_rollout):
    plan, bench = verify(output)
    cases = {c["case_index"]: c for c in get(output / "inputs.json")}
    receipts, threads = {}, {}
    for line in root_rollout.open():
        event = json.loads(line)
        p = event.get("payload", {})
        if p.get("type") == "item_completed":
            item = p.get("item", {})
            if re.fullmatch(r"/root/sol_single_\d+", item.get("agent_path", "")):
                threads[item["agent_path"]] = item.get("agent_thread_id")
        if p.get("type") != "agent_message" or not re.fullmatch(r"/root/sol_single_\d+", p.get("author", "")):
            continue
        for content in p.get("content", []):
            text = content.get("text", "")
            if "Message Type: FINAL_ANSWER" not in text:
                continue
            index = int(p["author"].rsplit("_", 1)[1])
            report = json.loads(text.split("Payload:\n", 1)[1])
            if index in receipts:
                raise ValueError("More than one native response for the same case")
            receipts[index] = {"case_index": index, "agent_name": p["author"], "report": report}
    for index, receipt in receipts.items():
        case = cases[index]
        if not case["model_assignment_required"]:
            raise ValueError("Unexpected model response for a human gate")
        receipt["agent_thread_id"] = threads.get(receipt["agent_name"])
        if not receipt["agent_thread_id"]:
            raise ValueError("Missing native thread identity")
        report = receipt["report"]
        bench.validate_report(case["packet"], report)
        job_id = f"c{index:05d}-r0-sol-single"
        job_dir = output / job_id
        job_dir.mkdir(exist_ok=True)
        job = {"job_id": job_id, "decision_id": case["packet"]["decision_id"],
            "role": "initial_a", "provider": "native_collaboration", "model": plan["model"], "effort": plan["effort"],
            "prompt_file": str(output / "prompts" / f"{index:05d}.txt"),
            "schema_file": str(output / "decider-schema.json"), "tool_mode": "assigned_input_loading_then_no_tools"}
        put(job_dir / "report.json", report)
        if not (job_dir / "stdout.log").exists():
            put(job_dir / "stdout.log", {"structured_output": report, "usage": None})
        if not (job_dir / "status.json").exists():
            put(job_dir / "status.json", {**job, "state": "completed", "agent_name": receipt["agent_name"],
                "agent_thread_id": receipt["agent_thread_id"], "recorded_finished_at": time.time(),
                "prompt_sha256": sha(Path(job["prompt_file"]))})
        put(output / "outcomes" / f"{index:05d}.json", {"case_index": index,
            "status": "escalated" if report["decision"] == "ESCALATE" else "accepted",
            "decision": report["decision"], "reports": [report], "jobs": [job]})
    put(output / "native-receipts.json", list(receipts.values()))
    put(output / "run-summary.json", {"recorded_outcomes": len(receipts) + sum(
        not c["model_assignment_required"] for c in cases.values()), "model_responses": len(receipts)})
    print(json.dumps(get(output / "run-summary.json")))


def score(output):
    plan, bench = verify(output)
    suite = Path(plan["source_suite"])
    bench.check_suite(suite, include_private=True)
    records = [get(p) for p in sorted((output / "outcomes").glob("*.json"))]
    if len(records) != plan["case_count"] or {r["case_index"] for r in records} != set(range(plan["case_count"])):
        raise ValueError("Missing or duplicated outcomes")
    keys = {i: get(suite / "private/answers" / f"{i:05d}.json")["acceptable"] for i in range(plan["case_count"])}
    accepted = [r for r in records if r["status"] == "accepted"]
    wrong = sum(r["decision"] not in keys[r["case_index"]] for r in accepted)
    eligible = sum(v != ["ESCALATE"] for v in keys.values())
    coverage = sum(keys[r["case_index"]] != ["ESCALATE"] for r in accepted) / eligible
    tokens, cost, unknown = {"input": 0, "cached_input": 0, "output": 0}, 0.0, 0
    for record in records:
        for job in record["jobs"]:
            usage = bench.usage_for(job, output)
            if usage is None:
                unknown += 1
                continue
            for key, value in usage.items():
                tokens[key] += value
                cost += value * plan["rates"][key] / 1e6
    upper = bench.error_upper_bound(wrong, len(accepted), plan["confidence_level"])
    result = {"evaluation_kind": plan["evaluation_kind"], "cases": len(records), "accepted": len(accepted),
        "correct_accepted": len(accepted) - wrong, "wrong_accepted": wrong,
        "correct_escalations": sum(r["status"] == "escalated" and keys[r["case_index"]] == ["ESCALATE"] for r in records),
        "unnecessary_escalations": sum(r["status"] == "escalated" and keys[r["case_index"]] != ["ESCALATE"] for r in records),
        "eligible_cases": eligible, "eligible_coverage": coverage,
        "wrong_accepted_rate_upper_bound": upper, "model_calls": sum(len(r["jobs"]) for r in records),
        "tokens": tokens, "unknown_usage": unknown, "known_api_equivalent_usd": cost,
        "api_equivalent_usd": cost if unknown == 0 else None,
        "meets_original_numeric_target": upper <= plan["max_wrong_accepted_rate"] and coverage >= plan["minimum_eligible_coverage"],
        "wrong_case_indices": [r["case_index"] for r in accepted if r["decision"] not in keys[r["case_index"]]],
        "limits": plan["limits"] + ["USD is conditional API-equivalent cost, not an account bill; preparation and coordinator are excluded."]}
    put(output / "scores.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--suite", type=Path, required=True)
    p.add_argument("--original", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    for name in ("verify", "collect", "score"):
        p = sub.add_parser(name)
        p.add_argument("--output", type=Path, required=True)
        if name == "collect":
            p.add_argument("--root-rollout", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.suite.resolve(), args.original.resolve(), args.output.resolve())
    elif args.command == "verify":
        plan, _ = verify(args.output.resolve())
        print(json.dumps({"verified_cases": plan["case_count"]}))
    elif args.command == "collect":
        collect(args.output.resolve(), args.root_rollout.resolve())
    else:
        score(args.output.resolve())
