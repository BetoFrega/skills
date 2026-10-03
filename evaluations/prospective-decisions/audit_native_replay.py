#!/usr/bin/env python3
"""Recover native-agent usage and audit assigned-input reads after a bounded replay."""

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shlex


def get(path):
    return json.loads(path.read_text())


def put(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def command_paths(command):
    """Admit literal file reads and the input-slicing used by native judges."""
    if "$" in command or "`" in command:
        raise ValueError("Shell expansion is not an audited input read")
    arguments = shlex.split(command)
    if len(arguments) >= 2 and arguments[0] == "cat":
        return arguments[1:]
    if len(arguments) == 4 and arguments[:2] == ["sed", "-n"] and \
            re.fullmatch(r"\d+(?:,\d+)?p", arguments[2]):
        return [arguments[3]]
    if len(arguments) >= 3 and arguments[0] == "dd" and arguments[1].startswith("if=") and all(
            re.fullmatch(r"(?:bs|skip|count)=\d+|2>/dev/null", argument) for argument in arguments[2:]):
        return [arguments[1].removeprefix("if=")]
    if len(arguments) != 3 or arguments[:2] not in (["python3", "-c"], ["python", "-c"]):
        raise ValueError("Unrecognized input-loading command")
    tree = ast.parse(arguments[2])
    permitted = (ast.Module, ast.ImportFrom, ast.alias, ast.Assign, ast.Name, ast.Load,
                 ast.Store, ast.Expr, ast.Call, ast.Attribute, ast.Constant, ast.Subscript, ast.Slice)
    paths = []
    for node in ast.walk(tree):
        if not isinstance(node, permitted):
            raise ValueError("Unrecognized Python input loader")
        if isinstance(node, ast.ImportFrom) and (node.module != "pathlib" or
                [(alias.name, alias.asname) for alias in node.names] != [("Path", None)] or node.level):
            raise ValueError("Unexpected Python import")
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        if isinstance(function, ast.Name) and function.id == "Path":
            if len(node.args) != 1 or node.keywords or not isinstance(node.args[0], ast.Constant) or \
                    not isinstance(node.args[0].value, str):
                raise ValueError("A literal input path is required")
            paths.append(node.args[0].value)
        elif isinstance(function, ast.Name) and function.id == "print" and not node.keywords:
            continue
        elif (isinstance(function, ast.Attribute) and function.attr == "read_text" and
              isinstance(function.value, ast.Call) and isinstance(function.value.func, ast.Name) and
              function.value.func.id == "Path" and not node.args and not node.keywords):
            continue
        else:
            raise ValueError("Unexpected Python call")
    if not paths:
        raise ValueError("No literal input paths")
    return paths


def scope_issue(call, allowed, workspace):
    code = call["code"]
    methods = re.findall(r"tools\.([a-zA-Z0-9_]+)\s*\(", code)
    commands = re.findall(r"tools\.exec_command\s*\(\s*\{([^{}]*)\}\s*\)", code, re.DOTALL)
    if call["name"] != "exec" or set(methods) != {"exec_command"} or len(commands) != len(methods):
        return True
    allowed = {Path(path).resolve() for path in allowed}
    workspace = Path(workspace).resolve()
    try:
        for body in commands:
            cmd = re.search(r'(?:(?:"cmd")|\bcmd)\s*:\s*("(?:\\.|[^"\\])*")', body)
            cwd = re.search(r'(?:(?:"workdir")|\bworkdir)\s*:\s*("(?:\\.|[^"\\])*")', body)
            if cmd is None or (re.search(r'(?:(?:"workdir")|\bworkdir)\s*:', body) and cwd is None):
                return True
            workdir = workspace if cwd is None else (workspace / json.loads(cwd.group(1))).resolve()
            paths = {(workdir / path).resolve() for path in command_paths(json.loads(cmd.group(1)))}
            if paths - allowed:
                return True
    except (ValueError, TypeError, SyntaxError):
        return True
    return False


def audit(output, session_dir):
    receipts = get(output / "native-receipts.json")
    rows, tools, issues = [], Counter(), []
    for receipt in receipts:
        index, thread = receipt["case_index"], receipt["agent_thread_id"]
        paths = list(session_dir.glob("*" + thread + ".jsonl"))
        if len(paths) != 1:
            raise ValueError("Missing or ambiguous native rollout: " + thread)
        path = paths[0]
        infos, contexts, calls = [], [], []
        for line in path.open():
            event = json.loads(line)
            p = event.get("payload", {})
            if event.get("type") == "turn_context":
                contexts.append({"model": p.get("model"), "effort": p.get("effort")})
            if p.get("type") == "token_count" and p.get("info"):
                infos.append(p["info"])
            if event.get("type") == "response_item" and p.get("type") in ("custom_tool_call", "function_call"):
                calls.append({"name": p.get("name"), "code": p.get("input", p.get("arguments", ""))})
        if not infos or not contexts:
            raise ValueError("Native model or usage metadata absent")
        if len(contexts) != 1 or contexts[0] != {"model": "gpt-6.1-sol", "effort": "high"}:
            raise ValueError("Unexpected native context or model configuration")
        total = infos[-1]["total_token_usage"]
        if total.get("cache_write_input_tokens", 0):
            raise ValueError("Cache-write pricing needs separate handling")
        maximum = max(i["last_token_usage"]["input_tokens"] for i in infos)
        if maximum > 272000:
            raise ValueError("A native request exceeds the short-context price boundary")
        outcomes = get(output / "outcomes" / f"{index:05d}.json")
        if len(outcomes["jobs"]) != 1:
            raise ValueError("This native audit covers one assignment per case")
        job = outcomes["jobs"][0]
        schema = Path(job["schema_file"])
        if schema not in {output / "judge-schema.json", output / "decider-schema.json"}:
            raise ValueError("Unexpected native response schema")
        allowed = {str(output / "prompts" / f"{index:05d}.txt"), str(schema)}
        for call in calls:
            tools[call["name"]] += 1
            if scope_issue(call, allowed, Path(__file__).resolve().parents[2]):
                issues.append({"case_index": index, "call": call})
        job_dir = output / outcomes["jobs"][0]["job_id"]
        if get(job_dir / "report.json") != receipt["report"]:
            raise ValueError("Recorded judgment differs from the native receipt")
        usage = {"input_tokens": total["input_tokens"] - total["cached_input_tokens"],
                 "cache_read_input_tokens": total["cached_input_tokens"],
                 "output_tokens": total["output_tokens"]}
        # Parent-generated envelope; the exact native usage record remains alongside it.
        put(job_dir / "stdout.log", {"structured_output": receipt["report"], "usage": usage,
                                   "usage_source": "native_rollout_total_token_usage"})
        provenance = {"agent_thread_id": thread, "source_rollout": str(path),
            "source_rollout_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "total_token_usage": total, "max_request_input_tokens": maximum,
            "reasoning_tokens_already_included_in_output": True, "contexts": contexts}
        put(job_dir / "usage-record.json", provenance)
        status = get(job_dir / "status.json")
        status.update({"agent_thread_id": thread,
            "limits": "Native tools are restricted by assignment, not disabled; local rollouts expose cumulative token usage. Aliases do not identify immutable hosted weights."})
        put(job_dir / "status.json", status)
        rows.append({"case_index": index, **provenance, "input_loading_calls": len(calls)})
    if len({r["agent_thread_id"] for r in rows}) != len(rows):
        raise ValueError("Native contexts were reused across decisions")
    result = {"agents": len(rows), "unique_native_threads": len(rows),
        "aggregate_token_usage": {k: sum(r["total_token_usage"].get(k, 0) for r in rows)
                                  for k in rows[0]["total_token_usage"]},
        "max_request_input_tokens": max(r["max_request_input_tokens"] for r in rows),
        "tool_names": dict(tools), "input_read_scope_issues": issues, "cases": rows,
        "limits": ["Native agents load assigned inputs with tools; the CLI baseline received them through stdin with tools disabled.",
                   "Scope checks inspect recorded command text; they are not an operating-system access boundary.",
                   "The normalized stdout envelope is derived from native logs, not raw CLI output.",
                   "Token counts support conditional API equivalents, not actual subscription charges."]}
    put(output / "native-execution-audit.json", result)
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))
    if issues:
        raise ValueError("Review native input-read scope issues before interpreting results")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--session-dir", type=Path, required=True)
    args = parser.parse_args()
    audit(args.output.resolve(), args.session_dir.resolve())
