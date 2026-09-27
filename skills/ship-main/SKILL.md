---
name: ship-main
description: Validate and push the current task's changes to main.
---

# Ship Main

Treat this explicit invocation as authorization to commit and integrate the current task's changes into the repository's main branch and push it. Identify the repository and intended changes from context; clarify only if either is ambiguous.

Inspect current remote state and local changes, preserve unrelated work, and run checks appropriate to the intended diff. Commit only the task's changes, integrate against current remote main without rewriting shared history, and push through the repository's permitted delivery route. Resolve routine integration issues within scope; stop for failing required checks, conflicts needing a substantive decision, or a repository restriction that prevents delivery.

Confirm the remote main revision and report the delivered commit and validation. This invocation does not authorize deployment, publication beyond the Git delivery, bypassing protections, or archival.
