---
name: orchestrate
description: Orchestrate an explicit GitHub ticket workset through parallel Codex tasks.
disable-model-invocation: true
---

# Orchestrate

Advance a GitHub ticket workset to `main`. Invocation authorizes creating Codex tasks
and merging their pull requests only within the user-selected workset; repository
protections and issue scope remain authoritative.

## Require the workset

Before any project or GitHub lookup, require the current request to state exactly one
membership mode and one selector. The user's explicit words are the sole authority. If
either choice is missing or ambiguous, ask the user and stop; perform no lookup or
write. Never infer a choice from the selector, repository state, history, or prior run.

Membership modes:

- `frozen`: evaluate the selector once before the first write and retain that exact
  membership for the run.
- `dynamic`: evaluate the selector initially and after every completion,
  needs-attention result, or wait timeout. Admit newly selected tickets and remove
  tickets that leave the selection before dispatch. Dispatch is the commitment
  boundary: continue tracking a dispatched ticket to a terminal result even if it
  later leaves the selection.

Selectors:

- `spec <issue>` selects the Spec's direct sub-issues.
- `filter <filter>` selects every result of the supplied GitHub issue-search query or
  URL, exhausting pagination and removing duplicates.
- `ticket <issue>` selects that issue alone. Its membership is stable, but its mode is
  still required.

## Resolve

1. Resolve exactly one saved Git project. An unqualified issue number or filter belongs
   to the current project. An issue URL or repository-qualified filter must match the
   project's canonical remote; stop on no match, ambiguity, or cross-repository filter
   results.
2. Read that project's instructions, `docs/agents/issue-tracker.md`, the selector source,
   and every currently selected ticket. Require `$implement` in the project. Stop before
   writes when the project, tracker rules, selector, or implementation skill is
   unavailable.
3. Evaluate the selector according to its mode. Before the first write, show the mode,
   canonical selector identity, repository, and complete current membership in a status
   update.
4. Recover prior work from GitHub and tasks titled
   `orchestrate <owner>/<repo>#<ticket-issue>`. Use the canonical mode and selector
   identity recorded in each task prompt to recover dispatched tickets that no longer
   match a dynamic selector. Keep a ledger containing every ticket admitted or
   dispatched during this run, and account for the ledger before dispatching. A valid
   empty membership with no recovered active task finishes without writes.

## Dispatch the frontier

The **frontier** contains current workset tickets that satisfy the tracker rules and
are open, unassigned, unblocked, `ready-for-agent`, and equipped with a valid OpenAI
`/implement` model and effort recommendation supported by the target host. Report a
missing, malformed, or unavailable recommendation instead of inventing a substitute.

An active or needs-attention matching task removes its issue from the frontier. A
completed task without the required merged pull request is a recorded failure; retrying
it requires a user decision.

For every frontier issue, create a task in a project worktree:

- Use the recommended OpenAI `/implement` model and effort exactly.
- Use the deterministic title above.
- Record the canonical mode and selector identity in the prompt.
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

After every completion, needs-attention result, or timeout, refresh GitHub state. For a
dynamic workset, fully re-evaluate the selector and update membership at this point; for
a frozen workset, retain its original membership. Then recompute the frontier and
dispatch newly eligible issues. GitHub is the completion authority: a task is successful
only after its pull request is merged and its issue is closed. Surface the task and
reason for every needs-attention result. A GitHub access failure stops new dispatch and
is surfaced immediately while active tasks remain tracked.

Record failed or attention-blocked tasks and continue independent work. A retry requires
a user decision. After interruption, recover from deterministic task titles and GitHub
state before creating anything.

Finish when both the frontier and active-task set are empty. Before finishing a dynamic
run, perform one final complete selector evaluation and continue if it admits a new
frontier ticket. Account for every ledger ticket as merged, failed, attention-blocked,
malformed, claimed elsewhere, blocked, or removed before dispatch, and report each
category. The finished run does not monitor for later changes.
