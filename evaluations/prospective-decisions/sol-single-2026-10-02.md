# Standalone Sol on the Original Cases — 2026-10-02

One standalone `gpt-6.1-sol/high` round accepted 16 correct decisions, accepted no
wrong decisions, and correctly escalated seven cases. One further response failed
because its JSON omitted commas. Its indicated choice matches the reference, but
the strict protocol counts that response as a failure, giving 94.1% eligible
coverage. No case was retried, reviewed by another model, or repaired.

The measured conditional API-equivalent cost was **$1.210454**, 61.5% below the
Luna-decider/Sol-judge hybrid's $3.146042 allocation. This fills the requested
standalone baseline on the same cases. It does not establish equal reliability or
the cheapest configuration at the original confidence target.

## Four configurations on the same 24 cases

All assignments use high effort. Twenty-one cases require model reasoning; the
three explicit human gates are mechanical escalations common to every arm.

| Measure | Single Luna | All-Luna ensemble | Luna deciders, Sol judge | Single Sol |
| --- | ---: | ---: | ---: | ---: |
| Cases | 24 | 24 | 24 | 24 |
| Accepted decisions | 21 | 17 | 17 | 16 |
| Correct accepted decisions | 15 | 16 | 17 | 16 |
| Wrong accepted decisions | 6 | 1 | 0 | 0 |
| Correct escalations, including three human gates | 3 | 6 | 7 | 7 |
| Unnecessary escalations | 0 | 1, checker defect | 0 | 0 |
| Failed responses | 0 | 0 | 0 | 1, invalid JSON |
| Eligible coverage | 100% | 94.1% | 100% | 94.1% |
| One-sided 95% binomial upper error bound among acceptances | 48.7% | 25.0% | 16.2% | 17.1% |
| Conditional API-equivalent USD | $0.075524 | $0.270341 | $3.146042 | $1.210454 |

The hybrid reused the original Luna reports and executed new Sol judgments. The
standalone Sol arm executed 21 independent decision assignments and had no judge.
Assignment counts are not counts of underlying native model requests: input
loading adds model turns, and their tokens are included in the measured cost.

The single Sol accepted no wrong decisions at lower measured cost than the hybrid.
Its format failure lowered effective coverage. The indicated choices in all 21
Sol responses match the finite reference when the malformed response's explicit
choice field is inspected diagnostically; that observation does not replace the
strict failure or turn its choice into an accepted decision.

## What happened in the difficult cases

| Case index | Prior observation | Standalone Sol outcome |
| --- | --- | --- |
| 2 | Single Luna accepted an infeasible plan | Correct acceptance |
| 5 | Single Luna accepted a plan optimal in only one world | Correct escalation |
| 10 | Single Luna accepted a plan optimal in only one world | Correct escalation |
| 12 | All-Luna ensemble escalated because of a checker defect | Correct acceptance |
| 14 | Single Luna accepted an infeasible plan | Invalid JSON; indicated choice is correct, counted as failure |
| 15 | Three Luna deciders and the Luna judge accepted the same suboptimal plan | Correct escalation |
| 20 | Single Luna accepted a plan optimal in only one world | Correct escalation |

In case 15, Sol independently found the serial option's score of 99 and the
capacity-2 alternatives' scores of 73 and 72. The serial plan is optimal in the
capacity-1 world, while the best parallel plan is infeasible there. No option is
optimal in both worlds, requiring escalation. No prior decider or judge report
was supplied to the standalone agent.

Case 14 returned the correct choice `plan-949b86667107`, whose feasible score is
140, but omitted separators between JSON fields. The native transport had received
the schema as an instruction; it did not enforce structured output during
generation. The original Luna CLI transport enforced a JSON schema. This execution
difference matters when comparing format failure rates. The raw native response
is preserved, its choice is not accepted, and its token usage remains included.

## Integrity, execution, and accounting

All original standalone Luna prompt bytes were copied and verified before dispatch.
The same packet, rulebook, options, and sealed reference were used for every arm.
The standalone configuration, source hashes, and rates were frozen before its
first assignment. Selecting the Sol arm after seeing prior results still makes
the comparison exploratory; it supplies no untouched confirmation data.

The host dispatched 21 fresh native contexts with at most three active children.
Every local turn record confirmed `gpt-6.1-sol/high`. Each agent performed one
input-loading tool call reading only its assigned prompt and schema, then returned
its decision without research, calculation tools, further delegation, or mutations.
The scope audit found no remaining assigned-input issues. The native interface
restricts tools by instruction and subsequent audit, rather than disabling them
as the CLI does. System context and loading turns also differ from the Luna CLI
baseline. Neither aliases nor one-round outputs identify immutable model behavior.

