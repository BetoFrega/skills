# Weigh Rival Explanations

Before naming a cause, test it against its rivals. Evidence counts by how many rivals
it rules out. The method is process tracing (Van Evera; Bennett and Checkel). Under
Fix Root Causes, apply it at every "why" that has more than one answer.

- List at least two rival explanations before gathering evidence. Include "the change
  did nothing" and "something else changed at the same time".
- For each, deduce what must appear if it is true and what would appear only if it is
  true. Classify each observation by those two questions, using Van Evera's tests:
  - **Hoop:** must appear, but rivals predict it too. Missing eliminates the
    explanation; present only keeps it alive.
  - **Smoking gun:** appears only if it is true, but may be missing. Present confirms
    it; missing proves little.
  - **Doubly decisive:** must appear and appears only if it is true. Settles it either
    way.
  - **Straw in the wind:** neither. Shifts confidence a little; several independent
    ones together can add up.
- Evidence every rival predicts supports none of them. "It started after the deploy"
  fits anything else that changed that day, and a passing test is usually a hoop.
- Be as hard on the favourite as on the rivals: run first the check that could
  eliminate it.
- Weigh the source. A commit message, postmortem, log line, or agent report records
  what its author knew or chose to show.
- When a finding contradicts the explanation, revise it only with a new observation
  the revision predicts, and run that check. Patching the story to fit each anomaly
  hides the real cause.
- Treat a surprise as a lead: add the explanation it suggests to the rivals.
- Stop gathering when new evidence repeats what you have and no longer separates the
  survivors.

**Check:** the report names the rivals and the observation that eliminated or
confirmed each, and labels the cause per Evidence Before Claims. When no observation
separates the survivors, report them as open, with the check that would decide.
