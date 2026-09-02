#!/usr/bin/env python3
"""Validate the inactive recommendation-versus-decision assessment profile.

PASS proves local declaration consistency only. No policy, recommendation,
decision, implementation, outcome, release, or publication action is performed.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/governance/recommendation_decision_authority_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/governance/recommendation_decision_authority_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "recommendation-decision-authority-assessment-fixture-only-v1"
MANDATORY_LIMITATIONS = (
    "DECISION_IS_NOT_IMPLEMENTATION",
    "IMPLEMENTATION_IS_NOT_OUTCOME",
    "NO_BINDING_AUTHORITY_CREATED",
    "RECOMMENDATION_IS_ADVISORY",
    "RECOMMENDATION_IS_NOT_DECISION",
)
FALSE_EFFECTS = {
    "recommendation_adopted": False,
    "decision_created": False,
    "implementation_started": False,
    "implementation_completed": False,
    "outcome_measured": False,
    "policy_evaluated": False,
    "released": False,
    "published": False,
}
ERROR_CODES = {
    "ASSESSMENT_ID_MISMATCH",
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "FIXTURE_MANIFEST_INVALID",
    "HASHING_UNAVAILABLE",
    "INPUT_SYMLINK_DENIED",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
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
            parse_float=_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "recommendation-decision-authority-assessment:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _dt(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical(values: Any) -> bool:
    return (
        isinstance(values, list)
        and all(isinstance(value, str) for value in values)
        and values == sorted(set(values))
    )


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    recommendation = candidate.get("recommendation")
    recommendation = recommendation if isinstance(recommendation, Mapping) else {}
    decision = candidate.get("decision")
    decision = decision if isinstance(decision, Mapping) else {}
    linkage = candidate.get("linkage")
    linkage = linkage if isinstance(linkage, Mapping) else {}

    arrays = (
        (recommendation, "source_snapshot_refs", "/recommendation/source_snapshot_refs"),
        (recommendation, "evidence_refs", "/recommendation/evidence_refs"),
        (decision, "authority_basis_refs", "/decision/authority_basis_refs"),
        (decision, "source_snapshot_refs", "/decision/source_snapshot_refs"),
        (decision, "evidence_refs", "/decision/evidence_refs"),
        (linkage, "implementation_refs", "/linkage/implementation_refs"),
        (linkage, "outcome_observation_refs", "/linkage/outcome_observation_refs"),
        (linkage, "reason_codes", "/linkage/reason_codes"),
    )
    for owner, key, path in arrays:
        if not _canonical(owner.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", path))

    if tuple(candidate.get("limitations", ())) != MANDATORY_LIMITATIONS:
        findings.append(Finding("LIMITATION_BOUNDARY_MISMATCH", "/limitations"))

    recommendation_state = recommendation.get("state")
    recommendation_issued = _dt(recommendation.get("issued_at"))
    recommendation_digest = recommendation.get("advisory_scope_digest")
    if recommendation_state == "ISSUED" and (
        recommendation_issued is None or recommendation_digest is None
    ):
        findings.append(Finding("RECOMMENDATION_EVIDENCE_INCOMPLETE", "/recommendation"))
    if recommendation_state == "DRAFT" and (
        recommendation.get("issued_at") is not None or recommendation_digest is not None
    ):
        findings.append(Finding("DRAFT_RECOMMENDATION_ISSUANCE_CONFLICT", "/recommendation"))

    decision_state = decision.get("state")
    decision_time = _dt(decision.get("decided_at"))
    decision_scalars = (
        decision.get("decision_ref"),
        decision.get("decided_at"),
        decision.get("authority_ref"),
        decision.get("instrument_digest"),
    )
    basis = decision.get("authority_basis_refs")
    complete_decision = all(value is not None for value in decision_scalars) and bool(basis)
    no_decision_evidence = all(value is None for value in decision_scalars) and basis == []
    formal_states = {"ADOPTED", "ADOPTED_WITH_CHANGES", "REJECTED", "DEFERRED"}

    if decision_state == "NO_DECISION_RECORDED":
        if not no_decision_evidence:
            findings.append(Finding("NO_DECISION_EVIDENCE_CONFLICT", "/decision"))
    elif decision_state in formal_states:
        if not complete_decision:
            findings.append(Finding("DECISION_EVIDENCE_INCOMPLETE", "/decision"))
    elif decision_state == "STATUS_UNCONFIRMED":
        if not (no_decision_evidence or complete_decision):
            findings.append(Finding("UNCONFIRMED_DECISION_PARTIAL_EVIDENCE", "/decision"))

    if recommendation_issued is not None and decision_time is not None and decision_time < recommendation_issued:
        findings.append(Finding("DECISION_BEFORE_RECOMMENDATION", "/decision/decided_at"))

    expected_disposition = {
        "NO_DECISION_RECORDED": "NO_DECISION",
        "ADOPTED": "ADOPTED_AS_RECOMMENDED",
        "ADOPTED_WITH_CHANGES": "ADOPTED_WITH_CHANGES",
        "REJECTED": "REJECTED",
        "DEFERRED": "DEFERRED",
        "STATUS_UNCONFIRMED": "UNRESOLVED",
    }.get(decision_state)
    if expected_disposition is not None and linkage.get("disposition") != expected_disposition:
        findings.append(Finding("DECISION_DISPOSITION_MISMATCH", "/linkage/disposition"))

    comparison = linkage.get("comparison_digest")
    if decision_state == "ADOPTED_WITH_CHANGES" and comparison is None:
        findings.append(Finding("CHANGE_COMPARISON_REQUIRED", "/linkage/comparison_digest"))
    elif decision_state != "ADOPTED_WITH_CHANGES" and comparison is not None:
        findings.append(Finding("CHANGE_COMPARISON_POSTURE_CONFLICT", "/linkage/comparison_digest"))

    implementations = linkage.get("implementation_refs", [])
    outcomes = linkage.get("outcome_observation_refs", [])
    if implementations and decision_state not in {"ADOPTED", "ADOPTED_WITH_CHANGES"}:
        findings.append(Finding("IMPLEMENTATION_WITHOUT_ADOPTED_DECISION", "/linkage/implementation_refs"))
    if outcomes and not implementations:
        findings.append(Finding("OUTCOME_WITHOUT_IMPLEMENTATION", "/linkage/outcome_observation_refs"))

    if decision_state == "STATUS_UNCONFIRMED" and linkage.get("boundary_outcome") not in {"HOLD", "ABSTAIN"}:
        findings.append(Finding("UNCONFIRMED_BOUNDARY_OVERCLAIM", "/linkage/boundary_outcome"))

    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_assessment_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("assessment_id") != expected_id:
            findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    outcome = "ERROR" if any(item.code in ERROR_CODES for item in ordered) else "DENY"
    return ValidationResult(outcome, ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
        if part
    ]
    current: Any = candidate
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise ValueError("unknown mutation path")
        current = current[part]
    if not parts or not isinstance(current, dict):
        raise ValueError("invalid mutation path")
    current[parts[-1]] = copy.deepcopy(value)


def _load_fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None
        or findings
        or not isinstance(document.get("bases"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case.get("base")
    if not isinstance(bases, Mapping) or base_name not in bases or not isinstance(bases[base_name], Mapping):
        raise ValueError("unknown fixture base")
    candidate = copy.deepcopy(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
            raise ValueError("invalid mutation")
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["assessment_id"] = "recommendation-decision-authority-assessment:" + "0" * 24
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _load_fixture_document()
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names:
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        result.append((raw, materialize_case(document, raw)))
    return result


def _serialize(result: ValidationResult, *, path: Path | None = None, case: str | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": SCOPE,
        "authority": {
            "network_fetch": False,
            "policy_evaluation": False,
            "recommendation_creation": False,
            "decision_creation": False,
            "implementation_write": False,
            "outcome_measurement": False,
            "release": False,
            "publication": False,
        },
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures() -> int:
    try:
        cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RuntimeError, RecursionError):
        result = ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),))
        print(_serialize(result, case="fixture_manifest"))
        return 2
    mismatches = 0
    for raw, candidate in cases:
        result = validate_payload(candidate)
        actual = [item.code for item in result.findings]
        if result.outcome != raw.get("expected_outcome") or actual != raw.get("expected_findings"):
            mismatches += 1
        print(_serialize(result, case=raw["name"]))
    return 1 if mismatches else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one fixture-only recommendation-decision authority assessment.")
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("--fixtures does not accept a path")
        return replay_fixtures()
    if args.path is None:
        parser.error("path or --fixtures is required")
    result = validate_file(args.path)
    print(_serialize(result, path=args.path))
    return 0 if result.outcome == "PASS" else 1 if result.outcome == "DENY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
