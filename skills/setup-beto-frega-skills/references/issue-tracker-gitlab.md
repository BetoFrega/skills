# Issue tracker: GitLab

Issues and specs live in this repository's GitLab Issues. Use `glab` from the repository
so its remote selects the project.

Document the verified commands for reading an issue with notes and labels, listing and
filtering issues, creating an issue, adding a note, changing labels, closing, and
verifying or creating a configured label. State whether merge requests are also a
request or triage surface; default to no.

When a skill says “fetch the relevant ticket,” read the issue and its notes. When it
says “publish,” create an issue only within the authorization of the active task.
Repository instructions may require preparing a publishing workflow, but they do not
authorize a persistent GitLab mutation. If the active task lacks the user's explicit
request or approval for the exact write, return the complete proposal and wait.
