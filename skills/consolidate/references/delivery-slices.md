# Delivery slices

Read this to record or maintain end-to-end feature increments, their acceptance,
dependencies, exposure strategy, and delivery evidence. Use
[selected delivery planning](../../plan-increment/references/selected-work.md) when
the cuts need development. This route owns records; the planning workflow develops
the selected cuts, using grilling for consequential unresolved choices.
Apply [record format](record-format.md) to the resulting living document.

## Outcome and authority

A slice provides a usable end-to-end result within a defined scope, across the layers
needed for that result. Narrow conditions, audiences, cases, or capability while
preserving the outcome. Layer-only or enabling technical work can be a prerequisite;
identify its purpose and satisfaction condition separately from usable increments.

The functionality remains canonical for product behavior. Reference its rules and
scenarios rather than copy the whole contract into each slice. Retain the relevant
actors, jobs, and value/cost references, adding material differences for this scope.
Keep proposed product changes distinguishable from accepted rules. Acceptance of a
slicing plan does not authorize a release or operational flag change.

## Identity and representation

Give each slice a stable reference, outcome-oriented title, functionality relationship,
and decision status with applicable authority evidence. Start with identifiable
sections in the functionality. Use related records when they improve individual
maintenance or queries across functionalities. Setup owns the native mapping; retain
identifiers and links when moving between sections, properties, and related objects.

A slice can require multiple tickets. Its scope comes from a coherent deliverable
outcome; a ticket's execution size does not impose the slice's size. Link derived
specs, tickets, and evidence without treating a single ticket's completion as proof
that the whole slice is implemented or exposed.

## Required slice meanings

Map these to the configured fields, sections, or objects:

- **Usable result and scope:** affected actors and conditions, covered contract rules
  and scenarios, exclusions, and material value/cost differences.
- **Acceptance:** independently verifiable criteria for this increment, including
  relevant failures, denied actions, limits, and recovery. Reference canonical
  scenarios and existing evidence where possible.
- **Dependencies:** implementation and exposure prerequisites, each with its reason
  and satisfaction condition. A complete result may depend on an earlier usable slice.
- **Exposure strategy:** proposed or authorized audience, control relationships,
  disabled behavior, and relevant advancement or reversal criteria. Generally use
  a dedicated flag for independent exposure; explain any shared control, other
  mechanism, or absence of a dedicated flag and its effect on exposure independence.
- **Delivery observations:** independently accessible implementation, deployment,
  authorized release, observed exposure, and flag observations, interpreted through
  [reconciliation](reconciliation.md). Capture evidence, time, environment, audience,
  coverage, and unknowns rather than derive every dimension from one status.
- **Traceability and maintenance:** feature and work references, evidence, outstanding
  decisions, and the configured maintenance process.

Keep a proposed flag name or control requirement separate from an observed provider
identifier and configuration. Map actual shared controls and prerequisites before
making an availability claim. Reconciliation owns operational authority and readback.

## Template, example, and completion

Adapt the [slice template](../assets/delivery-slice-template.md) when the project needs
a representation. Read the [worked example](delivery-slice-example.md) when establishing
that representation or distinguishing product slices from layer-only work.

Verify saved identities, feature relationships, coverage, acceptance, dependencies,
and controls. Account for relevant functionality scenarios as covered by identified
slices, deferred, or unresolved, retaining the reason. Reconcile each affected slice
and the feature's scope: partial delivery remains partial, and the feature's supported
state reflects the applicable audience and scenario coverage. Complete when every
agreed slice and affected relationship is verified or has a named gap.
