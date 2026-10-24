# Sequence Verifiable Units

Order work as small units that each end in a state you can check. Do not start the
next unit until the current one passes.

- **Execution.** In a sweep, migration, or run of similar edits, bracket each unit:
  known-good state, one change, run the check, then proceed. Start from a clean,
  current base so every check measures the real baseline. When a lever does the
  edits, run the per-unit check anyway.
- **Delivery.** Order commits and PRs so the sequence proves the work: the failing
  test, then the fix; the subtraction, then the reshape; the baseline, then the
  change; the scaffold, then the feature. Each commit stands on its own.
- A break found at the unit that caused it is cheap to locate. A break found after a
  batch is buried under work built on it.

**Check:** a reviewer can replay the sequence and watch each step go from red to
green, or from baseline to result.
