# Migrate Callers, Then Delete Legacy

Once a new internal API is the chosen design, migrate every caller and delete the old
API in the same wave. Do not keep both paths because internal callers still exist.

- Inventory callers, preferably with a rerunnable search or codemod per Build the
  Lever, migrate them, and delete the old API.
- A temporary adapter is an exception: state its removal condition and owner.
- Update tests to assert the new contract; delete tests that only protect the old
  implementation.
- Intermediate breakage inside a planned migration is acceptable when its scope is
  declared and the end state is fully verified.

Applies when no external consumer depends on the old API and the project can absorb a
coordinated change. With external or deployed consumers, use `migration-planning`.

**Check:** after the wave, a search for the old API returns nothing outside history.
