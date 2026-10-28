# Pin Behavior Before Changing

Before changing existing code, make sure a test fails if its current behavior changes.
A refactor that silently changes behavior is a regression nobody asked for.

- **Pin first.** Find the tests that cover the behavior the change touches. Where
  none would fail, add characterization tests at the nearest stable seam that assert
  today's actual output, quirks included, and run them green on the old code before
  the first edit. Pin only what the change touches; this is not a coverage campaign.
- **Learn why before removing.** For each behavior you plan to drop or alter, find
  why it exists: blame, the commit or PR that added it, a linked ticket, its callers.
  Remove it for a found reason or an approved behavior change. A behavior with no
  findable reason that callers may rely on is a question for the user, not a deletion.
- **Pinned is not intended.** A pin records what the code does, not what it should
  do. When a pinned behavior looks wrong, report it and change it as its own
  deliberate step, updating that pin in the same step, never as a side effect.
- **Prune pins after.** Keep pins that protect intended behavior; delete pins that
  only froze the old implementation, per Tests Earn Their Runtime.

**Check:** every pin that changed between the old and new code is named in the
report with the behavior change that justified it.
