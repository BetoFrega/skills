# Product workflow validation

Validated on 2026-10-06 against the [agreed model](../design/product-documentation-model.md)
and the consolidate, plan-increment, review-learnings, and contextual grilling entries.

## Independent behavioral exercise

An independent agent with no conversation history exercised three isolated fictional
projects. Each contained a README-only Git repository, external configuration, local
canonical Markdown records, and a local tracker. The agent could change only temporary
scenario files. No live product, provider, release, flag operation, or publication was
involved. User decisions were not invented; pending questions ended their scenario.

| Request | Observed outcome |
| --- | --- |
| Interview the first meal-reservation increment | Read canonical and domain context, retained confirmed rules, demonstrated a consistent slice, and proposed closure. Deferred ideas did not extend the interview; technical and exposure gaps stayed explicit. |
| Plan only that increment and prepare draft tickets | Saved one increment plan and three contributing work drafts with shared aggregate acceptance. Missing application inputs left every item blocked. No future increment or tracker publication was introduced. |
| Review a completed household trial | Recorded 7/10 collections within the deadline against a 90% hypothesis, with trial scope and missing evidence. Retained the approved 30-minute rule, proposed a follow-up experiment, and asked for the unresolved choice. Deployment, trial authority, observed outcomes, and unreadable flag state remained separate. |

The agent created seven files and updated five canonical files in the temporary
workspace, and checked 78 local references. The author read the responses and saved
records, including the plan, tickets, acceptance coverage, dependencies, and evidence.
These exercises support the observed workflow behavior; they do not establish live
provider integration, operational maintenance, or outcomes for every product scenario.

## Structural and discovery checks

- Five changed entrypoints passed skill-creator frontmatter validation.
- The package builder validated all 50 skills, relative resources, and 185 archive files.
- All 20 existing release-preparation tests passed; Git whitespace checks passed.
- Every repository skill had a readable relative user symlink. Retired names were
  removed from discovery with their previous links preserved in installer backup.
- A fresh local Codex app-server `skills/list` lookup from an unrelated temporary
  project returned consolidate, plan-increment, and review-learnings enabled at
  user scope, without discovery errors.

Git delivery requires subsequent remote CI verification, synchronization of the
primary checkout on main, and user-link verification against that checkout. Package
validation does not publish the private cloud plugin; its publication remains separate.
