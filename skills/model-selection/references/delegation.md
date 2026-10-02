# Delegation

Apply these rules before creating a subagent or separate task.

Identify whether the assignment performs the complete implementation, the complete
review, or narrower supporting work. Recalculate every child ticket independently; a
parent recommendation applies only when the same unresolved decision remains.

Before or alongside every subagent dispatch, tell the user the concrete model and
reasoning effort assigned to it. Report the actual configuration and any substitution
made because the recommendation is unavailable; do not defer disclosure to the final
summary.

- Give a complete implementation or review executor the model and effort recorded in
  the ticket for its provider. Set both explicitly when the interface supports them;
  otherwise include them in the assignment.
- Recalibrate narrower supporting work with the selection criteria in `SKILL.md`. The
  parent recommendation is context, not an automatic minimum.
- Include the applicable ticket recommendation and this delegation rule in the
  assignment. When using a compatible pricing snapshot, include its `checked_at`
  value and billing surface; otherwise carry the recommendation's pricing uncertainty.
  A receiving agent that delegates again carries the same obligation.
- When availability, the cached pricing snapshot, or task evidence changes, reapply the
  [selection and escalation rules](../SKILL.md). Record the revised recommendation
  and the evidence for it in the assignment or execution record.

Delegation is complete when every assignment is traceable to its individual
recommendation, with recalibration recorded under this skill for narrower supporting
work.
