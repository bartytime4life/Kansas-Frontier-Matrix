#!/usr/bin/env python3
"""Validate KFM MaterialChangeAssessment records without network access.

A passing result proves bounded shape and local consistency only. It does not
resolve evidence, evaluate policy, authorize promotion, release, or publish.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/material_change_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/material_change_assessment"
MAX_FILE_BYTES = 1_048_576
SCOPE = "material-change-assessment-shape-and-local-consistency-only"


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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
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
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: dict[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in validator.iter_errors(candidate)
    ]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + ("0" * 64)


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _semantic_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    assessment_id = candidate.get("assessment_id")
    profile = _mapping(candidate.get("profile"))
    comparison = _mapping(candidate.get("comparison"))
    classification = _mapping(candidate.get("classification"))
    evidence = _mapping(candidate.get("evidence"))
    timing = _mapping(candidate.get("timing"))
    lineage = _mapping(candidate.get("lineage"))
    governance = _mapping(candidate.get("governance"))
    criteria = _array(candidate.get("criteria"))

    for field, value in (
        ("/profile/spec_hash", profile.get("spec_hash")),
        ("/comparison/baseline_digest", comparison.get("baseline_digest")),
        ("/comparison/candidate_digest", comparison.get("candidate_digest")),
        ("/governance/spec_hash", governance.get("spec_hash")),
    ):
        if _is_zero_digest(value):
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    baseline_digest = comparison.get("baseline_digest")
    candidate_digest = comparison.get("candidate_digest")
    byte_changed = comparison.get("byte_changed")
    semantic_changed = comparison.get("semantic_changed")
    if isinstance(baseline_digest, str) and isinstance(candidate_digest, str) and isinstance(byte_changed, bool):
        if byte_changed != (baseline_digest != candidate_digest):
            findings.append(Finding("BYTE_CHANGE_DIGEST_MISMATCH", "/comparison/byte_changed"))

    criterion_ids = [item.get("criterion_id") for item in criteria if isinstance(item, dict)]
    if (
        len(criterion_ids) != len(criteria)
        or not all(isinstance(item, str) for item in criterion_ids)
        or criterion_ids != sorted(criterion_ids)
        or len(criterion_ids) != len(set(criterion_ids))
    ):
        findings.append(Finding("CRITERIA_NOT_CANONICAL", "/criteria"))
    for index, item in enumerate(criteria):
        if not isinstance(item, dict):
            continue
        refs = _array(item.get("evidence_refs"))
        if not _sorted_unique_strings(refs):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/criteria/{index}/evidence_refs"))

    for field in ("validation_report_refs", "source_refs"):
        refs = _array(evidence.get(field))
        if not _sorted_unique_strings(refs):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/evidence/{field}"))
    reasons = _array(classification.get("reason_codes"))
    if not _sorted_unique_strings(reasons):
        findings.append(Finding("REASONS_NOT_CANONICAL", "/classification/reason_codes"))

    change_class = classification.get("change_class")
    material = classification.get("material")
    outcome = classification.get("outcome")
    required_results = [item.get("result") for item in criteria if isinstance(item, dict) and item.get("required") is True]
    all_results = [item.get("result") for item in criteria if isinstance(item, dict)]

    expected = {
        "UNCHANGED": (False, "NON_EVENT", False),
        "BYTE_ONLY": (False, "NON_EVENT", False),
        "SEMANTIC_NON_MATERIAL": (False, "NON_EVENT", True),
        "MATERIAL": (True, "PROMOTION_CANDIDATE", True),
        "UNDETERMINED": (None, "HOLD", None),
        "ERROR": (None, "ERROR", None),
    }
    if change_class in expected:
        expected_material, expected_outcome, expected_semantic = expected[change_class]
        if material is not expected_material:
            findings.append(Finding("MATERIAL_STATE_MISMATCH", "/classification/material"))
        if outcome != expected_outcome:
            findings.append(Finding("OUTCOME_CLASS_MISMATCH", "/classification/outcome"))
        if expected_semantic is not None and semantic_changed is not expected_semantic:
            findings.append(Finding("SEMANTIC_STATE_MISMATCH", "/comparison/semantic_changed"))

    if change_class == "UNCHANGED":
        if byte_changed is not False:
            findings.append(Finding("UNCHANGED_BYTES_MISMATCH", "/comparison/byte_changed"))
        if "NO_BYTE_CHANGE" not in reasons:
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))
    elif change_class == "BYTE_ONLY":
        if byte_changed is not True:
            findings.append(Finding("BYTE_ONLY_BYTES_MISMATCH", "/comparison/byte_changed"))
        if not ({"BYTE_ONLY_CHANGE", "CANONICAL_EQUIVALENT"} & set(reasons)):
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))
    elif change_class == "SEMANTIC_NON_MATERIAL":
        if byte_changed is not True or "FAIL" not in all_results:
            findings.append(Finding("NON_MATERIAL_CRITERIA_MISMATCH", "/criteria"))
        if "BELOW_MATERIALITY_THRESHOLD" not in reasons:
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))
    elif change_class == "MATERIAL":
        if byte_changed is not True or not criteria or not required_results or any(result != "PASS" for result in required_results):
            findings.append(Finding("MATERIAL_CRITERIA_NOT_SATISFIED", "/criteria"))
        if not ({"MATERIALITY_THRESHOLD_MET", "DOMAIN_STATUS_CHANGE"} & set(reasons)):
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))
    elif change_class == "UNDETERMINED":
        if not ({"MISSING_BASELINE", "PROFILE_UNRESOLVED", "METRIC_UNAVAILABLE", "INSUFFICIENT_EVIDENCE"} & set(reasons)):
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))
    elif change_class == "ERROR":
        if not ({"INPUT_INVALID", "PROFILE_INVALID", "EVALUATION_ERROR"} & set(reasons)):
            findings.append(Finding("REASON_FAMILY_MISMATCH", "/classification/reason_codes"))

    baseline_time = _parse_time(timing.get("baseline_as_of"))
    candidate_time = _parse_time(timing.get("candidate_as_of"))
    assessed_time = _parse_time(timing.get("assessed_at"))
    if baseline_time and candidate_time and baseline_time > candidate_time:
        findings.append(Finding("BASELINE_AFTER_CANDIDATE", "/timing/baseline_as_of"))
    if candidate_time and assessed_time and candidate_time > assessed_time:
        findings.append(Finding("CANDIDATE_AFTER_ASSESSMENT", "/timing/candidate_as_of"))

    if assessment_id and lineage.get("supersedes") == assessment_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/supersedes"))
    if assessment_id and lineage.get("superseded_by") == assessment_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/supersed_by"))

    if any(governance.get(field) is not False for field in (
        "authority_created", "policy_evaluated", "promotion_authorized", "public_use_allowed"
    )) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_assessment(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(directory.glob(f"{prefix}*.json"), key=lambda path: path.as_posix())


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads((directory / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 1
    passed = True
    for path in valid_files:
        result = validate_assessment(path)
        print(_serialize(path, result))
        passed = passed and result.ok
    for path in invalid_files:
        result = validate_assessment(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(json.dumps({"actual": actual, "expected": expected, "file": path.as_posix(), "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":"))
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM MaterialChangeAssessment records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
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
