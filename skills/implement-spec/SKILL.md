---
name: implement-spec
description: Implement an entire specification and its ticket graph as one PR.
disable-model-invocation: true
---

Deliver the whole spec on one PR branch. Tickets form a dependency graph; dispatch
its ready frontier with maximum background concurrency.

Keep the user oriented through substantive conversational explanations of consequential
choices, responsibility/behavior changes, and verification limits. Links supplement
that context; do not assume the user read the spec or delegated reviews. Bring
unresolved consequential choices and deviations through [recommend](../recommend/SKILL.md)
before adoption; reuse approved choices and keep routine execution autonomous.

## Steps

1. Read the spec and ticket graph. For product work, read applicable canonical
   contracts/increments through [consolidate](../consolidate/SKILL.md), including
   external configuration. Technical work references product authority; surface
   consequential conflicts. Pass these pointers and the selected workset to agents.
2. If tickets require exploration, optionally delegate it. Save Markdown notes outside
   the repository where future agents can read them; ensure the agent can write there.
3. Create the integration branch and draft PR, marking it as closing the spec issue
   and tickets. Follow repository branch/worktree conventions.
4. Dispatch each ready ticket to an implementer in its own worktree and branch.
5. As implementers finish, use a merger subagent to integrate into the PR branch.
   Dispatch newly ready tickets as the frontier changes.
6. After all tickets complete, run [code-review](../code-review/SKILL.md). Use one
   implementer subagent to fix all issues raised.
7. Mark the PR ready for review and clean up implementer worktrees.
8. Reconcile affected product records through consolidate within existing documentation
   authority, preserving independent delivery/exposure evidence. Report implementation
   and delivery state through [next steps](../next-steps/SKILL.md).
