"""Validate fixture-only missing-value filter receipt candidates.

The validator proves closed shape, deterministic identity, explicit bindings,
missing-rule disclosure, row-count closure, before/after count summaries,
population-change posture, and canonical local references. It does not read a
dataset, execute a filter, compute statistics, resolve evidence, decide policy
or review, promote, release, deploy, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/missing_value_filter_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/missing_value_filter_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ANALYSIS_SCOPE_UNRESOLVED",
    "INPUT_DATASET_UNRESOLVED",
    "SUPPORTING_ARTIFACT_UNRESOLVED",
    "POPULATION_CHANGE_UNRESOLVED",
}


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


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)),
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


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    scope = candidate["analysis_scope"]
    input_dataset = candidate["input_dataset"]
    support = candidate["supporting_artifacts"]
    output_dataset = candidate["output_dataset"]
    population = candidate["population_change_assessment"]
    assert all(
        isinstance(value, Mapping)
        for value in (scope, input_dataset, support, output_dataset, population)
    )

    if scope["resolution"] == "UNRESOLVED":
        findings.add(Finding("ANALYSIS_SCOPE_UNRESOLVED", "/analysis_scope/resolution"))
    if input_dataset["resolution"] == "UNRESOLVED":
        findings.add(Finding("INPUT_DATASET_UNRESOLVED", "/input_dataset/resolution"))
    if any(
        isinstance(binding, Mapping) and binding["resolution"] == "UNRESOLVED"
        for binding in support.values()
    ):
        findings.add(Finding("SUPPORTING_ARTIFACT_UNRESOLVED", "/supporting_artifacts"))
    if population["resolution"] == "UNRESOLVED" or population["status"] == "UNKNOWN":
        findings.add(Finding("POPULATION_CHANGE_UNRESOLVED", "/population_change_assessment"))
    if not _canonical_strings(population["compared_dimensions"]):
        findings.add(Finding("COMPARED_DIMENSIONS_NOT_CANONICAL", "/population_change_assessment/compared_dimensions"))

    steps = candidate["filter_steps"]
    summaries = candidate["summary_statistic_steps"]
    assert isinstance(steps, list) and isinstance(summaries, list)
    step_ids = [step["step_id"] for step in steps]
    if len(step_ids) != len(set(step_ids)):
        findings.add(Finding("FILTER_STEP_ID_DUPLICATE", "/filter_steps"))
    if step_ids != sorted(step_ids):
        findings.add(Finding("FILTER_STEPS_NOT_CANONICAL", "/filter_steps"))

    prior_output: object = input_dataset["row_count"]
    steps_by_id: dict[str, Mapping[str, object]] = {}
    for index, step in enumerate(steps):
        assert isinstance(step, Mapping)
        steps_by_id.setdefault(str(step["step_id"]), step)
        rule = step["missing_rule"]
        assert isinstance(rule, Mapping)
        tokens = rule["sentinel_tokens"]
        if not rule["null_values"] and not rule["empty_strings"] and not tokens:
            findings.add(Finding("MISSING_RULE_EMPTY", f"/filter_steps/{index}/missing_rule"))
        if not _canonical_strings(tokens):
            findings.add(Finding("SENTINEL_TOKENS_NOT_CANONICAL", f"/filter_steps/{index}/missing_rule/sentinel_tokens"))
        if step["input_rows"] != step["excluded_rows"] + step["output_rows"]:
            findings.add(Finding("FILTER_COUNT_MISMATCH", f"/filter_steps/{index}"))
        if step["input_rows"] != prior_output:
            findings.add(Finding("FILTER_CHAIN_MISMATCH", f"/filter_steps/{index}/input_rows"))
        prior_output = step["output_rows"]

    if prior_output != output_dataset["row_count"]:
        findings.add(Finding("OUTPUT_COUNT_MISMATCH", "/output_dataset/row_count"))
    if input_dataset["artifact_ref"] == output_dataset["artifact_ref"]:
        findings.add(Finding("INPUT_OUTPUT_IDENTITY_COLLISION", "/output_dataset/artifact_ref"))

    summary_ids = [entry["step_id"] for entry in summaries]
    if len(summary_ids) != len(set(summary_ids)):
        findings.add(Finding("SUMMARY_STEP_ID_DUPLICATE", "/summary_statistic_steps"))
    coverage: dict[str, list[str]] = {step_id: [] for step_id in steps_by_id}
    for index, summary in enumerate(summaries):
        assert isinstance(summary, Mapping)
        step_id = str(summary["filter_step_id"])
        step = steps_by_id.get(step_id)
        if step is None:
            findings.add(Finding("SUMMARY_FILTER_REF_UNKNOWN", f"/summary_statistic_steps/{index}/filter_step_id"))
            continue
        coverage[step_id].append(str(summary["population"]))
        if summary["field_name"] != step["field_name"]:
            findings.add(Finding("SUMMARY_FIELD_MISMATCH", f"/summary_statistic_steps/{index}/field_name"))
        expected_count = step["input_rows"] if summary["population"] == "BEFORE_FILTER" else step["output_rows"]
        if summary["row_count"] != expected_count:
            findings.add(Finding("SUMMARY_ROW_COUNT_MISMATCH", f"/summary_statistic_steps/{index}/row_count"))
    for step_id, populations in coverage.items():
        if sorted(populations) != ["AFTER_FILTER", "BEFORE_FILTER"]:
            findings.add(Finding("SUMMARY_PAIR_INCOMPLETE", f"/summary_statistic_steps/{step_id}"))

    if not _canonical_strings(candidate["evidence_refs"]):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs"))
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
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({item.code for item in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
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
        description="Validate fixture-only missing-value filter receipt candidates."
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
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
