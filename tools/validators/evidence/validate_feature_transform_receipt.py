"""Validate fixture-only feature-transform receipt candidates.

This validator checks deterministic declaration and transform-chain coherence.
It does not inspect feature values, execute transforms or models, resolve
evidence, assess scientific fitness, decide policy or review, release, or
publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/feature_transform_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/feature_transform_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"EXECUTION_INCOMPLETE", "FIT_SCOPE_UNRESOLVED", "REFERENCE_UNRESOLVED"}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_EVIDENCE_RESOLUTION",
    "NO_MODEL_OR_TRANSFORM_EXECUTION",
    "NO_PUBLICATION_AUTHORITY",
]
EXPECTED_OUTPUT_STATE = {
    "SCALING": "SCALED",
    "NORMALIZATION": "NORMALIZED",
    "ENCODING": "ENCODED",
    "FEATURE_ENGINEERING": "ENGINEERED",
    "FEATURE_SELECTION": "SELECTED",
    "CUSTOM": "CUSTOM",
}


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


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
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


def _reference_unresolved(value: object) -> bool:
    return isinstance(value, Mapping) and value.get("resolution") == "UNRESOLVED"


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

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    for name in ("feature_set_manifest", "model_card", "run_receipt"):
        if _reference_unresolved(candidate[name]):
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    input_set = candidate["input_feature_set"]
    output_set = candidate["output_feature_set"]
    training = candidate["training_context"]
    transforms = candidate["transforms"]
    assert isinstance(input_set, Mapping)
    assert isinstance(output_set, Mapping)
    assert isinstance(training, Mapping)
    assert isinstance(transforms, list)

    for name, binding in (("input_feature_set", input_set), ("output_feature_set", output_set)):
        refs = binding["feature_refs"]
        if not _canonical_strings(refs):
            findings.add(Finding("FEATURE_REFS_NOT_CANONICAL", f"/{name}/feature_refs"))
        if binding["feature_count"] != len(refs):
            findings.add(Finding("FEATURE_COUNT_MISMATCH", f"/{name}/feature_count"))
        if binding["resolution"] == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    for name in ("split_reference", "leakage_review"):
        if _reference_unresolved(training[name]):
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/training_context/{name}/resolution"))
    if not _canonical_strings(training["review_record_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/training_context/review_record_refs"))
    if candidate["intended_use"] == "PUBLIC_CLAIM_SUPPORT_CANDIDATE" and not training["review_record_refs"]:
        findings.add(Finding("PUBLIC_CANDIDATE_REVIEW_REFERENCE_MISSING", "/training_context/review_record_refs"))
    if not _canonical_strings(candidate["evidence_bundle_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/evidence_bundle_refs"))

    ordinals: list[int] = []
    transform_ids: list[str] = []
    previous_output = input_set["feature_refs"]
    previous_state = "RAW"
    for index, raw_step in enumerate(transforms):
        assert isinstance(raw_step, Mapping)
        step = raw_step
        ordinals.append(step["ordinal"])
        transform_ids.append(step["transform_id"])

        inputs = step["input_feature_refs"]
        outputs = step["output_feature_refs"]
        if not _canonical_strings(inputs):
            findings.add(Finding("FEATURE_REFS_NOT_CANONICAL", f"/transforms/{index}/input_feature_refs"))
        if not _canonical_strings(outputs):
            findings.add(Finding("FEATURE_REFS_NOT_CANONICAL", f"/transforms/{index}/output_feature_refs"))
        if step["feature_count_before"] != len(inputs) or step["feature_count_after"] != len(outputs):
            findings.add(Finding("FEATURE_COUNT_MISMATCH", f"/transforms/{index}"))
        if inputs != previous_output:
            findings.add(Finding("TRANSFORM_CHAIN_MISMATCH", f"/transforms/{index}/input_feature_refs"))
        if step["input_state"] != previous_state:
            findings.add(Finding("FEATURE_STATE_MISMATCH", f"/transforms/{index}/input_state"))
        expected_state = EXPECTED_OUTPUT_STATE[step["transform_family"]]
        if step["output_state"] != expected_state:
            findings.add(Finding("FEATURE_STATE_MISMATCH", f"/transforms/{index}/output_state"))
        if step["transform_family"] in {"SCALING", "NORMALIZATION"} and len(inputs) != len(outputs):
            findings.add(Finding("FEATURE_COUNT_PRESERVATION_REQUIRED", f"/transforms/{index}"))
        if step["transform_family"] == "FEATURE_SELECTION":
            if not set(outputs) < set(inputs):
                findings.add(Finding("FEATURE_SELECTION_NOT_REDUCTIVE", f"/transforms/{index}/output_feature_refs"))
        for name in ("method", "parameter_manifest"):
            if _reference_unresolved(step[name]):
                findings.add(Finding("REFERENCE_UNRESOLVED", f"/transforms/{index}/{name}/resolution"))
        if step["fitted_on"] == "UNRESOLVED":
            findings.add(Finding("FIT_SCOPE_UNRESOLVED", f"/transforms/{index}/fitted_on"))
        if training["evaluation_population_present"] and step["fitted_on"] == "FULL_DATASET":
            findings.add(Finding("EVALUATION_LEAKAGE_RISK", f"/transforms/{index}/fitted_on"))

        previous_output = outputs
        previous_state = step["output_state"]

    if ordinals != list(range(len(transforms))):
        findings.add(Finding("TRANSFORM_ORDINAL_SEQUENCE_INVALID", "/transforms"))
    if len(transform_ids) != len(set(transform_ids)):
        findings.add(Finding("TRANSFORM_ID_DUPLICATE", "/transforms"))
    if previous_output != output_set["feature_refs"]:
        findings.add(Finding("TRANSFORM_CHAIN_MISMATCH", "/output_feature_set/feature_refs"))
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
    parser = argparse.ArgumentParser(description="Validate fixture-only feature-transform receipt candidates.")
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
