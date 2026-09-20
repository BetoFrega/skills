# Tracker-label defaults

| Kind | Canonical purpose | Default label | Meaning |
| --- | --- | --- | --- |
| workflow | needs triage | `needs-triage` | Investigation or maintainer evaluation required |
| workflow | needs information | `needs-info` | Waiting for reporter input |
| workflow | ready for agent | `ready-for-agent` | Fully specified for autonomous execution |
| workflow | ready for human | `ready-for-human` | Human implementation or judgment required |
| workflow | will not fix | `wontfix` | Intentionally not planned |
| category | low information density | `low-info-density` | Content reported for low information density |

The generated `docs/agents/triage-labels.md` maps each applicable canonical purpose to
the label actually used by the repository. Include `low information density` and
`needs triage` when either low-density skill is installed. Preserve existing tracker
vocabulary rather than creating synonyms, and record whether each mapped value is a
workflow state or an additive category.
