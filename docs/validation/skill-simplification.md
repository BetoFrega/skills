# Skill simplification validation

## Approved scope

The reviewed simplification updates 38 files and removes four files belonging to
`esds-compress-compressed` and `last-responsible-moment-compressed`. Their contracts
remain in [ESDS compression](../../skills/esds-compress/SKILL.md) and
[Last Responsible Moment](../../skills/last-responsible-moment/SKILL.md).
The explicit [grill-me alias](../../skills/grill-me/SKILL.md) remains. At delivery,
the repository contained 49 skills, down from 51. Removed command names have no
automatic redirect.

Compare against base commit
[bba0906](https://github.com/BetoFrega/skills/commit/bba09067bac3694bd71a731dffd70617eabf0acd).
Each replacement matched its independently reviewed SHA-256; every other retained
skill file matched the original baseline. The reviewed replacement patch digest was
`932bec4437146f4f7c1d3a7e72df4b9dc6d961712bcbcf7f21f7362ab14d942d`;
the approved deletion patch digest was
`cf0746cc1621459c86b5d4cdfb13eb039397b11faa957aeac9ca952444d4938d`.
Temporary source mirrors and audit drafts are local review artifacts, not maintained
or installed copies of skills.

## Reduction

Whitespace-delimited words include Markdown syntax and frontmatter. Whole-corpus
counts include references and examples; they exclude HTML, YAML, code, and licenses.
These are word counts, not measured model-token or billing savings.

| Measure | Before | After | Reduction |
| --- | ---: | ---: | ---: |
| Skill entrypoints | 19,981 | 14,642 | 26.7% |
| Entire Markdown corpus | 43,318 | 36,030 | 16.8% |

No instruction bulk was moved into new references. Independent workflows keep their
invocation and authority boundaries; equivalent compressed variants are retired.

## Review evidence

Three authors examined 17 skills each using `gpt-6.1-sol`, high effort. Three
cross-reviews compared originals, replacements, relevant sources, and affected
references. Every repair was rechecked by a reviewer independent of its author.
All 38 replacement hashes were covered; no actionable finding remained open.
A separate `claude-sonnet-5` consultation, medium effort, checked the optional
retirements against the final surviving contracts and invocation configuration.

Rechecks preserved the unconditional term-definition rule, 50–95% fidelity-limited
pruning aspiration, reconciliation before implementation commits, explicit spec
comparison and optional rather than mandatory historical issue closure.
Invocation-policy and retirement losses were made explicit.

## Compatibility and verification

- [Skill mechanics](../../skills/writing-for-agents/SKILL-MECHANICS.md) distinguishes
  implicit matching, explicit invocation, and linked-file reading. Its correction
  follows [official skill documentation](https://learn.chatgpt.com/docs/build-skills);
  disabling implicit invocation establishes neither zero context load nor unreadability.
- [Code review](../../skills/code-review/SKILL.md) uses a direct empty-tree comparison
  for a root commit. An isolated fixture reproduced the old three-dot diff's exit 128;
  the direct diff and root log returned 0 and included the root change. Ordinary
  commit comparisons retain their merge-base behavior.
- Markdown references and affected incoming anchors resolved. The translated
  [PR explanation template](../../skills/explain-pr/assets/pr-explanation.html) retained
  its stylesheet, renderer/security settings, print handling, and valid internal
  navigation/ARIA IDs. Browser/PDF rendering was not executed or claimed verified.
- All 49 installed skills were readable through relative links. Two retired global
  links were removed only after verifying their targets belonged to this repository.
  Installation must follow [the link workflow](../local-skill-links.md), pointing to
  the synchronized primary checkout after delivery.
- At delivery, package validation and archive readback covered all 49 surviving skills
  and excluded the retired files. The packaging workflow has since been retired.

The existing TDD trigger/UI versus refactoring-stage discrepancy retains its current
policy and metadata.
