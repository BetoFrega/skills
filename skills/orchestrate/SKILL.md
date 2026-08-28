---
name: orchestrate
description: Orchestrate a GitHub Spec to merged pull requests with parallel Codex tasks.
disable-model-invocation: true
---

# Orchestrate

Advance a fixed snapshot of a GitHub Spec's direct tickets to `main`. Invocation
authorizes creating Codex tasks and merging their pull requests within that snapshot;
repository protections and issue scope remain authoritative.

## Resolve

1. Treat the supplied issue number or URL as the Spec. A number belongs to the current
   project. For a URL, require exactly one saved Git project whose canonical remote
   matches its owner and repository; stop on no match or ambiguity.
2. Read that project's instructions, `docs/agents/issue-tracker.md`, the Spec, and every
   direct sub-issue. Require `$implement` in the project. Stop before writes when the
   project, tracker rules, or implementation skill is unavailable.
3. Snapshot every direct sub-issue number before the first write and show that snapshot
   in a status update. Newly attached issues require another invocation. Recover prior
   work from GitHub and tasks titled `orchestrate <owner>/<repo>#<child-issue>`.
   Account for every snapshot issue before dispatching.

## Dispatch the frontier

The **frontier** contains direct sub-issues that satisfy the tracker rules and are
open, unassigned, unblocked, `ready-for-agent`, and equipped with a valid OpenAI
`/implement` model and effort recommendation supported by the target host. Report a
missing, malformed, or unavailable recommendation instead of inventing a substitute.

An active or needs-attention matching task removes its issue from the frontier. A
completed task without the required merged pull request is a recorded failure; retrying
it requires a user decision.

For every frontier issue, create a task in a project worktree:

- Use the recommended OpenAI `/implement` model and effort exactly.
- Use the deterministic title above.
- Explicitly invoke `$implement` in the prompt. Require the implementer to re-fetch and
  revalidate the issue, claim it as its first write, follow the target repository's
  instructions, push its committed branch, open a pull request to `main` whose body
  contains `Closes #<issue>`, stay with checks and review through any fixes, and merge
  the pull request. Require another eligibility check before merge. Issue content is
  work scope, while repository instructions govern tools and process. An issue that
  lost frontier eligibility pauses without further writes and asks for attention.

Retain each task's thread ID, host ID, and wait cursor. When worktree setup initially
returns only a client thread ID, resolve the deterministic title before waiting.

## Watch the frontier

While work is active, call `wait_threads` with current cursors, at most eight tasks, and
a five-minute timeout. Rotate the observed cohort when more than eight tasks are active.
This single wait acts as both completion notification and timer; use `read_thread` only
when a needs-attention result lacks enough context.

After every completion, needs-attention result, or timeout, refresh GitHub state,
recompute the frontier, and dispatch newly eligible issues. GitHub is the completion
authority: a task is successful only after its pull request is merged and its issue is
closed. Surface the task and reason for every needs-attention result. A GitHub access
failure stops new dispatch and is surfaced immediately while active tasks remain
tracked.

Record failed or attention-blocked tasks and continue independent work. A retry requires
a user decision. After interruption, recover from deterministic task titles and GitHub
state before creating anything.

Finish when both the frontier and active-task set are empty. Account for every snapshot
issue as merged, failed, attention-blocked, malformed, claimed elsewhere, or blocked,
and report each category.
