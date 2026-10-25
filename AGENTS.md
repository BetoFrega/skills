## Git workflow

- Keep the primary checkout on `main` at all times. Work directly on its `main`
  branch or in a separate Git worktree; use other branches only in worktrees.
  Locate the primary checkout through `git worktree list --porcelain` (the first
  entry), including when working from another worktree.
- After every push or merge that updates remote `main`, fetch `origin` and
  synchronize `main` in the primary checkout with `git merge --ff-only origin/main`.
  Completion requires the primary checkout to remain on `main` and its `HEAD` to
  match the freshly fetched `origin/main`.
- Preserve uncommitted work and local commits. If they block synchronization,
  report the blocker and resolve it before declaring delivery complete; never
  force-reset the primary checkout to synchronize it.

## Language

Write all skill content in English, including frontmatter descriptions, headings, instructions, and examples. Apply this rule when creating or editing skills in this repository. Respond to the user in their preferred language.

## Global rule changes

For global additions, revisions, or removals, use [grilling](skills/grilling/SKILL.md),
reuse settled answers, and obtain approval. Update local global instructions and
[setup](skills/setup-beto-frega-skills/SKILL.md)'s maintained policy, installation,
and verification guidance. Setup must reproduce approved behavior on other computers,
including removals. Read back both destinations and verify configured agents' loading.
Report blocked destinations and Git delivery separately; local-only changes are incomplete.

## Skill installation

Install repository skills only through the `beto-frega-skills` plugin in each agent;
do not create local copies or symlinks of repository skills. When delivering a skill
change, bump `version` in `.claude-plugin/plugin.json`,
`.claude-plugin/marketplace.json`, and `.codex-plugin/plugin.json` together. A change
under `personal/` bumps `personal/.claude-plugin/plugin.json` and its
`marketplace.json` entry together instead. After
synchronizing delivered changes into the primary checkout, update the plugin in each
configured agent and verify that a fresh session loads the changed skill.

## Portable paths

Use repository-relative paths in maintained instructions and examples. Scripts must
discover the repository root from their own location or Git metadata rather than
hardcode a user's home, checkout name, or absolute checkout path. Resolve standard
user installation directories through the environment or `Path.home()`. Create
cross-directory symlinks with relative targets calculated from their actual locations.
