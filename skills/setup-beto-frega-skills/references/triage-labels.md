# Triage-label defaults

| Canonical role | Default label | Meaning |
| --- | --- | --- |
| needs triage | `needs-triage` | Maintainer evaluation required |
| needs information | `needs-info` | Waiting for reporter input |
| ready for agent | `ready-for-agent` | Fully specified for autonomous execution |
| ready for human | `ready-for-human` | Human implementation or judgment required |
| will not fix | `wontfix` | Intentionally not planned |

The generated `docs/agents/triage-labels.md` maps each canonical role to the label
actually used by the repository. Preserve existing tracker vocabulary rather than
creating synonyms.
