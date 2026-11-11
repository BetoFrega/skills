#!/usr/bin/env bash
# Rings a soft sound while the agent waits for Beto, until he answers.
#
#   alarm.sh start   the agent stopped or asked for input: ring in the background
#   alarm.sh stop    Beto answered or the agent is working again: silence it
#   alarm.sh tool    PreToolUse: AskUserQuestion waits for Beto, other tools mean work
#
# The first ring waits BETO_ALARM_GRACE seconds (20), so nothing sounds when Beto is
# watching. Then the gap starts at BETO_ALARM_FIRST (30) and doubles up to
# BETO_ALARM_MAX (300). After BETO_ALARM_GIVE_UP seconds (1800) it gives up.
# BETO_ALARM_SOUND picks a sound file; BETO_ALARM=0 turns the alarm off.
# Cloud sessions are skipped: their sound would play in the container.

ACTION="${1:-}"
INPUT="$(cat 2>/dev/null)"
[ "${BETO_ALARM:-1}" = 0 ] && exit 0
[ "${CLAUDE_CODE_REMOTE:-}" = true ] && exit 0

field() { printf '%s' "$INPUT" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p"; }

if [ "$ACTION" = tool ]; then
  if [ "$(field tool_name)" = AskUserQuestion ]; then ACTION=start; else ACTION=stop; fi
fi

SESSION="$(field session_id)"
SESSION="${SESSION//[^A-Za-z0-9_-]/}"
PIDFILE="${TMPDIR:-/tmp}/beto-alarm-${SESSION:-default}.pid"

silence() {
  local pid
  pid="$(cat "$PIDFILE" 2>/dev/null)"
  case "$pid" in '' | *[!0-9]*) ;; *) kill "$pid" 2>/dev/null ;; esac
  rm -f "$PIDFILE"
}

num() { case "$1" in '' | *[!0-9]*) printf '%s' "$2" ;; *) printf '%s' "$1" ;; esac; }

play() {
  local sound="${BETO_ALARM_SOUND:-}"
  if [ -n "${BETO_ALARM_PLAYER:-}" ]; then
    "$BETO_ALARM_PLAYER" "$sound"
  elif command -v afplay >/dev/null 2>&1; then
    afplay -v 0.6 "${sound:-/System/Library/Sounds/Glass.aiff}"
  elif command -v paplay >/dev/null 2>&1; then
    paplay "${sound:-/usr/share/sounds/freedesktop/stereo/message.oga}"
  elif command -v canberra-gtk-play >/dev/null 2>&1; then
    canberra-gtk-play -i message
  else
    printf '\a' >/dev/tty
  fi
} 2>/dev/null

ring() {
  local grace first max give_up gap elapsed
  grace="$(num "${BETO_ALARM_GRACE:-}" 20)"
  first="$(num "${BETO_ALARM_FIRST:-}" 30)"
  max="$(num "${BETO_ALARM_MAX:-}" 300)"
  give_up="$(num "${BETO_ALARM_GIVE_UP:-}" 1800)"
  [ "$first" -gt 0 ] || first=1
  sleep "$grace"
  elapsed="$grace"
  gap="$first"
  while [ "$elapsed" -lt "$give_up" ]; do
    play
    sleep "$gap"
    elapsed=$((elapsed + gap))
    gap=$((gap * 2))
    [ "$gap" -gt "$max" ] && gap="$max"
  done
  rm -f "$PIDFILE"
}

case "$ACTION" in
  start)
    silence
    # Detach so the hook returns at once and the loop outlives it.
    ring </dev/null >/dev/null 2>&1 &
    printf '%s\n' "$!" >"$PIDFILE"
    ;;
  stop) silence ;;
esac
exit 0
