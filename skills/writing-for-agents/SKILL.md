---
name: writing-for-agents
description: Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Write for a competent model. Keep guidance that changes behavior.

For skills, read [skill mechanics](SKILL-MECHANICS.md) for frontmatter, invocation, and routers. After editing local agent documents or skills, report their state and next step using [local document delivery](../consolidate/references/local-document-delivery.md).

## Context pointers

A context pointer names out-of-context material and states when to read it: a skill description or document reference.

Front-load the leading word. Describe the target and give one trigger per distinct branch; collapse synonyms and identity already carried by the body. Sharpen weak triggers before inlining required material. Missing triggers make retrieval unreliable.

Always-loaded pointers spend context and attention every turn; prune them harder than their targets. Documents users must remember spend cognitive load: keep that cost where human judgment matters.

## Information hierarchy

Separate ordered steps from reference. Place material where needed:

1. In-file steps: actions in order.
2. In-file reference: rules consulted on demand; a flat peer-set is valid.
3. Disclosed reference: separate material reached through a conditional pointer.

Inline what every branch needs; disclose what only some branches need. Keep steps visible and group each concept's definition, rules, and caveats together.

Even unique, relevant content can sprawl. Split by branch or sequence when excess dilutes attention; a split must justify its context or cognitive cost.

## Completion and splitting

Make completion criteria checkable and exhaustive. Demand coverage, such as “every modified model accounted for”; wording drives legwork even in flat reference.

When later steps invite premature completion, sharpen the current criterion first. Only if it remains irreducibly fuzzy and rushing is observed, hide later steps across a real context boundary: handoff or subagent dispatch. An inline call provides no boundary. Merging sequences exposes later steps again.

For splits by independent invocation, consult [skill mechanics](SKILL-MECHANICS.md).

## Leading words

Use compact, pretrained concepts to recruit existing behavior. Repeat the token, not its definition. Shared vocabulary across prompts, pointers, documentation, and code strengthens execution and retrieval. Coined words require definitions; prefer existing words.

Replace repeated explanations with a leading word only when it sharpens behavior. Prefer observable bounds: “red on the bug” over “a loop you believe in.”

State positive targets. Retain prohibitions only for hard guardrails that cannot be phrased positively; pair them with the desired behavior.

## Pruning

Keep each meaning in one authoritative place. Intentional repetition of a leading word differs from duplicated guidance.

Treat configuration, scripts, layout, and help output as sources of truth. Cache them only when lookup is expensive. Preserve unwritten conventions, rationale, and gotchas absent from configuration.

Delete stale or irrelevant material and sentence-level no-ops. Judge a no-op against the model's default behavior; settle disagreements through observed runs. Strengthen weak cues that fail to change behavior. Prefer deleting an ineffective sentence over trimming it.
