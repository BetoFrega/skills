---
name: explain-pr
description: Explain large or complex pull requests as a navigable HTML guide, tracing user journeys from entrypoints through changed code. Use when asked to understand a PR or build a guided walkthrough of its changes.
---

# Explain a PR

Deliver a portable HTML bundle that lets the reader explain the changed behavior and locate the decisions that produce it. Organize by journeys, weighted by significance rather than line count. A 1,000-line threshold is a useful signal, not a prerequisite.

## 1. Establish the reader and evidence

Always load and apply `simple-language`, including its final self-check. Resolve it from the available skills or [the sibling skill](../simple-language/SKILL.md); if unavailable, ask for its location before drafting.

Identify the reader, their question, the PR, and its base and head commits. Default to an engineer familiar with the product but unfamiliar with this change. Read the linked issue/specification, PR description, complete changed-file inventory, and diff. Inventory screenshots embedded in the PR description, including their surrounding text and intended before/after or journey context. Match local sources to the recorded commits; distinguish the diff baseline from the target branch tip.

Finish when the comparison is reproducible and the original user need is either sourced or explicitly unknown. Separate documented intent, observed implementation, and inference throughout the guide. If evidence is inaccessible or truncated, state the missing coverage and produce only a clearly labeled partial explanation.

## 2. Reconstruct the journeys

Choose a concrete user scenario for each materially distinct behavior. Trace its entrypoint, decisions, data transformations, side effects, and visible outcome through the changed code. Inspect unchanged callers and dependencies where needed to verify connections. For migrations, build tooling, or configuration, trace the lifecycle trigger and affected behavior instead of forcing a request-shaped story.

Follow consequential branches: authorization, validation, failure, retries, and asynchronous handoffs. For queues or events, identify producer, payload, consumer, and completion or failure signal; draw a handoff rather than a synchronous call.

Account for every changed file in a compact working map: a journey, a cross-cutting change, supporting tests, mechanical/generated changes, or unresolved evidence. Group repetitive changes. Finish when all files are accounted for and every narrated connection has source evidence; explicitly retain unresolved edges as uncertainty.

## 3. Write the explanation

Lead with the user's need and a concrete before/after example. Then explain the main journey, followed by independent journeys and cross-cutting changes that affect them.

At each meaningful step, explain the actor's responsibility, what changed, and the consequence. Mark existing, changed, added, or removed behavior with words as well as visual styling. Use small code excerpts only where they clarify a decision. Anchor implementation claims to verified symbols and lines, preferably immutable repository links at the appropriate base/head commit; validate URL schemes and escape source text for HTML.

When the PR description contains screenshots, embed them in the explanation beside the state, comparison, or journey step they demonstrate. Preserve their documented ordering and meaning rather than collecting them into an unconnected gallery. Give each image useful alternative text and a caption that distinguishes what the screenshot visibly shows from what the surrounding PR text claims; link the caption to the original PR description when possible. Treat screenshots as supporting evidence, not proof of implementation. Account for every description screenshot, explicitly naming any image omitted because it is inaccessible, redundant, sensitive, or unrelated to the changed behavior.

Use Mermaid when it clarifies relationships: sequence diagrams for calls and handoffs, flowcharts for decisions. Keep one question per diagram and provide a short textual equivalent. Verify every arrow against the code. Explain decision rationale only when supported; label inferred reasons.

Close with relevant test evidence, remaining uncertainty, and a short reading route through the most informative source locations. Distinguish tests inspected, reported by CI, and run during this task. Treat explaining and reviewing as separate outcomes: report a discovered concern with evidence, without presenting the guide as approval to merge.

Finish when a reader can state the new behavior, follow its cause, and find the supporting code without reading the entire diff.

## 4. Build and verify the bundle

Read and copy [assets/pr-explanation.html](assets/pr-explanation.html) into the bundle root as `index.html`. It is the presentation source of truth. Replace its illustrative content, adapt section count to actual journeys, update the document language/title, and synchronize navigation with section IDs. Keep CSS and narrative inline; keep the pinned CDN renderer, textual fallback, and accessible Mermaid source. Place source citations beside their claims.

Create one portable directory at the user's chosen output location, otherwise in a writable artifact directory outside the reviewed repository. Name it for the PR and keep `index.html` at its root. Store every included PR-description screenshot under `assets/screenshots/` with stable, descriptive filenames and reference it from the HTML with a relative path. Preserve the source image bytes and useful file extension when possible. The bundle must not depend on remote image URLs or absolute filesystem paths; external source links in captions may still point to the PR. Keep required narrative visible; use expandable details for supporting code and evidence. Preserve responsive navigation, keyboard focus, diagram overflow handling, and print styles.

Check the filled bundle for example residue, broken anchors, unescaped code, invented citations, and missing or distorted screenshots from the PR description. Move or copy the complete directory to a temporary location and open `index.html` there when possible; verify that every screenshot still loads from the bundle, desktop/mobile reading works, and details remain usable. Also verify rendered diagrams and their textual fallback with the CDN unavailable. Check print layout if claiming PDF readiness. Report any verification that could not run. Deliver a clickable link to `index.html`, identify the bundle directory, and give a concise coverage statement. Create a `.zip`, publish, or post externally only when requested.
