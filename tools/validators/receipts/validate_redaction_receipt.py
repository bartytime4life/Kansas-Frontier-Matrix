#!/usr/bin/env python3
"""Validate the fixture-only RedactionReceipt v1 machine profile."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/receipts/redaction_receipt.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/receipts/redaction_receipt/cases.json"
PREFIX = "kfm:redaction-receipt:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("REDACTION_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("REDACTION_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("REDACTION_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("REDACTION_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("REDACTION_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("REDACTION_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("REDACTION_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"receipt_id", "spec_hash"}}
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def recompute_result(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["processing_state"] == "ERROR":
        return {"status": "ERROR", "reason_codes": ["REDACTION_PROCESSING_ERROR"]}
    if "WITHHOLD" in value["transform"]["classes"]:
        return {"status": "WITHHELD", "reason_codes": ["CONTENT_WITHHELD"]}
    if value["processing_state"] == "HOLD":
        return {"status": "HOLD", "reason_codes": ["REDACTION_REVIEW_HOLD"]}
    return {"status": "RECORDED", "reason_codes": ["PUBLIC_SAFE_TRANSFORM_RECORDED"]}


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("REDACTION_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("REDACTION_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("REDACTION_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("REDACTION_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("REDACTION_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["receipt_id"] != expected_id:
            findings.add(Finding("REDACTION_ID_MISMATCH", "/receipt_id"))

    classes = set(value["transform"]["classes"])
    public_candidate = value["exposure"]["output_public_candidate"]
    output_digest = value["output_digest"]
    output_tier = value["exposure"]["output_sensitivity"]
    basis = value["basis"]
    release = value["release_context"]

    if "WITHHOLD" in classes:
        if output_digest is not None:
            findings.add(Finding("REDACTION_WITHHOLD_OUTPUT_FORBIDDEN", "/output_digest"))
        if public_candidate:
            findings.add(Finding("REDACTION_WITHHOLD_PUBLIC_FORBIDDEN", "/exposure/output_public_candidate"))
        if output_tier is not None:
            findings.add(Finding("REDACTION_WITHHOLD_TIER_FORBIDDEN", "/exposure/output_sensitivity"))
    elif value["processing_state"] == "COMPLETE" and output_digest is None:
        findings.add(Finding("REDACTION_OUTPUT_DIGEST_REQUIRED", "/output_digest"))

    if public_candidate:
        if output_tier not in {"T0", "T1"}:
            findings.add(Finding("REDACTION_PUBLIC_TIER_INVALID", "/exposure/output_sensitivity"))
        if basis["policy_decision_ref"] is None:
            findings.add(Finding("REDACTION_POLICY_REF_REQUIRED", "/basis/policy_decision_ref"))
        if basis["review_record_ref"] is None:
            findings.add(Finding("REDACTION_REVIEW_REF_REQUIRED", "/basis/review_record_ref"))
        if basis["validation_report_ref"] is None:
            findings.add(Finding("REDACTION_VALIDATION_REF_REQUIRED", "/basis/validation_report_ref"))
        if not basis["evidence_refs"]:
            findings.add(Finding("REDACTION_EVIDENCE_REQUIRED", "/basis/evidence_refs"))
        if release["release_candidate_ref"] is None:
            findings.add(Finding("REDACTION_RELEASE_CANDIDATE_REQUIRED", "/release_context/release_candidate_ref"))
        if release["rollback_ref"] is None:
            findings.add(Finding("REDACTION_ROLLBACK_REQUIRED", "/release_context/rollback_ref"))

    if value["result"] != recompute_result(value):
        findings.add(Finding("REDACTION_RESULT_MISMATCH", "/result"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    status = value["result"]["status"]
    if status in {"RECORDED", "WITHHELD"}:
        return Result("PASS", ())
    if status == "HOLD":
        return Result("ABSTAIN", (Finding("REDACTION_REVIEW_HOLD", "/result/status"),))
    return Result("ERROR", (Finding("REDACTION_PROCESSING_ERROR", "/result/status"),))


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["result"] = copy.deepcopy(case.get("result_override", recompute_result(document)))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["receipt_id"] = case.get("receipt_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    passed = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        print(json.dumps({"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "suite_match": match}, sort_keys=True, separators=(",", ":")))
        passed = passed and match
    return 0 if passed else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_restricted_input_open",
                "no_policy_execution",
                "no_authenticated_review",
                "no_lifecycle_mutation",
                "no_release",
                "no_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
