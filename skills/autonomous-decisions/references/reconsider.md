# Obtain the Additional Decision

Check the decision record. If `additional_decider_used` is already true, bring the
remaining impasse to the user with options, recommendation, and the exact gap.

Assemble the updated packet from the original scope and criteria, verified facts,
corrections, and points in dispute. Present competing proposals neutrally, including
material objections, without identifying previous votes or supplying peer reports,
judge preferences, or the coordinator's preferred choice.

If claims necessary for reconsideration still need checking, read
[verify.md](verify.md) before dispatch. Preserve unresolved claims as unresolved;
only confirmed facts become established additions to the packet. Apply the standing
rules again if verification reveals a conflict or excluded risk.

Read [decider.md](decider.md). Set `additional_decider_used: true` in the record
before dispatch, reserving the single additional assignment. Create a fresh read-only
decider under the entrypoint's dispatch rules. Give it the updated packet and ask
it to resolve the stated dispute.
Record its agent ID so uncertain tool outcomes can be reconciled without creating
another additional decider.

**Complete when:** the additional decider returns a structurally complete report,
including its attempted resolution and remaining uncertainty, or explains why no
choice is supported. Then read [adjudicate.md](adjudicate.md) for verification and
judgment. A report's uncertainty remains for the judge to assess. Failure to obtain
the report goes to the user; it does not open another decider round.
