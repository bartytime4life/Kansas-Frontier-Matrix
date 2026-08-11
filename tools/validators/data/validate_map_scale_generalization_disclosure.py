"""Validate fixture-only map-scale generalization disclosures.

The validator checks closed shape, deterministic identity, range/basis
coherence, and local disclosure obligations. It does not inspect geometry,
infer scale, resolve references, transform or render a layer, decide policy or
review, promote, release, deploy, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/map_scale_generalization_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/data/map_scale_generalization_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "DISCLOSURE_INCOMPLETE",
    "DISCLOSURE_UNKNOWN",
    "EVIDENCE_SCOPE_UNRESOLVED",
    "GENERALIZATION_METHOD_UNRESOLVED",
    "MAP_PURPOSE_UNRESOLVED",
    "PRECISION_POSTURE_UNKNOWN",
    "VALIDITY_CONTEXT_UNRESOLVED",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _validity_findings(validity: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    basis = validity.get("basis")
    zooms = (validity.get("minimum_zoom"), validity.get("maximum_zoom"))
    scales = (validity.get("minimum_scale_denominator"), validity.get("maximum_scale_denominator"))
    if basis == "UNRESOLVED":
        findings.add(Finding("VALIDITY_CONTEXT_UNRESOLVED", "/validity_context/basis"))
        expected = (None, None, None, None)
    elif basis == "ZOOM_RANGE":
        expected = ("set", "set", None, None)
    elif basis == "SCALE_DENOMINATOR_RANGE":
        expected = (None, None, "set", "set")
    else:
        expected = ("set", "set", "set", "set")
    actual = tuple("set" if value is not None else None for value in (*zooms, *scales))
    if actual != expected:
        findings.add(Finding("VALIDITY_BASIS_FIELDS_INCOHERENT", "/validity_context"))
    if all(isinstance(value, int) for value in zooms) and zooms[0] > zooms[1]:
        findings.add(Finding("VALIDITY_RANGE_INVERTED", "/validity_context"))
    if all(isinstance(value, int) for value in scales) and scales[0] > scales[1]:
        findings.add(Finding("VALIDITY_RANGE_INVERTED", "/validity_context"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    map_purpose = candidate["map_purpose"]
    evidence_scope = candidate["evidence_scope"]
    validity = candidate["validity_context"]
    generalization = candidate["generalization"]
    disclosure = candidate["disclosure"]
    assert all(isinstance(value, Mapping) for value in (map_purpose, evidence_scope, validity, generalization, disclosure))

    if map_purpose.get("resolution") == "UNRESOLVED":
        findings.add(Finding("MAP_PURPOSE_UNRESOLVED", "/map_purpose/resolution"))
    if evidence_scope.get("resolution") == "UNRESOLVED":
        findings.add(Finding("EVIDENCE_SCOPE_UNRESOLVED", "/evidence_scope/resolution"))
    findings.update(_validity_findings(validity))

    for field in ("retained_properties", "omitted_detail_classes"):
        if not _canonical_strings(generalization.get(field)):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/generalization/{field}"))
    if not _canonical_strings(disclosure.get("review_record_refs")):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/disclosure/review_record_refs"))

    method = generalization.get("method")
    omitted = generalization.get("omitted_detail_classes")
    if method == "UNRESOLVED":
        findings.add(Finding("GENERALIZATION_METHOD_UNRESOLVED", "/generalization/method"))
    elif method == "NONE":
        if generalization.get("transform_receipt_ref") is not None or omitted != ["NONE"]:
            findings.add(Finding("NO_GENERALIZATION_DECLARATION_INCOHERENT", "/generalization"))
    else:
        if generalization.get("transform_receipt_ref") is None:
            findings.add(Finding("GENERALIZATION_RECEIPT_REQUIRED", "/generalization/transform_receipt_ref"))
        if not isinstance(omitted, list) or "NONE" in omitted or not omitted:
            findings.add(Finding("GENERALIZATION_OMISSION_REQUIRED", "/generalization/omitted_detail_classes"))
        if disclosure.get("state") == "COMPLETE_FOR_DECLARED_SCOPE":
            if disclosure.get("public_caveat") is None or disclosure.get("details_surface") == "NONE":
                findings.add(Finding("GENERALIZATION_CAVEAT_REQUIRED", "/disclosure"))
            if not disclosure.get("review_record_refs"):
                findings.add(Finding("GENERALIZATION_REVIEW_REFERENCE_REQUIRED", "/disclosure/review_record_refs"))

    if generalization.get("precision_posture") == "UNKNOWN":
        findings.add(Finding("PRECISION_POSTURE_UNKNOWN", "/generalization/precision_posture"))
    state = disclosure.get("state")
    if state == "INCOMPLETE":
        findings.add(Finding("DISCLOSURE_INCOMPLETE", "/disclosure/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("DISCLOSURE_UNKNOWN", "/disclosure/state"))
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
    parser = argparse.ArgumentParser(description="Validate fixture-only map-scale generalization disclosures.")
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
