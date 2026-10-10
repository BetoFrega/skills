---
name: setup-beto-frega-skills
description: Configure global rules and project skill conventions, inside or outside the repository. Run explicitly before first use or for configuration gaps.
---

# Setup Beto Frega skills

Fill configuration gaps only; revisit settled choices only on request. This invocation authorizes configuration, not product records or unrelated work. Resolve decisions through [grilling](../grilling/SKILL.md).

## 1. Discover

Inspect existing instructions/configuration, installed skills and actual agent loading, architecture, product records, and live tracker vocabulary. Report gaps/conflicts. Use [configuration locations](references/project-configuration.md) to settle each section's location, project binding, and discovery before drafting. Keep global communication separate from project configuration.

## 2. Configure applicable gaps

| Branch | Required guidance and decisions |
| --- | --- |
| Global rules | [Global policy](references/global-communication.md): reuse approved choices; reconcile maintained global rules across configured agents. |
| Issue tracker | Confirm the remote-indicated tracker or user choice; adapt [GitHub](references/issue-tracker-github.md), [GitLab](references/issue-tracker-gitlab.md), or [Markdown](references/issue-tracker-local.md) to verified operations. |
| Tracker labels, when triage or low-density skills are installed | Confirm [label mappings](references/triage-labels.md); inspect live labels and propose missing ones. |
| Domain layout | Use [domain rules](references/domain.md); recommend one context, multiple only for demonstrated boundaries. Create domain records lazily. |
| Missing equivalent information-density rule | Apply [density rules](references/information-density.md), including only available skill branches. |
| Missing observability baseline | Grill with [observability defaults](references/observability-default.md), grounded in inspected architecture/tooling. |
| Missing accessibility baseline | Grill separately with [accessibility defaults](references/accessibility-default.md), grounded in inspected surfaces/platforms. |
| Missing/incomplete product conventions | Apply [product setup](references/product-documentation.md) for destinations, representation, and maintenance. |

For installed low-density reporting, require fingerprint search, labeled creation, and readback; for investigation, issue/discussion reading, commenting, and readback. Missing operations are configuration gaps.

Complete each baseline's applicable interview branches before drafting; defaults are recommendations.

## 3. Confirm drafts

Show complete proposed file contents, label mutations, and symlink/pointer changes. Resolve the canonical repository entry with the user when both or neither of `AGENTS.md`/`CLAUDE.md` exist; otherwise reuse the existing entry. Update applicable `## Agent skills` pointers and density rules without duplicating policies. Include external project binding and only selected repository edits.

Obtain approval before writing, including edits to existing configuration.

## 4. Write and verify

Apply approved changes only. Reconcile the communication policy in existing globals,
including replacement of superseded concision guidance and minimum context when
switching tasks; preserve unrelated rules.
Read back labels; verify references, discovery, project accuracy, relative global symlinks, policy loading through every configured agent, and idempotence. For external-only setup, verify the repository stayed untouched.

Report changed files, consumers, and [delivery state](../consolidate/references/local-document-delivery.md). Rerun setup only for gaps or intentional revisions.
