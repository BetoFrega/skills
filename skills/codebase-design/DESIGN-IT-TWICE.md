# Design It Twice

Use parallel designs when the user wants alternative interfaces for a chosen
deepening candidate. Apply [the vocabulary](SKILL.md) and
[dependency categories](DEEPENING.md).

## Process

### 1. Frame the problem space

Show the user constraints, dependencies/categories, and a rough illustrative code
sketch that makes constraints concrete without proposing a design. Immediately
proceed to dispatch while the user considers it.

### 2. Spawn sub-agents

Spawn at least three parallel agents, each producing a radically different interface.
Give each a separate technical brief: paths, coupling, dependency category, hidden
implementation, and both skill and `CONTEXT.md` vocabulary. Keep these briefs
independent of the user-facing explanation. Assign contrasting constraints:

1. Minimize the interface to 1–3 entry points; maximize leverage per entry point.
2. Maximize flexibility, use cases, and extension.
3. Make the most common caller's default case trivial.
4. When applicable, design around ports/adapters for cross-seam dependencies.

Each returns types/methods/parameters with invariants, ordering, and errors; usage;
hidden implementation; dependency/adapter strategy; and leverage trade-offs.

### 3. Present and compare

Present designs sequentially, then compare depth, locality, and seam placement in
prose. Recommend the strongest design with reasons; propose a hybrid when useful.
