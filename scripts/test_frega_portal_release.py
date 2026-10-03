"""Exercise the boundaries before an automated account-plugin mutation."""

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from package_frega_portal import collect_files, collect_modes, content_digest, validate, write_archive
from prepare_frega_portal_release import prepare, read_artifact


COMMIT = 'a' * 40
PLUGIN_ID = 'plugins_6abd6d03d40081919659c0ee5d6979c9'


class PrivateReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = collect_files()
        self.skills = [{'name': Path(path).parent.name, 'path': path}
                       for path in self.source if path.endswith('/SKILL.md')]
        self.base_inventory = self.inventory(self.source)
        self.current = {
            'plugin': {'plugin_id': PLUGIN_ID, 'name': 'frega-portal', 'scope': 'USER',
                       'discoverability': 'PRIVATE', 'version': '0.2.0',
                       'current_release_id': 'pluginrel-current'},
            'files': [{'path': path} for path in self.source] + [{'path': 'skills-inventory.json'}],
            'contents': {path: data.decode() for path, data in self.source.items()
                         if path in {'plugin.json', '.codex-plugin/plugin.json', 'mcp.json', '.mcp.json'}},
        }
        self.current['contents']['skills-inventory.json'] = json.dumps(self.base_inventory)
        self.candidate = dict(self.source)
        self.candidate['skills/proceed/SKILL.md'] += b'\nA changed workflow instruction.\n'
        self.artifact = self.root / 'candidate.zip'
        self.output = self.root / 'release.zip'
        self.write_candidate(self.candidate)

    def inventory(self, files, modes=None):
        modes = collect_modes(files) if modes is None else modes
        return {'plugin': 'frega-portal', 'version': '0.2.0', 'source_commit': COMMIT,
                'skills_worktree_modified': False, 'content_digest_schema': 2,
                'content_digest': content_digest(files, modes), 'file_modes': modes,
                'skill_count': len(self.skills), 'skills': self.skills,
                'files': {path: hashlib.sha256(data).hexdigest() for path, data in files.items()}}

    def write_candidate(self, files, modes=None):
        modes = collect_modes(files) if modes is None else modes
        complete = dict(files)
        complete['skills-inventory.json'] = json.dumps(self.inventory(files, modes)).encode()
        write_archive(complete, self.artifact, modes)

    def prepare(self, current=None):
        return prepare(self.artifact, current or self.current, COMMIT, self.output, 123)

    def test_changed_content_prepares_guarded_next_version(self):
        result = self.prepare()
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(result['version'], '0.2.1')
        self.assertEqual(result['expected_release_id'], 'pluginrel-current')
        files, _, inventory = read_artifact(self.output, COMMIT)
        self.assertEqual(inventory['ci_run_id'], 123)
        self.assertEqual(json.loads(files['plugin.json'])['version'], '0.2.1')
        self.assertEqual(json.loads(files['.codex-plugin/plugin.json'])['version'], '0.2.1')

    def test_same_content_creates_no_archive_or_version(self):
        self.write_candidate(self.source)
        result = self.prepare()
        self.assertEqual(result['status'], 'unchanged')
        self.assertFalse(self.output.exists())

    def test_release_number_alone_does_not_change_digest(self):
        files = dict(self.source)
        for path in ['plugin.json', '.codex-plugin/plugin.json']:
            value = json.loads(files[path])
            value['version'] = '7.8.9'
            files[path] = json.dumps(value).encode()
        modes = collect_modes(self.source)
        self.assertEqual(content_digest(files, modes), content_digest(self.source, modes))

    def test_privacy_identity_and_scope_are_required(self):
        for field, value in [('discoverability', 'LISTED'), ('scope', 'WORKSPACE'),
                             ('plugin_id', 'plugins-another'), ('name', 'another-plugin')]:
            with self.subTest(field=field):
                current = copy.deepcopy(self.current)
                current['plugin'][field] = value
                with self.assertRaisesRegex(ValueError, 'private binding'):
                    self.prepare(current)

    def test_overlay_cannot_silently_keep_deleted_skill(self):
        current = copy.deepcopy(self.current)
        current['files'].append({'path': 'skills/removed/SKILL.md'})
        with self.assertRaisesRegex(ValueError, 'cannot delete files'):
            self.prepare(current)

    def test_guard_requires_observed_release_id(self):
        current = copy.deepcopy(self.current)
        current['plugin'].pop('current_release_id')
        with self.assertRaisesRegex(ValueError, 'current release ID'):
            self.prepare(current)

    def test_mcp_change_requires_manual_handling(self):
        candidate = dict(self.candidate)
        value = json.loads(candidate['mcp.json'])
        value['mcpServers']['frega-portal']['url'] = 'https://different.example/mcp'
        candidate['mcp.json'] = json.dumps(value).encode()
        self.write_candidate(candidate)
        with self.assertRaisesRegex(ValueError, 'preserves MCP'):
            self.prepare()

    def test_current_version_drives_monotonic_next_version(self):
        current = copy.deepcopy(self.current)
        current['plugin']['version'] = '1.4.9'
        for name in ['plugin.json', '.codex-plugin/plugin.json']:
            data = json.loads(current['contents'][name])
            data['version'] = '1.4.9'
            current['contents'][name] = json.dumps(data)
        self.assertEqual(self.prepare(current)['version'], '1.4.10')

    def test_mixed_release_snapshot_is_rejected(self):
        current = copy.deepcopy(self.current)
        current['plugin']['version'] = '0.2.7'
        with self.assertRaisesRegex(ValueError, 'versions disagree'):
            self.prepare(current)

    def test_default_prompt_change_requires_manual_handling(self):
        candidate = dict(self.candidate)
        data = json.loads(candidate['plugin.json'])
        data['extensions']['com.openai']['interface']['defaultPrompt'] = 'Different prompt'
        candidate['plugin.json'] = json.dumps(data).encode()
        self.write_candidate(candidate)
        with self.assertRaisesRegex(ValueError, 'full default prompt'):
            self.prepare()

    def test_commit_mismatch_cannot_publish(self):
        with self.assertRaisesRegex(ValueError, 'selected main commit'):
            prepare(self.artifact, self.current, 'b' * 40, self.output, 123)

    def test_modified_skill_is_detected_by_inventory(self):
        with zipfile.ZipFile(self.artifact, 'a') as archive:
            archive.writestr('frega-portal/skills/untracked/SKILL.md', b'Injected content')
        with self.assertRaisesRegex(ValueError, 'Incomplete artifact inventory'):
            self.prepare()

    def test_path_traversal_is_rejected_before_loading(self):
        with zipfile.ZipFile(self.artifact, 'a') as archive:
            archive.writestr('frega-portal/../escape', b'Unexpected file')
        with self.assertRaisesRegex(ValueError, 'Unexpected artifact path'):
            self.prepare()

    def test_two_builds_have_identical_archive_bytes(self):
        initial = self.artifact.read_bytes()
        self.write_candidate(self.candidate)
        self.assertEqual(initial, self.artifact.read_bytes())

    def test_skill_frontmatter_rejects_invalid_yaml_and_metadata_types(self):
        for frontmatter in [
            'name: proceed\ndescription: [unterminated',
            'name: proceed\ndescription: Valid\nmetadata: [unterminated',
            'name: proceed\ndescription: [a, list]',
            'name: proceed\ndescription: true',
            'name: proceed\ndescription: "   "',
            'name: [proceed]\ndescription: Valid',
            '- proceed\n- description',
            'name: proceed\ndescription: !!python/object:builtins.object {}',
        ]:
            with self.subTest(frontmatter=frontmatter):
                files = dict(self.source)
                files['skills/proceed/SKILL.md'] = ('---\n' + frontmatter + '\n---\nBody.\n').encode()
                with self.assertRaisesRegex(ValueError, 'frontmatter|name or description'):
                    validate(files)

    def test_skill_frontmatter_accepts_yaml_quoted_and_block_strings(self):
        for description in ['"Text with: punctuation --- inside"', '|\n  First line.\n  Second line.', '>\n  Folded description.']:
            with self.subTest(description=description):
                files = dict(self.source)
                files['skills/proceed/SKILL.md'] = ('---\nname: "proceed"\ndescription: ' + description + '\n---\nBody.\n').encode()
                _, skills = validate(files)
                self.assertIn({'name': 'proceed', 'path': 'skills/proceed/SKILL.md'}, skills)

    def test_mode_only_change_prepares_release_and_preserves_permissions(self):
        target = next(path for path in self.source if path.startswith('skills/') and path.endswith('.py'))
        for before, after in [(0o100644, 0o100755), (0o100755, 0o100644)]:
            with self.subTest(before=oct(before), after=oct(after)):
                old_modes = collect_modes(self.source)
                old_modes[target] = before
                current = copy.deepcopy(self.current)
                current['contents']['skills-inventory.json'] = json.dumps(self.inventory(self.source, old_modes))
                new_modes = dict(old_modes)
                new_modes[target] = after
                self.write_candidate(self.source, new_modes)
                result = self.prepare(current)
                self.assertEqual(result['status'], 'ready')
                _, modes, inventory = read_artifact(self.output, COMMIT)
                self.assertEqual(modes[target], after)
                self.assertEqual(inventory['file_modes'][target], after)
                self.assertNotEqual(result['content_digest'], self.inventory(self.source, old_modes)['content_digest'])

    def test_archive_mode_tampering_is_rejected(self):
        with zipfile.ZipFile(self.artifact) as archive:
            entries = [(info, archive.read(info)) for info in archive.infolist()]
        with zipfile.ZipFile(self.artifact, 'w') as archive:
            for info, data in entries:
                if info.filename.endswith('/skills/proceed/SKILL.md'):
                    info.external_attr = 0o100755 << 16
                archive.writestr(info, data)
        with self.assertRaisesRegex(ValueError, 'mode inventory mismatch'):
            self.prepare()

    def test_legacy_published_digest_migrates_once(self):
        current = copy.deepcopy(self.current)
        previous = json.loads(current['contents']['skills-inventory.json'])
        previous.pop('content_digest_schema')
        previous.pop('file_modes')
        previous['content_digest'] = 'legacy-byte-only-digest'
        current['contents']['skills-inventory.json'] = json.dumps(previous)
        self.write_candidate(self.source)
        self.assertEqual(self.prepare(current)['status'], 'ready')
        _, _, inventory = read_artifact(self.output, COMMIT)
        current['contents']['skills-inventory.json'] = json.dumps(inventory)
        self.assertEqual(self.prepare(current)['status'], 'unchanged')


if __name__ == '__main__':
    unittest.main()
