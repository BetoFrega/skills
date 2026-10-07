---
name: migration-planning
description: Plan and execute infrastructure, architecture, and database migrations; choose and explain a strategy with the user, build a parallel alternative, transfer traffic, and retire the legacy path.
---

# Migration planning

Guide the migration from understanding the existing system through implementation, controlled transition, and legacy retirement. The central interaction is reasoning with the user about what changes, its impact, which strategy fits, and why.

## Establish the migration

Identify the current system, destination, reason for migrating, affected users and capabilities, and authorized scope: investigation, planning, implementation, operation, or the complete lifecycle. A planning request authorizes planning; existing authorization for further work remains sufficient within its scope.

Translate the reason into an observable outcome and baseline: deployment autonomy, operating cost, capacity, reliability, or time to change. Define behavior to preserve, obsolete capabilities to retire, and intentional changes with the user; use the legacy system as evidence of behavior rather than an unquestioned specification. Prioritize the first slice by expected value, risk, coupling, and available operational capacity.

Read the repository's domain, architecture, testing, deployment, feature-flag, and issue-tracking guidance. Follow its conventions for recording work, readiness, relationships, and decisions. Missing recording guidance is a publication gap; continue independent design and implementation work that is authorized.

When migration planning or execution changes local documents, apply
[local document delivery](../consolidate/references/local-document-delivery.md)
in progress and completion reports.

Inspect code, configuration, architectural decisions, existing migration work, and operational evidence. Establish behavior, interfaces, data ownership, deployment paths, and failure modes. Distinguish current production evidence from local tests, historical notes, and assumptions.

Inventory consumers for each capability: application flows, background jobs, queues, scheduled work, integrations, and older clients. Use available corporate search, service catalogs, relevant repositories, documentation, and responsible teams to discover dependencies beyond the local codebase. Corroborate discovery with runtime evidence where available. Track each consumer's disposition and ownership or usage gaps through transition and retirement. Absence of search results is not proof of disuse.

Discovery is sufficient to choose the first slice when its boundary, intended result, behavior to preserve, known consumers and prerequisites, and material unknowns are identified. Unknowns that affect its design or safe exposure remain explicit prerequisites.

## Choose and explain the strategy

Use **Strangler Fig** as the preferred approach: preserve the active path while building an alternative behind a replaceable boundary, then migrate bounded capabilities. Use feature flags and canaries for controlled activation. Choose gradual cohorts or a controlled switch according to the capability.

Prefer **vertical slices whenever feasible**: migrate one complete user journey, business capability, or representative traffic path through the necessary interface, behavior, data, and operations. Make each slice independently exposable, observable, and recoverable so it can deliver value and test migration assumptions before the next slice. If coupling prevents this, identify the smallest enabling work and explain how it leads to the first vertical slice.

Always consider routing affinity by user or organization, versioned contracts, backward-compatible evolution, staged read/write migration, and synchronization or replication. Select or combine them for the actual boundary, explaining material limitations or inapplicability. Affinity preserves destination choice; compatible contracts preserve interoperability; replication preserves specified data availability and consistency. Each addresses a different part of continuity.

For application decomposition or replacement behind a new boundary, read [boundaries and transitional architecture](references/boundaries-and-transition.md). Justify what separates and what stays together, including remaining execution, data, and deployment coupling. Define temporary transition mechanisms, their cost and ownership, and conditions for removal.

Conduct a collaborative investigation through progressive decisions. Use this cycle in the user's language, with descriptive work names:

1. Investigate available repository and operational evidence before asking for facts it can establish. Ask for missing goals, constraints, preferences, or decisions that materially affect the next action; continue independent investigation while awaiting answers.
2. Present a working hypothesis: what will migrate, which benefit it should deliver, and what must be preserved. Distinguish evidence from assumptions and incorporate corrections.
3. Select the next consequential unresolved decision. Explain today's flow and the intended flow, including what changes and remains shared. Compare viable alternatives and recommend one with its impact, costs, assumptions, and uncertainty. Explain named patterns in the project's terms.
4. Test the recommendation through a concrete normal journey and a failure scenario: where operations run, read and write, how their destination is selected, and how recovery works. Investigate consequences that could invalidate the recommendation and resolve interpretations that would change the design.
5. Consolidate the decision, rationale, assumptions, missing evidence, advancement conditions, and triggers for reconsideration using repository conventions. Carry accepted corrections through the plan, implementation, and validation.

Discuss one unresolved topic at a time. Reuse established answers and existing authorization rather than repeatedly requesting confirmation. Shared vocabulary alone does not establish shared understanding; concrete scenarios should expose meaningful differences. Repeat the cycle until the next slice can proceed, then revisit later decisions when relevant evidence becomes available.

This stage is complete for a slice when its expected benefit, boundary, affected journeys, selected strategy and rationale, intermediate states, data authority, continuity measures, recovery approach, and unresolved decisions are explicit. Resolve decisions required for the next action; retain later uncertainties as visible gates.

## Design coexistence and recovery

**No visible user interruption is the default acceptance requirement.** Define continuity for the affected journeys: availability, latency, session state, successful actions, and data correctness. Preserve it during coexistence, transition, recovery, and retirement. A deliberately accepted scream test can temporarily interrupt consumers; use the retirement procedure below for that exception.

Specify selection of old and new paths, coherence for the necessary lifetime, compatibility across versions, and treatment of in-flight and background work. Prefer stable canary assignment by user identity across journeys and return visits. When designing assignment, routing-policy overrides, or flag-service failure behavior, read [routing and recovery](references/routing-and-recovery.md).

