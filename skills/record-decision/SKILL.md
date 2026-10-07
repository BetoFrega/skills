---
name: record-decision
description: Record an approved decision in its canonical project or task record.
---

# Record Decision

Find the latest explicit user decision and its scope, rationale, and caveats in the
conversation. Resolve its canonical authority through the applicable branch below
before writing. Preserve relevant history and supersession. Record what was approved
without treating it as approval of later execution.

For a product or business choice, use
[`consolidate`](../consolidate/SKILL.md) to find the configured
authority, preserve decision history, and update affected product contracts. A spec
or ticket remains a linked work record rather than the implicit authority for product
policy. If a choice also affects architecture, link the architectural record.

When the destination is an ADR, or an architectural decision may warrant one, use
[`write-adr`](../write-adr/SKILL.md) for ADR authoring and lifecycle rules. Keep routine
task decisions in the task's canonical document.

For a routine task decision with no canonical document, create a concise note in the
task workspace. For unresolved product authority, identify the configuration gap and
keep any workspace note clearly marked as a draft. If the decision or destination is
ambiguous, ask before editing. Verify the saved result and report its path and the
decision recorded. Keep this invocation to documentation; external posting, memory
updates, commits, and pushes require their own authorization.
