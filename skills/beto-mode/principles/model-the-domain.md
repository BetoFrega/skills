# Model the Domain

Encode the real domain in a data structure instead of scattering it across
conditionals. A fitting structure makes invalid states unrepresentable and deletes
branches; choosing it at write time is cheap, while recovering it later becomes a
deferred refactor.

Reach for the structure that fits:

- A state machine instead of scattered booleans, phases, or lifecycle checks.
- A typed model instead of loose parameters or repeated shape assumptions.
- A map, registry, lookup table, or discriminated union instead of branching spread
  across files.
- A module organized around one body of domain knowledge, not around execution steps
  such as load, validate, transform, and save.

Use the project's domain vocabulary for these structures; see
[domain-modeling](../../domain-modeling/SKILL.md) when terms are unclear.

Do not force an abstraction. Keep boring code when the current shape is clear, local,
and unlikely to grow. Reject indirection that removes no branches, duplicated rules,
or invalid states.

**Signs you skipped this:** a new feature grows an existing if/else chain by one
branch, or a second boolean must stay in sync with the first.
