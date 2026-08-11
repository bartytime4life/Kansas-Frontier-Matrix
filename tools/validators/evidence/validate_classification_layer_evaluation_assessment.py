"""Validate fixture-only classification-layer evaluation assessments.

The validator checks declaration and confusion-matrix arithmetic coherence only.
It does not run a model, authenticate ground truth or references, select a
scientific threshold, decide policy or review, release, deploy, publish, or
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/classification_layer_evaluation_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/classification_layer_evaluation_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
PUBLIC_USES = {"PUBLIC_INTERPRETATION", "POLICY_CONTEXT"}
EXPECTED_LIMITATIONS = [
    "ARITHMETIC_CHECK_ONLY",
    "DECLARATION_ONLY",
    "NO_EVIDENCE_RESOLUTION",
    "NO_MODEL_EXECUTION",
    "NO_PUBLICATION_AUTHORITY",
    "NO_SCIENTIFIC_THRESHOLD",
]
ABSTAIN_CODES = {
    "EVALUATION_INCOMPLETE",
    "EVALUATION_METHOD_UNKNOWN",
    "EVALUATION_UNKNOWN",
    "PUBLIC_EVALUATION_SUPPORT_INSUFFICIENT",
    "REFERENCE_UNRESOLVED",
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


def _unresolved_evaluation_shape(evaluation: Mapping[str, object]) -> bool:
    return (
        evaluation.get("method") == "UNKNOWN"
        and evaluation.get("evaluation_dataset_ref") is None
        and evaluation.get("ground_truth_posture") == "UNKNOWN"
        and evaluation.get("class_labels") == []
        and evaluation.get("confusion_matrix") is None
        and evaluation.get("reported_metrics") is None
        and evaluation.get("comparable_evaluation_refs") == []
        and evaluation.get("limitation_refs") == []
    )


def _ratio(numerator: int, denominator: int) -> float | None:
    return None if denominator == 0 else numerator / denominator


def _f1(precision: float | None, recall: float | None) -> float | None:
    if precision is None or recall is None or precision + recall == 0:
        return None
    return 2 * precision * recall / (precision + recall)


def _mean(values: list[float | None]) -> float | None:
    finite = [value for value in values if value is not None]
    return None if not finite else sum(finite) / len(finite)


def _metric_equal(declared: object, computed: float | None) -> bool:
    if computed is None:
        return declared is None
    return isinstance(declared, (int, float)) and not isinstance(declared, bool) and math.isclose(
        float(declared), computed, rel_tol=1e-9, abs_tol=1e-9
    )


def _matrix_findings(evaluation: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    labels = evaluation["class_labels"]
    matrix = evaluation["confusion_matrix"]
    metrics = evaluation["reported_metrics"]
    assert isinstance(labels, list)
    assert isinstance(matrix, Mapping)
    assert isinstance(metrics, Mapping)
    rows = matrix["rows"]
    assert isinstance(rows, list)

    actual_labels = [row["actual_label"] for row in rows]
    if actual_labels != labels:
        findings.add(Finding("MATRIX_ACTUAL_LABEL_CLOSURE_MISMATCH", "/evaluation/confusion_matrix/rows"))
    for index, row in enumerate(rows):
        predictions = row["predictions"]
        predicted_labels = [item["predicted_label"] for item in predictions]
        if predicted_labels != labels:
            findings.add(Finding("MATRIX_PREDICTED_LABEL_CLOSURE_MISMATCH", f"/evaluation/confusion_matrix/rows/{index}/predictions"))
    per_class = metrics["per_class"]
    metric_labels = [item["label"] for item in per_class]
    if metric_labels != labels:
        findings.add(Finding("METRIC_CLASS_LABEL_CLOSURE_MISMATCH", "/evaluation/reported_metrics/per_class"))
    if findings:
        return sorted(findings)

    counts = [
        [int(item["count"]) for item in row["predictions"]]
        for row in rows
    ]
    sample_count = sum(sum(row) for row in counts)
    correct_count = sum(counts[index][index] for index in range(len(labels)))
    if metrics["sample_count"] != sample_count:
        findings.add(Finding("SAMPLE_COUNT_MISMATCH", "/evaluation/reported_metrics/sample_count"))
    if metrics["correct_count"] != correct_count:
        findings.add(Finding("CORRECT_COUNT_MISMATCH", "/evaluation/reported_metrics/correct_count"))

    precisions: list[float | None] = []
    recalls: list[float | None] = []
    f1_values: list[float | None] = []
    for index, declared in enumerate(per_class):
        support = sum(counts[index])
        predicted = sum(row[index] for row in counts)
        true_positive = counts[index][index]
        precision = _ratio(true_positive, predicted)
        recall = _ratio(true_positive, support)
        f1 = _f1(precision, recall)
        precisions.append(precision)
        recalls.append(recall)
        f1_values.append(f1)
        if (
            declared["support"] != support
            or not _metric_equal(declared["precision"], precision)
            or not _metric_equal(declared["recall"], recall)
            or not _metric_equal(declared["f1"], f1)
        ):
            findings.add(Finding("CLASS_METRIC_MISMATCH", f"/evaluation/reported_metrics/per_class/{index}"))

    if not _metric_equal(metrics["overall_accuracy"], _ratio(correct_count, sample_count)):
        findings.add(Finding("OVERALL_ACCURACY_MISMATCH", "/evaluation/reported_metrics/overall_accuracy"))
    if not _metric_equal(metrics["macro_precision"], _mean(precisions)):
        findings.add(Finding("MACRO_PRECISION_MISMATCH", "/evaluation/reported_metrics/macro_precision"))
    if not _metric_equal(metrics["macro_recall"], _mean(recalls)):
        findings.add(Finding("MACRO_RECALL_MISMATCH", "/evaluation/reported_metrics/macro_recall"))
    if not _metric_equal(metrics["macro_f1"], _mean(f1_values)):
        findings.add(Finding("MACRO_F1_MISMATCH", "/evaluation/reported_metrics/macro_f1"))
    return sorted(findings)


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
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for path, value in (
        ("/evaluation/class_labels", evaluation.get("class_labels")),
        ("/evaluation/comparable_evaluation_refs", evaluation.get("comparable_evaluation_refs")),
        ("/evaluation/limitation_refs", evaluation.get("limitation_refs")),
        ("/disclosure/validation_report_refs", disclosure.get("validation_report_refs")),
        ("/disclosure/review_record_refs", disclosure.get("review_record_refs")),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", path))

    for name in (
        "model_card",
        "model_run_receipt",
        "evidence_bundle",
        "predictive_generalization_assessment",
    ):
        reference = candidate[name]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/{name}/resolution"))

    state = evaluation.get("state")
    if state == "ERROR":
        findings.add(Finding("EVALUATION_ERROR", "/evaluation/state"))
        return sorted(findings)
    if state in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"EVALUATION_{state}", "/evaluation/state"))
        if not _unresolved_evaluation_shape(evaluation):
            findings.add(Finding("EVALUATION_STATE_INCOHERENT", "/evaluation"))
        return sorted(findings)

    method = evaluation.get("method")
    matrix = evaluation.get("confusion_matrix")
    metrics = evaluation.get("reported_metrics")
    comparable = evaluation.get("comparable_evaluation_refs")
    ground_truth = evaluation.get("ground_truth_posture")
    dataset_ref = evaluation.get("evaluation_dataset_ref")
    limitation_refs = evaluation.get("limitation_refs")

    if method == "SUPERVISED_CONFUSION_MATRIX":
        if dataset_ref is None or matrix is None or metrics is None or comparable:
            findings.add(Finding("CONFUSION_MATRIX_PROFILE_INCOMPLETE", "/evaluation"))
        elif ground_truth != "VERIFIED_REFERENCE":
            findings.add(Finding("VERIFIED_GROUND_TRUTH_REQUIRED", "/evaluation/ground_truth_posture"))
        else:
            findings.update(_matrix_findings(evaluation))
    elif method == "COMPARABLE_EVALUATION":
        if matrix is not None or metrics is not None or not comparable or not limitation_refs or ground_truth not in {"VERIFIED_REFERENCE", "PROXY_LABELS"}:
            findings.add(Finding("COMPARABLE_EVALUATION_INCOHERENT", "/evaluation"))
    elif method == "WEAKLY_SUPERVISED":
        if matrix is not None or metrics is not None or not comparable or not limitation_refs or ground_truth != "PROXY_LABELS":
            findings.add(Finding("WEAK_EVALUATION_INCOHERENT", "/evaluation"))
    elif method == "UNSUPERVISED":
        if matrix is not None or metrics is not None or comparable or not limitation_refs or ground_truth != "NO_LABELED_REFERENCE":
            findings.add(Finding("UNSUPERVISED_EVALUATION_INCOHERENT", "/evaluation"))
    elif method == "UNKNOWN":
        findings.add(Finding("EVALUATION_METHOD_UNKNOWN", "/evaluation/method"))

    if candidate.get("intended_use") in PUBLIC_USES:
        if method in {"WEAKLY_SUPERVISED", "UNSUPERVISED", "UNKNOWN"}:
            findings.add(Finding("PUBLIC_EVALUATION_SUPPORT_INSUFFICIENT", "/evaluation/method"))
        if not disclosure.get("review_record_refs"):
            findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/disclosure/review_record_refs"))
        if disclosure.get("evidence_drawer_section_ref") is None:
            findings.add(Finding("EVIDENCE_DRAWER_SECTION_REQUIRED", "/disclosure/evidence_drawer_section_ref"))
        caveat = disclosure.get("public_interpretation_caveat")
        if caveat is None or not isinstance(caveat, str) or caveat.strip() != caveat:
            findings.add(Finding("PUBLIC_INTERPRETATION_CAVEAT_REQUIRED", "/disclosure/public_interpretation_caveat"))
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
    parser = argparse.ArgumentParser(description="Validate fixture-only classification-layer evaluation assessments.")
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
