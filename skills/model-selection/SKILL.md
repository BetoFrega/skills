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

## Propagate the recommendation to execution

Before creating a subagent or separate task, read
[delegation.md](references/delegation.md) and apply its dispatch and disclosure rules.
