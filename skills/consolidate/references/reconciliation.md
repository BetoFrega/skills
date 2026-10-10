# Reconcile delivery, exposure, and flags

Read for implementation/deployment/release maintenance, periodic reconciliation, or
drift. Setup owns sources, representation, triggers, cadence, responsibility, and
permitted operations. For incremental delivery, read [delivery slices](delivery-slices.md)
and reconcile slices plus feature while retaining audience/scenario coverage.

## Independent dimensions

| Dimension | Evidence |
| --- | --- |
| Implementation | Constructed behavior, validated scenarios, revision, and coverage gaps. |
| Deployment | Presence in a named environment, with provider/equivalent evidence. |
| Authorized release | Approved audiences, conditions, rollout bounds, advancement/reversal criteria. |
| Observed exposure | Verified audience availability/behavior and actual coverage. |
| Flag observations | Control identity, environment, evaluated targeting/configuration, source/time, feature relationships. |

Keep dimensions independent regardless of provider vocabulary. Tests do not prove
deployment; deployment does not authorize release. Release plans describe intent;
targeting describes configuration; audience behavior verifies availability/correctness.

Map actual implementation/evaluation paths: multiple controls may gate one feature,
one control may affect several. Retain prerequisites, conditions, environments, and
identity/cohort rules. Target percentages are configuration, not measured user exposure.
Verify evaluation and behavior before claiming audience availability.

## Reconciliation workflow

1. **Locate authority/coverage.** Read records, decisions, release plans, and sources.
   Identify all functionalities/slices affected by shared controls/rules, relevant
   dimensions/audiences, scope, and existing authority; name unresolved scope.
2. **Observe.** Inspect relevant code/verification, deployed revisions, release authority,
   flag configuration/evaluation, and audience behavior. Each source needs a dated
   observation or access gap, with environment, identity/audience, available revision,
   and coverage. Preserve earlier dates when refresh fails; mark staleness/uncertainty.
3. **Reconcile.** Each affected record/dimension/audience gets a supported update or gap.
   Retain approved contracts and report implementation discrepancies. Separate external
   flag changes from release approval; record unexplained/unauthorized drift. Mixed
   lifecycle statuses need supporting fields or a representation gap.
4. **Read back.** Verify consolidated canonical observations/links. Report partial,
   draft-only, or unverifiable effects with affected records and unresolved sources.

Missing access/incomplete empty queries prove no absence of deployment, exposure, or
controls. Preserve conflicting observations with time/scope rather than silently
choosing a source.

## Operational flag changes

For requested operations, resolve release plan/session authority, actual control,
environment/audiences, bounds, advancement/reversal criteria, current state, and related
features. Verify provider capability and scope; ask only for unresolved or additional
authority, preserving prior approval.

Perform authorized operations through provider workflow. Read back configuration and
evaluate audience behavior against plan criteria; record intended scope, observed state,
coverage, and gaps. Failed/uncertain writes require readback before another mutation
and provider recovery rules. Reverse only within agreed authority and conditions.

Reconciliation alone authorizes documentation within scope, not flag operations.
Drift can require a release decision rather than automatic restoration to old records.

## Ongoing maintenance

Invoke reconciliation from related delivery work and carry configuration references
into delegation. Periodic work follows configured cadence/sources, including external
changes and missed events, with the same completion/query/audience coverage criteria.

Create an actual scheduler only for requested/already-authorized recurrence with a
verified mechanism. Carry project binding, configuration entry, sources, scope, and
permitted writes. Maintenance grants no flag authority. Cadence stays planned until
mechanism creation/readback; skill installation activates no recurring work.
