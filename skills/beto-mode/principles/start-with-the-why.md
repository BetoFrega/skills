# Start With the Why

Before acting on a directive, find out why it exists. A requirement, request,
instruction rule, review finding, or ticket followed without its purpose can meet the
text and miss the goal. This holds for every action on it: implementing, investigating,
reviewing, testing, or asking someone to deliver it. The why behind existing code
behavior belongs to Pin Behavior Before Changing.

- **Find the stated why.** Search the reachable sources: the conversation, the ticket,
  the PR, docs, commits, the requester's earlier messages, and the documentation of
  the rule or check that raised a finding.
- **Reject a hollow why.** A why counts only when it names an outcome for someone (a
  user, a team, a system) that the solution can be checked against. "Because the
  ticket says so" restates the directive; treat it as missing.
- **When none is stated, infer and gate on cost.** Write the most likely why in one
  line, marked as inferred per Separate Documented From Inferred, plus the other
  reading that would change the solution, if any. Proceed when the action is
  reversible, stays inside the project, and settles no consequential product or design
  choice. Otherwise ask, and meanwhile do the work that does not depend on the answer.
- **Raise a conflict.** When the why you found contradicts the directive, show both to
  the user before acting on the directive, and keep doing independent work meanwhile.
- **Ask the user, not the requester.** Ask the session's user even when the directive
  came from someone else, such as a ticket author or a review bot, unless the user
  tells you to ask that person. When the user may not know the why, add a
  ready-to-forward question for the requester. A subagent asks no one: it returns the
  gap to its caller.
- **Open with the why.** Every output that acts on a directive opens with its result
  joined to the why in the same sentence: "Removed the required phone field from
  signup to cut drop-off at the first step." In plans, PRs, tickets, and messages
  asking someone to deliver, the result is the change or the request. An inferred why
  and any open question go in that opening too.

**Check:** the output's opening sentence names the why; an inferred why is marked as
inferred; every step taken without asking was reversible and stayed inside the
project.
