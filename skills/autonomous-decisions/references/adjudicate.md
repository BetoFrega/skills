# Assess the Current Reports

Apply the standing rules to discovered risks or conflicts before continuing.

Identify material facts newly introduced by deciders, contradictory evidence, and
missing support for premises needed to choose. Material new facts require separate
verification even when both deciders agree. If any such claims remain unchecked,
read [verify.md](verify.md) and complete that verification before continuing here.
Preserve original reports; attach confirmed, refuted, or unresolved findings.

## Establish the candidate

With only the initial pair, full agreement means the same proposal, scope,
conditions, and determinant premises. Normalize equivalent wording, preserving
material differences. Different weights on secondary benefits are compatible;
incompatible conditions or premises are disagreement. If agreement is ambiguous,
treat it as disagreement.

- If the initial pair fully agrees, their shared choice is the candidate.
- If the initial pair disagrees, read [reconsider.md](reconsider.md).
- After the additional decider returns, its choice is the candidate. Record whether
  it explains and resolves the initial points in dispute.

## Obtain a judgment

Read [judge.md](judge.md). Dispatch a fresh read-only judge using the entrypoint's
dispatch rules. Supply only the role, structured decider reports, verification
appendix, candidate, and whether the additional decider has been used. Include the
relevant context inside the reports. Give the judge no research tools or access to
the original conversation or external sources.

Collect the structured judgment and route it:

| Judgment | Coordinator action |
| --- | --- |
| `accept` | Record the accepted choice and rationale. Apply the standing rules and existing execution authorization, execute through the coordinator, and verify the result. |
| `reconsider` | If the additional decider is unused, read [reconsider.md](reconsider.md). Otherwise bring the unresolved decision to the user. |
| `challenge_majority` | Read [majority-challenge.md](majority-challenge.md) and bring the decision to the user. |
| `user_decision` | Bring the decision, options, recommendation, and precise reason to the user. |

Acceptance ends this decision's deliberation. An impasse after the additional
decider ends autonomous deliberation. Keep the accepted decision distinct from its
execution status and verification evidence. Proceed to another activated decision
only when its prerequisites are settled.
