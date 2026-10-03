#!/usr/bin/env python3
"""Freeze, run, and score a post-hoc judge substitution on admitted Luna reports."""

import argparse
import asyncio
import copy
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

from report_validation import validate_schema
from benchmark import schema

VERSION = "posthoc-judge-swap-v3"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get(path):
    return json.loads(path.read_text())


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def prepare(suite, original, output, judge_provider="codex"):
    bench = load_module("source_benchmark", suite / "frozen/benchmark.py")
    source_plan = bench.check_suite(suite)
    reference = get(original / "suite-reference.json")
    if reference["manifest_sha256"] != bench.digest((suite / "manifest.json").read_bytes()):
        raise ValueError("Original run belongs to a different suite")
    arm = next(a for a in source_plan["arms"] if a["id"] == "luna-ensemble")
    if any(s != {"model": "gpt-6-luna", "effort": "high"} for s in arm["roles"].values()):
        raise ValueError("Expected the original all-Luna/high ensemble")
    cases = []
    for index in range(source_plan["case_count"]):
        record = get(original / "outcomes" / f"c{index:05d}-r0-luna-ensemble.json")
        if record["status"] == "failed":
            raise ValueError("Cannot substitute for an incomplete original decision")
        packet = get(suite / "packets" / f"{index:05d}.json")
        borrowed, judges = [], []
        for job in record["jobs"]:
            status = get(original / job["job_id"] / "status.json")
            if status["state"] != "completed":
                raise ValueError("Cannot reuse an incomplete assignment")
            if job["role"] == "judge":
                judges.append(job)
            else:
                borrowed.append({"job_id": job["job_id"], "role": job["role"],
                    "model": job["model"], "effort": job["effort"],
                    "usage": bench.usage_for(job, original),
                    "report_sha256": bench.digest((original / job["job_id"] / "report.json").read_bytes()),
                    "source_status": status})
        if record.get("route") == "explicit_user_gate":
            prompt = None
        else:
            if len(judges) != 1:
                raise ValueError("This replay requires exactly one original terminal judgment")
            prompt = Path(judges[0]["prompt_file"]).read_text()
            expected = bench.JUDGE + "\n" + bench.encoded({
                "reports": [{"embedded_context": packet, **r} for r in record["reports"]],
                "source_checks": bench.source_checks(packet, record["reports"]),
                "candidate": record["reports"][-1]["decision"],
                "additional_decider_used": len(record["reports"]) == 3}).decode()
            if prompt != expected or bench.digest(prompt.encode()) != get(
                    original / judges[0]["job_id"] / "status.json")["prompt_sha256"]:
                raise ValueError("Original judge prompt does not match admitted reports")
        cases.append({"case_index": index, "packet": packet,
            "reports": record.get("reports", []), "initial_judge_prompt": prompt,
            "borrowed_assignments": borrowed, "original_status": record["status"],
            "original_decision": record["decision"], "original_judgment": record.get("judgment")})
    output.mkdir(parents=True, exist_ok=False)
    os.chmod(output, 0o700)
    frozen = output / "frozen"
    frozen.mkdir()
    shutil.copyfile(Path(__file__), frozen / "judge_swap.py")
    shutil.copyfile(suite / "frozen/dispatch.py", frozen / "dispatch.py")
    for filename in ("benchmark.py", "report_validation.py"):
        shutil.copyfile(Path(__file__).with_name(filename), frozen / filename)
    plan = {"version": VERSION, "evaluation_kind": "post-hoc judge substitution; no new confirmation set",
        "judge_provider": judge_provider,
        "source_suite": str(suite), "source_run": str(original),
        "source_manifest_sha256": reference["manifest_sha256"],
        "case_count": source_plan["case_count"], "max_concurrency": 4, "timeout_seconds": 300,
        "confidence_level": source_plan["confidence_level"],
        "max_wrong_accepted_rate": source_plan["max_wrong_accepted_rate"],
        "minimum_eligible_coverage": source_plan["minimum_eligible_coverage"],
        "roles": {"judge": {"model": "gpt-6.1-sol", "effort": "high"},
                  "additional": {"model": "gpt-6-luna", "effort": "high"}},
        "selection_rationale": "Keep admitted Luna deliberations fixed; test whether a Sol/high judge catches the shared capacity-world error. High effort is justified by correlating feasibility and per-world optimality; a wrong acceptance survives the last review. The stronger judge is provisional, not presumed reliable.",
        "rates": {"gpt-6-luna": {"input": 0.1, "cached_input": 0.01, "output": 0.5},
                  "gpt-6.1-sol": {"input": 2.0, "cached_input": 0.1, "output": 10.0}},
        "price_source": "https://developers.openai.com/api/docs/models/gpt-6.1-sol",
        "limits": ["The v1 literal-checker warnings are retained so the first judge input is identical across models.",
                   "Luna deliberations are reused, not independently resampled; their cost is a protocol-equivalent allocation.",
                   "One new Luna reconsideration is permitted only when the original additional slot is unused.",
                   "Cases and failures were observed before selecting this variant; results are exploratory."]}
    put(frozen / "plan.json", plan)
    put(output / "inputs.json", cases)
    put(output / "freeze.json", {"frozen_at": time.time(),
        "files": {p.relative_to(output).as_posix(): bench.digest(p.read_bytes())
                  for p in [*sorted(frozen.iterdir()), output / "inputs.json"]}})
    print(json.dumps({"replay": str(output), "cases": len(cases), "model_calls": 0,
                      "roles": plan["roles"]}))


