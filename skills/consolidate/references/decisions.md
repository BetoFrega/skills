# Product and business decisions

Read this to record product or business choices, their rationale, or their contract
consequences. Follow the configured names and categories; PDR and BDR are optional
labels.

## Locate and ground the choice

Recover the scope, choice, rationale, caveats, authority, and effective timing from
the conversation and records. Look for existing proposals before creating objects.
Separate acceptance from options and unknowns. Code, merges, experiments, and flags
show execution or observation; they do not show approval.

If acceptance is unresolved, write a reviewable proposal. Ask for a missing choice
only when an accurate record or an authorized contract update needs it, and reuse the
session's write authority.

## Decision content

Map the applicable meanings to the native representation:

- identity, category and scope, status, decision date, and effective timing;
- the choice and the audiences, contracts, and rules it affects;
- context, constraints, evidence, assumptions, and uncertainty;
- options actually considered, with material criteria and tradeoffs;
- rationale, expected value and cost, consequences, and risks;
- authority, approval evidence, and relevant contributors;
- related decisions, shared rules, features, proposals, and derived work;
- relevant reconsideration and supersession relationships.

Scale detail to the deliberation. A routine approval can be metadata plus the
consolidated rule; a significant cross-functional choice, or one that is costly to
reverse, may need a linked rationale record. Cover the contract either way. Do not
invent alternatives, numeric values, or evidence.

Use [write-adr](../../write-adr/SKILL.md) for architecture. When rationale and
consequences span both, link each part from its own authority, and keep a single
decision log.

## Apply the accepted choice

Update the affected [catalogue](catalogue.md), [shared rules and direction](context.md),
and the relevant release plan. Keep future-effective changes apart from current rules,
and link specs and tickets without letting them replace policy.

Edit proposals and factual or editorial corrections in place. Consolidate accepted
changes through [record format](record-format.md), which owns native history and
bounded changelogs. A proposed replacement leaves the accepted choice in force until
it is accepted; retirement uses status, relationships, reason, and timing instead of
an edit narrative.

Read back the authority and status, check that rationale and history can be recovered
through the decision record and native versions, and account for every affected
contract update or named gap. Report partial updates and unresolved acceptance.
Acceptance says nothing about implementation, deployment, or exposure; use
[reconciliation](reconciliation.md) for those claims.
