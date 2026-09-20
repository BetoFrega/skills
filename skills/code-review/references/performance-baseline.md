# Universal performance baseline

Apply this baseline to every Performance review. A repository performance document
may add workloads, budgets, benchmarks, or stricter requirements; it does not remove
the obligation to surface a concrete degradation risk or accepted trade-off.

## Relevant costs

Inspect changes that can affect:

- user-facing latency, responsiveness, startup, or loading;
- throughput, algorithmic scaling, concurrency, or fan-out;
- CPU, memory, storage, queries, I/O, network transfer, payload or bundle size, and
  energy use;
- build, test, lint, type-check, packaging, deployment, and other development feedback
  loops, including lost caching, incremental work, or parallelism.

A development-loop cost is a finding when it grows out of proportion to the value
introduced by the change. Proportional growth is not a defect. Report clear
disproportion as a finding; label subjective cases `Potentially disproportionate` and
show the evidence for both cost and benefit.

## Causal threshold

A plausible degradation is actionable when the reviewer can show all four links:

1. the changed hunk;
2. additional work or lost efficiency caused by it;
3. a real execution path, workload, or scale condition where that difference matters;
4. the likely user or development consequence.

This chain, not a measurement, establishes the possibility. Omit abstract suspicions
that cannot identify the mechanism. When measurement confirms the effect, report the
regression and magnitude. When the chain is present but adequate measurement is not,
report `Impact: Unverified` and the smallest credible verification instead of asking
the user to discover the mechanism.

## Evidence and acknowledgement

Prefer repository-defined budgets and representative before-and-after evidence. Use or
request a benchmark only when it is already documented, reproducible, and proportionate
in cost. Do not create an ad hoc benchmark. Do not require measurement for changes
without a causal risk.

Every finding states whether the author has acknowledged the trade-off. Acceptance
may be recorded in chat, a pull request, an issue, or the spec; a pull-request warning
is preferable but not mandatory. Count acknowledgement only when the evidence shows
that the author understands:

- the degradation mechanism and affected flow;
- the known magnitude, or that it remains unknown;
- the scale or conditions that expose it;
- the benefit received in exchange;
- the credible verification or mitigation considered.

Acceptance resolves the awareness requirement, not the performance cost. Keep an
accepted trade-off in the report with its evidence. Use exactly one of these labels:

- `Author acknowledgement: Not found`
- `Author acknowledgement: Accepted trade-off — <evidence>`
