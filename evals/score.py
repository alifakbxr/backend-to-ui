#!/usr/bin/env python3
"""Evaluate recorded coding-agent runs against backend-to-ui scenarios.

This tool checks supplied evidence records, NOT the truth of an agent's claims.
Reviewers must inspect original transcripts, diffs, screenshots and metrics.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evals" / "scenarios.json"


def load_scenarios(path: Path = SCENARIOS) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("Unsupported scenario schema")
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, list):
        raise ValueError("scenarios must be an array")
    ids = [case.get("id") for case in scenarios]
    if len(ids) != len(set(ids)) or any(not ident for ident in ids):
        raise ValueError("Scenario IDs must be nonempty and unique")
    for case in scenarios:
        check = policy_decision(case["input"])
        if case["expected"]["action"] != check:
            raise ValueError(f"{case['id']}: expected action conflicts with policy ({check})")
    return scenarios


def policy_decision(request: dict) -> str:
    """Reference decision table for policy scenarios, not an LLM simulator."""
    if request.get("audit_only"):
        return "audit"
    if request.get("conflict"):
        return "ask_stack"
    if request.get("frontend_choice"):
        return "implement"
    if request.get("reuse_existing") and request.get("existing_frontend") not in (None, "", "mixed"):
        return "implement"
    return "ask_stack"


def grade_case(scenario: dict, run: dict) -> tuple[str, list[str]]:
    """Return pass/fail/inconclusive from a *declared* evidence record."""
    expected = scenario["expected"]
    errors: list[str] = []
    unknown: list[str] = []
    action = expected["action"]
    if run.get("action") != action:
        errors.append(f"expected action {action!r}, got {run.get('action')!r}")
    changed = run.get("files_changed", [])
    if not isinstance(changed, list):
        errors.append("files_changed must be a list")
        changed = []
    if action in ("ask_stack", "audit") and changed:
        errors.append("read-only/ask response changed implementation files")
    if action == "ask_stack":
        message = str(run.get("message", ""))
        if "?" not in message or not re.search(r"stack|framework|frontend|vue|react|svelte|html|flutter|compatible|incompatible", message, re.I):
            errors.append("missing a direct frontend stack or conflict question")
    if action == "implement":
        target = expected.get("stack")
        if target and str(run.get("stack", "")).casefold() != str(target).casefold():
            errors.append(f"expected selected stack {target!r}")
        if not changed:
            errors.append("no implementation file changes recorded")
    if action == "audit" and not run.get("message"):
        errors.append("read-only audit lacks a report")

    evidence = run.get("evidence") or {}
    if not isinstance(evidence, dict):
        errors.append("evidence must be an object")
        evidence = {}
    checks = evidence.get("checks") or {}
    for gate in expected.get("gates", []):
        if gate in ("stack", "conflict"):
            continue
        if gate == "backend":
            if not evidence.get("contracts"):
                unknown.append("no backend operation/field mapping evidence")
        elif gate == "interaction":
            result = checks.get("interaction") or {}
            if result.get("status") != "pass" or not result.get("cases"):
                unknown.append("no executed interaction test evidence")
        elif gate == "visual":
            result = checks.get("visual") or {}
            shots = result.get("screenshots") or {}
            if result.get("status") != "pass" or not (shots.get("desktop") and shots.get("mobile")):
                unknown.append("no desktop + mobile screenshot evidence")
        elif gate == "performance":
            result = checks.get("performance") or {}
            metrics = result.get("measurements") or {}
            if result.get("status") != "pass" or not (
                isinstance(metrics.get("request_count"), (int, float))
                and isinstance(metrics.get("render_duration_ms"), (int, float))
                and metrics["request_count"] >= 0
                and metrics["render_duration_ms"] >= 0
            ):
                unknown.append("no measured network + render evidence")
        else:
            errors.append(f"unknown gate {gate!r}")
    if errors:
        return "fail", errors + unknown
    if unknown:
        return "inconclusive", unknown
    return "pass", []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True, help="JSON evidence recorded from an actual agent run")
    parser.add_argument("--allow-partial", action="store_true", help="Evaluate only recorded scenarios")
    args = parser.parse_args(argv)
    try:
        scenarios = load_scenarios()
        record = json.loads(args.results.read_text(encoding="utf-8"))
        runs = record["cases"]
        if not isinstance(runs, list) or len(runs) != len({r["id"] for r in runs}):
            raise ValueError("Case records must be a list with unique IDs")
        by_id = {r["id"]: r for r in runs}
        known_ids = {s["id"] for s in scenarios}
        extra = set(by_id) - known_ids
        if extra:
            raise ValueError(f"Unknown scenario IDs: {sorted(extra)}")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    counts = {"pass": 0, "fail": 0, "inconclusive": 0, "not_run": 0}
    for scenario in scenarios:
        ident = scenario["id"]
        if ident not in by_id:
            counts["not_run"] += 1
            if not args.allow_partial:
                print(f"NOT_RUN {ident}")
            continue
        outcome, reasons = grade_case(scenario, by_id[ident])
        counts[outcome] += 1
        print(f"{outcome.upper():12s} {ident}" + (": " + "; ".join(reasons) if reasons else ""))
    print(f"SUMMARY agent={record.get('agent', 'unknown')} " + " ".join(f"{k}={v}" for k, v in counts.items()))
    if counts["fail"] or counts["inconclusive"] or (counts["not_run"] and not args.allow_partial):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
