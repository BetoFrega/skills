"""Protocol regressions for replay routing; no live model calls."""

import unittest

import judge_swap


class ReplayRoutingTests(unittest.IsolatedAsyncioTestCase):
    def case(self, count=2):
        return {"initial_judge_prompt": "frozen original input", "packet": {
            "evidence": [{"id": "plan-a"}, {"id": "plan-b"}]},
            "reports": [{"decision": "plan-a"} for _ in range(count)]}

    def judgment(self, outcome, preferred="plan-a"):
        return {"outcome": outcome, "candidate": "plan-a", "preferred_choice": preferred,
                "remaining_gap": "Check the second capacity world."}

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


if __name__ == "__main__":
    unittest.main()
