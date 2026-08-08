#!/usr/bin/env python3
"""Validate the inactive explicit PolicyInputBundle profile v1."""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json"
SCOPE = "policy-input-bundle-profile-v1-fixture-only"
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED", "JSON_INVALID", "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(item.code in ERROR_CODES for item in self.findings)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _nonfinite(_value: str) -> object:
    raise NonFiniteError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        raw = path.read_bytes()
        if len(raw) > 1_048_576:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
            for error in sorted(
                validator.iter_errors(candidate),
                key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
            )
        ]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    evidence = _mapping(candidate.get("evidence"))
    source = _mapping(candidate.get("source"))
    sensitivity = _mapping(candidate.get("sensitivity"))
    review = _mapping(candidate.get("review"))
    release = _mapping(candidate.get("release"))
    rights = _mapping(candidate.get("rights"))

    canonical_fields = (
        (evidence.get("evidence_refs"), "/evidence/evidence_refs"),
        (source.get("source_descriptor_refs"), "/source/source_descriptor_refs"),
        (source.get("source_roles"), "/source/source_roles"),
        (sensitivity.get("transform_refs"), "/sensitivity/transform_refs"),
        (review.get("review_refs"), "/review/review_refs"),
    )
    for value, field in canonical_fields:
        if not _canonical_strings(value):
            findings.append(Finding("REFERENCES_NOT_CANONICAL", field))

    operation = candidate.get("operation")
    if operation in {"ANSWER", "RENDER", "EXPORT"}:
        if evidence.get("resolution_status") != "RESOLVED":
            findings.append(Finding("EVIDENCE_NOT_RESOLVED", "/evidence/resolution_status"))
        if evidence.get("citation_validation") != "PASS":
            findings.append(Finding("CITATION_VALIDATION_REQUIRED", "/evidence/citation_validation"))

    if rights.get("status") == "UNKNOWN":
        findings.append(Finding("RIGHTS_UNRESOLVED", "/rights/status"))
    if sensitivity.get("status") == "UNKNOWN":
        findings.append(Finding("SENSITIVITY_UNRESOLVED", "/sensitivity/status"))

    if candidate.get("audience") == "PUBLIC":
        if rights.get("status") != "CLEAR":
            findings.append(Finding("PUBLIC_RIGHTS_NOT_CLEAR", "/rights/status"))
        if sensitivity.get("status") not in {"PUBLIC", "GENERALIZED"}:
            findings.append(Finding("PUBLIC_SENSITIVITY_UNSAFE", "/sensitivity/status"))
        if sensitivity.get("exact_location") is True and sensitivity.get("status") != "PUBLIC":
            findings.append(Finding("PUBLIC_EXACT_LOCATION_DENIED", "/sensitivity/exact_location"))
        if review.get("state") not in {"APPROVED", "NOT_REQUIRED"}:
            findings.append(Finding("PUBLIC_REVIEW_INCOMPLETE", "/review/state"))

    if operation in {"PROMOTE", "RELEASE"}:
        if review.get("state") != "APPROVED":
            findings.append(Finding("PROMOTION_REVIEW_REQUIRED", "/review/state"))
        if release.get("state") != "CANDIDATE":
            findings.append(Finding("RELEASE_CANDIDATE_STATE_REQUIRED", "/release/state"))
        if not isinstance(release.get("rollback_ref"), str):
            findings.append(Finding("ROLLBACK_REFERENCE_REQUIRED", "/release/rollback_ref"))
    if operation == "RELEASE" and not isinstance(release.get("release_manifest_ref"), str):
        findings.append(Finding("RELEASE_MANIFEST_REQUIRED", "/release/release_manifest_ref"))

    governance = _mapping(candidate.get("governance"))
    if any(value is not False for value in governance.values()):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_payload(candidate).findings)
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": outcome,
            "scope": SCOPE,
            "authority": {
                "policy_evaluation": False,
                "decision_emitted": False,
                "hidden_fetch": False,
                "lifecycle_write": False,
                "promotion": False,
                "release": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="+", type=Path)
    args = parser.parse_args(argv)
    ok = True
    for path in args.records:
        result = validate_record(path)
        print(serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
