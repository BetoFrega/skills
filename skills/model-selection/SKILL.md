---
name: model-selection
description: Select models and reasoning effort for implementation, review, recommendations, or delegated agent work using required capability, current costs, and unresolved reasoning.
---

# Model Selection

Choose the lowest expected cost configuration that can complete the assigned work
reliably. Treat a recommendation as a starting point, not insurance against every
possible complication.

Resolve current model names, capability descriptions, and supported effort values
from the live execution environment. An explicit model or effort requested by the
user remains authoritative.

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

## Determine minimum capability

Treat these tiers as capability floors. Select the actual configuration after
choosing the required effort.

For implementation:

- Mechanical work needs enough capability to apply the known edit.
- Contained work needs balanced capability.
- Judgment-heavy work needs strong workhorse capability.
- Frontier work needs the highest-capability tier only when a consequential decision
  remains unresolved **and** a wrong decision would be silent, expensive, or propagate
  into later work.

For review:

- Require balanced capability by default.
- Require strong workhorse capability when correctness depends on correlating subtle
  invariants.
- Require the highest-capability tier only when the review must resolve or challenge a
  frontier decision, rather than verify an already-decided implementation.

## Choose reasoning effort

Choose effort from the unresolved reasoning:

- Use the lowest suitable effort for one obvious edit or direct application of prior
  art.
- Use a middle effort for contained implementation or review with settled decisions.
- Use high effort when investigation, competing approaches, or subtle judgment remain.
- Use the environment's exceptional top effort only when a frontier decision will
  govern a broader slice of work.

Several files, layers, or test tiers do not independently justify high effort.

## Choose configuration by expected cost

Compare available configurations that meet the capability floor and the task's
latency, tooling, and context requirements. Verify current prices for the applicable
billing surface and speed mode in official provider documentation or account-specific
rates.

Estimate task cost from expected input, cache use, billable output (including
reasoning), and likely retries. Prefer greater capability when expected cost is equal
or lower and the configuration meets the same requirements. When evidence is
incomplete, state the uncertainty and use a suitable default.

Name the selected model and effort and the cost basis for the recommendation.

## Justify escalation

Any recommendation that pays more for greater capability or uses effort above middle
names both the concrete unresolved question and the concrete consequence of deciding
it incorrectly. Generic statements such as “crosses layers”, “touches authorization”,
“requires care”, or “must preserve behavior” do not justify escalation. When either
element is absent, choose the least expensive suitable configuration with at most
middle effort.

## Propagate the recommendation to execution

Before creating a subagent or separate task, read
[delegation.md](references/delegation.md) and apply its dispatch and disclosure rules.
