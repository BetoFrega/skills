---
name: codebase-design
description: Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.
---

# Codebase Design

Design deep modules: substantial behaviour behind a small interface, with leverage for callers, locality for maintainers, and testability.

## Vocabulary

Use these terms exactly; avoid unit/component/service, API/signature, and boundary:

- **Module**: scale-agnostic interface plus implementation; exactly one interface for callers and tests.
- **Interface**: everything callers must know: signatures, invariants, ordering, errors, configuration, performance. Broader than a language's interface keyword or public methods.
- **Implementation**: code inside the module. Use this for substance; **Adapter** for role at a seam, regardless of implementation size.
- **Depth**: behaviour accessible per unit of interface learned, never a ratio of code lines. Deep means substantial behaviour behind a small interface; shallow means comparable interface and implementation complexity.
- **Seam** (Michael Feathers): location where behaviour changes without editing there; where the interface lives. Placement is a separate design decision from implementation. Distinct from DDD's bounded context.
- **Adapter**: concrete fulfilment of an interface at a seam.
- **Leverage**: capability gained by callers and tests per unit of interface learned.
- **Locality**: changes, bugs, knowledge, and verification concentrated within the module.

## Principles

- Depth concerns the interface. Internals may contain small, swappable parts and private seams for their tests.
- **Deletion test**: complexity disappearing with the module signals pass-through; complexity reappearing across callers signals value.
- Callers and tests cross the same external seam. Needing tests past that interface suggests redesign; private internal seams remain valid.
- Introduce seams for actual variation: one adapter is hypothetical; two establish reality.
- Accept dependencies, return results rather than mutate through side effects, and keep methods and parameters few.

## Further design

For deepening clusters given dependencies, read [DEEPENING.md](DEEPENING.md): dependency categories, seam discipline, replace-don't-layer testing.

For alternative interfaces, read [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md): parallel agent designs compared on depth, locality, and seam placement.
