---
name: wizard
description: Wizard scripts for human-only provisioning, credential/CI setup, unfamiliar dashboards, migrations, or cutovers; use only for steps the agent cannot perform.
---

# Wizard

Copy [template.sh](template.sh); preserve the library above `STAGES` unchanged.
Author only the manual procedure's stages. Default to a scratch/`scripts/` file for
one run, deleted after completion; commit only when the user wants repeatable setup.

## Process

### 1. Scope the procedure

Inspect setup inputs: `.env*`, README, compose/framework configuration, and every
workflow `secrets.*`/`vars.*` reference; account for every referenced value. For transitions, inspect current/target states
and irreversible actions.

Show and confirm the ordered stages/produced values. Each value needs a verified
source, destination (`.env`, GitHub secret/variable, both, or none), and secrecy
classification. Pure-action stages need no captured value. Proceed when all are mapped.

### 2. Map each stage's journey

Write exact URLs, clicks/commands, value locations, and target variables. Verify
unfamiliar UI/commands against current documentation or user evidence; disclose gaps
instead of inventing steps. Every stage must be followable by a stranger.

### 3. Author the wizard

Replace the example with one focused `stage` per task, in dependency order; match
`TOTAL_STAGES` to the count. Use the template helpers for instructions, URLs, input,
persistence, and gates.

Open URLs before asking for values. Use `ask_secret` for secrets; `write_env` for
every persisted value; `set_secret` only for values CI needs.
Use `confirm` before irreversible actions. A stage clears the screen, so keep all
needed instructions within the current focused task. Do not modify the library.

### 4. Verify and hand off

Run `bash -n`, available `shellcheck`, and `chmod +x`. Do not run the interactive
procedure end-to-end yourself. Statically trace every scoped value to capture and
its promised destination; match `set_secret` names to actual CI `secrets.*` references.
Give the run command. For requested repeatable setup, commit and link from README.
