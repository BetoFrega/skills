---
name: model-selection
description: Select models and reasoning effort for implementation, review, recommendations, or delegated agent work using required capability, cached costs, and unresolved reasoning.
---

# Model Selection

Choose the lowest expected cost configuration that can reliably complete the assignment. Recommendations are starting points, not insurance against every complication.

Resolve model names, capabilities, and supported efforts from the live environment. Explicit user choices govern.

Select every assignment independently, including deciders, judges, and verifiers. Agent count or agreement alone justifies no capability or effort discount.

For explicit ensemble cost/reliability comparisons or adoption supported by relevant confirmation data, read [ensemble](references/ensemble.md).

## Classify the work

Classify unresolved reasoning:

- **Mechanical:** exact edit and precedent known; no meaningful design choice.
- **Contained:** behavior, seam, prior art, and acceptance criteria determine the solution, even across files or layers.
- **Judgment-heavy:** investigation or comparison between plausible solutions remains.
- **Frontier:** an unresolved architecture or product decision could silently or expensively affect later work.

Authorization, persistence, caching, public behavior, and file/layer/test counts affect verification and consequences; alone they justify neither judgment-heavy classification nor high effort.

## Set the capability floor

For implementation, mechanical work needs enough capability for the known edit; contained work needs balanced capability; judgment-heavy work needs strong workhorse capability. Highest capability requires an unresolved consequential decision whose errors would be silent, expensive, or propagate.

For review, default to balanced capability. Use strong workhorse capability for subtle invariants; highest only when resolving or challenging a frontier decision, rather than verifying settled implementation.

Deciders use implementation criteria; judges and verifiers use review criteria. Classify each role's reasoning independently; a coordinator's recommendation sets no universal minimum.

## Choose effort

Set effort from unresolved reasoning, independently of capability:

- Lowest suitable: obvious edit or direct application of prior art.
- Middle: contained implementation or review with settled decisions.
- High: investigation, competing approaches, or subtle judgment.
- Exceptional top: a frontier decision governing broader work.

## Compare expected cost

After setting capability and effort, compare configurations meeting latency, tooling, and context requirements.

Read `~/.agents/model-pricing.json` and reuse it within the session. Reload after successful explicit refresh or detected snapshot change. Routine selection uses this local snapshot exclusively; age is provenance, not a refresh trigger. Match billing surface, speed mode, and units.

Estimate input, cache use, billable output including reasoning, and retries. Prefer greater capability at equal or lower expected cost when other requirements are met. Missing or incompatible rates or incomplete evidence require stated uncertainty and a suitable default.

Name model, effort, and cost basis. For explicit cache setup, repair, or refresh, read [pricing cache](references/pricing-cache.md).

## Justify escalation

Paying more for capability or exceeding middle effort requires both a concrete unresolved question and concrete consequence of error. Generic risk claims are insufficient. If either is absent, choose the least expensive suitable configuration with at most middle effort.

Before creating subagents or separate tasks, apply [delegation](references/delegation.md) dispatch and disclosure rules.
