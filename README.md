# Beto Frega Skills

Agent workflows for developers: clarify the problem, define useful increments,
implement them, review the result, and deliver with evidence.

Start where your work is today. This is a journey map, not a mandatory sequence.
Reuse accepted decisions and existing records instead of repeating every stage.

## Install and invoke

Install the skills with:

```sh
npx skills add betofrega/skills
```

In Codex, name the skill and provide its scope, references, and intended result:

```text
$grill-with-docs Read the existing checkout contracts and help me select
the next usable increment. Focus on guest checkout.
```

Examples below use local Codex skill names. Other clients use their supported
invocation mechanism.
Available tools, agent delegation, and project configuration determine which
workflows a host can execute.

Installation makes instructions available; invocation starts the selected
workflow. Some skills require explicit invocation. Reading a skill is not proof
that its actions ran.

## 1. Prepare the project

Use [setup-beto-frega-skills](skills/setup-beto-frega-skills/SKILL.md) before first
use or when configuration is missing. It discovers existing conventions, proposes
the missing configuration, and obtains approval before writing. It covers tracker,
domain, product records, communication, observability, and accessibility conventions.

```text
$setup-beto-frega-skills Inspect this project's configuration and propose
only the gaps needed to use these workflows.
```

Configuration can live inside or outside the repository. Keep one authoritative
location for each rule and make it discoverable by the configured agents.

## 2. Turn an idea or report into a clear problem

Suppose you want guests to buy without creating an account. Before assigning work,
resolve behavior, terminology, and the uncertainties that affect the first increment.

| Situation | Skill and result |
| --- | --- |
| A selected plan has consequential unanswered questions | [grilling](skills/grilling/SKILL.md): a scoped interview that reaches usable closure. |
| You prefer the familiar explicit interview command | [grill-me](skills/grill-me/SKILL.md): an alias for grilling. |
| Product and domain records already exist | [grill-with-docs](skills/grill-with-docs/SKILL.md): read them first, interview about selected increments, and preserve confirmed knowledge. |
| A question needs trustworthy external evidence | [research](skills/research/SKILL.md): sourced findings with uncertainty retained. |
| A proposed approach depends on actual platform capabilities | [check-feasibility](skills/check-feasibility/SKILL.md): verify those capabilities before recommending it. |
| A small experiment can answer a design question | [prototype](skills/prototype/SKILL.md): a bounded, throwaway demonstrator. |
| Terms or relationships are ambiguous or changing | [domain-modeling](skills/domain-modeling/SKILL.md): sharpen the shared vocabulary and domain records. |

```text
$grill-with-docs Review the current purchase and identity rules. Help me
define the smallest useful guest-checkout increment and its acceptance.
```

Use discoverable facts before asking the user. A prototype or research finding
provides evidence; it does not itself approve product policy.

## 3. Choose an approach and preserve the decision

| Situation | Skill and result |
| --- | --- |
| Several alternatives are viable | [recommend](skills/recommend/SKILL.md): compare them and recommend an actionable choice. |
| One pending decision needs an answer | [decide](skills/decide/SKILL.md): present options and a recommendation, then await your choice. |
| You explicitly delegate a specified decision set | [autonomous-decisions](skills/autonomous-decisions/SKILL.md): independent deliberation and evidence-based judgment within existing authority. |
| A decision is already approved | [record-decision](skills/record-decision/SKILL.md): preserve it in the canonical record. |
| The choice changes architecture | [write-adr](skills/write-adr/SKILL.md): record or supersede architectural rationale. |
| You risk committing too early or deferring too long | [last-responsible-moment](skills/last-responsible-moment/SKILL.md): identify what must be decided now and what can wait. |

```text
$recommend Compare the feasible identity approaches for this selected
increment. Include user impact, maintenance cost, and the next decision.
```

Record accepted choices, including rationale and consequences. Retain unresolved
proposals as proposals. Autonomous deliberation does not grant additional execution
permission.

## 4. Define a usable increment and executable work

| Situation | Skill and result |
| --- | --- |
| Confirmed knowledge is scattered across conversations and records | [consolidate](skills/consolidate/SKILL.md): maintain canonical behavior, rules, decisions, increments, and evidence. |
| The selected outcome needs delivery cuts and tickets | [plan-increment](skills/plan-increment/SKILL.md): usable vertical slices, acceptance, dependencies, and executable work. |
| The change is a migration | [migration-planning](skills/migration-planning/SKILL.md): plan the transition and its operational constraints. |
| An incoming issue or external PR needs classification and readiness | [triage](skills/triage/SKILL.md): verify the report and develop an agent-ready brief through the configured workflow. |

```text
$plan-increment Plan the approved guest-checkout increment. Draft executable
tickets with dependencies, validation, and done criteria; show the breakdown
before publishing.
```

A vertical slice produces a usable result across the necessary layers. One
increment may need several tickets. Resolve outstanding scope and breakdown
choices before publication; reuse approval already given for the same workset.
Ticket readiness does not replace product approval.

## 5. Implement the selected scope

Choose the execution route deliberately:

| Route | Use it when |
| --- | --- |
| [implement](skills/implement/SKILL.md) | Implementing selected work from a specification or tickets. It validates, reviews, and commits the work. |
| [implement-spec](skills/implement-spec/SKILL.md) | Implementing an entire specification and ticket graph through delegated work, integrated into one PR. |

