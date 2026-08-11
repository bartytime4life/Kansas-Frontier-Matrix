"""Validate fixture-only API capability exposure assessments.

The validator checks declarations only. It does not discover or inspect routes,
authenticate references, execute authorization, read canonical stores, resolve
evidence, evaluate policy, mutate state, approve review, release, deploy,
publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/api_capability_exposure_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/release/api_capability_exposure_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_API_OR_ROUTE_MUTATION",
    "NO_AUTHORIZATION_EXECUTION",
    "NO_CANONICAL_STORE_ACCESS",
    "NO_EVIDENCE_OR_POLICY_EXECUTION",
    "NO_RELEASE_OR_PUBLICATION_AUTHORITY",
]
EXPECTED_FINITE_OUTCOMES = ["ABSTAIN", "ANSWER", "DENY", "ERROR"]
REQUIRED_PROHIBITED_USES = {
    "BYPASS_EVIDENCE_POLICY_REVIEW_RELEASE",
    "DIRECT_CANONICAL_STORE_ACCESS",
    "EVIDENCE_FREE_PUBLIC_CLAIM",
    "RELEASE_OR_PUBLICATION_BY_CALLER",
}
ABSTAIN_CODES = {
    "CAPABILITY_DETAILS_UNRESOLVED",
    "TRUST_BOUNDARY_REVIEW_INCOMPLETE",
    "TRUST_BOUNDARY_REVIEW_UNKNOWN",
}
NONPUBLIC_STATES = {"RAW", "WORK", "QUARANTINE", "PROCESSED", "CATALOG", "TRIPLET"}
MUTATION_KINDS = {"GOVERNED_MUTATION", "ADMINISTRATIVE_MUTATION"}
MUTATION_EFFECTS = {"GOVERNED_MUTATION", "ADMINISTRATIVE_MUTATION"}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


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


def _purpose_is_placeholder(value: object) -> bool:
    if not isinstance(value, str):
        return False
    lowered = value.casefold()
    return any(marker in lowered for marker in ("placeholder", "tbd", "todo", "unknown"))


def _details_unresolved(capability: Mapping[str, object], review: Mapping[str, object]) -> bool:
    return (
        capability.get("capability_kind") == "UNKNOWN"
        or capability.get("purpose_statement") is None
        or capability.get("audience_class") == "UNKNOWN"
        or capability.get("exposure_posture") == "UNRESOLVED"
        or review.get("boundary_kind") == "UNKNOWN"
        or review.get("state_effect") == "UNKNOWN"
        or review.get("evidence_resolution_required") is None
        or review.get("policy_evaluation_required") is None
        or review.get("public_payload_scrub_required") is None
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    capability = candidate["capability"]
    review = candidate["trust_boundary_review"]
    closure = candidate["closure"]
    limitations = candidate["limitations"]
    assert isinstance(capability, Mapping)
    assert isinstance(review, Mapping)
    assert isinstance(closure, Mapping)

    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for path, value in (
        ("/capability/allowed_data_states", capability.get("allowed_data_states")),
        ("/capability/prohibited_uses", capability.get("prohibited_uses")),
        ("/capability/finite_outcomes", capability.get("finite_outcomes")),
        ("/trust_boundary_review/review_record_refs", review.get("review_record_refs")),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", path))

    state = review.get("state")
    if state == "ERROR":
        findings.add(Finding("TRUST_BOUNDARY_REVIEW_ERROR", "/trust_boundary_review/state"))
        return sorted(findings)
    if state == "INCOMPLETE":
        findings.add(Finding("TRUST_BOUNDARY_REVIEW_INCOMPLETE", "/trust_boundary_review/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("TRUST_BOUNDARY_REVIEW_UNKNOWN", "/trust_boundary_review/state"))

    unresolved = _details_unresolved(capability, review)
    if unresolved:
        findings.add(Finding("CAPABILITY_DETAILS_UNRESOLVED", "/capability"))
        if state == "COMPLETE":
            findings.add(Finding("COMPLETE_REVIEW_HAS_UNRESOLVED_FIELDS", "/trust_boundary_review/state"))

    purpose = capability.get("purpose_statement")
    if _purpose_is_placeholder(purpose):
        findings.add(Finding("BUSINESS_PURPOSE_PLACEHOLDER", "/capability/purpose_statement"))

    posture = capability.get("exposure_posture")
    audience = capability.get("audience_class")
    if (
        posture == "PUBLIC_CANDIDATE" and audience != "PUBLIC_CLIENT"
    ) or (
        posture == "INTERNAL_ONLY" and audience != "INTERNAL_OPERATOR"
    ):
        findings.add(Finding("EXPOSURE_AUDIENCE_MISMATCH", "/capability/audience_class"))

    boundary = review.get("boundary_kind")
    if boundary == "DIRECT_STORE":
        findings.add(Finding("DIRECT_STORE_EXPOSURE_DENIED", "/trust_boundary_review/boundary_kind"))

    capability_kind = capability.get("capability_kind")
    state_effect = review.get("state_effect")
    if capability_kind == "ADMINISTRATIVE_MUTATION" or state_effect == "ADMINISTRATIVE_MUTATION":
        findings.add(Finding("ADMINISTRATIVE_CAPABILITY_EXPOSURE_DENIED", "/capability/capability_kind"))

    finite_outcomes = capability.get("finite_outcomes")
    if state == "COMPLETE" and finite_outcomes != EXPECTED_FINITE_OUTCOMES:
        findings.add(Finding("FINITE_OUTCOME_VOCABULARY_MISMATCH", "/capability/finite_outcomes"))
    prohibited_uses = capability.get("prohibited_uses")
    if state == "COMPLETE" and (
        not isinstance(prohibited_uses, list)
        or not REQUIRED_PROHIBITED_USES.issubset(set(prohibited_uses))
    ):
        findings.add(Finding("PROHIBITED_USE_SET_INCOMPLETE", "/capability/prohibited_uses"))

    if state == "COMPLETE":
        if capability.get("contract_ref") is None:
            findings.add(Finding("API_CONTRACT_REFERENCE_REQUIRED", "/capability/contract_ref"))
        if capability.get("documentation_ref") is None:
            findings.add(Finding("API_DOCUMENTATION_REFERENCE_REQUIRED", "/capability/documentation_ref"))
        if review.get("risk_assessment_ref") is None:
            findings.add(Finding("RISK_ASSESSMENT_REFERENCE_REQUIRED", "/trust_boundary_review/risk_assessment_ref"))
        if not review.get("review_record_refs"):
            findings.add(Finding("REVIEW_RECORD_REFERENCE_REQUIRED", "/trust_boundary_review/review_record_refs"))
        if closure.get("security_review_ref") is None:
            findings.add(Finding("SECURITY_REVIEW_REFERENCE_REQUIRED", "/closure/security_review_ref"))

    if posture == "PUBLIC_CANDIDATE":
        states = capability.get("allowed_data_states")
        if states != ["PUBLISHED"]:
            findings.add(Finding("PUBLIC_DATA_STATE_SCOPE_INVALID", "/capability/allowed_data_states"))
        if isinstance(states, list) and NONPUBLIC_STATES.intersection(states):
            findings.add(Finding("NONPUBLISHED_PUBLIC_STATE_DENIED", "/capability/allowed_data_states"))
        if boundary != "GOVERNED_API":
            findings.add(Finding("PUBLIC_TRUST_BOUNDARY_INVALID", "/trust_boundary_review/boundary_kind"))
        if capability_kind in MUTATION_KINDS or state_effect in MUTATION_EFFECTS:
            findings.add(Finding("PUBLIC_MUTATION_CAPABILITY_DENIED", "/capability/capability_kind"))
        if review.get("evidence_resolution_required") is False or (
            state == "COMPLETE" and review.get("evidence_resolution_required") is not True
        ):
            findings.add(Finding("PUBLIC_EVIDENCE_RESOLUTION_REQUIRED", "/trust_boundary_review/evidence_resolution_required"))
        if review.get("policy_evaluation_required") is False or (
            state == "COMPLETE" and review.get("policy_evaluation_required") is not True
        ):
            findings.add(Finding("PUBLIC_POLICY_EVALUATION_REQUIRED", "/trust_boundary_review/policy_evaluation_required"))
        if review.get("public_payload_scrub_required") is False or (
            state == "COMPLETE" and review.get("public_payload_scrub_required") is not True
        ):
            findings.add(Finding("PUBLIC_PAYLOAD_SCRUB_REQUIRED", "/trust_boundary_review/public_payload_scrub_required"))
        if state == "COMPLETE":
            if closure.get("release_manifest_ref") is None:
                findings.add(Finding("PUBLIC_RELEASE_MANIFEST_REQUIRED", "/closure/release_manifest_ref"))
            if closure.get("correction_ref") is None:
                findings.add(Finding("PUBLIC_CORRECTION_REFERENCE_REQUIRED", "/closure/correction_ref"))
            if closure.get("rollback_ref") is None:
                findings.add(Finding("PUBLIC_ROLLBACK_REFERENCE_REQUIRED", "/closure/rollback_ref"))

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
    if "TRUST_BOUNDARY_REVIEW_ERROR" in codes:
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
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
    parser = argparse.ArgumentParser(description="Validate fixture-only API capability exposure assessments.")
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
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
