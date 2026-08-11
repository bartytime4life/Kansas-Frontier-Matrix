"""Validate fixture-only claim scope dimension assessments.

The validator proves closed shape, deterministic identity, and local
time-space-attribute role coherence. It does not inspect claims, resolve
EvidenceBundles, authenticate scope references, evaluate representation
fitness or policy, approve review, release, deploy, publish, or authorize
public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/claim_scope_dimension_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/claim_scope_dimension_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ASSESSMENT_INCOMPLETE",
    "ASSESSMENT_UNKNOWN",
    "DIMENSION_ROLE_UNRESOLVED",
    "DIMENSION_SCOPE_UNRESOLVED",
}
INTERPRETATION_BY_DIMENSION = {
    "TIME": "TIME_SERIES_AT_CONTROLLED_SPACE_ATTRIBUTE",
    "SPACE": "SPATIAL_CROSS_SECTION_AT_CONTROLLED_TIME_ATTRIBUTE",
    "ATTRIBUTE": "ATTRIBUTE_COMPARISON_AT_CONTROLLED_TIME_SPACE",
}
EXPECTED_LIMITATIONS = [
    "CLAIM_SCOPE_ONLY",
    "NO_EVIDENCE_RESOLUTION",
    "NO_PUBLICATION_AUTHORITY",
    "NO_REPRESENTATION_AUTHORITY",
]


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    assessment = candidate["assessment"]
    dimensions = candidate["dimensions"]
    limitations = candidate["limitations"]
    assert isinstance(assessment, Mapping)
    assert isinstance(dimensions, Mapping)

    review_refs = assessment.get("review_record_refs")
    if not _canonical_strings(review_refs):
        findings.add(Finding("REVIEW_REFERENCES_NOT_CANONICAL", "/assessment/review_record_refs"))
    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    role_by_dimension: dict[str, object] = {}
    scope_refs: list[object] = []
    unresolved = False
    for name in ("time", "space", "attribute"):
        item = dimensions[name]
        assert isinstance(item, Mapping)
        role_by_dimension[name.upper()] = item.get("role")
        scope_refs.append(item.get("scope_ref"))
        if item.get("role") == "UNRESOLVED":
            unresolved = True
            findings.add(Finding("DIMENSION_ROLE_UNRESOLVED", f"/dimensions/{name}/role"))
        if item.get("resolution") == "UNRESOLVED":
            unresolved = True
            findings.add(Finding("DIMENSION_SCOPE_UNRESOLVED", f"/dimensions/{name}/resolution"))
    if len(scope_refs) != len(set(scope_refs)):
        findings.add(Finding("DUPLICATE_DIMENSION_SCOPE_REFERENCE", "/dimensions"))

    state = assessment.get("state")
    measured = [name for name, role in role_by_dimension.items() if role == "MEASURED"]
    controlled = [name for name, role in role_by_dimension.items() if role == "CONTROLLED"]
    declared = assessment.get("measured_dimension")
    interpretation = assessment.get("interpretation_class")

    if state == "COMPLETE":
        if unresolved:
            findings.add(Finding("COMPLETE_SCOPE_UNRESOLVED", "/assessment/state"))
        if len(measured) != 1 or len(controlled) != 2:
            findings.add(Finding("DIMENSION_ROLE_CARDINALITY_INVALID", "/dimensions"))
        elif declared != measured[0]:
            findings.add(Finding("MEASURED_DIMENSION_MISMATCH", "/assessment/measured_dimension"))
        if declared in INTERPRETATION_BY_DIMENSION:
            if interpretation != INTERPRETATION_BY_DIMENSION[str(declared)]:
                findings.add(Finding("INTERPRETATION_CLASS_MISMATCH", "/assessment/interpretation_class"))
        else:
            findings.add(Finding("COMPLETE_MEASURED_DIMENSION_UNKNOWN", "/assessment/measured_dimension"))
        if candidate.get("intended_use") in {"PUBLIC_CANDIDATE", "POLICY_CONTEXT"} and not review_refs:
            findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/assessment/review_record_refs"))
    elif state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
        if not unresolved or declared != "UNKNOWN" or interpretation != "UNRESOLVED":
            findings.add(Finding("ASSESSMENT_STATE_INCOHERENT", "/assessment"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))
        if not unresolved or declared != "UNKNOWN" or interpretation != "UNRESOLVED":
            findings.add(Finding("ASSESSMENT_STATE_INCOHERENT", "/assessment"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only claim scope dimension assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
