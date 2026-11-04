---
name: grilling
description: Clarify and stress-test a selected plan, decision, idea, or product increment through scoped interview rounds. Use for grilling or consequential uncertainty.
---

Establish the selected goal, scope, and next deliverable from conversation; ask only
if missing. Map its decisions as a **design tree** and keep it in the
[session tree](#session-tree) file. For product questions, first read
[product increments](references/product-increments.md): canonical context, slice
sufficiency, and discovery handoff. Retain settled choices; leave future branches deferred.

Assume the user holds less of the tree than you do, may have stepped away between
rounds, and is already busy. Write each question so they can answer it from the
question alone.

## Investigate before asking

Before the first question, read what the goal touches: the code, docs, tickets, and
earlier decisions you can reach. Before each later question, check whether its answer
or its options depend on a fact you could look up, and look it up first. Ask the user
only for decisions and for facts no available source holds; when you ask for a fact,
say which sources you checked. Use a subagent when the investigation is long, and work
inline when it takes a few reads. A running investigation is an unsettled
prerequisite: continue with questions that do not depend on it.

## Open with the plan

Then tell the user in a few lines what you understood the goal to be, what you found,
and which topics you will cover, in order. Update that list when an answer
changes it.

## Session tree

Keep the design tree in a file outside the repository, next to the session memory file
when there is one, and state its path in the conversation. Record each question when
it comes up, nested under the question whose answer raised it:

```
## <topic>
- Q1 [settled] <title>. Origin: initial. Answer: <answer>.
  - Q3 [open] <title>. Origin: answer to Q1.
- Q2 [deferred] <title>. Origin: initial. Reason: <why>.
```

Update the entry when its state changes. Read the file again after compaction or
resume. Show the user the tree when the topic changes, when they ask, and at closure.

## Rounds

Work in **rounds** of one question. The **frontier** contains questions whose
prerequisites are settled. Start with the branch that shapes the tree most, then take
each next question from the branch the user just answered, so every question follows
from the previous answer. Finish or defer a branch before switching. When you switch,
say in one sentence which topic closed and which one starts, and show the tree.

A question asks for one decision. When answering it would require another decision
first, or weighing several things at once, split it and ask the prerequisite first.

Group questions only when each one is a simple confirmation on the same branch: the
recommendation is supported by known facts and settled preferences, and you expect a
plain "OK". Keep a group to three. Questions requiring comparison, reflection, missing
context, or meaningful tradeoffs get their own round. Leave unasked frontier questions
pending.

## Context in every question

Give each question a short context paragraph that covers:

- where it comes from: the previous answer, or the part of the goal that raised it;
- what is already known: the facts you checked, each with a link or path and what it says;
- what depends on the answer: what changes in the plan for each choice.

Use the user's own terms and define any other term at first use. If the context needs
more than a short paragraph, the question is too big; split it.

## Alternatives

Use [recommend](../recommend/SKILL.md) to prepare alternatives and the recommendation,
then show the user only the format below; give the full comparison when they ask for
it. Offer the viable alternatives, usually two or three, each with its consequence in
one sentence. Skip invented options added to reach a count, and allow another answer.
Resolve decisive prerequisites before recommending dependent choices. Include the
recommendation only when evidence and settled preferences support it.

```
❓ **Q<n>: <question title>**

<context paragraph>

<the question, in one sentence>

A. <alternative>: <what happens if chosen>
B. <alternative>: <what happens if chosen>

💡 <recommended alternative and why>
```

Wait for the user's actual response before the next round; do not count an expected
"OK" as given. Recompute the frontier after answers. Questions depending on another
open question belong to a later round.

## Closure

Propose closure when this deliverable's knowledge requirements are met; show the
supported result, the tree, and consequential gaps. The user may accept, refine, or extend scope.
Deferred branches do not prevent closure. Reuse existing scope confirmation; on accepted
closure hand off settled choices, references, and gaps within existing authorization.
