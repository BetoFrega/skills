---
name: implement
description: Implement selected work from a spec or tickets.
disable-model-invocation: true
---

For product work, read affected canonical contracts through
[consolidate](../consolidate/SKILL.md), including external configuration. Preserve
functionality, shared-rule, decision, and scenario links; surface conflicts or
unresolved policy. Ticket readiness does not establish product approval. Carry the
configuration entry and affected record references into delegated work.

Explain the intended behavior and responsibility changes in conversation without
assuming the user read the spec. Bring unresolved consequential domain, product, or
code-design choices and discovered deviations through [recommend](../recommend/SKILL.md)
before implementing them; reuse approvals and continue routine work within them.
At delivery, explain resulting behavior, actual rationale, consequences, and what
verification establishes or leaves uncertain. Keep detail proportional to significance.

Use [tdd](../tdd/SKILL.md) where possible, at pre-agreed seams. Run typechecking and
single test files regularly, then the full suite once at the end. Finish with
[code-review](../code-review/SKILL.md).

After relevant implementation, deployment, or release actions, reconcile affected
product records through consolidate: supported observations and verification gaps
for each dimension, preserving release/operational flag authority. Commit the work to the current branch.
Report remaining delivery work or the next ticket through
[next steps](../next-steps/SKILL.md).
