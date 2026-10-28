---
name: correct
description: Sweep a repository's history for mistakes agents keep repeating and make each one impossible to repeat. Use for /correct as a periodic audit.
disable-model-invocation: true
---

# Correct

Change the repository so the next agent cannot repeat the mistakes the user keeps
correcting. Assume each contributor is an agent that sees only the files it opened,
copies the nearest example, and takes the shortest path that passes.

[Encode Lessons in Structure](../beto-mode/principles/encode-lessons-in-structure.md)
handles a single correction as it happens. This skill finds the ones that slipped
through. Read that principle first; it owns the fix ladder, the proof, the rule table,
and where each fix may go.

## 1. Find the mistake classes

Read recent commits, reverts, review comments, agent instruction files, and comments
that explain workarounds. Group the mistakes into classes. A class counts once it has
happened twice; cite each occurrence.

When a class traces to a skill from an installed plugin, do not edit it: prepare one
issue per class with `report-skill-lesson`.

## 2. Fix and prove

Fix the most frequent classes first, one commit each, at the highest level of the
ladder that works. Prove each new check fails on a real past mistake, then passes on
the fix. Run the same command locally and in CI. An exception goes on the offending
line with a reason, an expiry, and the user's approval.

Update the rule table and drop rules whose mistake can no longer happen.

**Reply:** each class with its evidence, the level chosen, why a higher level did not
work, the proof that the check fails on the past mistake, and any prepared plugin
issues awaiting approval.
