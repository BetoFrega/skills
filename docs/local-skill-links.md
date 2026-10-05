# Skill installation links

`skills/` owns the editable copies. Every repository skill is installed through a
relative symlink under the user's `~/.agents/skills`. Links under the repository's
`.agents/skills/` provide additional repository-local discovery. Imported
provenance lives in `skill-origins.json`; it does not enable automatic upstream
replacement.

The script discovers the repository's primary checkout through Git, including
when run from a linked worktree. It uses the script's repository directory when
Git metadata is absent. Preview, then apply from the repository:

```sh
python3 scripts/link_skills.py
python3 scripts/link_skills.py --apply
```

After creating or importing a skill in a worktree, install from that checkout
so it is available before delivery:

```sh
python3 scripts/link_skills.py --repo "$(git rev-parse --show-toplevel)"
python3 scripts/link_skills.py --repo "$(git rev-parse --show-toplevel)" --apply
```

After delivery, synchronize the primary checkout with remote `main`, then run
the default preview and apply commands again. This points installed skills at
the primary checkout before the worktree can be removed.

The script links every repository skill into `~/.agents/skills` using relative
paths calculated from the installation directory. It saves replaced
copies and the previous installer registry in `~/.agents/skill-link-backups`,
and removes those skills from the skills CLI update registry. Other installed
skills remain as they are. Repeated runs keep links that already resolve to the
canonical source. If the canonical checkout moves, rerun the script from its new
location. Use `--repo` only to choose a different checkout explicitly.

Update the canonical checkout to receive repository changes. Pull upstream
skill changes deliberately into `skills/` when useful; local edits belong to
this repository. Existing skills with the same name take precedence over imports.

Completion requires every repository skill's installed path to be a symlink with
a relative target, resolve to that skill in the chosen checkout, and expose a
readable `SKILL.md`. Rerun the preview: `linked` must be empty and `unchanged` must
include every repository skill. After delivery, the chosen checkout is the primary
checkout.
