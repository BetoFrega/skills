# Global personal communication

Read this when setup installs or reconciles Beto Frega's personal communication
policy. These choices are settled. Configure their global discovery; interview only
if the user asks to change the policy or existing instructions require a new decision.

## Discover and reconcile

1. Identify the agents actually configured and the global instruction entries they
   load. Resolve personal directories through the environment or the user's home
   directory. For Codex, inspect its configured home and global `AGENTS.md`, including
   an override file if present. For Claude, inspect its configured directory and global
   `CLAUDE.md`. Verify any other agent's loading mechanism before changing its entry.
2. Read existing entries and resolve symlinks before drafting changes. Preserve
   managed blocks, unrelated instructions, and agent-specific discovery references.
   An equivalent existing communication section is settled; update it in place only
   when its behavior needs the approved policy.
3. Retain an existing canonical global `AGENTS.md`; when none is established, use
   Codex's global `AGENTS.md`. Install the block below once in that canonical file.
   Keep global personal rules separate from project-specific instruction entries.
4. Make Claude's global `CLAUDE.md` a relative symlink to the canonical `AGENTS.md`.
   Calculate the target from the actual containing directories. Retain a correct
   existing link. If replacing a separate file, reconcile all unique instructions
   with their applicable scope and retain a recoverable copy before replacing it.
   Treat any unresolved instruction conflict as a decision for the user.
5. Route other configured agents to the same canonical file through a supported
   global symlink, import, or always-loaded reference. If an agent requires inline
   content, install the same block and record that setup must reconcile that copy.
   File creation alone does not prove the agent loads it. Surface an unsupported
   discovery mechanism rather than inventing a global entry.

Include the canonical edit, any preserved-content reconciliation, backups, entry
changes, and symlink targets in setup's complete draft. Apply within the confirmed
scope; an already approved draft requires no second approval.

## Canonical instruction block

Copy this block into the canonical global instruction file. This reference owns the
maintained policy; the installed global file is its runtime source for agents.

```markdown
## Personal communication

Communicate with the user in Brazilian Portuguese (pt-BR) in conversation, including
questions, recommendations, progress updates, and final replies. Write documentation,
code, comments, tickets, PRs, and other artifacts in the canonical language of their
repository or space, following its established conventions.

Be brutally concise, even at the expense of grammar. But do not skip relevant information, context, or instructions. Use the fewest words that convey the intended meaning. Avoid filler words, pleasantries, and unnecessary repetition. Use short sentences and paragraphs.

Every specific document or ticket cited in conversation or artifacts must have a
navigable link. Resolve the target before citing it; report an unavailable reference
explicitly instead of inventing a link or silently using only a name or identifier.

Use these semantic emoji markers in conversation:

| Marker | Meaning                                                    |
| ------ | ---------------------------------------------------------- |
| ❓     | A question for the user.                                   |
| 💡     | A suggestion or recommendation.                            |
| ⚠️     | An alert or risk that deserves attention.                  |
| 🛑     | A blocker that prevents the affected work from proceeding. |
| 🔐     | A request for authorization.                               |
| 🔄     | Work in progress or a meaningful progress update.          |
| ✅     | A verified result or completed work.                       |
| ➡️     | Concrete next steps.                                       |

Place one marker at the start of each relevant functional block, followed by clear
text. Category labels are optional; use them when they help organize a longer reply.
Simple replies need no marker, and individual sentences need no repeated marker.
Use 💡 for recommendations and reserve ➡️ for next steps. Keep alerts distinct from
blockers, and ordinary questions distinct from authorization requests. Use ✅ only
when the claimed result or completion has been verified; describe progress with 🔄.
The emoji convention applies to conversation only. Artifacts follow their own style.
```

## Verify

Read the installed policy through every configured agent's global entry. Confirm the
language split, concision rule, linked document/ticket citations, all eight meanings,
and one marker per relevant block.
For symlinks, check that the stored target is relative and resolves to the canonical file. Verify
that preserved content remains accessible, references still resolve, and no alternate
global override hides the policy. Distinguish verified filesystem configuration from
whether an already running conversation has reloaded its instructions.

Rerunning setup with the same agent configuration and policy must propose no edits.
Report the canonical source and configured entries, plus any discovery limitation.
