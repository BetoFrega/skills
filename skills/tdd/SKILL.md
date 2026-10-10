---
name: tdd
description: Test-first features, bug fixes, integration tests, or red-green-refactor requests at agreed seams.
---

# Test-Driven Development

Apply every section before and during each red → green cycle. Read `CONTEXT.md` when
present and relevant ADRs; use domain vocabulary in tests and interfaces.

## What a good test is

Test behavior through public interfaces. Tests read as specifications and survive
internal rewrites. Consult [tests.md](tests.md) for examples and
[mocking.md](mocking.md) for dependency strategy.

## Seams: where tests go

Test at public seams, never internals. Before writing any test, record seams and
confirm them with the user; reuse prior agreement. Prioritize critical paths and
complex logic instead of exhaustive edge coverage.

When interface shape, module depth, or seam placement is unresolved, consult
[codebase-design](../codebase-design/SKILL.md) as vocabulary reference.

## Anti-patterns

- **Implementation-coupled:** internal mocks, private methods, or side-channel
  verification such as querying storage past the interface; refactors break tests
  without changed behavior.
- **Tautological:** expected values recompute implementation, so assertions cannot
  disagree. Use independent literals, worked examples, or the spec.
- **Horizontal slicing:** all tests before all code locks in imagined behavior.
  Use vertical tracer bullets informed by the previous cycle.

## Rules of the loop

- **Red before green:** fail first; implement only enough to pass, without anticipated
  tests or speculative features.
- **One slice:** one seam, one test, one minimal implementation per cycle.
- **Refactoring:** belongs to [code-review](../code-review/SKILL.md), outside the
  red → green implementation cycle.
