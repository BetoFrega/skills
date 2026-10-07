# Worked delivery-slice example

This is a fictional accepted plan, not evidence of a real product or release. It
shows two increments embedded in one feature; native related records can carry the
same meanings. Names under exposure strategy are proposals, not provider observations.
The feature excerpt shows the rules needed to interpret these slices; it is not a
complete functionality template. The full feature owns its actors, job, and the four
separate value/cost dimensions referenced below.

## Feature: search listings

**Reference:** SEARCH. **Plan authority:** fictional product owner, 2026-10-06.

The accepted contract lets a visitor search visible published listings by words and
optionally restrict the results to a category. Both slices serve the same job: find
relevant listings with less effort. The feature owns value/cost rationale and these
rules:

- SEARCH-R1: return only published listings the visitor may view.
- SEARCH-R2: results match the supplied words under the agreed matching rules.
- SEARCH-R3: when supplied, a category constraint excludes other categories.

### SEARCH-01: find listings by words

**Feature:** SEARCH. **Plan status:** accepted under the feature's plan authority.
**Result and scope:** visitors obtain matching visible listings for supplied words;
covers SEARCH-R1 and SEARCH-R2. Category constraints remain outside this increment.
**Value and cost references:** user value, user cost, business value, and business cost
inherit SEARCH's respective fields; no material differences identified.

**Acceptance criteria:**

- Matching visible published listings are returned.
- Unpublished listings, listings the visitor cannot view, and nonmatches are excluded.
- A valid query with no matches produces an empty result.

**Dependencies:** none identified for this product increment; existing listing access
and publication rules remain applicable. Implementation feasibility is not yet verified.

**Exposure strategy:** pilot audience and rollout criteria are unresolved. A dedicated
`search.keyword` flag is proposed. While disabled, keyword search is unavailable and
existing listing access remains available. Operational creation and release are not
authorized by this plan.

| Dimension | Supported state and evidence |
| --- | --- |
| Implementation | Unknown; no code or acceptance evidence was inspected. |
| Deployment | Unknown; no environment or deployed revision was inspected. |
| Authorized release | Unresolved; the pilot audience and bounds are not approved. |
| Observed exposure | Unknown; no audience behavior was verified. |
| Flag observations | Unknown; the proposed name is not an observed provider control. |

**Work and maintenance:** derived specs and tickets are not yet created. Related
implementation and release work must refresh this slice and the feature's coverage.

### SEARCH-02: restrict a word search to a category

**Feature:** SEARCH. **Plan status:** accepted under the feature's plan authority.
**Result and scope:** visitors obtain word matches within a selected category;
covers SEARCH-R3 together with SEARCH-R1 and SEARCH-R2. Keyword-only search remains
usable while this increment is unavailable.
**User value:** improves relevance for visitors who know the category they want;
inherits the rest of SEARCH's user-value rationale.
**User cost:** inherits SEARCH's user-cost field; no material difference identified.
**Business value:** inherits SEARCH's business-value field; no material difference identified.
**Business cost:** inherits SEARCH's business-cost field; additional operating cost is unmeasured.

**Acceptance criteria:**

- A constrained query returns only visible published word matches in that category.
- An unconstrained query retains the keyword-only behavior.
- A category with no matching listings produces an empty result.
- Disabling this increment preserves keyword-only search and excludes category
  constraints from the available behavior.

| Prerequisite | Dimension | Reason and satisfaction condition |
| --- | --- | --- |
| SEARCH-01 | Implementation | The baseline query path is needed; its applicable acceptance checks must pass. |
| SEARCH-01 | Exposure | Category search extends keyword search; the baseline must be available to the same audience before this increment is exposed. |

**Exposure strategy:** a dedicated `search.category` flag is proposed. Exposure
requires both this control and the baseline keyword-search control for the audience.
Pilot targeting and advancement/reversal criteria remain unresolved. Disabling category
search preserves the baseline; disabling the baseline makes both increments unavailable.

| Dimension | Supported state and evidence |
| --- | --- |
| Implementation | Unknown; no code or acceptance evidence was inspected. |
| Deployment | Unknown; no environment or deployed revision was inspected. |
| Authorized release | Unresolved; audience, bounds, and prerequisite evidence are missing. |
| Observed exposure | Unknown; no audience behavior was verified. |
| Flag observations | Unknown; neither proposed control was inspected at a provider. |

**Work and maintenance:** derived specs and tickets are not yet created. Maintenance
must account for both controls, both slices, and the feature's audience coverage.

## Coverage and current gaps

SEARCH-01 covers SEARCH-R1 and SEARCH-R2. SEARCH-02 adds SEARCH-R3 while retaining the
baseline rules. Each increment is a usable end-to-end result once its prerequisites
hold; enabling query infrastructure is work toward those results. The plan defines
coverage, not proof that any slice or the complete feature is available. Implementation
feasibility, operational controls, pilot audience, and rollout criteria remain open.
