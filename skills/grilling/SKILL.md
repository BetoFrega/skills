---
name: grilling
description: Clarify and stress-test a selected plan, decision, idea, or product increment through scoped interview rounds. Use for grilling or consequential uncertainty.
---

Establish the selected goal, scope, and next deliverable from conversation; ask only
if missing. Map its decisions as a **design tree**. For product questions, first read
[product increments](references/product-increments.md): canonical context, slice
sufficiency, and discovery handoff. Retain settled choices; leave future branches deferred.

Work in **rounds**. The **frontier** contains questions whose prerequisites are settled.
Ask **one question per round by default**, prioritizing the decision that shapes the
tree most. Group only when every recommendation is supported by known facts and settled
preferences, clearly preferable, and likely to require just one simple “OK.” Independence
alone does not make answers obvious; confidence alone does not remove user effort.
Questions requiring comparison, reflection, missing context, or meaningful tradeoffs
stay in separate rounds. Leave unasked frontier questions pending.

Number questions; use [recommend](../recommend/SKILL.md) for alternatives, pros/cons,
comparison, and supported recommendations. Resolve decisive prerequisites before
recommending dependent choices. Try for **at least three distinct viable alternatives**
with their main tradeoffs; explain when fewer exist and allow another answer. Include
the recommendation only when evidence and settled preferences support it.

Use this format; repeat only for a qualifying group:

```
❓ **Q1** - **<question title>**: <question body>

A. <alternative and main tradeoff>
B. <alternative and main tradeoff>
C. <alternative and main tradeoff>

💡 <recommended alternative and reason>
```

Wait for the user's actual response before the next round; expected “OK” is not
approval. Recompute the frontier after answers. Questions depending on another open
question belong to a later round.

Find discoverable facts yourself: dispatch a subagent for environmental investigation
instead of asking the user. A running investigation is an unsettled prerequisite;
continue independent frontier questions and wait only for dependent ones. Users own
decisions, which require their responses.

Propose closure when this deliverable's knowledge requirements are met; show the
supported result and consequential gaps. The user may accept, refine, or extend scope.
Deferred branches do not prevent closure. Reuse existing scope confirmation; on accepted
closure hand off settled choices, references, and gaps within existing authorization.
