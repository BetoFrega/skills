# Deepening

Deepen shallow module clusters using [the vocabulary](SKILL.md): module, interface,
seam, adapter.

## Dependency categories

Classify dependencies to choose tests across the deepened module's seam:

| Category | Design and test strategy |
| --- | --- |
| In-process | Pure computation/in-memory state, no I/O: merge and test through the new interface; no adapter needed. |
| Local-substitutable | Use an existing local stand-in, such as PGLite or an in-memory filesystem, in the suite. Deepenable when one exists; the seam stays internal, without an external port. |
| Remote but owned (Ports & Adapters) | Own services across a network: the deep module owns logic behind an injected port; in-memory test adapter and HTTP/gRPC/queue production adapter. |
| True external (Mock) | Third-party services: inject a port and supply a mock adapter in tests. |

## Seam discipline

One adapter is hypothetical; introduce a port only when at least two adapters are
justified, typically production and test. Private seams used by internal tests remain
valid; do not expose them through the external interface.

## Testing strategy: replace, don't layer

Once tests through the deepened interface exist, delete old shallow-module
unit tests. Assert observable outcomes through that interface, not internal state.
Tests describe behavior and survive internal refactors; otherwise they cross past
the interface.
