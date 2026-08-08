"""Closed fixture materialization and exact polarity replay."""
from __future__ import annotations

import copy
import json
from typing import Any, Mapping

from .model import CASES, SCOPE, Finding, ValidationResult, assign_identity, read_object
from .rules import validate_payload


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
        if part
    ]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = copy.deepcopy(value)


def _document() -> dict[str, Any]:
    document, findings = read_object(CASES)
    valid = (
        document is not None
        and not findings
        and document.get("profile")
        == "kfm.governance.published-language-review-fixtures.v1"
        and isinstance(document.get("bases"), dict)
        and isinstance(document.get("cases"), list)
    )
    if not valid:
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(
    document: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case["base"]
    if base_name not in bases or not isinstance(bases[base_name], Mapping):
        raise ValueError("unknown fixture base")
    candidate = copy.deepcopy(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["review_id"] = "published-language-review:" + "0" * 24
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _document()
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for case in document["cases"]:
        if (
            not isinstance(case, dict)
            or not isinstance(case.get("name"), str)
            or case["name"] in names
        ):
            raise ValueError("invalid fixture case")
        names.add(case["name"])
        result.append((case, materialize_case(document, case)))
    return result


def replay_fixtures() -> int:
    try:
        cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RecursionError):
        print(
            json.dumps(
                {
                    "outcome": "ERROR",
                    "findings": [
                        {"code": "FIXTURE_MANIFEST_INVALID", "path": "/"}
                    ],
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 1

    ok = True
    for definition, candidate in cases:
        result = validate_payload(candidate)
        expected = tuple(
            Finding(item["code"], item["path"])
            for item in definition.get("expected_findings", [])
        )
        matches = (
            result.outcome == definition.get("expected_outcome")
            and result.findings == expected
        )
        print(
            json.dumps(
                {
                    "case": definition["name"],
                    "outcome": result.outcome,
                    "findings": [
                        {"code": item.code, "path": item.path}
                        for item in result.findings
                    ],
                    "matches_expected": matches,
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        ok &= matches
    return 0 if ok else 1
