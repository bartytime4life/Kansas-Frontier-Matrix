"""Validate fixture-only hyperparameter-tuning receipt candidates.

This validator checks declared search, selection, reproducibility, disclosure,
and deterministic identity only. It never reads data, trains or evaluates a
model, resolves evidence, or grants review, release, deployment, publication,
or public-use authority.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import CanonicalizationFailure, compute_spec_hash  # noqa: E402

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/hyperparameter_tuning_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/hyperparameter_tuning_receipt/cases.json"
)
MAX_FILE_BYTES = 1_048_576
PUBLIC_USE = "PUBLIC_CLAIM_SUPPORT_CANDIDATE"
STOCHASTIC_METHODS = {
    "RANDOM_SEARCH",
    "BAYESIAN_OPTIMIZATION",
    "SUCCESSIVE_HALVING",
}
ABSTAIN_CODES = {
    "REFERENCE_UNRESOLVED",
    "REPRODUCIBILITY_UNRESOLVED",
    "SEARCH_METHOD_UNRESOLVED",
    "TUNING_INCOMPLETE",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_DATASET_ACCESS",
    "NO_EVIDENCE_RESOLUTION",
    "NO_METRIC_RECOMPUTATION",
    "NO_MODEL_EXECUTION",
    "NO_PUBLICATION_AUTHORITY",
    "NO_SENSITIVE_VALUES",
    "NO_TRAINING_EXECUTION",
]


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


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    subject.pop("receipt_ref", None)
    return compute_spec_hash(subject)


def expected_receipt_ref(profile_hash: str) -> str:
    return "kfm:hyperparameter-tuning-receipt:" + profile_hash.removeprefix(
        "sha256:"
    )


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
    )
    findings: list[Finding] = []
    for error in errors[:100]:
        path = "/" + "/".join(str(part) for part in error.absolute_path)
        findings.append(Finding("SCHEMA_INVALID", path or "/"))
    if len(errors) > 100:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _canonical_names(value: object) -> list[str] | None:
    if not isinstance(value, list):
        return None
    names = [item.get("parameter_name") for item in value if isinstance(item, Mapping)]
    if len(names) != len(value) or not all(isinstance(name, str) for name in names):
        return None
    return names  # type: ignore[return-value]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.utcoffset() == timezone.utc.utcoffset(parsed)


def _reference_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    for group_name in ("model", "inputs"):
        group = candidate[group_name]
        assert isinstance(group, Mapping)
        for field, reference in group.items():
            assert isinstance(reference, Mapping)
            if reference.get("resolution") == "UNRESOLVED":
                findings.add(Finding("REFERENCE_UNRESOLVED", f"/{group_name}/{field}"))
    method_definition = candidate["search"]["method_definition"]  # type: ignore[index]
    if isinstance(method_definition, Mapping):
        if method_definition.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", "/search/method_definition"))
    return findings


def validate_candidate(candidate: Mapping[str, object]) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("DENY", tuple(sorted(schema_findings)))

    findings = _reference_findings(candidate)
    try:
        expected_hash = compute_profile_hash(candidate)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        return ValidationResult(
            "ERROR", (Finding("CANONICALIZATION_FAILED", "/"),)
        )
    if candidate.get("profile_spec_hash") != expected_hash:
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("receipt_ref") != expected_receipt_ref(expected_hash):
        findings.add(Finding("RECEIPT_REF_MISMATCH", "/receipt_ref"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    state = candidate["tuning_state"]
    if state == "ERROR":
        findings.add(Finding("TUNING_ERROR", "/tuning_state"))
        return ValidationResult("ERROR", tuple(sorted(findings)))
    if state == "INCOMPLETE":
        findings.add(Finding("TUNING_INCOMPLETE", "/tuning_state"))

    search = candidate["search"]
    selection = candidate["selection"]
    reproducibility = candidate["reproducibility"]
    disclosure = candidate["disclosure"]
    assert isinstance(search, Mapping)
    assert isinstance(selection, Mapping)
    assert isinstance(reproducibility, Mapping)
    assert isinstance(disclosure, Mapping)

    method = search["method"]
    method_definition = search["method_definition"]
    random_seed = search["random_seed"]
    if method == "UNRESOLVED":
        findings.add(Finding("SEARCH_METHOD_UNRESOLVED", "/search/method"))
    elif method in STOCHASTIC_METHODS:
        if random_seed is None:
            findings.add(Finding("RANDOM_SEED_REQUIRED", "/search/random_seed"))
        if reproducibility["determinism_posture"] != "SEEDED_STOCHASTIC":
            findings.add(
                Finding(
                    "DETERMINISM_POSTURE_MISMATCH",
                    "/reproducibility/determinism_posture",
                )
            )
    if method == "CUSTOM" and method_definition is None:
        findings.add(
            Finding("CUSTOM_METHOD_DEFINITION_REQUIRED", "/search/method_definition")
        )
    if method not in {"CUSTOM", "UNRESOLVED"} and method_definition is not None:
        findings.add(Finding("METHOD_DEFINITION_FORBIDDEN", "/search/method_definition"))

    planned = search["planned_trials"]
    completed = search["completed_trials"]
    failed = search["failed_trials"]
    rank = selection["selected_trial_rank"]
    assert isinstance(planned, int) and isinstance(completed, int)
    assert isinstance(failed, int) and isinstance(rank, int)
    if completed + failed > planned:
        findings.add(Finding("TRIAL_ACCOUNTING_INVALID", "/search"))
    if completed == 0:
        findings.add(Finding("COMPLETED_TRIAL_REQUIRED", "/search/completed_trials"))
    if rank > completed:
        findings.add(Finding("SELECTED_TRIAL_RANK_INVALID", "/selection/selected_trial_rank"))
    if method == "MANUAL" and planned != 1:
        findings.add(Finding("MANUAL_TRIAL_COUNT_INVALID", "/search/planned_trials"))

    space = search["search_space"]
    selected = selection["selected_values"]
    space_names = _canonical_names(space)
    selected_names = _canonical_names(selected)
    if space_names != sorted(set(space_names or [])):
        findings.add(Finding("SEARCH_SPACE_NOT_CANONICAL", "/search/search_space"))
    if selected_names != sorted(set(selected_names or [])):
        findings.add(
            Finding("SELECTED_VALUES_NOT_CANONICAL", "/selection/selected_values")
        )
    if set(space_names or []) != set(selected_names or []):
        findings.add(
            Finding("SELECTED_PARAMETER_SET_MISMATCH", "/selection/selected_values")
        )
    space_by_name = {
        item["parameter_name"]: item for item in space if isinstance(item, Mapping)
    }
    for index, item in enumerate(selected):
        assert isinstance(item, Mapping)
        declared = space_by_name.get(item["parameter_name"])
        if declared and declared["value_kind"] != item["value_kind"]:
            findings.add(
                Finding("SELECTED_VALUE_KIND_MISMATCH", f"/selection/selected_values/{index}")
            )
    for index, parameter in enumerate(space):
        assert isinstance(parameter, Mapping)
        mode = parameter["selection_mode"]
        count = parameter["candidate_count"]
        invalid = (
            mode == "FIXED" and count != 1
        ) or (
            mode == "DISCRETE" and count is None
        ) or (
            mode in {"RANGE", "DISTRIBUTION"} and count is not None
        )
        if invalid:
            findings.add(
                Finding("DOMAIN_CANDIDATE_COUNT_INVALID", f"/search/search_space/{index}")
            )

    posture = reproducibility["determinism_posture"]
    if posture in {"UNKNOWN", "NONDETERMINISTIC"}:
        findings.add(
            Finding("REPRODUCIBILITY_UNRESOLVED", "/reproducibility/determinism_posture")
        )
    for field in ("evidence_bundle_refs", "review_record_refs"):
        if not _canonical_strings(disclosure[field]):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/disclosure/{field}"))
    if candidate["limitations"] != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    if candidate["intended_use"] == PUBLIC_USE:
        if disclosure["search_summary"] is None:
            findings.add(Finding("PUBLIC_SEARCH_SUMMARY_REQUIRED", "/disclosure/search_summary"))
        if not disclosure["evidence_bundle_refs"]:
            findings.add(Finding("PUBLIC_EVIDENCE_REQUIRED", "/disclosure/evidence_bundle_refs"))
        if not disclosure["review_record_refs"]:
            findings.add(Finding("PUBLIC_REVIEW_REQUIRED", "/disclosure/review_record_refs"))
        if disclosure["generalization_assessment_ref"] is None:
            findings.add(
                Finding(
                    "PUBLIC_GENERALIZATION_ASSESSMENT_REQUIRED",
                    "/disclosure/generalization_assessment_ref",
                )
            )

    ordered = tuple(sorted(findings))
    if not ordered:
        outcome = "PASS"
    elif all(item.code in ABSTAIN_CODES for item in ordered):
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, ordered)


def _merge_patch(target: object, patch: object) -> object:
    if not isinstance(target, Mapping) or not isinstance(patch, Mapping):
        return copy.deepcopy(patch)
    merged = copy.deepcopy(dict(target))
    for key, value in patch.items():
        merged[key] = _merge_patch(merged.get(key), value)
    return merged


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    profile_hash = compute_profile_hash(candidate)
    candidate["profile_spec_hash"] = profile_hash
    candidate["receipt_ref"] = expected_receipt_ref(profile_hash)
    overrides = entry.get("identity_overrides", {})
    assert isinstance(overrides, Mapping)
    candidate.update(overrides)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        expected_codes = entry["expected_codes"]
        results.append(
            {
                "name": entry["name"],
                "outcome": result.outcome,
                "codes": result.codes,
                "ok": result.outcome == entry["expected_outcome"]
                and result.codes == expected_codes,
            }
        )
    return results


def _print_result(result: ValidationResult) -> None:
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, sort_keys=True))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    if args.candidate is None:
        parser.error("candidate or --fixtures is required")
    candidate, findings = load_json_object(args.candidate)
    if findings:
        _print_result(ValidationResult("ERROR", tuple(findings)))
        return 1
    assert candidate is not None
    result = validate_candidate(candidate)
    _print_result(result)
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
