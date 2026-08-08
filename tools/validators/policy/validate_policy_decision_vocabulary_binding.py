#!/usr/bin/env python3
"""Validate PolicyDecision reason/obligation codes against an inactive vocabulary.

This validator checks declared bytes only. It does not evaluate policy, authenticate an
actor, authorize an operation, or mutate lifecycle/release/public state.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/policy/policy_decision.schema.json"
DEFAULT_VOCABULARY = REPO_ROOT / "policy/decision/vocabulary.v1.json"


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _finding(code: str, path: str, detail: str) -> dict[str, str]:
    return {"code": code, "path": path, "detail": detail}


def validate_binding(
    decision: dict[str, Any],
    vocabulary: dict[str, Any],
    schema: dict[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, str]] = []

    schema_errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(decision),
        key=lambda error: list(error.absolute_path),
    )
    if schema_errors:
        for error in schema_errors:
            pointer = "/" + "/".join(str(part) for part in error.absolute_path)
            findings.append(_finding("POLICY_DECISION_SCHEMA_INVALID", pointer or "/", error.message))
        return {"status": "ERROR", "findings": findings, "authority": _authority()}

    if vocabulary.get("object_type") != "PolicyDecisionVocabulary":
        findings.append(_finding("VOCABULARY_TYPE_INVALID", "/object_type", "unexpected vocabulary object_type"))
    if vocabulary.get("version") != "v1" or vocabulary.get("status") != "PROPOSED_INACTIVE":
        findings.append(
            _finding(
                "VOCABULARY_NOT_INACTIVE_V1",
                "/status",
                "binding v1 requires version v1 with status PROPOSED_INACTIVE",
            )
        )

    governance = vocabulary.get("governance")
    if not isinstance(governance, dict) or not governance or any(value is not False for value in governance.values()):
        findings.append(
            _finding(
                "VOCABULARY_AUTHORITY_OVERCLAIM",
                "/governance",
                "inactive vocabulary governance flags must all be false",
            )
        )

    reasons_raw = vocabulary.get("reason_codes")
    obligations_raw = vocabulary.get("obligation_codes")
    if not isinstance(reasons_raw, list) or not isinstance(obligations_raw, list):
        findings.append(_finding("VOCABULARY_SHAPE_INVALID", "/", "reason_codes and obligation_codes must be arrays"))
        return {"status": "ERROR", "findings": findings, "authority": _authority()}

    reasons_by_code: dict[str, dict[str, Any]] = {}
    for item in reasons_raw:
        if not isinstance(item, dict) or not isinstance(item.get("code"), str):
            findings.append(_finding("VOCABULARY_REASON_INVALID", "/reason_codes", "reason entry lacks string code"))
            continue
        code = item["code"]
        if code in reasons_by_code:
            findings.append(_finding("VOCABULARY_REASON_DUPLICATE", "/reason_codes", code))
        reasons_by_code[code] = item

    obligations_by_code: dict[str, dict[str, Any]] = {}
    for item in obligations_raw:
        if not isinstance(item, dict) or not isinstance(item.get("code"), str):
            findings.append(_finding("VOCABULARY_OBLIGATION_INVALID", "/obligation_codes", "obligation entry lacks string code"))
            continue
        code = item["code"]
        if code in obligations_by_code:
            findings.append(_finding("VOCABULARY_OBLIGATION_DUPLICATE", "/obligation_codes", code))
        obligations_by_code[code] = item

    outcome = decision["outcome"]
    family = decision["policy_family"]
    decision_reasons = decision["reasons"]
    decision_obligations = decision["obligations"]

    if decision_reasons != sorted(set(decision_reasons)):
        findings.append(_finding("REASONS_NOT_CANONICAL", "/reasons", "reason codes must be unique and sorted"))
    if decision_obligations != sorted(set(decision_obligations)):
        findings.append(_finding("OBLIGATIONS_NOT_CANONICAL", "/obligations", "obligation codes must be unique and sorted"))

    if outcome in {"ABSTAIN", "DENY", "ERROR"} and not decision_reasons:
        findings.append(_finding("REASON_REQUIRED", "/reasons", f"{outcome} requires at least one reason code"))

    if outcome != "ANSWER" and decision_obligations:
        findings.append(
            _finding(
                "OBLIGATION_OUTCOME_INVALID",
                "/obligations",
                "v1 obligations apply only to ANSWER",
            )
        )

    for index, code in enumerate(decision_reasons):
        entry = reasons_by_code.get(code)
        if entry is None:
            findings.append(_finding("REASON_CODE_UNKNOWN", f"/reasons/{index}", code))
            continue
        if entry.get("outcome") != outcome:
            findings.append(
                _finding(
                    "REASON_OUTCOME_MISMATCH",
                    f"/reasons/{index}",
                    f"{code} is registered for {entry.get('outcome')}, not {outcome}",
                )
            )
        families = entry.get("policy_families")
        if not isinstance(families, list) or family not in families:
            findings.append(
                _finding(
                    "REASON_POLICY_FAMILY_MISMATCH",
                    f"/reasons/{index}",
                    f"{code} is not registered for {family}",
                )
            )

    for index, code in enumerate(decision_obligations):
        entry = obligations_by_code.get(code)
        if entry is None:
            findings.append(_finding("OBLIGATION_CODE_UNKNOWN", f"/obligations/{index}", code))
            continue
        applicable = entry.get("applicable_outcomes")
        families = entry.get("policy_families")
        if not isinstance(applicable, list) or outcome not in applicable:
            findings.append(
                _finding(
                    "OBLIGATION_OUTCOME_MISMATCH",
                    f"/obligations/{index}",
                    f"{code} is not registered for {outcome}",
                )
            )
        if not isinstance(families, list) or family not in families:
            findings.append(
                _finding(
                    "OBLIGATION_POLICY_FAMILY_MISMATCH",
                    f"/obligations/{index}",
                    f"{code} is not registered for {family}",
                )
            )

    if outcome == "ANSWER" and "OPERATION_ALLOWED_WITH_OBLIGATIONS" in decision_reasons and not decision_obligations:
        findings.append(
            _finding(
                "ANSWER_OBLIGATION_REQUIRED",
                "/obligations",
                "OPERATION_ALLOWED_WITH_OBLIGATIONS requires at least one registered obligation",
            )
        )

    status = "DENY" if findings else "PASS"
    return {"status": status, "findings": findings, "authority": _authority()}


def _authority() -> dict[str, bool]:
    return {
        "policy_evaluated": False,
        "decision_emitted": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "publication_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decision", type=Path)
    parser.add_argument("--vocabulary", type=Path, default=DEFAULT_VOCABULARY)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    try:
        decision = _load_json(args.decision)
        vocabulary = _load_json(args.vocabulary)
        schema = _load_json(args.schema)
    except (OSError, json.JSONDecodeError) as exc:
        result = {
            "status": "ERROR",
            "findings": [_finding("INPUT_READ_ERROR", "/", str(exc))],
            "authority": _authority(),
        }
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 2

    if not isinstance(decision, dict) or not isinstance(vocabulary, dict) or not isinstance(schema, dict):
        result = {
            "status": "ERROR",
            "findings": [_finding("INPUT_SHAPE_ERROR", "/", "decision, vocabulary, and schema must be objects")],
            "authority": _authority(),
        }
    else:
        result = validate_binding(decision, vocabulary, schema)

    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["status"] == "PASS" else 2 if result["status"] == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())
