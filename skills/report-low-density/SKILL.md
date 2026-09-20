---
name: report-low-density
description: Publish one existing low-information-density flag as a minimal, reproducible tracker issue when a parent agent explicitly delegates reporting under the repository's information-density rule. Do not use for investigation or remediation.
---

# Report low density

Run only as a subagent explicitly delegated by a parent agent under the repository's
information-density rule. Otherwise create nothing and state that reporting requires
that delegation. Publish one observed flag. Do not inspect beyond what is needed to
verify stable reproduction pointers. The parent agent must supply the exact flag plus
every grouped source pointer, revision or environment when relevant, and minimal
reproduction steps. Without those inputs, return the missing fields and create nothing.

## Resolve the tracker contract

Read the repository's canonical agent instructions, `docs/agents/issue-tracker.md`, and
`docs/agents/triage-labels.md`, following any normative alternate paths. Resolve these
two configured labels:

- category `low information density`, defaulting to `low-info-density` only when the
  project document explicitly keeps that default;
- workflow `needs triage`, defaulting to `needs-triage` only when explicitly mapped.

Verify that both labels exist in an external tracker. For a local Markdown tracker,
verify its documented category and status representation. If configuration or labels
are missing or contradictory, create nothing and direct the parent to
`$setup-beto-frega-skills`. Never guess, fall back to an unmapped default, or create a
label from this skill.

## Build the minimal issue

Use this title:

`‼️ LOW INFORMATION DENSITY ‼️ — <short source>`

The body contains only:

- stable source pointers such as a path and lines, log or command, or durable artifact;
- revision and environment only when they affect reproduction;
- the minimum steps or command that reproduce the flagged content;
- `low-density-fingerprint: sha256:<hex>`;
- `Investigate with $investigate-low-density.` when that skill is available, otherwise
  `Investigation required.`

Exclude diagnosis, severity, proposed reduction, copied dumps, implementation plans,
and speculative context. Redact secrets and sensitive data; prefer a reproducible
pointer over copied content.

Build the fingerprint input with LF separators from the tracker project identifier,
repo-relative source pointers sorted lexicographically, and reproduction steps with
trailing whitespace removed. Hash those exact UTF-8 bytes with SHA-256.

## Detect duplicates and publish

Immediately before creation, search open issues carrying the configured
low-information-density label and fingerprint.

- If no match exists, create one issue with the configured category and workflow
  values.
- If a match exists, make no mutation.
- Never reset the workflow label of an existing issue.

After creation, search the fingerprint again. If multiple open issues match, report the
lowest-numbered issue as canonical and report every duplicate; do not close or edit
them. For a local Markdown tracker, use the fingerprint in a deterministic filename
and require atomic create-if-absent semantics.

Return the created or matched issue reference to the parent. After an uncertain create,
search the fingerprint once: accept one matching issue as success; otherwise keep the
outcome unresolved. Never retry an uncertain create. On missing access, authentication
failure, or an unresolved write, state that no issue was confirmed and that creation
may be unresolved, preserve the exact flag and reproduction pointers, and stop.
