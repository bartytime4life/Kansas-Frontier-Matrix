"""Validate fixture-only optimistic conditional-write preflight candidates.

No target is contacted, no request is emitted, and no write, lifecycle, policy,
review, promotion, release, publication, or public-use authority is created.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file
from tools.validators.release._conditional_write_preflight_model import (
    CASES_PATH,
    EXECUTION_MODE,
    INVALID_PATH,
    NON_EFFECTS,
    SCOPE,
    VALID_PATH,
    Finding,
    ValidationResult,
    _derive,
    _keys,
    _m,
    _path,
    _validator,
    build_candidate,
)


def validate_document(candidate: object) -> ValidationResult:
    findings: set[Finding] = set()
    errors = sorted(
        _validator().iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    findings.update(
        Finding("SCHEMA_INVALID", _path(tuple(error.absolute_path))) for error in errors
    )
    if errors or not isinstance(candidate, Mapping):
        return ValidationResult("DENY", tuple(sorted(findings)))

    target = _m(candidate["target"], "target")
    request = _m(candidate["request"], "request")
    upstream = _m(candidate["upstream"], "upstream")
    try:
        expected_preflight = _derive(target, request, upstream)
        expected_idempotency = _keys(target, request)[0]
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        findings.add(Finding("SEMANTIC_INPUT_INVALID", "$"))
        expected_preflight = expected_idempotency = None

    if expected_preflight is not None and dict(candidate["preflight"]) != expected_preflight:
        findings.add(Finding("PREFLIGHT_DERIVATION_MISMATCH", "$.preflight"))
    if expected_idempotency is not None and request["idempotency_key"] != expected_idempotency:
        findings.add(Finding("IDEMPOTENCY_KEY_MISMATCH", "$.request.idempotency_key"))

    projection = {
        key: value for key, value in candidate.items() if key not in {"intent_id", "spec_hash"}
    }
    try:
        expected_hash = compute_spec_hash(projection)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", tuple(sorted(findings)))

    expected_id = "kfm:conditional-write-intent:" + expected_hash.removeprefix("sha256:")
    if candidate["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if candidate["intent_id"] != expected_id:
        findings.add(Finding("INTENT_ID_MISMATCH", "$.intent_id"))
    return ValidationResult(
        "DENY" if findings else "PASS", tuple(sorted(findings)), expected_id
    )


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
    return [_m(case, "case") for case in value["cases"]]


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    issues: list[dict[str, object]] = []
    cases = _cases()
    for case in cases:
        built = build_candidate(case)
        result = validate_document(built)
        actual = {
            "outcome": built["preflight"]["outcome"],
            "reason_codes": built["preflight"]["reason_codes"],
        }
        if result.outcome != "PASS":
            issues.append({"case_id": case.get("case_id"), "code": "BUILT_CASE_INVALID"})
        if actual != dict(_m(case.get("expected"), "expected")):
            issues.append({"case_id": case.get("case_id"), "code": "CASE_EXPECTATION_MISMATCH"})

    if validate_file(VALID_PATH).outcome != "PASS":
        issues.append({"case_id": "valid_propose_write", "code": "VALID_FIXTURE_INVALID"})
    invalid = validate_file(INVALID_PATH)
    if invalid.outcome != "DENY" or not any(
        finding.code == "SCHEMA_INVALID" for finding in invalid.findings
    ):
        issues.append(
            {
                "case_id": "invalid_authority_overreach",
                "code": "INVALID_FIXTURE_POLARITY_MISMATCH",
            }
        )

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
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "intent_id": result.intent_id,
            "non_effects": list(NON_EFFECTS),
            "outcome": result.outcome,
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
