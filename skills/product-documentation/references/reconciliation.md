# Reconcile delivery, exposure, and flags

Read this during related implementation, deployment, and release work, for periodic
maintenance, or when records disagree with observed behavior. Setup supplies sources,
representation, update triggers, cadence, responsibility, and permitted operations.

## Independent dimensions

| Dimension | Evidence it records |
| --- | --- |
| Implementation | Constructed behavior, validated scenarios, relevant revision, and coverage gaps. |
| Deployment | Presence of that change in a named environment, from provider or equivalent evidence. |
| Authorized release | Approved audiences, conditions, rollout bounds, and advancement or reversal criteria. |
| Observed exposure | Availability and relevant behavior for particular audiences and conditions, with actual verification coverage. |
| Flag observations | Control identity, environment, evaluated targeting/configuration, source, observation time, and related functionalities. |

Adapt status vocabulary while keeping these dimensions independently accessible.
A green test does not prove deployment; deployment does not establish release
authority. A release plan describes intended exposure. Flag targeting describes
control configuration; verification of an audience's behavior supports actual
availability and correctness. Provider terminology does not collapse these meanings.

Map control relationships from actual implementation and evaluation paths. Several
flags may gate one functionality, and one flag may affect several functionalities.
Include material prerequisites, conditions, environments, and identity/cohort rules.
A configured percentage is a targeting parameter, not a measured share of users who
experienced the functionality. Verify actual flag evaluation and relevant behavior
before drawing audience availability conclusions.

## Reconciliation workflow

1. **Locate authority and coverage.** Read affected records, governing product decisions,
   release plans, and configured sources. For a shared control or rule, identify all
   affected functionalities. Complete when the relevant records, dimensions, audiences,
   sources, and existing authorization are identified; keep unresolved scope explicit.
2. **Observe.** Inspect code and meaningful verification evidence, deployed revisions,
   release authority, flag configuration/evaluation, and actual audience behavior as
   relevant. Capture source, observation time, environment, identity/audience context,
   revision where available, and coverage. Complete when each relevant source has a
   dated observation or an identified access gap. Preserve the time of earlier evidence
   when a source cannot be refreshed; identify its current staleness or uncertainty.
3. **Reconcile.** Update each supported dimension in the configured representation.
   Retain approved behavior and record implementation discrepancies. Distinguish an
   external flag change from an approved release change; record unauthorized or
   unexplained drift for the appropriate authority. A lifecycle label that mixes
   dimensions needs supporting fields or an explicit representation gap. Complete when
   each affected record, dimension, and audience has a supported update or named gap.
4. **Read back.** Verify consolidated observations and links in the canonical
   destination. Complete with a verified change set; report partial, draft-only, or
   unverifiable effects separately, including the records and sources still unresolved.

Do not interpret missing access or an empty result with incomplete query coverage as
absence of deployment, exposure, or a flag. Preserve contradictory observations with
their time and scope rather than select a convenient source silently.

## Operational flag changes

When the task requests flag operations, read the authorized release plan and existing
session authorization. Resolve the target control, environment, audiences, bounds,
advancement/reversal conditions, current state, and related functionalities. Verify
that the requested operation is within that authority and that the actual provider
operation is available. Ask for authority only for unresolved scope or changes beyond
it; preserve prior authorization for the same scope.

Perform the authorized change using the configured provider workflow. Read back its
actual configuration and evaluate the relevant audience behavior according to the
plan's verification criteria. Record intended scope, observed state, coverage, and any
remaining gap. A failed or uncertain operation needs readback before another mutation;
follow provider recovery rules and report unresolved effects without assuming success.
Use an authorized reversal only when its agreed conditions apply.

Reconciliation alone authorizes documentation within its scope, not a new operational
flag change. A drift observation can require a release decision rather than an
automatic attempt to make the provider match an old record.

## Ongoing maintenance

Related implementation, deployment, and release tasks invoke reconciliation for their
affected records and carry its configuration references to delegated agents. Periodic
reconciliation follows the cadence and sources configured for the product, covering
external changes and missed events. Its completion criteria are the same as event
maintenance, with query and audience coverage recorded.

Use an actual scheduler only when recurring operation is requested or already
authorized and a verified mechanism exists. Include project binding, configuration
entry, sources, scope, and permitted writes in its task. Keep observation and
documentation maintenance distinct from authority for operational flags. Report a
configured cadence as a plan until the recurring mechanism is created and verified;
ordinary skill installation does not activate maintenance.
