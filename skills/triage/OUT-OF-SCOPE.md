# Out-of-Scope Knowledge Base

The repository's `.out-of-scope/` records durable rejected feature concepts for
institutional memory and deduplication.

## Directory structure

Use one short kebab-case file per concept, such as `.out-of-scope/dark-mode.md`.
Group equivalent issue and PR requests together rather than creating a file per item.

## File format

Write a readable short design document: concept decision, substantive durable reason,
and linked prior requests. Use paragraphs, examples, or code when they clarify the
reason; this is not a database entry.

```markdown
# <Concept>

<Decision and scope.>

## Why this is out of scope

<Reason grounded in project scope, technical constraints, or strategic decisions.>

## Prior requests

- [<Issue or PR identifier>](<verified URL>): <request summary>
```

### Naming the file

Choose a recognizable concept name, such as `dark-mode.md` or `plugin-system.md`.

### Writing the reason

Explain why the feature conflicts with project scope, technical constraints, or
strategy. Temporary workload is a deferral, not a durable rejection.

## When to check `.out-of-scope/`

During triage's initial context gathering, read every file and match by concept,
not keywords: “night theme” may match `dark-mode.md`. Present the prior decision and
reason to the maintainer, who can confirm, reconsider, or distinguish the request.
Confirmation appends the linked request and closes it; distinct requests continue
normal triage.

## When to write to `.out-of-scope/`

Only rejected enhancements marked `wontfix`, including enhancement PRs. Bugs and
already-implemented requests do not belong here; link the existing implementation
in the closing comment instead.

After the maintainer rejects an enhancement, append it to the matching concept's
prior requests or create its decision/reason/request record. Post the decision and
record link, then close the item with `wontfix`.

## Updating or removing out-of-scope files

When the maintainer reconsiders, update or delete the concept record and continue
normal triage for the triggering item. Historical issues need not be reopened.
