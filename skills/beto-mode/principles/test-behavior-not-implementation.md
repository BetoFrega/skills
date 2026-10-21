# Test Behavior, Not Implementation

A test calls the code as its users do and asserts the exact result they see. Rewrite
or delete any test that would still pass if every imported function returned
`undefined` or a wrong value.

These shapes fail that check:

- Loose or missing assertions: "is defined", "is truthy", "does not throw",
  "greater than zero".
- Call-or-absence-only assertions: "was called", "was not called", "is empty".
- An expected value computed by the code under test.
- A restated constant, configuration default, table row, or prompt string.
- Assertions on data the test built, with no call to the subject.

**Fix:** call the subject with one concrete input and assert the literal output or
effect. For a mock, assert the payload it received. For an absence, also assert the
presence on another input. For a constant, test the mechanism that reads it.

Relation checks across tables (a key present in two tables, a parent that exists) and
type-level checks remain valid.
