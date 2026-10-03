#!/usr/bin/env python3
"""Run a bounded wave of explicitly configured, read-only CLI assignments."""

import argparse
import asyncio
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import time


ROLES = {"initial_a", "initial_b", "additional", "judge", "verifier"}
CLEANUP_TIMEOUT = 5


def load_jobs(path):
    jobs = json.loads(path.read_text())
    if not isinstance(jobs, list) or not jobs:
        raise ValueError("Manifest must be a nonempty JSON array")
    identifiers = set()
    for job in jobs:
        if not isinstance(job, dict):
            raise ValueError("Each job must be an object")
        for key in ("job_id", "decision_id", "role", "provider", "model", "effort"):
            if not isinstance(job.get(key), str) or not job[key].strip():
                raise ValueError(f"Missing or invalid {key}")
        identifier = job["job_id"]
        if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,95}", identifier):
            raise ValueError(f"Invalid job_id: {identifier}")
        if identifier in identifiers:
            raise ValueError(f"Duplicate job_id: {identifier}")
        identifiers.add(identifier)
        if job["role"] not in ROLES or job["provider"] not in {"codex", "claude"}:
            raise ValueError(f"Unsupported role or provider: {identifier}")
        if job.get("tool_mode") not in {"none", "files"}:
            raise ValueError(f"tool_mode must be none or files: {identifier}")
        if job["role"] == "judge" and job["tool_mode"] != "none":
            raise ValueError(f"Judges require tool_mode none: {identifier}")
        for key in ("prompt_file", "schema_file"):
            source = Path(job.get(key, ""))
            if not source.is_absolute() or not source.is_file():
                raise ValueError(f"{key} must name an existing absolute file")
        schema = json.loads(Path(job["schema_file"]).read_text())
        if not isinstance(schema, dict):
            raise ValueError(f"Schema must be a JSON object: {identifier}")
        directories = job.get("read_dirs", [])
        if not isinstance(directories, list):
            raise ValueError("read_dirs must be an array")
        for directory in directories:
            if not isinstance(directory, str) or not Path(directory).is_absolute() or not Path(directory).is_dir():
                raise ValueError("read_dirs must contain existing absolute directories")
        if job["tool_mode"] == "none" and directories:
            raise ValueError(f"A tool-free job cannot request read directories: {identifier}")
        if not shutil.which(job["provider"]):
            raise ValueError(f"CLI unavailable: {job['provider']}")
    return jobs


def command_for(job, directory):
    executable = shutil.which(job["provider"])
    if job["provider"] == "codex":
        return [executable, "exec", "--ignore-user-config", "--strict-config",
                "--ephemeral", "--sandbox", "read-only", "--model", job["model"],
                "-c", "model_reasoning_effort=" + json.dumps(job["effort"]),
                "-c", 'approval_policy="never"',
                "-c", "features.shell_tool=" + str(job["tool_mode"] == "files").lower(),
                "-c", "features.multi_agent=false", "-c", "features.apps=false",
                "-c", "features.plugins=false", "-c", 'web_search="disabled"',
                "--skip-git-repo-check", "--cd", str(directory), "--json",
                "--output-schema", job["schema_file"],
                "--output-last-message", str(directory / "report.json"), "-"]
    tools = "Read,Glob,Grep" if job["tool_mode"] == "files" else ""
    command = [executable, "--print", "--restricted", "--safe-mode",
               "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
               "--tools", tools, "--disallowedTools", "mcp__*",
               "--permission-mode", "dontAsk", "--permission-prompts", "none",
               "--no-session-persistence", "--no-chrome", "--model", job["model"],
               "--effort", job["effort"], "--output-format", "json",
               "--json-schema", Path(job["schema_file"]).read_text()]
    if tools:
        command.extend(["--allowedTools", "Read", "Glob", "Grep"])
    for directory in job.get("read_dirs", []):
        command.extend(["--add-dir", directory])
    return command


def stop_process(process):
    # A reaped leader can still have descendants holding the output pipes.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


