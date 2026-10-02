# Verify Supplied Claims

Create a bounded claim list from the current reports or judgment: exact claims,
their supplied source locations, and the decision premises they affect. Include
material new facts and missing or conflicting support. Keep decider votes and
preferred outcomes out of the verification assignment.

Dispatch a fresh read-only verifier under the entrypoint's dispatch rules. Give it
the claim list, necessary factual context, and authorized source access. Its task is
to check those claims against the actual sources; research belongs here, outside
the judge's context. Further claims discovered during verification remain qualified
until checked if they will materially influence the decision.

The verifier returns, for each claim:

- Confirmed, refuted, or unresolved status.
- Source location, excerpt or observed result, revision or observation time, and
  method used to check the claim.
- Any source limits, contradictions, or correction to the supplied assertion.

Attach findings without rewriting the deciders' historical reports. An unsupported
or refuted claim cannot serve as an established premise. An unresolved fact may be
irrelevant to a supported alternative; preserve that distinction.

**Complete when:** every listed material claim has a recorded verification outcome.
Return to the stage that requested verification. A failed attempt remains unresolved;
retrying the same uncertainty without a concrete way to settle it is an impasse.
