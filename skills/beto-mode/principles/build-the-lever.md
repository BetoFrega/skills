# Build the Lever

When work is not trivial, build the tool that does or proves it instead of doing it
by hand. A script reruns the same way every time; a reviewer can read and rerun it
instead of trusting a report.

- The bar is triviality, not repetition. Skip the lever only for a couple of obvious
  edits visible at a glance. A one-off still earns one when it makes the work checkable.
- Do the first unit by hand to learn the recipe, then build the tool and prove it by
  rerunning it on that unit and diffing against the hand-done result. Make it safe to
  rerun.
- Pick the smallest lever per Keep It Lean: a codemod or script for edits, a generator
  for repetitive files, a query for analysis, a rerunnable check for verification.
  Never a framework.
- A deterministic lever beats fan-out. When one pass covers every unit, run it
  yourself instead of delegating hand edits.
- When delegates share the work, give them the recipe, the verification contract, and
  the do-not-touch fences in one file outside their write scope.
- Commit the lever when the work outlives the session.

**Check:** citing this principle produces a file. With no script, codemod, generator,
or delegate recipe in the result, the principle was not applied.

Distinct from Encode Lessons in Structure, which turns a recurring correction into a
lasting guardrail; this one is about the work in front of you.