async def run_job(job, root, semaphore, timeout, halted):
    async with semaphore:
        directory = root / job["job_id"]
        directory.mkdir()
        status = {key: job[key] for key in ("job_id", "decision_id", "role", "provider", "model", "effort")}
        prompt = Path(job["prompt_file"]).read_text()
        guard = ("This is a read-only assignment. Use only the assigned role and inputs. "
                 "Return findings without mutations, external messages, further delegation, "
                 "or consulting artifacts outside your assignment.\n")
        if job["tool_mode"] == "files":
            guard += "Authorized source directories: " + json.dumps(job.get("read_dirs", [])) + "\n"
        status["prompt_sha256"] = hashlib.sha256(prompt.encode()).hexdigest()
        status["schema_sha256"] = hashlib.sha256(Path(job["schema_file"]).read_bytes()).hexdigest()
        status["started_at"] = time.time()
        status["state"] = "running"
        process = None
        communication = None
        stdout = stderr = b""
        try:
            if halted.is_set():
                raise RuntimeError("Dispatch stopped because another job could not be cleaned up")
            process = await asyncio.create_subprocess_exec(
                *command_for(job, directory), cwd=directory,
                start_new_session=True,
                stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            status["pid"] = process.pid
            (directory / "status.json").write_text(json.dumps(status, indent=2))
            communication = asyncio.create_task(process.communicate((guard + prompt).encode()))
            try:
                stdout, stderr = await asyncio.wait_for(
                    asyncio.shield(communication), timeout)
            except asyncio.TimeoutError:
                status["state"] = "timed_out"
            status["returncode"] = process.returncode
            if status["state"] != "timed_out":
                if process.returncode:
                    status["state"] = "failed"
                else:
                    if job["provider"] == "claude":
                        envelope = json.loads(stdout)
                        if envelope.get("is_error") or not isinstance(envelope.get("structured_output"), dict):
                            raise ValueError("Claude returned no successful structured report")
                        report = envelope["structured_output"]
                        status["effective_models"] = list(envelope.get("modelUsage", {}))
                        (directory / "report.json").write_text(json.dumps(report, indent=2))
                    else:
                        report = json.loads((directory / "report.json").read_text())
                        if not isinstance(report, dict):
                            raise ValueError("Codex report must be a JSON object")
                        for line in stdout.splitlines():
                            event = json.loads(line)
                            if event.get("type") == "thread.started":
                                status["thread_id"] = event.get("thread_id")
                    status["state"] = "completed"
        except asyncio.CancelledError:
            status["state"] = "interrupted"
            raise
        except Exception as error:
            status["state"] = "failed"
            status["error"] = str(error)
        finally:
            if process is not None:
                try:
                    stop_process(process)
                    if communication is not None:
                        stdout, stderr = await asyncio.wait_for(
                            asyncio.shield(communication), CLEANUP_TIMEOUT)
                    await asyncio.wait_for(process.wait(), CLEANUP_TIMEOUT)
                except Exception as error:
                    halted.set()
                    status["state"] = "failed"
                    status["cleanup_error"] = str(error) or type(error).__name__
                    if communication is not None and not communication.done():
                        communication.cancel()
                status["returncode"] = process.returncode
            (directory / "stdout.log").write_bytes(stdout)
            (directory / "stderr.log").write_bytes(stderr)
            status["finished_at"] = time.time()
            (directory / "status.json").write_text(json.dumps(status, indent=2))
        print(json.dumps({"job_id":job["job_id"], "state":status["state"], "path":str(directory)}), flush=True)
        return status


async def run_wave(jobs, root, concurrency, timeout):
    semaphore = asyncio.Semaphore(concurrency)
    halted = asyncio.Event()
    results = await asyncio.gather(*(run_job(job, root, semaphore, timeout, halted) for job in jobs))
    (root / "summary.json").write_text(json.dumps(results, indent=2))
    return 0 if all(result["state"] == "completed" for result in results) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-concurrency", type=int, required=True)
    parser.add_argument("--timeout-seconds", type=float, required=True)
    args = parser.parse_args()
    if os.name != "posix":
        parser.error("This runner requires POSIX process groups; use native agents on other systems")
    if args.max_concurrency < 1 or not math.isfinite(args.timeout_seconds) or args.timeout_seconds <= 0:
        parser.error("Concurrency and timeout must be positive")
    try:
        jobs = load_jobs(args.manifest)
        root = args.output_dir.resolve()
        root.mkdir(parents=True, exist_ok=False)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    raise SystemExit(asyncio.run(run_wave(jobs, root, args.max_concurrency, args.timeout_seconds)))


if __name__ == "__main__":
    main()
