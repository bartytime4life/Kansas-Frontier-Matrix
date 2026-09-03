#!/usr/bin/env python3
"""Validate the inert repository-topology correction register shape.

Stage-1 boundary: this validator validates only the register's machine shape and
internal exact-transition invariants. It does not consume entries to authorize
repository-topology baseline transitions.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_REGISTER = ROOT / "control_plane/repository_topology_correction_register.yaml"
DEFAULT_SCHEMA = ROOT / "schemas/contracts/v1/governance/repository_topology_correction_register.schema.json"

PASS = "PASS"
FAIL_INVALID = "FAIL_INVALID"


def _load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("register root must be a mapping")
    return value


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("schema root must be an object")
    return value


def validate(register_path: Path = DEFAULT_REGISTER, schema_path: Path = DEFAULT_SCHEMA) -> list[str]:
    errors: list[str] = []
    try:
        register = _load_yaml(register_path)
        schema = _load_json(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        for error in sorted(validator.iter_errors(register), key=lambda item: list(item.absolute_path)):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"schema:{location}:{error.message}")
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError, jsonschema.SchemaError) as exc:
        return [f"load:{exc}"]

    entries = register.get("entries", [])
    ids: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        correction_id = entry.get("correction_id")
        if correction_id in ids:
            errors.append(f"entry[{index}]:duplicate correction_id:{correction_id}")
        if isinstance(correction_id, str):
            ids.add(correction_id)

        from_state = entry.get("from", {})
        to_state = entry.get("to", {})
        delta = entry.get("exact_delta", {})
        if isinstance(from_state, dict) and isinstance(to_state, dict) and isinstance(delta, dict):
            old_count = from_state.get("member_count")
            new_count = to_state.get("member_count")
            unchanged = delta.get("unchanged_member_count")
            if isinstance(old_count, int) and isinstance(new_count, int) and isinstance(unchanged, int):
                if old_count != new_count:
                    errors.append(f"entry[{index}]:correction branch requires equal member counts")
                if unchanged != old_count - 1:
                    errors.append(f"entry[{index}]:unchanged_member_count must equal member_count - 1")

        status = entry.get("status")
        decision_ref = entry.get("decision_ref", {})
        if status == "accepted" and isinstance(decision_ref, dict):
            if not decision_ref.get("blob") or not decision_ref.get("accepted_commit"):
                errors.append(f"entry[{index}]:accepted entry requires exact decision blob and accepted commit")

    return sorted(set(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args(argv)

    errors = validate(args.register, args.schema)
    if errors:
        print(FAIL_INVALID)
        for error in errors:
            print(error)
        return 1

    print(PASS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
