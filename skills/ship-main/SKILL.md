---
name: ship-main
description: Fix validation failures, address reviews, and deliver the current task's changes to main.
---

# Ship Main

Treat this explicit invocation as authorization to commit and integrate the current task's changes into the repository's main branch and push it. Identify the repository and intended changes from context; clarify only if either is ambiguous.

Inspect current remote state and local changes, preserve unrelated work, and run checks appropriate to the intended diff. Commit only the task's changes, integrate against current remote main without rewriting shared history, and push through the repository's permitted delivery route, creating or updating a pull request and merging it when required.

Carry delivery through to completion: diagnose and fix validation or CI failures within scope, address actionable review feedback, resolve routine integration conflicts, and rerun affected checks after changes. Inspect current review threads and required checks after each update; continue until the final revision satisfies the repository's merge requirements and reaches remote main. Evaluate review findings against the code and task intent, implement warranted fixes, and explain with evidence when a requested change is unwarranted. Treat a failed check or requested revision as work to complete, not an automatic stopping condition.

Pause only when progress requires unavailable access, an external dependency, a substantive user decision, or changes beyond the authorized task. First exhaust safe remedies within scope; if attempts cease making progress, report the specific blocker, attempted remedies, and the smallest action needed to resume. Honor repository protections and required checks throughout.

Confirm the remote main revision and report the delivered commit and validation. This invocation does not authorize deployment, publication beyond the Git delivery, bypassing protections, or archival.

For ticket work, finish the report using [next steps](../next-steps/SKILL.md) to identify any remaining delivery requirements or recommend a successor after full delivery.
