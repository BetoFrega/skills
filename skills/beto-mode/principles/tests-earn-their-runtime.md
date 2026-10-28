# Tests Earn Their Runtime

Every test runs on every future change, so each one adds runtime for as long as it
exists. Add or keep a test only when it catches a failure that no cheaper test
already catches.

- **Name the unique failure.** Before adding a test, name the behavior, boundary, or
  past bug it alone would catch. If an existing test already fails on that breakage,
  extend that test or add nothing.
- **One case per class.** Cover one input per equivalence class or boundary, not one
  per value. Parametrize only over inputs that take different branches or cross
  different boundaries.
- **Cheapest level that catches it.** Prefer a pure function over a module, a module
  over an integration, an integration over an end-to-end test. Go slower only for a
  failure that exists only at that level, such as wiring, real I/O, or a browser, and
  then write one test per such seam.
- **No idle time.** No real sleeps, polling, wall clock, or external network. Fake time
  and stub third parties at the boundary. Share read-only expensive fixtures across a
  file or suite.
- **Delete what a change made redundant**, in the same change. Removing a test whose
  failure another test catches is an improvement.
- Coverage targets, symmetry with other files, and "just in case" do not justify a
  test.

When reporting work that adds tests, list each one with the failure it catches. A
test without an answer gets deleted before delivery.
