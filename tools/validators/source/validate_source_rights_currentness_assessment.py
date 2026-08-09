#!/usr/bin/env python3
"""Validate fixture-only SourceRightsCurrentnessAssessment records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/source_rights_currentness_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_rights_currentness_assessment/cases.json"
PREFIX = "kfm:source-rights-currentness:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
REASON_ORDER = (
    "PUBLISHER_IDENTITY_UNRESOLVED",
    "PRODUCT_IDENTITY_UNRESOLVED",
    "OFFICIAL_LOCATOR_UNRESOLVED",
    "TERMS_CURRENTNESS_UNRESOLVED",
    "RIGHTS_NOT_VERIFIED",
    "ATTRIBUTION_NOT_RESOLVED",
    "REDISTRIBUTION_NOT_VERIFIED",
    "DERIVATIVE_USE_NOT_VERIFIED",
    "ACCESS_POSTURE_UNRESOLVED",
    "CADENCE_NOT_DOCUMENTED",
)


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


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("RIGHTS_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("RIGHTS_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("RIGHTS_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("RIGHTS_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("RIGHTS_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("RIGHTS_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("RIGHTS_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def recompute_result(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return {"status": "ERROR", "reason_codes": ["ASSESSMENT_ERROR"]}

    checks = value["checks"]
    blocked: list[str] = []
    if checks["publisher_identity"] != "VERIFIED":
        blocked.append("PUBLISHER_IDENTITY_UNRESOLVED")
    if checks["product_identity"] != "VERIFIED":
        blocked.append("PRODUCT_IDENTITY_UNRESOLVED")
    if checks["official_locator"] != "VERIFIED":
        blocked.append("OFFICIAL_LOCATOR_UNRESOLVED")
    if checks["terms_currentness"] != "CURRENT":
        blocked.append("TERMS_CURRENTNESS_UNRESOLVED")
    if checks["rights_status"] in {"PERMISSION_REQUIRED", "UNKNOWN", "DENIED"}:
        blocked.append("RIGHTS_NOT_VERIFIED")
    if checks["attribution_status"] == "UNKNOWN":
        blocked.append("ATTRIBUTION_NOT_RESOLVED")
    if checks["redistribution_status"] in {"UNKNOWN", "DENIED"}:
        blocked.append("REDISTRIBUTION_NOT_VERIFIED")
    if checks["derivative_use_status"] in {"UNKNOWN", "DENIED"}:
        blocked.append("DERIVATIVE_USE_NOT_VERIFIED")
    if checks["access_status"] in {"UNAVAILABLE", "UNKNOWN"}:
        blocked.append("ACCESS_POSTURE_UNRESOLVED")
    if checks["cadence_status"] == "UNKNOWN":
        blocked.append("CADENCE_NOT_DOCUMENTED")

    if blocked:
        ordered = [code for code in REASON_ORDER if code in blocked]
        return {"status": "BLOCKED", "reason_codes": ordered}

    assessed = _time(value["assessed_at"])
    due = _time(value["review_due_at"])
    if assessed is None or due is None:
        return {"status": "ERROR", "reason_codes": ["ASSESSMENT_ERROR"]}
    if due <= assessed:
        return {"status": "REVIEW_DUE", "reason_codes": ["SOURCE_REVIEW_DUE"]}
    return {"status": "CURRENT", "reason_codes": ["SOURCE_RIGHTS_CURRENT"]}


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
        return (Finding("RIGHTS_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("RIGHTS_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("RIGHTS_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("RIGHTS_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("RIGHTS_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("RIGHTS_ID_MISMATCH", "/assessment_id"))
    if value["source_descriptor_ref"] != f"kfm://source/{value['source_id']}":
        findings.add(Finding("RIGHTS_SOURCE_REF_MISMATCH", "/source_descriptor_ref"))
    if value["result"] != recompute_result(value):
        findings.add(Finding("RIGHTS_RESULT_MISMATCH", "/result"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    status = value["result"]["status"]
    reasons = value["result"]["reason_codes"]
    if status == "CURRENT":
        return Result("PASS", ())
    if status == "REVIEW_DUE":
        return Result("ABSTAIN", (Finding(reasons[0], "/result/status"),))
    if status == "BLOCKED":
        return Result("DENY", tuple(Finding(code, "/result/status") for code in reasons))
    return Result("ERROR", (Finding("ASSESSMENT_ERROR", "/result/status"),))


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
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    passed = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": finding.code, "path": finding.path} for finding in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        print(
            json.dumps(
                {"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "suite_match": match},
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and match
    return 0 if passed else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "non_effects": [
                "no_network",
                "no_source_activation",
                "no_fetch",
                "no_raw_write",
                "no_promotion",
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
