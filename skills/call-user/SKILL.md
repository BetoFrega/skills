---
name: call-user
description: Ring a soft, repeating alarm on the user's computer when you need them back, such as a question, approval, or blocker, and stop it when they answer.
---

# Call User

Use this when you need the user and they may not be watching: you are blocked on a
question, a decision, an approval, or a credential, or you finished work they asked to
be called for. Skip it for routine replies that can wait.

The alarm only helps when you run on the user's own computer. In a cloud or remote
session the script refuses, because the sound would play where nobody hears it; use
the platform's notification instead.

1. Write the question or status the user needs to read.
2. Start the alarm with `scripts/alarm.sh start`, from this skill's directory. It
   returns at once and rings in the background.
3. End your turn or wait for the answer.
4. As soon as the user answers, run `scripts/alarm.sh stop` before anything else.
   Also stop it if you resume work without needing them.

The alarm waits 20 seconds before the first ring, so it stays quiet when the user is
already looking. Then it rings a short system sound with a gap that doubles from
30 seconds to 5 minutes, and stops by itself after 30 minutes. A new start replaces
the alarm running from the same directory.

The user can tune it with environment variables: `CALL_USER_GRACE`,
`CALL_USER_FIRST`, `CALL_USER_MAX`, and `CALL_USER_GIVE_UP` in seconds, and
`CALL_USER_SOUND` for a sound file.
