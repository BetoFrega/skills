---
name: demo-day
description: Prepare a feature-review demo for a demo day — demo script, setup scenarios that seed the environment and print test data and users, a rehearsal recording each feature's demonstrability, and polished demo videos.
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

## 2. Build setup scenarios

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

## 3. Write the demo script

Fill [the demo script template](assets/demo-script-template.md) per feature: the
problem, the before/after, the observable steps on the audience-facing interface,
what each step shows, and the reset or recovery for a step that goes wrong. Order the
features and estimate each one's time.

## 4. Rehearse

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

## 5. Record videos

When the user asks for videos, record each demonstrable feature after its rehearsal
passes, following [recording](references/recording.md). Direct the recording boldly:
stage the feature's key moment with motion, suspense, spotlight, and zoom.

## 6. Record and report

Save the filled template in the demo day's folder as the demo script and rehearsal
report: each step's result, evidence links, timing, verdict, and video link. Record only the
verdict and a link to the report in each feature's canonical work item or record
([One Canonical Record](../beto-mode/principles/one-canonical-record.md)); features
known only by PR keep the report alone.

Complete when every named feature has a verdict backed by a rehearsal from a clean
setup, the setup command reproduces the demo state, and each pending product
decision is presented to the user. Report the verdicts, the setup command and its
output, the pending decisions, and the
[delivery state](../consolidate/references/local-document-delivery.md) of the
versioned scenarios and records.
