#!/usr/bin/env python3
"""Validate proposed SourceRecordAbsenceAssessment records without network access.

A passing result proves bounded source-mode, chronology, deterministic-identity,
and fail-closed absence semantics only. It does not delete history, clear an
advisory or event, mutate source state, resolve evidence, evaluate policy,
promote, release, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_record_absence_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_record_absence_assessment"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source-record-absence-mode-chronology-and-false-clear-prevention-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
        return any(
            item.code.startswith(
                ("FILE_", "JSON_", "INPUT_", "ROOT_", "SCHEMA_UNAVAILABLE")
            )
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise NonFiniteNumberError
    return result


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    return "sha256:" + hashlib.sha256(_canonical_json(projected)).hexdigest()


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any] | None:
    source = _mapping(candidate.get("source"))
    record = _mapping(candidate.get("record"))
    timing = _mapping(candidate.get("timing"))
    values = {
        "source_descriptor_ref": source.get("source_descriptor_ref"),
        "source_mode": source.get("mode"),
        "record_key_hash": record.get("record_key_hash"),
        "prior_snapshot_ref": record.get("prior_snapshot_ref"),
        "current_snapshot_ref": record.get("current_snapshot_ref"),
        "current_captured_at": timing.get("current_captured_at"),
    }
    if not all(isinstance(value, str) for value in values.values()):
        return None
    return values


def canonical_assessment_id(candidate: Mapping[str, Any]) -> str | None:
    projection = _identity_projection(candidate)
    if projection is None:
        return None
    digest = hashlib.sha256(_canonical_json(projection)).hexdigest()
    return "urn:kfm:source-record-absence:sha256:" + digest


def _parse_aware(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def _canonical_string_array(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _expected_decision(candidate: Mapping[str, Any]) -> tuple[str, tuple[str, ...], bool, bool]:
    source = _mapping(candidate.get("source"))
    mode = source.get("mode")
    health = source.get("health")
    completeness = source.get("completeness_verified") is True
    parse_status = source.get("parse_status")

    if health == "ERROR" or parse_status == "FAILED":
        return "ERROR", ("SOURCE_OR_PARSE_ERROR",), True, False

    if mode == "COMPLETE_AUTHORITATIVE_SNAPSHOT":
        verified = health == "HEALTHY" and completeness and parse_status == "COMPLETE"
        if verified:
            return (
                "REMOVAL_CANDIDATE",
                ("ABSENT_FROM_VERIFIED_COMPLETE_SNAPSHOT",),
                False,
                True,
            )
        reasons: list[str] = []
        if not completeness:
            reasons.append("SNAPSHOT_COMPLETENESS_UNVERIFIED")
        if health == "UNKNOWN":
            reasons.append("SOURCE_HEALTH_UNRESOLVED")
        elif health == "DEGRADED":
            reasons.append("SOURCE_HEALTH_DEGRADED")
        if parse_status != "COMPLETE":
            reasons.append("PARSE_INCOMPLETE")
        if not reasons:
            reasons.append("SOURCE_HEALTH_UNRESOLVED")
        return "ABSTAIN", tuple(sorted(set(reasons))), True, False

    if mode == "INCREMENTAL_EVENT_FEED":
        return "RETAIN_PRIOR_STATE", ("ABSENCE_NOT_STATE_TRANSITION",), True, False
    if mode == "PUBLICATION_PAGE":
        return "ABSTAIN", ("LAYOUT_OR_PARSE_DRIFT_POSSIBLE",), True, False
    if mode == "MIXED_SURFACE":
        return "ABSTAIN", ("CROSS_SURFACE_RECONCILIATION_REQUIRED",), True, False
    return "ERROR", ("SOURCE_OR_PARSE_ERROR",), True, False


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    supplied_hash = candidate.get("spec_hash")
    if isinstance(supplied_hash, str) and supplied_hash != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    expected_id = canonical_assessment_id(candidate)
    supplied_id = candidate.get("assessment_id")
    if expected_id is not None and isinstance(supplied_id, str) and supplied_id != expected_id:
        findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    timing = _mapping(candidate.get("timing"))
    prior_time = _parse_aware(timing.get("prior_captured_at"))
    current_time = _parse_aware(timing.get("current_captured_at"))
    assessed_time = _parse_aware(timing.get("assessed_at"))
    if (
        prior_time is not None
        and current_time is not None
        and assessed_time is not None
        and not (prior_time <= current_time <= assessed_time)
    ):
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/timing"))

    decision = _mapping(candidate.get("decision"))
    provenance = _mapping(candidate.get("provenance"))
    for field, value in (
        ("/decision/reason_codes", decision.get("reason_codes")),
        ("/provenance/input_refs", provenance.get("input_refs")),
        ("/provenance/evidence_refs", provenance.get("evidence_refs")),
    ):
        if isinstance(value, list) and not _canonical_string_array(value):
            findings.append(Finding("REFERENCE_ARRAY_NOT_CANONICAL", field))

    expected_outcome, expected_reasons, expected_retain, transition_required = _expected_decision(candidate)
    actual_outcome = decision.get("outcome")
    actual_reasons = tuple(decision.get("reason_codes", ())) if isinstance(decision.get("reason_codes"), list) else ()
    if actual_outcome != expected_outcome:
        findings.append(Finding("SOURCE_MODE_OUTCOME_MISMATCH", "/decision/outcome"))
    if actual_reasons != expected_reasons:
        findings.append(Finding("REASON_CODES_MISMATCH", "/decision/reason_codes"))
    if decision.get("retain_prior_state") is not expected_retain:
        findings.append(Finding("PRIOR_STATE_RETENTION_MISMATCH", "/decision/retain_prior_state"))

    transition = decision.get("transition_candidate_ref")
    transition_valid = isinstance(transition, str) if transition_required else transition is None
    if not transition_valid:
        findings.append(Finding("TRANSITION_CANDIDATE_MISMATCH", "/decision/transition_candidate_ref"))

    source = _mapping(candidate.get("source"))
    verified_complete = (
        source.get("mode") == "COMPLETE_AUTHORITATIVE_SNAPSHOT"
        and source.get("health") == "HEALTHY"
        and source.get("completeness_verified") is True
        and source.get("parse_status") == "COMPLETE"
    )
    if actual_outcome == "REMOVAL_CANDIDATE" and not verified_complete:
        findings.append(Finding("FALSE_CLEAR_RISK", "/decision/outcome"))

    if decision.get("history_deletion_allowed") is not False:
        findings.append(Finding("HISTORY_DELETION_DENIED", "/decision/history_deletion_allowed"))

    governance = _mapping(candidate.get("governance"))
    if any(
        governance.get(field) is not False
        for field in (
            "source_state_mutated",
            "clearance_authorized",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
            "public_use_allowed",
        )
    ):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_assessment(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_manifest() -> dict[str, list[str]]:
    path = FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected findings manifest must be an object")
    return {
        str(name): sorted(str(code) for code in codes)
        for name, codes in value.items()
        if isinstance(name, str) and isinstance(codes, list)
    }


def validate_fixtures() -> int:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted(
        path
        for path in (FIXTURE_ROOT / "invalid").glob("*.json")
        if path.name != "expected_findings_manifest.json"
    )
    try:
        expected = _expected_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        print("ERROR: expected findings manifest is unavailable or invalid.")
        return 1
    if not valid_paths or not invalid_paths or sorted(expected) != [path.name for path in invalid_paths]:
        print("ERROR: source record absence fixture inventory is incomplete or drifted.")
        return 1
    failed = False
    for path in valid_paths:
        result = validate_assessment(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    for path in invalid_paths:
        result = validate_assessment(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        failed = failed or result.ok or actual != expected[path.name]
    if failed:
        print("ERROR: source record absence fixture polarity failed.")
        return 1
    print(
        f"CONFIRMED: {len(valid_paths)} valid and {len(invalid_paths)} invalid "
        "source record absence fixtures passed exact polarity."
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM SourceRecordAbsenceAssessment records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_assessment(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
