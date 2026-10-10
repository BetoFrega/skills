---
name: permission-preflight
description: Forecast or batch task authorizations as numbered requests for selective approval.
---

# Permission Preflight

Use already authorized inspection to identify actions needing additional authority;
retain conversation approvals and continue independent authorized work. If the user
requests only an inventory, forecast permissions without starting execution.

## Prepare the list

Prepare concrete, reviewable results before seeking authority to publish, send,
deploy, or cause other external effects. Forecast early when useful; ask for those
effects after preparation.

Use the user's language. Give each independently approvable request a stable number:

- action and target: path, branch, environment, service, recipient;
- purpose and actual authorization reason, including its originating instruction or
  restriction;
- relevant effect: publication, production change, deletion, cost, access.

Limit access to the necessary resource. Name each conditional request's trigger.
If none are needed, state it briefly and proceed. Present requests directly in chat;
optional question tools remain for preferences/clarification when they cannot take
permission requests. End with:

> You can reply “approve all”, “approve all except 4”, “approve 1 and 3”, or “approve none”.

## Interpret and execute

“All” authorizes the presented list within its limits; exclusions deny those items;
selected numbers authorize only those items; “none” denies the list. Accept equivalent
wording, ranges, and multiple exclusions when unambiguous. Clarify ambiguity or
nonexistent numbers before affected actions; silence is not approval.

Acknowledge approved/excluded numbers and continue. Retain decisions across task
turns. Explain blocked dependencies and continue independent work; never route around
a denial.

Append new permissions with new numbers. Materially changed targets, effects, or
scope require a new item and approval. Blanket approval covers only the list shown.

## Approval boundaries

Chat authorization does not replace mandatory tool, sandbox, or platform confirmations,
or an instruction requiring confirmation immediately before execution. Explain when
relevant; promise no elimination of those dialogs.

If automatic review rejects an action, try an alternative within approved scope.
For a remaining blocker, separately report the rejected action and stated reason;
request only the intervention still needed.
