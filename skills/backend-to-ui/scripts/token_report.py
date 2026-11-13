#!/usr/bin/env python3
"""Estimate skill file budgets; optionally extract exact whole-run AGY usage.

Estimates are NOT model-billed tokens. No agent calls, file modification, or network.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def estimate(text: str) -> int:
    """Simple, clearly labeled heuristic; tokenizer-dependent and approximate."""
    return round(len(text) / 4)


def file_report(skill_dir: Path) -> dict:
    if not (skill_dir / "SKILL.md").is_file():
        raise FileNotFoundError(f"Skill not found at {skill_dir}")
    core = skill_dir / "SKILL.md"
    refs = sorted((skill_dir / "references").glob("*.md"))
    supporting = sorted(
        p for sub in ("assets", "scripts") for p in (skill_dir / sub).rglob("*")
        if p.is_file() and p.suffix in (".json", ".py", ".md")
    )

    def size(paths: list[Path]) -> dict:
        n = sum(len(p.read_text(encoding="utf-8")) for p in paths)
        return {"files": len(paths), "characters": n, "estimated_tokens_chars_div_4": estimate("x" * n)}

    report = {
        "measurement": "estimated_static_text_only",
        "warning": "Character/4 is NOT a model tokenizer, context trace, or billed AGY usage. Files are read only if the agent loads them.",
        "core": size([core]),
        "references": size(refs),
        "scripts_assets": size(supporting),
        "core_plus_all_references": size([core, *refs]),
        "all_skill_text": size([core, *refs, *supporting]),
        "reference_breakdown": [
            {"file": str(p.relative_to(skill_dir)), "characters": len(p.read_text(encoding="utf-8")),
             "estimated_tokens_chars_div_4": estimate(p.read_text(encoding="utf-8"))}
            for p in refs
        ],
    }
    return report


def usage_from_agy(content: str) -> dict:
    """Read only the final usage object; never reproduce prompts or tool output."""
    try:
        records = [json.loads(content)]
    except json.JSONDecodeError:
        records = [json.loads(line) for line in content.splitlines() if line.strip()]
    results = [r for r in records if isinstance(r, dict)
               and (r.get("event") == "result" or "usage" in r)]
    if not results:
        raise ValueError("No terminal AGY result/usage object in file")
    terminal = results[-1]
    payload = terminal.get("result", terminal)
    usage = payload.get("usage") if isinstance(payload, dict) else None
    if not isinstance(usage, dict):
        raise ValueError("Terminal result has no usage object")
    keys = ("input_tokens", "output_tokens", "thinking_tokens",
            "cache_read_tokens", "total_tokens")
    if not all(isinstance(usage.get(k), int) and usage[k] >= 0 for k in keys):
        raise ValueError("AGY usage fields are missing or invalid")
    return {
        "measurement": "AGY_terminal_session_usage",
        "warning": "Whole AGY run, including prompts, built-in tools, loaded skills, cache and reasoning. NOT an isolated backend-to-ui token cost.",
        "usage": {k: usage[k] for k in keys},
        "status": payload.get("status"),
        "duration_seconds": payload.get("duration_seconds"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--usage-json", type=Path, help="Optional local AGY --output-format json or stream-json file")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = file_report(args.skill_dir)
        if args.usage_json:
            report["agy_actual_usage"] = usage_from_agy(args.usage_json.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
        return 0
    print("STATIC SKILL TEXT ESTIMATE (characters / 4; NOT actual billed tokens)")
    for key in ("core", "references", "scripts_assets", "core_plus_all_references", "all_skill_text"):
        item = report[key]
        print(f"  {key:25} {item['files']:2} files | {item['characters']:7} chars | ~{item['estimated_tokens_chars_div_4']:6} tokens")
    if args.usage_json:
        u = report["agy_actual_usage"]
        print("AGY REPORTED SESSION USAGE (actual run, NOT skill-only)")
        print(" ", u["usage"])
    print("For per-skill loaded-token counts in interactive AGY, use /context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