```text
$implement Implement the selected guest-checkout ticket against its linked
contracts and acceptance criteria.
```

Supporting skills solve specific implementation problems:

| Need | Skill |
| --- | --- |
| Design module boundaries and test seams | [codebase-design](skills/codebase-design/SKILL.md) |
| Develop through tests at agreed seams | [tdd](skills/tdd/SKILL.md) |
| Diagnose a difficult bug or performance regression | [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) |
| Obtain independent help when stuck | [advisory](skills/advisory/SKILL.md) |
| Select models and reasoning effort for delegated assignments | [model-selection](skills/model-selection/SKILL.md) |
| Forecast or batch necessary task authorizations | [permission-preflight](skills/permission-preflight/SKILL.md) |
| Resolve sandbox network or misleading authentication failures | [host-network](skills/host-network/SKILL.md) |
| Resolve an active merge or rebase conflict | [resolving-merge-conflicts](skills/resolving-merge-conflicts/SKILL.md) |
| Guide a genuinely human-only provisioning or cutover step | [wizard](skills/wizard/SKILL.md) |

## 6. Review a concrete result

| Need | Skill and result |
| --- | --- |
| Review a branch, PR, or in-progress change | [code-review](skills/code-review/SKILL.md): findings against the selected scope and standards. |
| Write the PR description | [pr](skills/pr/SKILL.md): a reviewer-facing body describing behavior and validation. |
| Resolve review findings and determine readiness | [review-triage](skills/review-triage/SKILL.md): verified dispositions and a gate covering the current target. |
| Explain a large change through user journeys | [explain-pr](skills/explain-pr/SKILL.md): a navigable HTML explanation linked to code. |

```text
$code-review Review the current branch against the selected increment and
acceptance criteria. Include affected error paths and observability.
```

Resolve actionable findings and rerun affected validation. Passing tests alone
does not establish that expected reviews completed.

## 7. Deliver and verify the claimed outcome

Invoke [ship-main](skills/ship-main/SKILL.md) when the current task should be
committed, integrated, and pushed through the repository's permitted main route.
It handles required PRs, checks, automatic reviews, finding triage, and remote
readback.

```text
$ship-main
```

Git delivery, deployment, and audience exposure are separate outcomes.
Deployment and publication beyond Git need their own authority.

Use [verify](skills/verify/SKILL.md) to inspect evidence for a specific claim without
performing fixes:

```text
$verify Confirm that the delivered increment is available to the intended
users in the target environment. Report any verification gaps.
```

Reconcile supported implementation and delivery observations through
[consolidate](skills/consolidate/SKILL.md), preserving unknowns and release authority.

## 8. Learn and select the next useful work

Use [review-learnings](skills/review-learnings/SKILL.md) after meaningful experiments,
feedback, or delivery observations. It separates evidence from interpretation,
resolves consequential choices, and feeds supported knowledge into canonical records.

```text
$review-learnings Review the guest-checkout results and feedback. Identify
supported learning, unresolved questions, and implications for pending work.
```

Use [next-steps](skills/next-steps/SKILL.md) for remaining completion requirements,
learning-review triggers, and ready successors. Learning review does not itself
authorize publishing new tickets or changing release controls.

## Commands for an ongoing task

| Intent | Skill |
| --- | --- |
| Understand progress and blockers | [status](skills/status/SKILL.md) |
| Compare current work with agreed scope | [scope-check](skills/scope-check/SKILL.md) |
| Prepare a continuation brief | [handoff](skills/handoff/SKILL.md) |
| Resume the agreed plan through completion | [proceed](skills/proceed/SKILL.md) |

Status, scope checks, handoffs, verification, and next-step requests are informational.
Use `proceed` to continue execution within existing scope and approval boundaries.

## Maintain the instructions agents and people read

| Need | Skill and result |
| --- | --- |
| Write or improve agent instructions | [writing-for-agents](skills/writing-for-agents/SKILL.md): behavior-changing guidance and useful retrieval structure. |
| Reduce an agent document | [prune-agent-docs](skills/prune-agent-docs/SKILL.md): exact, independently reviewed cuts, applied only after authorization. |
| Clarify reader-facing prose | [simple-language](skills/simple-language/SKILL.md): plain, readable language. |
| Prepare an explicitly delegated low-density tracker report | [report-low-density](skills/report-low-density/SKILL.md): a reproducible flag; publication requires explicit instruction or approval. |
| Investigate a low-density flag | [investigate-low-density](skills/investigate-low-density/SKILL.md): causes and safe reduction options, without implementing fixes. |
| Encode a dense semantic payload | [esds-compress](skills/esds-compress/SKILL.md): compression preserving required operational literals. |
| Recover readable content from that payload | [esds-decompress](skills/esds-decompress/SKILL.md): compact human-readable expansion. |

For ordinary documentation, start with clear prose and links to authoritative
records. Use semantic compression when the task specifically needs that representation.

## Repository layout

- [skills/](skills/): canonical workflows, references, scripts, and agent metadata.
- [Local development links](docs/local-skill-links.md): checkout linking and verification.

For local development, edit canonical copies under `skills/` and expose them
through relative links. From the repository checkout, preview and apply:

```sh
python3 scripts/link_skills.py
python3 scripts/link_skills.py --apply
```

This development script uses the primary checkout by default. Follow the
[local development workflow](docs/local-skill-links.md) for worktree selection,
verification, and synchronization after delivery.
