"""A gate-only run must remain auditable without any dispatched assignments."""

import asyncio
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import audit_execution
import benchmark


class ExecutionAuditTests(unittest.TestCase):
    def test_one_case_user_gate_has_zero_job_wall_duration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plan = benchmark.get(Path(__file__).with_name("plan.example.json"))
            plan["case_count"] = 1
            benchmark.put(root / "plan.json", plan)
            suite, output = root / "suite", root / "run"
            with contextlib.redirect_stdout(io.StringIO()), \
                    patch.object(benchmark.subprocess, "check_output", return_value="offline-test-version"):
                benchmark.prepare(root / "plan.json", suite)
                asyncio.run(benchmark.run_suite(suite, output))
                audit_execution.audit(suite, output)
            result = benchmark.get(output / "execution-audit.json")
            self.assertEqual(result["outcomes"], len(plan["arms"]))
            self.assertEqual(result["wall_seconds_first_job_to_last_job"], 0)
            self.assertEqual(result["peak_live_jobs"], 0)
            self.assertEqual(result["assignment_time_by_arm"], {})
            self.assertTrue(result["concurrency_cap_respected"])


if __name__ == "__main__":
    unittest.main()
