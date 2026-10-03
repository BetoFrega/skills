# Frega Portal

Private plugin combining Beto Frega's agent skills with the existing remote MCP
endpoint https://mcp.frega.dev/mcp.

## Skills

The release includes every skill under this repository's `skills/` directory,
with its references, executable scripts, agent metadata, and assets. Skill content
is copied unchanged. `skills-inventory.json` records the included names and each
source file's SHA-256 digest and archived permissions. The repository's MIT license
is included.

The client discovers `skills/<name>/SKILL.md`. Select a skill from the client's
skill catalog or invoke its client-supported command. Metadata discovery and
loading a skill's instructions are separate from executing its workflow.
Codex presents packaged skills with the plugin prefix, such as
`frega-portal:decide` and `frega-portal:proceed`.

## Runtime requirements

Skills run through the host client's available tools and the target project's
configuration. The MCP connection supplies the portal's upstream tools; it does
not supply a shell, a repository checkout, or native Codex task management.

- `orchestrate` requires Codex task tools, an accessible GitHub project, and the
  project's separately installed `implement` skill. The release retains its
  explicit prerequisite checks.
- `advisory`, `autonomous-decisions`, and `code-review` require supported agent
  delegation. The autonomous decision CLI adapter also requires Python 3 and
  the selected provider's CLI.
- `model-selection` uses the host's model catalog and pricing data. Its Python
  helper reads a shared local cache and refreshes it only through the documented
  command.
- Repository, tracker, network, and publishing workflows require their documented
  project configuration, integrations, tools, and user authorization.

Clients with different capabilities can load the same instructions, but may be
unable to execute workflows whose prerequisites are unavailable.

## Connection

Install the plugin in a supported client and complete that client's OAuth flow.
Cloudflare Access and the upstream services control account permissions. This
package includes no credentials or copied sessions. The endpoint and OAuth
configuration are preserved from the existing plugin.

For hosted ChatGPT surfaces, MCP tools may require a registered connection and
its verified app binding. This release adds skill files to the existing package;
hosted execution remains dependent on that client's supported integrations.

## Build and update

From the skills repository, run:

```sh
python3 -m venv /tmp/frega-portal-builder
/tmp/frega-portal-builder/bin/python -m pip install -r scripts/frega_portal_requirements.txt
/tmp/frega-portal-builder/bin/python scripts/package_frega_portal.py --output /tmp/frega-portal.zip
```

The command validates manifests, skill frontmatter, relative Markdown references,
and the final archive. It uses tracked files under `skills/`, excluding tests and
Git ignore rules, and writes a reproducible ZIP containing one `frega-portal/`
directory. Build output belongs outside this source directory.

Every push to `main` validates and builds a CI artifact. Scheduled publication
is disabled. An explicitly requested update can publish changed content to the
same private plugin, preserving its MCP connection and audience. The release
preparer increments the current published version and treats executable permission
changes as new content. Unchanged content creates no release.

The repository's `plugins/frega-portal/PUBLISHING.md` describes the CI artifact,
publication protocol, verification, and recovery. Publication uses the observed
current release ID to guard updates against concurrent changes.

## Verification

After updating, read back the release, visibility, manifests, inventory, and
skill files. Refresh the installed plugin when the client offers an update and
confirm that its skill catalog discovers the packaged names. Load a skill and a
referenced document before claiming host behavior is verified.

Discover the portal's tools and run a read-only request to verify MCP connectivity.
Skills that mutate repositories, trackers, or content retain their original
authorization requirements.

## Formats

- `plugin.json` and `mcp.json`: portable Agent Plugins 1.0 package.
- `.codex-plugin/plugin.json` and `.mcp.json`: Codex compatibility layout.
- `skills/`: the packaged workflows and supporting files.
