---
name: setup-beto-frega-skills
description: "Configure Beto Frega's global communication rules and project skill conventions, using files inside or outside the repository. Run explicitly before first use or to fill configuration gaps."
---

# Setup Beto Frega skills

Configure personal communication in the installed agents' global instruction files,
then the project documents consumed by the skills:

- global conversation language, concision, and semantic emoji markers;
- issue-tracker workflow;
- tracker-label vocabulary when triage or low-density reporting is installed;
- domain-document layout;
- information-density reporting rules in the chosen agent-instruction entry;
- the project's observability and accessibility baselines;
- product-documentation destinations, native formats, and maintenance conventions.

This is an incremental, prompt-driven setup. Preserve existing decisions. Explore,
interview, show complete drafts, obtain confirmation, then write. Invocation authorizes
only this configuration work.

For every unresolved setup decision, read and use
[grilling](../grilling/SKILL.md). It owns the interview protocol, including question
selection, grouping, recommendations, and shared-understanding confirmation. Scope
each design tree to the configuration gaps identified here; retain settled choices.

## 1. Explore without writing

Inspect facts the user should not have to supply:

- remotes and `.git/config` for tracker clues;
- root `AGENTS.md` and `CLAUDE.md`, including existing skill pointers;
- installed agents' global instruction sources, their actual loading conventions,
  existing communication rules, and symlink targets;
- external configuration references supplied by the user or personal instructions,
  and whether their project binding matches this repository;
- any existing rule for flagging low-information-density content;
- `docs/agents/`, `.scratch/`, `CONTEXT.md`, `CONTEXT-MAP.md`, and ADR directories;
- whether triage and low-density reporting skills are installed;
- configured tracker labels and their live existence when the tracker is external;
- monorepo signals and context boundaries;
- `OBSERVABILITY.md` and `ACCESSIBILITY.md`, plus any alternate paths explicitly
  declared by repository instructions;
- existing product records, documentation destinations, and maintenance conventions;
- runtime architecture, deployed services, telemetry libraries, user-facing surfaces,
  UI platforms, and relevant test tooling.

Report what exists, what is missing, and any contradictory pointers. Existing files
are authoritative; ask before changing them.

### Resolve locations and discovery

Before drafting missing documents, use
[project configuration locations](references/project-configuration.md) to settle
placement, project binding, and discovery. Support repository files, external files,
and mixed configurations. Confirm external placement when the user requests working
without changes to a third-party repository. Continue to honor its applicable
instructions.

Resolve each section's configuration path and any document destinations it describes.
The defaults below apply only where the user has not selected another location.
Complete when each applicable section has a location and agents have an agreed way
to receive the configuration entry.

## 2. Configure only the gaps

Take the applicable sections in order. Skip settled sections unless the user explicitly
asks to revisit them.

### Personal communication (global)

Use [global communication](references/global-communication.md) to install the settled
personal policy in every configured agent's global instruction entry. Keep this scope
separate from project configuration and project binding. Use one canonical global
`AGENTS.md`; expose Claude's global `CLAUDE.md` through a relative symlink to it.
Reuse the approved language, concision, and emoji choices rather than interviewing again. Inspect
and fill installation gaps; retain entries that already provide the same behavior.

### A. Issue tracker

If the resolved issue-tracker document is absent, recommend the tracker indicated by
the remote: GitHub, then GitLab, otherwise local Markdown. Also support a user-described
tracker. Use the matching reference as a starting point:

- [GitHub](references/issue-tracker-github.md)
- [GitLab](references/issue-tracker-gitlab.md)
- [Local Markdown](references/issue-tracker-local.md)

Confirm the choice before drafting. Adapt commands and conventions to the repository;
do not claim integrations that were not verified.

When `$report-low-density` is installed, the workflow must support searching open
issues by a deterministic fingerprint, creating an issue with labels, and reading back
the result. Treat any missing operation in an existing document as a configuration gap
and ask before filling it.

When `$investigate-low-density` is installed, the workflow must support reading an
issue with discussion, commenting, and reading back the comment. Treat missing
operations as configuration gaps too.

### B. Tracker labels

Run when a triage skill, `$report-low-density`, or `$investigate-low-density` is
installed. If the resolved tracker-label document is absent, recommend the applicable
canonical labels in [the template](references/triage-labels.md). Ask one question:
whether to keep them. Collect overrides only when the answer is no.

When either low-density skill is installed, require mappings for `low information
density` and `needs triage`. After the mapping is confirmed, inspect the external
tracker and include any missing-label creation in the proposed mutations. For a local
Markdown tracker, confirm its equivalent category and status representation.

### C. Domain docs

