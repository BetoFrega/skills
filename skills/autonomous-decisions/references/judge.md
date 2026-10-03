# Judge Assignment

Judge the supplied candidate using only the decider reports and verification
appendix. Evaluate whether their embedded evidence supports the factual premises,
whether scope and constraints are respected, and whether the rationale is enough
to decide. Source references are provenance; evaluate the supplied excerpts and
results without opening sources, searching, or gathering new information.

Verification findings qualify the claims they checked. Agreement alone is not proof.
Identify unsupported premises and decision-changing uncertainty explicitly.

Count majority support using completed decider reports only. A strict majority is
more than half selecting an equivalent proposal, scope, and material conditions.
Judge and verifier findings are evidence, not votes. Keep earlier choices visible
even when later evidence undermines their rationale; describe that limitation.

If your supported preference differs from a strict majority, return
`challenge_majority`. This takes precedence over autonomous acceptance or requesting
another decider. State your supported preference and the strongest case on each side,
using only evidence already supplied. The user resolves this exception.

When no strict majority exists, you may accept the additional decider's candidate
if it demonstrably resolves the original objections with sufficient evidence.
Unanimity after reconsideration is not required. A different preferred choice,
insufficient evidence, or a continuing material dispute remains a user decision
once the additional decider has been used.

Return:

| Field | Required content |
| --- | --- |
| `outcome` | `accept`, `reconsider`, `challenge_majority`, or `user_decision`. |
| `candidate` | The submitted choice, scope, and conditions. |
| `preferred_choice` | Your supported preference, if any, from the supplied alternatives. |
| `evidence_assessment` | Supported premises, missing support, refutations, and unresolved material facts. |
| `agreement_assessment` | Agreement or disagreement, strict majority if present, and any original dispute resolved by the additional candidate. |
| `rationale` | Why evidence and reasoning are sufficient or insufficient. |
| `remaining_gap` | The concrete fact or reasoning that reconsideration would need to resolve. |

Use `accept` only for a supported candidate that clears constraints and relevant
uncertainties. Use `reconsider` for a concrete resolvable gap while the single
additional decider remains unused. Use `user_decision` for excluded risks, binding
conflicts, or an impasse that requires user judgment. Formulate no new alternative
and conduct no additional research.
