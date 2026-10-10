---
name: orchestrate
description: Advance an explicitly selected GitHub ticket workset through parallel Codex tasks.
---

# Orchestrate

Advance the selected workset to `main`. Invocation authorizes Codex task creation
and PR merges within that workset; repository protections and issue scope govern.

## Require the workset

Before project/GitHub lookup, require the current request to explicitly provide one
membership mode and selector. Missing/ambiguous choices: ask and stop without lookup
or write. Infer neither from repository state, history, selector, nor prior runs.

| Mode | Membership |
| --- | --- |
| `frozen` | Evaluate once before the first write; retain exact membership. |
| `dynamic` | Evaluate initially and after completion, attention, or timeout. Admit new matches; remove departed tickets before dispatch. Continue dispatched tickets to terminal results even after departure. |

| Selector | Selection |
| --- | --- |
| `spec <issue>` | Spec's direct sub-issues. |
| `filter <filter>` | Every GitHub search-query/URL result; exhaust pagination, deduplicate. |
| `ticket <issue>` | One issue; mode still required despite stable membership. |

## Resolve

1. Resolve one saved Git project. Unqualified numbers/filters use the current project;
   issue URLs or qualified filters must match its canonical remote. Stop on missing
   or ambiguous matches or cross-repository results.
2. Read project instructions and [project configuration locations](../setup-beto-frega-skills/references/project-configuration.md),
   including scoped external files, tracker workflow, selector source, and every
   selected ticket. Require `$implement`; missing project, tracker rules, selector,
   or skill stops writes.
3. Before the first write, show mode, canonical selector identity, repository, and
   complete current membership.
4. Recover GitHub work and tasks titled `orchestrate <owner>/<repo>#<ticket-issue>`.
   Match recorded canonical mode/selector prompts to recover dispatched tickets
   that left dynamic membership. Maintain and reconcile a ledger of every admitted
   or dispatched ticket before dispatch. Empty membership with no recovered active
   task finishes without writes.

## Dispatch the frontier

Frontier tickets meet tracker rules and are open, unassigned, unblocked,
`ready-for-agent`, with a valid host-supported OpenAI `/implement` model/effort
recommendation. Report missing, malformed, or unavailable recommendations; substitute
nothing. Matching active/attention tasks leave the frontier. Completed tasks without
the required merged PR are failures; retry requires a user decision.

Create one project-worktree task per frontier ticket, using the recommended model
and effort exactly and deterministic title above. Include canonical mode/selector,
configuration entry and external document locations. Explicitly invoke `$implement`.
Require the implementer to:

- Re-fetch/revalidate the issue and claim it as its first write.
- Follow repository instructions for tools/process and issue content for scope.
- Push its committed branch; open a PR to `main` containing `Closes #<issue>`.
- Stay through checks, review, and fixes; recheck eligibility, then merge the PR.
  Lost eligibility pauses further writes and requests attention.

Retain thread ID, host ID, and wait cursor. If setup returns only a client thread ID,
resolve the deterministic title before waiting.

## Watch the frontier

Use `wait_threads` with current cursors, cohorts of at most eight, and the longest
supported timeout up to five minutes. Rotate larger worksets. Read a thread only
when an attention result lacks context.

After completion, attention, or timeout, refresh GitHub; fully re-evaluate dynamic
selectors, retain frozen membership, recompute the frontier, and dispatch eligible
work. GitHub establishes success: merged PR and closed issue. Surface each attention
task/reason. Surface GitHub access failure immediately, stop new dispatch, and track active tasks.

Record failures/attention blocks and continue independent work. Retry needs a user
decision. After interruption, reconcile task titles and GitHub state before creation.

Finish only with empty frontier and active-task sets. Dynamic runs require a final
complete selector evaluation; continue if it adds frontier tickets. Report every
ledger ticket as merged, failed, attention-blocked, malformed, claimed elsewhere,
blocked, or removed before dispatch. Completion does not monitor later changes.
