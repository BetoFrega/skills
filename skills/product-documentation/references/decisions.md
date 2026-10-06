# Product and business decisions

Read this to record a product/business choice, preserve its rationale, or update the
contracts it affects. Use the project's conventions for record names and categories;
PDR and BDR are optional local labels, not mandatory separate systems.

## Locate and ground the choice

Find the decision, scope, rationale, caveats, acceptance authority, and effective
timing in the conversation and project records. Search for the same proposal or
choice before creating another object. Distinguish accepted choices from options
and unresolved decisions. A code change, merged ticket, experiment result, or active
flag is evidence of execution or observation; acceptance needs its own authority.

Record a reviewable proposal when acceptance is unresolved. Ask for a missing choice
only when needed for an accurate record or authorized contract update. Reuse existing
session authorization for documentation within its scope.

## Decision content

Map applicable content to the configured native representation:

- identity, decision scope/category, status, decision date, and effective timing;
- the choice and affected audiences, product contracts, or business rules;
- context, constraints, material evidence, assumptions, and uncertainty;
- options actually considered and the criteria or trade-offs that mattered;
- rationale, expected value and cost, consequences, and material risks;
- decision authority and acceptance evidence, contributors when relevant;
- related decisions, shared rules, functionalities, proposals, and derived work;
- reconsideration triggers and supersession relationships when relevant.

Keep the explanation proportional to the deliberation. Routine acceptance can be
represented by compact authority metadata and the consolidated rule. Significant
cross-functional or costly-to-reverse choices may warrant a linked decision record
explaining the choice and rationale. Cover the affected product contract regardless
of whether the project requires a standalone decision object. Preserve unknowns
rather than invent alternatives, numeric value, or evidence.

For architecture decisions, use [write-adr](../../write-adr/SKILL.md). A mixed choice
can link product/business rationale and architectural consequences; keep each meaning
at its configured authority without copying the same decision into competing logs.

## Apply the accepted choice

For an accepted choice, update the affected [catalogue](catalogue.md),
[shared rules or direction](context.md), and release plan where relevant. Preserve
future-effective changes separately from the currently effective contract. Link
derived specs and tickets; those work records do not silently replace product policy.

Edit proposals and factual or editorial corrections in place. Consolidate accepted
changes in the affected records using [record format](record-format.md); it owns
native history and the optional bounded changelog. A proposed replacement leaves the
accepted choice in force. Use status, relationships, reasons, and effective timing
when retiring a decision, without adding a narrative of document revisions.

Complete when the decision's saved status matches its authority, rationale and history
are recoverable through the configured decision authority and native versions, and
every affected contract has a verified consolidated update or a named gap.
Report unresolved acceptance or partial contract updates explicitly. Acceptance does
not establish implementation, deployment, or actual exposure; use
[reconciliation](reconciliation.md) for those claims.
