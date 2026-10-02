# Luna Deciders and Sol Judges — 2026-10-02

Replacing the judge on the original Luna deliberations resolved both remaining
problems: the wrong acceptance in case 15 became a justified escalation, and the
harness-induced escalation in case 12 became a correct acceptance. All 21 native
Sol/high judges completed. The resulting hybrid accepted 17 correct decisions,
accepted no wrong decisions, and correctly escalated seven cases.

This is an exploratory replay of the same synthetic architecture cases. The
configuration was chosen after observing the pilot, the Luna reports were reused,
and execution moved from CLI to native subagents. It does not qualify reliability
on untouched data or demonstrate the cheapest way to attain equal confidence.

## Observed comparison

All configurations use high effort. Three explicit human gates are mechanical
escalations common to every arm; they do not count as model reasoning successes.

| Measure | Single Luna | All-Luna ensemble | Luna deciders, Sol judge |
| --- | ---: | ---: | ---: |
| Cases | 24 | 24 | 24 |
| Accepted decisions | 21 | 17 | 17 |
| Wrong accepted decisions | 6 | 1 | 0 |
| Correct accepted decisions | 15 | 16 | 17 |
| Correct escalations, including three human gates | 3 | 6 | 7 |
| Unnecessary escalations | 0 | 1, caused by the checker | 0 |
| Eligible coverage | 100% | 94.1% | 100% |
| One-sided 95% binomial upper error bound among acceptances | 48.7% | 25.0% | 16.2% |
| Conditional API-equivalent USD | $0.075524 | $0.270341 | $3.146042 |

The hybrid's realized allocation was **11.64 times** the all-Luna ensemble's cost.
The hybrid includes 56 reused Luna deliberations and 21 newly executed Sol
judgments, rather than a new end-to-end run. No additional decider was needed
after the Sol judgments. The original 14 additional Luna reports remain included.
No proposed product or repository change was executed.

Seventeen accepted cases with zero errors still permit an upper error bound of
16.2% under the stated binomial assumptions. This does not meet the original 1%
target. The post-hoc variant selection adds another reason not to treat the sample
as confirmation. Product, code design, tone and manner, and factual truth remain
separate untested tracks.

## What the judge changed

In case 15, the three Luna deciders and original Luna judge accepted a plan scoring
99 in both capacity worlds. Sol identified feasible alternatives scoring 73 and 72
in the second world. The serial candidate was optimal only in the first world;
no supplied plan was optimal in both. Sol returned `challenge_majority` with
`ESCALATE`, correctly invoking the human route instead of accepting the shared error.

In case 12, Sol checked the explicit embedded required-operation list despite the
v1 checker's false unsupported warning. It confirmed the candidate's feasibility
and score 137, below the other feasible scores 138 and 212, and accepted it.

Those were the only final routing changes. Other Sol rationales also identified
incorrect comparative calculations or feasibility statements in Luna reports.
The scorer certifies selected choices and routing against the finite reference;
it does not certify every sentence of a judge's explanation.

## Runtime, isolation, and measured usage

The first CLI attempt made 21 requests for `gpt-6.1-sol/high`. All were rejected
with HTTP 400: the model was unsupported through this account's Codex CLI
authentication. The CLI emitted no completed judgments or token usage. Those
failures are preserved separately; they are not model decision errors, and their
unreported monetary usage is not inferred to be zero.

The fallback kept the requested model and effort and used 21 fresh native
subagents, with at most three running simultaneously. Local native turn metadata
confirmed `gpt-6.1-sol/high` in every thread. Each agent loaded only its assigned
original judge prompt and schema, then judged without research or further
delegation. A command-text audit found 132 input-loading calls and no other
assigned-path or tool-scope issues. These are instruction and audit controls;
the native interface cannot disable tool capabilities as the CLI adapter does.

Every original judge prompt's bytes were retained. The outer transport, system
context, and input-loading turns differed, so this is not a strict single-variable
model comparison. Aliases still do not identify immutable hosted weights.

Native token counts were recovered after execution from each thread's final
cumulative usage record. All 21 threads exposed usage, and the largest recorded
request had 81,943 input tokens, within the short-context price boundary. Reasoning
tokens are already included in output tokens and were not charged twice.

| Cost allocation | Uncached input | Cached input | Output | Equivalent USD |
| --- | ---: | ---: | ---: | ---: |
| Reused Luna deliberations | 564,836 | 639,744 | 244,729 | $0.185246 |
| Newly executed Sol judges, including input loading | 953,377 | 8,161,920 | 23,785 | $2.960796 |
| Hybrid path allocation | — | — | — | $3.146042 |

Conversions use standard short-context rates per million tokens: Luna
$0.10/$0.01/$0.50 and Sol $2.00/$0.10/$10.00 for uncached input, cached input,
and output. These are conditional API equivalents, not actual subscription bills.
Coordinator, preparation, analysis, and the rejected CLI attempt are excluded.
See the [official Sol model pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

Before execution, pricing the old Luna judge's exact token quantities at Sol rates
gave a hypothetical hybrid cost of $1.875412, or 6.94 times all-Luna. The measured
native allocation was higher because its token quantities and input-loading
execution differed. Neither figure predicts the cost of a fresh CLI or API hybrid.

## Artifacts and reproduction

- [Original all-Luna pilot](pilot-2026-10-02.md)
- Native replay configuration (`runs/judge-swap-sol-native-2026-10-02/frozen/plan.json`, local artifact)
- Native replay integrity manifest (`runs/judge-swap-sol-native-2026-10-02/freeze.json`, local artifact)
- Captured native judgments (`runs/judge-swap-sol-native-2026-10-02-live-01/native-receipts.json`, local artifact)
- Hybrid scores and allocations (`runs/judge-swap-sol-native-2026-10-02-live-01/scores.json`, local artifact)
- Native usage and scope audit (`runs/judge-swap-sol-native-2026-10-02-live-01/native-execution-audit.json`, local artifact)
- Rejected CLI attempt (`runs/judge-swap-sol-2026-10-02-live-01/run-summary.json`, local artifact)

The private local `runs/` artifacts preserve inputs, reports, thread identifiers,
source-log hashes, and normalized usage records. Exact outputs are not guaranteed
on replay. The CLI frozen runner deliberately rejects a native configuration;
native calls must be dispatched through the host's subagent interface.

```bash
python3 runs/judge-swap-sol-native-2026-10-02/frozen/judge_swap.py verify \
  --replay runs/judge-swap-sol-native-2026-10-02
python3 audit_native_replay.py \
  --output runs/judge-swap-sol-native-2026-10-02-live-01 \
  --session-dir /Users/betofrega/.codex/sessions/2026/10/02
python3 runs/judge-swap-sol-native-2026-10-02/frozen/judge_swap.py score \
  --replay runs/judge-swap-sol-native-2026-10-02 \
  --output runs/judge-swap-sol-native-2026-10-02-live-01
```

The [subsequent standalone Sol round](sol-single-2026-10-02.md) supplies the missing
same-case baseline. It accepted no wrong decisions and cost less, with one format
failure reducing eligible coverage to 94.1%. A qualifying comparison still needs
fresh cases, the corrected verifier, and a shared execution interface. Test total
cost at the same final error target and coverage floor. The current results make
a strong judge a useful candidate for calibration, not an unconditional ensemble
requirement.
