---
name: recommend
description: Compare viable alternatives and recommend a choice; resolve missing information that could change it.
---

# Recommend

Compare alternatives against the user's goal, constraints, and priorities. This
invocation produces advice; execution uses its own authorization.

Within this recommendation only, the user is open to revisiting earlier decisions and
rejected options. Treat them as context that can change when they shape the comparison: if an earlier choice blocks a better option or a rejected option now fits,
include that option, name the decision it would reopen, and state the cost of
reversing it. Leave decisions that do not affect this comparison alone.

A previous recommendation on the same question, including your own, is one more
candidate, not the default. Evaluate it against the same criteria as the others
and look for what it got wrong: new facts, weak assumptions, or options it never
considered. Keep it only when it still wins on the merits, and say what you
checked to reach that.

This openness ends with the recommendation; elsewhere, settled decisions stay
settled until the user explicitly reopens them.

## Establish the comparison

Use supplied alternatives, then widen the field before narrowing it. Look for
options that differ in approach, not only in detail: doing nothing or deferring,
changing or dropping the requirement, solving it at another layer or by another
owner, adopting an existing tool or service instead of building, a partial or
manual solution, and combinations. Treat the first obvious answer as one candidate
among these. Screen the field to the distinct viable options, usually three or
more; explain when scope leaves fewer, and name in one line each the options you
discarded and why.
Retrieve project/tool/source facts before questioning the user. Verify feasibility
and changing capabilities against current evidence; distinguish facts, assumptions,
and unknowns and cite evidence that affects the comparison.

## Resolve decisive gaps

A gap is decisive if its answer could change the preferred option under the user's
priorities. Ask one question at a time, starting with the most influential gap;
explain why it matters and offer three meaningful answers when viable, allowing
another answer. Wait, update the comparison, and repeat only for decisive gaps.

Use conditional scenarios while the recommendation remains pending. For an
unavailable decisive fact, state the limitation and smallest resolution. Keep
minor unknowns as explicit assumptions only when they would not change the choice.

## Compare and recommend

Scale depth to impact, uncertainty, and cost; start compact. Include pros and cons
for every alternative against the same criteria, decisive tradeoffs, and a preferred
choice whose advantages outweigh its disadvantages for this user.

Lead with the supported recommendation and a compact table or equivalent comparison.
Explain why it beats the strongest alternative and which changed assumptions or
conditions would reverse it. Use qualitative judgment unless evidence supports
quantification. Make consequential domain, product, architecture, and code-design
choices assessable in conversation: explain affected behavior/responsibilities and
implications without assuming the user read linked artifacts. Describe only the options
and rationale that actually exist; do not invent alternatives after the fact. Finish when no decisive gap
remains; adoption awaits the user's decision unless already explicitly approved.
