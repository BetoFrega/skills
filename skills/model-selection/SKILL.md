---
name: model-selection
description: Select models and reasoning effort for implementation, review, recommendations, or delegated agent work based on unresolved reasoning and concrete escalation risk.
---

# Model Selection

Choose the least expensive configuration expected to complete the assigned work
reliably. Treat a recommendation as a starting point, not insurance against every
possible complication.

Resolve current model names, capability descriptions, and supported effort values
from the live execution environment. This skill defines capability tiers, not a cache
of provider catalogs. An explicit model or effort requested by the user remains
authoritative.

## Classify the assigned work

Classify the work by unresolved reasoning, not by file, layer, or test count:

- **Mechanical:** the exact edit and precedent are known; there is no meaningful
  design choice.
- **Contained:** work may span files or layers, but the behavior, seam, prior art, and
  acceptance criteria determine the shape of the solution.
- **Judgment-heavy:** investigation or comparison between plausible solutions remains
  necessary.
- **Frontier:** an unresolved architectural or product decision could silently or
  expensively affect later work.

Authorization, persistence, caching, public behavior, multiple layers, and multiple
test tiers affect verification and the consequence of mistakes. They do not by
themselves make the work judgment-heavy.

## Choose model capability

For implementation:

- Mechanical work uses the fastest suitable model.
- Contained work uses a balanced model by default.
- Judgment-heavy work uses a strong workhorse model.
- Frontier work uses the highest-capability model only when a consequential decision
  remains unresolved **and** a wrong decision would be silent, expensive, or propagate
  into later work.

For review:

- Use a balanced model by default.
- Use a strong workhorse when correctness depends on correlating subtle invariants.
- Use the highest-capability model only when the review must resolve or challenge a
  frontier decision, rather than verify an already-decided implementation.

When the assigned work specifies its seam, behavior, precedent, and a contained
acceptance checklist, cap implementation at the balanced tier unless a remaining
decision defeats that cap.

## Choose reasoning effort

Choose effort from the unresolved reasoning:

- Use the lowest suitable effort for one obvious edit or direct application of prior
  art.
- Use a middle effort for contained implementation or review with settled decisions.
- Use high effort when investigation, competing approaches, or subtle judgment remain.
- Use the environment's exceptional top effort only when a frontier decision will
  govern a broader slice of work.

Several files, layers, or test tiers do not independently justify high effort.

## Justify escalation

Any recommendation above a balanced model or middle effort names both the concrete
unresolved question and the concrete consequence of deciding it incorrectly. Generic
statements such as “crosses layers”, “touches authorization”, “requires care”, or “must
preserve behavior” do not justify escalation. When either element is absent, use the
lower configuration.

Recalculate every child ticket independently. A parent recommendation applies to a
child only when the same unresolved decision remains in that child. Execution may
escalate after discovering evidence absent from the ticket; record that evidence when
escalating.

## Propagate the recommendation to execution

Before creating a subagent or a separate task, identify whether it will perform the
complete implementation, the complete review, or a narrower supporting assignment.

Before or alongside every subagent dispatch, tell the user the concrete model and
reasoning effort assigned to it. Report the actual configuration, including any
substitution made because the recommended configuration is unavailable; do not defer
this disclosure to the final summary.

- Give the complete implementation or review executor the corresponding model and
  effort recorded in the ticket for its provider. Set both explicitly when the
  dispatch interface supports them; otherwise include them in the assignment.
- Recalibrate a narrower assignment with this skill. The parent recommendation is
  context, not an automatic minimum, so mechanical exploration or editing can use a
  cheaper configuration.
- Include the applicable ticket recommendation and this delegation rule in the
  assignment. A receiving agent that delegates again carries the same obligation.
- When the recommended model is unavailable, use the closest available capability
  tier and record the substitution.
- Deviate upward only because of concrete evidence discovered after the ticket was
  written, and record that evidence in the assignment or execution record.

Delegation is complete when every delegated assignment is traceable either to the
ticket recommendation for complete implementation or review, or to a recalibration
recorded under this skill for supporting work.
