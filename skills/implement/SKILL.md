---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

For product behavior, read the affected canonical contracts through
[consolidate](../consolidate/SKILL.md), including project-scoped
external configuration. Preserve links from the work to functionalities, shared rules,
decisions, and scenarios. Surface conflicts or unresolved policy rather than treating
ticket readiness as product approval.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /code-review to review the work.

Reconcile affected product records through `consolidate` after relevant
implementation, deployment, or release actions. Record supported observations and
verification gaps for each dimension; preserve release and operational flag authority.
Carry the configuration entry and affected record references into delegated work.

Commit your work to the current branch.

When reporting completed implementation or full ticket delivery, use [next steps](../next-steps/SKILL.md) to explain remaining delivery work or recommend the next ticket.
