---
name: pr
description: "Use when writing a PR body."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

Use this PR-body template:

```markdown
## Summary

<diagram, diff-sketch, or tree>

## Evidence

- **Before:** <screenshot/output/failing test run>
  **After:** <screenshot/output/passing test run>

## Merge Danger

**Door:** <one-way or two-way>

<optional: description>

**Blast Radius:** <one-word description>

<optional: potential ramifications of merge>

## Review Contract

Classify each finding by what merging this PR causes, not by severity:

- **PR Blocker:** the merge introduces or exposes a defect or regression in
  production, including a spec violation. Fix it in this PR; a ticket cannot waive it.
- **Feature Blocker:** the feature violates the spec, but an inactive flag verifiably
  isolates it from production at merge time. Fix it here, or defer it to a ticket that
  blocks release and activation. Until the isolation is verified, approval stays pending.
- **Tech Debt:** significant maintainability cost without a regression. Fix it here,
  or defer it to a ticket.
- **Improvement:** optional. Deferring one the author accepts needs a ticket.

For each finding, give the location, evidence, impact, and smallest fix. Report
concerns you could not confirm as unconfirmed, not as blockers.

If no PR Blocker or Feature Blocker is open, submit the review as APPROVE; Tech Debt,
Improvements, and unconfirmed concerns go in its comments and do not hold the approval.
Otherwise, request changes for an open PR Blocker, or leave approval pending and name
the action a Feature Blocker still needs.
```

## Sections

Keep prose brief, without preambles. Use the user's domain vocabulary from `CONTEXT.md`.

### Summary

Choose the smallest view explaining the change:

- pseudocode for logic/algorithms;
- a call tree for runtime order;
- a component tree for relevant UI state/module boundaries;
- a shallow file tree for responsibility/refactors;
- Mermaid for interactions/control/data flow;
- a diff sketch for changed components, files, calls, or states when surrounding
  structure already exists.

Show a whole block when mostly new, omission hides ownership/order, or the reader
needs a copyable target. Put visuals beside their short explanation. Retain only
calls, files, props, states, and boundaries answering the current question or choice;
combine useful views without overwhelming the reader.

### Evidence

Show concrete before/after evidence. Prefer screenshots for visual changes when the
environment supports them; otherwise use execution evidence, such as tests or output.
For test evidence, show the exact failing/passing case, using pseudocode.

### Merge Danger

State reversibility: two-way doors are cheap to roll back; destructive or hard-to-reverse
choices are one-way doors. Describe the potential scope and ramifications of merging,
including affected consumers, layout, and responsiveness where relevant.

### Review Contract

Copy this section verbatim into every PR body. It tells the reviewer how to classify
findings and which verdict to give, so keep it unchanged even when the PR has no
feature flag.
