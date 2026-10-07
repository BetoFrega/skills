# Executable work items

Read this to turn selected increments or bounded discovery into tracker work. Use the
configured native representation, labels, and readiness rules; local files are a tracker
choice, not a required intermediate destination.

## Decompose and validate

Each item specifies a concrete action, scope, expected output, validation, and done
criteria. Delivery work references the canonical increment and the acceptance it
contributes. Discovery, prototypes, experiments, maintenance, and necessary enabling
work describe their own verifiable result and affected product knowledge where relevant.
A raw idea without executable work belongs in the canonical knowledge space.

Prefer end-to-end execution cuts that can be verified independently. Size execution
items for reliable work in a fresh context without redefining the product increment
to fit that context. Explicitly link necessary enabling or layer work to the result
it gates. Refactoring belongs in this plan when needed or justified for the selected
result; do not prepend every possible cleanup.

Retain relevant approved technical constraints, ADRs, and existing test boundaries.
Resolve consequential execution gaps before readiness or create bounded discovery
that resolves them. Tests should establish the result, including relevant failures,
rather than mirror proposed implementation details. Use domain and module identities
when helpful; avoid brittle file locations or code listings. Decision-rich prototype
schemas or state machines can be included with their source and limited purpose.

## Dependencies and readiness

Add only genuine blocking edges, explaining the prerequisite and its satisfaction
condition. Distinguish implementation prerequisites from release or exposure gates;
a release gate need not block implementation. Existing approved work and constraints
remain usable. Product approval, breakdown approval, readiness, and operational release
authority are separate meanings.

Apply the configured ready disposition only when required choices, execution inputs,
and start prerequisites are satisfied. Keep blocked or uncertain items in the mapped
non-ready disposition. The absence of ticket blockers alone does not prove readiness.
The executable frontier contains items whose actual start prerequisites are met.

Wide mechanical changes that cannot land independently green may need expand–contract:
introduce the new form alongside the old, migrate call sites in verifiable batches,
then remove the old form after all batches. If batches cannot stay green independently,
use an integration branch and a final integrate-and-verify item with explicit dependencies
and verification. Do not call intermediate broken states usable delivery increments.

## Publish and verify

Use the [work-item template](../assets/work-item-template.md), adapting sections to native
properties. Show the proposed graph and resolve outstanding breakdown decisions before
publication. Reuse approval already covering the same workset; do not ask for it again.
Publish within requested authority and preserve partial results for safe resumption.

- **Local tracker:** one file per ticket at its configured work-record location. Use
  `.scratch/<feature-slug>/issues/<NN>-<slug>.md` only when no replacement is configured.
  Number in dependency order; reference blockers by stable number, title, or file.
- **Remote tracker:** create records in dependency order so relationships can use real
  identifiers. Use verified native blocking or sub-issue operations; otherwise retain
  explicit dependency links in the record. Apply configured readiness and relationships.

Link the source or parent when applicable; planning does not itself close or modify
the parent. Changing existing work requires applicable authorization and the same
scope and readiness checks. Read back every published item, canonical reference,
blocking relationship, and readiness assignment. Account for selected acceptance
across the workset and explicitly identify gaps or failed operations.
