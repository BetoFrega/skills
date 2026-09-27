# Shadow testing and result equivalence

Read before implementing or operating shadow comparison, with either path serving as the active system.

## Isolate effects

The active path returns the official response and produces authoritative production effects. The shadow receives comparable operations for validation. Isolate or suppress its production writes, external calls, notifications, charges, emitted events, and downstream jobs. If testing writes is necessary, use isolated state and integrations.

Inspect indirect effects rather than assuming reads are harmless. Verify isolation at relevant seams, correlate comparison results, and bound shadow load so it preserves active-path continuity. Real-operation retries and replay also need appropriate idempotency; isolation does not provide that automatically.

## Define equivalence with the user

For each capability, identify the decisions, values, and observable outcomes that must match under equivalent inputs and relevant state. Compare semantic results rather than requiring byte-for-byte equality. Define justified tolerances and irrelevant differences, such as generated identifiers, while preserving meaningful behavior changes.

Account for write ordering, replication lag, and nondeterministic results. A stale comparator or different input state can make comparison inconclusive rather than prove a defect. Classify outcomes as equivalent, intentionally different and accepted, unexplained mismatch, or inconclusive.

## Compare in either direction

Initially the legacy path can serve users while the alternative is shadowed. After promotion, the new path can serve users while the legacy path becomes the isolated comparator. Transfer response and effect authority explicitly per exposed operation and apply the same equivalence criteria in both directions.

Reverse shadowing provides comparison evidence; legacy readiness for rollback still requires compatible current data and state. Isolated execution does not establish every property of real production operation, so combine it with implementation checks and canary evidence.

Shadow validation is ready to use as promotion evidence when effects are isolated, conditions are comparable, equivalence criteria are defined, and outcome classification exposes unexplained or inconclusive differences rather than hiding them.
