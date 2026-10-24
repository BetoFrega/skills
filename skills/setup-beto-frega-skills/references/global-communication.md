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
2. Preserve managed blocks, unrelated rules, and agent-specific references. Exception:
   remove the `@bufferapp/cli` managed block.
   Reconcile approved changes in place without duplicates; retain equivalent policy.
   Keep project-specific instructions separate.
3. Claude receives the policy only from plugin `SessionStart` hooks: require the
   `beto-frega-skills` 0.8.0+ and `beto-frega-personal` 0.2.0+ installed and enabled
   (earlier personal versions skip local sessions). Record how to restore the global
   `CLAUDE.md` (a copy of a regular file, or a symlink's target), reconcile its unique
   instructions by scope, then remove it. If a fresh local session then lacks the
   policy, restore it as recorded and report the hook gap. Bring unresolved conflicts
   to the user.
4. Retain Codex's global `AGENTS.md` as the inline entry and install the block below
   once, because this repository ships no Codex hooks.
5. Route other agents through supported global symlinks, imports, or always-loaded
   references. For required inline copies, install this block and record reconciliation.
6. Remove superseded global paragraphs now owned by `beto-mode` principles: the lean
   paragraph beginning "YAGNI, Last Responsible Moment", the exploratory-experiment
   paragraph, and "Time matters". Keep their sentence on cognitive overload.

Include edits, reconciled content, backups, entries, and symlink targets in setup's
complete draft. Apply within approved scope; no repeat approval for approved drafts.

## Canonical instruction block

This reference owns installation. The policy text lives in two files, which the
plugin hooks inject into every Claude session:

- [`hooks/beto-mode-routing.md`](../../../hooks/beto-mode-routing.md), injected by
  `beto-frega-skills`;
- [`personal/global-rules.md`](../../../personal/global-rules.md), injected by
  `beto-frega-personal`.

For inline entries such as Codex's `AGENTS.md`, install both files' contents once, in
that order. Remove any `@bufferapp/cli` managed block (`!buffer context`) from global
entries.

## Verify

Read back all configured agents' global entries: every maintained rule, including
revisions/removals, must match approved behavior. Check preserved content, references,
that no global Claude `CLAUDE.md` remains unless restored after a reported hook gap, that both plugins are enabled, and overrides
hiding policy.
Check that the substantive communication policy replaces the superseded concision
sentence, preserves user ownership of consequential choices, and avoids mandatory
reports or approval of routine steps. Check that the `beto-mode` pointer is present
and the superseded principle paragraphs are absent. Check that consequential status, decisions,
and next steps recover concrete referents and purpose without a full recap; unavailable
detail stays an explicit gap. Verify native loading in fresh sessions where
available without pasting the policy into the prompt; report unsupported probes.
Distinguish filesystem verification, fresh-session loading, and reload in running
chats. Identical reruns must propose no edits. Report canonical source, configured entries, and discovery limits.
