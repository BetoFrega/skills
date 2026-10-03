---
name: autonomous-decisions
description: Resolve a specified set of decisions through independent deliberation and evidence-based judgment.
---

# Autonomous Decisions

Activate only on the user's explicit instruction, for the specified decision set.
Expansion to all decisions in the task requires an explicit user instruction.
An accepted decision permits the coordinator to act within existing task
authorization; deliberation creates no additional execution permission.

## Standing rules

- Bring high-risk or irreversible choices, conflicts with previous directions or
  established values, and unresolved material uncertainty about these boundaries
  to the user. Apply this gate whenever relevant facts change.
- Use this process for choices between viable alternatives that materially affect
  behavior, experience, cost, or maintenance. Carry out mechanically determined
  choices directly within the authorized task.
- Before **every** subagent dispatch, apply the available `model-selection` skill
  independently to that assignment and follow its delegation rules.
  Resolve it from the skill catalog;
  in this repository, use [model-selection](../model-selection/SKILL.md). Set the
  actual model and reasoning effort explicitly and disclose them at dispatch.
- Give every subagent a fresh context, its current role instructions, necessary
  evidence, and only the authorized read-only resources. Use read-only tool
  restrictions when supported; otherwise enforce the boundary in the assignment
  and describe isolation accurately. Subagents return findings without mutations,
  external messages, or further delegation. Keep each decider isolated from peer
  deliberations; give judges and verifiers only their explicitly assigned artifacts.
- Complete at most two initial decider assignments and one additional decider
  assignment per decision. The coordinator owns execution and verification.

Use the same decision protocol in Codex and Claude Code. Native isolated agents
and fresh CLI sessions are execution options. Before using a CLI, read only its
adapter: [Codex](references/codex.md) or [Claude](references/claude.md).

## Begin

For multiple activated decisions, begin with [batch.md](references/batch.md).
For one decision, begin with [prepare.md](references/prepare.md).
Load each subsequent reference only when
the current stage's completion criterion names it. Give subagents their role and
inputs rather than the coordinator's routing documents. Splitting files controls
disclosure; fresh subagent contexts provide the actual context boundary.
