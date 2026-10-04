---
name: write-adr
description: Write, revise, or supersede architecture decision records (ADRs) when documenting an architectural choice and its rationale.
---

# Write ADR

Record one architectural decision so a future reader can understand its scope,
reasons, and consequences using the evidence available when it was made.

## When an ADR helps

Use an ADR for a decision that materially affects system structure, domain
boundaries, interfaces, dependencies, or operational qualities. Costly reversal,
competing constraints, and a choice whose rationale is invisible in code are good
signals. For a routine task decision, use the existing task document. Honor an
explicit request to document a particular architectural decision.

## Find the governing records

Read repository instructions, any domain-document configuration, and existing ADRs
that govern the affected area. Use the glossary for domain terms. Follow the
project's existing location, format, numbering, and approval conventions. Reuse an
existing record for the same proposal rather than create a duplicate.

If conventions are absent, use `docs/adr/NNNN-short-decision-title.md`, starting at
`0001`. Increment the highest number in the selected directory, including retired
records; preserve existing filenames and never reuse numbers. Create the directory
only when saving the first record. Follow an existing context map when it defines
context-specific ADR locations.

## Ground and write

Recover the decision, scope, rationale, and approval evidence from the conversation
and project records. Inspect relevant code and referenced sources for claims that
affect the reasoning. Distinguish observed facts, assumptions, and intended
behavior; code can establish implementation, but does not by itself establish who
approved a decision. State material unknowns instead of inventing evidence,
alternatives, or results.

Read [ADR-FORMAT.md](ADR-FORMAT.md) when drafting or reviewing a record. Adapt its
content requirements to the project's format. Write a reviewable proposal when
acceptance is unresolved. Ask for a missing decision only when its absence prevents
an accurate draft; use existing session authorization for documentation edits.

## Revise or replace

Edit proposals and factual or editorial corrections in place. When changing an
accepted decision's substance, create a new ADR and link it to the earlier one,
preserving the earlier rationale. A proposed replacement leaves the earlier
decision's status intact. Once the replacement is accepted under the project's
approval convention, mark the earlier ADR as superseded and link both directions.
When retiring a decision without a replacement, record the reason for deprecation.

## Verify and report

Read back the saved files. Check that the required content is present, material
claims have evidence or explicit assumptions, status matches approval evidence,
numbering is unique, and local references and replacement links resolve. For a
review-only request, report concrete gaps without changing files.

Report the saved path, decision status, and material unresolved questions. Acceptance
records agreement on the decision; implementation and deployment claims require
their own evidence and authorization.
