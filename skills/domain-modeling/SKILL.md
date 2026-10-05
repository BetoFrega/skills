---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology or writing or editing a CONTEXT.md.
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* `CONTEXT.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

## File structure

Resolve the domain-document layout through
[project configuration locations](../setup-beto-frega-skills/references/project-configuration.md),
including project-scoped external files. Follow configured glossary, context-map,
and ADR destinations. The layouts below are defaults for unconfigured repository
documentation; external configuration can select an external documentation root.

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a context map exists at the configured location, the project has multiple contexts.
The default repository map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily at the resolved destinations: the glossary when the first term
is resolved, and the ADR directory when the first record is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up: capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Record architectural decisions

When modeling resolves an architectural choice, use
[`write-adr`](../write-adr/SKILL.md) to determine whether it warrants an ADR and to
write or update the record. That skill owns ADR authoring rules and the format.

### Product behavior and policy

When modeling depends on product behavior, read the affected canonical contracts
through [product-documentation](../product-documentation/SKILL.md). When an approved
choice changes a product rule, actor permission, state, or exception, use its decision
and catalogue routes to record the choice and affected contracts. Preserve vocabulary
definitions in the glossary and link behavior to its product authority.
