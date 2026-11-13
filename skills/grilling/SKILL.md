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

Group questions only when each one is a [trivial](#alternatives) decision on the same
branch. Keep a group to three. Questions requiring comparison, reflection, missing
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

Classify each decision before preparing its alternatives.

A decision is **trivial** when all of these hold: known facts and settled preferences
already pick one option, the choice is cheap to reverse, and you expect a plain "OK".
Every other decision is **non-trivial**. Signs of a non-trivial decision:

- reversing it later is costly or slow: it touches data, a public interface, the
  architecture, a lasting dependency, or behavior users see;
- the viable options differ in cost, risk, or what they rule out, and no fact or
  settled preference decides between them;
- other open questions in the session tree depend on its answer;
- the user has to weigh tradeoffs they care about.

For a trivial decision, use [recommend](../recommend/SKILL.md) to check the options
and show the short format below.

For a non-trivial decision, apply [recommend](../recommend/SKILL.md) in full before
proposing anything: widen the field of options, then weigh the pros and cons of every
viable option, the recommended one included, each with its consequence and its high,
medium, or low impact. Show that weighing in the question, using the long format
below, so the user can judge the recommendation without asking for it.

A non-trivial decision is **particularly hard** when any of these hold:

- after the weighing, no high-impact item separates the two best options;
- the decision is both hard to reverse and high impact;
- a decisive fact stays unknown and is expensive to obtain;
- the options interact across several layers, systems, or owners in ways you cannot
  trace with confidence;
- you changed your recommendation on it, or the user rejected it and you are unsure
  what to propose next.

For a particularly hard decision, consult [advisory](../advisory/SKILL.md) before
recommending. Give the advisor the question, the evidence, the options, and the
criteria, and leave out your own conclusion. Then check the advice against the
evidence and say in the question that you consulted an advisor and where it agreed
or disagreed with you.

In both formats, offer the viable alternatives, usually two or three, written in
[recommend's option format](../recommend/SKILL.md#compare-and-recommend). Skip invented
options added to reach a count, and allow another answer. Resolve decisive
prerequisites before recommending dependent choices. Include the recommendation only
when evidence and settled preferences support it.

Short format, for trivial decisions:

```
❓ **Q<n>: <question title>** (topic <k> of <m>, about <x> questions left)

<context paragraph>

<the question, in one sentence>

<the alternatives, in recommend's option format, without Pro and Con lines>

💡 <recommended alternative and why>
```

Long format, for non-trivial decisions:

```
❓ **Q<n>: <question title>** (topic <k> of <m>, about <x> questions left)

<context paragraph>

<the question, in one sentence>

<the alternatives with their weighed pros and cons, in recommend's option format>

💡 <recommended alternative>, decided by <the high-impact items>. It beats <strongest
alternative> because <reason>; <condition> would reverse it. <Advisor: agreed, or
where it disagreed, when consulted.>
```

Take the progress counts from the session tree; the estimate can change as answers
raise new questions.

Before sending, check the question against this list and fix it if any item fails:

- every fact it depends on was looked up, or you say which sources lacked it;
- the context paragraph is there, with a link or path for each fact cited;
- it asks for one decision;
- it is classified as trivial, non-trivial, or particularly hard, and uses the
  matching format, with the weighing for non-trivial and the advisor for particularly
  hard;
- the alternatives follow recommend's option format;
- it follows from the previous answer, or the topic switch was announced;
- it is recorded in the session tree.

Wait for the user's actual response before the next round; do not count an expected
"OK" as given. Recompute the frontier after answers. Questions depending on another
open question belong to a later round.

## Closure

Propose closure when this deliverable's knowledge requirements are met; show the
supported result, the tree, and consequential gaps. The user may accept, refine, or extend scope.
Deferred branches do not prevent closure. Reuse existing scope confirmation; on accepted
closure hand off settled choices, references, and gaps within existing authorization.
