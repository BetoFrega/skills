# Local document delivery

Apply this when creating, changing, deleting, or reporting local documents. Reading
back a file verifies that it was saved on disk. State its Git delivery separately
in meaningful progress updates and the final report.

## Establish the actual state

Resolve the Git repository that owns the affected files, which may differ from the
task's checkout. Inspect the intended changes, including untracked files, unstaged
and staged edits, local commits, and any existing remote branch or pull request.
If that repository has no `origin/main`, report the missing destination or its
configured equivalent before recommending a delivery route.
Report the state supported by evidence:

| State | What the user needs to understand |
| --- | --- |
| Saved locally, uncommitted | The files are on disk; the changes are not committed or integrated into `origin/main`. |
| Committed locally, not pushed | A local commit exists; it has not reached the remote. |
| Pushed to a branch, integration pending | The remote branch contains the changes; its push or open PR does not establish integration into `origin/main`. |
| Integrated into `origin/main` | A freshly fetched remote main revision contains the intended changes. Link the verified commit or merged PR. |

Account for remaining local edits even when an earlier revision was delivered.
Before claiming integration, fetch `origin` and verify the intended version in
`origin/main`; a clean working tree or local `main` alone does not establish it.
If remote verification is unavailable, label integration unverified.

## Explain the remaining route

Until integration is verified, explicitly say the changes are saved locally or
pushed to the named branch and have not yet been confirmed in `origin/main`.
Link the affected files and explain the immediate remaining step.

Recommend [ship-main](../../ship-main/SKILL.md) when available to deliver only this
task's documentation changes. Otherwise describe the repository's permitted route:
review the diff, run appropriate checks, commit the scoped changes, push, complete
required PR reviews and merge when applicable, then fetch and verify `origin/main`.
Start at the first unfinished step and link any existing PR. Preserve unrelated
work and follow the repository's primary-checkout synchronization rules.

A requested local edit can be complete while Git delivery remains pending. During
execution, continue already authorized delivery within scope. Informational status,
handoff, and verification invocations retain their read-only boundaries. Otherwise
recommend the route without treating a documentation edit or this recommendation
as authorization to commit, push, or merge.

For documents outside Git, identify the actual persistence destination and any
pending publication or synchronization. For native provider records, verify their
saved state through that provider. Keep temporary drafts and external configuration
at their configured destinations; use `origin/main` only for repository documents.
