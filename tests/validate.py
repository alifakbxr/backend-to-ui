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
    "evals/README.md",
    "evals/scenarios.json",
    "evals/score.py",
    "tests/test_evals.py",
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

    for target in ("Inspect.", "Understand.", "Map.", "Plan for speed.", "Art direct.", "Build.", "Test, critique, fix.", "Deliver."):
        check(target in body, f"Missing essential workflow step: {target}")
    for concept in ("permission", "backend", "speed", "test", "user"):
        check(concept in body.lower(), f"Essential concept missing: {concept}")

    refs = sorted((SKILL_DIR / "references").glob("*.md"))
    check(len(refs) >= 5, "Expected the core reference set")
    for ref in refs:
        check(ref.stat().st_size > 500, f"Reference unexpectedly empty: {ref}")
        check(ref.name in skill, f"Reference is not discoverable from SKILL.md: {ref.name}")

    # Regression gate: generic-skin redesigns must be explicitly blocked by skill guidance.
    check("product mode" in skill.lower(), "Skill must require product-mode analysis")
    check("mandatory frontend stack gate" in skill.lower(), "Missing mandatory frontend stack gate")
    check("ask one direct question" in skill.lower(), "Missing ask-first requirement")
    check("never silently fall back to native html" in skill.lower(), "Missing native HTML fallback prohibition")
    policy = (SKILL_DIR / "references/stack-selection.md").read_text(encoding="utf-8").lower()
    check("do not create or edit frontend implementation files until answered" in policy,
          "Stack policy must forbid edits before approval")
    check("two materially different compositions" in skill.lower(), "Skill must require competing compositions")
    check("actual rendered desktop and mobile screenshots" in skill.lower(), "Skill must require render-based critique")
    visual = (SKILL_DIR / "references/visual-review.md").read_text(encoding="utf-8").lower()
    case_studies = (SKILL_DIR / "references/cases.md").read_text(encoding="utf-8").lower()
    check("stop-ship" in visual and "viewport composition" in visual, "Missing visual stop-ship gate")
    check("gacha" in case_studies and "warehouse" in case_studies, "Missing contrasting design case studies")
    check((SKILL_DIR / "references/existing-frontend.md").is_file(), "Missing existing frontend playbook")
    check("existing frontend" in skill.lower(), "Missing support for established frontend projects")
    check("frontend-only" in (SKILL_DIR / "references/existing-frontend.md").read_text(encoding="utf-8").lower(),
          "Existing frontend playbook must allow projects without a backend")

    for rel in REQUIRED_DOCS:
        path = ROOT / rel
        check(path.is_file(), f"Required documentation or CI file missing: {rel}")
        check(path.stat().st_size > 100, f"Suspiciously empty repository file: {rel}")

    gif = ROOT / "media/intro.gif"
    check(gif.is_file() and gif.read_bytes()[:6] in (b"GIF89a", b"GIF87a"),
          "Introduction must be a valid GIF")
    check(gif.stat().st_size < 3_000_000, "Keep committed introduction GIF under 3 MB")
    check(not (ROOT / "docs").exists(), "The docs/ folder should be removed after consolidation")
    movie = ROOT / "media/intro.mp4"
    check(movie.is_file() and b"ftyp" in movie.read_bytes()[:32], "Video must be an MP4")
    check(movie.stat().st_size < 5_000_000, "Keep the MP4 under 5 MB")
    cover = ROOT / "media/cover.png"
    check(cover.is_file() and cover.read_bytes()[:8] == bytes.fromhex("89504e470d0a1a0a"),
          "Cover must be a valid PNG")
    check((ROOT / "scripts/render_intro.py").is_file(), "Missing motion source generator")

    markdown_files = [ROOT / "README.md", ROOT / "SECURITY.md", ROOT / "CONTRIBUTING.md",
                      ROOT / "evals/README.md", skill_file, *refs]
    link_count = sum(check_link_targets(path) for path in markdown_files)

    # The evaluator scenarios are consistency-checked separately by unittest.
    import json
    scenarios = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
    check(scenarios.get("schema_version") == 1, "Unsupported evaluation schema")
    cases = scenarios.get("scenarios", [])
    check(len(cases) >= 25, "Not enough evaluation scenarios")
    check({"ask_stack", "implement", "audit"}.issubset({c["expected"]["action"] for c in cases}),
          "Missing stack/implementation/audit scenario classes")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("![product-ui — introduction](media/intro.gif)" in readme, "README must display the GIF")
    check("[Watch the 30 FPS introduction with audio](media/intro.mp4)" in readme, "README must link the full video")
    check("--skill backend-to-ui" in readme, "README must specify the skill name")
    check("illustrative motion concept" in readme.lower() and "not a claim of live backend integration" in readme.lower(), "Demo provenance must be explicit")
    check("private" in (ROOT / "SECURITY.md").read_text().lower(), "Security reporting guidance missing")

    print(f"PASS: Agent Skill metadata, {len(refs)} references, {len(REQUIRED_DOCS)} docs/config files, {link_count} local links, intro GIF and MP4")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
