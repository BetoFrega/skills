---
name: implement
description: Implement selected work from a spec or tickets.
disable-model-invocation: true
---

Read [beto-mode](../beto-mode/SKILL.md) first and apply the principles it routes to
throughout the work.

For product work, read affected canonical contracts through
[consolidate](../consolidate/SKILL.md), including external configuration. Preserve
functionality, shared-rule, decision, and scenario links; surface conflicts or
unresolved policy. A ready ticket still needs product approval. Carry the
configuration entry and affected record references into delegated work.

Before coding a ticket, read its related tickets: parent, siblings, dependencies, and
the tickets it blocks. Keep the code within the contracts they fix, such as
interfaces, data formats, and accepted decisions, and bring a needed change through
recommend before making it.

Explain the intended behavior and responsibility changes in conversation without
assuming the user read the spec. Bring unresolved consequential domain, product, or
code-design choices and discovered deviations through [recommend](../recommend/SKILL.md)
before implementing them; reuse approvals and continue routine work within them.
At delivery, explain resulting behavior, actual rationale, consequences, and what
verification establishes or leaves uncertain. Keep detail proportional to significance.

Use [tdd](../tdd/SKILL.md) where possible, at pre-agreed seams. Run typechecking and
single test files regularly, then the full suite once at the end. Once the work
passes, make a simplification pass per
[Subtract Before You Add](../beto-mode/principles/subtract-before-you-add.md)'s
"Simplify again in the same change", check the comments you wrote against
[Comments Earn Their Place](../beto-mode/principles/comments-earn-their-place.md),
then finish with [code-review](../code-review/SKILL.md).

After relevant implementation, deployment, or release actions, reconcile affected
product records through consolidate: supported observations and verification gaps
for each dimension, preserving release/operational flag authority. Commit the work to the current branch.
Report remaining delivery work or the next ticket through
[next steps](../next-steps/SKILL.md).
