# Domain-document consumer rules

Adapt these consumer rules to the selected documentation destinations, including
external files. Before changing code, read the resolved glossary or the relevant
contexts selected by the resolved context map. Read the ADRs that govern the change
from the selected system-wide and context-scoped directories. Missing domain files
are not a setup failure; domain-modeling creates them lazily when terminology or a
durable decision is resolved.

Use glossary terms consistently. Surface conflicts with an ADR rather than silently
overriding it.

Recommended single-context layout, relative to the selected documentation root:

```text
CONTEXT.md
docs/adr/
```

Use a `CONTEXT-MAP.md` with per-context `CONTEXT.md` and ADR directories only for a
project with genuine, independently modeled contexts. Record actual locations in the
generated configuration; external paths need not mirror the source tree.
