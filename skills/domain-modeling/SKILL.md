---
name: domain-modeling
description: Build and sharpen domain terms and relationships, or write/edit the domain glossary in CONTEXT.md. Reading existing vocabulary alone does not require this skill.
---

# Domain Modeling

Challenge terminology and relationships; capture resolved glossary terms and
architectural choices as they crystallize.

## File structure

Resolve [domain configuration](../setup-beto-frega-skills/references/project-configuration.md),
including external files. Honor configured glossary, context map, and ADR destinations.
Defaults: root `CONTEXT.md` and `docs/adr/` for one context; root `CONTEXT-MAP.md`
identifies multiple contexts, their glossaries, and context-specific ADR locations,
with `docs/adr/` for system-wide choices. Create a glossary at its first resolved
term and an ADR directory at its first record.

## During the session

### Challenge against the glossary

Surface conflicting use immediately: the glossary says X while the discussion means Y.
Resolve the distinction rather than silently changing terminology.

### Sharpen fuzzy language

Propose precise canonical terms for vague or overloaded words.

### Discuss concrete scenarios

Stress-test relationships and concept boundaries with specific edge-case scenarios.

### Cross-reference with code

Check behavioral claims against code; surface contradictions for resolution rather
than treating implementation as approved intent.

### Update CONTEXT.md inline

Capture each resolved term immediately using [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md);
do not batch it. Keep `CONTEXT.md` exclusively a glossary, without implementation
details, specs, scratch notes, or implementation decisions. Report local glossary/map
changes through [document delivery](../consolidate/references/local-document-delivery.md).

### Record architectural decisions

Use [write-adr](../write-adr/SKILL.md) for admission, authoring, format, and updates.

### Product behavior and policy

Read affected canonical contracts through [consolidate](../consolidate/SKILL.md).
For approved rule, permission, state, or exception changes, use its decision and
catalogue routes within session documentation authority. Keep definitions in the
glossary and link behavior to its product authority.
