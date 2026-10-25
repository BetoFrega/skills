#!/usr/bin/env bash
# Routes every Claude session to beto-mode. Personal rules live in the separate
# beto-frega-personal plugin.
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
printf '# beto-frega-skills\n\n'
cat "$ROOT/hooks/beto-mode-routing.md"