def verify(replay):
    bench = load_module("replay_benchmark", replay / "frozen/benchmark.py")
    for name, expected in get(replay / "freeze.json")["files"].items():
        if bench.digest((replay / name).read_bytes()) != expected:
            raise ValueError("Changed replay artifact: " + name)
    if bench.digest(Path(__file__).read_bytes()) != get(replay / "freeze.json")["files"]["frozen/judge_swap.py"]:
        raise ValueError("Use this replay's frozen judge_swap.py")
    plan = get(replay / "frozen/plan.json")
    suite = Path(plan["source_suite"])
    if bench.digest((suite / "manifest.json").read_bytes()) != plan["source_manifest_sha256"]:
        raise ValueError("Source suite reference changed")
    source_bench = load_module("original_benchmark", suite / "frozen/benchmark.py")
    source_bench.check_suite(suite)
    return plan, bench


def validate_judgment(packet, reports, judgment):
    validate_schema(judgment, schema(True))
    candidate = reports[-1]["decision"]
    allowed = {e["id"] for e in packet["evidence"] if e["id"].startswith("plan-")} | {"ESCALATE"}
    if (judgment["outcome"] not in {"accept", "reconsider", "challenge_majority", "user_decision"}
            or judgment["preferred_choice"] not in allowed or judgment["candidate"] != candidate):
        raise ValueError("Invalid judgment or changed candidate")
    majority = next((r["decision"] for r in reports
        if sum(s["decision"] == r["decision"] for s in reports) > len(reports) / 2), None)
    if judgment["outcome"] == "accept" and (judgment["preferred_choice"] != candidate
            or (majority is not None and judgment["preferred_choice"] != majority)):
        raise ValueError("Acceptance violates candidate or majority-challenge routing")


async def route(case, assignment):
    if case["initial_judge_prompt"] is None:
        return {"status": "escalated", "decision": "ESCALATE", "route": "explicit_user_gate", "reports": []}
    reports = copy.deepcopy(case["reports"])
    judgment = await assignment("judge", reports, initial=True)
    validate_judgment(case["packet"], reports, judgment)
    if judgment["outcome"] == "reconsider" and len(reports) == 2:
        reports.append(await assignment("additional", reports, gap=judgment["remaining_gap"]))
        judgment = await assignment("judge", reports)
        validate_judgment(case["packet"], reports, judgment)
    accepted = judgment["outcome"] == "accept" and reports[-1]["decision"] != "ESCALATE"
    return {"status": "accepted" if accepted else "escalated",
        "decision": reports[-1]["decision"] if accepted else "ESCALATE",
        "reports": reports, "judgment": judgment}


