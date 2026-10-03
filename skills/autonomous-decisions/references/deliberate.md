# Obtain Independent Deliberations

Read [decider.md](decider.md) and dispatch two fresh read-only deciders under the
entrypoint's dispatch rules. Give both the same packet and resource permissions.
They may investigate independently and run concurrently. Keep their findings,
preferred choices, and reasoning isolated until both return.

Each assignment receives only the packet and decider role. Independence does not
require different models: select each configuration with `model-selection`.

Collect the two structured reports. If an assignment fails or returns an incomplete
report, report the specific gap rather than treating it as agreement or substituting
the coordinator's opinion. Distinguish a tool failure from a completed deliberation.

**Complete when:** two complete reports for the same decision packet are recorded,
including considered options, advantages, disadvantages, choice, reasoning, and
the evidence supporting material claims. Then read [adjudicate.md](adjudicate.md).
