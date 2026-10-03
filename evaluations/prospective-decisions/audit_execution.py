#!/usr/bin/env python3
"""Audit a completed run without changing its frozen references or scores."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text())


def reference_by_ticks(packet):
    """Independent discrete-time check, rather than the oracle's event sweep."""
    values = {fact["id"]: fact["value"] for fact in packet["evidence"]}
    if values["user_gate"]["required"]:
        return {"ESCALATE"}
    candidates = [v for k, v in values.items() if k.startswith("plan-")]
    intersection = {p["id"] for p in candidates}
    for capacity in values["capacity"]:
        scores = {}
        for plan in candidates:
            steps = plan["steps"]
            if sorted(s["operation"] for s in steps) != packet["required_operations"]:
                continue
            starts, ends, valid = {}, {}, True
            for step in steps:
                operation = values[step["operation"]]
                if (type(step["start"]) is not int or step["start"] < 0
                        or type(step["attempts"]) is not int or step["attempts"] < 1
                        or (step["attempts"] > 1 and not operation["idempotent"])):
                    valid = False
                    break
                starts[operation["id"]] = step["start"]
                ends[operation["id"]] = step["start"] + operation["duration"] * step["attempts"]
            if not valid:
                continue
            final = max(ends.values())
            if final > values["deadline"]:
                continue
            if any(ends[parent] > starts[identifier] for identifier in packet["required_operations"]
                   for parent in values[identifier]["prerequisites"]):
                continue
            occupancy = [sum(values[identifier]["slots"] for identifier in starts
                             if starts[identifier] <= tick < ends[identifier])
                         for tick in range(final)]
            if any(count > capacity for count in occupancy):
                continue
            scores[plan["id"]] = (plan["maintenance"] * values["weights"]["maintenance"]
                                  + final * values["weights"]["latency"])
        best = min(scores.values()) if scores else None
        intersection &= {identifier for identifier, score in scores.items() if score == best}
    return intersection or {"ESCALATE"}


def audit(suite, output):
    plan = load(suite / "frozen/plan.json")
    version = load(suite / "freeze.json")["version"]
    run = load(output / "run-summary.json")
    job_arms = {job["job_id"]: outcome["arm"]
                for path in (output / "outcomes").glob("*.json")
                for outcome in [load(path)] for job in outcome["jobs"]}
    states, items, models, roles = Counter(), Counter(), Counter(), Counter()
    events, threads, header_models = [], [], Counter()
    prompt_mismatches, missing_threads = [], []
    per_arm = {}
    for path in sorted(output.glob("c*/status.json")):
        status = load(path)
        states[status["state"]] += 1
        models[(status["model"], status["effort"])] += 1
        roles[status["role"]] += 1
        events.extend([(status["started_at"], 1), (status["finished_at"], -1)])
        arm = job_arms[status["job_id"]]
        entry = per_arm.setdefault(arm, {"assignments": 0, "sum_assignment_seconds": 0,
                                        "first_start": status["started_at"], "last_finish": 0})
        entry["assignments"] += 1
        entry["sum_assignment_seconds"] += status["finished_at"] - status["started_at"]
        entry["first_start"] = min(entry["first_start"], status["started_at"])
        entry["last_finish"] = max(entry["last_finish"], status["finished_at"])
        prompt = output / "prompts" / (status["job_id"] + ".txt")
        if hashlib.sha256(prompt.read_bytes()).hexdigest() != status["prompt_sha256"]:
            prompt_mismatches.append(status["job_id"])
        if status.get("thread_id"):
            threads.append(status["thread_id"])
        elif status["state"] == "completed" and status["provider"] == "codex":
            missing_threads.append(status["job_id"])
        for line in (path.parent / "stdout.log").read_text().splitlines():
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if event.get("type") == "item.completed" and isinstance(event.get("item"), dict):
                items[event["item"].get("type", "unknown")] += 1
        for line in (path.parent / "stderr.log").read_text().splitlines():
            if line.startswith("model: "):
                header_models[line.removeprefix("model: ")] += 1
    live, peak = 0, 0
    for _, change in sorted(events):
        live += change
        peak = max(peak, live)
    reference_mismatches = []
    for index in range(plan["case_count"]):
        packet = load(suite / "packets" / f"{index:05d}.json")
        expected = set(load(suite / "private/answers" / f"{index:05d}.json")["acceptable"])
        if reference_by_ticks(packet) != expected:
            reference_mismatches.append(index)
    result = {"outcomes": run["outcomes"], "states": dict(states), "role_counts": dict(roles),
              "requested_configurations": [{"model": m, "effort": e, "jobs": n} for (m, e), n in models.items()],
              "cli_header_models": dict(header_models), "peak_live_jobs": peak,
              "concurrency_cap_respected": peak <= plan["max_concurrency"],
              "unique_thread_ids": len(set(threads)), "thread_ids_seen": len(threads),
              "missing_thread_ids_for_completed_jobs": missing_threads,
              "completed_item_types": dict(items),
              "research_or_tool_items": sum(n for kind, n in items.items() if kind not in {"agent_message", "reasoning"}),
              "prompt_hash_mismatches": prompt_mismatches,
              "independent_tick_reference_checked_cases": plan["case_count"],
              "independent_reference_mismatches": reference_mismatches,
              "wall_seconds_first_job_to_last_job": (max(t for t, _ in events) - min(t for t, _ in events)) if events else 0,
              "assignment_time_by_arm": per_arm,
              "limits": (["The frozen v1 scheduler queued individual assignments ahead of initial ensemble pairs; elapsed decision time includes this queue effect."]
                         if version == "prospective-decisions-v1" else []) + [
                         "Assignment and decision times include resource contention under the shared concurrency cap.",
                         "The independent reference audit checks the specified finite model; it does not validate production realism.",
                         "Requested models and CLI headers do not identify immutable hosted weights."]}
    (output / "execution-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit(args.suite.resolve(), args.output.resolve())
