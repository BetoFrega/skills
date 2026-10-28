---
name: beto-mode
description: Read first for multi-step, design, implementation, debugging, planning, or review work. Routes the task to working principles and workflow skills.
---

# Beto mode

Route the task to the principles and workflow skills it triggers. Global rules keep
authority over decisions and permissions; nothing here overrides them.

## Principles

Read a principle's file in full before applying it. In the reply, name each principle
that shaped a decision and the specific choice it changed. Cite only principles whose
file you read in this session; a name with no decision behind it is name-dropping.

Each entry says when it applies. Files live at `principles/<name>.md`.

- **Keep It Lean** (`keep-it-lean`). Scoping a change, choosing a design, or tempted
  to add an abstraction, option, dependency, or optimization.
- **Subtract Before You Add** (`subtract-before-you-add`). Adding to an existing area,
  refactoring, migrating, or simplifying a plan or document. Remove first, then build.
- **Least Surprise** (`least-surprise`). Writing or reviewing code someone must read,
  trace, or change.
- **Fail Loud, Handle on Evidence** (`fail-loud-handle-on-evidence`). Deciding which
  failures, edge cases, or concurrency risks the code handles; writing briefs, plans,
  or review findings about them.
- **Boundary Discipline** (`boundary-discipline`). Wiring validation, parsing, error
  handling, or framework adapters, or designing types and signatures.
- **Security by Design** (`security-by-design`). Touching a trust boundary: untrusted
  input, authentication, authorization, secrets, personal data, permissions, or a new
  dependency or network exposure.
- **Fix Root Causes** (`fix-root-causes`). Debugging a failure or regression.
- **Attack the Premise** (`attack-the-premise`). Two or more fixes sharing one premise
  have failed the same check.
- **Test Behavior, Not Implementation** (`test-behavior-not-implementation`). Writing,
  changing, or keeping a test.
- **Model the Domain** (`model-the-domain`). Writing stateful logic, or code that
  branches a lot or repeats a shape assumption across files.
- **Migrate Callers, Then Delete Legacy** (`migrate-callers-then-delete-legacy`).
  Introducing a new internal API while old callers exist.
- **Price the Experiment** (`price-the-experiment`). Tempted to prototype, spike, or
  measure before deciding.
- **Don't Spend Avoidable Time** (`dont-spend-avoidable-time`). Choosing between paths,
  sequencing work, or deliberating longer than the next step needs.
- **Build the Lever** (`build-the-lever`). Any non-trivial edit, migration, analysis,
  or check that a script, codemod, or generator could do or prove.
- **Sequence Verifiable Units** (`sequence-verifiable-units`). Multi-step work, sweeps,
  migrations, or ordering commits and PRs.
- **Encode Lessons in Structure** (`encode-lessons-in-structure`). Writing the same
  instruction a second time, or meeting a recurring correction.
- **Evidence Before Claims** (`evidence-before-claims`). Reporting a result, status, or
  completion, or judging whether something works or is feasible.
- **One Canonical Record** (`one-canonical-record`). Writing or updating a decision,
  rule, term, or other fact that may already be recorded elsewhere.
- **Separate Documented From Inferred** (`separate-documented-from-inferred`). Writing
  a spec, record, brief, explanation, or citation, or meeting a missing detail.

## Routes

Match the situation and use the named skill. Skip a route whose result already exists
in settled decisions or records.

**Clarify the problem**

- Selected plan or idea with consequential open questions → `grilling`.
- Question needing trustworthy external evidence → `research`.
- Approach depending on platform capabilities → `check-feasibility`.
- Design question a small throwaway build can answer → `prototype`, after
  Price the Experiment.
- Ambiguous or changing terms → `domain-modeling`.

**Decide**

- Several viable alternatives → `recommend`; one pending decision → `decide`.
- Approved decision to preserve → `record-decision`; architectural → `write-adr`.
- Risk of committing too early or deferring too long → `last-responsible-moment`.

**Plan**

- Scattered confirmed knowledge → `consolidate`.
- Selected outcome needing slices and tickets → `plan-increment`.
- Plan with speculative parts → `simplify-plan`.
- Migration → `migration-planning`.

**Build**

- Module boundaries and seams → `codebase-design`; test-first work → `tdd`.
- Hard bug or performance regression → `diagnosing-bugs`.
- Stuck, repeated errors, or a consequential diagnosis → `advisory`.
- Delegating work → `model-selection`; in Claude, spawn delegates as the
  `beto-frega-skills:beto-agent` subagent.

**Review and deliver**

- Review a change → `code-review`; triage its findings → `review-triage`.
- PR body → `pr`; deliver to main → `ship-main`; confirm a claimed outcome → `verify`.
- Remaining work and successors → `next-steps`; learning from results →
  `review-learnings`.

**Instructions**

- Creating or editing skills, `AGENTS.md`, or `CLAUDE.md` → `writing-for-agents`.
- The user corrects the same mistake class again → suggest `/correct`.
