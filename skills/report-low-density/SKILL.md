---
name: report-low-density
description: Prepare one delegated low-information-density flag as a reproducible tracker issue; publish only with the user's explicit request or approval. Use neither for investigation nor remediation.
---

# Report low density

Run only as a subagent delegated under the repository's information-density rule.
Without that delegation, create nothing and name what is missing. The delegation
covers preparing the report; tracker authority comes separately. Require the exact
flag, every grouped source pointer, the relevant revision and environment, and minimal
reproduction steps. If any is missing, return the missing inputs without creating
anything. Publish only with explicit user authority in the active task. When the
source is a skill from an installed plugin, create nothing here: return the flag for
`report-skill-lesson`, which files it on the plugin's repository.

## Resolve the tracker contract

Resolve [project configuration](../setup-beto-frega-skills/references/project-configuration.md),
including external files, and read the repository instructions and tracker and label
contracts. Resolve the category `low information density` and the workflow value
`needs triage`. Use the defaults `low-info-density` and `needs-triage` only when
project documents map them explicitly. Verify both external labels, or the local
Markdown category and status representation. If configuration is missing or
contradictory, write nothing and direct the parent to `$setup-beto-frega-skills`. Do
not guess or create labels or unmapped defaults.

## Build the minimal issue

Title: `‼️ LOW INFORMATION DENSITY ‼️ — <short source>`.
The body contains only:

- stable source pointers: path and lines, log or command, or a durable artifact;
- revision and environment when reproduction depends on them;
- the minimum reproduction steps or command;
- `low-density-fingerprint: sha256:<hex>`;
- `Investigate with $investigate-low-density.` if that skill is available, otherwise
  `Investigation required.`

Leave out diagnosis, severity, reductions, copied dumps, plans, and speculative
context. Redact sensitive data and prefer reproducible pointers. Compute the
fingerprint as SHA-256 over the exact UTF-8 bytes of: the tracker project ID, the
repo-relative source pointers sorted lexicographically, and the steps with trailing
whitespace stripped, separated by LF.

## Resolve publication authority

Search for duplicates while preparing, before you request or use publication
authority. Without a match, authority is either the user's explicit request to
publish this report, or their explicit approval of the shown destination, title,
labels, and complete body, passed on by the parent in the delegation. Repository or
standing rules, approval of another report, or the parent's own decision do not count.

Without authority, return `approval-required` with the exact prepared issue and this
question in the user's language: `May I publish this low-density issue to <tracker>?`
The parent asks, then delegates again with the approval and the unchanged issue. This
outcome is a successful preparation; it is neither an access failure nor an uncertain
write.

## Detect duplicates and publish

Search open issues for the configured category and the fingerprint while preparing,
and again just before an authorized creation. Leave an existing match untouched,
including its workflow value. Otherwise create one issue with the category and
workflow values. For local Markdown, use a filename derived from the fingerprint and
an atomic create-if-absent.

After creating, search for the fingerprint again. If several open issues match,
report the lowest-numbered one as canonical and list every duplicate, without editing
or closing any. Return the link to the created or matched issue. If the creation
result is uncertain, search once: one match means it succeeded; otherwise leave it
unresolved and do not retry the create. On an access or authentication failure or an
unresolved write, say that no issue was confirmed and that creation may be
unresolved, keep the exact flag and reproduction pointers, and stop.

For local Markdown issues, carry [document delivery](../consolidate/references/local-document-delivery.md)
in the parent handoff.
