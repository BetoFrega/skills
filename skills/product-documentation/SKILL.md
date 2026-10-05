---
name: product-documentation
description: Maintain product catalogues, shared rules, direction and evidence, product/business decisions, and proposals; reconcile implementation, deployment, release, audience exposure, and feature flags against canonical product records.
---

# Product documentation

Maintain explicit product knowledge that product owners and agents can use across
sessions. Preserve intent, behavior, authority, evidence, and history. Adapt formats,
workflow, hierarchy, and depth to the product while covering the relevant contract.

## Resolve authority and intent

Use [project configuration locations](../setup-beto-frega-skills/references/project-configuration.md#resolve-configuration)
to resolve the product configuration, including files outside the repository. Read
its canonical destinations, native representation, product conventions, applicable
decisions, and maintenance sources. Retain existing identifiers and settled choices.
Locate affected records and the operation's existing authorization before writing.

Standard setup owns configuration. For an unresolved destination or convention,
identify the gap and suggest explicit `$setup-beto-frega-skills` use. Continue work
that has a known authority; prepare a clearly identified draft for blocked writes.
A draft stays subordinate to the canonical destination. A configured replacement
that is unavailable remains an explicit gap.

Read only the references needed for the task. Combine routes when one change affects
several documentation functions; the table is a router, not a mandatory sequence.

| Route | Read when |
| --- | --- |
| [Catalogue](references/catalogue.md) | Finding capabilities or defining and updating functionalities, audiences, jobs, behavior, value, and cost. |
| [Context](references/context.md) | Maintaining product direction, business context, shared rules, vocabulary links, or research and experiment evidence. |
| [Decisions](references/decisions.md) | Recording product or business choices and rationale, preserving history, or applying an accepted change to affected contracts. |
| [Proposals](references/proposals.md) | Shaping a product proposal or pitch for an investment decision. |
| [Reconciliation](references/reconciliation.md) | Maintaining implementation, deployment, release, exposure, and flag observations, or investigating documentation drift. |

For an architectural choice, use [write-adr](../write-adr/SKILL.md). For vocabulary
definitions, follow [the glossary format](../domain-modeling/CONTEXT-FORMAT.md) and
configured domain conventions. Keep product-specific behavior in the catalogue and
cross-functional rules in their shared authority.
Specs and tickets describe work derived from these records and retain links to them.

## Write the affected knowledge

Distinguish approved intent, proposals, observed implementation, and assumptions.
Use conversation and project evidence for approval; code or flag configuration alone
does not establish a product decision. State material unknowns and discrepancies.
Carry observation time, source, scope, and coverage with claims about actual state.

Use the configured properties, sections, objects, and links. Preserve a single
canonical record for each meaning rather than duplicate it across views. Capture
all relevant behavior, exceptions, and scenarios needed for agents to implement
and verify the contract; proportionality adjusts detail and governance, not whether
known rules are documented. Update linked records affected by an accepted change.

Interaction illustrations may express intent. Label them illustrative and
replaceable; write binding outcomes and rules explicitly so implementation choices
remain open.

Exercise existing authorization within its scope. Documentation maintenance does
not itself authorize a new release, flag change, scheduled job, or product policy.
Read the reconciliation route before any authorized operational flag change.

## Verify completion

Read back saved records and relationships in the configured destination. Check
identity, representation, applicable content, authority and effective timing,
source coverage, and links to decisions, shared rules, work, and verification.
Account for every affected record with a verified result or a named remaining gap.

For a lookup or review, answer with the relevant canonical references and concrete
findings. For a change, report what was saved, what remains proposed or unknown, and
any unverifiable effect. A prepared draft, an accepted decision, an implemented
change, and a verified release are distinct outcomes.
