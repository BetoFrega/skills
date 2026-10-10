---
name: prune-agent-docs
description: Propose independently reviewed reductions to agent documents, then apply user-authorized cuts.
---

Use [writing-for-agents](../writing-for-agents/SKILL.md). Keep behavior-changing
guidance; trust model competence.

Inspect the user's chosen file; otherwise select an agent-facing document relevant
to the active task and documents discussed, referenced, or open in context, with
clear pruning potential. Use a broader inventory to select one large document only
when context supplies no relevant candidate. Show exact cuts and estimated word
reduction, targeting 50–95%.
Preserve intent, essential contracts, exceptions, and reference triggers. Prefer
deletion over relocating bulk; explain when fidelity limits reduction.

Before requesting authorization, have an independent subagent review the original,
proposed text, and relevant sources. Check changed or lost rules, contracts,
exceptions, retrieval triggers, outgoing links, and incoming anchors. Use execution
scenarios only for concrete behavioral uncertainty. Resolve findings and have the
reviewer recheck affected cuts before presenting the proposal.

Apply only user-authorized cuts. Compare the diff with the reviewed proposal; return
deviations to the reviewer and obtain authorization for changed cuts. Verify retained
requirements and references. Report measured before/after word counts, reduction,
and [document delivery state](../consolidate/references/local-document-delivery.md).
