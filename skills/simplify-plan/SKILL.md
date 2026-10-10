---
name: simplify-plan
description: Simplify an implementation or delivery plan using YAGNI and Last Responsible Moment while preserving proportional SOLID design. Use when a plan has speculative abstractions, unnecessary layers, excessive phases, or commitments beyond the next useful increment.
---

# Simplify Plan

Reduce work, dependencies, concepts, and operations for the next usable outcome.
Preserve requirements, accepted decisions, and authority;
flag evidence-based challenges separately.

## Find the necessary work

Read plan evidence, contracts, acceptance criteria, constraints, and failure paths.
Label assumptions; ask only about consequential gaps.

**YAGNI:** justify each mechanism, abstraction, dependency, or phase by a current
requirement or evidenced risk. Remove speculative scale, providers, configuration,
reuse, and features. Prefer existing capabilities or concrete implementations;
avoid shifting complexity into callers or operations. Preserve correctness,
permissions, data integrity, contracts, recovery, and required checks.

## Decide at the Last Responsible Moment

Decide when delivery, option loss, or lead time requires it. Use minimal checks for
potentially invalidating uncertainty. For necessary, cheaply reversible choices,
use simple provisional options within authority. Defer unnecessary commitments with
observable triggers and time for investigation, implementation, and validation.
Remove speculative prerequisites alongside deferred work; out-of-scope ideas create
no backlog promises.

## Preserve proportional SOLID

Keep reasons to change local, established contracts and real variation protected,
substitutions behaviorally compatible, consumer interfaces narrow, and core policy
isolated from volatile dependencies where coupling matters today.

Prefer cohesive modules over pass-through layers. Concrete edits and bounded
duplication are acceptable when abstraction binds unrelated changes. A narrow seam
may serve testing, an external dependency, or required variation with one implementation.
Retain separations preventing scattered dependency details or independently changing
policies from mixing. SOLID does not require classes, interface types,
inheritance, containers, generic repositories, or extension frameworks.

## Return a usable replacement

Lead with the result, dependency order, and verification. Preserve
the vertical slice and acceptance while merging artificial phases. Explain cuts,
retained complexity, deferral triggers, and why waiting is safe;
avoid exhaustive inventories, scoring, or an ADR per cut.

Stop when the increment is executable and verifiable, retained complexity is justified,
and material deferrals have usable triggers. Return the plan in conversation; edit a
plan file only when requested. This grants no implementation, ticket-publication,
or external-change authority.
