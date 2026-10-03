# Dispatch a CLI Wave

Use [dispatch.py](../scripts/dispatch.py) to execute already-prepared assignments.
Select the current environment's [Codex](codex.md) or [Claude](claude.md) adapter.
Keep the required `model-selection` decision and disclosure outside the runner.
The bundled runner requires macOS or Linux process groups for bounded cleanup.
Use native agents or a verified equivalent runner on other operating systems.

## Ready-job manifest

Use a JSON array. Each job contains `job_id`, `decision_id`, `role`, `provider`,
`model`, `effort`, `prompt_file`, `schema_file`, `tool_mode`, and optional `read_dirs`.
Roles are `initial_a`, `initial_b`, `additional`, `judge`, or `verifier`.
`tool_mode` is `none` or `files`; a judge always uses `none`. Paths are absolute.
Put the role instructions and admissible packet inside the prompt file. Use an
object response schema matching that role's required fields. Models and efforts
are selected by `model-selection`, never by the runner.

For file-reading jobs, list the authorized source directories in `read_dirs`.
The adapter exposes only its supported read-only capabilities; missing connectors
require a suitable native agent or a verified packet, not relaxed permissions.

Run with an unused output directory and explicit process cap and timeout:

```bash
python3 /path/to/autonomous-decisions/scripts/dispatch.py /tmp/ready-jobs.json \
  --output-dir /tmp/decision-wave-01 --max-concurrency 4 --timeout-seconds 300
```

The cap applies across both providers within this wave. Do not overlap waves unless
a separate shared limiter enforces the same global cap. Timeouts are recorded as
failed attempts and never automatically retried.
The runner terminates each job's remaining process group before releasing its slot,
including when the CLI leader has already exited. Cleanup has a finite deadline;
a cleanup failure stops subsequent dispatches and requires reconciliation.

Check exit status and each job's `status.json`, `report.json`, and logs before routing
its decision. A process exit alone is not a valid report. The runner rejects reused
output directories to prevent accidentally replaying a wave. The coordinator owns
cross-wave budgets, stage transitions, factual verification, and execution approval.

After changing the runner, run `python3 tests/test_dispatch.py` from the skill
directory. These transport regressions use fake CLIs and make no model calls.
