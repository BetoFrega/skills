# Prospective Decision Calibration

This evaluation separates two questions: whether new local cases can be reproduced,
and whether a particular model configuration reliably resolves a particular decision
class. It does not treat agent agreement as the answer key.

## What is implemented

`benchmark.py` freezes the plan, prompts, generator, and CLI transport, then draws a
new 256-bit local seed. It produces private answer keys and new synthetic instances,
checks byte-identical regeneration, runs paired individual and ensemble protocols,
and scores their decisions with an executable reference.

The implemented generator is an **architecture constraint diagnostic**: dependency
ordering, capacity, concurrency, retries, deadlines, competing costs, and uncertainty
across possible worlds. Its three scenario names evoke publication, upload, and image
recovery. They are fictional controlled problems, not claims about Tudo Macaé or
three independent decision classes. Operation names add no hidden domain constraints.
This diagnostic does not establish skill in open-ended architecture or product design.

The [2026-10-02 live pilot report](pilot-2026-10-02.md) records 24 paired cases and
98 completed Luna/high calls, including observed errors, costs, and a source-checking
defect. Its frozen v1 results remain unchanged. Those ensembles exposed peer reports
to the additional decider, so their reliability and cost describe an anchored variant,
not the skill's blind reconsideration protocol. Current v3 retains v2's checker and
scheduling fixes, removes peer reports and judge preferences from reconsideration,
validates complete response schemas, and repairs portable scope and accounting
checks. It has regression coverage but no fresh live confirmation.

The other tracks and their required references are specified in
[calibration-plan.json](calibration-plan.json). Product, architecture, code design,
tone and manner, and factual truth need separate results, targets, and model choices.
An average across them cannot qualify an untested class. Subtypes and consequences
can require further separation within a class.

## Prospective exposure and reproducibility

The seed is sampled **after** configurations, role prompts, scoring rules, and budgets
are hashed into the frozen artifacts. Both inputs and keys have integrity hashes.
Relations, durations, capacity worlds, retry properties, alternatives, and objective
weights vary, in addition to opaque identifiers and a 128-bit case nonce.

Exact cases are created locally at evaluation time. This gives strong resistance to
reuse of a memorized benchmark instance. It cannot independently prove that a
provider has never trained on equivalent reasoning, templates, or an accidentally
matching instance. A new nonce alone would only make the text new; the varying
decision structure is essential. Record the narrower prospective-exposure claim.

Reproduction means identical packets, references, protocols, and scoring. Hosted
model outputs can vary; aliases do not pin provider weights. Record CLI versions,
requested models and efforts, observed model metadata, timestamps, reports, failures,
and emitted token usage. Use immutable model snapshots where the provider supports
them. Repetitions characterize model variation without increasing the independent
case count.

Keep development cases separate. Cases exposed to tested models or used to tune
configurations cannot be reused as an untouched confirmation set. Independent
reference raters may inspect private cases to establish sealed labels. After changing the generator,
prompts, rubric, configurations, or budgets based on pilot outcomes, freeze the new
plan and generate a fresh confirmation set. Replaying an old seed audits an old run;
it does not create a new uncontaminated evaluation.

## References by decision class

| Class | Objective reference | Judgment reference |
| --- | --- | --- |
| Product | Binding priorities, budget, scope, and evidence checks | Domain owner labels acceptable tradeoffs before model runs |
| Architecture | Executable invariants, failure traces, or a finite model | Independent engineering review of boundaries and operational tradeoffs |
| Code design | Hidden behavioral tests and generated counterexamples | Frozen rubric for API, cohesion, clarity, and repository fit |
| Tone and manner | Explicit language and information requirements | Blind human judgments against approved voice examples and rating anchors |
| Factual truth | Generated fact records or frozen authoritative source snapshots | Human resolution where real-world sources leave material ambiguity |

Controlled utility calculations test adherence to a specified product objective;
they do not establish that the objective represents user value. Passing code tests
does not establish good code design. A tone checklist does not settle voice quality.
Reference labels can allow several acceptable choices and required user escalation.
Use these limits when interpreting results.

Human references are sealed before model execution. Human outcome raters see
anonymized responses in randomized order, with the same rubric for every arm.
Record disagreement rather than making a tested model its own sole truth reference.
Prepare and approve actual voice or value rubrics before claiming results in those
tracks; the current files do not invent the user's preferences.

## Run the controlled pilot

The example plan preserves the prior Luna-only experiment constraint. It compares a
single `gpt-6-luna/high` with an all-Luna ensemble using high effort for every decider
and judge. The ensemble selection is provisional. To compare Terra, Sol, or Claude,
add explicitly authorized arms and live-supported configurations **before prepare**.
Record each arm's `model-selection` rationale. Re-resolve rates before a new study;
the sample prices are conditional API equivalents, not actual subscription charges.

Run from this directory:

