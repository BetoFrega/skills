---
name: explain-code
description: Walk through code from entrypoint to the end of execution as a navigable HTML guide with editor links to exact lines, or explain a large pull request through its user journeys. Use for code walkthroughs, "how does this get from X to Y", or understanding a PR.
---

# Explain code

Deliver a portable HTML guide for a reader who cannot see the code you read. Pick
the scope:

- **Walkthrough:** one behavior under discussion, followed through one concrete
  scenario from its entrypoint to the end of execution.
- **PR:** every behavior a pull request changes, with each changed file accounted for.

Weight each part by significance, not line count.

## 1. Confirm and establish evidence

Unless the user invoked `explain-code` or `explain-pr` by name, ask before building
the guide: name the behavior and the scenario you would trace, and wait for a yes.

Apply [writing-for-humans](../writing-for-humans/SKILL.md) and its self-check; if it
is unavailable, ask where it is before drafting.

Identify the reader and their question. The default reader is an engineer who knows
the product but has not read this code. Record the revision: commit SHA, and for a
walkthrough, whether traced files have uncommitted changes.

- **Walkthrough:** state the scenario as input, actor, and starting state, taken from
  the conversation. Ask for it only when the conversation leaves it open.
- **PR:** read the linked issue or spec, the description, the complete file list and
  diff, and any screenshots in the description with the before, after, or journey
  context around them. Match local sources to the base and head commits; the diff
  baseline is not the target tip.

Keep documented intent, observed behavior, and inference apart. For inaccessible or
truncated evidence, name the gap and label the explanation partial.

## 2. Trace

Start where execution begins for the scenario (route, command, event handler, job,
UI handler, or test) and end where it ends: the response, the persisted state, the
visible outcome, or the last consumer.

Expand a call only when it changes the path: it picks the branch the scenario takes,
produces a side effect the outcome depends on, or passes control to the code that
continues the chain. Collapse a call whose result is predictable from its name and
contract into one step that says what it returns in this scenario. The rule covers
repository and library code alike; inside a library, cite only the lines that meet
it, such as the line that invokes a registered callback from the repository.

At each decision point:

- **Walkthrough:** follow the scenario. List each other branch in one line with its
  condition, link, and where it ends. Follow one in full only when it is the subject.
- **PR:** follow the authorization, validation, failure, retry, and asynchronous
  branches each changed behavior touches. Trace migrations, tooling, and
  configuration through their lifecycle triggers.

Show an event, queue, or job as a handoff: producer, payload, the line that registers
the consumer, the consumer, and its completion or failure signal. Follow into the
consumer when the behavior continues there; otherwise stop at the handoff and name
the consumer in one line.

For a PR, map every changed file to a journey, a cross-cutting change, tests,
mechanical or generated changes, or unresolved evidence, grouping repetition.

The trace is done when every step connects to the next through a cited line, every
collapsed call says what it returns, uncertain edges are marked, and, for a PR,
every changed file is accounted for.

## 3. Explain

Open a walkthrough with the question, the scenario, the entrypoint, and the end
point. Open a PR guide with the user need and a concrete before and after, then the
main and independent journeys, then cross-cutting changes, labeling behavior as
existing, changed, added, or removed in text and visually.

Give each step:

- one sentence on what happens;
- an editor link to the repository-relative path and line;
- a short excerpt of the lines that matter;
- what goes in and what comes out in this scenario, labeled observed (from a test,
  log, or run) or inferred (from reading);
- the line that leads to the next step.

Source each rationale or label it inference. Use Mermaid sequence diagrams for calls
and handoffs and flowcharts for decisions when they help: one question per diagram,
verified arrows, and a text equivalent.

For a PR, place each description screenshot beside the state or journey it shows, in
order, with alt text and a caption separating what is visible from what the PR
claims; link the original description when possible. Screenshots support claims
about the implementation without proving them. Name omitted screenshots and why:
inaccessible, redundant, sensitive, or unrelated.

Close with tests (inspected, CI-reported, and run by you, kept apart), remaining
uncertainty, and a reading route through the source. Report concerns with evidence
and give no merge approval. The guide is done when the reader can explain the
behavior, follow causes, and find the code without the full diff.

## 4. Build and verify

Copy the [HTML template](assets/code-explanation.html) to `index.html` at the bundle
root. Replace the examples, adapt sections, language, and title, and keep navigation
and IDs in sync. Drop the before-and-after section for a walkthrough. Keep the inline
CSS, the pinned CDN renderer, accessible Mermaid source with a text fallback,
citations next to their claims, expandable supporting evidence, responsive
navigation, keyboard focus, diagram overflow, and print styles.

Write every code citation as `<a class="src" data-path="<relative path>"
data-line="<line>">`, with the path and line as its text. The template's editor bar
turns these into VS Code or IntelliJ IDEA links from the editor and repository folder
the reader picks, and the browser remembers both per repository. Set `data-repo` on
`<body>` to the repository name. Set `data-default-root` to the checkout's absolute
path only when you run on the reader's machine; leave it empty otherwise.

Write to the chosen destination, or a writable artifacts location outside the
explained repository, in a directory named for the PR or the behavior. Save
screenshots under `assets/screenshots/` with stable descriptive names and original
bytes where possible, referenced by relative paths. Avoid remote images and absolute
paths; external citations in captions are fine.

Check for leftover examples, broken anchors, escaping, citations, and screenshot
coverage or distortion. Validate URL schemes and HTML-escape source text. Open the
page in a browser, pick each editor, set a folder, and read back a sample of the
generated links. When possible, move the whole directory elsewhere and open it:
screenshots, desktop and mobile layouts, details, and diagrams with the CDN
unavailable. Check print before claiming PDF readiness, and report checks you could
not run.

Apply [local document delivery](../consolidate/references/local-document-delivery.md)
to the actual destination. Deliver a clickable `index.html`, the directory, and, for
a PR, a coverage statement. Zip, publish, or post only when asked.
