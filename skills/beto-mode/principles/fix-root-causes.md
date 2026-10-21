# Fix Root Causes

When debugging, trace each problem to its root cause and fix it there, not at the
symptom. Symptom fixes accumulate and leave the real bug in place.

- Reproduce first.
- Ask "why" until you reach the cause.
- Do not silence a failure with a guard; a null check that hides a crash is a symptom
  fix. Let it fail loudly until the cause is fixed.
- If a workaround needs a long comment to justify it, fix the code instead.
- Fix the pattern, not just the instance: search for the same mistake elsewhere.
- When stuck, instrument instead of guessing: add logging, read the actual error.
- If the deciding fact took a deep dig to find, propose the cheap, always-on signal
  that would have shown it at first look.
- For failures after a restart, suspect stale persistent state (configuration, caches,
  lock files, serialized state) before code.
