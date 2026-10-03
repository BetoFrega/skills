# Local skill links

`skills/` owns the editable copies. `.agents/skills/writing-for-agents` links to
that source within the repository. Imported provenance lives in
`skill-origins.json`; it does not enable automatic upstream replacement.

The script discovers the repository's primary checkout through Git, including
when run from a linked worktree. It uses the script's repository directory when
Git metadata is absent. Preview, then apply from the repository:

```sh
python3 scripts/link_skills.py
python3 scripts/link_skills.py --apply
```

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
