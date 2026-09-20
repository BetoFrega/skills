# Information-density rule

Build the inline `### Information density` rule from the base, one reporter branch, and
the investigator clause only when that skill is confirmed available. Match the
repository's language when helpful, but preserve the literal flag format and
operational boundaries.

## Base

```markdown
### Information density
While reading or producing logs, documentation, instructions, and responses, flag
content that is substantially reducible without losing facts, constraints, decisions,
or relevant evidence. Indicators include repetition without new information, routine
logs without diagnostic value, unselected dumps, and duplicated or rephrased
instructions. Use
`‼️ LOW INFORMATION DENSITY ‼️ — <location>: <concrete evidence>; <proposed reduction>.`
Emit one flag per distinct cause and group similar occurrences. Preserve details needed
for comprehension, failure reproduction, and audit; size alone is not a defect.
Correct content produced or edited within the active scope before finishing.
```

## Reporter clause

Include only when `$report-low-density` is available:

```markdown
For a flag in pre-existing or out-of-scope content, delegate `$report-low-density` to a
subagent with the exact flag, source, minimal reproduction command or steps, and the
relevant revision and environment. This rule authorizes only the reporter's minimal
issue creation. If no subagent is available or publication cannot be confirmed,
preserve the flag and reproduction pointers, distinguish confirmed absence from an
unresolved write, state the remediation path, and stop.
```

## Investigator clause

Include only when `$investigate-low-density` is available:

```markdown
For focused investigation, use `$investigate-low-density`. When the active task
explicitly assigns a low-density tracker issue, this rule authorizes one append-only
findings comment on that issue, not remediation or state changes.
```

## Reporter-unavailable fallback

Include instead of the reporter clause when `$report-low-density` is unavailable:

```markdown
For a flag in pre-existing or out-of-scope content, preserve the flag and reproduction
pointers, state that automated reporting is unavailable, give the remediation path,
and stop.
```
