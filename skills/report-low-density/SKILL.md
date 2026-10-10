---
name: report-low-density
description: Prepare one delegated low-information-density flag as a reproducible tracker issue; publish only with the user's explicit request or approval. Use neither for investigation nor remediation.
---

# Report low density

Run only as a subagent delegated under the repository's information-density rule;
otherwise create nothing and name the missing delegation. Delegation scopes reporting,
not tracker authority. Require the exact flag, every grouped source pointer, relevant
revision/environment, and minimal reproduction steps; return missing inputs without
creating anything. Publish only with explicit user authority in the active task.

## Resolve the tracker contract

Resolve [project configuration](../setup-beto-frega-skills/references/project-configuration.md),
including external files; read repository instructions and tracker/label contracts.
Resolve category `low information density` and workflow `needs triage`. Use defaults
`low-info-density` / `needs-triage` only when explicitly mapped by project documents.
Verify both external labels, or the local Markdown category/status representation.
Missing/contradictory configuration means no write: direct the parent to
`$setup-beto-frega-skills`. Guess/create no labels or unmapped defaults.

## Build the minimal issue

Title: `‼️ LOW INFORMATION DENSITY ‼️ — <short source>`.
Body only:

- stable source pointers (path/lines, log/command, durable artifact);
- revision/environment when reproduction depends on them;
- minimum reproduction steps/command;
- `low-density-fingerprint: sha256:<hex>`;
- `Investigate with $investigate-low-density.` if available, otherwise `Investigation required.`

Exclude diagnosis, severity, reductions, copied dumps, plans, and speculative context.
Redact sensitive data; prefer reproducible pointers. Fingerprint the exact UTF-8 bytes
of tracker project ID, lexicographically sorted repo-relative source pointers, and
steps stripped of trailing whitespace, separated by LF; use SHA-256.

## Resolve publication authority

Search duplicates during preparation before requesting/exercising publication authority.
Without a match, authority is either the user's explicit request to publish this report,
or their explicit approval of the shown destination, title, labels, and complete body,
carried by the parent in delegation. Repository/standing rules, another report's approval,
or the parent's decision are insufficient.

Without authority, return `approval-required` and that exact prepared issue plus this
question in the user's language: `May I publish this low-density issue to <tracker>?`
The parent asks, then delegates again with approval and unchanged issue. This is
successful preparation, not access failure or uncertain write.

## Detect duplicates and publish

Search open issues with configured category and fingerprint during preparation and
again immediately before authorized creation. An existing match gets no mutation,
including no workflow reset. Otherwise create one with category/workflow values.
For local Markdown use a deterministic fingerprint filename and atomic create-if-absent.

After creation search the fingerprint again. Multiple open matches: report the
lowest-numbered as canonical and every duplicate; edit/close none. Return the created
or matched link. After uncertain creation search once: one match establishes success;
otherwise remain unresolved and never retry the create. On access/authentication
failure or unresolved write, say no issue was confirmed and creation may be unresolved,
preserve exact flag/reproduction pointers, and stop.

For local Markdown issues, carry [document delivery](../consolidate/references/local-document-delivery.md)
in the parent handoff.
