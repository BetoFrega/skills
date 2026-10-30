---
name: explain-pr
description: Explain large or complex pull requests as a navigable HTML guide, tracing user journeys from entrypoints through changed code. Use when asked to understand a PR or build a guided walkthrough of its changes.
---

# Explain a PR

Deliver a portable HTML guide organized by user journeys, for a PR of any size.
Weight each part by significance, not line count.

## 1. Establish evidence

Apply [simple-language](../simple-language/SKILL.md) and its self-check; if it is
unavailable, ask where it is before drafting.

Identify the reader and their question, the PR, and its base and head commits. The
default reader is an engineer who knows the product but not this change. Read the
linked issue or spec, the description, the complete file list and diff, and any
screenshots in the description with the before, after, or journey context around
them. Match local sources to the commits; the diff baseline is not the target tip.

The comparison must be reproducible, and the user need sourced or marked unknown.
Keep documented intent, observed implementation, and inference apart. For
inaccessible or truncated evidence, name the gap and label the explanation partial.

## 2. Trace journeys

For every distinct behavior, trace the scenario, entrypoint, decisions,
transformations, side effects, and visible outcome, verifying connections through
unchanged callers and dependencies. For migrations, tooling, and configuration, trace
their lifecycle triggers.

Follow authorization, validation, failure, retry, and asynchronous branches. Show an
event or queue as a handoff: producer, payload, consumer, and completion or failure
signal.

Map every changed file to a journey, a cross-cutting change, tests, mechanical or
generated changes, or unresolved evidence, grouping repetition. Finish with every file
accounted for, every connection sourced, and uncertain edges marked.

## 3. Explain

Start with the user need and a concrete before and after, then the main and
independent journeys, then cross-cutting changes. Explain each one's
responsibility, change, and consequence, labeling behavior as existing, changed,
added, or removed in text and visually. Use small excerpts. Cite verified symbols and
lines, preferably with immutable base or head links. Validate
URL schemes and HTML-escape source text.

Place each description screenshot beside the state or journey it shows, in order.
Give it alt text and a caption separating what is visible from what the PR claims,
and link the original description when possible. Screenshots support claims about
the implementation without proving them. Name omitted screenshots and why:
inaccessible, redundant, sensitive, or unrelated.

Use Mermaid sequence diagrams for calls and handoffs and flowcharts for decisions when
they help: one question per diagram, verified arrows, and a text equivalent. Source
each rationale or label it inference.

Close with tests (inspected, CI-reported, and run by you, kept apart), remaining
uncertainty, and a route for reading the source. Report concerns with evidence and
give no merge approval. The guide is done when a reader can explain the behavior,
follow causes, and find the code without the full diff.

## 4. Build and verify

Copy the [HTML template](assets/pr-explanation.html) to `index.html` at the bundle
root. Replace the examples, adapt journeys, language, and title, and keep navigation
and IDs in sync. Keep the inline CSS and narrative, the pinned CDN
renderer, accessible Mermaid source with a text fallback, citations next to their
claims, visible required narrative, expandable supporting evidence, responsive
navigation, keyboard focus, diagram overflow, and print styles.

Write to the chosen destination, or a writable artifacts location outside the
reviewed repository, in a directory named for the PR. Save screenshots under
`assets/screenshots/` with stable descriptive names and original bytes where possible,
referenced by relative paths. Avoid remote images and absolute paths; external
citations in captions are fine.

Check for leftover examples, broken anchors, escaping, citations, and screenshot
coverage or distortion. When possible, move the whole directory elsewhere and open it:
screenshots, desktop and mobile layouts, details, and diagrams with the CDN
unavailable. Check print before claiming PDF readiness, and report checks you could
not run.

Apply [local document delivery](../consolidate/references/local-document-delivery.md)
to the actual destination. Deliver a clickable `index.html`, the directory, and a
coverage statement. Zip, publish, or post only when asked.
