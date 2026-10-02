"""Standalone replay integrity and accounting checks; no model calls."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

import benchmark
import native_single


class NativeSingleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        plan = benchmark.get(Path(__file__).with_name("plan.example.json"))
        plan["case_count"] = 3
        benchmark.put(self.root / "plan.json", plan)
        self.suite, self.original, self.output = [self.root / n for n in ("suite", "original", "solo")]
        with contextlib.redirect_stdout(io.StringIO()):
            benchmark.prepare(self.root / "plan.json", self.suite)
        benchmark.put(self.original / "suite-reference.json", {"manifest_sha256": native_single.sha(self.suite / "manifest.json")})
        for i in range(3):
            packet = benchmark.get(self.suite / "packets" / f"{i:05d}.json")
            jobs = []
            if not benchmark.facts(packet)["user_gate"]["required"]:
                identifier = f"original-{i}"
                path = self.original / "prompts" / (identifier + ".txt")
                path.parent.mkdir(exist_ok=True)
                path.write_text(benchmark.DECIDER + "\n" + benchmark.encoded({"packet": packet}).decode())
                jobs.append({"job_id": identifier, "prompt_file": str(path)})
                benchmark.put(self.original / identifier / "status.json", {"prompt_sha256": native_single.sha(path)})
            benchmark.put(self.original / "outcomes" / f"c{i:05d}-r0-luna-single.json", {"jobs": jobs})
        with contextlib.redirect_stdout(io.StringIO()):
            native_single.prepare(self.suite, self.original, self.output)

    def test_exact_original_prompts_and_tamper_rejection(self):
        self.assertEqual((self.output / "prompts/00001.txt").read_bytes(),
                         (self.original / "prompts/original-1.txt").read_bytes())
        native_single.verify(self.output)
        (self.output / "prompts/00001.txt").write_text("changed after freeze")
        with self.assertRaisesRegex(ValueError, "artifact changed"):
            native_single.verify(self.output)

    def test_missing_outcomes_prevent_partial_scoring(self):
        with self.assertRaisesRegex(ValueError, "Missing"):
            native_single.score(self.output)

    def test_missing_usage_is_not_a_complete_monetary_total(self):
        for i in (1, 2):
            choice = benchmark.get(self.suite / "private/answers" / f"{i:05d}.json")["acceptable"][0]
            job = {"job_id": f"native-{i}", "provider": "native_collaboration"}
            benchmark.put(self.output / job["job_id"] / "stdout.log", {"usage": None})
            benchmark.put(self.output / "outcomes" / f"{i:05d}.json", {"case_index": i,
                "status": "escalated" if choice == "ESCALATE" else "accepted", "decision": choice, "jobs": [job]})
        with contextlib.redirect_stdout(io.StringIO()):
            native_single.score(self.output)
        scored = benchmark.get(self.output / "scores.json")
        self.assertEqual(scored["wrong_accepted"], 0)
        self.assertEqual(scored["unknown_usage"], 2)
        self.assertIsNone(scored["api_equivalent_usd"])
        self.assertFalse(scored["meets_original_numeric_target"])


if __name__ == "__main__":
    unittest.main()
