#!/usr/bin/env python3
"""Link installed skills to a maintained checkout, retaining replaced copies."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone


def canonical_repo(checkout=None):
    checkout = Path(checkout or Path(__file__).resolve().parents[1]).resolve()
    try:
        listing = subprocess.check_output(
            ["git", "-C", str(checkout), "worktree", "list", "--porcelain", "-z"],
            stderr=subprocess.DEVNULL,
        ).decode()
    except (OSError, subprocess.CalledProcessError):
        return checkout
    return Path(listing.split("\0", 1)[0].removeprefix("worktree "))


def atomic_write(path, content):
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix=".skill-lock-")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def link_skills(repo, target, apply=False):
    repo = Path(repo).resolve(strict=True)
    target = Path(target).absolute()
    sources = sorted((repo / "skills").glob("*/SKILL.md"))
    if not sources:
        raise ValueError(f"No skills found in {repo / 'skills'}")
    # A directory symlink would redirect all mutations somewhere else.
    if target.is_symlink():
        raise ValueError(f"The installation directory must be a real directory: {target}")
    target = target.resolve()
    names = [source.parent.name for source in sources]
    lock_path = target.parent / ".skill-lock.json"
    lock_bytes = lock_path.read_bytes() if lock_path.exists() else None
    lock = json.loads(lock_bytes) if lock_bytes is not None else None
    managed = lock.get("skills", {}) if lock else {}
    for name in names:
        origin = managed.get(name, {}).get("source")
        if origin and origin.lower() not in {"betofrega/skills", "mattpocock/skills"}:
            raise ValueError(f"Conflicting installed skill {name}: {origin}")
    changes, unchanged = [], []
    for source in sources:
        destination = target / source.parent.name
        relative = os.path.relpath(source.parent, target)
        if destination.is_symlink() and destination.readlink() == Path(relative):
            unchanged.append(source.parent.name)
        else:
            changes.append((source.parent, destination))
    registry_names = sorted(set(names) & managed.keys())
    result = {
        "repo": str(repo), "target": str(target), "applied": apply,
        "linked": [source.name for source, _ in changes],
        "unchanged": unchanged, "unmanaged_registry_entries": registry_names,
        "backup": None,
    }
    if not apply or (not changes and not registry_names):
        return result
    target.mkdir(parents=True, exist_ok=True)
    backups = target.parent / "skill-link-backups"
    backups.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-")
    backup = Path(tempfile.mkdtemp(prefix=timestamp, dir=backups))
    if lock_bytes is not None:
        (backup / ".skill-lock.json").write_bytes(lock_bytes)
    completed = []
    try:
        for source, destination in changes:
            saved = backup / destination.name
            existed = os.path.lexists(destination)
            if existed:
                destination.rename(saved)
            completed.append((destination, saved, existed))
            destination.symlink_to(os.path.relpath(source, target), target_is_directory=True)
        # Repository links are maintained locally, outside skills CLI update tracking.
        if registry_names:
            for name in registry_names:
                del managed[name]
            atomic_write(lock_path, (json.dumps(lock, indent=2) + "\n").encode())
        for name in names:
            destination = target / name
            if not destination.is_symlink() or destination.resolve() != repo / "skills" / name:
                raise RuntimeError(f"Link verification failed: {destination}")
            if not (destination / "SKILL.md").is_file():
                raise RuntimeError(f"Missing skill through link: {destination}")
    except Exception:
        for destination, saved, existed in reversed(completed):
            if destination.is_symlink():
                destination.unlink()
            if existed:
                saved.rename(destination)
        if lock_bytes is not None and lock_path.read_bytes() != lock_bytes:
            atomic_write(lock_path, lock_bytes)
        raise
    result["backup"] = str(backup)
    (backup / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=canonical_repo(),
                        help="Override the primary checkout discovered from this script's repository")
    parser.add_argument("--target", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--apply", action="store_true", help="Apply the previewed links")
    args = parser.parse_args()
    print(json.dumps(link_skills(args.repo, args.target, args.apply), indent=2))


if __name__ == "__main__":
    main()
