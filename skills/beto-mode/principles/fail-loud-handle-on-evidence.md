# Fail Loud, Handle on Evidence

Handle what normal operation will hit. Make everything else fail loudly.

- A case is expected when the spec requires it, it has been observed, or it follows
  directly from the system's known scale and frequency (a multi-million-row backfill
  will be interrupted; a production network call will time out). Handle expected
  cases as ordinary behavior.
- Everything else is an edge case. Do not search for edge cases or reason through
  hypothetical chains to justify handling one. Let it fail.
- Where an edge case would be irreversible (data loss or corruption, security,
  money, privacy), prevent that outcome with the cheapest mechanism that refuses
  the operation: a constraint, a version check, an assertion, a rejected write.
  Refusing is enough; do not add retries, locks, queues, or reconciliation.
- Every refusal or unexpected failure emits a signal under the project's
  observability baseline, so someone learns it happened.
- When a signal shows an edge case recurring, it has become expected; handle it then.
- In plans and reviews, ask for the refusal and its signal, not for handling of a
  hypothetical case.
