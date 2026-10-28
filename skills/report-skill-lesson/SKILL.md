---
name: report-skill-lesson
description: Prepare an issue on an installed plugin's repository when one of its skills misled the agent or needs a change; publish only with the user's approval. Use instead of editing plugin skills in place.
---

# Report skill lesson

Use when a session shows that a skill from an installed plugin caused, allowed, or
failed to prevent a mistake, or the user asks to change such a skill. Plugin skills
are read-only per
[Encode Lessons in Structure](../beto-mode/principles/encode-lessons-in-structure.md);
this skill files the lesson where the maintainers work. Skills of the repository you
are working in are edited directly instead.

## Resolve the destination

Read the installed plugin's manifest (`.claude-plugin/plugin.json` or
`.codex-plugin/plugin.json` in the plugin's install directory) and take its
`repository`. Record the plugin name and installed `version`. Without a repository
field, name the gap and return the prepared issue for the user to file.

## Build the issue

Title: `<skill>: <observed problem in one line>`.

Body:

- **Skill and version:** plugin name, skill, installed version, agent (Claude or Codex).
- **What happened:** the instruction followed, the resulting behavior, and the user's
  correction. Quote only the lines needed; redact secrets, private data, and
  unrelated project details.
- **Expected:** the behavior the skill should have produced.
- **Proposed change:** the highest level from the Encode Lessons ladder that would
  prevent it, with the exact sentence or file to change when known. Label it a
  proposal.
- **Recurrence:** earlier sessions or issues showing the same mistake, if any.

Keep one lesson per issue. Separate observation from inference per
[Separate Documented From Inferred](../beto-mode/principles/separate-documented-from-inferred.md).

## Check duplicates and publish

Search the destination's open issues for the skill name and symptom. On a match,
propose a comment with only the new evidence instead of a new issue.

Publishing is an external action. Show the destination, title, and complete body, and
publish only with the user's explicit approval of that issue in the active task. Read
back the created issue or comment and return its link. Without access or a GitHub
tool, return the prepared issue ready to paste and say nothing was filed.
