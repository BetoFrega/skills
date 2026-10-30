---
name: review-triage
description: "Triage code-review findings, determine PR approval versus feature activation readiness, and require verified tickets for deferred work. Use to apply or explain this process in an existing review."
---

# Review triage

Work from the existing review, changed code, spec, and release evidence, and inspect
only what you need to validate each disposition. Explaining this process needs no
writes.

## 1. Classify findings

The class does not depend on severity or review axis.

| Class | Evidence | Disposition |
| --- | --- | --- |
| **PR Blocker** | The merge introduces or materially exposes a defect or a functional or non-functional regression, including a production spec violation. | Fix and verify in this PR; a ticket cannot waive it. |
| **Feature Blocker** | The feature violates the spec, but verified isolation behind an inactive flag prevents a production regression at merge time. | Fix and verify, or defer explicitly with a verified ticket that blocks release and activation. |
| **Tech Debt** | Significant maintainability cost without a regression. | Fix and verify, or defer explicitly with a verified ticket before approval. |
| **Improvement** | Optional maintainability improvement. | Advisory; an accepted deferral needs a verified ticket. |

Record the location, evidence, impact, smallest credible correction, and the axis
that reported it.

Keep actionable concerns grounded in the changed code until they are confirmed or
dismissed. When evidence is missing, say so without calling the concern a blocker.
Dismiss disproved or speculative concerns with an evidence or scope reason.

For a Feature Blocker, verify the flag's actual default, rollout and activation,
evaluation path, and isolation, including shared migrations, startup, and flag-off
paths. Flag metadata or conditionals alone are not enough. While isolation is
unverified, approval stays pending; a demonstrated regression at merge time makes it
a PR Blocker.

## 2. Resolve or defer

Verify each fix against the evidence and acceptance conditions. A promise or changed
lines alone are not enough.

For deferred Feature Blockers, Tech Debt, and accepted Improvements:

1. Before writing tickets, resolve
   [project configuration](../setup-beto-frega-skills/references/project-configuration.md),
   including external files: tracker destination, labels, ownership, and
   dependencies. Classification and explanation need no tracker configuration.
2. Reuse an open ticket that covers the scope and acceptance criteria, or prepare a
   new one. Group only findings the ticket explicitly covers.
3. Include the review or PR reference, reviewed revision, locations, evidence,
   impact, class, correction scope, acceptance criteria, and ownership or triage
   disposition. For a Feature Blocker, name the feature and flag and block release
   and activation until a verified resolution, using tracker relationships where
   available. Otherwise add explicit gates in the ticket plus backlinks from the
   existing spec or checklist when there is one.
4. Write tickets, dependencies, specs, and checklists within the task's authorization
   and the repository's rules. Otherwise return the complete proposed content or
   edits, with approval still pending.
5. Read back the tickets and supporting dependencies or release entries: verify the
   ID and link, open status, coverage, and activation gate. Link each deferred
   finding to its ticket.

Drafts, unverified creation responses, closed or unrelated tickets, and promises do
not count as deferral. Apply
[local document delivery](../consolidate/references/local-document-delivery.md) when
reporting local ticket, spec, or release changes.

## 3. Determine readiness

Establish the scope requested or required by the repository: comparison base,
changes, and required axes. Verify that the source review covered it; a matching SHA
shows only that the review is current. Missing hunks or axes keep readiness pending.
Qualify limited reviews and state the remaining whole-PR coverage.

Compare the reviewed revision with the current PR head or branch HEAD, the actual
tip of the target base, the diff and merge-base, and any uncommitted patch. If any of
them changed, review the entire affected delta, including unrelated new hunks and
integration with the updated base, and recheck findings, release evidence, and
integration with the repository's checks. A clean merge is not enough. Classify new
findings, and keep readiness pending until coverage reaches the current target.

- **Changes required:** a PR Blocker is unresolved.
- **Approval pending follow-up:** coverage is incomplete, an actionable concern is
  unsettled, isolation is unverified, a verified resolution or ticket-backed deferral
  is missing, or accepted follow-up is incomplete. State the exact pending action.
- **Ready for approval:** coverage reaches the current target; actionable concerns
  are resolved or dismissed; PR Blockers are fixed and verified; other required
  findings are fixed and verified or deferred with verified tickets; and deferred
  Feature Blockers are isolated with recorded activation gates.

Apply the repository's other checks and approvals. A Feature Blocker keeps blocking
activation until its fix is verified. A recommendation authorizes no PR approval,
merge, activation, or writes. For reviews outside a PR, report the readiness of the
scoped branch or working change without implying that a PR exists or is approved.

## 4. Report

Order findings as PR Blockers, Feature Blockers, Tech Debt, then Improvements. Keep
each finding's evidence, meaning, axes, and distinct aspects, and show whether it is
resolved, deferred with a verified link, or awaiting action. List unconfirmed
concerns and missing evidence separately.

End with counts per class, readiness and its evidence, outstanding actions, and
activation restrictions. When only explaining, apply these rules to the supplied
findings without implying that tickets exist.
