"""Protocol regressions for replay routing; no live model calls."""

import unittest
import asyncio
import contextlib
import io
import json
from pathlib import Path
from unittest.mock import patch

import benchmark
import judge_swap
import test_benchmark as fixtures


class ReplayRoutingTests(unittest.IsolatedAsyncioTestCase):
    def case(self, count=2):
        return {"initial_judge_prompt": "frozen original input", "packet": {
            "evidence": [{"id": "plan-a"}, {"id": "plan-b"}]},
            "reports": [{"decision": "plan-a"} for _ in range(count)]}

    def judgment(self, outcome, preferred="plan-a"):
        return {"outcome": outcome, "candidate": "plan-a", "preferred_choice": preferred,
                "remaining_gap": "Check the second capacity world.", "rationale": "Fixture"}

    async def test_reconsideration_uses_one_additional_then_escalates(self):
        calls = []
        async def assignment(role, reports, **kwargs):
            calls.append((role, len(reports)))
            return {"decision": "plan-a"} if role == "additional" else self.judgment("reconsider")
        result = await judge_swap.route(self.case(), assignment)
        self.assertEqual(calls, [("judge", 2), ("additional", 2), ("judge", 3)])
        self.assertEqual((result["status"], result["decision"]), ("escalated", "ESCALATE"))

    async def test_used_additional_slot_cannot_be_replenished(self):
        calls = []
        async def assignment(role, reports, **kwargs):
            calls.append(role)
            return self.judgment("reconsider")
        result = await judge_swap.route(self.case(3), assignment)
        self.assertEqual(calls, ["judge"])
        self.assertEqual(result["status"], "escalated")

    async def test_majority_challenge_escalates_and_changed_acceptance_is_rejected(self):
        async def assignment(role, reports, **kwargs):
            return self.judgment("challenge_majority", "plan-b")
        result = await judge_swap.route(self.case(3), assignment)
        self.assertEqual(result["status"], "escalated")
        with self.assertRaises(ValueError):
            judge_swap.validate_judgment(self.case()["packet"], self.case()["reports"],
                                         self.judgment("accept", "plan-b"))

    async def test_explicit_gate_assigns_no_model(self):
        async def assignment(*args, **kwargs):
            self.fail("Explicit human gate must not call a worker")
        case = self.case()
        case["initial_judge_prompt"] = None
        result = await judge_swap.route(case, assignment)
        self.assertEqual(result["route"], "explicit_user_gate")

    def test_partial_native_judgment_is_rejected(self):
        judgment = self.judgment("accept")
        judgment.pop("rationale")
        with self.assertRaisesRegex(ValueError, "Missing required"):
            judge_swap.validate_judgment(self.case()["packet"], self.case()["reports"], judgment)


class ReplayDispatchTests(unittest.TestCase):
    def test_frozen_replay_reconsideration_is_blind_and_schema_checked(self):
        fixture = fixtures.StudyTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        original = fixture.root / "original"
        transport = fixture.fake_transport(repeated_reconsider=True)
        run_job = transport.run_job
        async def accepting_initial_pair(job, *args):
            result = await run_job(job, *args)
            if job["role"] == "judge":
                path = original / job["job_id"] / "report.json"
                report = benchmark.get(path)
                report["outcome"] = "accept"
                benchmark.put(path, report)
            return result
        transport.run_job = accepting_initial_pair
        with patch.object(benchmark, "load_dispatch", return_value=transport), \
                patch.object(benchmark.subprocess, "check_output", return_value="offline-test-version"), \
                contextlib.redirect_stdout(io.StringIO()):
            asyncio.run(benchmark.run_suite(fixture.suite, original))
        for path in (original / "outcomes").glob("*.json"):
            for job in benchmark.get(path)["jobs"]:
                benchmark.put(original / job["job_id"] / "status.json", {"state": "completed",
                    "prompt_sha256": benchmark.digest(Path(job["prompt_file"]).read_bytes())})
        replay, output = fixture.root / "replay", fixture.root / "replayed"
        with contextlib.redirect_stdout(io.StringIO()):
            judge_swap.prepare(fixture.suite, original, replay)
        self.assertTrue((replay / "frozen/report_validation.py").is_file())
        loader = judge_swap.load_module
        transport = fixture.fake_transport(repeated_reconsider=True)
        with patch.object(judge_swap, "load_module", side_effect=lambda name, path:
                          transport if name == "replay_dispatch" else loader(name, path)), \
                patch.object(judge_swap.subprocess, "check_output", return_value="offline-test-version"), \
                contextlib.redirect_stdout(io.StringIO()):
            asyncio.run(judge_swap.run(replay, output))
            judge_swap.score(replay, output)
        additional = [p for p in (output / "prompts").glob("*additional*.txt")]
        self.assertTrue(additional)
        for path in additional:
            text = path.read_text()
            payload = json.loads(text[text.index("\n{\n") + 1:])
            self.assertNotIn("reports", payload)
            self.assertNotIn("gap", payload)
            self.assertTrue(payload["points_in_dispute"])
        self.assertEqual(benchmark.get(output / "scores.json")["failed"], 0)
        with (replay / "frozen/report_validation.py").open("a") as stream:
            stream.write("\n# changed after freeze\n")
        with self.assertRaisesRegex(ValueError, "Changed replay artifact"):
            judge_swap.verify(replay)


if __name__ == "__main__":
    unittest.main()
