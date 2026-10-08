---
name: prune-agent-docs
description: Propose independently reviewed reductions to agent documents, then apply user-authorized cuts.
---

Use [writing-for-agents](../writing-for-agents/SKILL.md). Trust model competence; retain only behavior-changing guidance.

Inspect the user's chosen file; otherwise select one large agent-facing document with clear pruning potential. Show concrete cuts and estimated word reduction, targeting 50–95%. Preserve original intent, essential contracts, exceptions, and reference triggers. Prefer deletion over relocating bulk; explain when fidelity limits reduction.

Before requesting authorization, have an independent subagent review the original, proposed text, and relevant sources and references. Check for lost or changed rules, contracts, exceptions, and reference triggers; verify affected outgoing links and incoming anchors. Use execution scenarios only to resolve concrete behavioral uncertainty. Resolve findings and have the reviewer recheck affected cuts before presenting the reviewed proposal for authorization.

Execute only cuts explicitly authorized by the user. Compare the resulting diff with the reviewed, authorized proposal. Return deviations to the reviewer; obtain authorization for changed cuts. Verify preserved requirements and references. Report before/after word counts, measured reduction, and [document delivery state](../consolidate/references/local-document-delivery.md).
