#!/usr/bin/env python3
"""Validate UI_CONTRACT.json structure and provenance, not visual attractiveness."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

MODES = {"operate", "explore", "play", "create", "read", "persuade", "mixed"}
SOURCES = ("file:", "user:", "inference:")

def validate(data: object, root: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["contract must be a JSON object"]
    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")

    def obj(parent: dict, key: str, prefix: str = "") -> dict:
        value = parent.get(key)
        if not isinstance(value, dict):
            errors.append(f"{prefix}{key} must be an object")
            return {}
        return value

    def required(parent: dict, key: str, prefix: str) -> str:
        value = parent.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}.{key} must be a nonempty string")
            return ""
        return value.strip()

    def texts(value: object, field: str, nonempty: bool = False) -> None:
        if not isinstance(value, list) or (nonempty and not value) or any(not isinstance(x, str) or not x.strip() for x in value):
            errors.append(f"{field} must be a {'nonempty ' if nonempty else ''}list of strings")

    seen: list[str] = []
    def source(value: object, field: str) -> None:
        if not isinstance(value, str) or not any(value.startswith(prefix) and len(value) > len(prefix) for prefix in SOURCES):
            errors.append(f"{field} must specify file:, user:, or inference: provenance")
            return
        seen.append(value)
        if value.startswith("file:"):
            filename = value[5:]
            if filename.startswith(("/", "~")):
                errors.append(f"{field}: file source must be relative")
                return
            path = (root / filename).resolve()
            if not path.is_relative_to(root.resolve()):
                errors.append(f"{field}: source escapes project root")
            elif not path.is_file():
                errors.append(f"{field}: source does not exist: {filename}")

    product = obj(data, "product")
    for field in ("name", "primary_user", "primary_task"):
        required(product, field, "product")
    if product.get("mode") not in MODES:
        errors.append("product.mode is invalid")
    if "EXAMPLE ONLY" in str(product.get("name", "")):
        errors.append("replace illustrative example values before using this contract")
    front = obj(data, "frontend")
    required(front, "stack", "frontend")
    if front.get("choice") not in ("user-explicit", "existing-authorized"):
        errors.append("frontend.choice must be user-explicit or existing-authorized")

    direction = obj(data, "direction")
    if direction.get("status") not in ("approved", "provisional"):
        errors.append("direction.status must be approved or provisional")
    for field in ("dominant_subject", "composition", "density"):
        required(direction, field, "direction")
    source(direction.get("source"), "direction.source")
    texts(direction.get("visual_principles"), "direction.visual_principles", True)
    texts(direction.get("rejected_patterns", []), "direction.rejected_patterns")

    composition = obj(data, "composition")
    alternatives = composition.get("alternatives")
    if not isinstance(alternatives, list) or len(alternatives) < 2:
        errors.append("composition.alternatives must have at least two options")
        alternatives = []
    ids: list[str] = []
    descriptions: list[str] = []
    for i, option in enumerate(alternatives):
        if not isinstance(option, dict):
            errors.append(f"composition.alternatives[{i}] must be an object")
            continue
        ids.append(required(option, "id", f"composition.alternatives[{i}]"))
        descriptions.append(required(option, "description", f"composition.alternatives[{i}]").casefold())
    if len(ids) != len(set(ids)) or len(descriptions) != len(set(descriptions)):
        errors.append("composition alternatives cannot be duplicates")
    if composition.get("selected") not in ids:
        errors.append("composition.selected must name one alternative")
    required(composition, "reason", "composition")

    preservation = obj(data, "preserve")
    for field in ("routes", "components", "state", "permissions"):
        texts(preservation.get(field), f"preserve.{field}")
    evidence = data.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must include provenance-backed claims")
    else:
        for i, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append(f"evidence[{i}] must be an object")
                continue
            required(item, "claim", f"evidence[{i}]")
            source(item.get("source"), f"evidence[{i}].source")
    if direction.get("status") == "approved" and any(s.startswith("inference:") for s in seen):
        errors.append("approved contracts cannot rely on inferred evidence")
    return errors

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.contract.read_text(encoding="utf-8"))
        errors = validate(data, (args.project_root or args.contract.parent).resolve())
    except (OSError, json.JSONDecodeError) as exc:
        data = {}
        errors = [f"cannot read contract: {exc}"]
    status = data.get("direction", {}).get("status") if isinstance(data, dict) and isinstance(data.get("direction"), dict) else None
    if args.json:
        print(json.dumps({"valid": not errors, "status": status, "errors": errors}, indent=2))
    elif errors:
        for issue in errors:
            print("FAIL:", issue, file=sys.stderr)
    else:
        print("PASS: contract structure/provenance; rendered visual quality remains UNVERIFIED.", status)
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
