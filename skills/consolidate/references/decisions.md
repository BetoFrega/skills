# Product and business decisions

Read to record product/business choices, rationale, or contract consequences. Follow
configured names/categories; PDR/BDR are optional labels, not required systems.

## Locate and ground the choice

Recover scope, choice, rationale, caveats, authority, and effective timing from
conversation/records. Find existing proposals before creating objects. Distinguish
acceptance from options/unknowns: code, merges, experiments, and flags establish
execution/observation, not approval.

If acceptance is unresolved, write a reviewable proposal. Ask for a missing choice
only when an accurate record/authorized contract update requires it; reuse session
write authority.

## Decision content

Map applicable meanings to native representation:

- identity, category/scope, status, decision date, effective timing;
- choice and affected audiences/contracts/rules;
- context, constraints, evidence, assumptions, uncertainty;
- actually considered options and material criteria/tradeoffs;
- rationale, expected value/cost, consequences, risks;
- authority/approval evidence and relevant contributors;
- related decisions, shared rules, features, proposals, derived work;
- relevant reconsideration and supersession relationships.

Scale detail to deliberation. Routine approval can use metadata plus the consolidated
rule; significant cross-functional or costly-reversal choices may need a linked
rationale record. Cover the contract regardless of standalone-record requirements.
Invent no alternatives, numeric value, or evidence.

Use [write-adr](../../write-adr/SKILL.md) for architecture. Cross-link mixed rationale
and consequences at their own authorities, without competing decision logs.

## Apply the accepted choice

Update affected [catalogue](catalogue.md), [shared rules/direction](context.md), and
relevant release plan. Separate future-effective changes from current rules; link
specs/tickets without letting them replace policy.

Edit proposals and factual/editorial corrections in place. Consolidate accepted
changes through [record format](record-format.md), which owns native history and
bounded changelogs. Proposed replacements leave acceptance in force; retirement uses
status, relationships, reason, and timing rather than an edit narrative.

Read back authority/status, recoverable rationale/history through decision authority
and native versions, and every affected contract update or named gap. Report partial
updates/unresolved acceptance. Acceptance proves no implementation, deployment, or
exposure; use [reconciliation](reconciliation.md) for those claims.
