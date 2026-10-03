# Luna-only Tudo Macaé decision experiment

Three real architecture/recovery questions were evaluated against a pinned, clean
local Tudo Macaé checkout at `7da1e3af1bb963d42cc75578463816155a63c3e9`, acquired on
2026-10-02. This is an exploratory case study of the decision protocol. It does not
estimate a model's general accuracy or verify the unnamed paper mentioned by the user.

## Decision results

| Decision | Candidate | Judge outcome | Practical meaning |
| --- | --- | --- | --- |
| Publication recovery after a committed write and failed post-commit effects | Existing state machine with bounded request-driven recovery | `user_decision` | The judge preferred A but required clearer evidence for recovery of an active `publishing` record and repeat-safe invalidation. No further decider was created. |
| Concurrent media finalization and quarantine expiry | Keep two transactions, verify races, separate staged-object reconciliation | `accept` | Accepted as a conditional research recommendation. Adapter concurrency and safe reclamation remain prerequisites to implementation. |
| Public-image revocation after partial receipt/purge/cleanup failures | Directed replay from the durable intent, with single recovery ownership | `accept` | Accepted as a conditional research recommendation. Serialization, repeated-effect safety, and provider evidence remain prerequisites to adoption. |

Accepted recommendations do not authorize implementation or production operations.
The source project was not modified; no product tests or provider operations were run.

## Method and recorded constraints

- Every decision used two fresh `gpt-6-luna/high` sessions with identical packets and
  authorized read-only resources. Each pair selected the same option ID, A, but their
  material conditions differed. Option labels alone were not treated as full agreement.
- Supplied material claims were checked by separate `gpt-6-luna/medium` verifiers.
  Narrow follow-ups supplied missing caller-keying source and reconciled provenance.
- Every case used exactly one additional `gpt-6-luna/high` decider, receiving the
  updated packet, verified facts and neutral disputes, without earlier votes or reports.
- Three fresh `gpt-6-luna/high` judges received only reports and verification appendices.
  Their recorded command counts were zero. An impasse after reconsideration ended
  autonomous deliberation for that case.
- Ready work ran in bounded waves through the new CLI runner, with a global cap of four
  and a 300-second deadline per assignment. No failed assignment was silently replayed.
- An additional Luna-only audit checks this case study; its findings are recorded below.

## Evidence quality and observed failures

The six initial reports supplied 53 evidence entries, including three packet-origin
observations. Of the 50 entries pointing to source files, 45 excerpts matched literally
and one more matched after whitespace normalization. This is a quotation/provenance
check, not a factual accuracy score. Composite excerpts need separate assessment.

One report presented `pending preserva private work` as part of a literal English ADR
quotation; the source instead says `` `pending` preserves private work ``. The underlying
state distinction can be supported by the source, but the quotation itself was changed.

Two first-pass verifiers ran Git metadata commands in copied source directories nested
inside the skills checkout. The returned HEAD belongs to the skills repository, not
Tudo Macaé. This is a scope/provenance failure despite all operations being read-only.
Original reports are preserved. A targeted check reconciled the labeled repository
observations; all 46 copied-source hashes remained consistent with their manifests.

The upload packet initially omitted the caller's intent-keying implementation. The
verifier preserved that uncertainty. Supplying the specific helper established the
source-level mapping from caller identity, operation and idempotency key to the stable
operation ID. This still does not prove deployed retry behavior.

## Audit

The broad `gpt-6-luna/high` audit exhausted its 300-second deadline after 42 completed
read commands and returned no verdict. That timeout is preserved at
its status (`wave-07-audit/experiment-audit/status.json`, local artifact); it was not silently replayed.
Three new, narrower tool-free audits with `gpt-6-luna/medium` then completed.

- Publication audit (`wave-08-bounded-audits/publication-recovery-audit/report.json`, local artifact):
  distinguishes the source-level `publishing` mapping from incomplete judge excerpts,
  while retaining adoption uncertainty about invalidation and pause races.
- Upload audit (`wave-08-bounded-audits/upload-finalization-audit/report.json`, local artifact):
  supports conditional research acceptance and identifies the unverified concurrency
  and staged-object lifecycle prerequisites, plus incomplete provenance metadata in
  the targeted caller-mapping report.
- Image audit (`wave-08-bounded-audits/image-revocation-recovery-audit/report.json`, local artifact):
  supports conditional research acceptance but warns that calling replay “idempotent”
  overstates a property the sources and provider evidence have not established.

The image audit also introduced a factual error: it said a missing revocation receipt
preserves an origin `403`. A tool-free Luna/low factual check (`wave-09-audit-factual-check/audit-receipt-status-verifier/report.json`, local artifact)
refuted that claim using the actual function. Its initialization is
`let status = originStatus === 404 ? 404 : originStatus === 410 ? 410 : 502;`.
An absent receipt keeps `502` for origin `403`, and `404` for origin `404`.
The original audit is preserved and must be read with this correction.

The case results show useful domain reasoning and explicit uncertainty handling.
They also show that light-model consensus and an additional model audit can retain
or introduce errors. Source/provenance checks, bounded scopes and escalation gates
remain necessary parts of this demonstrated workflow. The data do not establish
unattended production reliability or a general model accuracy percentage.

## Execution footprint

23 fresh CLI sessions were started; 22 completed and one audit timed out. Every configured model was `gpt-6-luna`. The decision protocol itself used 18 successful assignments: six initial deciders, three additional deciders, six factual verifiers and three judges. Five additional audit/check assignments account for the remaining sessions.

Peak overlapping assignment lifetimes: 4. First dispatch to final completion: 37.4 minutes, including coordinator preparation between waves. All three judge command counts were zero.

The CLI reported 1,675,012 input tokens, including 959,232 cached input tokens, and 82,561 output tokens for emitted completion records. Usage for the timed-out audit is unavailable. These are cumulative session counts and do not establish monetary cost.

## Reproducibility and limits

The repository includes this report, the assessment rubric, and the
[aggregate measurements](measurements-summary.json). Source snapshots, packets,
raw reports, and execution logs are retained locally and excluded from Git.

Index and activation/execution boundaries (`index.json`, local artifact), [pre-registered assessment
rubric](assessment-rubric.json), initial quotation checks (`initial-provenance-checks.json`, local artifact)
and per-assignment execution measurements (`execution-measurements.json`, local artifact) are retained.
Each case directory contains its original packet, source manifests and source copies.
The `wave-*` directories retain exact reports, status, JSONL events and stderr.
`*-jobs.json` files record explicit provider, model, effort and source permissions.

Replay using a new output directory; reused output directories are intentionally
rejected. Replays consume new model calls and are not included in these results.

This study used only one lightweight model family, three selected cases, and no
single-agent baseline, repeated sampling, independent human design oracle or strong
model comparison. The final audit also uses Luna and can share blind spots. Source
inspection and authored tests cannot establish runtime, provider, deployment or safety
guarantees. General reliability percentages and claims about Haiku are unsupported.
