"""Validate fixture-only aggregate NULL-semantics disclosures.

The validator checks closed shape, deterministic identity, aggregate-kind
fields, NULL treatment, adjacent opaque references, and disclosure posture. It
never executes a query, computes a metric, imputes data, resolves evidence,
decides policy or review, or grants release or publication authority.
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

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/aggregate_null_semantics_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/aggregate_null_semantics_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "AGGREGATE_KIND_UNRESOLVED",
    "DISCLOSURE_INCOMPLETE",
    "DISCLOSURE_UNKNOWN",
    "EMPTY_INPUT_RESULT_UNRESOLVED",
    "GROUP_NULL_HANDLING_UNRESOLVED",
    "INPUT_NULL_HANDLING_UNRESOLVED",
    "MISSINGNESS_PROFILE_UNRESOLVED",
    "QUERY_RECEIPT_UNRESOLVED",
}
COUNT_KINDS = {"ROW_COUNT", "VALUE_COUNT", "DISTINCT_COUNT"}
SINGLE_VALUE_KINDS = {"VALUE_COUNT", "SUM", "AVERAGE", "MINIMUM", "MAXIMUM"}


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
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
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


def _aggregate_findings(semantics: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    kind = semantics.get("aggregate_kind")
    value_fields = semantics.get("value_fields")
    group_fields = semantics.get("group_by_fields")
    input_null = semantics.get("input_null_handling")
    group_null = semantics.get("group_null_handling")
    empty_result = semantics.get("empty_input_result")
    count_ref = semantics.get("count_population_disclosure_ref")
    imputation_ref = semantics.get("imputation_receipt_ref")

    if not _canonical_strings(value_fields):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/semantics/value_fields"))
    if not _canonical_strings(group_fields):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/semantics/group_by_fields"))
    assert isinstance(value_fields, list) and isinstance(group_fields, list)

    if kind == "UNRESOLVED":
        findings.add(Finding("AGGREGATE_KIND_UNRESOLVED", "/semantics/aggregate_kind"))
        if value_fields:
            findings.add(Finding("AGGREGATE_KIND_FIELDS_INCOHERENT", "/semantics/value_fields"))
    elif kind == "ROW_COUNT":
        if value_fields:
            findings.add(Finding("AGGREGATE_KIND_FIELDS_INCOHERENT", "/semantics/value_fields"))
    elif kind == "DISTINCT_COUNT":
        if not value_fields:
            findings.add(Finding("AGGREGATE_KIND_FIELDS_INCOHERENT", "/semantics/value_fields"))
    elif kind in SINGLE_VALUE_KINDS and len(value_fields) != 1:
        findings.add(Finding("AGGREGATE_KIND_FIELDS_INCOHERENT", "/semantics/value_fields"))

    expected_input = {
        "ROW_COUNT": {"INCLUDED_AS_ROW"},
        "VALUE_COUNT": {"EXCLUDED"},
        "DISTINCT_COUNT": {"EXCLUDED"},
        "SUM": {"EXCLUDED", "IMPUTED", "ERROR"},
        "AVERAGE": {"EXCLUDED", "IMPUTED", "ERROR"},
        "MINIMUM": {"EXCLUDED", "IMPUTED", "ERROR"},
        "MAXIMUM": {"EXCLUDED", "IMPUTED", "ERROR"},
        "UNRESOLVED": {"UNRESOLVED"},
    }[kind]
    if input_null not in expected_input:
        findings.add(Finding("INPUT_NULL_SEMANTICS_INCOHERENT", "/semantics/input_null_handling"))
    if input_null == "UNRESOLVED":
        findings.add(Finding("INPUT_NULL_HANDLING_UNRESOLVED", "/semantics/input_null_handling"))

    allowed_empty = {
        "ROW_COUNT": {"ZERO"},
        "VALUE_COUNT": {"ZERO"},
        "DISTINCT_COUNT": {"ZERO"},
        "SUM": {"ZERO", "NULL", "NO_RESULT", "ERROR"},
        "AVERAGE": {"NULL", "NO_RESULT", "ERROR"},
        "MINIMUM": {"NULL", "NO_RESULT", "ERROR"},
        "MAXIMUM": {"NULL", "NO_RESULT", "ERROR"},
        "UNRESOLVED": {"UNRESOLVED"},
    }[kind]
    if empty_result not in allowed_empty:
        findings.add(Finding("EMPTY_INPUT_RESULT_INCOHERENT", "/semantics/empty_input_result"))
    if empty_result == "UNRESOLVED":
        findings.add(Finding("EMPTY_INPUT_RESULT_UNRESOLVED", "/semantics/empty_input_result"))

    if kind in COUNT_KINDS and count_ref is None:
        findings.add(Finding("COUNT_POPULATION_DISCLOSURE_REQUIRED", "/semantics/count_population_disclosure_ref"))
    elif kind not in COUNT_KINDS and count_ref is not None:
        findings.add(Finding("COUNT_POPULATION_DISCLOSURE_PROHIBITED", "/semantics/count_population_disclosure_ref"))

    if input_null == "IMPUTED" and imputation_ref is None:
        findings.add(Finding("IMPUTATION_RECEIPT_REQUIRED", "/semantics/imputation_receipt_ref"))
    elif input_null != "IMPUTED" and imputation_ref is not None:
        findings.add(Finding("IMPUTATION_RECEIPT_PROHIBITED", "/semantics/imputation_receipt_ref"))

    if not group_fields:
        if group_null != "NOT_GROUPED":
            findings.add(Finding("GROUP_NULL_SEMANTICS_INCOHERENT", "/semantics/group_null_handling"))
    elif group_null == "NOT_GROUPED":
        findings.add(Finding("GROUP_NULL_SEMANTICS_INCOHERENT", "/semantics/group_null_handling"))
    if group_null == "UNRESOLVED":
        findings.add(Finding("GROUP_NULL_HANDLING_UNRESOLVED", "/semantics/group_null_handling"))
    return findings


def _disclosure_findings(disclosure: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    if not _canonical_strings(disclosure.get("review_record_refs")):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/disclosure/review_record_refs"))
    state = disclosure.get("state")
    if state == "INCOMPLETE":
        findings.add(Finding("DISCLOSURE_INCOMPLETE", "/disclosure/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("DISCLOSURE_UNKNOWN", "/disclosure/state"))
    elif disclosure.get("summary") is None:
        findings.add(Finding("DISCLOSURE_SUMMARY_REQUIRED", "/disclosure/summary"))
    if disclosure.get("intended_use") == "PUBLIC_CANDIDATE":
        if disclosure.get("details_surface") == "NONE":
            findings.add(Finding("PUBLIC_DISCLOSURE_SURFACE_REQUIRED", "/disclosure/details_surface"))
        if not disclosure.get("review_record_refs"):
            findings.add(Finding("PUBLIC_DISCLOSURE_REVIEW_REQUIRED", "/disclosure/review_record_refs"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    query = candidate["query_receipt"]
    missingness = candidate["missingness_profile"]
    semantics = candidate["semantics"]
    disclosure = candidate["disclosure"]
    assert all(isinstance(value, Mapping) for value in (query, missingness, semantics, disclosure))
    if query.get("resolution") == "UNRESOLVED":
        findings.add(Finding("QUERY_RECEIPT_UNRESOLVED", "/query_receipt/resolution"))
    if missingness.get("resolution") == "UNRESOLVED":
        findings.add(Finding("MISSINGNESS_PROFILE_UNRESOLVED", "/missingness_profile/resolution"))
    findings.update(_aggregate_findings(semantics))
    findings.update(_disclosure_findings(disclosure))
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
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})},
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
    parser = argparse.ArgumentParser(description="Validate fixture-only aggregate NULL-semantics disclosures.")
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
