---
name: recommend
description: Compare viable alternatives and recommend a choice; resolve missing information that could change it.
---

# Recommend

Compare alternatives against the user's goal, constraints, and priorities, respecting
settled decisions and rejected options. This invocation produces advice; execution
uses its own authorization.

## Establish the comparison

Use supplied alternatives and add relevant options, or identify them when absent.
Try for three distinct viable alternatives; explain when scope leaves fewer.
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
implications without assuming the user read linked artifacts. Describe actual options
and rationale; do not invent retrospective alternatives. Finish when no decisive gap
remains; adoption awaits the user's decision unless already explicitly approved.
