# Local skill links

`skills/` owns the editable copies. `.agents/skills/writing-for-agents` links to
that source within the repository. Imported provenance lives in
`skill-origins.json`; it does not enable automatic upstream replacement.

Point global installations at a stable canonical checkout so edits appear
immediately. Preview, then apply:

```sh
python3 scripts/link_skills.py --repo /Users/betofrega/Code/skills
python3 scripts/link_skills.py --repo /Users/betofrega/Code/skills --apply
```

The script links every repository skill into `~/.agents/skills`, saves replaced
copies and the previous installer registry in `~/.agents/skill-link-backups`,
and removes those skills from the skills CLI update registry. Other installed
skills remain as they are. Repeated runs keep links that already resolve to the
canonical source. If the canonical checkout moves, rerun with its new path.

Update the canonical checkout to receive repository changes. Pull upstream
skill changes deliberately into `skills/` when useful; local edits belong to
this repository. Existing skills with the same name take precedence over imports.
