"""Validate fixture-only attested-compute boundary assessments.

The validator derives one decision posture from local declarations. It does
not resolve references, verify an external attestation, use credentials,
select a cloud or TEE, process data, execute compute, release, or publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/attested_compute_boundary_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/attested_compute_boundary_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576

CONTROL_NAMES = {
    "human_review": "HUMAN_REVIEW",
    "policy": "POLICY",
    "quarantine": "QUARANTINE",
    "receipt": "RECEIPT",
}
UNSUPPORTED_AUTHORITIES = [
    "CONSENT_VALIDITY",
    "DISCLOSURE_SAFETY",
    "EVIDENCE_SUFFICIENCY",
    "PURPOSE_AUTHORITY",
    "RELEASE_FITNESS",
    "REVIEW_APPROVAL",
    "SOURCE_ADMISSIBILITY",
]


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
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
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


def _controls(candidate: Mapping[str, object]) -> Mapping[str, object]:
    controls = candidate["existing_controls"]
    assert isinstance(controls, Mapping)
    return controls


def _problem(candidate: Mapping[str, object]) -> Mapping[str, object]:
    problem = candidate["problem"]
    assert isinstance(problem, Mapping)
    return problem


def _boundaries(candidate: Mapping[str, object]) -> Mapping[str, object]:
    boundaries = candidate["boundary_declarations"]
    assert isinstance(boundaries, Mapping)
    return boundaries


def _attestation(candidate: Mapping[str, object]) -> Mapping[str, object]:
    attestation = candidate["attestation_claim"]
    assert isinstance(attestation, Mapping)
    return attestation


def _all_boundary_states(candidate: Mapping[str, object], state: str) -> bool:
    return all(
        isinstance(declaration, Mapping) and declaration.get("resolution") == state
        for declaration in _boundaries(candidate).values()
    )


def derive_decision(candidate: Mapping[str, object]) -> dict[str, object]:
    """Derive the closed v1 posture without performing external effects."""

    if candidate["assessment_state"] == "ERROR":
        return {
            "posture": "DEFER_REAL_TEE",
            "reason_codes": ["ASSESSMENT_ERROR"],
            "simulation_assessment_allowed": False,
            "real_tee_authorized": False,
        }

    attestation = _attestation(candidate)
    if attestation["state"] == "UNVERIFIED_EXTERNAL":
        return {
            "posture": "DENY_UNVERIFIED_ATTESTATION",
            "reason_codes": ["UNVERIFIED_ATTESTATION_DENIED"],
            "simulation_assessment_allowed": False,
            "real_tee_authorized": False,
        }

    controls = _controls(candidate)
    problem = _problem(candidate)
    request = candidate["execution_request"]
    safeguards = candidate["safeguards"]
    assert isinstance(safeguards, Mapping)
    simulation_plan_ref = safeguards["simulation_plan_ref"]
    review_complete = all(state != "NOT_REVIEWED" for state in controls.values())

    if (
        problem["residual_state"] == "NONE"
        and request == "NONE"
        and review_complete
        and _all_boundary_states(candidate, "NOT_REQUIRED")
        and attestation["state"] == "ABSENT"
        and simulation_plan_ref is None
    ):
        return {
            "posture": "NO_TRE",
            "reason_codes": ["EXISTING_CONTROLS_SUFFICIENT"],
            "simulation_assessment_allowed": False,
            "real_tee_authorized": False,
        }

    if (
        problem["residual_state"] == "DEFINED"
        and request == "SYNTHETIC_SIMULATION"
        and review_complete
        and _all_boundary_states(candidate, "RESOLVED")
        and attestation["state"] == "SYNTHETIC_ONLY"
        and simulation_plan_ref is not None
    ):
        return {
            "posture": "SIMULATED_ASSESSMENT",
            "reason_codes": ["SYNTHETIC_BOUNDARY_COMPLETE"],
            "simulation_assessment_allowed": True,
            "real_tee_authorized": False,
        }

    reasons: set[str] = set()
    if not review_complete:
        reasons.add("CONTROL_REVIEW_INCOMPLETE")
    if problem["residual_state"] == "UNRESOLVED":
        reasons.add("RESIDUAL_PROBLEM_UNRESOLVED")
    if request == "REAL_TEE":
        reasons.add("REAL_TEE_DEFERRED")
    elif request == "SYNTHETIC_SIMULATION":
        if not _all_boundary_states(candidate, "RESOLVED"):
            reasons.add("BOUNDARY_COMPONENT_UNRESOLVED")
        if attestation["state"] != "SYNTHETIC_ONLY":
            reasons.add("ATTESTATION_BOUNDARY_INCOMPLETE")
        if simulation_plan_ref is None:
            reasons.add("SIMULATION_PLAN_INCOMPLETE")
    if not reasons:
        reasons.add("DECISION_DEFERRED")
    return {
        "posture": "DEFER_REAL_TEE",
        "reason_codes": sorted(reasons),
        "simulation_assessment_allowed": False,
        "real_tee_authorized": False,
    }


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    controls = _controls(candidate)
    problem = _problem(candidate)
    unsolved = problem["unsolved_by_existing_controls"]
    if not _canonical_strings(unsolved):
        findings.add(
            Finding(
                "ARRAY_NOT_CANONICAL",
                "/problem/unsolved_by_existing_controls",
            )
        )

    residual_state = problem["residual_state"]
    statement = problem["statement"]
    affected_owner_refs = problem["affected_owner_refs"]
    if not _canonical_strings(affected_owner_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/problem/affected_owner_refs"))
    if residual_state == "DEFINED" and not isinstance(statement, str):
        findings.add(Finding("PROBLEM_DECLARATION_INCOHERENT", "/problem/statement"))
    if residual_state != "DEFINED" and statement is not None:
        findings.add(Finding("PROBLEM_DECLARATION_INCOHERENT", "/problem/statement"))
    if residual_state == "DEFINED" and not affected_owner_refs:
        findings.add(
            Finding("AFFECTED_OWNER_REFERENCE_REQUIRED", "/problem/affected_owner_refs")
        )
    if residual_state == "NONE" and affected_owner_refs:
        findings.add(
            Finding("AFFECTED_OWNER_REFERENCE_UNEXPECTED", "/problem/affected_owner_refs")
        )

    insufficient = sorted(
        CONTROL_NAMES[name]
        for name, state in controls.items()
        if state == "REVIEWED_INSUFFICIENT"
    )
    if residual_state == "DEFINED":
        if unsolved != insufficient or not insufficient:
            findings.add(
                Finding(
                    "EXISTING_CONTROL_MAPPING_MISMATCH",
                    "/problem/unsolved_by_existing_controls",
                )
            )
    elif unsolved or (residual_state == "NONE" and insufficient):
        findings.add(
            Finding(
                "EXISTING_CONTROL_MAPPING_MISMATCH",
                "/problem/unsolved_by_existing_controls",
            )
        )

    attestation = _attestation(candidate)
    attestation_state = attestation["state"]
    verifier_ref = attestation["verifier_profile_ref"]
    trust_root_ref = attestation["trust_root_ref"]
    claimed_support = attestation["claimed_support"]
    unsupported_authorities = attestation["unsupported_authorities"]
    coherent_attestation = (
        (
            attestation_state == "ABSENT"
            and verifier_ref is None
            and trust_root_ref is None
            and claimed_support is None
            and unsupported_authorities == []
        )
        or (
            attestation_state == "SYNTHETIC_ONLY"
            and verifier_ref is not None
            and trust_root_ref is None
            and isinstance(claimed_support, str)
            and unsupported_authorities == UNSUPPORTED_AUTHORITIES
        )
        or (
            attestation_state == "UNVERIFIED_EXTERNAL"
            and verifier_ref is not None
            and isinstance(claimed_support, str)
            and unsupported_authorities == UNSUPPORTED_AUTHORITIES
        )
    )
    if not coherent_attestation:
        findings.add(
            Finding("ATTESTATION_DECLARATION_INCOHERENT", "/attestation_claim")
        )

    safeguards = candidate["safeguards"]
    assert isinstance(safeguards, Mapping)
    if (
        candidate["execution_request"] == "NONE"
        and safeguards["simulation_plan_ref"] is not None
    ):
        findings.add(
            Finding("SIMULATION_PLAN_UNEXPECTED", "/safeguards/simulation_plan_ref")
        )

    decision = candidate["decision"]
    assert isinstance(decision, Mapping)
    if not _canonical_strings(decision["reason_codes"]):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/decision/reason_codes"))
    if dict(decision) != derive_decision(candidate):
        findings.add(Finding("DECISION_MISMATCH", "/decision"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    semantic_findings = _semantic_findings(candidate)
    if semantic_findings:
        return ValidationResult("DENY", tuple(semantic_findings))

    decision = candidate["decision"]
    assert isinstance(decision, Mapping)
    posture = decision["posture"]
    if candidate["assessment_state"] == "ERROR":
        outcome = "ERROR"
    elif posture in {"NO_TRE", "SIMULATED_ASSESSMENT"}:
        outcome = "PASS"
    elif posture == "DEFER_REAL_TEE":
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    if outcome == "PASS":
        return ValidationResult(outcome, ())
    return ValidationResult(
        outcome,
        tuple(
            Finding(str(code), "/decision/posture")
            for code in decision["reason_codes"]
        ),
    )


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
    candidate["decision"] = copy.deepcopy(
        entry.get("decision_override", derive_decision(candidate))
    )
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(
    path: Path = FIXTURE_PATH,
) -> list[dict[str, object]]:
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
        description="Validate fixture-only attested-compute boundary assessments."
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
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
