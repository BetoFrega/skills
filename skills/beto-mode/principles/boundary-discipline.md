# Boundary Discipline

Validate, parse, and handle errors at system boundaries. Trust internal code. Keep
business logic in pure functions behind a thin shell.

- **At boundaries** (CLI arguments, configuration, network, external APIs, storage,
  user input): validate and parse raw data into domain types once, and reject bad
  input loudly per Fail Loud, Handle on Evidence.
- **Inside:** pass typed data, propagate errors, and do not re-validate. A null check
  deep in a call chain that the boundary already guarantees is noise.
- **Across the boundary:** expose domain concepts, not transport, storage, framework,
  or wire types. Keep general mechanism inside and special-purpose policy at the edge.
- **In typed languages:** make illegal states unrepresentable, give semantic
  primitives their own types, and handle every variant instead of casting around the
  compiler.
- Keep logic out of framework wiring so tests can call it without the framework.

**Check:** for each guard, ask "is this data crossing a boundary right now?" If not,
remove the guard. For each handler, ask "can this logic be a pure function the shell
calls?" If so, extract it.
