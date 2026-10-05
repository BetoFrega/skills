---
name: review-triage
description: "Triage code-review findings, determine PR approval versus feature activation readiness, and require verified tickets for deferred work. Use to apply or explain this process in an existing review."
---

# Review triage

Apply this process to findings from any code review. Work from the existing review,
changed code, spec, and release evidence; inspect only what is needed to validate
classification and disposition. This skill can also explain the process without
performing tracker or pull-request writes.

## 1. Classify each finding

Keep classification separate from numerical severity and the review axis. A serious
defect in an inactive feature can block activation without blocking merge. A
maintainability concern without a regression belongs in Tech Debt or Improvement.

| Classification | Evidence and impact | Required disposition |
| --- | --- | --- |
| **PR Blocker** | Merging introduces or materially exposes a defect or functional/non-functional regression, including production behavior contrary to spec. | Fix and verify in this PR before approval. A follow-up ticket does not clear it. |
| **Feature Blocker** | Prevents a feature from working as specified, while a verified inactive feature flag isolates it and merge causes no production regression. | Fix and verify in this PR, or create and verify a ticket that blocks the feature's release and flag activation. |
| **Tech Debt** | No functional/non-functional regression, but a significant maintainability cost. | Fix in this PR, or create and verify a follow-up ticket before recommending approval. |
| **Improvement** | Optional maintainability improvement. | Advisory; no ticket required unless accepted as deferred work. |

For each actionable finding record classification, location, evidence, impact, and
smallest credible correction. Preserve the originating review axis when supplied.
Unsupported concerns remain unconfirmed and cannot be presented as established
blockers; explain the missing evidence. A potentially actionable concern grounded
in changed code keeps readiness pending until confirmed or dismissed. Record
disproved or purely speculative concerns as dismissed with the evidence or scope
reason, rather than imposing speculative approval gates.

For **Feature Blocker**, verify the flag's actual default, rollout/activation state,
evaluation path, and isolation of the affected behavior. A conditional in the diff
or a flag mentioned in PR metadata is a lead, not proof. Shared migrations, startup
effects, or code reached with the flag off can still cause a PR Blocker. When
isolation is unverified, keep approval pending that verification; use PR Blocker
when merge-time regression is demonstrated.

## 2. Resolve findings or track deferred work

Verify fixes against each finding's evidence and acceptance condition. An author's
promise or a changed line alone does not establish resolution.

For every deferred Feature Blocker or Tech Debt finding, and every Improvement
accepted as deferred work:

1. Resolve the project's issue-tracker instructions through
   [project configuration locations](../setup-beto-frega-skills/references/project-configuration.md),
   including project-scoped external files. Follow its
   tracker, labels, ownership, and dependency conventions. Classification and
   explanation can proceed without tracker configuration; ticket writes require a
   known destination and applicable conventions.
2. Search for an existing open ticket covering the finding. Reuse it when its
   scope and acceptance criteria cover the work; otherwise prepare a new ticket.
   Related findings can share a ticket only when each remains explicitly covered.
3. Prepare ticket content with the review/PR reference and reviewed revision,
   affected locations, evidence and impact, classification, correction scope,
   acceptance criteria, and the repository's ownership or triage disposition.
   For a Feature Blocker, name the feature and flag, and record that release and
   activation depend on verified resolution. Prepare the tracker's blocking
   relationship when available; otherwise include an explicit activation gate in
   the ticket and prepare a backlink from the existing feature spec or release
   checklist when available.
4. Perform ticket, dependency, feature-spec, and release-checklist writes only
   within the active task's authorization and repository rules. If a required
   write is unauthorized or unavailable, return the complete proposed content or
   edit and report approval pending that write.
5. Read back each ticket and any dependency or release-document entry used.
   Confirm the ID/link, open status, coverage, and activation gate. Record the
   verified link beside every deferred finding.

A ticket draft, proposed title, unverified create response, closed unrelated ticket,
or “will follow up” promise does not satisfy the ticket requirement. Tracking debt
permits deferral without hiding it; it does not turn a production regression into
Tech Debt.

## 3. Determine approval readiness

Establish the intended review scope from the request and repository requirements:
comparison base, change set, and required review axes. Record evidence that the
source review covered that scope; a matching SHA establishes freshness, not
completeness. Missing hunks or required axes keep readiness pending. For an
explicitly limited review, qualify the recommendation to the reviewed scope and
identify remaining coverage before whole-PR approval.

Record the revision covered by the source review and compare it with the current
PR head, or the current branch tip (`HEAD`) for a non-PR review. Also record and
compare the actual target-base tip and diff base or merge-base used by the source
review. For uncommitted work, capture the reviewed patch too. A changed base or
patch changes the review target even when the head is unchanged. If any part of
the target changed, review the entire affected delta, including unrelated new
hunks and the updated integration against the target base. Recheck affected
findings, release evidence, and integration behavior with appropriate repository
checks; a clean merge alone does not establish compatibility. Keep readiness
pending until coverage reaches the current target. Reapply classification and
disposition to new findings.

- **Changes required**: at least one unresolved PR Blocker. Tickets cannot waive it.
- **Approval pending follow-up**: no unresolved PR Blocker, but review coverage is
  incomplete, a potentially actionable unconfirmed concern remains unsettled,
  a Feature Blocker or Tech Debt finding lacks a verified resolution
  or explicit deferral with verified ticket coverage, or required feature isolation
  verification or other accepted follow-up remains incomplete. State the precise
  outstanding action; this is a process gate, not a new defect class.
- **Ready for approval**: review coverage includes the full intended scope at the
  current target; potentially actionable unconfirmed concerns are confirmed and
  dispositioned or dismissed; PR Blockers are resolved and verified; every
  Feature Blocker and Tech Debt finding is either
  resolved and verified or explicitly deferred with verified ticket coverage;
  every Improvement accepted for later work has verified ticket coverage; deferred
  Feature Blockers have verified isolation and recorded activation gates.

Ready for approval means this review process permits approval. Feature Blockers
still prevent activation until fixed and verified. Apply any other repository
checks or approval requirements as well. A review recommendation does not itself
approve or merge a PR, activate a flag, or authorize those writes.
For non-PR reviews, report the equivalent readiness for the branch or working
changes within the stated scope; do not imply that a PR exists or was approved.

## 4. Report the disposition

Group actionable findings under `PR Blockers`, `Feature Blockers`, `Tech Debt`, and
`Improvements`, in that order. Preserve each finding's evidence, meaning, and axis;
keep distinct aspects of the same issue visible. Show whether each finding is
resolved, deferred with a verified ticket link, or awaiting an action. Report
unconfirmed concerns separately with the evidence needed to settle them.

End with counts per classification, approval readiness and its evidence, any
outstanding actions, and feature activation restrictions. When asked to explain
the process in another review, give a concise explanation of these same rules and
apply them to the supplied findings without implying tickets already exist.

Examples:

- A changed permission check exposes data with the flag off: **PR Blocker**;
  creating a ticket leaves approval blocked until the fix is verified.
- An export fails only behind a verified inactive flag: **Feature Blocker**;
  merge can proceed after a verified ticket records the export's activation gate.
- New duplication significantly increases maintenance cost without a regression:
  **Tech Debt**; a verified follow-up ticket permits deferral.
- A suggested helper rename: **Improvement**; advisory unless accepted for later work.
