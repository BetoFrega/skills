#!/usr/bin/env python3
"""Prepare a guarded private update from an approved main-branch CI artifact."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

from package_frega_portal import PACKAGE_NAME, SOURCE, content_digest, write_archive


def read_artifact(path, expected_commit):
    files, modes = {}, {}
    with zipfile.ZipFile(path) as archive:
        if sum(info.file_size for info in archive.infolist()) > 20 * 1024 * 1024:
            raise ValueError("Plugin artifact exceeds 20 MiB")
        for info in archive.infolist():
            parts = PurePosixPath(info.filename).parts
            if len(parts) < 2 or parts[0] != PACKAGE_NAME or '..' in parts or '\\' in info.filename:
                raise ValueError("Unexpected artifact path")
            if info.is_dir() or stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError("Only regular artifact files are supported")
            name = '/'.join(parts[1:])
            if name in files:
                raise ValueError("Duplicate artifact path")
            files[name] = archive.read(info)
            modes[name] = info.external_attr >> 16 or 0o100644
    inventory = json.loads(files['skills-inventory.json'])
    if inventory['plugin'] != PACKAGE_NAME or inventory['source_commit'] != expected_commit:
        raise ValueError("Artifact does not match the selected main commit")
    if inventory.get('skills_worktree_modified') is not False:
        raise ValueError("Artifact must come from an unmodified CI checkout")
    source_files = set(files) - {'skills-inventory.json'}
    if source_files != set(inventory['files']):
        raise ValueError("Incomplete artifact inventory")
    for name in source_files:
        if hashlib.sha256(files[name]).hexdigest() != inventory['files'][name]:
            raise ValueError(f"Artifact hash mismatch: {name}")
    digest = content_digest(files)
    if digest != inventory['content_digest']:
        raise ValueError("Artifact content digest mismatch")
    paths = {name for name in files if name.startswith('skills/') and name.endswith('/SKILL.md')}
    if paths != {skill['path'] for skill in inventory['skills']} or len(paths) != inventory['skill_count']:
        raise ValueError("Artifact skill inventory mismatch")
    return files, modes, inventory


def version_tuple(version):
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError("Private releases require a semantic version")
    return tuple(int(part) for part in version.split('.'))


def prepare(artifact, current, expected_commit, output, run_id):
    binding = json.loads((SOURCE / 'publication.json').read_text())
    plugin = current['plugin']
    for field, expected in [('plugin_id', binding['plugin_id']), ('name', binding['plugin_name']),
                            ('scope', binding['scope']), ('discoverability', 'PRIVATE')]:
        if plugin.get(field) != expected:
            raise ValueError(f"Current plugin does not match the private binding: {field}")
    release_id = plugin.get('current_release_id')
    if not release_id:
        raise ValueError("A guarded update requires the current release ID")
    files, modes, inventory = read_artifact(artifact, expected_commit)
    contents = current['contents']
    for name in ['mcp.json', '.mcp.json']:
        if json.loads(contents[name]) != json.loads(files[name]):
            raise ValueError("Automatic skill publication preserves MCP configuration")
    manifest = json.loads(files['plugin.json'])
    published_manifest = json.loads(contents['plugin.json'])
    if published_manifest['version'] != plugin['version']:
        raise ValueError("Current metadata and source versions disagree; refresh the release")
    if manifest['name'] != plugin['name'] or manifest['author'] != published_manifest['author']:
        raise ValueError("Automatic publication preserves plugin identity and author")
    if manifest['extensions']['com.openai']['interface']['defaultPrompt'] != published_manifest['extensions']['com.openai']['interface']['defaultPrompt']:
        raise ValueError("Automatic publication preserves the full default prompt")
    remote_paths = {entry['path'] for entry in current['files']}
    removed = remote_paths - set(files)
    if removed:
        raise ValueError("The overlay update API cannot delete files: " + ', '.join(sorted(removed)))
    previous = json.loads(contents['skills-inventory.json'])
    if previous.get('content_digest') == inventory['content_digest']:
        return {'status': 'unchanged', 'plugin_id': plugin['plugin_id'],
                'release_id': release_id, 'version': plugin['version'],
                'source_commit': expected_commit, 'content_digest': inventory['content_digest']}
    major, minor, patch = version_tuple(plugin['version'])
    next_version = max((major, minor, patch + 1), version_tuple(manifest['version']))
    version = '.'.join(str(part) for part in next_version)
    for name in ['plugin.json', '.codex-plugin/plugin.json']:
        data = json.loads(files[name])
        if data['name'] != PACKAGE_NAME:
            raise ValueError("Artifact manifest identity mismatch")
        data['version'] = version
        files[name] = (json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode()
    inventory['version'] = version
    inventory['ci_run_id'] = run_id
    inventory['files'] = {name: hashlib.sha256(data).hexdigest() for name, data in sorted(files.items())
                          if name != 'skills-inventory.json'}
    files['skills-inventory.json'] = (json.dumps(inventory, indent=2) + '\n').encode()
    write_archive(files, output, modes)
    return {'status': 'ready', 'archive': str(output.resolve()), 'plugin_id': plugin['plugin_id'],
            'expected_release_id': release_id, 'version': version, 'source_commit': expected_commit,
            'ci_run_id': run_id, 'content_digest': inventory['content_digest'],
            'skill_count': inventory['skill_count'], 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, required=True)
    parser.add_argument('--current', type=Path, required=True,
                        help='Current get_plugin_files result: plugin, contents, and all files')
    parser.add_argument('--commit', required=True)
    parser.add_argument('--run-id', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.commit) or args.run_id <= 0:
        parser.error('Use the approved full main commit SHA and positive CI run ID')
    if args.output.suffix != '.zip' or args.output.resolve() == args.artifact.resolve():
        parser.error('Write a separate release .zip file')
    result = prepare(args.artifact, json.loads(args.current.read_text()), args.commit,
                     args.output, args.run_id)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
