---
name: code-review
description: "Review changes since a fixed point along five independent axes: repository standards, originating spec, performance, observability, and accessibility. Use for branches, pull requests, work in progress, or requests to review since a commit, branch, tag, or merge-base."
---

# Five-axis code review

Review `HEAD` against one fixed point. Keep the axes independent so strength in one
cannot hide failure in another:

- **Standards**: repository rules plus the heuristic smell baseline below.
- **Spec**: fidelity to the originating requirement.
- **Performance**: concrete regression risks, measured regressions, and consciously
  accepted performance trade-offs.
- **Observability**: fidelity to the repository's operational baseline.
- **Accessibility**: fidelity to the repository's accessibility baseline.

Each applicable axis gets an isolated reviewer. Preserve the axes when grouping
their findings by classification.

## 1. Pin the comparison

Use the fixed point supplied by the user. Otherwise infer it from repository
evidence: prefer the pull request's base branch, then a documented target
branch, then the repository's default branch.
Use their merge-base with `HEAD` as the fixed point. If no target branch can be
identified, use `HEAD^`; for a root commit, use the empty tree. State the
inferred point and the evidence for choosing it in the review. Do not ask the
user to choose the comparison point.

Resolve it with `git rev-parse <fixed-point>`, then capture these exact views once:

```text
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

The three-dot diff compares `HEAD` with the merge-base. Stop on an invalid ref or an
empty diff.

## 2. Require repository configuration

Read repository instructions first. Use
[project configuration locations](../setup-beto-frega-skills/references/project-configuration.md)
to resolve applicable configuration, including project-scoped external files.
Require all three sources, using these defaults when no replacement is configured:

- `docs/agents/issue-tracker.md`
- `OBSERVABILITY.md`
- `ACCESSIBILITY.md`

If any source is absent, stop before review dispatch, list the missing sources, and
suggest that the user explicitly invoke `$setup-beto-frega-skills`. Do not invoke the
setup skill autonomously and do not substitute an implicit baseline.

Read the resolved domain-layout document when present, then follow its pointers to
relevant context and ADR files. Existing repository rules override generic review
heuristics.

`PERFORMANCE.md` is optional. Read it, or an explicit normative pointer that replaces
it, when present. It may add critical paths, representative workloads, budgets,
benchmarks, or acceptance rules; its absence never blocks the Performance review. The
universal performance baseline still applies.

## 3. Resolve the spec

Follow the resolved issue-tracker workflow. Look in this order:

1. Issue or merge-request references in `git log <fixed-point>..HEAD --oneline`.
2. A spec path or issue supplied by the user.
3. A matching file under `docs/`, `specs/`, or `.scratch/`.
4. Pull-request metadata when the current branch identifies a pull request.

Ask for the source only after exhausting repository evidence. If the user confirms
there is no spec, mark the Spec axis `N/A — no spec available`.

For product behavior, read the referenced canonical functionality, shared rules, and
accepted decisions through [consolidate](../consolidate/SKILL.md).
Check the spec's intended change against the contract and its approval evidence. A
ticket or spec does not by itself establish release or policy authority.

## 4. Resolve standards

Find repository documents that govern changed code, such as `AGENTS.md`, `CLAUDE.md`,
`CONTRIBUTING.md`, and scoped coding standards. Also read
[the smell baseline](references/standards-smells.md). Repository rules override the
baseline, and tooling-enforced rules do not need manual findings.

## 5. Dispatch isolated reviewers

Read [review-triage](../review-triage/SKILL.md), the authoritative classification,
follow-up ticket, and approval policy shared with other review workflows.

Use `model-selection` for each review assignment. Before or alongside dispatch, tell
the user the concrete model and reasoning effort for every reviewer, including any
substitution. Start as many reviewers concurrently as capacity permits and queue the
rest; never combine axes in one reviewer context.

Give every reviewer:

- the fixed point, full diff command, and commit-list command;
- the changed-file list and applicable repository instructions;
- its authoritative source documents or contents;
- this finding format: classification, location, evidence, impact, and smallest credible correction;
- the classification rules and feature-isolation evidence requirements from
  review-triage; paste them in full into each isolated reviewer context;
- a limit of 400 words, findings ordered by review-triage's classification order;
- the constraint to report only actionable findings introduced or materially exposed
  by the diff, without praise, pass lists, or speculative hardening.

Each reviewer returns one of:

- findings;
- `No findings`;
- `N/A — <brief evidence-backed reason>` when the axis does not apply.

Use these axis briefs:

### Standards reviewer

Provide every standards source and paste the smell baseline in full. Report documented
rule breaches with a file-and-rule citation. Label smell findings as judgement calls,
name the smell, and cite the changed hunk. Repository rules can be hard requirements;
smells never are.

### Spec reviewer

Provide the spec path and contents. Report missing or partial requirements, unrequested
scope, and implementation that appears to satisfy a requirement incorrectly. Quote or
precisely cite the controlling spec passage for each finding.

### Performance reviewer

Provide the spec, [the universal performance baseline](references/performance-baseline.md)
in full, any repository performance source, and every available author-authored
acknowledgement from the current chat, pull request, issue, or spec. First determine
whether the diff changes runtime, build, tests, distribution, or a development
feedback loop. Return `N/A` when it changes none of them; return `No findings` only
after reviewing an applicable change.

Apply every relevant baseline and repository rule. Cite the changed hunk and controlling
rule, preserve the baseline's evidence and acknowledgement labels, and give the user
the complete causal explanation rather than leaving the mechanism for them to infer.
Use `Author acknowledgement: Not found` only after checking the supplied evidence and
other acknowledgement sources accessible in the reviewer context.

### Observability reviewer

Provide the complete authoritative observability document. First determine whether the
diff changes runtime behavior, failure modes, operational dependencies, or diagnostic
paths. Apply every relevant repository requirement. Look especially for lost failure
visibility, unusable signal context or correlation, unsafe data exposure, unbounded
cardinality or volume, and operational behavior that cannot be verified. Cite the
specific baseline rule for every finding; do not invent requirements absent from it.

### Accessibility reviewer

Provide the complete authoritative accessibility document. First determine whether the
diff changes a user-facing surface, content, interaction, accessibility API, or
assistive-technology behavior. Apply every relevant repository requirement across the
whole affected journey, including states and errors. Cite the specific baseline rule
for every finding; do not treat automated checks as proof of requirements that need
human or assistive-technology verification.

## 6. Triage findings and determine approval readiness

Apply review-triage to the collected reports: validate classifications, verify
resolutions and required follow-up tickets within the active task's authorization,
and report findings grouped by classification with their originating axes.
Preserve each reviewer's meaning and distinct aspects of the same issue; lightly
clean wording only. Include finding counts, approval readiness, outstanding
actions, and any feature activation gates as specified by review-triage.
