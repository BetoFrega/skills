#!/usr/bin/env bash
# Reminds the agent of beto-mode every N prompts, so long sessions keep following
# it. Set BETO_MODE_REMINDER_EVERY to change N (default 10). Compaction is covered
# by session-start.sh, which runs again after it.
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
EVERY="${BETO_MODE_REMINDER_EVERY:-10}"
case "$EVERY" in '' | *[!0-9]* | 0) exit 0 ;; esac

# The counter sits next to the transcript, like the session memory file.
INPUT="$(cat 2>/dev/null)"
field() { printf '%s' "$INPUT" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p"; }
TRANSCRIPT="$(field transcript_path)"
SESSION="$(field session_id)"
if [ -n "$TRANSCRIPT" ]; then
  COUNTER="${TRANSCRIPT%.jsonl}.prompt-count"
elif [ -n "$SESSION" ]; then
  COUNTER="${HOME}/.claude/session-memory/${SESSION}.prompt-count"
else
  exit 0
fi

COUNT="$(cat "$COUNTER" 2>/dev/null)"
case "$COUNT" in '' | *[!0-9]*) COUNT=0 ;; esac
COUNT=$((COUNT + 1))
mkdir -p "$(dirname "$COUNTER")" 2>/dev/null
printf '%s\n' "$COUNT" > "$COUNTER" 2>/dev/null || exit 0
[ $((COUNT % EVERY)) -eq 0 ] && cat "$ROOT/hooks/beto-mode-reminder.md"
exit 0
