---
name: setup-beto-frega-skills
description: "Configure a repository for Beto Frega's engineering skills, including issue tracking, domain documentation, observability, and accessibility baselines. Run explicitly before first use or to fill a missing configuration document."
---

# Setup Beto Frega skills

Scaffold the per-repository configuration consumed by the engineering skills:

- issue-tracker workflow;
- triage-label vocabulary when a triage skill is installed;
- domain-document layout;
- the repository's own observability baseline;
- the repository's own accessibility baseline.

This is an incremental, prompt-driven setup. Preserve existing decisions. Explore,
interview, show complete drafts, obtain confirmation, then write. Invocation authorizes
only this configuration work.

## 1. Explore without writing

Inspect facts the user should not have to supply:

- remotes and `.git/config` for tracker clues;
- root `AGENTS.md` and `CLAUDE.md`, including existing skill pointers;
- `docs/agents/`, `.scratch/`, `CONTEXT.md`, `CONTEXT-MAP.md`, and ADR directories;
- whether a triage skill is installed;
- monorepo signals and context boundaries;
- `OBSERVABILITY.md` and `ACCESSIBILITY.md`, plus any alternate paths explicitly
  declared by repository instructions;
- runtime architecture, deployed services, telemetry libraries, user-facing surfaces,
  UI platforms, and relevant test tooling.

Report what exists, what is missing, and any contradictory pointers. Existing files
are authoritative; ask before changing them.

## 2. Configure only the gaps

Take the applicable sections in order. Skip settled sections unless the user explicitly
asks to revisit them.

### A. Issue tracker

If `docs/agents/issue-tracker.md` is absent, recommend the tracker indicated by the
remote: GitHub, then GitLab, otherwise local Markdown. Also support a user-described
tracker. Use the matching reference as a starting point:

- [GitHub](references/issue-tracker-github.md)
- [GitLab](references/issue-tracker-gitlab.md)
- [Local Markdown](references/issue-tracker-local.md)

Confirm the choice before drafting. Adapt commands and conventions to the repository;
do not claim integrations that were not verified.

### B. Triage labels

Run only when a triage skill is installed and `docs/agents/triage-labels.md` is absent.
Recommend the canonical labels in [the template](references/triage-labels.md). Ask one
question: whether to keep them. Collect overrides only when the answer is no.

### C. Domain docs

If `docs/agents/domain.md` is absent, default to one root `CONTEXT.md` and `docs/adr/`.
Offer multi-context layout only when exploration found real monorepo boundaries. Use
[the domain consumer rules](references/domain.md) as the draft basis. Domain files
themselves remain lazy: do not create an empty `CONTEXT.md` or ADR directory.

### D. Observability baseline

If the authoritative observability document is absent, run the grilling protocol below
with [the observability defaults](references/observability-default.md). Treat defaults
as recommendations, not repository policy. Resolve every applicable branch before
drafting the resolved observability path, defaulting to `OBSERVABILITY.md`.

Base recommendations on inspected architecture and tooling. The interview must settle
scope, critical behavior, signals, correlation, failure reporting, privacy, volume and
cardinality, alert ownership, operational response, verification, and exceptions.

### E. Accessibility baseline

If the authoritative accessibility document is absent, run a separate grilling tree
using [the accessibility defaults](references/accessibility-default.md). Resolve every
applicable branch before drafting the resolved accessibility path, defaulting to
`ACCESSIBILITY.md`.

Base recommendations on inspected product surfaces and platforms. The interview must
settle scope, conformance target, supported interaction and assistive technology,
semantics, visual and motion behavior, content and errors, verification, ownership,
and exceptions.

Do not combine the two trees. For each tree, map every decision and its dependencies.
In each round, ask the complete frontier: all decisions whose prerequisites are already
settled. Number the questions, recommend an answer for each, then wait. Recompute the
frontier from the user's answers. Find repository facts yourself; ask the user only for
decisions. Write nothing until the frontier is empty and the user confirms shared
understanding.

## 3. Confirm complete drafts

Show the complete proposed contents of every file that would change:

- the `## Agent skills` block for the chosen agent-instruction file;
- `docs/agents/issue-tracker.md` when missing;
- `docs/agents/triage-labels.md` when applicable and missing;
- `docs/agents/domain.md` when missing;
- the resolved observability and accessibility paths when missing (defaulting to
  `OBSERVABILITY.md` and `ACCESSIBILITY.md`).

If both `AGENTS.md` and `CLAUDE.md` exist, ask which is canonical. If one exists, use
it. If neither exists, ask which one to create. Update an existing `## Agent skills`
section in place and preserve surrounding user content.

The block contains only applicable pointers, each with a one-line repository-specific
summary. Point directly to the resolved observability and accessibility paths; do not
duplicate their policies in agent instructions. The example below uses the defaults.

Use this shape, omitting only sections that genuinely do not apply:

```markdown
## Agent skills

### Issue tracker
<repository-specific summary>. See `docs/agents/issue-tracker.md`.

### Triage labels
<repository-specific summary>. See `docs/agents/triage-labels.md`.

### Domain docs
<single-context or multi-context summary>. See `docs/agents/domain.md`.

### Observability
<repository-specific scope summary>. See `OBSERVABILITY.md`.

### Accessibility
<repository-specific scope summary>. See `ACCESSIBILITY.md`.
```

Wait for confirmation or edits to the drafts.

## 4. Write and verify

Create only confirmed files and directories. Existing configuration is preserved
unless the user explicitly approved its edit. Check that every pointer resolves, every
generated document describes the actual repository, and no placeholder remains.

Finish by listing created or changed files and the skills that consume them. Tell the
user that the documents can be edited directly later and that setup should be rerun
only to fill another gap or intentionally revisit configuration.
