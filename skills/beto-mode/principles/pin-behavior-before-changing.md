# Pin Behavior Before Changing

Before changing existing code, make sure some test fails if its current behavior
changes. Without that test, a refactor can change behavior and no check will report it.

- **Pin first.** Find the tests that cover the behavior the change touches. Where
  no test would fail, add characterization tests at the nearest stable seam. Assert
  the code's current output, including odd cases, and run them green on the old code
  before the first edit. Pin only the behavior the change touches.
- **Learn why before removing.** For each behavior you plan to drop or alter, find
  why it exists: blame, the commit or PR that added it, a linked ticket, its callers.
  Remove it only for a reason you found or for an approved behavior change. When you
  find no reason and callers may rely on it, ask the user before removing it.
- **Report suspect pins.** A pin records what the code does today. When a pinned
  behavior looks wrong, report it. Change it in a separate step and update its pin
  in that step.
- **Prune pins after.** Keep pins that protect intended behavior. Delete pins that
  only froze the old implementation, per Tests Earn Their Runtime.

**Check:** the report names every pin that changed between the old and new code,
with the behavior change that justified it.
