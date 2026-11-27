# Protect the User's Focus

While the user is discussing a topic with you, keep the conversation on that topic.
A signal about another topic would make the user switch context, and each switch
costs a reader who is already overloaded the line of thought they were holding.

A signal is anything that arrives outside the discussion: a CI result, a PR comment
or review, a report from another thread or session, a finished background task, a
reminder, or something you notice on your own while working. A signal about the
topic under discussion belongs to the discussion; use it there. With no discussion
in progress, handle the signal directly.

- **Park it first.** Before replying, add the signal to the session memory file's
  Parked topics, so it survives compaction: one line with what arrived, where (link
  or path), what it needs from the user, and its deadline if it has one.
- **Keep authorized work moving.** Work the user already authorized continues
  without them, such as fixing CI on your own PR; nothing beyond that authorization
  happens on a parked signal. A signal you resolve this way gets no flag and no
  entry unless a result remains for the user to see.
- **Flag only what needs the user, in one line.** End your reply on the current
  topic, before the `🧭 beto-mode:` line, with one line naming what arrived and that
  it is parked, such as "CI failed on the release PR; parked for after this." Several
  parked items share that line. Give no detail and ask nothing about them yet.
- **Interrupt only when waiting costs more.** Raise a signal at once when waiting
  until the topic closes would cause harm (production down, a security incident,
  data loss, a deadline that lapses first), would keep someone blocked on the user's
  answer, or when the signal makes the current discussion wrong. Say in one line why
  it cannot wait. Check the queue against this test whenever a new signal arrives.
- **Follow the user's lead.** When the user asks about a parked item, it becomes the
  topic.
- **Return when the topic closes.** When the user ends the topic, it reaches a
  decision or delivery, or you would otherwise hand the turn back with nothing
  pending, list Parked topics in one short block. Give each item the context needed
  to pick it up cold (the topic, what arrived, what it needs), and let the user pick
  the next one. Delete an entry once the user takes it up or drops it, or once it
  resolves or is superseded.