If the resolved domain-layout document is absent, recommend one `CONTEXT.md` and an
ADR directory at the configured documentation destination. Repository defaults are
root `CONTEXT.md` and `docs/adr/`; an external layout keeps those files outside the
checkout when selected. Offer multi-context layout only when exploration found real
monorepo boundaries. Use
[the domain consumer rules](references/domain.md) as the draft basis. Domain files
themselves remain lazy: do not create an empty `CONTEXT.md` or ADR directory.

### D. Information density

If the selected agent-instruction entry has no equivalent rule, add an inline rule that
follows [the information-density rule](references/information-density.md). Use the
reporter clause or its unavailable fallback, and include the investigator clause only
when that skill is confirmed available. Treat an existing rule with the same behavior
as settled even when its heading or wording differs. Preserve it rather than adding a
duplicate.

### E. Observability baseline

If the authoritative observability document is absent, use `grilling`
with [the observability defaults](references/observability-default.md). Treat defaults
as recommendations, not repository policy. Resolve every applicable branch before
drafting the resolved observability path.

Base recommendations on inspected architecture and tooling. The interview must settle
scope, critical behavior, signals, correlation, failure reporting, privacy, volume and
cardinality, alert ownership, operational response, verification, and exceptions.

### F. Accessibility baseline

If the authoritative accessibility document is absent, use `grilling` in a separate tree
using [the accessibility defaults](references/accessibility-default.md). Resolve every
applicable branch before drafting the resolved accessibility path.

Base recommendations on inspected product surfaces and platforms. The interview must
settle scope, conformance target, supported interaction and assistive technology,
semantics, visual and motion behavior, content and errors, verification, ownership,
and exceptions.

Keep the observability and accessibility trees separate. Complete each tree under
`grilling` before drafting its document; confirm the complete drafts in step 3 before
writing.

### G. Product documentation

If product-documentation conventions are absent or incomplete, use
[product-documentation setup](references/product-documentation.md) to resolve the
applicable destinations, native representations, product conventions, and maintenance.
Draft the resolved product configuration. This standard setup owns configuration;
consolidate consumes it to register and maintain records.

## 3. Confirm complete drafts

Show the complete proposed contents of every file that would change:

- the global communication block, any reconciliation with existing global content,
  and each global entry or relative symlink to be created or changed;
- the `## Agent skills` block for the chosen agent-instruction entry, including the
  information-density rule when missing;
- the resolved tracker, label, domain, and product configuration paths when applicable
  and missing or incomplete;
- the resolved observability and accessibility paths when missing;
- any discovery pointer that would change, with its project scope;
- every tracker label that would be created or changed.

For a repository entry, if both `AGENTS.md` and `CLAUDE.md` exist, ask which is canonical.
If one exists, use it. If neither exists, ask which one to create. For an external
entry, draft the confirmed external file instead. Update an existing `## Agent skills`
section in place and preserve surrounding user content. Include the project binding
in the external entry. Include repository edits only when selected in the draft.

The block contains the information-density rule and only applicable pointers, each with
a one-line project-specific summary. Point directly to the resolved observability
and accessibility paths; do not duplicate their policies in agent instructions. The
example below uses repository defaults; external entries use their resolved paths.

Use this shape, omitting only sections that genuinely do not apply:

```markdown
## Agent skills

### Information density
<the rule from `references/information-density.md`>

### Issue tracker
<repository-specific summary>. See `docs/agents/issue-tracker.md`.

### Tracker labels
<repository-specific summary>. See `docs/agents/triage-labels.md`.

### Domain docs
<single-context or multi-context summary>. See `docs/agents/domain.md`.

### Product documentation
<canonical destinations and representation summary>. See `docs/agents/product.md`.

### Observability
<repository-specific scope summary>. See `OBSERVABILITY.md`.

### Accessibility
<repository-specific scope summary>. See `ACCESSIBILITY.md`.
```

Wait for confirmation or edits to the drafts.

## 4. Write and verify

When reporting local configuration or document changes, apply
[local document delivery](../consolidate/references/local-document-delivery.md).

Create only confirmed files, directories, symlinks, and tracker labels. Existing
configuration is preserved unless the user explicitly approved its edit. Read back every external
label mutation. Check that every pointer resolves, every generated document describes
the actual project, and no placeholder remains. Verify the chosen configuration
discovery mechanism as described in the locations reference. For an external-only
setup, verify that the target repository was not changed by setup.

For global communication, read the policy through every configured agent's entry,
verify relative symlink targets, and check that rerunning setup would make no changes.

Finish by listing created or changed files and the skills that consume them. Tell the
user that the documents can be edited directly later and that setup should be rerun
only to fill another gap or intentionally revisit configuration.
