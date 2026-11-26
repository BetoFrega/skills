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

<one sentence: the change and why it is needed>

<diagram, diff-sketch, or tree>

## Where to Look

<omit for a small single-purpose PR>

**Needs judgment:**

- `<path:lines>`: <the choice, risk, or trade-off>; <what to check>

**Mechanical:** <renames, moves, generated files, formatting, version bumps>; skim.

## Evidence

- **Before:** <screenshot/output/failing test run>
  **After:** <screenshot/output/passing test run>

## Merge Danger

**Door:** <one-way or two-way>

<optional: description>

**Blast Radius:** <one-word description>

<optional: potential ramifications of merge>

<optional, only if the user says yes:>
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

Open with one sentence that joins the change to its why, per Start With the Why in
`beto-mode`. Mark an inferred why as inferred.

Then choose the smallest view explaining the change:

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

### Where to Look

Point the reviewer's attention where human judgment changes the outcome: risky
logic, design choices, non-obvious trade-offs, security or data boundaries, and
anything you are unsure of. Order items by risk, and give each a location, the
reason it needs judgment, and the question the reviewer should answer. Name
rejected alternatives only when they explain the choice.

List mechanical, low-risk changes separately, grouped by kind with paths or globs,
so the reviewer can skim them. When a mechanical group hides one real change, move
that change to Needs judgment.

Include this section when the PR spans several concerns or more files than a
reviewer reads at once; the larger the PR, the more it matters. Omit it for a small
single-purpose PR, where the Summary already shows where to look.

### Evidence

Show concrete before/after evidence. Prefer screenshots for visual changes when the
environment supports them; otherwise use execution evidence, such as tests or output.
For test evidence, show the exact failing/passing case, using pseudocode.

### Merge Danger

State reversibility: two-way doors are cheap to roll back; destructive or hard-to-reverse
choices are one-way doors. Describe the potential scope and ramifications of merging,
including affected consumers, layout, and responsiveness where relevant.

### Review Contract

Before writing the body, ask the user whether to include the Review Contract. It
tells the reviewer how to classify findings and when to approve. If the user says
yes, copy it verbatim, even when the PR has no feature flag; otherwise leave it out.
