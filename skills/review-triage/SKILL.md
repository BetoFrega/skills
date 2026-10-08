---
name: review-triage
description: "Triage code-review findings, determine PR approval versus feature activation readiness, and require verified tickets for deferred work. Use to apply or explain this process in an existing review."
---

# Review triage

Use existing review, changed code, spec, and release evidence; inspect only what validates disposition. Explanation requires no writes.

## 1. Classify findings

Classification is independent of severity and review axis.

| Class | Evidence | Disposition |
| --- | --- | --- |
| **PR Blocker** | Merge introduces or materially exposes a defect or functional/non-functional regression, including production spec violations. | Fix and verify in this PR; tickets cannot waive it. |
| **Feature Blocker** | Feature violates spec, but verified inactive flag isolation prevents merge-time production regression. | Fix/verify or explicitly defer with a verified ticket blocking release/activation. |
| **Tech Debt** | Significant maintainability cost without regression. | Fix/verify or explicitly defer with a verified ticket before approval. |
| **Improvement** | Optional maintainability improvement. | Advisory; accepted deferral requires a verified ticket. |

Record location, evidence, impact, minimal credible correction, and supplied axis.

Keep actionable concerns grounded in changed code pending confirmation/dismissal; state missing evidence without asserting blockers. Dismiss disproved/speculative concerns with evidence/scope reasons.

For Feature Blockers, verify actual flag default, rollout/activation, evaluation path, and isolation, including shared migrations, startup, and flag-off paths. Metadata/conditionals alone are insufficient. Unverified isolation keeps approval pending; demonstrated merge-time regression is a PR Blocker.

## 2. Resolve or defer

Verify fixes against evidence and acceptance conditions; promises or changed lines alone are insufficient.

For deferred Feature Blockers, Tech Debt, and accepted Improvements:

1. Before ticket writes, resolve [project configuration](../setup-beto-frega-skills/references/project-configuration.md), including external files: tracker destination, labels, ownership, dependencies. Classification/explanation needs no tracker configuration.
2. Reuse open tickets covering scope/acceptance criteria, otherwise prepare one. Group only explicitly covered findings.
3. Include review/PR reference, reviewed revision, locations, evidence, impact, classification, correction scope, acceptance criteria, and ownership/triage disposition. Feature Blockers: name feature/flag; block release/activation until verified resolution through available tracker relationships, otherwise explicit ticket gates plus existing spec/checklist backlinks when available.
4. Write tickets, dependencies, specs, and checklists within task authorization/repository rules. Otherwise return complete proposed content/edits; approval remains pending.
5. Read back tickets and supporting dependencies/release entries: verify ID/link, open status, coverage, activation gate. Link each deferred finding.

Drafts, unverified creation responses, closed/unrelated tickets, and promises do not satisfy deferral. Apply [local document delivery](../consolidate/references/local-document-delivery.md) when reporting local ticket/spec/release changes.

## 3. Determine readiness

Establish requested/repository scope: comparison base, changes, required axes. Verify source-review coverage; matching SHA proves freshness only. Missing hunks/axes keep readiness pending. Qualify limited reviews and remaining whole-PR coverage.

Compare reviewed revision with current PR head or branch HEAD, actual target-base tip, diff/merge-base, and uncommitted patch when applicable. If any changed, review the entire affected delta, including unrelated new hunks and integration against the updated base; recheck findings, release evidence, and integration with appropriate repository checks. A clean merge is insufficient. Reclassify new findings; keep readiness pending until coverage reaches the current target.

- **Changes required:** unresolved PR Blocker.
- **Approval pending follow-up:** incomplete coverage, unsettled actionable concern, unverified isolation, missing verified resolution or explicit ticket-backed deferral, or incomplete accepted follow-up. State the exact pending action.
- **Ready for approval:** complete current-target coverage; actionable concerns resolved or dismissed; PR Blockers fixed and verified; other required findings fixed/verified or explicitly deferred with verified tickets; deferred Feature Blockers isolated with recorded activation gates.

Apply other repository checks/approvals. Feature Blockers continue to prohibit activation until verified fixes. Recommendations authorize no PR approval, merge, activation, or writes. For non-PR reviews, report scoped branch/working-change readiness without implying PR existence/approval.

## 4. Report

Order findings: PR Blockers, Feature Blockers, Tech Debt, Improvements. Preserve evidence, meaning, axes, distinct aspects; show resolved, deferred with verified link, or awaiting action. Separate unconfirmed concerns and missing evidence.

End with counts per class, readiness/evidence, outstanding actions, activation restrictions. Explanations apply these rules to supplied findings without implying tickets exist.
