# Contracts, data, and business recovery

Read when changing persisted data, evolving an incompatible interface, or dividing a transactional workflow. Apply the relevant branches.

## Evolve incompatible contracts

Use **expand–migrate–contract** where it fits: first support old and new contracts, then migrate their consumers, then remove the old contract after retirement evidence passes. Define which deployed clients, readers, and writers are compatible at each intermediate state and what permits the next transition.

For staged read/write changes, establish compatible reads before enabling new writes. Verify recovery compatibility at every state; switching application code back is insufficient if the old version cannot interpret newly written data.

## Transfer persisted data

Define historical-data transfer, concurrent-change capture, completeness checks, and correctness. Make backfill restartable, with progress tracking and idempotent retries. Account for updates and deletions occurring during transfer; define how to catch up and prove acceptable completeness before handing over authority.

Replication or multiple writes require ordering, partial-failure handling, reconciliation, acceptable lag, and recovery compatibility. Define when authority transfers and how writes admitted around that transition are handled. Use the authoritative-writer policy from the main workflow.

Data transition is ready when compatible readers and writers, transfer progress, concurrent changes, authority handoff, and tested recovery are accounted for at the next exposure state.

## Preserve business invariants across boundaries

Identify invariants that currently depend on one transaction. Explain whether they remain atomic, tolerate temporary inconsistency, or require a different boundary. Consider keeping the transaction together before introducing distributed coordination.

When a multi-step workflow needs compensating actions, consider a **saga**: committed steps are followed by explicit business compensation when required, rather than one database rollback. Choose orchestration or choreography from the workflow's coordination, state, and failure needs. Explain the choice with a concrete operation.

Define retries, duplicate delivery, ordering, timeouts, partial completion, compensation failure, and reconciliation according to the workflow. A refund can compensate a charge, but cannot erase every consequence of the original payment. Preserve valid user activity and specify who resolves work that cannot be recovered automatically.

Business recovery is ready when acceptable partial states, completion or compensation behavior, and unresolved-work handling are explicit and verified at relevant seams. Distinguish these rules from traffic rollback and legacy-path readiness.

## Basis

[Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) and the data, workflow, and saga topics in [The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/). The operational guidance applies these topics to the migration workflow.
