---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

For product discussions, read relevant canonical contracts, decisions, and evidence
through [product-documentation](../product-documentation/SKILL.md). Retain settled
choices and identify changes from current behavior. After the user confirms a product
choice, use that skill to preserve the decision and affected contracts within the
authorized documentation scope. Unresolved options remain proposals.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet.

Ask **one question per round by default**, prioritizing the decision that most shapes the remaining tree. Group questions only when **every** recommendation in the group is supported by known facts and settled user preferences, is clearly preferable to the alternatives, and is likely to need only a simple "OK" from the user for the entire group. Independence makes questions ready; it does not make their answers obvious. Confidence in your recommendation alone is insufficient: judge how much thought the user needs to give it.

Keep any question that needs comparison, reflection, missing context, or a meaningful tradeoff in its own round, even when other ready questions qualify for grouping. Leave unasked frontier questions pending. Number each question, give your recommended answer, and wait for the user's response before the next round. An expected "OK" is not approval; only the user's actual answer settles decisions.

Format each question like so; repeat the block only for a qualifying group:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

💡 <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; select the next round from the remaining frontier using the grouping rule above. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
