#!/usr/bin/env python3
"""Compare declared agent runs on the exact same inputs. NOT evidence authentication."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evals.score import grade_case, load_scenarios

FINGERPRINTS = ("repo_commit", "contract_sha256", "prompt_sha256", "skill_commit")

def compare(runs: list[dict]) -> dict:
    problems: list[str] = []
    if len(runs) < 2:
        problems.append("at least two agent runs required")
    agents = [r.get("agent") for r in runs]
    if any(not isinstance(a, str) or not a.strip() for a in agents) or len(set(agents)) != len(agents):
        problems.append("agent names must be unique and nonempty")
    for key in FINGERPRINTS:
        values = [r.get(key) for r in runs]
        if any(not isinstance(v, str) or not re.fullmatch(r"[a-fA-F0-9]{40,64}", v) for v in values):
            problems.append(f"{key}: missing or invalid fingerprint")
        if len(set(values)) > 1:
            problems.append(f"{key}: inputs differ between agents")
    sets = []
    for run in runs:
        cases = run.get("cases")
        if not isinstance(cases, list) or not cases or any(not isinstance(c, dict) or not c.get("id") for c in cases):
            problems.append(f"{run.get('agent')}: missing or invalid cases")
            cases = []
        ids = [c["id"] for c in cases]
        if len(ids) != len(set(ids)):
            problems.append(f"{run.get('agent')}: duplicate scenario")
        sets.append(set(ids))
    if sets and any(s != sets[0] for s in sets):
        problems.append("different scenarios evaluated")
    scenarios = {s["id"]: s for s in load_scenarios()}
    grades: dict[str, dict] = {}
    for run in runs:
        case_scores = {}
        for result in run.get("cases", []):
            case_id = result.get("id")
            if case_id not in scenarios:
                problems.append(f"{run.get('agent')}: unknown scenario {case_id}")
                continue
            status, reasons = grade_case(scenarios[case_id], result)
            case_scores[case_id] = {"status": status, "reasons": reasons}
        grades[str(run.get("agent"))] = case_scores
    statuses = [v["status"] for group in grades.values() for v in group.values()]
    verdict = "invalid" if problems else "fail" if "fail" in statuses else "inconclusive" if "inconclusive" in statuses else "pass"
    return {"status": verdict, "comparable": not problems, "problems": problems, "per_agent": grades,
            "limitation": "Self-reported records. Original agent transcripts, screenshots, code diffs and browser traces must be independently reviewed."}

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("results", nargs="+", type=Path)
    args = p.parse_args(argv)
    try:
        runs = [json.loads(path.read_text(encoding="utf-8")) for path in args.results]
        report = compare(runs)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return int(report["status"] != "pass")

if __name__ == "__main__":
    raise SystemExit(main())
