---
name: record-decision
description: Record an approved decision in the task's canonical document.
---

# Record Decision

Find the latest explicit user decision and its scope, rationale, and caveats in the conversation. Update the task's existing canonical document, keeping prior history where relevant and clearly marking any superseded decision. Record what was approved without treating it as approval of later execution.

When the destination is an ADR, or the decision may warrant one, use
[`write-adr`](../write-adr/SKILL.md) for ADR authoring and lifecycle rules. Keep other
decisions in the task's canonical document.

If no canonical document exists, create a concise decision note in the task workspace. If the decision or destination is ambiguous, ask before editing. Verify the saved result and report its path and the decision recorded. Keep this invocation to documentation; external posting, memory updates, commits, and pushes require their own authorization.
