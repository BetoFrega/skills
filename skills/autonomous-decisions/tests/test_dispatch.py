"""Exercise the CLI transport with local fake providers and no model calls."""

import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest


RUNNER = Path(__file__).resolve().parents[1] / "scripts" / "dispatch.py"
FAKE_CLI = r'''#!/usr/bin/env python3
import json, os, subprocess, sys, time
from pathlib import Path
args = sys.argv[1:]
data = json.loads(sys.stdin.read().splitlines()[-1])
trace = Path(os.environ['DECISION_TEST_TRACE'])
def event(kind, **extra):
    with trace.open('a') as output:
        output.write(json.dumps({'kind':kind, 'job':data['identity'],
                                 'cwd':os.getcwd(), 'args':args, **extra}) + '\n')
event('start')
behavior = data.get('behavior')
if behavior in ('slow', 'orphan_pipes', 'orphan_closed'):
    options = {} if behavior != 'orphan_closed' else {
        'stdin':subprocess.DEVNULL, 'stdout':subprocess.DEVNULL,
        'stderr':subprocess.DEVNULL}
    heartbeat = Path.cwd() / 'child-heartbeat.txt'
    child_code = ('import time\nfrom pathlib import Path\ncount=0\nwhile True:\n'
                  '    count += 1\n    Path(' + repr(str(heartbeat)) + ').write_text(str(count))\n'
                  '    time.sleep(0.02)\n')
    child = subprocess.Popen([sys.executable, '-c', child_code], **options)
    deadline = time.monotonic() + 2
    while not heartbeat.exists():
        if time.monotonic() > deadline: raise RuntimeError('Child did not start')
        time.sleep(0.005)
    event('child', pid=child.pid, heartbeat=str(heartbeat))
    if behavior == 'slow': time.sleep(20)
time.sleep(0.025)
if behavior == 'fail':
    event('end')
    sys.exit(7)
report = {'identity':data['identity']}
if 'exec' in args:
    Path(args[args.index('--output-last-message')+1]).write_text(json.dumps(report))
    print(json.dumps({'type':'thread.started', 'thread_id':data['identity']}))
else:
    print(json.dumps({'is_error':False, 'structured_output':report,
                      'modelUsage':{'fixture-model':{}}}))
event('end')
'''


@unittest.skipUnless(os.name == "posix", "Runner requires POSIX process groups")
class DispatchTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="decision-dispatch-tests-")
        self.root = Path(self.temporary.name)
        binary = self.root / "bin"
        binary.mkdir()
        for provider in ("codex", "claude"):
            executable = binary / provider
            executable.write_text(FAKE_CLI)
            executable.chmod(0o755)
        self.trace = self.root / "trace.jsonl"
        self.environment = dict(os.environ, DECISION_TEST_TRACE=str(self.trace))
        self.environment["PATH"] = str(binary) + os.pathsep + os.environ["PATH"]
        self.schema = self.root / "schema.json"
        self.schema.write_text(json.dumps({"type":"object", "properties":{
            "identity":{"type":"string"}}, "required":["identity"], "additionalProperties":False}))

    def tearDown(self):
        # Also reap fixtures if an assertion or the runner itself fails.
        for status_file in self.root.glob("*/*/status.json"):
            pid = json.loads(status_file.read_text()).get("pid")
            if pid:
                try:
                    os.killpg(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        self.temporary.cleanup()

    def job(self, number, provider="codex", **data):
        identifier = f"job-{number}"
        prompt = self.root / f"{identifier}.txt"
        prompt.write_text(json.dumps({"identity":identifier, **data}))
        return {"job_id":identifier, "decision_id":f"decision-{number}",
                "role":"judge", "provider":provider, "model":"fixture-model", "effort":"low",
                "prompt_file":str(prompt), "schema_file":str(self.schema), "tool_mode":"none"}

    def run_wave(self, name, jobs, cap=4, timeout=5):
        manifest = self.root / f"{name}.json"
        manifest.write_text(json.dumps(jobs))
        output = self.root / name
        command = [sys.executable, str(RUNNER), str(manifest), "--output-dir", str(output),
                   "--max-concurrency", str(cap), "--timeout-seconds", str(timeout)]
        result = subprocess.run(command, env=self.environment, capture_output=True,
                                text=True, timeout=15)
        return result, output, command

    def states(self, output):
        return {item["job_id"]:item["state"]
                for item in json.loads((output / "summary.json").read_text())}

    def test_mixed_wave_respects_cap_and_preserves_assignments(self):
        jobs = [self.job(n, "codex" if n % 2 else "claude") for n in range(35)]
        result, output, command = self.run_wave("mixed", jobs)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(self.states(output)), 35)
        for job in jobs:
            report = json.loads((output / job["job_id"] / "report.json").read_text())
            self.assertEqual(report["identity"], job["job_id"])
        active = maximum = 0
        for event in map(json.loads, self.trace.read_text().splitlines()):
            active += 1 if event["kind"] == "start" else -1
            maximum = max(maximum, active)
            if event["kind"] != "start":
                continue
            self.assertEqual(Path(event["cwd"]).name, event["job"])
            args = event["args"]
            if "exec" in args:
                self.assertEqual(args[args.index("--sandbox") + 1], "read-only")
                self.assertIn("features.shell_tool=false", args)
                self.assertIn("features.apps=false", args)
            else:
                self.assertEqual(args[args.index("--tools") + 1], "")
                self.assertIn("--restricted", args)
                self.assertIn("--strict-mcp-config", args)
        self.assertGreater(maximum, 1)
        self.assertLessEqual(maximum, 4)
        replay = subprocess.run(command, env=self.environment, capture_output=True, timeout=5)
        self.assertNotEqual(replay.returncode, 0)

    def test_failure_preserves_other_jobs(self):
        result, output, _ = self.run_wave("failure", [
            self.job(1, behavior="fail"), self.job(2, "claude")])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.states(output), {"job-1":"failed", "job-2":"completed"})

    def test_timeout_and_exited_leaders_clean_up_descendants(self):
        for behavior, expected in (("slow", "timed_out"), ("orphan_pipes", "timed_out"),
                                   ("orphan_closed", "completed")):
            with self.subTest(behavior=behavior):
                start = time.monotonic()
                result, output, _ = self.run_wave(behavior, [
                    self.job(1, behavior=behavior), self.job(2, "claude")], cap=1, timeout=0.4)
                self.assertLess(time.monotonic() - start, 4)
                self.assertEqual(self.states(output), {"job-1":expected, "job-2":"completed"})
                self.assertEqual(result.returncode, 0 if expected == "completed" else 1)
                events = [json.loads(line) for line in self.trace.read_text().splitlines()]
                heartbeat = Path([event["heartbeat"] for event in events
                                  if event["kind"] == "child"][-1])
                observation = heartbeat.read_text()
                time.sleep(0.1)
                self.assertEqual(heartbeat.read_text(), observation, "Descendant remains active")

    def test_invalid_judge_rejected_before_dispatch(self):
        job = self.job(1)
        job["tool_mode"] = "files"
        result, output, _ = self.run_wave("invalid", [job])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())
        self.assertFalse(self.trace.exists())


if __name__ == "__main__":
    unittest.main()