async def run(replay, output):
    plan, bench = verify(replay)
    if plan.get("judge_provider", "codex") != "codex":
        raise ValueError("Native collaboration assignments require the host's explicit subagent dispatcher")
    transport = load_module("replay_dispatch", replay / "frozen/dispatch.py")
    output.mkdir(parents=True, exist_ok=False)
    semaphore, halted = asyncio.Semaphore(plan["max_concurrency"]), asyncio.Event()
    put(output / "cli-versions.json", {"codex": subprocess.check_output(["codex", "--version"], text=True).strip()})
    for role in ("judge", "additional"):
        put(output / (role + "-schema.json"), bench.schema(role == "judge"))
    put(output / "replay-reference.json", {"replay": str(replay),
        "freeze_sha256": bench.digest((replay / "freeze.json").read_bytes())})

    async def decision(case):
        index, packet = case["case_index"], case["packet"]
        record = {"case_index": index, "status": "failed", "jobs": [], "started_at": time.time()}
        async def assignment(role, reports, initial=False, gap=""):
            job_id = f"c{index:05d}-r0-luna-sol-{role}-{len(reports)}"
            if initial:
                prompt = case["initial_judge_prompt"]
            elif role == "judge":
                prompt = bench.JUDGE + "\n" + bench.encoded({
                    "reports": [{"embedded_context": packet, **r} for r in reports],
                    "source_checks": bench.source_checks(packet, reports),
                    "candidate": reports[-1]["decision"], "additional_decider_used": True}).decode()
            else:
                prompt = bench.DECIDER + "\n" + bench.ADDITIONAL + "\n" + bench.encoded(
                    bench.reconsideration_payload(packet, reports)).decode()
            path = output / "prompts" / (job_id + ".txt")
            path.parent.mkdir(exist_ok=True)
            path.write_text(prompt)
            job = {"job_id": job_id, "decision_id": packet["decision_id"], "role": role,
                "provider": "codex", **plan["roles"][role], "tool_mode": "none", "read_dirs": [],
                "prompt_file": str(path), "schema_file": str(output / (role + "-schema.json"))}
            record["jobs"].append(job)
            print(json.dumps({"dispatch": job_id, "role": role, **plan["roles"][role]}), flush=True)
            status = await transport.run_job(job, output, semaphore, plan["timeout_seconds"], halted)
            if status["state"] != "completed":
                raise ValueError("Assignment ended: " + status["state"])
            report = get(output / job_id / "report.json")
            validate_schema(report, get(Path(job["schema_file"])))
            if role == "additional":
                bench.validate_report(packet, report)
            return report
        try:
            record.update(await route(case, assignment))
        except Exception as error:
            record["error"] = str(error)
        record["finished_at"] = time.time()
        put(output / "outcomes" / f"{index:05d}.json", record)
        return record
    cases = get(replay / "inputs.json")
    cases.sort(key=lambda c: bench.digest(str(c["case_index"]).encode()))
    results = await asyncio.gather(*(decision(case) for case in cases))
    put(output / "run-summary.json", {"outcomes": len(results), "failed": sum(r["status"] == "failed" for r in results)})


