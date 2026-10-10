---
name: code-review
description: Review branch, PR, or in-progress changes from a commit, branch, tag, or merge-base across standards, spec, performance, observability, and accessibility.
---

# Five-axis code review

Review `HEAD` against one fixed point. Keep **Standards**, **Spec**, **Performance**,
**Observability**, and **Accessibility** independent: each applicable axis gets an
isolated reviewer, and findings retain their originating axes.

## 1. Pin the comparison

Use the user's fixed point. Otherwise infer the target from repository evidence:
PR base, documented target, then default branch. Use its merge-base with `HEAD`;
without a target use `HEAD^`, or the empty tree for a root commit. State the inferred
point and evidence; do not ask the user to select it.

Resolve the ref with `git rev-parse <fixed-point>` and capture once:

```text
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Three-dot diff compares `HEAD` with the merge-base. For the root-commit exception,
obtain the empty tree with `git hash-object -t tree /dev/null`, then use
`git diff <empty-tree> HEAD` and `git log HEAD --oneline`; a tree has no merge-base.
Stop on an invalid ref or empty diff.

## 2. Require repository configuration

Read repository instructions and resolve applicable sources, including external
project files, through [project configuration locations](../setup-beto-frega-skills/references/project-configuration.md).
Require the tracker, observability, and accessibility configuration; defaults:

- `docs/agents/issue-tracker.md`
- `OBSERVABILITY.md`
- `ACCESSIBILITY.md`

If any is absent, stop before dispatch, list gaps, and suggest explicit
`$setup-beto-frega-skills`. Do not invoke setup autonomously or invent a baseline.
Read the resolved domain-layout document when present and its relevant context/ADR
pointers. Repository rules override generic heuristics.

Read optional `PERFORMANCE.md` or its normative replacement when present. It can add
critical paths, workloads, budgets, benchmarks, and acceptance rules; its absence
never blocks Performance review or removes the universal baseline.

## 3. Resolve the spec

Follow the configured tracker. Search in order:

1. Issue/MR references in the captured commit list.
2. User-supplied spec path or issue.
3. Matching files in `docs/`, `specs/`, or `.scratch/`.
4. PR metadata when the branch identifies a PR.

Ask only after exhausting repository evidence. User-confirmed absence makes Spec
`N/A — no spec available`.
For product behavior, read canonical functionality, shared rules, accepted decisions,
and approval evidence through [consolidate](../consolidate/SKILL.md). Check the spec
against these contracts and approval evidence. Tickets/specs do not themselves
establish release or policy authority.

## 4. Resolve standards

Read applicable `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, scoped standards, and
[the smell baseline](references/standards-smells.md). Repository rules override smells;
omit findings for tooling-enforced rules.

## 5. Dispatch isolated reviewers

Read [review-triage](../review-triage/SKILL.md) for classification, follow-up tickets,
and approval. Use [model-selection](../model-selection/SKILL.md) for each assignment;
disclose each concrete model, effort, and substitution before or alongside dispatch.
Run reviewers concurrently within capacity; queue others. Never combine axes.

Give every reviewer the fixed point, exact diff/log commands, changed files,
repository instructions, and authoritative sources. Paste review-triage's
classification and feature-isolation evidence requirements in full. Require:

- classification, location, evidence, impact, smallest credible correction;
- at most 400 words, ordered by triage classification;
- only actionable findings introduced or materially exposed by the diff; no praise,
  pass lists, or speculative hardening;
- findings, `No findings`, or `N/A — <evidence-backed reason>`.

### Standards reviewer

Provide all standards and paste the smell baseline in full. Cite file and controlling
rule for breaches. Smells are judgement calls, never hard requirements: name the
smell and cite the changed hunk.

### Spec reviewer

Provide spec path and contents. Find missing/partial requirements, unrequested scope,
and incorrect apparent compliance; quote or precisely cite the controlling passage.

### Performance reviewer

Provide the spec, [universal baseline](references/performance-baseline.md) in full,
repository performance sources, and available author acknowledgements from chat,
PR, issue, or spec. Return `N/A` only if runtime, build, tests, distribution, and
feedback loops are all unaffected; `No findings` requires an applicable review.
Apply relevant rules, cite controlling rule and hunk, preserve baseline evidence and
acknowledgement labels, and explain the complete causal mechanism. Use
`Author acknowledgement: Not found` only after checking supplied and other accessible
acknowledgement sources.

### Observability reviewer

Provide the complete repository baseline. Check applicability to runtime behavior,
failure modes, operational dependencies, or diagnostics. Examine lost failure
visibility, unusable context/correlation, unsafe data, unbounded cardinality/volume,
and unverifiable operation. Cite an actual baseline rule for every finding.

### Accessibility reviewer

Provide the complete repository baseline. Check applicability to user-facing surfaces,
content, interaction, accessibility APIs, or assistive technology. Review the whole
journey, states, and errors against applicable rules; cite each controlling rule.
Automated checks do not prove requirements needing human or assistive verification.

## 6. Triage findings and determine approval readiness

Apply review-triage to validate dispositions and verify resolutions/required tickets
within active authorization. Group by classification, retaining axes and distinct
aspects of shared issues. Preserve reviewer meaning; clean wording lightly.
Report counts, approval readiness, outstanding actions, and activation gates.
