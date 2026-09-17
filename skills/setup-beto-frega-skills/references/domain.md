# Domain-document consumer rules

Before changing code, read the root `CONTEXT.md`, or the relevant contexts selected by
root `CONTEXT-MAP.md`. Read ADRs under `docs/adr/` and any context-scoped ADR directory
that governs the change. Missing domain files are not a setup failure; domain-modeling
creates them lazily when terminology or a durable decision is resolved.

Use glossary terms consistently. Surface conflicts with an ADR rather than silently
overriding it.

Recommended single-context layout:

```text
CONTEXT.md
docs/adr/
```

Use a root `CONTEXT-MAP.md` with per-context `CONTEXT.md` and ADR directories only for
a repository with genuine, independently modeled contexts.
