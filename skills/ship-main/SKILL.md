---
name: ship-main
description: Deliver current-task changes to main with validation, automatic reviews, and finding triage.
---

# Ship Main

Invoking this skill authorizes committing, integrating, and pushing the current task
through the repository's permitted route to main, including a required PR and merge.
Take the repository and scope from context and ask only about real ambiguity. Leave
unrelated work alone, inspect the live remote and local state, validate the intended
diff, commit only the task's changes, and integrate against current remote main
without rewriting shared history.

Fix in-scope validation and CI failures, actionable feedback, and routine conflicts,
and rerun the affected checks. Failed checks and requested revisions are part of the
work.

## Automatic reviews and merge gate

For PR delivery, mark the PR ready when it is reviewable. Inspect the repository
configuration and the live PR and provider evidence for reviews that opening, marking
ready, or updating the PR is expected to trigger: requests, checks and statuses,
submitted reviews, comments, and provider state when the PR does not show it.
Establish that each review started and finished for the current target. Passing CI,
silence, or the lack of a pending request do not show that reviews finished. A
missing, failed, or cancelled expected review keeps readiness pending; investigate it
or retry.

After each event that can trigger a review, watch for at least 30 seconds, refreshing
about every 10 seconds and once at the end, and longer for known provider delays.
This window is for discovering reviews; it is not a completion timeout, and an empty
first look clears nothing. Only after the window, if no reviews are configured or
observed, follow the repository's normal review requirements.

Read PR comments, review bodies, and inline threads, including bot feedback outside
required checks. Wait for queued and running reviews, then apply
[review-triage](../review-triage/SKILL.md) to every finding: a verified fix, a
dismissal backed by evidence, or a permitted deferral with a verified ticket and
activation gate. Merge waits until **Ready for approval** covers the full scope, the
current head, and the target base, and the repository's other requirements are met.

After pushing corrections, rebasing, or a base change, repeat discovery, waiting,
reading, triage, fixes, and validation. Earlier findings keep their verified
dispositions, but new runs and findings need their own completion. If automation does
not rerun, get coverage of the changed target through triage. Just before merging,
reread the target, checks, reviews, and comments. Merge only the verified head, with
no expected review outstanding and no finding unaddressed; a target change reopens
the gate. Enable auto-merge only after the gate passes.

## Complete delivery

Pause only for unavailable access, external dependencies, substantive user
decisions, or out-of-scope changes. Try every safe in-scope remedy first. When
progress stops, report the blocker, what you tried, and the smallest action to resume.
Respect branch protections and required checks.

Confirm the remote main revision and report the commit and validation. Deployment,
publication beyond Git, bypassing protections, and archiving need separate authority.

For product changes, reconcile records through [consolidate](../consolidate/SKILL.md)
within existing documentation authority. Record the supported revision, observations,
and remaining gaps. Git delivery shows neither deployment nor audience exposure.

At the final checkpoint, use [next steps](../next-steps/SKILL.md) for remaining
requirements, learning-review triggers, and ready successors. When meaningful
learning or a configured review point warrants it, recommend
[review-learnings](../review-learnings/SKILL.md) with evidence and a bounded scope.
Finish authorized delivery before reporting; recommendations keep their own scope.
Apply [artifact links](../consolidate/references/artifact-links.md) to cited documents
and tickets.
