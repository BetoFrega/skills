---
name: permission-preflight
description: Anticipate permissions needed for a task and group requests into a numbered list for selective approval. Use when the user asks to predict or batch authorizations before execution.
---

# Permission Preflight

Reduce interruptions by grouping foreseeable authorizations for the current task. Respond in the user's language.

## Prepare the list

Inspect context, applicable instructions, and available tools using actions already authorized. Identify actions that actually require additional authorization, accounting for approvals already given in the conversation. Continue independent work that is already authorized.

Prepare concrete, reviewable results before requesting approval to publish, send, deploy, or perform another action with external effects. Present an early forecast when useful, but request approval for those effects after the result is prepared. If the user only wants an inventory, provide the forecast without starting execution.

Assign requests stable numbers throughout the task. Each item must specify:

- The action and target: path, branch, environment, service, or recipient.
- The purpose and concrete reason authorization is needed, including the originating instruction or restriction when applicable.
- The relevant effect: publication, production changes, deletion, cost, or additional access.

Separate actions the user can approve independently. Limit access to the necessary resource. Mark conditional permissions with the event that would make them necessary. If no requests are needed, state this briefly and proceed.

Present the list in chat and end the request with:

> You can reply “approve all”, “approve all except 4”, “approve 1 and 3”, or “approve none”.

Ask directly in chat for authorization; reserve optional question tools for preferences and clarification when those tools do not support permission requests.

## Interpret and execute

Map the response to the presented list:

- **“Approve all”** authorizes every item in that list within its stated limits.
- **“Approve all except 4”** authorizes the other items and denies item 4.
- **“Approve 1 and 3”** authorizes only those items; the rest remain unauthorized.
- **“Approve none”** denies the list.

Accept equivalent wording, ranges, and multiple exclusions when the meaning is unambiguous. Clarify ambiguous responses or nonexistent numbers before executing affected actions. Silence is not approval.

Briefly acknowledge approved or excluded numbers and continue authorized work. Preserve the decision across subsequent turns of the same task. When a denied item blocks another, explain the dependency and continue independent parts; do not perform the denied action through an alternative route.

Append newly discovered permissions with new numbers, preserving earlier numbers. Material changes to a target, effect, or scope require a new item and fresh approval. Blanket approval applies only to the list the user saw.

## Approval boundaries

Chat approval records the user's authorization; mandatory tool, sandbox, or platform confirmations still apply when the action is performed. Explain this distinction when relevant without promising to eliminate those dialogs. Advance approval does not replace a confirmation that applicable instructions require immediately before execution.

If an automatic review rejects an action, seek an alternative within the approved scope. If the action remains blocked, separately report the rejected action and stated reason; request intervention only for what still depends on the user.