```bash
python3 -m unittest -v test_benchmark.py
python3 benchmark.py prepare --plan plan.example.json --output runs/pilot-01
python3 runs/pilot-01/frozen/benchmark.py verify --suite runs/pilot-01
```

Preparation and verification make **zero model calls**. The following command makes
live model calls and must be run only under the user's authorized model and budget
constraints. The frozen plan is disclosed before dispatch; actual configurations
and failures are recorded for every assignment.

```bash
python3 runs/pilot-01/frozen/benchmark.py run \
  --suite runs/pilot-01 --output runs/pilot-01-output
python3 runs/pilot-01/frozen/benchmark.py score \
  --suite runs/pilot-01 --output runs/pilot-01-output
python3 audit_execution.py \
  --suite runs/pilot-01 --output runs/pilot-01-output
```

Each provider job has fresh context and tools disabled. Its prompt contains only
its role's admitted inputs. Deciders receive the original packet; an additional
decider receives verified literal facts and neutral checks covering all objections
allowed by this finite rulebook, with no peer reports, votes, or judge preferences.
Judges receive prior reports and literal source checks. The runner never reads
private keys or the private seed. The offline verifier and scorer do read them.
Tool restrictions are the exposure boundary; Unix directory modes alone do not
isolate processes running as the same user. The oracle source is not secret, while
the generated instances and their labels remain private until needed.

Within an ensemble, two initial reports are compared by choice, scope, conditions,
and determinant literal premises. Different premises conservatively trigger the
single additional decider. A judge receives reports with their admitted context and
literal source checks, and uses no research tools. Reconsideration may consume the
one additional decider; a continuing gap or majority challenge escalates. At most
three decider calls and two judge calls complete per decision. Failures remain
failures, with no automatic retries. Complete schemas are checked before acceptance
and scoring, including required fields, nested types, and forbidden properties.
The standard-library validator covers the frozen formats' schema keywords and
rejects unsupported keywords. Its source is frozen alongside new runners.
A shared semaphore caps all live jobs across
arms, repetitions, and decision stages. No proposal is executed.

The source checker compares literal input facts only. It does not calculate
feasibility, optimize schedules, or disclose the private answer. Determinant derived
reasoning remains the agents' responsibility and is evaluated by the private scorer.

The native scope audit resolves literal paths against the supplied workspace and
recorded working directory. It recognizes bounded `cat`, `sed`, `dd`, and Python
input-slicing reads; unfamiliar or dynamic commands require review. Working-directory
metadata grants no access to neighboring files. This remains a command-text check,
not an operating-system boundary. A gate-only CLI run has zero job wall duration.
Missing, incomplete, or invalid token-category rate maps count as unknown pricing;
zero-valued complete rate maps are valid. Known cost is a subtotal when any job is
unpriced.
This controlled variant needs no external factual research and therefore no research
verifier agent. It is not a test of discovering unknown facts with tools.

## Interpret results

Score every arm on the same cases. Report wrong accepted decisions, justified and
unnecessary escalations, failures, eligible coverage, known token cost, unknown cost,
and time. A configuration cannot appear reliable merely by escalating everything.
Missing timed-out usage prevents claiming a complete monetary total.

The optional post-run audit checks the references with a separate discrete-time
implementation, plus prompt hashes, session IDs, actual overlap, CLI model headers,
and completed tool-event types. It leaves frozen keys and scores unchanged. This
frozen v1 scheduler queued individual calls before initial ensemble pairs; decision
wall time includes that ordering and is unsuitable as an isolated latency comparison.
Report this queue effect when interpreting the pilot. Current v2 schedules both
arms' initial children through the same event-loop path and preserves the planned
interleaving; this fix does not retroactively change v1 observations.

The sample target is at most 1% wrong accepted decisions with a one-sided 95%
binomial bound and at least 90% eligible coverage. The 24-case example is a pipeline
pilot and will normally be far too small to qualify. Even zero errors require at
least 299 independent accepted cases for this particular binomial bound to fall
below 1%; this assumes the sampled cases represent the target distribution. It
does not certify real product decisions. Report each repetition separately.

Choose the cheapest configuration among those meeting the same class-specific
target and coverage floor on untouched confirmation data. If none qualifies, the
comparison is inconclusive. Do not infer equal reliability from overlapping
confidence intervals, agreement rates, or three successful examples.

The scorer checks selected choices and routing. It does not certify the semantic
truth of every sentence in a rationale. Broader class evaluations need the separate
claim and human-rubric checks described above before they can support broader trust.

## Compare a Sol judge on the same Luna deliberations

The [2026-10-02 hybrid replay](judge-swap-2026-10-02.md) records zero wrong accepted
decisions, full eligible coverage, actual native token counts, and the runtime
differences that limit a direct cost or model-effect comparison.

`judge_swap.py` prepares a post-hoc substitution of `gpt-6.1-sol/high` for the
original ensemble's `gpt-6-luna/high` judge. Its first judgment uses the exact original
prompt, including admitted context and v1 literal-checker warnings. Original Luna
reports remain fixed. One new Luna/high decider and one further Sol/high judgment
are allowed only if reconsideration uses a previously unused additional slot.
The original majority-challenge and human-gate routes remain in force.

