"""Validate bounded fixture-only model-evaluation split receipt candidates.

The validator checks split declarations, partition accounting, leakage-check
posture, disclosure, and deterministic identity only. It never reads dataset
rows, creates a split, trains or evaluates a model, resolves evidence, decides
policy or review, promotes, releases, deploys, or publishes.
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
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/model_evaluation_split_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/model_evaluation_split_receipt/cases.json"
)
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "EVALUATION_INCOMPLETE",
    "LEAKAGE_CHECK_UNRESOLVED",
    "PARTITION_UNRESOLVED",
    "REFERENCE_UNRESOLVED",
    "SPATIAL_HOLDOUT_UNRESOLVED",
    "SPLIT_METHOD_UNRESOLVED",
    "TEMPORAL_HOLDOUT_UNRESOLVED",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_DATASET_ACCESS",
    "NO_EVIDENCE_RESOLUTION",
    "NO_MODEL_EXECUTION",
    "NO_PUBLICATION_AUTHORITY",
]
EXPECTED_CHECK_TYPES = [
    "IDENTITY_OVERLAP",
    "GROUP_OVERLAP",
    "SPATIAL_OVERLAP",
    "TEMPORAL_ORDER",
]
VALID_PARTITION_ORDERS = [
    ["TRAIN", "TEST"],
    ["TRAIN", "VALIDATION", "TEST"],
]
STOCHASTIC_METHODS = {
    "RANDOM_HOLDOUT",
    "STRATIFIED_HOLDOUT",
    "K_FOLD",
}
SPATIAL_METHODS = {"SPATIAL_BLOCK", "SPATIOTEMPORAL_BLOCK"}
TEMPORAL_METHODS = {"TEMPORAL_BLOCK", "SPATIOTEMPORAL_BLOCK"}
PUBLIC_USE = "PUBLIC_EXPLANATION_SUPPORT_CANDIDATE"


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
    subject.pop("receipt_ref", None)
    return canonical_hash(subject)


def expected_receipt_ref(profile_hash: str) -> str:
    return "kfm:model-evaluation-split-receipt:" + profile_hash.removeprefix(
        "sha256:"
    )


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


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash = compute_profile_hash(candidate)
    if candidate.get("profile_spec_hash") != expected_hash:
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("receipt_ref") != expected_receipt_ref(expected_hash):
        findings.add(Finding("RECEIPT_REF_MISMATCH", "/receipt_ref"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    model = candidate["model"]
    dataset = candidate["dataset"]
    split = candidate["split"]
    partitions = candidate["partitions"]
    leakage_checks = candidate["leakage_checks"]
    evaluation = candidate["evaluation"]
    disclosure = candidate["disclosure"]
    limitations = candidate["limitations"]
    assert isinstance(model, Mapping)
    assert isinstance(dataset, Mapping)
    assert isinstance(split, Mapping)
    assert isinstance(partitions, list)
    assert isinstance(leakage_checks, list)
    assert isinstance(evaluation, Mapping)
    assert isinstance(disclosure, Mapping)

    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for field in ("stratification_fields", "grouping_fields"):
        if not _canonical_strings(split.get(field)):
            findings.add(Finding("FIELD_ARRAY_NOT_CANONICAL", f"/split/{field}"))
    if not _canonical_strings(evaluation.get("metric_refs")):
        findings.add(Finding("METRIC_REFERENCES_NOT_CANONICAL", "/evaluation/metric_refs"))
    for field in ("evidence_bundle_refs", "review_record_refs"):
        if not _canonical_strings(disclosure.get(field)):
            findings.add(
                Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/disclosure/{field}")
            )

    references: list[tuple[str, object]] = []
    for field in ("model_card", "model_artifact", "layer_manifest"):
        references.append((f"/model/{field}", model[field]))
    for field in ("source_snapshot", "split_manifest"):
        references.append((f"/dataset/{field}", dataset[field]))
    references.append(("/split/method_definition", split["method_definition"]))
    references.append(("/evaluation/evaluation_receipt", evaluation["evaluation_receipt"]))
    for path, reference in references:
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", path))

    evaluation_state = candidate.get("evaluation_state")
    if evaluation_state == "ERROR":
        findings.add(Finding("EVALUATION_ERROR", "/evaluation_state"))
        return sorted(findings)
    if evaluation_state == "INCOMPLETE":
        findings.add(Finding("EVALUATION_INCOMPLETE", "/evaluation_state"))
        return sorted(findings)

    method = split.get("method")
    random_seed = split.get("random_seed")
    stratification_fields = split.get("stratification_fields")
    grouping_fields = split.get("grouping_fields")
    assert isinstance(stratification_fields, list)
    assert isinstance(grouping_fields, list)
    spatial_holdout = split["spatial_holdout"]
    temporal_holdout = split["temporal_holdout"]
    assert isinstance(spatial_holdout, Mapping)
    assert isinstance(temporal_holdout, Mapping)

    if method == "UNRESOLVED":
        findings.add(Finding("SPLIT_METHOD_UNRESOLVED", "/split/method"))
    else:
        if method in STOCHASTIC_METHODS and random_seed is None:
            findings.add(Finding("RANDOM_SEED_REQUIRED", "/split/random_seed"))
        if method == "STRATIFIED_HOLDOUT" and not stratification_fields:
            findings.add(
                Finding(
                    "STRATIFICATION_FIELDS_REQUIRED",
                    "/split/stratification_fields",
                )
            )
        if method == "GROUP_HOLDOUT" and not grouping_fields:
            findings.add(
                Finding("GROUPING_FIELDS_REQUIRED", "/split/grouping_fields")
            )

    spatial_scope = spatial_holdout.get("scope")
    if spatial_scope == "UNRESOLVED":
        findings.add(
            Finding("SPATIAL_HOLDOUT_UNRESOLVED", "/split/spatial_holdout/scope")
        )
    elif method in SPATIAL_METHODS:
        if (
            spatial_scope not in {"BLOCKED", "LEAVE_REGION_OUT"}
            or spatial_holdout.get("geography_ref") is None
            or spatial_holdout.get("policy_ref") is None
        ):
            findings.add(
                Finding(
                    "SPATIAL_HOLDOUT_REQUIRED",
                    "/split/spatial_holdout",
                )
            )
    elif spatial_scope != "NOT_APPLICABLE":
        findings.add(
            Finding(
                "SPATIAL_HOLDOUT_METHOD_MISMATCH",
                "/split/spatial_holdout/scope",
            )
        )

    temporal_scope = temporal_holdout.get("scope")
    if temporal_scope == "UNRESOLVED":
        findings.add(
            Finding(
                "TEMPORAL_HOLDOUT_UNRESOLVED",
                "/split/temporal_holdout/scope",
            )
        )
    elif method in TEMPORAL_METHODS:
        if (
            temporal_scope not in {"FORWARD_CHAIN", "HOLDOUT_WINDOW"}
            or temporal_holdout.get("window_ref") is None
            or temporal_holdout.get("policy_ref") is None
        ):
            findings.add(
                Finding(
                    "TEMPORAL_HOLDOUT_REQUIRED",
                    "/split/temporal_holdout",
                )
            )
    elif temporal_scope != "NOT_APPLICABLE":
        findings.add(
            Finding(
                "TEMPORAL_HOLDOUT_METHOD_MISMATCH",
                "/split/temporal_holdout/scope",
            )
        )

    roles: list[str] = []
    artifact_refs: list[str] = []
    digests: list[str] = []
    partition_total = 0
    for index, partition in enumerate(partitions):
        assert isinstance(partition, Mapping)
        role = partition["role"]
        artifact_ref = partition["artifact_ref"]
        digest = partition["digest"]
        count = partition["count"]
        assert isinstance(role, str)
        assert isinstance(artifact_ref, str)
        assert isinstance(digest, str)
        assert isinstance(count, int)
        roles.append(role)
        artifact_refs.append(artifact_ref)
        digests.append(digest)
        partition_total += count
        if partition.get("resolution") == "UNRESOLVED":
            findings.add(Finding("PARTITION_UNRESOLVED", f"/partitions/{index}"))
        if stratification_fields and partition.get("class_distribution_ref") is None:
            findings.add(
                Finding(
                    "CLASS_DISTRIBUTION_REFERENCE_REQUIRED",
                    f"/partitions/{index}/class_distribution_ref",
                )
            )
        if method in SPATIAL_METHODS and partition.get("spatial_scope_ref") is None:
            findings.add(
                Finding(
                    "PARTITION_SPATIAL_SCOPE_REQUIRED",
                    f"/partitions/{index}/spatial_scope_ref",
                )
            )
        if method in TEMPORAL_METHODS and partition.get("temporal_scope_ref") is None:
            findings.add(
                Finding(
                    "PARTITION_TEMPORAL_SCOPE_REQUIRED",
                    f"/partitions/{index}/temporal_scope_ref",
                )
            )
    if roles not in VALID_PARTITION_ORDERS:
        findings.add(Finding("PARTITION_ORDER_INVALID", "/partitions"))
    if len(artifact_refs) != len(set(artifact_refs)):
        findings.add(Finding("PARTITION_REFERENCE_DUPLICATE", "/partitions"))
    if len(digests) != len(set(digests)):
        findings.add(Finding("PARTITION_DIGEST_DUPLICATE", "/partitions"))
    if partition_total != dataset.get("total_count"):
        findings.add(Finding("PARTITION_COUNT_MISMATCH", "/dataset/total_count"))

    check_types: list[str] = []
    check_status: dict[str, str] = {}
    for index, check in enumerate(leakage_checks):
        assert isinstance(check, Mapping)
        check_type = check["check_type"]
        status = check["status"]
        evidence_ref = check["evidence_ref"]
        assert isinstance(check_type, str)
        assert isinstance(status, str)
        check_types.append(check_type)
        check_status[check_type] = status
        if status == "UNRESOLVED":
            findings.add(
                Finding(
                    "LEAKAGE_CHECK_UNRESOLVED",
                    f"/leakage_checks/{index}/status",
                )
            )
            if evidence_ref is not None:
                findings.add(
                    Finding(
                        "UNRESOLVED_CHECK_EVIDENCE_PRESENT",
                        f"/leakage_checks/{index}/evidence_ref",
                    )
                )
        elif status == "NOT_APPLICABLE":
            if evidence_ref is not None:
                findings.add(
                    Finding(
                        "NOT_APPLICABLE_CHECK_EVIDENCE_PRESENT",
                        f"/leakage_checks/{index}/evidence_ref",
                    )
                )
        else:
            if evidence_ref is None:
                findings.add(
                    Finding(
                        "LEAKAGE_CHECK_EVIDENCE_REQUIRED",
                        f"/leakage_checks/{index}/evidence_ref",
                    )
                )
            if status == "FAIL":
                findings.add(
                    Finding(
                        "LEAKAGE_CHECK_FAILED",
                        f"/leakage_checks/{index}/status",
                    )
                )
    if check_types != EXPECTED_CHECK_TYPES:
        findings.add(Finding("LEAKAGE_CHECK_ORDER_INVALID", "/leakage_checks"))
    if check_status.get("IDENTITY_OVERLAP") == "NOT_APPLICABLE":
        findings.add(
            Finding("IDENTITY_OVERLAP_CHECK_REQUIRED", "/leakage_checks/0")
        )
    if grouping_fields and check_status.get("GROUP_OVERLAP") == "NOT_APPLICABLE":
        findings.add(Finding("GROUP_OVERLAP_CHECK_REQUIRED", "/leakage_checks/1"))
    if method in SPATIAL_METHODS and check_status.get("SPATIAL_OVERLAP") == "NOT_APPLICABLE":
        findings.add(
            Finding("SPATIAL_OVERLAP_CHECK_REQUIRED", "/leakage_checks/2")
        )
    if method in TEMPORAL_METHODS and check_status.get("TEMPORAL_ORDER") == "NOT_APPLICABLE":
        findings.add(Finding("TEMPORAL_ORDER_CHECK_REQUIRED", "/leakage_checks/3"))

    if candidate.get("intended_use") == PUBLIC_USE:
        note = disclosure.get("holdout_scope_note")
        if not isinstance(note, str) or note.strip() != note:
            findings.add(
                Finding(
                    "PUBLIC_HOLDOUT_SCOPE_NOTE_REQUIRED",
                    "/disclosure/holdout_scope_note",
                )
            )
        if not disclosure.get("evidence_bundle_refs"):
            findings.add(
                Finding(
                    "PUBLIC_EVIDENCE_REFERENCE_REQUIRED",
                    "/disclosure/evidence_bundle_refs",
                )
            )
        if not disclosure.get("review_record_refs"):
            findings.add(
                Finding(
                    "PUBLIC_REVIEW_REFERENCE_REQUIRED",
                    "/disclosure/review_record_refs",
                )
            )
        if evaluation.get("generalization_assessment_ref") is None:
            findings.add(
                Finding(
                    "PUBLIC_GENERALIZATION_ASSESSMENT_REQUIRED",
                    "/evaluation/generalization_assessment_ref",
                )
            )
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
    profile_hash = compute_profile_hash(candidate)
    candidate["profile_spec_hash"] = profile_hash
    candidate["receipt_ref"] = expected_receipt_ref(profile_hash)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    if entry.get("tamper") == "receipt_ref":
        candidate["receipt_ref"] = "kfm:model-evaluation-split-receipt:" + "f" * 64
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
        description="Validate fixture-only model-evaluation split receipts."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, load_findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(load_findings))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "findings": [
                    {"code": finding.code, "field": finding.field}
                    for finding in result.findings
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
