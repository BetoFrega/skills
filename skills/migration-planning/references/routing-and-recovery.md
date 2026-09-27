# Routing and recovery

Read when designing stable variant assignment, operational routing overrides, or behavior during feature-flag evaluation failures.

## Assign a variant and preserve the journey

Evaluate identity-based assignment through the feature-flag service or SDK and persistence of the assigned variant alongside the user's identity in application-controlled context. Session affinity alone does not establish persistence across return visits.

Define the journey's coherence unit and how all relevant components use the same assignment. Verify audience expansion, identity changes, and evaluation across components preserve the intended choice. Specify behavior for a user without an assignment, unavailable evaluation, and an unavailable or incompatible assigned path.

## Override persisted assignment deliberately

Separate stable user assignment from operational routing policy. The policy can override a choice for controlled recovery without deleting assignments and re-randomizing the audience.

For each operation:

1. Prefer an existing operation binding; otherwise use the user's persisted assignment. Assign and persist a variant under exposure policy when neither exists.
2. Check whether operational policy permits this operation on that path. Distinguish admission of new work from continuation of in-flight work: a draining path may allow only continuation.
3. If the path cannot be used, select recovery only when compatibility with the operation's data and state has been verified. Otherwise use its defined failure handling; automatic redirection to the legacy path is not inherently safe.

Define how deliberate recovery or retirement affects existing operations and future requests. Stable assignment preserves coherence while valid, not indefinite routing to an unavailable path.

## Propagate policy changes

Operator actions or authorized automated monitors can change operational policy. Define allowed triggers and resulting transitions so policy enforcement follows the agreed recovery strategy.

If routers cache a versioned local policy to avoid per-request external evaluation, specify propagation, cache validity, and stale-policy behavior. Verify the interval when different components hold different versions; updates are not instantly global.

Routing design is ready when assignment, admission, continuation, failure, policy-update, and recovery behavior are explicit and tested at relevant seams. Compatibility is established by the migration design and evidence, not inferred by the router.
