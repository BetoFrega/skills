# Global personal rules

When setup reconciles global rules, use this maintained policy. Reopen settled choices
only for requested revisions or new decisions required by existing instructions.
For additions, revisions, or removals, follow the
[global rule workflow](../../../AGENTS.md#global-rule-changes); update the
[canonical instruction block](#canonical-instruction-block), setup guidance, and
installed entries. Preserve unrelated instructions.

## Discover and reconcile

1. Inspect configured agents' actual global loading and resolve existing symlinks.
   Use environment/home directories: Codex home, `AGENTS.md` and overrides;
   Claude directory and `CLAUDE.md`. Verify other agents' mechanisms; report unsupported
   discovery rather than inventing entries.
2. Preserve managed blocks, unrelated rules, and agent-specific references.
   Reconcile approved changes in place without duplicates; retain equivalent policy.
   Keep project-specific instructions separate.
3. Retain the canonical global `AGENTS.md`, defaulting to Codex's when none exists.
   Install the block below once.
4. Link Claude's `CLAUDE.md` relatively to that canonical file; retain correct links.
   Before replacing a separate file, reconcile unique instructions by scope and keep
   a recoverable copy. Bring unresolved conflicts to the user.
5. Route other agents through supported global symlinks, imports, or always-loaded
   references. For required inline copies, install this block and record reconciliation.
6. Remove superseded global paragraphs now owned by `beto-mode` principles: the lean
   paragraph beginning "YAGNI, Last Responsible Moment", the exploratory-experiment
   paragraph, and "Time matters". Keep their sentence on cognitive overload.

Include edits, reconciled content, backups, entries, and symlink targets in setup's
complete draft. Apply within approved scope; no repeat approval for approved drafts.

## Canonical instruction block

This reference owns installation; [`personal/global-rules.md`](../../../personal/global-rules.md)
owns the policy text, and the `beto-frega-personal` plugin injects that same file into
Claude cloud sessions, which have no global `CLAUDE.md`. Install the full contents of
`personal/global-rules.md` into each global entry once. Remove any
`@bufferapp/cli` managed block (`!buffer context`) from global entries.

## Verify

Read back all configured agents' global entries: every maintained rule, including
revisions/removals, must match approved behavior. Check preserved content, references,
relative symlinks resolving to the canonical file, and overrides hiding policy.
Check that the substantive communication policy replaces the superseded concision
sentence, preserves user ownership of consequential choices, and avoids mandatory
reports or approval of routine steps. Check that the `beto-mode` pointer is present
and the superseded principle paragraphs are absent. Check that consequential status, decisions,
and next steps recover concrete referents and purpose without a full recap; unavailable
detail stays an explicit gap. Verify native loading in fresh sessions where
available without pasting the policy into the prompt; report unsupported probes.
Distinguish filesystem verification, fresh-session loading, and reload in running
chats. Identical reruns must propose no edits. Report canonical source, configured entries, and discovery limits.
