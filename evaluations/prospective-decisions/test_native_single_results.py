"""Offline collection must preserve failed native output without retry or repair."""

import contextlib
import io
import json
import types
import unittest
from unittest.mock import patch

import benchmark
import native_single_results
from test_native_single import NativeSingleTests


class NativeResultsTests(unittest.TestCase):
    def setUp(self):
        self.fixture = NativeSingleTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.output = self.fixture.output
        packet = benchmark.get(self.fixture.suite / "packets/00001.json")
        choice = benchmark.get(self.fixture.suite / "private/answers/00001.json")["acceptable"][0]
        report = {"decision_id": packet["decision_id"], "decision": choice, "scope": "as_specified",
            "conditions": [], "rationale": "Fixture decision", "claims": [], "options": [
                {"id": e["id"], "advantages": "Fixture", "disadvantages": "Fixture"}
                for e in packet["evidence"] if e["id"].startswith("plan-")]}
        self.report = report
        events = []
        for index, raw in ((1, json.dumps(report)), (2, '{"decision": "x" "scope": "as_specified"}')):
            name = f"/root/sol_single_{index:02d}"
            events.extend([
                {"payload": {"type": "item_completed", "item": {"agent_path": name,
                    "agent_thread_id": f"test-thread-{index}"}}},
                {"payload": {"type": "agent_message", "author": name, "content": [{"text":
                    "Message Type: FINAL_ANSWER\nPayload:\n" + raw}]}}
            ])
        self.events = events
        self.rollout = self.fixture.root / "root.jsonl"
        self.rollout.write_text("\n".join(json.dumps(e) for e in events) + "\n")

    def test_invalid_json_is_a_failure_with_usage_still_required(self):
        with contextlib.redirect_stdout(io.StringIO()):
            native_single_results.collect(self.output, self.rollout)
            native_single_results.score(self.output)
        outcome = benchmark.get(self.output / "outcomes/00002.json")
        self.assertEqual(outcome["status"], "failed")
        self.assertIsNone(outcome["decision"])
        self.assertEqual(outcome["failure"]["kind"], "invalid_json")
        self.assertEqual((self.output / "c00002-r0-sol-single/raw-report.txt").read_text(),
                         '{"decision": "x" "scope": "as_specified"}')
        score = benchmark.get(self.output / "scores.json")
        self.assertEqual(score["failed_case_indices"], [2])
        self.assertEqual(score["model_calls"], 2)
        self.assertEqual(score["unknown_usage"], 2)
        self.assertIsNone(score["api_equivalent_usd"])

    def test_duplicate_answers_are_rejected(self):
        with self.rollout.open("a") as stream:
            stream.write(json.dumps(self.events[-1]) + "\n")
        with self.assertRaisesRegex(ValueError, "More than one"):
            native_single_results.collect(self.output, self.rollout)

    def test_full_frozen_schema_is_enforced_with_a_legacy_partial_validator(self):
        plan, _ = native_single_results.original.module(self.output / "frozen/native_single.py").verify(self.output)
        legacy = types.SimpleNamespace(validate_report=lambda packet, report: None)
        frozen = types.SimpleNamespace(verify=lambda output: (plan, legacy))
        self.report.pop("rationale")
        self.events[1]["payload"]["content"][0]["text"] = "Message Type: FINAL_ANSWER\nPayload:\n" + json.dumps(self.report)
        self.rollout.write_text("\n".join(json.dumps(e) for e in self.events) + "\n")
        with patch.object(native_single_results.original, "module", return_value=frozen), \
                contextlib.redirect_stdout(io.StringIO()):
            native_single_results.collect(self.output, self.rollout)
        outcome = benchmark.get(self.output / "outcomes/00001.json")
        self.assertEqual(outcome["status"], "failed")
        self.assertEqual(outcome["failure"]["kind"], "invalid_report")
        self.assertIsNone(outcome["decision"])

    def test_scoring_rejects_native_reports_with_extra_properties(self):
        with contextlib.redirect_stdout(io.StringIO()):
            native_single_results.collect(self.output, self.rollout)
        outcome_path = self.output / "outcomes/00001.json"
        outcome = benchmark.get(outcome_path)
        outcome["reports"][0]["extra"] = "forbidden"
        benchmark.put(outcome_path, outcome)
        with self.assertRaisesRegex(ValueError, "Unexpected report fields"):
            native_single_results.score(self.output)


if __name__ == "__main__":
    unittest.main()
