"""Validate fixture-only aggregate-grouping disclosure candidates.

The validator checks grouping-level declarations and safe local invariants. It
does not execute an aggregation, inspect values, resolve evidence, decide
policy or review, release, or publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/aggregate_grouping_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/aggregate_grouping_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"ENGINE_PARITY_UNRESOLVED", "EXECUTION_INCOMPLETE", "REFERENCE_UNRESOLVED"}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_AGGREGATION_EXECUTION",
    "NO_EVIDENCE_RESOLUTION",
    "NO_PUBLICATION_AUTHORITY",
]
EXPECTED_LABEL = {"DETAIL": "DETAIL_GROUP", "SUBTOTAL": "SUBTOTAL", "GRAND_TOTAL": "GRAND_TOTAL"}


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
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
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


def _ordered_subset(value: object, dimensions: list[str]) -> bool:
    if not isinstance(value, list) or len(value) != len(set(value)):
        return False
    return value == [dimension for dimension in dimensions if dimension in value]


def _reference_unresolved(value: object) -> bool:
    return isinstance(value, Mapping) and value.get("resolution") == "UNRESOLVED"


def _grouping_mask(dimensions: list[str], rolled_up: list[str]) -> int:
    rolled = set(rolled_up)
    return sum(1 << index for index, dimension in enumerate(dimensions) if dimension in rolled)


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/recorded_at"))

    execution_state = candidate["execution_state"]
    if execution_state == "INCOMPLETE":
        findings.add(Finding("EXECUTION_INCOMPLETE", "/execution_state"))
    elif execution_state == "ERROR":
        findings.add(Finding("EXECUTION_ERROR", "/execution_state"))

    for name in ("query_run", "method_definition"):
        if _reference_unresolved(candidate[name]):
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(candidate["evidence_bundle_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/evidence_bundle_refs"))

    dimensions = candidate["grouping_dimensions"]
    rows = candidate["rows"]
    aggregate_output = candidate["aggregate_output"]
    engine = candidate["engine_semantics"]
    disclosure = candidate["public_disclosure"]
    assert isinstance(dimensions, list)
    assert isinstance(rows, list)
    assert isinstance(aggregate_output, Mapping)
    assert isinstance(engine, Mapping)
    assert isinstance(disclosure, Mapping)

    if _reference_unresolved(aggregate_output):
        findings.add(Finding("REFERENCE_UNRESOLVED", "/aggregate_output/resolution"))
    if _reference_unresolved(engine["engine_profile"]):
        findings.add(Finding("REFERENCE_UNRESOLVED", "/engine_semantics/engine_profile/resolution"))
    if engine["parity_state"] == "UNRESOLVED":
        findings.add(Finding("ENGINE_PARITY_UNRESOLVED", "/engine_semantics/parity_state"))
    elif engine["parity_state"] == "MISMATCH":
        findings.add(Finding("ENGINE_PARITY_MISMATCH", "/engine_semantics/parity_state"))
    if engine["parity_state"] == "SYNTHETIC_PARITY" and engine["parity_fixture_ref"] is None:
        findings.add(Finding("PARITY_FIXTURE_MISSING", "/engine_semantics/parity_fixture_ref"))

    if not _canonical_strings(disclosure["review_record_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/public_disclosure/review_record_refs"))
    if not _canonical_strings(disclosure["release_manifest_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/public_disclosure/release_manifest_refs"))
    if candidate["intended_use"] == "PUBLIC_AGGREGATE_SUPPORT_CANDIDATE":
        if not disclosure["review_record_refs"] or not disclosure["release_manifest_refs"]:
            findings.add(Finding("PUBLIC_CANDIDATE_REFERENCE_MISSING", "/public_disclosure"))
        for field in ("detail_rows_labeled", "subtotals_labeled", "grand_total_labeled", "source_nulls_distinguished"):
            if disclosure[field] is not True:
                findings.add(Finding("PUBLIC_LABEL_DISCLOSURE_INCOMPLETE", f"/public_disclosure/{field}"))

    ordinals: list[int] = []
    row_refs: list[str] = []
    row_kinds: set[str] = set()
    all_dimensions = set(dimensions)
    for index, raw_row in enumerate(rows):
        assert isinstance(raw_row, Mapping)
        row = raw_row
        ordinals.append(row["ordinal"])
        row_refs.append(row["row_ref"])
        row_kinds.add(row["row_kind"])
        keys = row["grouping_keys"]
        rolled = row["rolled_up_dimensions"]
        source_nulls = row["source_null_dimensions"]
        assert isinstance(keys, list)
        assert isinstance(rolled, list)
        assert isinstance(source_nulls, list)

        if not _ordered_subset(keys, dimensions) or not _ordered_subset(rolled, dimensions) or not _ordered_subset(source_nulls, dimensions):
            findings.add(Finding("DIMENSION_ORDER_INVALID", f"/rows/{index}"))
        if set(keys) & set(rolled) or set(keys) | set(rolled) != all_dimensions:
            findings.add(Finding("DIMENSION_PARTITION_INVALID", f"/rows/{index}"))
        if not set(source_nulls) <= set(keys):
            findings.add(Finding("SOURCE_NULL_ROLE_INVALID", f"/rows/{index}/source_null_dimensions"))
        if row["grouping_mask"] != _grouping_mask(dimensions, rolled):
            findings.add(Finding("GROUPING_MASK_MISMATCH", f"/rows/{index}/grouping_mask"))
        if row["display_label"] != EXPECTED_LABEL[row["row_kind"]]:
            findings.add(Finding("ROW_LABEL_MISMATCH", f"/rows/{index}/display_label"))

        if row["row_kind"] == "DETAIL" and (rolled or keys != dimensions):
            findings.add(Finding("ROW_KIND_SEMANTICS_INVALID", f"/rows/{index}"))
        elif row["row_kind"] == "SUBTOTAL" and (not keys or not rolled):
            findings.add(Finding("ROW_KIND_SEMANTICS_INVALID", f"/rows/{index}"))
        elif row["row_kind"] == "GRAND_TOTAL" and (keys or rolled != dimensions):
            findings.add(Finding("ROW_KIND_SEMANTICS_INVALID", f"/rows/{index}"))

        if candidate["aggregation_operation"] == "GROUP_BY" and row["row_kind"] != "DETAIL":
            findings.add(Finding("GROUP_BY_NON_DETAIL_ROW", f"/rows/{index}/row_kind"))
        if candidate["aggregation_operation"] == "ROLLUP" and row["row_kind"] == "SUBTOTAL":
            if keys != dimensions[: len(keys)] or rolled != dimensions[len(keys) :]:
                findings.add(Finding("ROLLUP_PREFIX_SEMANTICS_INVALID", f"/rows/{index}"))

        for name in ("group_values", "aggregate_statistic"):
            if _reference_unresolved(row[name]):
                findings.add(Finding("REFERENCE_UNRESOLVED", f"/rows/{index}/{name}/resolution"))

    if ordinals != list(range(len(rows))):
        findings.add(Finding("ROW_ORDINAL_SEQUENCE_INVALID", "/rows"))
    if len(row_refs) != len(set(row_refs)):
        findings.add(Finding("ROW_REFERENCE_DUPLICATE", "/rows"))
    if aggregate_output["declared_row_count"] != len(rows):
        findings.add(Finding("OUTPUT_ROW_COUNT_MISMATCH", "/aggregate_output/declared_row_count"))
    if execution_state == "COMPLETE" and candidate["aggregation_operation"] in {"ROLLUP", "CUBE"}:
        if row_kinds != {"DETAIL", "SUBTOTAL", "GRAND_TOTAL"}:
            findings.add(Finding("ROW_KIND_COVERAGE_INCOMPLETE", "/rows"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "EXECUTION_ERROR" in codes:
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
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
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
    parser = argparse.ArgumentParser(description="Validate fixture-only aggregate-grouping disclosures.")
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
