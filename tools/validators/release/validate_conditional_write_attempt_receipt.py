"""Validate fixture-only conditional-write attempt receipt candidates."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
for candidate_path in (REPO_ROOT, REPO_ROOT / "packages/hashing/src"):
    if str(candidate_path) not in sys.path:
        sys.path.insert(0, str(candidate_path))

from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file
from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.release._conditional_write_attempt_receipt_model import (
    CASES_PATH,
    EXECUTION_MODE,
    INVALID_PATH,
    NON_EFFECTS,
    SCHEMA_PATH,
    SCOPE,
    VALID_PATH,
    Finding,
    ValidationResult,
    _attempt_fingerprint,
    _mapping,
    build_candidate,
    derive_result,
)
from tools.validators.release.validate_conditional_write_preflight import (
    validate_document as validate_preflight_document,
)

def _json_path(parts: Sequence[object]) -> str:
    value = "$"
    for part in parts:
        value += f"[{part}]" if isinstance(part, int) else "." + str(part)
    return value

def validate_document(candidate: object) -> ValidationResult:
    findings: set[Finding] = set()
    errors = sorted(
        load_validator(SCHEMA_PATH).iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    findings.update(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))) for error in errors)
    if errors or not isinstance(candidate, Mapping):
        return ValidationResult("DENY", tuple(sorted(findings)))

    preflight = _mapping(candidate["preflight_candidate"], "preflight_candidate")
    attempt = _mapping(candidate["attempt"], "attempt")
    upstream_result = validate_preflight_document(preflight)
    if upstream_result.outcome != "PASS":
        findings.add(Finding("PREFLIGHT_CANDIDATE_INVALID", "$.preflight_candidate"))

    try:
        expected_result = derive_result(preflight, attempt)
        expected_fingerprint = _attempt_fingerprint(preflight, attempt)
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        findings.add(Finding("SEMANTIC_INPUT_INVALID", "$"))
        expected_result = expected_fingerprint = None

    result = _mapping(candidate["result"], "result")
    if result["reason_codes"] != sorted(result["reason_codes"]):
        findings.add(Finding("REASON_CODE_ORDER_INVALID", "$.result.reason_codes"))
    if expected_result is not None and dict(result) != expected_result:
        findings.add(Finding("RESULT_DERIVATION_MISMATCH", "$.result"))
    if expected_fingerprint is not None and result["attempt_fingerprint"] != expected_fingerprint:
        findings.add(Finding("ATTEMPT_FINGERPRINT_MISMATCH", "$.result.attempt_fingerprint"))

    projection = {key: value for key, value in candidate.items() if key not in {"receipt_id", "spec_hash"}}
    try:
        expected_hash = compute_spec_hash(projection)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", tuple(sorted(findings)))
    expected_id = "kfm:conditional-write-attempt-receipt:" + expected_hash.removeprefix("sha256:")
    if candidate["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if candidate["receipt_id"] != expected_id:
        findings.add(Finding("RECEIPT_ID_MISMATCH", "$.receipt_id"))
    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)), expected_id)

def validate_file(path: Path) -> ValidationResult:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return ValidationResult("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    except (KeyError, TypeError, ValueError):
        return ValidationResult("ERROR", (Finding("INPUT_OR_DEPENDENCY_ERROR", "$"),))

def _cases() -> list[Mapping[str, Any]]:
    value = load_json_file(CASES_PATH)
    if not isinstance(value, Mapping) or not isinstance(value.get("cases"), list):
        raise ValueError("cases fixture is invalid")
    return [_mapping(case, "case") for case in value["cases"]]

def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    issues: list[dict[str, object]] = []
    cases = _cases()
    for case in cases:
        built = build_candidate(case)
        result = validate_document(built)
        expected = _mapping(case.get("expected"), "expected")
        actual = {
            "outcome": built["result"]["outcome"],
            "reason_codes": built["result"]["reason_codes"],
        }
        if result.outcome != "PASS":
            issues.append({"case_id": case.get("case_id"), "code": "BUILT_CASE_INVALID"})
        if actual != dict(expected):
            issues.append({"case_id": case.get("case_id"), "code": "CASE_EXPECTATION_MISMATCH"})
    if validate_file(VALID_PATH).outcome != "PASS":
        issues.append({"case_id": "valid_applied", "code": "VALID_FIXTURE_INVALID"})
    invalid = validate_file(INVALID_PATH)
    if invalid.outcome != "DENY" or not any(finding.code == "SCHEMA_INVALID" for finding in invalid.findings):
        issues.append({"case_id": "invalid_authority_overreach", "code": "INVALID_FIXTURE_POLARITY_MISMATCH"})
    payload = {
        "authority": "NONE",
        "cases": len(cases),
        "execution_mode": EXECUTION_MODE,
        "findings": issues,
        "non_effects": list(NON_EFFECTS),
        "outcome": "DENY" if issues else "PASS",
        "scope": SCOPE,
    }
    return not issues, payload

def _serialize(result: ValidationResult, path: Path | None = None) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "candidate": str(path) if path else None,
            "execution_mode": EXECUTION_MODE,
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "non_effects": list(NON_EFFECTS),
            "outcome": result.outcome,
            "receipt_id": result.receipt_id,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--build-case")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        try:
            ok, payload = run_fixture_suite()
        except Exception:
            ok, payload = False, {
                "authority": "NONE",
                "cases": 0,
                "execution_mode": EXECUTION_MODE,
                "findings": [{"code": "FIXTURE_SUITE_ERROR", "path": "$"}],
                "non_effects": list(NON_EFFECTS),
                "outcome": "ERROR",
                "scope": SCOPE,
            }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.build_case:
        matches = [case for case in _cases() if case.get("case_id") == args.build_case]
        if len(matches) != 1:
            parser.error("--build-case must name exactly one fixture case")
        rendered = json.dumps(build_candidate(matches[0]), indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
        return 0
    if args.candidate is None:
        parser.error("candidate is required unless --fixtures or --build-case is used")
    result = validate_file(args.candidate)
    print(_serialize(result, args.candidate))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]

if __name__ == "__main__":
    raise SystemExit(main())
