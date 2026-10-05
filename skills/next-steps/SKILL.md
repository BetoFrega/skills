---
name: next-steps
description: Explain remaining ticket delivery steps after implementation, suggest the next ticket after full delivery, or list next actions when asked.
---

# Next Steps

Use the latest goal, agreed plan, completed work, and user corrections. For ticket work, read the ticket and the repository's tracker and delivery rules, then verify the current state of relevant artifacts before choosing the applicable branch below.

## Implementation complete, delivery pending

Explain what remains to fully deliver the current ticket. Return a short numbered list in execution order, with the immediate next action first and any blocker or required decision beside the affected action. Derive the remaining work from the ticket's acceptance criteria and repository workflow: checks, review, integration, deployment, operational verification, and tracker closure apply only where required.

Call delivery complete only when every required acceptance and delivery condition has verified evidence. A completed implementation, merged PR, or closed ticket alone may leave required work outstanding. Missing evidence remains an explicit delivery gap.

## Ticket fully delivered

1. Read the ticket's parent relationships and specification references. If it belongs to a spec, read that spec and its remaining tickets, including current status and blocking relationships. Recommend the next open ticket whose prerequisites are complete, using dependency order and documented priority. When several tickets are ready, choose one and explain its value toward the spec's goal. Include the ticket link or identifier and the reason it comes next. If no ticket is ready or the spec is complete, omit a next-ticket suggestion.
2. If the ticket has no spec, inspect its explicit follow-up links, dependency relationships, and directly related open tickets. Suggest a ticket only when those sources establish a clear successor that is ready to start. Include its link or identifier and the relationship that makes it next. Otherwise, omit a suggestion.

If tracker or spec evidence is unavailable, report the lookup gap and base recommendations only on verified relationships. A suggestion does not itself authorize starting another ticket; honor any existing authorization for the workset.

## Invocation boundary

An explicit request for next steps is informational: return the applicable result and end the turn. When reached automatically after implementation or delivery, apply this guidance to the final report once the authorized work is complete or blocked; continue any remaining authorized delivery work before reporting. For work without a ticket, list the remaining task actions, or say the task is complete. If no goal can be identified, ask which task the user means.
