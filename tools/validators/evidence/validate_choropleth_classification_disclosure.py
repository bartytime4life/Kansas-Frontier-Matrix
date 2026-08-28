"""Validate fixture-only choropleth classification disclosures.

The validator checks declared shape, deterministic identity, classification
break coherence, and review-facing disclosure only. It does not read source
values, calculate classes, choose a method, render a legend, resolve evidence,
decide policy or review, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/choropleth_classification_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/choropleth_classification_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CLASSIFICATION_INCOMPLETE",
    "CLASSIFICATION_UNKNOWN",
    "REFERENCE_UNRESOLVED",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_CLASSIFICATION_COMPUTATION",
    "NO_LEGEND_RENDERING",
    "NO_PUBLICATION_AUTHORITY",
]
PUBLIC_USES = {"PUBLIC_MAP_CANDIDATE", "POLICY_CONTEXT_CANDIDATE"}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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


def _decimal(value: object) -> Decimal | None:
    if not isinstance(value, str):
        return None
    try:
        return Decimal(value)
    except InvalidOperation:
        return None


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    limitations = candidate["limitations"]
    disclosure = candidate["disclosure"]
    classification = candidate["classification"]
    assert isinstance(disclosure, Mapping)
    assert isinstance(classification, Mapping)

    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(disclosure.get("review_record_refs")):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/disclosure/review_record_refs"))

    for name in (
        "layer_manifest",
        "aggregate_statistic",
        "indicator_definition",
        "geography_version",
    ):
        reference = candidate[name]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    method_definition = classification["method_definition"]
    assert isinstance(method_definition, Mapping)
    if method_definition.get("resolution") == "UNRESOLVED":
        findings.add(Finding("REFERENCE_UNRESOLVED", "/classification/method_definition/resolution"))

    state = classification.get("state")
    if state == "ERROR":
        findings.add(Finding("CLASSIFICATION_ERROR", "/classification/state"))
        return sorted(findings)
    if state == "INCOMPLETE":
        findings.add(Finding("CLASSIFICATION_INCOMPLETE", "/classification/state"))
        return sorted(findings)
    if state == "UNKNOWN":
        findings.add(Finding("CLASSIFICATION_UNKNOWN", "/classification/state"))
        return sorted(findings)

    method = classification.get("method")
    class_count = classification.get("class_count")
    break_values = classification.get("break_values")
    if method == "UNKNOWN":
        findings.add(Finding("CLASSIFICATION_METHOD_REQUIRED", "/classification/method"))
    if method in {"MANUAL", "CUSTOM"} and classification.get("rationale_ref") is None:
        findings.add(Finding("CLASSIFICATION_RATIONALE_REQUIRED", "/classification/rationale_ref"))
    if class_count is None:
        findings.add(Finding("CLASS_COUNT_REQUIRED", "/classification/class_count"))

    decimals: list[Decimal] = []
    if isinstance(break_values, list):
        decimals = [item for item in (_decimal(value) for value in break_values) if item is not None]
        if isinstance(class_count, int) and len(break_values) != class_count + 1:
            findings.add(Finding("BREAK_COUNT_MISMATCH", "/classification/break_values"))
        if len(decimals) != len(break_values) or any(
            right <= left for left, right in zip(decimals, decimals[1:])
        ):
            findings.add(Finding("BREAKS_NOT_STRICTLY_INCREASING", "/classification/break_values"))

    if classification.get("boundary_rule") == "UNKNOWN":
        findings.add(Finding("BOUNDARY_RULE_REQUIRED", "/classification/boundary_rule"))
    if classification.get("geography_unit") == "UNKNOWN":
        findings.add(Finding("GEOGRAPHY_UNIT_REQUIRED", "/classification/geography_unit"))

    value_range = classification["value_range"]
    null_treatment = classification["null_treatment"]
    outlier_treatment = classification["outlier_treatment"]
    assert isinstance(value_range, Mapping)
    assert isinstance(null_treatment, Mapping)
    assert isinstance(outlier_treatment, Mapping)

    minimum = _decimal(value_range.get("minimum"))
    maximum = _decimal(value_range.get("maximum"))
    if minimum is None or maximum is None:
        findings.add(Finding("VALUE_RANGE_REQUIRED", "/classification/value_range"))
    elif minimum >= maximum:
        findings.add(Finding("VALUE_RANGE_INVALID", "/classification/value_range"))
    elif decimals and (decimals[0] != minimum or decimals[-1] != maximum):
        findings.add(Finding("VALUE_RANGE_BREAK_MISMATCH", "/classification/value_range"))

    range_assumption = value_range.get("assumption")
    if range_assumption == "UNKNOWN":
        findings.add(Finding("VALUE_RANGE_ASSUMPTION_REQUIRED", "/classification/value_range/assumption"))
    if range_assumption == "CUSTOM" and value_range.get("assumption_ref") is None:
        findings.add(Finding("VALUE_RANGE_REFERENCE_REQUIRED", "/classification/value_range/assumption_ref"))

    null_mode = null_treatment.get("mode")
    if null_mode == "UNKNOWN":
        findings.add(Finding("NULL_TREATMENT_REQUIRED", "/classification/null_treatment/mode"))
    if null_mode == "EXCLUDED_WITH_COUNT" and null_treatment.get("null_count") is None:
        findings.add(Finding("NULL_COUNT_REQUIRED", "/classification/null_treatment/null_count"))
    if null_mode == "IMPUTED_WITH_METHOD_REF" and null_treatment.get("treatment_ref") is None:
        findings.add(Finding("NULL_TREATMENT_REFERENCE_REQUIRED", "/classification/null_treatment/treatment_ref"))

    outlier_mode = outlier_treatment.get("mode")
    if outlier_mode == "UNKNOWN":
        findings.add(Finding("OUTLIER_TREATMENT_REQUIRED", "/classification/outlier_treatment/mode"))
    if outlier_mode in {"CLIPPED", "TRIMMED", "WINSORIZED"} and outlier_treatment.get("treatment_ref") is None:
        findings.add(Finding("OUTLIER_TREATMENT_REFERENCE_REQUIRED", "/classification/outlier_treatment/treatment_ref"))

    if candidate.get("intended_use") in PUBLIC_USES:
        if disclosure.get("legend_ref") is None:
            findings.add(Finding("PUBLIC_LEGEND_REFERENCE_REQUIRED", "/disclosure/legend_ref"))
        if not disclosure.get("review_record_refs"):
            findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/disclosure/review_record_refs"))
        if disclosure.get("evidence_drawer_section_ref") is None:
            findings.add(Finding("EVIDENCE_DRAWER_SECTION_REQUIRED", "/disclosure/evidence_drawer_section_ref"))
        caveat = disclosure.get("public_interpretation_caveat")
        if not isinstance(caveat, str) or caveat.strip() != caveat:
            findings.add(Finding("PUBLIC_INTERPRETATION_CAVEAT_REQUIRED", "/disclosure/public_interpretation_caveat"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "CLASSIFICATION_ERROR" in codes:
        outcome = "ERROR"
    elif not codes:
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
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({finding.code for finding in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only choropleth classification disclosures."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
