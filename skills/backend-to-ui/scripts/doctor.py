#!/usr/bin/env python3
"""Read-only host skill diagnostic. On-disk checks NEVER prove activation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

NAME = "backend-to-ui"
HOSTS = ("antigravity", "antigravity-cli", "gemini-cli", "codex")

def locations(host: str, home: Path, workspace: Path | None) -> list[tuple[str, Path]]:
    gem = home / ".gemini"
    if host in ("antigravity", "antigravity-cli"):
        items = [("shared-global", gem / "config/skills" / NAME)]
        if host == "antigravity":
            items.append(("legacy-global", gem / "antigravity/skills" / NAME))
        else:
            items += [("cli-only", gem / "antigravity-cli/skills" / NAME), ("cli-only", gem / "skills" / NAME)]
    elif host == "gemini-cli":
        items = [("global", gem / "skills" / NAME), ("global-alias", home / ".agents/skills" / NAME)]
    elif host == "codex":
        items = [("global", home / ".agents/skills" / NAME)]
    else:
        raise ValueError(host)
    if workspace:
        items.append(("workspace", workspace / ".agents/skills" / NAME))
        if host == "gemini-cli":
            items.append(("workspace-gemini", workspace / ".gemini/skills" / NAME))
    return items

def checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inspect(host: str, home: Path, workspace: Path | None, reference: Path | None) -> dict:
    source_hash = checksum(reference) if reference and reference.is_file() else None
    candidates: list[dict] = []
    for scope, directory in locations(host, home, workspace):
        path = directory / "SKILL.md"
        item = {"scope": scope, "path": str(path), "found": path.is_file(), "valid": False}
        if directory.is_symlink() and not directory.exists():
            item["problem"] = "broken symlink"
        elif path.is_file():
            try:
                body = path.read_text(encoding="utf-8")
                valid = body.startswith("---\n") and bool(re.search(r"(?m)^name:\s*backend-to-ui\s*$", body)) and "description:" in body
                item["valid"] = valid
                item["sha256"] = checksum(path)
                if not valid:
                    item["problem"] = "invalid metadata"
                elif source_hash and item["sha256"] != source_hash:
                    item["problem"] = "different from reference version"
            except (UnicodeError, OSError) as exc:
                item["problem"] = f"unreadable: {exc}"
        candidates.append(item)
    found = [c for c in candidates if c["found"]]
    diverging = len({c.get("sha256") for c in found if c["valid"]}) > 1
    problems = [c["problem"] for c in candidates if c.get("problem")]
    if diverging:
        problems.append("conflicting copies; host precedence may shadow the intended version")
    ok = bool(found) and any(c["valid"] for c in found) and not problems
    return {
        "host": host, "installed_on_disk": bool(found),
        "filesystem_discovery_ok": ok,
        "host_discovered": "unverified", "activated": "unverified",
        "candidates": candidates, "problems": problems,
    }

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=(*HOSTS, "all"), default="all")
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--source", type=Path, help="Reference SKILL.md to detect stale copies")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    source = args.source or Path(__file__).resolve().parents[1] / "SKILL.md"
    hosts = HOSTS if args.host == "all" else (args.host,)
    result = [inspect(host, args.home.expanduser(), args.workspace, source) for host in hosts]
    if args.json:
        print(json.dumps({"source": str(source), "hosts": result}, indent=2))
    else:
        for item in result:
            print(f"{item['host']}: {'FILES OK' if item['filesystem_discovery_ok'] else 'MISSING/CONFLICT'}; actual host activation UNVERIFIED")
            for p in item["candidates"]:
                if p["found"] or p.get("problem"):
                    print(" ", p["scope"], p["path"], p.get("problem", "present"))
            if not item["installed_on_disk"]:
                print("  Expected:", ", ".join(p["path"] for p in item["candidates"]))
    return int(args.strict and any(not r["filesystem_discovery_ok"] for r in result))

if __name__ == "__main__":
    raise SystemExit(main())
