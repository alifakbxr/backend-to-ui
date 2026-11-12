#!/usr/bin/env python3
"""Validate the publishable Agent Skills repository with Python stdlib only."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "backend-to-ui"
REQUIRED_DOCS = (
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/USAGE.md",
    "docs/WORKFLOW.md",
    "docs/PUBLISHING.md",
    ".github/workflows/validate.yml",
)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_link_targets(file: Path) -> int:
    content = file.read_text(encoding="utf-8")
    # Standard Markdown links and images, excluding fenced code samples.
    content = re.sub(r"(?ms)^```.*?^```\s*$", "", content)
    count = 0
    for raw in re.findall(r"!?\[[^\]\n]*\]\(([^)]+)\)", content):
        target = raw.strip().split(" ")[0]
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        relative_path = target.split("#", 1)[0]
        resolved = (file.parent / relative_path).resolve()
        check(resolved.is_relative_to(ROOT), f"Link escapes repository: {file}: {target}")
        check(resolved.is_file(), f"Broken local link: {file}: {target}")
        count += 1
    return count


def main() -> None:
    skill_file = SKILL_DIR / "SKILL.md"
    check(skill_file.is_file(), "Missing skills/backend-to-ui/SKILL.md")
    skill = skill_file.read_text(encoding="utf-8")
    check(skill.startswith("---\n"), "SKILL.md must begin with YAML frontmatter")
    split = skill[4:].split("\n---\n", 1)
    check(len(split) == 2, "Malformed YAML frontmatter")
    frontmatter, body = split
    fields = dict(re.findall(r"(?m)^([a-z][a-z-]*):\s*([^\n]+)$", frontmatter))
    name = fields.get("name", "")
    description = fields.get("description", "")
    check(name == SKILL_DIR.name, "Name must match skill directory")
    check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), "Invalid skill name")
    check(0 < len(name) <= 64, "Skill name length out of spec")
    check(20 <= len(description) <= 1024, "Skill description should be 20-1024 chars")
    check("# Backend to UI" in body, "Skill body must have a heading")
    check(len(skill.splitlines()) < 500, "Keep SKILL.md concise; use references")

    for target in ("Inspect.", "Understand.", "Map.", "Plan for speed.", "Build.", "Test, critique, fix.", "Deliver."):
        check(target in body, f"Missing essential workflow step: {target}")
    for concept in ("permission", "backend", "speed", "test", "user"):
        check(concept in body.lower(), f"Essential concept missing: {concept}")

    refs = sorted((SKILL_DIR / "references").glob("*.md"))
    check(len(refs) >= 5, "Expected the core reference set")
    for ref in refs:
        check(ref.stat().st_size > 500, f"Reference unexpectedly empty: {ref}")
        check(ref.name in skill, f"Reference is not discoverable from SKILL.md: {ref.name}")

    for rel in REQUIRED_DOCS:
        path = ROOT / rel
        check(path.is_file(), f"Required documentation or CI file missing: {rel}")
        check(path.stat().st_size > 100, f"Suspiciously empty repository file: {rel}")

    cover, intro = ROOT / "media/cover.png", ROOT / "media/intro.mp4"
    check(cover.is_file() and cover.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", "Cover must be a valid PNG")
    check(intro.is_file() and b"ftyp" in intro.read_bytes()[:32], "Introduction must be an MP4")
    check(intro.stat().st_size < 10_000_000, "Keep committed introduction video under 10 MB")

    markdown_files = [ROOT / "README.md", ROOT / "SECURITY.md", ROOT / "CONTRIBUTING.md", *list((ROOT / "docs").glob("*.md")), skill_file, *refs]
    link_count = sum(check_link_targets(path) for path in markdown_files)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("[![Watch the introduction](media/cover.png)](media/intro.mp4)" in readme, "README must show a clickable video cover")
    check("--skill backend-to-ui" in readme, "README must specify the skill name")
    check("not a recording of a live API" in readme, "Demo provenance must be explicit")
    check("private" in (ROOT / "SECURITY.md").read_text().lower(), "Security reporting guidance missing")

    print(f"PASS: Agent Skill metadata, {len(refs)} references, {len(REQUIRED_DOCS)} docs/config files, {link_count} local links, cover and MP4")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
