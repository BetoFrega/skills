---
name: simple-language
description: Rewrite or audit reader-facing prose for plain language, clarity, readability, or actionability. Also use to review any produced text for AI'isms, length, and tense before delivery.
---

Use ISO 24495's four principles. Numeric targets below are working proxies,
not standard clauses or caps: use them as review tripwires.

## Relevant — content selection

Name the reader before editing. Remove throat-clearing and content that reader will
not use: known background, internal process, defensive caveats. Move uncertain cuts
to the end. Preserve every fact, number, condition, and honest uncertainty.

## Findable — structure

Front-load the conclusion, decision, or action; give headings an informative message
when it fits. Keep one topic per paragraph (~5 sentences prompts review). Use parallel
lists for 3+ steps/options/conditions, tables for lookups/comparisons, prose for reasoning.

## Understandable — wording

Keep one idea per sentence (~20 words prompts review). Use active voice with explicit
actors; passive is fine for unknown/irrelevant actors. Prefer verbs and common words,
retaining terms of art. Define terms at first use. Gloss abbreviations at first use
unless the named audience already knows them; use one name per concept. Remove stacked hedges
without deleting real uncertainty.

## Usable — actionability

Name who does what. Give instructions as imperatives with explicit objects and
applicable deadlines; put conditions before actions. End messages with a next step
when one exists.

## Remove AI'isms

Review every text you produce before delivering it: docs, skills, PR and commit
descriptions, tickets, and messages. Rewrite each of these patterns as a direct
statement of the fact or action:

- Slogans and punchy closers: "Pinned is not intended.", "leaving the growth is not."
- Contrast frames: "this is X, not Y", "X, not Y", "not a coverage campaign". State X.
- Emphatic negations: "never as a side effect", "nobody asked for". Say what to do.
- Forced metaphors: "exhale in the same change". Name the action: "simplify again in
  the same change".
- Decorative symbols in prose: `≠`, `→` chains, tree blocks (`├──`, `└──`), emoji
  outside an agreed convention.

Keep terms of art and literal comparisons that carry information.

## Write at human length

Before drafting, estimate how much a person who knows the subject would write for
this reader. Aim for that length; an unchecked draft runs longer. On review, ask
whether a person would have written this much, and cut until the answer is yes.
In running prose, cut every sentence or clause the reader would infer without it.

Read the text as the reader would hear it. Vary sentence length, and join short
related sentences so the text reads with rhythm.

## Use the right tense

Place each verb in time and mood: past for what happened, present for what holds
now, future for what has not happened, conditional for hypotheses and the reader's
options. Apply [verb-tense](../verb-tense/SKILL.md) for the full list of forms and
errors.

## Make every reference reachable

The reader sees only what you showed them in this conversation. When you cite a
page, ticket, file, list item, commit, message, or earlier result, give a link or
path the reader can open, and say what the cited part contains:

- "item 12 on the page": name the page, link it, and quote or summarize item 12.
- "ticket 1234": link the ticket and say what it is about.
- "the fifth point of the list": give the file's path and the point's text.
- "as discussed above": restate the point; the reader may not find it.

Resolve the target before citing it. Show or summarize content you read but did
not show before you refer to it. If you cannot link a target, say so instead of
inventing a link.

## Self-Check (run before returning)

Verify the named reader understands the intended knowledge/action after one reading;
the main point appears in the first two lines; sentences/paragraphs hold one
idea/topic; terms have one name and no unexplained jargon; all facts, numbers,
conditions, and honest hedges survive; no AI'ism from the list above remains; the length matches what a person would write and nothing obvious remains; each verb's tense matches when its event happens; every cited page, ticket, file, or item has a link or path and says what it contains.

For local rewrites, report [document delivery](../consolidate/references/local-document-delivery.md).
