#!/usr/bin/env bash
# Injects Beto's global rules into every Claude session, local or cloud; Claude has
# no global CLAUDE.md for them.
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
cat "$ROOT/global-rules.md"
