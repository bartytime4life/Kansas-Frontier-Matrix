"""Pure semantic checks for fixture-only k-anonymity assessments."""

from __future__ import annotations

import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, compute_spec_hash, load_json_file

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/k_anonymity_assessment.schema.json"
MAX_SCHEMA_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str
    severity: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    assessment_id: str | None = None
    spec_hash: str | None = None


def pointer(parts: Sequence[object]) -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped) if escaped else "/"


def identity_subject(candidate: Mapping[str, object]) -> dict[str, object]:
    return {key: value for key, value in candidate.items() if key not in {"assessment_id", "spec_hash"}}


def refresh_identity(document: dict[str, object]) -> None:
    digest = compute_spec_hash(identity_subject(document))
    document["spec_hash"] = digest
    document["assessment_id"] = f"kfm:k-anonymity-assessment:{digest}"


def outcome(findings: set[Finding]) -> str:
    severities = {finding.severity for finding in findings}
    return "ERROR" if "ERROR" in severities else "DENY" if "DENY" in severities else "ABSTAIN" if "ABSTAIN" in severities else "PASS"


def schema_findings(candidate: Mapping[str, object]) -> set[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return {Finding("KANON_SCHEMA_UNAVAILABLE", "/", "ERROR")}
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda error: (pointer(tuple(error.absolute_path)), str(error.validator or "schema")))
    findings = {Finding("KANON_SCHEMA_INVALID", pointer(tuple(error.absolute_path)), "DENY") for error in errors}
    if truncated:
        findings.add(Finding("KANON_SCHEMA_FINDINGS_TRUNCATED", "/", "ERROR"))
    return findings


def semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    add = lambda code, path, severity: findings.add(Finding(code, path, severity))
    expected_hash = compute_spec_hash(identity_subject(candidate))
    if candidate["spec_hash"] != expected_hash:
        add("KANON_SPEC_HASH_MISMATCH", "/spec_hash", "DENY")
    if candidate["assessment_id"] != f"kfm:k-anonymity-assessment:{expected_hash}":
        add("KANON_ASSESSMENT_ID_MISMATCH", "/assessment_id", "DENY")

    quasi = candidate["quasi_identifiers"]
    policy = candidate["policy_selection"]
    classes = candidate["equivalence_classes"]
    generalization = candidate["generalization"]
    suppression = candidate["suppression"]
    subject = candidate["subject"]
    assessment = candidate["assessment"]
    assert isinstance(quasi, list) and isinstance(policy, Mapping) and isinstance(classes, list)
    assert isinstance(generalization, Mapping) and isinstance(suppression, Mapping)
    assert isinstance(subject, Mapping) and isinstance(assessment, Mapping)

    if not quasi:
        add("KANON_QUASI_IDENTIFIERS_REQUIRED", "/quasi_identifiers", "DENY")
    if not candidate["evidence_refs"]:
        add("KANON_SUPPORT_INCOMPLETE", "/evidence_refs", "ABSTAIN")
    if not policy["policy_decision_refs"]:
        add("KANON_SUPPORT_INCOMPLETE", "/policy_selection/policy_decision_refs", "ABSTAIN")

    keys = [item["key_digest"] for item in classes]
    if keys != sorted(keys):
        add("KANON_CLASS_ORDER_INVALID", "/equivalence_classes", "DENY")
    if len(keys) != len(set(keys)):
        add("KANON_DUPLICATE_CLASS_KEY", "/equivalence_classes", "DENY")
    selected_k = policy["selected_k"]
    for index, item in enumerate(classes):
        if item["record_count"] < selected_k:
            add("KANON_THRESHOLD_NOT_MET", f"/equivalence_classes/{index}/record_count", "DENY")

    class_total = sum(item["record_count"] for item in classes)
    if class_total + suppression["record_count"] != subject["row_count"]:
        add("KANON_ROW_COUNT_CLOSURE_INVALID", "/subject/row_count", "ERROR")
    if assessment["class_count"] != len(classes):
        add("KANON_CLASS_COUNT_MISMATCH", "/assessment/class_count", "ERROR")
    if assessment["min_class_size"] != min(item["record_count"] for item in classes):
        add("KANON_MIN_CLASS_SIZE_MISMATCH", "/assessment/min_class_size", "ERROR")

    steps = generalization["steps"]
    if generalization["applied"] and not steps:
        add("KANON_GENERALIZATION_UNEXPLAINED", "/generalization/steps", "ERROR")
    if not generalization["applied"] and steps:
        add("KANON_GENERALIZATION_STATE_INVALID", "/generalization/applied", "ERROR")
    for index, step in enumerate(steps):
        if step["field"] not in set(quasi):
            add("KANON_GENERALIZATION_FIELD_INVALID", f"/generalization/steps/{index}/field", "DENY")

    count = suppression["record_count"]
    reasons = suppression["reasons"]
    receipts = suppression["transform_receipt_refs"]
    if count > 0 and not reasons:
        add("KANON_SUPPRESSION_UNEXPLAINED", "/suppression/reasons", "ERROR")
    if count > 0 and not receipts:
        add("KANON_SUPPRESSION_UNEXPLAINED", "/suppression/transform_receipt_refs", "ERROR")
    if count == 0 and (reasons or receipts):
        add("KANON_SUPPRESSION_STATE_INVALID", "/suppression", "ERROR")
    return findings


def validate_document(candidate: object) -> ValidationResult:
    if not isinstance(candidate, Mapping):
        finding = Finding("KANON_ROOT_TYPE", "/", "DENY")
        return ValidationResult("DENY", (finding,))
    findings = schema_findings(candidate)
    if not findings:
        findings = semantic_findings(candidate)
    return ValidationResult(
        outcome(findings),
        tuple(sorted(findings)),
        candidate.get("assessment_id") if isinstance(candidate.get("assessment_id"), str) else None,
        candidate.get("spec_hash") if isinstance(candidate.get("spec_hash"), str) else None,
    )
