# ADR Format

The project format takes precedence. With no established format, use the template
below. Keep the record as short as its reasoning allows: simple decisions can use
short paragraphs; complex trade-offs can justify more detail.

## Required content

| Content | What the reader must learn |
| --- | --- |
| Title | The specific decision, rather than a broad topic such as "Database." |
| Status and date | Whether the decision is proposed, accepted, deprecated, or superseded; when it was proposed and, when known, accepted or retired. |
| Context | The problem, affected scope, constraints, and relevant facts or assumptions at the time. |
| Decision | The concrete choice and where it applies. |
| Rationale | Why the choice fits the context, including meaningful alternatives and the reasons for rejecting them when known. |
| Consequences | Expected benefits, costs, limitations, and commitments. Identify observed outcomes separately from expectations. |

`proposed` means acceptance has not been established. Use `accepted` only with
approval evidence under the project's convention. Use `deprecated` for a retired
decision without a replacement, and `superseded` with a link to an accepted
replacement. These statuses describe the decision, not implementation progress.

Write reasoning from the information available at the time. Add later discoveries
as dated notes when useful, preserving the original rationale. Keep detailed
execution plans in linked specs or tickets and domain definitions in the glossary.

## Default template

```md
# NNNN: Short title stating the decision

Status: proposed
Date: YYYY-MM-DD

## Context

Describe the problem, scope, constraints, and relevant facts or assumptions.

## Decision

State the choice and where it applies.

## Rationale

Explain why this choice fits the context. Include meaningful alternatives and
their rejection reasons when they were actually considered.

## Consequences

Describe expected benefits, costs, limitations, and commitments.
```

Add references to approval evidence, research, related ADRs, specs, tickets, or PRs
when they support the record. Add open questions or conditions for reconsideration
only when they affect the decision. Use repository-relative links for local files.

The default builds on [Michael Nygard's ADR format](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions),
with an explicit rationale and date.
