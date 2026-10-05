# Project configuration locations

Read this when setup chooses configuration locations or a consuming skill resolves
tracker, label, domain, product, observability, or accessibility instructions.
Consumers use the resolution rules below; setup also uses the placement and discovery
sections.

## Resolve configuration

Global personal communication is configured separately through
[global communication](global-communication.md). Its language and emoji policy applies
across projects; global instruction entries require no repository identity binding.
Keep project-specific rules and pointers scoped using the binding rules below.

Read the project's applicable repository instructions. Follow configuration pointers
provided by the user, personal agent instructions, or those repository instructions,
including pointers to files outside the checkout. A supplied configuration entry may
route to several documents; read only the documents required by the current task.

Verify that external configuration applies to the current project. Bind it to a
normalized repository identity such as host/owner/repository, or an explicitly scoped
local project when there is no remote. Record whether it applies across the project's
checkouts or only to named contexts. Folder names alone do not establish that binding.
For delegated work, pass the entry reference and necessary scoped configuration to
the receiving agent.

Resolve relative file references from the containing document, unless that document
explicitly declares another base. Use repository defaults for sections with no
configured replacement. A missing or unreadable declared replacement is an access or
configuration gap; surface it rather than silently reverting to a default. Preserve
repository instructions and follow the normal instruction hierarchy when sources
conflict; identify any unresolved conflict that affects the requested operation.

## Choose locations during setup

Retain declared locations. For missing sections, ask whether configuration belongs
in the repository, outside it, or in a mixture of locations. External configuration
is useful when contributing to a repository whose tracked files should stay untouched.
Confirm the external directory and how agents will receive its entry reference.

| Section | Repository default | External directory default |
| --- | --- | --- |
| Entry and information-density rule | Chosen `AGENTS.md` or `CLAUDE.md` | `agent-skills.md` |
| Issue-tracker workflow | `docs/agents/issue-tracker.md` | `issue-tracker.md` |
| Tracker-label vocabulary | `docs/agents/triage-labels.md` | `triage-labels.md` |
| Domain-document layout | `docs/agents/domain.md` | `domain.md` |
| Product-documentation conventions | `docs/agents/product.md` | `product.md` |
| Observability baseline | `OBSERVABILITY.md` | `OBSERVABILITY.md` |
| Accessibility baseline | `ACCESSIBILITY.md` | `ACCESSIBILITY.md` |

These are placement defaults, not required names. An external `agent-skills.md`
contains the project binding, applicable information-density rule, and scoped
pointers to the selected documents. A mixed configuration points to the existing
authority for each section and fills only gaps. Keep configuration location separate
from the location of the records it describes: an external tracker configuration can
point to GitHub, and an external product configuration can point to a shared catalogue.
Personal workflow guidance remains scoped to the user's work; identify project policy
and its authority explicitly when documenting a shared baseline.

Use relative references between files where possible. Resolve standard personal
directories through the environment or the user's home directory; infer no particular
home, checkout path, or agent application's global configuration convention.

## Make external configuration discoverable

Agree on an actual entry source: an explicit reference in the task, an existing
personal instruction source loaded by the agent, or an approved repository pointer.
When all configuration is external, put the skill pointers and information-density
rule in that external entry. Repository instruction edits and repository symlinks are
optional changes requiring their own inclusion in the confirmed draft.

Read back the entry and resolve its project binding and every selected document.
Verify a persistent discovery pointer when setup writes one. If discovery is limited
to the current task, state that later tasks need the entry reference supplied again.
Creating files alone does not establish automatic loading by an agent application.
