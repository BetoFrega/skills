# Reconcile delivery, exposure, and flags

Read this to maintain implementation, deployment, and release records, for periodic
reconciliation, or to investigate drift. Setup owns the sources, representation,
triggers, cadence, responsibility, and permitted operations. For incremental
delivery, also read [delivery slices](delivery-slices.md), and reconcile both the
slices and the feature while keeping their audience and scenario coverage.

## Independent dimensions

| Dimension | Evidence |
| --- | --- |
| Implementation | Constructed behavior, validated scenarios, revision, and coverage gaps. |
| Deployment | Presence in a named environment, with provider or equivalent evidence. |
| Authorized release | Approved audiences, conditions, rollout bounds, and advancement or reversal criteria. |
| Observed exposure | Verified availability and behavior for an audience, with actual coverage. |
| Flag observations | Control identity, environment, evaluated targeting and configuration, source and time, and feature relationships. |

Keep the dimensions independent whatever the provider calls them. Passing tests say
nothing about deployment, and deployment does not authorize release. A release plan
describes intent, targeting describes configuration, and only audience behavior
verifies availability and correctness.

Map the actual implementation and evaluation paths: several controls may gate one
feature, and one control may affect several features. Keep prerequisites, conditions,
environments, and identity or cohort rules. A target percentage is configuration;
it does not measure how many users see the feature. Verify evaluation and behavior
before claiming that an audience has the feature.

## Reconciliation workflow

1. **Locate authority and coverage.** Read records, decisions, release plans, and
   sources. Identify every functionality and slice affected by shared controls or
   rules, the relevant dimensions and audiences, the scope, and existing authority.
   Name scope you cannot resolve.
2. **Observe.** Inspect the relevant code and verification, deployed revisions,
   release authority, flag configuration and evaluation, and audience behavior. Each
   source gets a dated observation or an access gap, with environment, identity or
   audience, revision when available, and coverage. When a refresh fails, keep the
   earlier date and mark the record as stale or uncertain.
3. **Reconcile.** Each affected record, dimension, and audience gets a supported
   update or a named gap. Keep approved contracts and report where implementation
   differs. Record external flag changes separately from release approval, and record
   unexplained or unauthorized drift. A mixed lifecycle status needs supporting fields
   or a representation gap.
4. **Read back.** Verify the consolidated observations and links. Report partial,
   draft-only, or unverifiable effects with the affected records and unresolved sources.

A missing access or an incomplete query that returns nothing does not show that a
deployment, exposure, or control is absent. Keep conflicting observations with their
time and scope instead of silently picking one source.

## Operational flag changes

For a requested operation, resolve the release plan and session authority, the actual
control, environment and audiences, bounds, advancement and reversal criteria, current
state, and related features. Verify the provider's capability and scope. Ask only for
authority that is unresolved or new, and reuse prior approval.

Perform authorized operations through the provider's workflow. Read back the
configuration and check audience behavior against the plan's criteria; record the
intended scope, observed state, coverage, and gaps. After a failed or uncertain write,
read back before another change and follow the provider's recovery rules. Reverse only
within agreed authority and conditions.

Reconciliation authorizes documentation updates within scope. Flag operations need
their own authority, and drift may call for a release decision instead of restoring
the old records automatically.

## Ongoing maintenance

Run reconciliation from related delivery work, and pass configuration references to
delegates. Periodic runs follow the configured cadence and sources, including external
changes and missed events, with the same completion, query, and audience coverage
criteria.

Create a real scheduler only for recurrence that was requested or already authorized,
using a verified mechanism. Give it the project binding, configuration entry, sources,
scope, and permitted writes. Maintenance grants no flag authority. A cadence stays a
plan until the mechanism is created and read back; installing the skill starts no
recurring work.
