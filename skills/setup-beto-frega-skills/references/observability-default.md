# Observability baseline defaults

Use this only to recommend answers while creating a repository-owned
`OBSERVABILITY.md`. It is not policy after that document exists.

## Recommended decisions

- **Outcome**: a maintainer can detect user-visible failure, determine affected scope,
  follow one operation across relevant boundaries, and identify the owning component
  without first adding instrumentation.
- **Scope**: cover deployed runtime behavior, asynchronous work, external dependencies,
  scheduled jobs, and operational tooling. Mark build-only or static repositories
  explicitly when runtime observability is not applicable.
- **Signals by question**: use logs for discrete events, metrics for aggregatable health
  and outcomes, and traces for causality across boundaries. Require a signal only when
  it answers a named operational question.
- **Context and correlation**: use stable event names and include service, environment,
  release, outcome, and the available request, trace, job, or operation identifier.
  Propagate context across asynchronous and service boundaries where the repository's
  architecture needs it.
- **Failures**: record a failure once at the boundary that owns the response, preserving
  causal context and distinguishing expected domain outcomes from operational faults.
- **Privacy and security**: exclude secrets and credentials. Minimize personal and
  customer data, document approved identifiers, and define redaction at ingestion
  boundaries. Treat propagated context as data that can cross trust boundaries.
- **Volume and cardinality**: bound dimensions, avoid raw user-controlled values as
  metric attributes, and specify sampling, retention, or verbosity controls where cost
  can grow materially.
- **Health and response**: define the user or system outcomes worth alerting on, the
  owner, and the expected response. Prefer actionable symptom alerts over internal
  noise. Link a runbook when response is not obvious.
- **Verification**: identify which requirements are enforced by tests, telemetry-schema
  checks, staging probes, dashboards, or manual operational exercises. A log statement
  alone is not proof that exported telemetry is usable.
- **Exceptions**: name an owner, rationale, compensating control, and review condition.

## Questions the grilling must settle

1. Which deployed components and critical journeys are in scope?
2. Which failures or degradations must be detectable, and by whom?
3. Which operational questions require logs, metrics, traces, or another signal?
4. Which context must correlate work across each real boundary?
5. Which data is prohibited, redacted, hashed, sampled, or retention-limited?
6. Which dimensions can grow, and what bounds their cardinality and volume?
7. Which conditions page, notify, or remain dashboard-only; who responds?
8. How is the baseline verified before and after release?
9. How are exceptions approved and retired?

## Suggested document shape

Keep the repository document concise and testable:

1. Scope and system boundaries
2. Required operational outcomes
3. Signal and correlation requirements
4. Data-safety and cost constraints
5. Alerts, ownership, and response
6. Verification
7. Exceptions

Reference: [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
and [signal model](https://opentelemetry.io/docs/concepts/signals/).
