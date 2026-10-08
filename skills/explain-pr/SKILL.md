---
name: explain-pr
description: Explain large or complex pull requests as a navigable HTML guide, tracing user journeys from entrypoints through changed code. Use when asked to understand a PR or build a guided walkthrough of its changes.
---

# Explain a PR

Deliver a portable HTML guide by journeys, weighted by significance, not line count; no size prerequisite.

## 1. Establish evidence

Apply [simple-language](../simple-language/SKILL.md), including its self-check; if unavailable, ask its location before drafting.

Identify reader/question, PR, base/head commits; default reader: product-familiar engineer unfamiliar with this change. Read linked issue/spec, description, complete file inventory/diff, and description screenshots with surrounding before/after/journey context. Match local sources to commits; distinguish diff baseline from target tip.

Require reproducible comparison and sourced or explicitly unknown user need. Separate documented intent, observed implementation, inference. Inaccessible/truncated evidence requires named coverage gaps and a labeled partial explanation.

## 2. Trace journeys

For every distinct behavior, trace scenario, entrypoint, decisions, transformations, side effects, visible outcome; verify connections through unchanged callers/dependencies. Trace lifecycle triggers for migrations/tooling/configuration.

Follow authorization, validation, failure, retry, asynchronous branches. Show event/queue producer, payload, consumer, completion/failure signal as handoffs.

Map every changed file to journey, cross-cutting change, tests, mechanical/generated changes, or unresolved evidence; group repetition. Finish with all files accounted for, sourced connections, and explicit uncertain edges.

## 3. Explain

Lead with user need and concrete before/after; follow with main/independent journeys and cross-cutting changes. Explain responsibility, change, consequence; label existing/changed/added/removed behavior textually and visually. Use small clarifying excerpts; cite verified symbols/lines, preferably immutable base/head links. Validate URL schemes; HTML-escape source text.

Place every description screenshot beside its demonstrated state/comparison/journey, preserving meaning/order. Provide alt text and captions separating visible evidence from PR claims; link the original description when possible. Screenshots support, not prove, implementation. Name inaccessible/redundant/sensitive/unrelated omissions.

Use Mermaid sequences for calls/handoffs, flowcharts for decisions when useful: one question per diagram, verified arrows, textual equivalent. Source rationale or label inference.

Close with tests (inspected, CI-reported, task-run distinguished), uncertainty, source reading route. Keep explanation/review separate; report concerns with evidence, without merge approval. Finish when readers can explain behavior, follow causes, locate code without reading the full diff.

## 4. Build and verify

Copy [HTML template](assets/pr-explanation.html) as bundle-root `index.html`; replace examples, adapt journeys, language/title, synchronize navigation/IDs. Preserve inline CSS/narrative, pinned CDN renderer, accessible Mermaid source/textual fallback, adjacent citations, visible required narrative, expandable supporting evidence, responsive navigation, keyboard focus, diagram overflow, print styles.

Use chosen destination or writable artifacts outside reviewed repository. Name directory for PR. Save screenshots under `assets/screenshots/` with stable descriptive names, source bytes/useful extensions where possible, relative HTML paths. No remote-image/absolute-path dependency; external caption citations are allowed.

Check example residue, anchors, escaping, citations, screenshot coverage/distortion. Copy/move whole directory temporarily and open when possible: verify portable screenshots, desktop/mobile, details, diagrams/textual fallback with CDN unavailable. Check print before claiming PDF readiness; report unavailable checks.

Apply [local document delivery](../consolidate/references/local-document-delivery.md) to actual destination. Deliver clickable `index.html`, directory, coverage statement. Zip/publish/post only when requested.
