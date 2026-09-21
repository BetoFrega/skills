# Standards smell baseline

Use these Fowler-inspired smells as heuristics. A documented repository rule overrides
them. Always label a smell as a judgement call and omit anything tooling already
enforces.

- **Mysterious Name**: a name does not reveal what a function, variable, or type does
  or holds. Rename it; if no honest name emerges, revisit the design.
- **Duplicated Code**: the same logic shape appears in multiple changed hunks or files.
  Extract the shared shape and call it from both places.
- **Redundant Tests**: tests exercise the same behavior and one adds no distinct
  failure signal, boundary, or regression contract. Remove or merge it.
- **Feature Envy**: a method reaches into another object's data more than its own. Move
  the behavior toward the data it uses.
- **Data Clumps**: the same fields or parameters repeatedly travel together. Give the
  group a type.
- **Primitive Obsession**: a primitive stands in for a domain concept. Introduce a
  small domain type when it clarifies invariants.
- **Repeated Switches**: equivalent branching on the same type recurs. Centralize the
  mapping or use polymorphism.
- **Shotgun Surgery**: one logical change requires scattered edits. Gather the changing
  behavior behind one module boundary.
- **Divergent Change**: one module changes for several unrelated reasons. Split the
  responsibilities.
- **Speculative Generality**: an abstraction, option, or hook serves no current
  requirement. Remove it until a concrete need exists.
- **Message Chains**: a caller navigates a long object chain. Hide the navigation
  behind an operation on the owning abstraction.
- **Middle Man**: a type or function mostly delegates without adding a useful boundary.
  Call the underlying behavior directly.
- **Refused Bequest**: an implementation ignores or replaces most inherited behavior.
  Prefer composition over the unsuitable inheritance relationship.
