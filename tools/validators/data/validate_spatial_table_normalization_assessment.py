"""Validate fixture-only spatial table normalization assessments.

The validator evaluates declared metadata only. It does not open table bytes,
infer keys or dependencies, resolve registries, mutate databases, normalize
data, decide policy or review, promote, release, deploy, or publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/spatial_table_normalization_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/data/spatial_table_normalization_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"ASSESSMENT_INCOMPLETE", "ASSESSMENT_UNKNOWN", "NORMAL_FORM_UNASSESSED", "SCHEMA_REGISTRY_UNRESOLVED"}
ANOMALY_BY_KIND = {
    "PARTIAL": "PARTIAL_DEPENDENCY",
    "TRANSITIVE": "TRANSITIVE_DEPENDENCY",
    "MULTIVALUED": "MULTIVALUED_DEPENDENCY",
    "DERIVATIVE_DUPLICATION": "DERIVATIVE_DUPLICATION",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class UnpairedSurrogateError(ValueError):
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


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


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
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


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

    registry = candidate["schema_registry"]
    dependencies = candidate["dependencies"]
    relationships = candidate["relationships"]
    assessment = candidate["assessment"]
    assert isinstance(registry, Mapping) and isinstance(dependencies, list) and isinstance(relationships, list) and isinstance(assessment, Mapping)

    if registry.get("resolution") == "UNRESOLVED":
        findings.add(Finding("SCHEMA_REGISTRY_UNRESOLVED", "/schema_registry/resolution"))

    inventory = candidate["field_inventory"]
    entity_key = candidate["entity_key_fields"]
    for path, value in (("/field_inventory", inventory), ("/entity_key_fields", entity_key), ("/assessment/anomaly_codes", assessment.get("anomaly_codes")), ("/assessment/review_record_refs", assessment.get("review_record_refs"))):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", path))
    inventory_set = set(inventory)
    if not set(entity_key) <= inventory_set:
        findings.add(Finding("FIELD_REFERENCE_UNKNOWN", "/entity_key_fields"))

    dependency_ids: list[object] = []
    dependency_signatures: list[tuple[object, object, object]] = []
    observed_anomalies: set[str] = set()
    for index, dependency in enumerate(dependencies):
        assert isinstance(dependency, Mapping)
        dependency_ids.append(dependency.get("dependency_id"))
        determinant = dependency.get("determinant_fields")
        dependent = dependency.get("dependent_fields")
        evidence = dependency.get("evidence_refs")
        for name, value in (("determinant_fields", determinant), ("dependent_fields", dependent), ("evidence_refs", evidence)):
            if not _canonical_strings(value):
                findings.add(Finding("ARRAY_NOT_CANONICAL", f"/dependencies/{index}/{name}"))
        assert isinstance(determinant, list) and isinstance(dependent, list)
        if not (set(determinant) | set(dependent)) <= inventory_set:
            findings.add(Finding("FIELD_REFERENCE_UNKNOWN", f"/dependencies/{index}"))
        if set(determinant) & set(dependent):
            findings.add(Finding("DEPENDENCY_FIELD_OVERLAP", f"/dependencies/{index}"))
        kind = dependency.get("kind")
        dependency_signatures.append((tuple(determinant), tuple(dependent), kind))
        if kind in ANOMALY_BY_KIND:
            observed_anomalies.add(ANOMALY_BY_KIND[str(kind)])
    if dependency_ids != sorted(dependency_ids) or len(dependency_ids) != len(set(dependency_ids)):
        findings.add(Finding("DEPENDENCIES_NOT_CANONICAL", "/dependencies"))
    if len(dependency_signatures) != len(set(dependency_signatures)):
        findings.add(Finding("DUPLICATE_DEPENDENCY", "/dependencies"))

    relationship_ids: list[object] = []
    for index, relationship in enumerate(relationships):
        assert isinstance(relationship, Mapping)
        relationship_ids.append(relationship.get("relationship_id"))
        local_fields = relationship.get("local_fields")
        target_fields = relationship.get("target_key_fields")
        for name, value in (("local_fields", local_fields), ("target_key_fields", target_fields)):
            if not _canonical_strings(value):
                findings.add(Finding("ARRAY_NOT_CANONICAL", f"/relationships/{index}/{name}"))
        if isinstance(local_fields, list) and not set(local_fields) <= inventory_set:
            findings.add(Finding("FIELD_REFERENCE_UNKNOWN", f"/relationships/{index}/local_fields"))
    if relationship_ids != sorted(relationship_ids) or len(relationship_ids) != len(set(relationship_ids)):
        findings.add(Finding("RELATIONSHIPS_NOT_CANONICAL", "/relationships"))

    declared_anomalies = assessment.get("anomaly_codes")
    if isinstance(declared_anomalies, list) and declared_anomalies != sorted(observed_anomalies):
        findings.add(Finding("ANOMALY_DISCLOSURE_MISMATCH", "/assessment/anomaly_codes"))

    state = assessment.get("state")
    normal_form = assessment.get("declared_normal_form")
    if state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))
    if normal_form == "UNASSESSED":
        findings.add(Finding("NORMAL_FORM_UNASSESSED", "/assessment/declared_normal_form"))

    role = candidate.get("lifecycle_role")
    if role == "PROCESSED_CANONICAL_CANDIDATE":
        if any(assessment.get(name) is not None for name in ("canonical_source_ref", "canonical_source_digest", "denormalization_purpose")):
            findings.add(Finding("CANONICAL_SOURCE_LINK_INCOHERENT", "/assessment"))
        if state == "COMPLETE_FOR_DECLARED_SCOPE" and normal_form not in {"THIRD_NORMAL_FORM", "BOYCE_CODD_NORMAL_FORM"}:
            findings.add(Finding("CANONICAL_NORMAL_FORM_INSUFFICIENT", "/assessment/declared_normal_form"))
        if observed_anomalies:
            findings.add(Finding("CANONICAL_NORMALIZATION_ANOMALY", "/dependencies"))
    else:
        if normal_form != "DENORMALIZED_DERIVATIVE":
            findings.add(Finding("DERIVATIVE_FORM_REQUIRED", "/assessment/declared_normal_form"))
        if not all(assessment.get(name) is not None for name in ("canonical_source_ref", "canonical_source_digest", "denormalization_purpose")):
            findings.add(Finding("DERIVATIVE_SOURCE_BINDING_REQUIRED", "/assessment"))
        if "DERIVATIVE_DUPLICATION" not in observed_anomalies:
            findings.add(Finding("DERIVATIVE_DECLARATION_REQUIRED", "/dependencies"))
        if observed_anomalies - {"DERIVATIVE_DUPLICATION"}:
            findings.add(Finding("DERIVATIVE_ANOMALY_UNSUPPORTED", "/dependencies"))

    if state == "COMPLETE_FOR_DECLARED_SCOPE" and not assessment.get("review_record_refs"):
        findings.add(Finding("REVIEW_REFERENCE_REQUIRED", "/assessment/review_record_refs"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
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


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only spatial table normalization assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
