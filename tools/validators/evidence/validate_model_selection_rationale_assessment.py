"""Validate fixture-only model-selection rationale assessments.

The validator checks declared linkage and coherence only. It does not execute,
compare, rank, evaluate, approve, register, release, deploy, or publish a model
and grants no evidence, policy, review, lifecycle, or public-use authority.
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
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/model_selection_rationale_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/model_selection_rationale_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:model-selection:"
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_MODEL_EXECUTION_OR_RANKING",
    "NO_PERFORMANCE_OR_SCIENTIFIC_VALIDATION",
    "NO_POLICY_OR_REVIEW_AUTHORITY",
    "NO_RELEASE_DEPLOYMENT_OR_PUBLICATION_AUTHORITY",
]
ABSTAIN_CODES = {
    "CLAIM_ROLE_UNRESOLVED",
    "CONSEQUENCE_UNRESOLVED",
    "INTERPRETABILITY_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SELECTION_UNRESOLVED",
    "SENSITIVE_DATA_UNRESOLVED",
    "TASK_TYPE_UNRESOLVED",
}
OPAQUE_FAMILIES = {"ENSEMBLE", "KERNEL", "NEURAL_NETWORK"}
DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "kfm://raw/",
    "kfm://work/",
    "kfm://quarantine/",
)
QUERY_MARKERS = ("match (", "select *", "sparql ", "cypher:")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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
    subject.pop("assessment_id", None)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def compute_assessment_id(candidate: Mapping[str, object]) -> str:
    return IDENTITY_PREFIX + compute_profile_hash(candidate).split(":", 1)[1][:24]


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


def _walk_strings(value: object, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path or "/", value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_strings(item, f"{path}/{index}")
    elif isinstance(value, Mapping):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from _walk_strings(value[key], f"{path}/{escaped}")


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    problem = candidate["problem"]
    data = candidate["data_characteristics"]
    candidates = candidate["candidates"]
    selection = candidate["selection"]
    governance = candidate["governance"]
    assert all(isinstance(item, Mapping) for item in (problem, data, selection, governance))
    assert isinstance(candidates, list)

    for path, value in (
        ("/data_characteristics/characteristic_refs", data["characteristic_refs"]),
        ("/selection/problem_fit_refs", selection["problem_fit_refs"]),
        ("/selection/data_fit_refs", selection["data_fit_refs"]),
        ("/selection/decision_reason_codes", selection["decision_reason_codes"]),
        ("/governance/evidence_refs", governance["evidence_refs"]),
        ("/governance/review_record_refs", governance["review_record_refs"]),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCES_NOT_CANONICAL", path))

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    for path, text in _walk_strings(candidate):
        lowered = text.lower()
        if any(marker in lowered for marker in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))

    candidate_ids: list[str] = []
    candidate_by_id: dict[str, Mapping[str, object]] = {}
    for index, model_candidate in enumerate(candidates):
        assert isinstance(model_candidate, Mapping)
        candidate_id = model_candidate["candidate_id"]
        assert isinstance(candidate_id, str)
        candidate_ids.append(candidate_id)
        candidate_by_id.setdefault(candidate_id, model_candidate)
        if not _canonical_strings(model_candidate["exclusion_codes"]):
            findings.add(Finding("EXCLUSION_CODES_NOT_CANONICAL", f"/candidates/{index}/exclusion_codes"))
        if model_candidate["eligible"] and model_candidate["evaluation_receipt_ref"] is None:
            findings.add(Finding("ELIGIBLE_EVALUATION_REQUIRED", f"/candidates/{index}/evaluation_receipt_ref"))
        if not model_candidate["eligible"] and not model_candidate["exclusion_codes"]:
            findings.add(Finding("INELIGIBLE_REASON_REQUIRED", f"/candidates/{index}/exclusion_codes"))
    if candidate_ids != sorted(set(candidate_ids)):
        findings.add(Finding("CANDIDATES_NOT_CANONICAL", "/candidates"))

    unresolved_fields = (
        ("task_type", "UNRESOLVED", "TASK_TYPE_UNRESOLVED"),
        ("claim_role", "UNRESOLVED", "CLAIM_ROLE_UNRESOLVED"),
        ("consequence_level", "UNRESOLVED", "CONSEQUENCE_UNRESOLVED"),
        ("interpretability_requirement", "UNRESOLVED", "INTERPRETABILITY_UNRESOLVED"),
    )
    for field, unresolved, code in unresolved_fields:
        if problem[field] == unresolved:
            findings.add(Finding(code, f"/problem/{field}"))
    if problem["task_type"] != "UNRESOLVED" and problem["problem_statement_ref"] is None:
        findings.add(Finding("PROBLEM_STATEMENT_REQUIRED", "/problem/problem_statement_ref"))
    if problem["claim_role"] in {"CAUSAL", "REGULATORY"}:
        findings.add(Finding("CAUSAL_OR_REGULATORY_AUTHORITY_DENIED", "/problem/claim_role"))

    if data["sensitive_data_state"] == "UNKNOWN":
        findings.add(Finding("SENSITIVE_DATA_UNRESOLVED", "/data_characteristics/sensitive_data_state"))
    elif data["sensitive_data_state"] == "PRESENT" and selection["policy_consequence_ref"] is None:
        findings.add(Finding("SENSITIVE_DATA_POLICY_REFERENCE_REQUIRED", "/selection/policy_consequence_ref"))

    selected_id = selection["selected_candidate_id"]
    baseline_id = selection["baseline_candidate_id"]
    selected = candidate_by_id.get(selected_id) if isinstance(selected_id, str) else None
    baseline = candidate_by_id.get(baseline_id) if isinstance(baseline_id, str) else None
    if selected_id is None and baseline_id is None:
        findings.add(Finding("SELECTION_UNRESOLVED", "/selection"))
    elif selected_id is None or baseline_id is None:
        findings.add(Finding("SELECTION_REFERENCE_INCOHERENT", "/selection"))
    else:
        if selected is None:
            findings.add(Finding("SELECTED_CANDIDATE_UNKNOWN", "/selection/selected_candidate_id"))
        elif not selected["eligible"]:
            findings.add(Finding("SELECTED_CANDIDATE_INELIGIBLE", "/selection/selected_candidate_id"))
        if baseline is None:
            findings.add(Finding("BASELINE_CANDIDATE_UNKNOWN", "/selection/baseline_candidate_id"))
        elif not baseline["eligible"]:
            findings.add(Finding("BASELINE_CANDIDATE_INELIGIBLE", "/selection/baseline_candidate_id"))
        if selected_id == baseline_id:
            findings.add(Finding("BASELINE_MUST_DIFFER", "/selection/baseline_candidate_id"))

        if not selection["problem_fit_refs"]:
            findings.add(Finding("PROBLEM_FIT_REFERENCE_REQUIRED", "/selection/problem_fit_refs"))
        if not selection["data_fit_refs"]:
            findings.add(Finding("DATA_FIT_REFERENCE_REQUIRED", "/selection/data_fit_refs"))
        if not selection["decision_reason_codes"]:
            findings.add(Finding("DECISION_REASON_REQUIRED", "/selection/decision_reason_codes"))
        if not selection["performance_not_sole_basis"]:
            findings.add(Finding("PERFORMANCE_ONLY_SELECTION_DENIED", "/selection/performance_not_sole_basis"))

        missing_data_refs = any(
            data[name] is None
            for name in ("training_population_ref", "feature_manifest_ref", "data_quality_ref")
        ) or not data["characteristic_refs"]
        if missing_data_refs:
            findings.add(Finding("DATA_CHARACTERISTIC_REFERENCE_REQUIRED", "/data_characteristics"))
        missing_governance_refs = any(
            governance[name] is None
            for name in ("model_card_ref", "training_receipt_ref", "evaluation_split_ref")
        )
        if missing_governance_refs:
            findings.add(Finding("GOVERNANCE_REFERENCE_REQUIRED", "/governance"))
        if not governance["evidence_refs"]:
            findings.add(Finding("EVIDENCE_REFERENCE_REQUIRED", "/governance/evidence_refs"))

    if selected is not None:
        selected_family = selected["model_family"]
        clustering_task = problem["task_type"] == "CLUSTERING"
        clustering_family = selected_family == "CLUSTERING"
        if clustering_task != clustering_family:
            findings.add(Finding("TASK_MODEL_FAMILY_INCOHERENT", "/selection/selected_candidate_id"))
        if (
            problem["interpretability_requirement"] == "HIGH"
            and selected_family in OPAQUE_FAMILIES
            and selected["interpretability_method_ref"] is None
        ):
            findings.add(Finding("INTERPRETABILITY_METHOD_REQUIRED", "/selection/selected_candidate_id"))

    if problem["consequence_level"] == "HIGH":
        if selection["policy_consequence_ref"] is None:
            findings.add(Finding("HIGH_CONSEQUENCE_POLICY_REFERENCE_REQUIRED", "/selection/policy_consequence_ref"))
        if governance["review_state"] != "COMPLETE_FOR_DECLARED_SCOPE":
            findings.add(Finding("HIGH_CONSEQUENCE_REVIEW_REQUIRED", "/governance/review_state"))

    review_state = governance["review_state"]
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/governance/review_state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/governance/review_state"))
    elif not governance["review_record_refs"]:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/governance/review_record_refs"))
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
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    candidate["assessment_id"] = compute_assessment_id(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    if entry.get("tamper") == "assessment_id":
        candidate["assessment_id"] = "kfm:model-selection:" + "f" * 24
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
    parser = argparse.ArgumentParser(description="Validate fixture-only model-selection rationale assessments.")
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
