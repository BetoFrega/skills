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
relevant revision and environment. Delegation authorizes preparation and duplicate
detection, not a tracker mutation. If the active task does not contain the user's
explicit request or approval to publish the exact report, the reporter returns the
complete proposed issue and the parent asks before delegating publication. If no
subagent is available or publication cannot be confirmed, preserve the flag and
reproduction pointers, distinguish approval required or confirmed absence from an
unresolved write, state the remediation path, and stop.
```

## Investigator clause

Include only when `$investigate-low-density` is available:

```markdown
For focused investigation, use `$investigate-low-density`. When the user explicitly
requests investigation of an assigned low-density tracker issue, one append-only
findings comment is within that task's scope; remediation and state changes are not.
```

## Reporter-unavailable fallback

Include instead of the reporter clause when `$report-low-density` is unavailable:

```markdown
For a flag in pre-existing or out-of-scope content, preserve the flag and reproduction
pointers, state that automated reporting is unavailable, give the remediation path,
and stop.
```
