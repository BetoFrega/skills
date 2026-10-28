# Encode Lessons in Structure

When you catch yourself writing the same instruction a second time, or the user
corrects a mistake that has happened before, make the mistake impossible to repeat
instead of adding more text.

Fix it at the highest level that works:

1. **Architecture.** One owner per piece of state, one supported way per task, hidden
   internals, one source of truth instead of hand-synced lists. Delete old paths and
   dead code an agent would copy.
2. **Types.** Make the bad state impossible to write.
3. **Lint or CI check** whose error names the file, type, or function to use instead.
   When the pattern is already common, fail only when a change adds more.
4. **Test** of the behavior the mistake breaks.
5. **Text,** only for judgment calls nothing can check: make the instruction more
   prominent in its one authoritative place and add an example of the failure.

- Prove a new check fails on the real past mistake and passes on the fix.
- When an instruction elsewhere causes the mistake, correct that source instead of
  adding a counter-instruction.
- Keep a table in the repository's agent instruction file pairing each rule with what
  enforces it. A repeat of a rule nothing enforces moves it up a level.

**Where the source lives.** Edit files of the repository you are working in, including
its own skills, `AGENTS.md`, and `CLAUDE.md`. Skills from an installed plugin are
read-only, even when a local copy is writable: a lesson about one becomes an issue on
the plugin's repository through `report-skill-lesson`. Working in a checkout of that
plugin's repository itself, edit through its normal delivery flow.
