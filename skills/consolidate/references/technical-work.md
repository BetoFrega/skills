# Technical decisions and scoped specs

Read this when consolidation includes technical choices or a technical work spec.
Use configured domain, ADR, and tracker destinations. A technical spec is a work
artifact linked to canonical product behavior; it can be useful without being
mandatory for every increment.

## Route the knowledge

- Product outcomes, permissions, rules, and exceptions go to their catalogue or
  shared-rule authority through the relevant product routes.
- Terms go to the configured glossary using the domain-modeling format.
- Significant architectural choices use [write-adr](../../write-adr/SKILL.md), which
  owns admission, rationale, approval, and supersession.
- A selected implementation approach, constraints, interfaces, migration strategy,
  feasibility questions, and validation can belong in a scoped technical tracker spec.

Keep each meaning at its authority and connect mixed decisions through references.
Existing decisions and approvals remain usable; consolidation does not reopen the
interview or select additional increments.

## Prepare the selected technical work

Read the selected increment definitions, relevant code, existing interfaces, ADRs,
and verification evidence. Record decisions needed to preserve the scope and make
the work executable; leave routine implementation choices to the implementer. Reuse
existing test boundaries and prior tests where they verify the intended behavior.
Choose a practical boundary that can establish acceptance without testing internals.
Reuse agreed boundaries; resolve a consequential new validation choice with the user.

Distinguish accepted decisions, feasible alternatives, and assumptions needing evidence.
For a blocking factual gap, apply the
[discovery handoff](../../grilling/references/product-increments.md#when-evidence-blocks-the-slice).
Preserve its question and completion criterion instead of describing indefinite
investigation followed by implementation of whatever emerges.

## Write only the useful spec

When the requested work benefits from a spec, adapt the
[technical-spec template](../assets/technical-spec-template.md) to the configured
tracker representation. Reference canonical product rules and the selected increment
IDs. Cover the relevant technical approach, constraints, dependencies, validation,
and exclusions. Keep proposals and unresolved choices explicit.

Use modules and interface identities where they clarify commitments; look up current
file locations when implementing. A prototype-derived state machine, schema, or type
shape can encode a decision more precisely than prose: retain only the decision-rich
part and its provenance. Illustrative interaction concepts leave presentation choices
open; binding product outcomes remain in their product authority.

Resolve the tracker workflow through project configuration. Prepare or publish only
within the requested scope and existing authority, reusing applicable confirmation.
Map readiness to concrete work with completion criteria and satisfied prerequisites;
unresolved execution-blocking choices use the configured non-ready disposition.
An approved product direction or technical proposal alone does not establish readiness.

Read back published content, identity, references, relationships, and readiness.
Report draft-only or partial effects explicitly. The spec is complete when the selected
technical knowledge is preserved, its product and architectural authorities remain
reachable, and consequential gaps and their next actions are identifiable.
