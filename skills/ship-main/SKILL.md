---
name: ship-main
description: Deliver current-task changes to main with validation, automatic reviews, and finding triage.
---

# Ship Main

Explicit invocation authorizes committing, integrating, and pushing the current task
through the repository's permitted main delivery route, including a required PR/merge.
Resolve repository/scope from context; clarify only ambiguity. Preserve unrelated
work, inspect live remote/local state, validate the intended diff, commit only task
changes, and integrate against current remote main without rewriting shared history.

Complete in-scope validation/CI fixes, actionable feedback, and routine conflicts;
rerun affected checks. Failed checks or requested revisions are work to resolve.

## Automatic reviews and merge gate

For PR delivery, mark ready when reviewable. Inspect repository configuration and live
PR/provider evidence for reviews expected or triggered by opening, marking ready,
and updates: requests, checks/statuses, submitted reviews, comments, and provider state
when the PR lacks it. Establish startup and completion for the current review target.
Passing CI, silence, and no pending request do not prove completed reviews. Missing,
failed, or cancelled expected reviews keep readiness pending; investigate/retry.

After each potential trigger, cover at least 30 seconds, refreshing roughly every
10 seconds and at the end; extend for known provider delays. This discovers reviews,
not a completion timeout. Initial emptiness clears nothing. Only after this window,
if no reviews are configured or observed, follow normal repository review requirements.

Read PR comments, review bodies, and inline threads, including bot feedback outside
required checks. Wait for queued/running reviews, then apply
[review-triage](../review-triage/SKILL.md) to every finding: verified fixes,
evidence-backed dismissals, or permitted verified-ticket deferrals and activation gates.
Merge stays pending until **Ready for approval** covers the full scope, current head,
and target base, with other repository requirements satisfied.

After correction pushes, rebases, or base changes, repeat discovery, wait, read,
triage, fix, and validation. Earlier findings retain verified dispositions; earlier
review completion does not clear new runs/findings. If automation does not rerun,
obtain changed-target coverage under triage. Immediately before merge, reread target,
checks, reviews, and comments. Merge only the verified head, with no outstanding
expected review or unaddressed finding; target changes reopen the gate. Enable
auto-merge only after this gate passes.

## Complete delivery

Pause only for unavailable access, external dependencies, substantive user decisions,
or out-of-scope changes. Exhaust safe in-scope remedies first; when progress stops,
report blocker, attempts, and smallest resume action. Honor protections/required checks.

Confirm remote main revision; report commit and validation. Deployment, publication
beyond Git delivery, protection bypass, and archival require separate authority.

For product changes, reconcile records through [consolidate](../consolidate/SKILL.md)
within existing documentation authority. Record supported revision/observations and
remaining gaps; Git delivery proves neither deployment nor audience exposure.

At final checkpoint, use [next steps](../next-steps/SKILL.md) for remaining requirements,
learning-review triggers, and ready successors. When meaningful learning or a configured
review point warrants it, explicitly recommend [review-learnings](../review-learnings/SKILL.md)
with evidence and bounded scope. Complete authorized delivery before reporting;
recommendations retain their own scope. Apply
[artifact links](../consolidate/references/artifact-links.md) to cited documents/tickets.
