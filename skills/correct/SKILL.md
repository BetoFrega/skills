---
name: correct
description: Make repeated agent mistakes in a repository impossible to repeat, starting from architecture and ending with docs. Use for /correct or when the user corrects the same mistake class again.
disable-model-invocation: true
---

# Correct

Change the repository so the next agent cannot make the mistakes the user keeps
correcting. Assume each contributor is an agent that sees only the files it opened,
copies the nearest example, and takes the shortest path that passes. A change that
looks right from one file must be right for the whole repository.

Apply [Encode Lessons in Structure](../beto-mode/principles/encode-lessons-in-structure.md)
and [Build the Lever](../beto-mode/principles/build-the-lever.md).

## 1. Find the mistake classes

Read recent commits, reverts, review comments, agent instruction files, and comments
that explain workarounds. Group the mistakes into classes. A class counts once it has
happened twice; cite each occurrence.

## 2. Fix each class at the highest level that works

1. **Architecture.** Give each piece of state one owner and each task one supported
   way. Hide internals so the wrong import fails. Replace hand-synced lists with one
   source of truth. Delete old paths and dead code an agent would copy.
2. **Types.** Make the bad state impossible to write.
3. **Lint or CI check.** When bad code still passes, add a check whose error names
   the file, type, or function to use instead. If the pattern is already common, fail
   only when a change adds more.
4. **Test.** Test the behavior the mistake breaks, per
   [Test Behavior, Not Implementation](../beto-mode/principles/test-behavior-not-implementation.md).
5. **Docs or agent rules,** only for judgment calls nothing can check. Put each rule
   in its one canonical place.

## 3. Fix and prove

Fix the most frequent classes first, one commit each. Prove each new check fails on a
real past mistake, then passes on the fix. Run the same command locally and in CI.
An exception goes on the offending line with a reason, an expiry, and the user's
approval.

## 4. Keep the rule table

Keep a table in the repository's agent instruction file pairing each rule with what
enforces it. When the user corrects a mistake whose rule is already there and nothing
enforces it, treat it as a repeat and fix it at a higher level in the same change.
Drop a rule once its mistake can no longer happen.

**Reply:** each class with its evidence, the level chosen, why a higher level did not
work, and the proof that the check fails on the past mistake.
