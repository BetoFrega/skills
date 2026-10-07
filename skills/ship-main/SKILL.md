---
name: ship-main
description: Fix validation failures, complete automatic review cycles, triage findings, and deliver the current task's changes to main.
---

# Ship Main

Treat this explicit invocation as authorization to commit and integrate the current task's changes into the repository's main branch and push it. Identify the repository and intended changes from context; clarify only if either is ambiguous.

Inspect current remote state and local changes, preserve unrelated work, and run checks appropriate to the intended diff. Commit only the task's changes, integrate against current remote main without rewriting shared history, and push through the repository's permitted delivery route, creating or updating a pull request and merging it when required.

Carry delivery through to completion: diagnose and fix validation or CI failures within scope, address actionable review feedback, resolve routine integration conflicts, and rerun affected checks after changes. Treat a failed check or requested revision as work to complete, not an automatic stopping condition.

When delivery uses a pull request, move it out of draft when ready for review. Inspect repository review configuration and live PR evidence to determine which automatic reviews opening, marking ready, or updating it triggered or should trigger. Check review requests, check runs/statuses, submitted reviews, and reviewer comments; consult the review provider when its state is not exposed on the PR. Establish whether each expected review started and completed for the current review target. Passing CI, no comments, or no pending review request does not prove automatic reviews are complete. A missing expected result or failed/cancelled review keeps readiness pending; investigate and retry within scope.

Review startup can lag the triggering event. Cover at least the first 30 seconds after each potential trigger, refreshing review activity roughly every 10 seconds and once at the end; extend this window for known provider delays. An empty initial response is not evidence that no review was triggered. This window discovers new reviews; it is not a completion timeout and cannot clear an expected review with a missing result. Only after this discovery window, if no automatic reviews are configured or observed, follow the repository's normal review requirements.

Read PR-level comments, submitted review bodies, and inline review threads, including bot feedback outside required checks. Wait for queued or running reviews to finish, then apply [review-triage](../review-triage/SKILL.md) to every finding. Verify fixes, evidence-backed dismissals, and any permitted deferral with its required verified tickets and activation gates. Merge remains pending until triage reports **Ready for approval** for the full intended scope at the current head and target base, and the repository's other merge requirements are satisfied.

After every correction push, rebase, or target-base change, rediscover automatic review activity and repeat the wait, read, triage, fix, and validation cycle. Corrections can trigger new reviews; earlier completion does not clear new runs or findings, and earlier findings still need verified disposition. If automation does not rerun, obtain the review coverage needed for the changed target under that triage process. Immediately before merging, re-read the current review target, checks, review activity, and comments. Merge only the verified head with no outstanding expected review or unaddressed finding under triage; if the target changes, repeat the gate. Do not enable auto-merge before this gate is satisfied.

Pause only when progress requires unavailable access, an external dependency, a substantive user decision, or changes beyond the authorized task. First exhaust safe remedies within scope; if attempts cease making progress, report the specific blocker, attempted remedies, and the smallest action needed to resume. Honor repository protections and required checks throughout.

Confirm the remote main revision and report the delivered commit and validation. This invocation does not authorize deployment, publication beyond the Git delivery, bypassing protections, or archival.

When this task changes product behavior, reconcile affected product records through
[consolidate](../consolidate/SKILL.md) within the task's existing
documentation authority. Use the verified revision and supported observations;
Git delivery alone does not establish deployment or audience exposure. Account for
remaining documentation gaps in the delivery report.

At the final delivery checkpoint, use [next steps](../next-steps/SKILL.md) to identify
remaining requirements, learning-review triggers, and ready successor work. When
meaningful learning or a configured review point warrants it, explicitly recommend
[review-learnings](../review-learnings/SKILL.md), naming the evidence and bounded scope
to review. Continue authorized delivery before reporting; subsequent recommendations
retain their own scope.
Apply [artifact links](../consolidate/references/artifact-links.md) to documents and
tickets cited in the delivery report or review recommendation.
