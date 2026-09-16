---
name: explain-pr
description: Explain large or complex pull requests as a navigable HTML guide, tracing user journeys from entrypoints through changed code. Use when asked to understand a PR or build a guided walkthrough of its changes.
---

# Explain a PR

Deliver an HTML guide that lets the reader explain the changed behavior and locate the decisions that produce it. Organize by journeys, weighted by significance rather than line count. A 1,000-line threshold is a useful signal, not a prerequisite.

## 1. Establish the reader and evidence

Always load and apply `simple-language`, including its final self-check. Resolve it from the available skills or [the sibling skill](../simple-language/SKILL.md); if unavailable, ask for its location before drafting.

Identify the reader, their question, the PR, and its base and head commits. Default to an engineer familiar with the product but unfamiliar with this change. Read the linked issue/specification, PR description, complete changed-file inventory, and diff. Match local sources to the recorded commits; distinguish the diff baseline from the target branch tip.

Finish when the comparison is reproducible and the original user need is either sourced or explicitly unknown. Separate documented intent, observed implementation, and inference throughout the guide. If evidence is inaccessible or truncated, state the missing coverage and produce only a clearly labeled partial explanation.

## 2. Reconstruct the journeys

Choose a concrete user scenario for each materially distinct behavior. Trace its entrypoint, decisions, data transformations, side effects, and visible outcome through the changed code. Inspect unchanged callers and dependencies where needed to verify connections. For migrations, build tooling, or configuration, trace the lifecycle trigger and affected behavior instead of forcing a request-shaped story.

Follow consequential branches: authorization, validation, failure, retries, and asynchronous handoffs. For queues or events, identify producer, payload, consumer, and completion or failure signal; draw a handoff rather than a synchronous call.

Account for every changed file in a compact working map: a journey, a cross-cutting change, supporting tests, mechanical/generated changes, or unresolved evidence. Group repetitive changes. Finish when all files are accounted for and every narrated connection has source evidence; explicitly retain unresolved edges as uncertainty.

## 3. Write the explanation

Lead with the user's need and a concrete before/after example. Then explain the main journey, followed by independent journeys and cross-cutting changes that affect them.

At each meaningful step, explain the actor's responsibility, what changed, and the consequence. Mark existing, changed, added, or removed behavior with words as well as visual styling. Use small code excerpts only where they clarify a decision. Anchor implementation claims to verified symbols and lines, preferably immutable repository links at the appropriate base/head commit; validate URL schemes and escape source text for HTML.

Use Mermaid when it clarifies relationships: sequence diagrams for calls and handoffs, flowcharts for decisions. Keep one question per diagram and provide a short textual equivalent. Verify every arrow against the code. Explain decision rationale only when supported; label inferred reasons.

Close with relevant test evidence, remaining uncertainty, and a short reading route through the most informative source locations. Distinguish tests inspected, reported by CI, and run during this task. Treat explaining and reviewing as separate outcomes: report a discovered concern with evidence, without presenting the guide as approval to merge.

Finish when a reader can state the new behavior, follow its cause, and find the supporting code without reading the entire diff.

## 4. Build and verify the HTML

Read and copy [assets/pr-explanation.html](assets/pr-explanation.html). It is the presentation source of truth. Replace its illustrative content, adapt section count to actual journeys, update the document language/title, and synchronize navigation with section IDs. Keep CSS and narrative inline; keep the pinned CDN renderer, textual fallback, and accessible Mermaid source. Place source citations beside their claims.

Write a single `.html` artifact to the user's chosen output location, otherwise a writable artifact directory outside the reviewed repository. Keep required narrative visible; use expandable details for supporting code and evidence. Preserve responsive navigation, keyboard focus, diagram overflow handling, and print styles.

Check the filled artifact for example residue, broken anchors, unescaped code, and invented citations. Open it in a browser when available; verify desktop/mobile reading, rendered diagrams, details, and readability with the CDN unavailable. Check print layout if claiming PDF readiness. Report any verification that could not run. Deliver a clickable file link and a concise coverage statement; publish or post externally only when requested.
