# Skill mechanics

Read this branch of [writing-for-agents](SKILL.md) for skill frontmatter,
invocation choices, splitting, and routers.

## Invocation

Keep required `name` and `description` frontmatter. Front-load trigger words in the
description: discovery surfaces may shorten it. In Codex, configure implicit
matching through `policy.allow_implicit_invocation` in `agents/openai.yaml`:

- **Model-invoked:** allow implicit invocation when the agent should select the skill
  independently. Its description carries distinct trigger branches; explicit user
  invocation remains available.
- **User-invoked:** set `allow_implicit_invocation: false` when use requires explicit
  selection. Keep a concise human-facing summary. Explicit `$skill` still works;
  this policy disables implicit matching, not description requirements or file reading.

Directly following a reference to a skill file is different from invoking that skill.
A false implicit-invocation policy does not make its files unreadable to other skills.
Treat loaded descriptions as context cost; do not promise zero load from this policy.
Check another provider's mechanisms before applying Codex-specific configuration.

See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Splitting by invocation

Split a model-invoked skill when a distinct leading word needs independent retrieval,
or independent selection by another workflow warrants it. The always-available
pointer costs attention; justify that reach. For sequence boundaries, use
[writing-for-agents](SKILL.md).

Shared reference can remain a plain file readable by any workflow; it need not become
another skill merely because several explicit workflows use it.

## Router skills

When explicit skills exceed what the user can remember, a router can list names and
selection conditions. Distinguish suggesting explicit invocation from reading referenced
files or invoking another skill; do not treat the router as bypassing implicit policy.
