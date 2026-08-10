"""Validate fixture-only predictive layer generalization assessments.

The validator checks declaration coherence only. It does not execute or
evaluate a model, recompute metrics, authenticate referenced records, select
scientific thresholds, decide policy or review, release, deploy, publish, or
authorize public interpretation.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/predictive_layer_generalization_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/predictive_layer_generalization_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CROSS_VALIDATION_NOT_PERFORMED",
    "CROSS_VALIDATION_UNKNOWN",
    "EVALUATION_INCOMPLETE",
    "EVALUATION_UNKNOWN",
    "GENERALIZATION_LIMITED",
    "GENERALIZATION_UNKNOWN",
    "OVERFITTING_RISK_PRESENT",
    "OVERFITTING_UNKNOWN",
    "REFERENCE_UNRESOLVED",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_METRIC_RECOMPUTATION",
    "NO_MODEL_EXECUTION",
    "NO_PUBLICATION_AUTHORITY",
]
PUBLIC_USES = {"PUBLIC_INTERPRETATION", "POLICY_CONTEXT"}


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


def _unresolved_evaluation_shape(evaluation: Mapping[str, object]) -> bool:
    cross = evaluation.get("cross_validation")
    assert isinstance(cross, Mapping)
    return (
        evaluation.get("split_strategy") == "UNKNOWN"
        and evaluation.get("training_dataset_ref") is None
        and evaluation.get("evaluation_dataset_ref") is None
        and evaluation.get("data_independence") == "UNKNOWN"
        and cross.get("status") == "UNKNOWN"
        and cross.get("fold_count") is None
        and cross.get("repeat_count") is None
        and cross.get("metric_refs") == []
        and evaluation.get("overfitting_label") == "UNKNOWN"
        and evaluation.get("generalization_label") == "UNKNOWN"
        and evaluation.get("validation_report_refs") == []
        and evaluation.get("limitation_refs") == []
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    limitations = candidate["limitations"]
    evaluation = candidate["evaluation"]
    disclosure = candidate["disclosure"]
    assert isinstance(evaluation, Mapping)
    assert isinstance(disclosure, Mapping)
    cross = evaluation["cross_validation"]
    assert isinstance(cross, Mapping)

    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for path, value in (
        ("/evaluation/cross_validation/metric_refs", cross.get("metric_refs")),
        ("/evaluation/validation_report_refs", evaluation.get("validation_report_refs")),
        ("/evaluation/limitation_refs", evaluation.get("limitation_refs")),
        ("/disclosure/review_record_refs", disclosure.get("review_record_refs")),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", path))

    for name in ("model_card", "model_run_receipt", "analytic_output_disclosure"):
        reference = candidate[name]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    state = evaluation.get("state")
    if state == "ERROR":
        findings.add(Finding("EVALUATION_ERROR", "/evaluation/state"))
        return sorted(findings)
    if state == "INCOMPLETE":
        findings.add(Finding("EVALUATION_INCOMPLETE", "/evaluation/state"))
        if not _unresolved_evaluation_shape(evaluation):
            findings.add(Finding("EVALUATION_STATE_INCOHERENT", "/evaluation"))
        return sorted(findings)
    if state == "UNKNOWN":
        findings.add(Finding("EVALUATION_UNKNOWN", "/evaluation/state"))
        if not _unresolved_evaluation_shape(evaluation):
            findings.add(Finding("EVALUATION_STATE_INCOHERENT", "/evaluation"))
        return sorted(findings)

    training_ref = evaluation.get("training_dataset_ref")
    evaluation_ref = evaluation.get("evaluation_dataset_ref")
    if training_ref is None or evaluation_ref is None:
        findings.add(Finding("DATASET_REFERENCE_REQUIRED", "/evaluation"))
    elif training_ref == evaluation_ref:
        findings.add(Finding("EVALUATION_DATA_NOT_SEPARATE", "/evaluation/evaluation_dataset_ref"))
    if evaluation.get("split_strategy") == "UNKNOWN" or evaluation.get("data_independence") == "UNKNOWN":
        findings.add(Finding("COMPLETE_EVALUATION_INCOHERENT", "/evaluation"))
    if evaluation.get("data_independence") == "NOT_INDEPENDENT":
        findings.add(Finding("DATA_INDEPENDENCE_DENIED", "/evaluation/data_independence"))

    cross_status = cross.get("status")
    if cross_status == "PERFORMED":
        if (
            cross.get("fold_count") is None
            or cross.get("repeat_count") is None
            or not cross.get("metric_refs")
            or not evaluation.get("validation_report_refs")
        ):
            findings.add(Finding("CROSS_VALIDATION_EVIDENCE_INCOMPLETE", "/evaluation/cross_validation"))
    elif cross_status == "NOT_APPLICABLE":
        if (
            cross.get("fold_count") is not None
            or cross.get("repeat_count") is not None
            or cross.get("metric_refs")
            or not evaluation.get("validation_report_refs")
            or not evaluation.get("limitation_refs")
        ):
            findings.add(Finding("CROSS_VALIDATION_NOT_APPLICABLE_INCOHERENT", "/evaluation/cross_validation"))
    elif cross_status == "NOT_PERFORMED":
        if cross.get("fold_count") is not None or cross.get("repeat_count") is not None or cross.get("metric_refs"):
            findings.add(Finding("CROSS_VALIDATION_STATUS_INCOHERENT", "/evaluation/cross_validation"))
        findings.add(Finding("CROSS_VALIDATION_NOT_PERFORMED", "/evaluation/cross_validation/status"))
    elif cross_status == "UNKNOWN":
        if cross.get("fold_count") is not None or cross.get("repeat_count") is not None or cross.get("metric_refs"):
            findings.add(Finding("CROSS_VALIDATION_STATUS_INCOHERENT", "/evaluation/cross_validation"))
        findings.add(Finding("CROSS_VALIDATION_UNKNOWN", "/evaluation/cross_validation/status"))

    overfitting = evaluation.get("overfitting_label")
    generalization = evaluation.get("generalization_label")
    if overfitting == "UNKNOWN":
        findings.add(Finding("OVERFITTING_UNKNOWN", "/evaluation/overfitting_label"))
    if generalization == "UNKNOWN":
        findings.add(Finding("GENERALIZATION_UNKNOWN", "/evaluation/generalization_label"))
    if overfitting == "DETECTED" and generalization == "SUPPORTED":
        findings.add(Finding("GENERALIZATION_LABEL_INCOHERENT", "/evaluation/generalization_label"))

    if candidate.get("intended_use") in PUBLIC_USES:
        if not disclosure.get("review_record_refs"):
            findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/disclosure/review_record_refs"))
        if disclosure.get("evidence_drawer_section_ref") is None:
            findings.add(Finding("EVIDENCE_DRAWER_SECTION_REQUIRED", "/disclosure/evidence_drawer_section_ref"))
        caveat = disclosure.get("public_interpretation_caveat")
        if caveat is None or not isinstance(caveat, str) or caveat.strip() != caveat:
            findings.add(Finding("PUBLIC_INTERPRETATION_CAVEAT_REQUIRED", "/disclosure/public_interpretation_caveat"))
        if overfitting == "RISK_PRESENT":
            findings.add(Finding("OVERFITTING_RISK_PRESENT", "/evaluation/overfitting_label"))
        elif overfitting == "DETECTED":
            findings.add(Finding("PUBLIC_OVERFITTING_DENIED", "/evaluation/overfitting_label"))
        if generalization == "LIMITED":
            findings.add(Finding("GENERALIZATION_LIMITED", "/evaluation/generalization_label"))
        elif generalization == "NOT_SUPPORTED":
            findings.add(Finding("PUBLIC_GENERALIZATION_DENIED", "/evaluation/generalization_label"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "EVALUATION_ERROR" in codes:
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
    parser = argparse.ArgumentParser(description="Validate fixture-only predictive layer generalization assessments.")
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
