#!/usr/bin/env python3
"""Validate the fixture-only RuntimeResponseEnvelope HTTP binding profile v1."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/runtime/runtime_response_http_binding_v1.schema.json"

EXPECTED = {
    200: ("ANSWER", "NONE"),
    403: ("DENY", "POLICY_OR_GOVERNANCE_DENIAL"),
    422: ("ABSTAIN", "INSUFFICIENT_EVIDENCE_OR_CONTEXT"),
    500: ("ERROR", "INTERNAL_RUNTIME_FAILURE"),
    503: ("ERROR", "DEPENDENCY_UNAVAILABLE"),
}


def _authority() -> dict[str, bool]:
    return {
        "http_status_is_authority": False,
        "policy_evaluated": False,
        "lifecycle_write_authorized": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "publication_authorized": False,
    }


def validate_payload(value: Any) -> dict[str, Any]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: list(e.absolute_path))
    findings: list[dict[str, str]] = []
    if errors:
        for error in errors:
            path = "/" + "/".join(str(part) for part in error.absolute_path)
            findings.append({"code": "SCHEMA_INVALID", "path": path or "/"})
        return {"status": "ERROR", "findings": findings, "authority": _authority()}

    assert isinstance(value, dict)
    status = value["http_status"]
    expected_outcome, expected_failure = EXPECTED[status]
    if value["outcome"] != expected_outcome:
        findings.append({"code": "HTTP_OUTCOME_MISMATCH", "path": "/outcome"})
    if value["failure_class"] != expected_failure:
        findings.append({"code": "HTTP_FAILURE_CLASS_MISMATCH", "path": "/failure_class"})
    if value["governance"] != _authority():
        findings.append({"code": "AUTHORITY_OVERCLAIM", "path": "/governance"})

    return {
        "status": "DENY" if findings else "PASS",
        "findings": findings,
        "authority": _authority(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        value = json.loads(args.record.read_text(encoding="utf-8"))
        result = validate_payload(value)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        result = {
            "status": "ERROR",
            "findings": [{"code": "INPUT_READ_ERROR", "path": "/"}],
            "authority": _authority(),
        }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["status"] == "PASS" else 2 if result["status"] == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())
