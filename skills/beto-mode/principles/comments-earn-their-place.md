# Comments Earn Their Place

A comment is the last home for a fact. Put each fact where it is checked or where
its reader looks for it, and write a comment only for what has no better home.

**Make the code say it first.** When a comment would explain our own code, rename,
extract, or type until the comment is unneeded.

**Route each fact to its home:**

- What the code does: a name, an extracted function, or a type.
- An invariant on our own code: a type, an assertion, or a test, per
  [Encode Lessons in Structure](encode-lessons-in-structure.md).
- What changed, what was tried, who asked, how it was verified: the commit or PR.
- Work still to do: a ticket. A `TODO` stays only with the ticket's link.
- An architectural choice: an ADR, linked from the code when the reader needs it.
- What a domain term means: the `CONTEXT.md` glossary.
- Old code: delete it. Git keeps it.

**Keep a comment when it is one of these:**

- A license header or a tool directive.
- An interface comment on an API used outside its module, stating what the signature
  cannot: units, ownership, side effects, errors.
- A constraint set outside our code (dependency bug, platform, vendor, protocol,
  regulation), naming its source. A workaround also states when it can go.
- A non-obvious why that the code cannot show yet, in one or two lines.
- A lint or type suppression, with what the rule gets wrong at that line.

**Form.** Every comment is true against today's code, carries no task history, and
links the record when the fact lives elsewhere.

**Scope.** Apply this to comments the change adds, edits, or deletes. Follow the
repository's own comment convention where it has one. Leave other comments as they
are, and mention a false one in the report.

**When unsure.** Drop narration you wrote in this change. Keep or move a comment that
carries rationale; delete a claim only after verifying it is false. Propose a code
reshape or an encoding instead of making it outside the task's scope.

**Workarounds.** If a workaround needs a long comment to justify it, fix the code
instead.
