"""Validate fixture-only claim scope dimension assessments.

This module checks declared time, space, and attribute scope metadata. It does
not inspect observations, resolve evidence, infer scope, decide policy or
review, change lifecycle state, release, publish, or authorize a public claim.
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
DIMENSIONS = ("ATTRIBUTE", "SPACE", "TIME")
ABSTAIN_CODES = {"ASSESSMENT_INCOMPLETE", "ASSESSMENT_UNKNOWN", "DIMENSION_SCOPE_UNRESOLVED", "EVIDENCE_SCOPE_UNRESOLVED"}
BASE_DISCLOSURES = {"ATTRIBUTE_SCOPE_DISCLOSURE", "SPACE_SCOPE_DISCLOSURE", "TIME_SCOPE_DISCLOSURE"}
PUBLIC_USES = {"PUBLIC_MAP", "PUBLIC_ANSWER", "POLICY_CONTEXT"}


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
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
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
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (list(error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    dimensions = candidate["dimensions"]
    assessment = candidate["assessment"]
    evidence_scope = candidate["evidence_bundle_scope"]
    assert isinstance(dimensions, Mapping) and isinstance(assessment, Mapping) and isinstance(evidence_scope, Mapping)

    for field in ("controlled_dimensions", "measured_dimensions", "unresolved_dimensions", "obligations", "review_record_refs"):
        if not _canonical_strings(assessment.get(field)):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/assessment/{field}"))

    role_by_name: dict[str, str] = {}
    for name, key in (("ATTRIBUTE", "attribute"), ("SPACE", "space"), ("TIME", "time")):
        declaration = dimensions[key]
        assert isinstance(declaration, Mapping)
        role = str(declaration["role"])
        role_by_name[name] = role
        resolution = declaration["resolution"]
        if (role == "UNRESOLVED") != (resolution == "UNRESOLVED"):
            findings.add(Finding("DIMENSION_RESOLUTION_ROLE_MISMATCH", f"/dimensions/{key}"))

    expected = {
        "controlled_dimensions": sorted(name for name, role in role_by_name.items() if role == "CONTROLLED"),
        "measured_dimensions": sorted(name for name, role in role_by_name.items() if role == "MEASURED"),
        "unresolved_dimensions": sorted(name for name, role in role_by_name.items() if role == "UNRESOLVED"),
    }
    for field, values in expected.items():
        if assessment.get(field) != values:
            findings.add(Finding("DIMENSION_PARTITION_MISMATCH", f"/assessment/{field}"))

    state = assessment["state"]
    unresolved = expected["unresolved_dimensions"]
    if state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))
    if unresolved:
        if state == "COMPLETE":
            findings.add(Finding("UNRESOLVED_DIMENSION_COMPLETE_DENIED", "/assessment/state"))
        else:
            findings.add(Finding("DIMENSION_SCOPE_UNRESOLVED", "/assessment/unresolved_dimensions"))
    if evidence_scope["resolution"] == "UNRESOLVED":
        findings.add(Finding("EVIDENCE_SCOPE_UNRESOLVED", "/evidence_bundle_scope/resolution"))

    if state == "COMPLETE":
        if not expected["controlled_dimensions"]:
            findings.add(Finding("CONTROLLED_DIMENSION_REQUIRED", "/assessment/controlled_dimensions"))
        if not expected["measured_dimensions"]:
            findings.add(Finding("MEASURED_DIMENSION_REQUIRED", "/assessment/measured_dimensions"))
        obligations = set(assessment["obligations"])
        if not BASE_DISCLOSURES <= obligations:
            findings.add(Finding("SCOPE_DISCLOSURES_REQUIRED", "/assessment/obligations"))
        if candidate["intended_use"] in PUBLIC_USES:
            if "PUBLIC_SCOPE_CAVEAT_REQUIRED" not in obligations:
                findings.add(Finding("PUBLIC_SCOPE_CAVEAT_REQUIRED", "/assessment/obligations"))
            if not assessment["review_record_refs"]:
                findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/assessment/review_record_refs"))
            if evidence_scope["resolution"] != "RESOLVED":
                findings.add(Finding("PUBLIC_EVIDENCE_SCOPE_REQUIRED", "/evidence_bundle_scope/resolution"))
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest() -> list[tuple[str, str, list[str]]]:
    manifest, findings = load_json_object(FIXTURE_PATH)
    if manifest is None or findings:
        raise ValueError("fixture manifest is unreadable")
    results: list[tuple[str, str, list[str]]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        result = validate_candidate(materialize_fixture_case(manifest, entry))
        expected = entry["expected"]
        assert isinstance(expected, Mapping)
        name = str(entry["name"])
        if result.outcome != expected["outcome"] or result.codes != expected["codes"]:
            raise AssertionError(f"{name}: expected {expected}, got {result.outcome} {result.codes}")
        results.append((name, result.outcome, result.codes))
    return results


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        for name, outcome, codes in validate_fixture_manifest():
            print(json.dumps({"case": name, "codes": codes, "outcome": outcome}, sort_keys=True, separators=(",", ":")))
        return 0
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        candidate, findings = load_json_object(path)
        result = ValidationResult("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
        print(json.dumps({"file": path.name, "codes": result.codes, "outcome": result.outcome}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.outcome == "PASS" else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
