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
