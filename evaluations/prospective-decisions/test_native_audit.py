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


if __name__ == "__main__":
    unittest.main()
