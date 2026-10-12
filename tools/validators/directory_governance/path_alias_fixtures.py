"""Reviewed positive/negative fixture execution for path aliases."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence

from .path_alias_io import read_object
from .path_alias_model import FIXTURE_ROOT


def set_path(candidate: dict[str, Any], path: Sequence[Any], value: Any) -> None:
    current: Any = candidate
    for part in path[:-1]:
        current = current[part]
    current[path[-1]] = value


def invalid_cases() -> list[dict[str, Any]]:
    payload = json.loads((FIXTURE_ROOT / "invalid" / "cases.json").read_text(encoding="utf-8"))
    cases = payload.get("cases") if isinstance(payload, dict) else None
    return cases if isinstance(cases, list) else []


def run_fixture_profile(validate_register, serialize) -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
    try:
        cases = invalid_cases()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return 2
    if len(valid) != 1 or not cases:
        return 2
    base_candidate, findings = read_object(valid[0])
    if base_candidate is None or findings:
        return 2
    result = validate_register(valid[0], check_repository=False, enforce_projection_binding=False)
    print(serialize(valid[0], result))
    passed = result.ok
    for case in cases:
        if not isinstance(case, Mapping):
            return 2
        candidate = copy.deepcopy(base_candidate)
        operations = case.get("operations")
        if not isinstance(operations, list):
            operations = [{"path": case.get("path"), "value": case.get("value")}]
        try:
            for operation in operations:
                if not isinstance(operation, Mapping) or not isinstance(operation.get("path"), list):
                    return 2
                set_path(candidate, operation["path"], operation.get("value"))
        except (KeyError, IndexError, TypeError):
            return 2
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / f"{case.get('name', 'invalid')}.yaml"
            path.write_text(json.dumps(candidate, sort_keys=True), encoding="utf-8")
            result = validate_register(path, check_repository=False, enforce_projection_binding=False)
        print(serialize(Path(str(case.get("name", "invalid")) + ".yaml"), result))
        expected = sorted(case.get("expected_codes", []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": str(case.get("name", "invalid")),
                        "expected_codes": expected,
                        "actual_codes": actual,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1
