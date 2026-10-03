"""Relative input reads must not turn the working directory into a read grant."""

import json
from pathlib import Path
import unittest

from audit_native_replay import scope_issue


class NativeAuditTests(unittest.TestCase):
    def setUp(self):
        self.workspace = Path("/Users/betofrega/example")
        self.allowed = {str(self.workspace / "runs/prompts/00021.txt"),
                        str(self.workspace / "runs/decider-schema.json")}

    def call(self, command):
        return {"name": "exec", "code": "const r = await tools.exec_command({cmd:" +
                json.dumps(command) + ",workdir:" + json.dumps(str(self.workspace)) + "});text(r.output)"}

    def test_exact_relative_input_loading(self):
        self.assertFalse(scope_issue(self.call("cat runs/prompts/00021.txt runs/decider-schema.json"),
                                     self.allowed, self.workspace))

    def test_other_files_in_same_workdir_remain_flagged(self):
        self.assertTrue(scope_issue(self.call("cat runs/prompts/00021.txt private/answers/00021.json"),
                                    self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call("cat /Users/betofrega/example"), self.allowed, self.workspace))

    def test_portable_relative_and_absolute_paths(self):
        for directory in ("/tmp/decision-workspace", "/home/ci/decision-workspace", "/tmp/decision workspace"):
            with self.subTest(directory=directory):
                workspace = Path(directory)
                allowed = {str(workspace / "runs/prompt.txt"), str(workspace / "runs/schema.json")}
                def call(command, workdir=True):
                    arguments = {"cmd": command}
                    if workdir:
                        arguments["workdir"] = directory
                    return {"name": "exec", "code": "text(await tools.exec_command(" + json.dumps(arguments) + "));"}
                self.assertFalse(scope_issue(call("cat runs/prompt.txt runs/schema.json"), allowed, workspace))
                self.assertFalse(scope_issue(call("cat runs/prompt.txt", False), allowed, workspace))
                for workdir in (True, False):
                    self.assertTrue(scope_issue(call("cat private/answers/00001.json", workdir), allowed, workspace))
                self.assertFalse(scope_issue(call("cat " + json.dumps(str(workspace / "runs/prompt.txt"))), allowed, workspace))
                self.assertTrue(scope_issue(call("cat " + json.dumps(str(workspace / "private/answers/00001.json"))), allowed, workspace))
                self.assertTrue(scope_issue(call("cat /outside-workspace/answer.json"), allowed, workspace))

    def test_python_input_slices_and_unknown_commands(self):
        command = "python3 -c 'from pathlib import Path; s=Path(\"runs/prompts/00021.txt\").read_text(); print(s[0:20000])'"
        self.assertFalse(scope_issue(self.call(command), self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call(command.replace("runs/prompts/00021.txt", "private/answers/00021.json")),
                                    self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call("python3 -c 'import os; print(os.listdir())'"), self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call("cat runs/prompts/00021.txt; cat private/answers/00021.json"),
                                    self.allowed, self.workspace))
        self.assertTrue(scope_issue({"name": "exec", "code": "text(await tools.exec_command({cmd:dynamicCommand}));"},
                                    self.allowed, self.workspace))

    def test_literal_range_reads_preserve_input_scope(self):
        commands = ["sed -n '1,700p' runs/prompts/00021.txt",
                    "dd if=runs/prompts/00021.txt bs=20000 skip=0 count=1 2>/dev/null"]
        for command in commands:
            with self.subTest(command=command):
                self.assertFalse(scope_issue(self.call(command), self.allowed, self.workspace))
                self.assertTrue(scope_issue(self.call(command.replace("runs/prompts/00021.txt", "private/answers/00021.json")),
                                            self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call("sed -n '1e cat private/answers/00021.json' runs/prompts/00021.txt"),
                                    self.allowed, self.workspace))
        self.assertTrue(scope_issue(self.call("dd if=runs/prompts/00021.txt of=private/output.json"),
                                    self.allowed, self.workspace))


if __name__ == "__main__":
    unittest.main()
