#!/usr/bin/env python3
"""Build the private Frega Portal package from its manifests and tracked skills."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins" / "frega-portal"
PACKAGE_NAME = "frega-portal"
SOURCE_FILES = (
    "plugin.json", "mcp.json", ".codex-plugin/plugin.json", ".mcp.json", "README.md"
)


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def read_file(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular source file: {path}")
    return path.read_bytes()


def collect_files():
    files = {name: read_file(SOURCE / name) for name in SOURCE_FILES}
    files["LICENSE"] = read_file(ROOT / "LICENSE")
    tracked = git("ls-files", "-z", "--", "skills").decode().split("\0")
    for name in sorted(filter(None, tracked)):
        path = Path(name)
        if "tests" in path.parts or path.name == ".gitignore":
            continue
        if path.name.startswith(".") or path.suffix in {".pyc", ".zip"}:
            raise ValueError(f"Unexpected packaged skill file: {name}")
        files[path.as_posix()] = read_file(ROOT / path)
    return files


def validate(files):
    manifest = json.loads(files["plugin.json"])
    overlay = json.loads(files[".codex-plugin/plugin.json"])
    if manifest["name"] != PACKAGE_NAME or overlay["name"] != PACKAGE_NAME:
        raise ValueError("Both manifests must retain the Frega Portal identity")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
        raise ValueError("Use a semantic release version")
    for field in ("version", "description", "author"):
        if manifest[field] != overlay[field]:
            raise ValueError(f"Manifest mismatch: {field}")
    interface = manifest["extensions"]["com.openai"]["interface"]
    if interface != overlay["interface"] or len(interface["shortDescription"]) > 30:
        raise ValueError("Invalid or inconsistent presentation metadata")
    if overlay.get("skills") not in {"./skills", "./skills/"} or overlay["mcpServers"] != "./.mcp.json":
        raise ValueError("Unexpected compatibility component paths")
    modern = json.loads(files["mcp.json"])["mcpServers"]
    legacy = json.loads(files[".mcp.json"])["mcpServers"]
    if set(modern) != {PACKAGE_NAME} or set(legacy) != {PACKAGE_NAME}:
        raise ValueError("Unexpected MCP server identity")
    for config in (modern[PACKAGE_NAME], legacy[PACKAGE_NAME]):
        if config["type"] != "streamable-http" or config["url"] != "https://mcp.frega.dev/mcp":
            raise ValueError("The portal endpoint and transport must be preserved")
        if config.get("headers"):
            raise ValueError("Use host-managed OAuth without packaged credentials")

    skills = []
    for name, content in sorted(files.items()):
        path = Path(name)
        if path.name == "SKILL.md":
            text = content.decode()
            if not text.startswith("---\n") or "\n---\n" not in text[4:]:
                raise ValueError(f"Missing skill frontmatter: {name}")
            frontmatter = text.split("---", 2)[1]
            skill_name = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.M)
            description = re.search(r"^description:\s*([^\n]+)$", frontmatter, re.M)
            if not skill_name or skill_name[1].strip() != path.parent.name or not description:
                raise ValueError(f"Invalid skill name or description: {name}")
            skills.append({"name": path.parent.name, "path": name})
        if path.suffix == ".md" and path.parts[0] == "skills":
            for link in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content.decode()):
                link = link.strip().split("#", 1)[0]
                if not link or ":" in link:
                    continue
                target = (ROOT / path.parent / link).resolve()
                if not target.is_relative_to(ROOT):
                    raise ValueError(f"Reference escapes the repository: {name}: {link}")
                relative = target.relative_to(ROOT).as_posix()
                if relative not in files:
                    raise ValueError(f"Reference missing from package: {name}: {link}")
    if not skills:
        raise ValueError("The plugin must include skills")
    available = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
    if available != sorted(skill["name"] for skill in skills):
        raise ValueError("All repository skills must be tracked and included")
    return manifest, skills


def content_digest(files):
    """Identify package content independently of release numbers and Git commits."""
    hashes = {}
    for name, data in sorted(files.items()):
        if name == "skills-inventory.json":
            continue
        if name in {"plugin.json", ".codex-plugin/plugin.json"}:
            manifest = json.loads(data)
            manifest.pop("version", None)
            if isinstance(manifest.get("skills"), str):
                manifest["skills"] = manifest["skills"].rstrip("/")
            data = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
        hashes[name] = hashlib.sha256(data).hexdigest()
    return hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()


def write_archive(files, output, modes=None):
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(f"{PACKAGE_NAME}/{name}", (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            source = ROOT / name if name.startswith("skills/") else SOURCE / name
            mode = 0o100755 if source.exists() and source.stat().st_mode & 0o111 else 0o100644
            info.external_attr = (modes or {}).get(name, mode) << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(files):
            raise ValueError("Invalid or incomplete archive")
        for name, data in files.items():
            if archive.read(f"{PACKAGE_NAME}/{name}") != data:
                raise ValueError(f"Archive mismatch: {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(SOURCE) or output.suffix != ".zip":
        parser.error("Write a .zip archive outside plugins/frega-portal")
    files = collect_files()
    manifest, skills = validate(files)
    inventory = {
        "plugin": PACKAGE_NAME,
        "version": manifest["version"],
        "source_repository": "https://github.com/BetoFrega/skills",
        "source_commit": git("rev-parse", "HEAD").decode().strip(),
        "skills_worktree_modified": bool(git("status", "--porcelain", "--", "skills")),
        "content_digest": content_digest(files),
        "skill_count": len(skills),
        "skills": skills,
        "external_skill_requirements": {"orchestrate": ["implement"]},
        "files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(files.items())},
    }
    files["skills-inventory.json"] = (json.dumps(inventory, indent=2) + "\n").encode()
    write_archive(files, output)
    print(json.dumps({"archive": str(output), "version": manifest["version"],
                      "skill_count": len(skills), "file_count": len(files),
                      "source_commit": inventory["source_commit"],
                      "content_digest": inventory["content_digest"],
                      "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
