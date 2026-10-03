import importlib.util
import json
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("link_skills", Path(__file__).with_name("link_skills.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class LinkSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "canonical"
        self.target = self.root / ".agents" / "skills"
        self.target.mkdir(parents=True)
        for name in ["alpha", "beta"]:
            source = self.repo / "skills" / name
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text(f"canonical {name}")
            installed = self.target / name
            installed.mkdir()
            (installed / "SKILL.md").write_text(f"installed {name}")
        self.other = self.target / "unrelated"
        self.other.mkdir()
        (self.other / "SKILL.md").write_text("unrelated")
        self.lock = self.target.parent / ".skill-lock.json"
        self.lock.write_text(json.dumps({"version": 3, "skills": {
            "alpha": {"source": "betofrega/skills"},
            "beta": {"source": "mattpocock/skills"},
            "unrelated": {"source": "other/skills"},
        }}))

    def test_links_follow_edits_preserve_backups_and_other_installations(self):
        preview = module.link_skills(self.repo, self.target)
        self.assertFalse(preview["applied"])
        self.assertFalse((self.target / "alpha").is_symlink())
        result = module.link_skills(self.repo, self.target, apply=True)
        self.assertFalse((self.target / "alpha").readlink().is_absolute())
        source = self.repo / "skills" / "alpha" / "SKILL.md"
        source.write_text("edited in canonical checkout")
        self.assertEqual((self.target / "alpha" / "SKILL.md").read_text(), source.read_text())
        self.assertEqual((Path(result["backup"]) / "alpha" / "SKILL.md").read_text(), "installed alpha")
        self.assertEqual(json.loads(self.lock.read_text())["skills"], {"unrelated": {"source": "other/skills"}})
        self.assertEqual((self.other / "SKILL.md").read_text(), "unrelated")
        repeated = module.link_skills(self.repo, self.target, apply=True)
        self.assertEqual(repeated["linked"], [])
        self.assertIsNone(repeated["backup"])

    def test_partial_failure_restores_copies_and_registry(self):
        original_lock = self.lock.read_bytes()
        real_symlink = Path.symlink_to

        def fail_second(destination, target, **kwargs):
            if destination.name == "beta":
                raise OSError("simulated link failure")
            return real_symlink(destination, target, **kwargs)

        with patch.object(Path, "symlink_to", fail_second):
            with self.assertRaisesRegex(OSError, "simulated"):
                module.link_skills(self.repo, self.target, apply=True)
        for name in ["alpha", "beta"]:
            self.assertFalse((self.target / name).is_symlink())
            self.assertEqual((self.target / name / "SKILL.md").read_text(), f"installed {name}")
        self.assertEqual(self.lock.read_bytes(), original_lock)

    def test_conflicting_origin_is_rejected_before_writes(self):
        lock = json.loads(self.lock.read_text())
        lock["skills"]["alpha"]["source"] = "other/skills"
        self.lock.write_text(json.dumps(lock))
        with self.assertRaisesRegex(ValueError, "Conflicting installed skill alpha"):
            module.link_skills(self.repo, self.target, apply=True)
        self.assertFalse((self.target / "alpha").is_symlink())
        self.assertFalse((self.target.parent / "skill-link-backups").exists())

    def test_primary_checkout_is_discovered_from_a_linked_worktree(self):
        def git(*args):
            return subprocess.check_output(["git", "-C", str(self.repo),
                                            "-c", "commit.gpgsign=false",
                                            "-c", "core.hooksPath=/dev/null", *args],
                                           stderr=subprocess.STDOUT)

        git("init", "--quiet")
        git("-c", "user.name=Test", "-c", "user.email=test@example.com",
            "commit", "--quiet", "--allow-empty", "-m", "Initialize test checkout")
        linked = self.root / "arbitrary folder" / "linked"
        git("worktree", "add", "--quiet", "--detach", str(linked))
        self.assertEqual(module.canonical_repo(linked).resolve(), self.repo.resolve())

    def test_relative_links_survive_moving_the_parent_directory(self):
        module.link_skills(self.repo, self.target, apply=True)
        moved = self.root.with_name(self.root.name + "-moved")
        self.root.rename(moved)
        try:
            self.assertEqual((moved / ".agents/skills/alpha/SKILL.md").read_text(), "canonical alpha")
        finally:
            moved.rename(self.root)


if __name__ == "__main__":
    unittest.main()
