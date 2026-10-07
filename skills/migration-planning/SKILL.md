---
name: migration-planning
description: Plan and execute infrastructure, architecture, or database migrations.
---

# Migration planning

Work within authorized scope and repository conventions. Resolve each consequential decision with the user through a recommendation, rationale, and concrete normal and failure scenarios.

Prefer **Strangler Fig** and **vertical slices**: complete capabilities independently exposable, observable, and recoverable. When coupling prevents a slice, justify the smallest enabling work.

## Plan the next slice

Establish its measurable benefit and baseline, boundary, required behavior, intentional changes, consumers inside and outside the repository, operational owner, and prerequisites. Corroborate consumer discovery with runtime evidence; search silence proves nothing.

Specify intermediate states, compatibility, data authority, in-flight work, and recovery. Prefer stable identity-based canary assignment across journeys and return visits. Prefer one authoritative writer; justify independent writers with conflict resolution.

Default to uninterrupted user journeys. Keep a tested return path until migration acceptance, preserving valid activity after activation. For small migrations, recovery through corrective work requires explicit acceptance of the point of no return and consequences.

Proceed when decisions and prerequisites required for the next action are resolved; retain later uncertainties as explicit gates.

## Implement and expose

Follow the repository implementation and review workflow. Characterize unprotected required legacy behavior; verify coexistence, compatibility, controlled activation, and recovery. Automate measurable architectural goals where useful.

Before exposure, require passed checks, usable operational controls, ownership, and flow-specific promotion/recovery criteria: baseline, thresholds, observation period, and representative coverage.

Evaluate canary results separately from legacy results. Before each promotion or authority transfer, revalidate recovery against current data, deployed versions, and in-flight work. Advance only on conclusive evidence. On failure, stop expansion, recover, and diagnose.

## Retire

Require production evidence that consumers, deployed versions, background jobs, and in-flight work no longer need the legacy path. Remove obsolete infrastructure and temporary mechanisms, preserving shared resources. Verify continuity and benefit against the baseline.

Completion requires verified adoption, continuity, and agreed retirement. Report evidence, actual exposure, recovery readiness, and remaining work; distinguish planning, implementation, rollout, and completed migration.

## Read when applicable

- Decomposition or replacement boundaries: [transitional architecture](references/boundaries-and-transition.md).
- Routing assignment, overrides, or flag failures: [routing and recovery](references/routing-and-recovery.md).
- Persisted data, incompatible contracts, or split transactions: [data and business recovery](references/contracts-data-and-recovery.md).
- Before shadow comparison: [shadow testing](references/shadow-testing.md).
- Before proposing retirement-discovery experiments: [scream tests](references/scream-tests.md); interruptions require explicit acceptance.
- Local document changes: [document delivery](../consolidate/references/local-document-delivery.md).
