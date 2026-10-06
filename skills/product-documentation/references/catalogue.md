# Catalogue

Read this to find or maintain product capabilities and functionality records.
Use [record format](record-format.md) for the living document's representation,
template, example, and consolidation checks.

## Organize outcomes

Start with product areas, capabilities, and functionalities when the project has no
settled hierarchy. Adapt depth and grouping to meaningful domain outcomes. Profiles,
jobs, implementation, and exposure are views over the same records, not reasons to
duplicate a functionality.

A functionality is a recognizable outcome an actor can achieve under relevant
conditions and rules. Split records when outcomes, contracts, or independently
deliverable behavior differ materially. Preserve identity through ordinary evolution.
When splitting, merging, or retiring records, preserve redirects or relationships
and the reason so historical work can still be traced.

Roles describe responsibilities and permissions; segments describe needs and context.
A functionality may serve several roles, segments, and jobs. Capture material
differences without filling every possible combination. Query the native catalogue
through its configured indexes and relationships, including pagination where needed;
a partial search is not evidence that a record does not exist.

## Required meanings

Map the following meanings to the configured native representation. They may be
properties, sections, or linked objects. Cover relevant information; distinguish
unknown, unverified, and inapplicable content with reasons rather than invent data.

| Meaning | Content |
| --- | --- |
| Identity and organization | Stable reference, title, applicable product/context, parent area or capability, and related functionalities. |
| Product decision state | Current approved contract or proposal, acceptance authority and evidence, effective timing, and relevant decision links. |
| User roles | Actors, responsibilities, permissions, and conditions. |
| User segments | Material differences in needs or context. |
| Job to be done | Situation, need, and desired progress. |
| User story | Actor, desired outcome, and reason. |
| Expected behavior | Outcomes, domain states and transitions, permissions, conditions, invariants, limits, exceptions, and scenarios. |
| User value | Benefit, rationale, and evidence in the relevant job and segment context. |
| User cost | Time, effort, money, obligations, friction, or risk in that context. |
| Business value | Contribution to business outcomes, with material audience differences. |
| Business cost | Build investment, operation, support, opportunity cost, and other burdens. |
| Implementation | Behavior constructed and validated, scenario coverage, and verification gaps. |
| Deployment | Observed presence in particular environments, with revision or equivalent provider evidence. |
| Authorized release | Approved audiences, conditions, rollout bounds, and advancement or reversal criteria. |
| Observed exposure | Actual availability by audience and conditions, with coverage and observation time. |
| Flag observations | Relevant controls and their relationships, configuration and targeting, source, and time. |
| Evidence and maintenance | Sources, dates, coverage, maintenance responsibility, unresolved questions, and discrepancies. |
| Traceability | Decisions, shared rules, vocabulary, research, pitches, work records, and verification evidence. |

Use [reconciliation](reconciliation.md) when updating any delivery, exposure, or flag
meaning; it owns interpretation and operational authority for those observations.

## State the behavioral contract

The functionality record is canonical for its specific behavior and rules. Link shared
rules from their canonical records. Define applicable actors, preconditions, outcome,
business transitions, and postconditions. Cover relevant invalid actions, denied
permissions, limits, failures, exceptions, and recovery behavior. Add stable scenario
references where they aid work and verification; link existing tests instead of
copying their implementation into the contract.

For example, a reservation functionality may specify who can reserve, which states
permit it, whether simultaneous reservations are valid, and what happens after expiry.
An illustration of a reservation interface can accompany that contract as replaceable
intent. The interface illustration does not define those business rules by itself.

Read current records and approval evidence before editing. If implementation differs
from approved behavior, retain the contract and record the discrepancy until an
authorized decision changes it. A future-effective accepted change remains separately
identifiable from the contract currently in force.

## Value and cost

Keep user value, user cost, business value, and business cost independently accessible.
Explain each qualitatively for material contexts, then add supported measurements.
Distinguish hypotheses, estimates, and observed outcomes. Numbers and comparative
scores retain their rationale, source, units, and uncertainty where relevant. Absence
of a measurement is not zero cost or proof of value.

## Catalogue admission and completion

Include existing functionalities and proposals sufficiently defined to identify an
actor, desired outcome, scope, and material open questions. Label proposals as such;
raw ideas stay in discovery until their identity is meaningful. Adding a proposal
does not establish acceptance, implementation, or release authority.

After a change, verify the saved contract and its native relationships. Check the
affected audience and job views against the same identity, ensure shared rules and
decisions remain reachable, and identify content or observation gaps. Complete when
each affected functionality and material contract change is accounted for.
