# Writing Agent Briefs

An agent brief is the authoritative execution contract posted as a GitHub issue or PR comment when it moves to `ready-for-agent`. The original body and discussion provide context.

For an issue, specify the requested change. For a PR, describe the current diff and only the remaining work: completion, gaps, and review corrections.

Describe behavior and contracts; leave implementation decisions to the agent. Identify work through stable types, signatures, interfaces, and configuration shapes rather than implementation paths or line numbers. The brief must remain useful after refactoring.

Use every field below. Include edge cases and errors, independently verifiable acceptance criteria, and explicit scope boundaries.

## Template

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** One-line requested outcome.

**Current behavior:**
Present behavior, or current diff state for a PR.

**Desired behavior:**
Required outcome, including edge cases and errors.

**Key interfaces:**
- Stable symbol or contract: required change and rationale.

**Acceptance criteria:**
- [ ] Observable condition proving a requirement is satisfied.
- [ ] Add criteria until every requirement is covered.

**Out of scope:**
- Excluded changes and adjacent features.
```
