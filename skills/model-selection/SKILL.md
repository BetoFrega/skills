---
name: model-selection
description: Select models and effort for implementation, review, recommendations, or delegation using capability, cached costs, and unresolved reasoning.
---

# Model Selection

Choose the cheapest reliable configuration meeting latency, tooling, and context needs, subject to explicit user or role preferences. Resolve IDs, capabilities, and supported efforts live.

Assess every assignment independently: deciders follow implementation criteria; judges/verifiers follow review criteria. Coordination or agreement sets no universal floor or discount.

Read [ensemble](references/ensemble.md) for explicit ensemble cost/reliability comparisons or adoption backed by relevant confirmation data.

## Classify the work

- **Mechanical:** known edit and precedent, no design choice.
- **Contained:** behavior, seam, precedent, and acceptance determine the solution.
- **Judgment-heavy:** investigation or competing solutions remain.
- **Frontier:** unresolved architecture/product choices risk silent, expensive downstream effects.

Authorization, persistence, caching, public behavior, and file/layer/test counts alone justify neither judgment-heavy classification nor high effort.

## Set the capability floor

Implementation: sufficient for mechanical edits; balanced for contained work; strong workhorse for judgment-heavy work; highest for consequential decisions risking silent, expensive, or propagating errors.

Review: balanced; strong workhorse for subtle invariants; highest for frontier decisions.

Opus 5.5: highest/frontier capability, with cheaper standard API rates than Opus 5, a strong workhorse. Capability sets neither effort nor cost.

## Choose effort

Independently: lowest for obvious edits/precedent; middle for settled, contained work; high for investigation, competing approaches, or subtle judgment; exceptional top for broader frontier decisions.

## Compare expected cost

Reuse `~/.agents/model-pricing.json` exclusively for routine pricing; reload after explicit refresh or snapshot change. Age is provenance, not a refresh trigger. Match billing surface, speed, and units; API rates imply neither subscription costs nor dispatch availability.

Estimate input, cache, billable output/reasoning, and retries. Prefer higher capability at equal/lower cost. Disclose missing/incompatible rates or incomplete evidence; choose a suitable default. Name model, effort, and cost basis.

Read [pricing cache](references/pricing-cache.md) for explicit setup, repair, or refresh.

## Recommend advisory

For stalls, repeated errors, complex algorithms, or unresolved cross-layer interactions, use [advisory](../advisory/SKILL.md), which owns consultation triggers and model preference.

## Justify escalation

Above-middle effort always requires an unresolved question and concrete error consequence; paying more requires both unless an explicit model preference applies. Otherwise use at most middle effort.

Before dispatch, apply [delegation](references/delegation.md).
