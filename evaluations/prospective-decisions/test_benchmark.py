"""Reference, contamination-boundary, and routing regressions; no model calls."""

import asyncio
import contextlib
import io
import json
import math
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

import benchmark as b


class ReferenceTests(unittest.TestCase):
    def test_hand_checked_schedule_and_uncertain_optimum(self):
        packet = {"required_operations": ["op-a", "op-b"], "evidence": [
            {"id": "capacity", "value": [1, 2]}, {"id": "deadline", "value": 5},
            {"id": "weights", "value": {"maintenance": 1, "latency": 1}},
            {"id": "user_gate", "value": {"required": False}},
            {"id": "op-a", "value": {"id": "op-a", "duration": 2, "slots": 1, "idempotent": False, "prerequisites": []}},
            {"id": "op-b", "value": {"id": "op-b", "duration": 2, "slots": 1, "idempotent": True, "prerequisites": []}},
            {"id": "plan-serial", "value": {"id": "plan-serial", "maintenance": 0, "steps": [
                {"operation": "op-a", "start": 0, "attempts": 1}, {"operation": "op-b", "start": 2, "attempts": 1}]}},
            {"id": "plan-parallel", "value": {"id": "plan-parallel", "maintenance": 0, "steps": [
                {"operation": "op-a", "start": 0, "attempts": 1}, {"operation": "op-b", "start": 0, "attempts": 1}]}}]}
        self.assertEqual(b.oracle(packet)["acceptable"], ["ESCALATE"])
        packet["evidence"][0]["value"] = [1]
        self.assertEqual(b.oracle(packet)["acceptable"], ["plan-serial"])
        packet["evidence"][0]["value"] = [2]
        self.assertEqual(b.oracle(packet)["acceptable"], ["plan-parallel"])
        serial = b.facts(packet)["plan-serial"]
        serial["steps"][0]["attempts"] = 2
        self.assertIsNone(b.evaluate_option(packet, serial, 2))

    def test_random_generation_and_order_invariance(self):
        reasons, optimum_indices = set(), set()
        for i in range(180):
            packet = b.generate_case("development-seed-only", i)
            self.assertEqual(packet, b.generate_case("development-seed-only", i))
            self.assertNotEqual(packet, b.generate_case("different-development-seed", i))
            original = b.oracle(packet)
            reasons.add(original["reason"])
            # Event-order independence includes shuffled operations and evidence entries.
            packet["evidence"].reverse()
            self.assertEqual(original, b.oracle(packet))
            if original["acceptable"] != ["ESCALATE"]:
                source = b.facts(packet)
                for identifier in original["acceptable"]:
                    self.assertTrue(all(b.evaluate_option(packet, source[identifier], world) is not None
                                        for world in source["capacity"]))
                    optimum_indices.add(source[identifier]["maintenance"])
        self.assertEqual(reasons, {"explicit_user_gate", "robust_optimum", "no_common_optimum"})
        self.assertGreater(len(optimum_indices), 5)

    def test_literal_check_cannot_solve_the_decision(self):
        packet = b.generate_case("development", 1)
        source = b.facts(packet)
        reports = [{"claims": [{"fact_id": "capacity", "value_json": json.dumps(source["capacity"])},
                                {"fact_id": "required_operations", "value_json": json.dumps(packet["required_operations"])},
                                {"fact_id": "new-provider-guarantee", "value_json": "true"}]}]
        with patch.object(b, "oracle", side_effect=AssertionError("Oracle must remain private")), \
             patch.object(b, "evaluate_option", side_effect=AssertionError("No plan solving")):
            checks = b.source_checks(packet, reports)
        self.assertEqual([f["status"] for f in checks["findings"]], ["confirmed", "confirmed", "unsupported"])

    def test_confidence_does_not_count_small_pilots_as_proof(self):
        self.assertGreater(b.error_upper_bound(0, 24, .95), .01)
        self.assertGreater(b.error_upper_bound(0, 298, .95), .01)
        self.assertLess(b.error_upper_bound(0, 299, .95), .01)
        self.assertAlmostEqual(b.error_upper_bound(1, 2, .95), math.sqrt(.95), places=10)
        self.assertEqual(b.error_upper_bound(0, 0, .95), 1)


class StudyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        plan = b.get(Path(__file__).with_name("plan.example.json"))
        plan["case_count"] = 7
        self.plan = plan
        self.started_jobs = []
        self.plan_path = self.root / "plan.json"
        b.put(self.plan_path, plan)
        self.suite = self.root / "suite"
        with contextlib.redirect_stdout(io.StringIO()):
            b.prepare(self.plan_path, self.suite)

    def test_frozen_regeneration_and_tamper_rejection(self):
        self.assertEqual(b.check_suite(self.suite, include_private=True), self.plan)
        packet = self.suite / "packets/00001.json"
        packet.write_text(packet.read_text() + " ")
        with self.assertRaisesRegex(ValueError, "Packet changed"):
            b.check_suite(self.suite)

    def test_model_phase_does_not_read_private_material(self):
        real_get = b.get
        def guarded_get(path):
            self.assertNotIn("private", Path(path).parts)
            return real_get(path)
        with patch.object(b, "get", side_effect=guarded_get):
            b.check_suite(self.suite)

    def fake_transport(self, repeated_reconsider=False):
        async def run_job(job, root, semaphore, timeout, halted):
            async with semaphore:
                self.started_jobs.append(job)
                folder = root / job["job_id"]
                folder.mkdir()
                text = Path(job["prompt_file"]).read_text()
                payload = json.loads(text[text.index("\n{\n") + 1:])
                if job["role"] == "judge":
                    report = {"outcome": "reconsider" if repeated_reconsider else "accept",
                              "candidate": payload["candidate"], "preferred_choice": payload["candidate"],
                              "rationale": "Development transport fixture.", "remaining_gap": "One bounded reassessment."}
                else:
                    packet = payload["packet"]
                    source = b.facts(packet)
                    choice = b.oracle(packet)["acceptable"][0]
                    if job["role"] == "initial_b" and not repeated_reconsider:
                        choice = next(e["id"] for e in packet["evidence"] if e["id"].startswith("plan-") and e["id"] != choice)
                    report = {"decision_id": packet["decision_id"], "decision": choice,
                              "scope": "as_specified", "conditions": [], "rationale": "Fixture only.",
                              "options": [{"id": e["id"], "advantages": "Fixture", "disadvantages": "Fixture"}
                                          for e in packet["evidence"] if e["id"].startswith("plan-")],
                              "claims": [{"fact_id": "capacity", "value_json": json.dumps(source["capacity"])}]}
                b.put(folder / "report.json", report)
                b.put(folder / "status.json", {"state": "completed"})
                (folder / "stdout.log").write_text(json.dumps({"type": "turn.completed", "usage": {
                    "input_tokens": 100, "cached_input_tokens": 20, "output_tokens": 10}}) + "\n")
                return {"state": "completed"}
        return types.SimpleNamespace(run_job=run_job)

    def run_fake(self, repeated_reconsider=False):
        output = self.root / ("reconsider-run" if repeated_reconsider else "run")
        with patch.object(b, "load_dispatch", return_value=self.fake_transport(repeated_reconsider)), \
             patch.object(b.subprocess, "check_output", return_value="fake-cli-test-version"), \
             contextlib.redirect_stdout(io.StringIO()):
            asyncio.run(b.run_suite(self.suite, output))
            b.score_suite(self.suite, output)
        return output

    def test_bounded_disagreement_routing_and_scoring(self):
        output = self.run_fake()
        summaries = b.get(output / "scores.json")["summaries"]
        self.assertTrue(all(s["wrong_accepted"] == 0 and s["failed"] == 0 for s in summaries))
        self.assertTrue(all(not s["meets_preregistered_target_under_binomial_assumptions"] for s in summaries))
        for path in (output / "outcomes").glob("*.json"):
            record = b.get(path)
            self.assertLessEqual(sum(j["role"] == "additional" for j in record["jobs"]), 1)
            self.assertTrue(all(j["tool_mode"] == "none" and not j["read_dirs"] for j in record["jobs"]))
            if record["arm"] == "luna-ensemble" and record["jobs"]:
                self.assertEqual(sum(j["role"] == "additional" for j in record["jobs"]), 1)

    def test_repeated_reconsideration_escalates_without_new_budget(self):
        output = self.run_fake(repeated_reconsider=True)
        for path in (output / "outcomes").glob("*.json"):
            record = b.get(path)
            if record["arm"] == "luna-ensemble" and record["jobs"]:
                self.assertEqual(record["status"], "escalated")
                self.assertEqual(len(record["jobs"]), 5)
                self.assertEqual(sum(j["role"] == "additional" for j in record["jobs"]), 1)

    def test_missing_outcome_prevents_cherry_picked_score(self):
        output = self.run_fake()
        next((output / "outcomes").glob("*.json")).unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            b.score_suite(self.suite, output)

    def test_initial_arm_order_follows_frozen_interleaving(self):
        self.run_fake()
        actual = [j['job_id'] for j in self.started_jobs if j['role'] in {'initial_a', 'initial_b'}]
        work = [(i, 0, a) for i in range(self.plan['case_count']) for a in self.plan['arms']]
        work.sort(key=lambda x: b.digest(f"{x[0]}:{x[1]}:{x[2]['id']}".encode()))
        expected = []
        for i, r, arm in work:
            if b.facts(b.get(self.suite/'packets'/f'{i:05d}.json'))['user_gate']['required']:
                continue
            for serial in range(1 if arm['protocol']=='single' else 2):
                expected.append(f"c{i:05d}-r{r}-{arm['id']}-decider-{serial}")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