```bash
python3 -m unittest -v test_judge_swap.py
python3 judge_swap.py prepare \
  --suite runs/pilot-2026-10-02 \
  --original runs/pilot-2026-10-02-live-01 \
  --output runs/judge-swap-sol-01
python3 runs/judge-swap-sol-01/frozen/judge_swap.py verify \
  --replay runs/judge-swap-sol-01
```

Preparation makes no model calls. Freeze artifacts record exact configurations,
source references, model-selection rationale, and conditional rates. Running the
following command requires authorization for Sol judges and any bounded Luna
reconsideration calls; the prior Luna-only constraint does not authorize Sol by itself.

```bash
python3 runs/judge-swap-sol-01/frozen/judge_swap.py run \
  --replay runs/judge-swap-sol-01 --output runs/judge-swap-sol-01-output
python3 runs/judge-swap-sol-01/frozen/judge_swap.py score \
  --replay runs/judge-swap-sol-01 --output runs/judge-swap-sol-01-output
```

Scoring distinguishes new-call expenditure from the reused deliberations' allocated
cost. Their sum estimates this realized hybrid path; it is not the cost of a fresh
end-to-end run. Choosing this variant after observing pilot failures makes it
exploratory. It retains the original checker defect to avoid changing two variables
at once and supplies no untouched confirmation data. Qualifying a hybrid requires
a separate prospective study, including a single Sol baseline at matched targets.

For a host-native variant, prepare with `--judge-provider native_collaboration` and
dispatch fresh agents through that host's subagent interface. The CLI `run` command
rejects this mode. Preserve each returned report, explicit model and effort, assigned
input, native thread ID, and final routing under the same bounded protocol. Native
input loading is a tool step; document that difference from the tool-disabled CLI
protocol. `audit_native_replay.py` can recover cumulative usage from local native
rollouts and inspect assigned-input reads. Missing usage remains unknown, and the
scorer withholds a complete monetary total until every assignment has usage.

## Compare one standalone Sol on the original cases

The [2026-10-02 standalone Sol result](sol-single-2026-10-02.md) completes the
same-case comparison: zero wrong accepted decisions, one invalid-JSON failure,
94.1% eligible coverage, and $1.210454 in conditional API-equivalent cost.

`native_single.py` prepares one `gpt-6.1-sol/high` assignment for each of the
original 21 reasoning cases. The other three cases retain their explicit human
gate without a model call. It copies each original standalone Luna prompt byte
for byte, supplies no peer reports or judge, and freezes the configuration before
dispatch. This is one round on reused cases, not a new confirmation set.

```bash
python3 -m unittest -v test_native_single.py
python3 native_single.py prepare \
  --suite runs/pilot-2026-10-02 \
  --original runs/pilot-2026-10-02-live-01 \
  --output runs/sol-single-native-01
python3 runs/sol-single-native-01/frozen/native_single.py verify \
  --output runs/sol-single-native-01
```

Preparation makes no model calls. Dispatch through the host's native subagent
interface only under authorization for the standalone Sol comparison. Use fresh
contexts, explicit Sol/high assignments, and at most three concurrent children.
Each child may load only its assigned prompt and decider schema, then answer
without tools or further delegation. Name children `/root/sol_single_01`, and so
on, using their case indices; the collector matches these names. Do not dispatch
the human-gate cases. Preserve a failed assignment rather than automatically
rerunning a case.

The collector extracts exact returned JSON and native thread identities from the
root's local rollout. After all responses arrive, recover usage from the native
logs and score against the original sealed references:

```bash
python3 native_single_results.py collect \
  --output runs/sol-single-native-01 --root-rollout /absolute/root-rollout.jsonl
python3 audit_native_replay.py \
  --output runs/sol-single-native-01 --session-dir /absolute/native-session-directory
python3 native_single_results.py score \
  --output runs/sol-single-native-01
```

Native tools are restricted by assignment and audited afterward; this does not
provide the CLI baseline's disabled-tool boundary. The prompt bytes match, while
system context and input-loading turns differ. Native token totals include these
loading turns. The scorer rejects missing outcomes and withholds a complete
monetary total when usage is missing.

The offline `native_single_results.py` adapter retains malformed responses as
failures and counts their token usage. It was added after the strict frozen
collector encountered invalid JSON in case 14; the frozen runner, prompts, keys,
and model responses remain unchanged. The adapter never repairs or retries an
answer. Its hash and reason are recorded in the run summary. An extracted choice
from malformed text can be reported diagnostically, while the outcome stays failed.

Procedural generation with verifiable references follows the general approach in
[Reasoning Gym](https://arxiv.org/abs/2505.24760). That paper is methodological context,
not validation of this generator or evidence about Luna, Terra, Sol, or Haiku.
