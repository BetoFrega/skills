#!/usr/bin/env bash
# Routes every Claude session to beto-mode and points it to its session memory
# file. Personal rules live in the separate beto-frega-personal plugin.
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
printf '# beto-frega-skills\n\n'
cat "$ROOT/hooks/beto-mode-routing.md"

# The hook input is one JSON object on stdin. The memory file sits next to the
# transcript, so it lasts as long as the session can be resumed.
INPUT="$(cat 2>/dev/null)"
field() { printf '%s' "$INPUT" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p"; }
TRANSCRIPT="$(field transcript_path)"
SOURCE="$(field source)"
SESSION="$(field session_id)"
if [ -n "$TRANSCRIPT" ]; then
  MEMORY="${TRANSCRIPT%.jsonl}.memory.md"
elif [ -n "$SESSION" ]; then
  MEMORY="${HOME}/.claude/session-memory/${SESSION}.md"
else
  exit 0
fi
printf '\nSession memory file: `%s`\n' "$MEMORY"
if [ -f "$MEMORY" ] && { [ "$SOURCE" = compact ] || [ "$SOURCE" = resume ]; }; then
  printf 'The session was compacted or resumed. Read the session memory file now.\n'
fi