Keep a tested return path until final migration acceptance, before agreed legacy retirement. This is expected for large migrations and preferred for small ones. For a small migration, recovery through new corrective work is an exceptional alternative requiring explicit acceptance of the point of no return, recovery work, and consequences. That exception preserves the default continuity requirement. Every recovery strategy must preserve valid user activity produced after activation.

Prefer one authoritative writer per datum or capability at each stage. Authority can stay with the old path or transfer by capability; define its owner and transfer conditions. Independent authoritative writes on both sides require a concrete need and an explained conflict-detection, resolution, and recovery strategy. Replication of one authoritative change is distinct from independent authority.

When changing persisted data, evolving an incompatible interface, or dividing a transactional workflow, read [contracts, data, and business recovery](references/contracts-data-and-recovery.md). For application decomposition, define contracts, ownership, authentication, and cross-boundary dependencies. For hosting changes, cover all affected traffic types and deployed-version compatibility.

Identify who operates the destination and sustains coexistence, including deployment access, monitoring, recovery responsibility, and capacity for running both paths. Resolve missing operational ownership before exposure.

## Organize and implement slices

Review existing work before adding tickets. Map bounded results, acceptance checks, and evidence gaps. Separate shared context from actual prerequisites, and build prerequisites from exposure prerequisites. State each prerequisite's reason and satisfaction condition; check direction, cycles, duplicate work, and obsolete dependencies.

Separate implementation from operational transition when their requirements differ. Keep later design awaiting pilot evidence explicit while accounting for recovery and eventual legacy removal. Assess specification gaps, autonomous readiness, and human decisions using repository rules. Maintain the plan, labels, decisions, and follow-up comments through its documented workflow, within authorized publication scope. Comments explain consequential changes, evidence, and next actions without duplicating the plan.

Implement authorized slices using the available **implement** skill, or the repository's implementation workflow if it is unavailable. Use its TDD, checks, and review discipline. Add migration-specific behavior at agreed public test seams: coexistence, compatibility, activation, and recovery. Existing agreements need not be requested again.

Where relevant legacy behavior lacks protection, add characterization tests at observable seams before replacing it. Preserve required behavior and distinguish accepted changes from defects discovered during characterization.

Turn agreed architectural goals into focused **fitness functions** where automation is useful: independent deployment checks, dependency restrictions, contract compatibility, or cross-component latency budgets. Explain what each check proves; choose checks from the intended benefit and enforce them at the appropriate build, deployment, or operational stage.

Build the alternative with activation under agreed control and observability for behavior comparison and failure detection. When using **shadow testing**, read [shadow testing and equivalence](references/shadow-testing.md) before implementing or operating the comparison, in either direction.

A slice is ready for canary exposure when its alternative behavior and continuity checks pass, required compatibility and recovery are verified, operational controls are usable, implementation checks and review are complete, and operational prerequisites are satisfied. Local checks establish implementation evidence, not production completion.

## Canary, transfer, and promote

Define promotion and recovery criteria before exposure. For each affected flow, specify the initial audience or operation set, journeys, baseline, validation scenarios, indicators, thresholds, observation period, and sufficient sample coverage. Prefer automated user journeys, with manual validation as a complement. Include representative reads, writes, full journeys, and relevant user and data conditions; a traffic percentage alone is insufficient coverage.

Within authorized operational scope, expose the canary and compare errors, latency, user outcomes, and data correctness against the baseline for every required flow. Evaluate the canary separately from the legacy path so aggregate success cannot hide failures. Resolve misleading probes, inconclusive comparisons, and measurement gaps before using them as promotion evidence.

Before each promotion or transfer of authority, revalidate the agreed recovery against current data, active versions, and in-flight work, including valid activity produced on the new path. Maintain this evidence until final migration acceptance. Expand traffic or perform the planned switch only when the slice's gate passes. Verify each transition and maintain consequential evidence. On a failed gate, stop expansion, execute the agreed recovery within authorized scope, and diagnose before retrying. Choose observation periods from the evidence required rather than arbitrary calendar waits.

If access or authorization is missing, complete independently possible work, prepare the concrete operational next step, and identify the unmet requirement and unexecuted actions. Distinguish completed implementation from actual exposure.

## Retire and verify completion

When unknown consumers may remain despite the inventory, consider a **scream test**. Read [scream tests](references/scream-tests.md) before proposing or operating either reversible disablement or consumer-controlled deprecation opt-in. Apply the procedure only within its explicitly accepted scope.

Retire the old path after the new path meets migration criteria and evidence shows required consumers, live versions, background jobs, and in-flight work no longer depend on it. Compare the intended benefits against their baseline, including architectural checks and operational results. Account for compatibility and recovery needs; elapsed time alone does not establish readiness.

Remove temporary flags, routing branches, adapters, synchronization, and infrastructure when no longer required, preserving shared resources and unrelated behavior. Verify affected journeys and operational evidence, including cessation of obsolete execution or consumption where applicable.

Refresh and verify records after authorized publication, preserving unrelated concurrent edits. Establish current state before retrying ambiguous writes to avoid duplicates.

Report behavior, validation evidence, actual exposure, recovery readiness, remaining dependencies, and outstanding actions. Distinguish a completed plan, implementation, partial rollout, and completed migration. The migration is complete only when the intended scope uses the new path, required continuity evidence is verified, and agreed retirement work is done.
