---
name: write-adr
description: Write, revise, or supersede architecture decision records (ADRs) documenting an architectural choice and its rationale.
---

# Write ADR

Record one architectural choice, its scope, reasons, and consequences from the
evidence available when decided.

## When an ADR helps

Use ADRs for material structure, domain boundary, interface, dependency, or operational
quality choices. Costly reversal, competing constraints, and rationale invisible in
code are useful signals. Routine task choices stay in the task document; honor explicit
requests for a particular architectural record.

## Find the governing records

Resolve [domain configuration](../setup-beto-frega-skills/references/project-configuration.md),
including external files. Read repository instructions, governing ADRs, and glossary.
Follow configured location, context map, format, numbering, and approval conventions;
reuse the record for the same proposal.

For product/business consequences, use [consolidate](../consolidate/SKILL.md) to find
contract authority and cross-link consequences. ADR acceptance supplies neither
unrelated product nor release authority.

Without naming conventions, use `NNNN-short-decision-title.md`; default to `docs/adr/`
only if no destination is configured. Start at `0001`, otherwise increment the highest
number including retired records. Preserve names and never reuse numbers. Create the
directory only with its first saved record; honor context-specific ADR locations.

## Ground and write

Recover scope, decision, rationale, and approval evidence from conversation and records.
Inspect code/sources affecting reasoning. Distinguish facts, assumptions, intent, and
unknowns; code proves implementation, not approval. Invent no evidence, alternatives,
or results.

Read [ADR-FORMAT.md](ADR-FORMAT.md) for drafting/review; adapt to project format.
Unresolved acceptance yields a reviewable proposal. Ask for a missing choice only if
an accurate draft requires it; reuse session authorization for documentation edits.

## Revise or replace

Edit proposals and factual/editorial corrections in place. During initial architecture
consolidation, an accepted decision without implementation or downstream commitments
may be revised in place: record date, reason, and approval; retain accepted status only
for an approved revision.

Otherwise replace substantive accepted decisions with a new cross-linked ADR,
preserving earlier rationale. Proposed replacements leave the earlier status intact;
once accepted under project conventions, mark the earlier record superseded and link
both ways. Deprecation without replacement records its reason.

## Verify and report

Apply [local document delivery](../consolidate/references/local-document-delivery.md)
for local changes. Read back required content, evidence/assumptions, approval/status,
unique numbering, local references, and replacement links. Reviews remain read-only.
Report the saved link, status, and material open questions. Acceptance records agreement;
implementation and deployment require their own evidence and authority.
