# Least Surprise

Code should do what a reader expects from its names and shape, and be easy to read
even by a tired developer. Reader effort is the cost to minimize.

- Favor explicitness over implicitness and clarity over cleverness.
- Collapse layers that cost more than they save: wrappers with one caller, adapters
  with no second implementation, pass-through layers that repeat the same methods.
- Shrink state scope: prefer returned values over mutation, locals over fields, and
  derived values over synchronized copies.
- Name an invariant once, at the boundary that owns it, not in every consumer.
- Before adding a layer or a piece of state, check that it removes at least as much
  reader effort elsewhere.

**Check:** a new reader can answer "where does X come from?" and "what can change X?"
quickly. If not, cut layers or state.
