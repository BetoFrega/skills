---
name: demo-day
description: Prepare a feature-review demo for a demo day — a story planned with the user, demo script, setup scenarios that seed the environment and print test data and users, a rehearsal recording each feature's demonstrability, and polished demo videos.
---

# Demo day

Read [beto-mode](../beto-mode/SKILL.md) first and apply the principles it routes to;
name each principle that changed a choice. Global rules keep authority over decisions
and permissions.

The invocation authorizes the demo artifacts below: scenarios, setup, demo script,
rehearsal report, and demo videos. Product code, shared environments, and tracker writes beyond
the verdict comment need their own authority.

## 1. Select features

The user names the features. For each, find its work item or PR and read the draft
demo script from its validation section (see
[plan-increment](../plan-increment/SKILL.md)), acceptance, and references. Without a
draft, reconstruct the steps from the work item, PR, and code, and mark them as
inferred per [Separate Documented From Inferred](../beto-mode/principles/separate-documented-from-inferred.md).

Resolve the records location: an existing project convention or configured product
documentation; otherwise ask, defaulting to `docs/demos/<YYYY-MM-DD>/`. Record the
chosen convention in the project's agent-skills entry so later demo days reuse it.

## 2. Plan the story with the user

Before building anything, agree on the demo's story with the user through
[grilling](../grilling/SKILL.md). Open with one drafted proposal they can correct,
one line per item, drafted from what step 1 read. Mark each guess. Guess where a
wrong guess is cheap to correct (time budget, cast); ask where the answer would
reshape the proposal (usually the audience). Put the first such question after the
proposal, and continue the remaining ones as grilling rounds. The proposal is
grilling's opening plan; its topics, progress counts, and session tree cover only the
questions that stay open. The proposal covers:

- **Audience:** who watches, what they should leave believing, and the time budget.
  It sets how much theatre fits.
- **Per feature:** the problem and before/after; the key moment, the screen the
  audience came to see; the cut, which steps appear and which become starting state;
  the cast and data, the people, companies, and numbers that tell the story.
- **Order** of the features and how one leads into the next, when there are several.

Name what step 1 found that limits the story, such as a "before" that can no longer
be shown, and how the cut handles it. A suspected product defect waits for step 5's
classification.

Record the settled answers in the demo script's Audience section and each feature's
Key moment and Cast lines. The scenarios in step 3 seed exactly that cast and data.

## 3. Build setup scenarios

Target the local environment. Use staging or another shared environment only when
the user names it for this demo day; then isolate demo data under a per-demo marker,
provide a cleanup command, and keep credentials out of tracked files and output
records ([Security by Design](../beto-mode/principles/security-by-design.md)).

Give each feature a reusable, idempotent scenario, versioned in the project and built
on its existing seed, factories, or fixtures. Extend that tooling before adding a new
mechanism; when the project has no seed entry point, add the smallest one the
scenarios need. Compose the demo day's setup from the scenarios: one command that
brings the environment to the demo state and prints what the presenter needs — URLs,
test users and credentials, record identifiers, and the state each feature starts in.

## 4. Write the demo script

Fill [the demo script template](assets/demo-script-template.md) per feature: the
problem, the before/after, the observable steps on the audience-facing interface,
what each step shows, and the reset or recovery for a step that goes wrong. Keep the
order, cut, and key moments agreed in step 2, and estimate each feature's time.

## 5. Rehearse

Run the setup from a clean state, then perform every step through the interface the
audience will see: drive UI with Playwright and capture a screenshot per step; use a
CLI or API only when that is the feature's own interface. When the audience-facing
interface cannot be driven here, the feature is not demonstrable; record exactly what
blocked it.

On a failed step, classify the cause per [Fix Root Causes](../beto-mode/principles/fix-root-causes.md):

- **Demo artifact** (scenario, setup, script): fix it and rehearse the feature again
  from a clean setup.
- **Product defect**: stop that feature, mark it not demonstrable, record the
  diagnosis and evidence, and bring a proposed fix to the user. Change product code
  only after their decision.

Assign each feature a verdict — **demonstrable**, **demonstrable with caveats**, or
**not demonstrable** — supported by the rehearsal evidence
([Evidence Before Claims](../beto-mode/principles/evidence-before-claims.md)).

## 6. Record videos

When the user asks for videos, record each demonstrable feature after its rehearsal
passes, following [recording](references/recording.md).

1. **Plan the staging.** Propose each step's staging over its rehearsal screenshot,
   in the same proposal-then-questions shape as step 2: captions and their text, which moment
   gets spotlight, zoom, or suspense, the motion style, chapter titles, and the
   cursor's acting: its entrance and exit and the expression at each turn of the
   story. Be bold on the key moment and brisk elsewhere. Record the answers in the
   Staging column.
2. **Record** from a clean setup, following the Staging column, and check the frames.
3. **Get approval.** Send each video and ask for direction notes. Turn each note into
   a Staging change and record that feature again. A video is done only when the user
   approves it ([Evidence Before Claims](../beto-mode/principles/evidence-before-claims.md));
   until then the report marks it awaiting approval.

## 7. Record and report

Save the filled template in the demo day's folder as the demo script and rehearsal
report: each step's result, evidence links, timing, verdict, and video link with its
approval state. Record only the
verdict and a link to the report in each feature's canonical work item or record
([One Canonical Record](../beto-mode/principles/one-canonical-record.md)); features
known only by PR keep the report alone.

Complete when every named feature has a verdict backed by a rehearsal from a clean
setup, the setup command reproduces the demo state, each requested video is approved
by the user, and each pending product decision is presented to the user. Report the verdicts, the setup command and its
output, the pending decisions, and the
[delivery state](../consolidate/references/local-document-delivery.md) of the
versioned scenarios and records.
