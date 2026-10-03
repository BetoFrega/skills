# Claude Code Execution Adapter

Install this skill and `model-selection` in Claude Code's skill search paths. Use
`/autonomous-decisions` for explicit invocation. Keep the shared skill body and stage
references unchanged.

For a personal or project installation, merge the setting in
[claude.settings.json](../agents/claude.settings.json) into the existing Claude settings,
preserving unrelated settings. Alternatively pass that file with `--settings` for a
session. It makes this skill user-invocable only without adding Claude-specific
frontmatter to the shared entrypoint. `agents/openai.yaml` is Codex metadata and does
not configure Claude. For plugin distribution, set `disable-model-invocation: true`
in the generated Claude entrypoint: Claude's `skillOverrides` excludes plugin skills.

## Native agents

Use a fresh agent per assignment, with only its role instructions and necessary
inputs. Apply `model-selection` to available Claude models and supported efforts.
Set both through the dispatch interface or a role-specific agent definition; verify
the effective configuration when the environment inherits or substitutes a setting.
Use restricted read-only tools for deciders and verifiers. Judges receive the report
packet directly and have no research tools. A tool permission grant such as
`allowed-tools` is not a tool restriction.

## Independent CLI sessions

Inspect `claude --help` before using the bundled runner. Its Claude adapter uses
`--print`, `--restricted`, `--safe-mode`, `--no-session-persistence`, explicit model
and effort, a response schema, and strict empty MCP configuration. It disables
browser integration. Judges use `--tools ""`; file-reading jobs expose only
`Read,Glob,Grep` and explicitly named read directories. Permission prompts are
denied rather than bypassed.

Restricted mode and these switches require a supporting Claude Code version. If
unavailable, use a native restricted agent or report the missing capability. Keep
authentication in the CLI's existing mechanism; preserve the user's configuration.

Read [cli.md](cli.md) for the shared manifest and artifact contract, using
`provider: "claude"`. The runner unwraps Claude's
`structured_output` and records the effective model reported by the CLI.

The bundled adapter supports local files and supplied evidence. Use a native agent
with explicitly restricted read-only tools when the assignment requires additional
connectors or research capabilities. Preserve incomplete claims as unresolved.

Sources: [CLI reference](https://code.claude.com/docs/en/cli-reference),
[Skills](https://code.claude.com/docs/en/skills),
[Subagents](https://code.claude.com/docs/en/sub-agents).