def score(replay, output):
    plan, bench = verify(replay)
    if get(output / "replay-reference.json")["freeze_sha256"] != bench.digest((replay / "freeze.json").read_bytes()):
        raise ValueError("Run belongs to another replay")
    source_bench = load_module("scoring_benchmark", Path(plan["source_suite"]) / "frozen/benchmark.py")
    source_bench.check_suite(Path(plan["source_suite"]), include_private=True)
    cases = {c["case_index"]: c for c in get(replay / "inputs.json")}
    records = [get(p) for p in sorted((output / "outcomes").glob("*.json"))]
    if len(records) != len(cases) or {r["case_index"] for r in records} != set(cases):
        raise ValueError("Missing or duplicated outcomes")
    for record in records:
        if record["status"] != "failed" and record["jobs"]:
            packet = cases[record["case_index"]]["packet"]
            for report in record["reports"]:
                bench.validate_report(packet, report)
            validate_judgment(packet, record["reports"], record["judgment"])
    keys = {i: get(Path(plan["source_suite"]) / "private/answers" / f"{i:05d}.json")["acceptable"] for i in cases}
    accepted = [r for r in records if r["status"] == "accepted"]
    wrong = sum(r["decision"] not in keys[r["case_index"]] for r in accepted)
    eligible = sum(v != ["ESCALATE"] for v in keys.values())
    coverage = sum(keys[r["case_index"]] != ["ESCALATE"] for r in accepted) / eligible
    costs = {"reused_luna_deliberations": {"jobs": 0, "tokens": {"input": 0, "cached_input": 0, "output": 0}, "usd": 0.0, "unknown_usage": 0},
             "new_assignments": {"jobs": 0, "tokens": {"input": 0, "cached_input": 0, "output": 0}, "usd": 0.0, "unknown_usage": 0}}
    def account(group, model, usage):
        c = costs[group]
        c["jobs"] += 1
        if usage is None:
            c["unknown_usage"] += 1
            return
        for key, value in usage.items():
            c["tokens"][key] += value
            c["usd"] += value * plan["rates"][model][key] / 1e6
    for case in cases.values():
        for job in case["borrowed_assignments"]:
            account("reused_luna_deliberations", job["model"], job["usage"])
    for record in records:
        for job in record["jobs"]:
            try:
                usage = bench.usage_for(job, output)
            except (OSError, ValueError, KeyError):
                usage = None
            account("new_assignments", job["model"], usage)
    upper = bench.error_upper_bound(wrong, len(accepted), plan["confidence_level"])
    result = {"evaluation_kind": plan["evaluation_kind"], "cases": len(cases), "accepted": len(accepted),
        "correct_accepted": len(accepted) - wrong, "wrong_accepted": wrong,
        "correct_escalations": sum(r["status"] == "escalated" and keys[r["case_index"]] == ["ESCALATE"] for r in records),
        "unnecessary_escalations": sum(r["status"] == "escalated" and keys[r["case_index"]] != ["ESCALATE"] for r in records),
        "failed": sum(r["status"] == "failed" for r in records), "eligible_cases": eligible,
        "eligible_coverage": coverage, "wrong_accepted_rate_upper_bound": upper,
        "meets_original_numeric_target": upper <= plan["max_wrong_accepted_rate"] and coverage >= plan["minimum_eligible_coverage"],
        "cost_allocations": costs,
        "known_protocol_equivalent_usd": sum(c["usd"] for c in costs.values()),
        "protocol_equivalent_usd": (sum(c["usd"] for c in costs.values())
            if all(c["unknown_usage"] == 0 for c in costs.values()) else None),
        "judge_changed_cases": [{"case_index": r["case_index"], "old_status": cases[r["case_index"]]["original_status"],
            "new_status": r["status"], "old_decision": cases[r["case_index"]]["original_decision"], "new_decision": r.get("decision")}
            for r in records if (r["status"], r.get("decision")) != (cases[r["case_index"]]["original_status"], cases[r["case_index"]]["original_decision"])],
        "limits": plan["limits"] + ["USD values are conditional API equivalents, not account charges.",
            "Binomial bounds describe this small reused synthetic sample, not production reliability or untouched confirmation."]}
    put(output / "scores.json", result)
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--suite", type=Path, required=True)
    p.add_argument("--original", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--judge-provider", choices=("codex", "native_collaboration"), default="codex")
    for name in ("verify", "run", "score"):
        p = sub.add_parser(name)
        p.add_argument("--replay", type=Path, required=True)
        if name != "verify":
            p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.suite.resolve(), args.original.resolve(), args.output.resolve(), args.judge_provider)
    elif args.command == "verify":
        plan, _ = verify(args.replay.resolve())
        print(json.dumps({"verified_cases": plan["case_count"]}))
    elif args.command == "run":
        asyncio.run(run(args.replay.resolve(), args.output.resolve()))
    else:
        score(args.replay.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
