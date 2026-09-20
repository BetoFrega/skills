---
name: investigate-low-density
description: Investigate flagged or suspected low information density in logs, documentation, instructions, or responses. Use for deep analysis of repetition, noisy output, unselected dumps, or reducible content, including issues labeled `low-info-density`; this skill finds causes and safe reductions but does not implement them.
---

# Investigate low density

Investigate the user-defined scope. If none is explicit, use only the artifacts or
tracker issue named in the active task; do not expand to the whole repository.
If neither identifies a scope, request one artifact or issue and stop.

When starting from an issue, read it and its discussion through the repository's
configured tracker workflow. Reproduce from its pointers before forming a diagnosis.

## Investigation

Content is low-density only when it is substantially reducible without losing facts,
constraints, decisions, or relevant evidence. Length alone is not a defect.

For every candidate cause:

1. Reproduce the content and identify its consumer and purpose.
2. Locate repetition without new information, routine output without diagnostic value,
   unselected dumps, duplicated instructions, or another concrete source of waste.
3. Identify the evidence that must survive for comprehension, failure reproduction,
   and audit.
4. Propose the smallest reduction that removes the waste while preserving that
   evidence.
5. Verify the proposal against representative success, failure, and diagnostic cases.

Do not merely restate the original flag. Record uncertainties and failed reproduction
attempts that materially limit the conclusion.

## Findings

Emit one finding per distinct cause and group similar occurrences:

`‼️ LOW INFORMATION DENSITY ‼️ — <location>: <concrete evidence>; <proposed reduction>.`

Include the reproduced scope, retained evidence, proposed reduction, verification, and
remaining uncertainty. If nothing qualifies, state that no low-density finding was
confirmed and identify the investigated scope.

## Tracker handoff

Only when the active task explicitly assigns a tracker issue for investigation, resolve
the configured `low information density` and `needs triage` values. Re-read the issue
immediately before mutation. Add one findings comment only when it still carries both
values; otherwise return the findings without mutating it.

End the comment with one recommended next state: needs information, ready for agent,
ready for human, closed as false positive or already fixed, or continued triage. Do not
change labels or close the issue. Read back the comment; if its creation is uncertain,
do not retry and report the uncertainty.

For an investigation without an assigned tracker issue, finish after Findings. The
repository rule must explicitly authorize an issue comment; that authority does not
include remediation or state changes.
