#!/usr/bin/env bash
# Injects Beto's global rules into cloud sessions, which have no ~/.claude/CLAUDE.md.
# Local sessions already load the same rules from that file, so skip them.
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
cat "$ROOT/global-rules.md"
