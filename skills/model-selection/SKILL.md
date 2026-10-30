---
name: model-selection
description: Select models and effort for implementation, review, recommendations, or delegation using capability, cached costs, and unresolved reasoning.
---

# Model Selection

Choose the cheapest configuration that does the work reliably and meets its latency,
tooling, and context needs, unless the user or the role states a preference. Look up
model IDs, capabilities, and supported efforts live.

Assess every assignment on its own: deciders follow the implementation criteria, and
judges or verifiers follow the review criteria. Coordinating with other agents, or
expecting agreement among them, neither raises nor lowers the choice.

Read [ensemble](references/ensemble.md) when explicitly comparing ensemble cost and
reliability, or when adopting an ensemble backed by relevant confirmation data.

## Classify the work

- **Mechanical:** the edit and its precedent are known, with no design choice.
- **Contained:** the behavior, seam, precedent, and acceptance determine the solution.
- **Judgment-heavy:** investigation or competing solutions remain.
- **Frontier:** unresolved architecture or product choices risk silent, expensive
  downstream effects.

Touching authorization, persistence, caching, or public behavior, or a high count of
files, layers, or tests, does not by itself make work judgment-heavy or call for high
effort.

## Set the capability floor

Implementation: a sufficient model for mechanical edits, a balanced one for contained
work, a strong workhorse for judgment-heavy work, and the highest for consequential
decisions whose errors would be silent, expensive, or spread.

Review: a balanced model; a strong workhorse for subtle invariants; the highest for
frontier decisions.

Current Claude anchors: Fable 5.1 is the highest, frontier capability, and Opus 5.5 is
a strong workhorse at lower rates. Capability does not decide effort or cost.

## Choose effort

Choose effort separately: the lowest for obvious edits with precedent, middle for
settled contained work, high for investigation, competing approaches, or subtle
judgment, and the top level only for broad frontier decisions.

## Compare expected cost

Use `~/.agents/model-pricing.json` as the only source for routine pricing, and reload
it after an explicit refresh or when the snapshot changes. An old snapshot is still
valid; its age is provenance. Match billing surface, speed, and units. API rates say
nothing about subscription costs or what can be dispatched.

Estimate input, cache, billable output and reasoning, and retries. At equal or lower
cost, prefer higher capability. Disclose missing or incompatible rates and incomplete
evidence, and pick a suitable default. Name the model, effort, and cost basis.

Read [pricing cache](references/pricing-cache.md) for explicit setup, repair, or refresh.

## Recommend advisory

For stalls, repeated errors, complex algorithms, or unresolved cross-layer
interactions, use [advisory](../advisory/SKILL.md), which owns consultation triggers
and model preference.

## Justify escalation

Effort above middle needs an open question and a concrete consequence of getting it
wrong. A more expensive model needs both too, unless an explicit model preference
applies. Otherwise use middle effort or lower.

Before dispatch, apply [delegation](references/delegation.md).