A subsequent offline check against the complete frozen decider schema confirmed
the same 20 valid reports and one already recorded invalid response. The portable
scope checker admitted all 21 recorded input reads. No model call or frozen artifact
was changed. The all-Luna and hybrid comparators reused additional-decider inputs
with visible peer reports; their cost and reliability describe an anchored variant,
not the skill's blind reconsideration protocol.

The first command-text audit falsely flagged case 21's working-directory metadata
when its `cat` command used the two assigned relative paths. The checker now admits
that exact two-file command without granting reads elsewhere in the directory.
Regression checks cover both the permitted read and forbidden neighboring reads;
the original flagged audit is retained separately.

The original frozen collector stopped at case 14's malformed JSON. An offline
adapter was then added to record the failure and collect every other response,
without changing frozen inputs, responses, or choices. Its hash and reason are
recorded in the run summary. Regression checks cover raw-output preservation,
failure counting, missing usage, and rejection of duplicate answers. No new model
call was made to resolve either collection or audit issue.

The literal source checker confirmed all **400 submitted claims in the 20 valid
reports**, with no unsupported claims. This post-run check does not certify every
derived comparison, calculation, or sentence of a rationale. It excludes the
malformed report from structured claim checking.

| Token allocation | Tokens | Equivalent USD |
| --- | ---: | ---: |
| Uncached input | 138,138 | $0.276276 |
| Cached input | 1,438,080 | $0.143808 |
| Output, including reasoning | 79,037 | $0.790370 |
| Total | — | $1.210454 |

All 21 native sessions exposed cumulative usage, including the failed response.
The 7,315 reasoning output tokens are already included in total output and were
not counted twice. The largest request had 40,412 input tokens, below the
short-context price boundary. Conversion uses standard Sol rates per million
tokens of $2.00 uncached input, $0.10 cached input, and $10.00 output. See the
[official Sol model pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

These are conditional API equivalents, not account charges. They exclude
coordinator, preparation, analysis, and the prior rejected Sol CLI attempt. The
high cached-input share and host-specific input-loading behavior mean this cost
does not predict a fresh deployment's uncached cost. Recorded dispatch-to-completion
time was 20 minutes 9 seconds, including coordination; it is not a controlled
latency comparison with the other arms.

## Confidence and scope

Zero errors among 16 accepted responses still yield a one-sided 95% binomial upper
error bound of 17.1%. None of the four configurations meets the original 1% error
target. The reused cases and selection after observing results also prevent a
confirmatory reliability claim. Equivalent error counts, overlapping intervals,
or an extracted correct choice do not prove equal reliability.

These are synthetic architecture constraint problems with finite references.
Product, open-ended architecture, code design, tone and manner, and factual truth
remain separate unqualified decision tracks. No change to Tudo Macaé was executed.
The requested round is complete; no additional cases or repetitions were started.

## Artifacts and reproduction

- [Original Luna pilot](pilot-2026-10-02.md)
- [Hybrid replay](judge-swap-2026-10-02.md)
- Standalone configuration (`runs/sol-single-native-2026-10-02/frozen/plan.json`, local artifact)
- Integrity manifest (`runs/sol-single-native-2026-10-02/freeze.json`, local artifact)
- Exact native receipts (`runs/sol-single-native-2026-10-02/native-receipts.json`, local artifact)
- Strict scores (`runs/sol-single-native-2026-10-02/scores.json`, local artifact)
- Four-arm comparison and failed-choice diagnostic (`runs/sol-single-native-2026-10-02/comparison.json`, local artifact)
- Raw failed response (`runs/sol-single-native-2026-10-02/c00014-r0-sol-single/raw-report.txt`, local artifact)
- Native usage and scope audit (`runs/sol-single-native-2026-10-02/native-execution-audit.json`, local artifact)
- Literal claim audit (`runs/sol-single-native-2026-10-02/literal-claim-audit.json`, local artifact)
- Concurrency and completion audit (`runs/sol-single-native-2026-10-02/coordination-audit.json`, local artifact)

The private local `runs/` artifacts retain the original inputs, reports, failures,
thread identities, source-log hashes, and normalized token records. Verification,
collection, accounting, and scoring make no inference calls:

```bash
python3 runs/sol-single-native-2026-10-02/frozen/native_single.py verify \
  --output runs/sol-single-native-2026-10-02
python3 native_single_results.py collect \
  --output runs/sol-single-native-2026-10-02 \
  --root-rollout /absolute/root-rollout.jsonl
python3 audit_native_replay.py \
  --output runs/sol-single-native-2026-10-02 \
  --session-dir /absolute/native-session-directory
python3 native_single_results.py score \
  --output runs/sol-single-native-2026-10-02
```
