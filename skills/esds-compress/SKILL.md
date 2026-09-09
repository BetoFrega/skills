---
name: esds-compress
description: Compress input text using Exponential Semantic Density Scaling (ESDS). Use when asked for ESDS compression or a dense semantic payload of state changes, architectural decisions, outcomes, and blockers.
---

# ESDS_COMPRESS

Execute Exponential Semantic Density Scaling (ESDS) on the supplied input text.

1. **Purge NLP syntax.** Strip grammar, stop-words, and conversational framing.
   Preserve semantic operators: negation, conditions, scope, and temporal order.
2. **Maximize entropy.** Encode retained facts as strict DSL, KV-pairs, or logic
   triples, such as `Event(X) -> StateDelta(Y)`. Use consistent identifiers and
   explicit relations; retain source meaning without inventing causality or certainty.
3. **Filter by invariants.** Retain ONLY state-deltas, architectural decisions,
   deterministic outcomes, and blockers. Preserve identifiers and constraints needed
   to interpret them. Distinguish decided from proposed and verified from pending;
   discard narrative, repetition, and facts outside these categories.
4. **Fractal rollup.** Weight detail by temporal distance. Keep recent changes
   specific; recursively merge older context into progressively broader summaries
   over exponentially growing time or sequence windows. Use source order when dates
   are absent. Target an O(log n) historical token footprint for n input events;
   this is a compression target, not a guarantee for independent retained facts.
   Preserve still-active decisions and unresolved blockers regardless of age.
5. **Output.** Yield pure semantic payload: no introduction, commentary, Markdown
   fences, or closing text. If nothing survives filtering, emit `{}`.

Before output, verify that each retained relation is supported by the input and
that rollup preserves the current state, decision scope, and blocker status.

6. **Blind interpretation.** Give an independent subagent only the compacted
   version and ask it to explain what it understands. Start with no inherited
   conversation context; withhold the original, intended interpretation, and
   compression rationale.
7. **Independent loss review.** Give a second independent subagent the original
   and compacted versions and ask it to list semantic losses. Start with no
   inherited conversation context; withhold the first subagent's explanation and
   your own conclusions.
8. **Recover relevant losses.** Compare the blind interpretation and loss review
   against the original. Treat a loss as relevant when it changes the meaning or
   application of retained facts, including state, decisions, conditions, scope,
   certainty, temporal order, or blockers. Restore relevant missing or distorted
   meaning in the compacted output using the same compact format. Keep review
   commentary outside the payload; verify restored relations against the original
   before yielding the final output.
