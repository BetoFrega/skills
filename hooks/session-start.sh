#!/usr/bin/env bash
# Routes every Claude session to beto-mode, including cloud sessions that have no
# user-level CLAUDE.md. Personal rules live in the separate beto-frega-personal plugin.
cat <<'RULES'
# beto-frega-skills

Use `beto-frega-skills:advisory` skill when stuck.

Before multi-step, design, implementation, debugging, planning, or review work, read
the `beto-frega-skills:beto-mode` skill and apply the principles it routes to.
RULES
