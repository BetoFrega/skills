---
name: writing-for-agents
description: Write agent-facing documents. Use when creating or editing skills, AGENTS.md, or CLAUDE.md.
---

Write for a competent model; keep guidance that changes behavior.
For skills, read [skill mechanics](SKILL-MECHANICS.md) for invocation, frontmatter,
and routers. Report local edits through
[document delivery](../consolidate/references/local-document-delivery.md).

## Context pointers

A pointer names out-of-context material and says when to read it. Front-load its
leading word; give one trigger per distinct branch, collapsing synonyms and repeated
identity. Sharpen weak triggers before inlining required material. Missing triggers
make retrieval unreliable.

Always-loaded pointers cost context and attention every turn: prune them harder
than their targets. User-invoked documents cost memory; reserve that burden for
human judgment.

## Information hierarchy

Separate ordered actions from reference. Inline what every branch needs; disclose
branch-specific material through conditional pointers. Keep steps visible and each
concept's definition, rules, and caveats together; a flat reference peer-set is valid.
Even unique relevant content can dilute attention. Split by branch or sequence only
when the attention benefit justifies added context or cognitive cost.

## Completion and splitting

Make completion checkable and exhaustive: “every modified model accounted for” drives
coverage even in flat reference. When later steps invite premature completion,
sharpen the current criterion first. If it stays irreducibly fuzzy and rushing is
observed, hide later steps behind a real context boundary: handoff or subagent
dispatch. Inline calls create no boundary; merging sequences exposes later steps.
For independent invocation, consult [skill mechanics](SKILL-MECHANICS.md).

## Leading words

Use compact pretrained concepts and shared vocabulary across prompts, pointers,
docs, and code. Repeat the token, not its definition; prefer familiar terms over
coined ones. Replace explanations only when the leading word sharpens behavior.
Prefer observable bounds, such as “red on the bug,” to subjective reassurance.
State positive targets; retain hard prohibitions that resist positive phrasing,
paired with the desired behavior.

## Pruning

Keep each meaning authoritative in one place; intentional token repetition differs
from duplicated guidance. Configuration, scripts, layout, and help output own their
facts. Cache only expensive lookups; preserve conventions, rationale, and gotchas
absent from those sources.

Delete stale, irrelevant, and sentence-level no-op content. Judge no-ops against
model defaults and settle disagreement through observed runs. Strengthen failed
cues; prefer deleting an ineffective sentence to merely trimming it.
