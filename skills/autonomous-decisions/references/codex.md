# Codex Execution Adapter

Use native fresh-context agents when they expose the needed read-only tools and
model/effort controls. For independent CLI sessions, inspect the installed
`codex exec --help` and available model catalog before dispatching.

The bundled runner uses a fresh `codex exec` invocation with explicit model and
effort, `--sandbox read-only`, `--ephemeral`, `--ignore-user-config`, JSONL events,
and a final response schema. It disables apps, plugins, web search, and further
delegation. File-reading jobs retain sandboxed shell access; judges have shell
access disabled as well. It preserves execution-policy rules and approval checks.

The CLI sandbox governs model-generated commands. Connector permissions require
their own restrictions; inheriting a writable MCP tool is not a read-only assignment.
The bundled adapter supports supplied evidence and local file reading. When an
assignment needs another capability, provide a verified evidence packet or use a
native agent with the required explicitly limited read-only tools.

Each job has a private working directory and a prompt containing only the current
role and its inputs. A new session has no deliberation history. Local files still
share a host: keep allowed resources explicit and describe the actual isolation.
The parent runner saves returned artifacts outside the child's tool permissions.

Use `$autonomous-decisions` for explicit invocation. Codex's policy is declared in
[openai.yaml](../agents/openai.yaml).

For a CLI dispatch, read [cli.md](cli.md) for the shared manifest and artifact contract.

Sources: [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode),
[Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
