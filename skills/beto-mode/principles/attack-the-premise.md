# Attack the Premise

When two or more fixes that share one premise fail the same check, suspect the
premise they share. Each failure is evidence against the assumption they share.

- Write the premise down: the one sentence every failed fix assumed.
- Before the next fix, gather evidence that tests the premise directly, per Build the
  Lever: a rerunnable census, measurement, or reproduction. Rereading the code
  does not test it. For an imbalance, count it per actor to see who holds it.
- If the evidence is skewed (the same actors, inputs, or paths every run), find what
  assigns them that role. That assignment is the next "why" under Fix Root Causes.
- Remove the asymmetry instead of compensating for it. A retry, a rebalance, or a
  return path leaves the cause in place and adds work on every run.
- If the evidence is even, the premise is not the cause. Keep the evidence and look
  elsewhere.

**Stop:** do not write a third fix on the same premise until the premise is written
down and tested. If still stuck, use `advisory`.
