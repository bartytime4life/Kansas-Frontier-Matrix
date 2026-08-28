#!/usr/bin/env python3
"""Validate the inactive sensitive-location parity assessment profile.

PASS proves local declaration consistency only. The validator reads no
coordinates, fetches no source, evaluates no policy, executes no transform,
grants no access, and performs no lifecycle, release, or publication action.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
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

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/governance/sensitive_location_parity_assessment.schema.json"
)
CASES = (
    ROOT
    / "fixtures/contracts/v1/governance/sensitive_location_parity_assessment/cases.json"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "sensitive-location-parity-assessment-fixture-only-v1"

MANDATORY_LIMITATIONS = (
    "DECLARATION_ONLY",
    "NO_ACCESS_AUTHORITY",
    "NO_COORDINATES_OR_SOURCE_PAYLOADS",
    "NO_POLICY_OR_STEWARD_DECISION",
    "NO_RELEASE_OR_PUBLICATION",
    "NO_TRANSFORM_EXECUTED",
)

FALSE_EFFECTS = {
    "access_granted": False,
    "evidence_resolved": False,
    "lifecycle_mutated": False,
    "policy_evaluated": False,
    "promoted": False,
    "public_output_created": False,
    "published": False,
    "released": False,
    "source_activated": False,
    "steward_reviewed": False,
    "transform_executed": False,
}

FAMILY_OWNERS = {
    "ARCHAEOLOGICAL_SITE": "archaeology",
    "CRITICAL_INFRASTRUCTURE": "settlements-infrastructure",
    "ECOLOGICAL_DEN": "fauna",
    "ECOLOGICAL_NEST": "fauna",
    "ECOLOGICAL_ROOST": "fauna",
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
    return "sensitive-location-parity-assessment:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _canonical(values: Any) -> bool:
    return (
        isinstance(values, list)
        and all(isinstance(value, str) for value in values)
        and values == sorted(set(values))
    )


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    request = candidate.get("request")
    request = request if isinstance(request, Mapping) else {}
    support = candidate.get("support")
    support = support if isinstance(support, Mapping) else {}
    disposition = candidate.get("disposition")
    disposition = disposition if isinstance(disposition, Mapping) else {}
    transform = candidate.get("transform")
    transform = transform if isinstance(transform, Mapping) else {}
    output = candidate.get("output")
    output = output if isinstance(output, Mapping) else {}

    arrays = (
        (support, "domain_contract_refs", "/support/domain_contract_refs"),
        (support, "evidence_refs", "/support/evidence_refs"),
        (support, "policy_refs", "/support/policy_refs"),
        (support, "sensitivity_registry_refs", "/support/sensitivity_registry_refs"),
        (support, "source_snapshot_refs", "/support/source_snapshot_refs"),
        (disposition, "reason_codes", "/disposition/reason_codes"),
    )
    for owner, key, path in arrays:
        if not _canonical(owner.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", path))

    if tuple(candidate.get("limitations", ())) != MANDATORY_LIMITATIONS:
        findings.append(Finding("LIMITATION_BOUNDARY_MISMATCH", "/limitations"))

    family = request.get("subject_family")
    expected_owner = FAMILY_OWNERS.get(family)
    if expected_owner is not None and request.get("owner_domain") != expected_owner:
        findings.append(Finding("SUBJECT_OWNER_MISMATCH", "/request/owner_domain"))

    if disposition.get("review_required") is not True:
        findings.append(Finding("REVIEW_REQUIRED", "/disposition/review_required"))

    precision = request.get("requested_precision")
    outcome = disposition.get("outcome")
    reasons = set(disposition.get("reason_codes", []))
    receipt_ref = transform.get("receipt_ref")
    method_ref = transform.get("method_profile_ref")
    target = transform.get("target_precision")
    generalized_candidate = output.get("generalized_output_candidate")

    if precision == "EXACT":
        if outcome != "EXACT_DENIED":
            findings.append(
                Finding("PRECISION_DISPOSITION_MISMATCH", "/disposition/outcome")
            )
        if "EXACT_LOCATION_PUBLIC_DENY" not in reasons:
            findings.append(
                Finding("EXACT_DENY_REASON_REQUIRED", "/disposition/reason_codes")
            )
        if receipt_ref is not None or method_ref is not None or target != "NONE":
            findings.append(
                Finding("EXACT_REQUEST_TRANSFORM_CONFLICT", "/transform")
            )
        if generalized_candidate is not False:
            findings.append(
                Finding(
                    "EXACT_REQUEST_OUTPUT_CONFLICT",
                    "/output/generalized_output_candidate",
                )
            )
    elif precision == "GENERALIZED":
        if outcome != "GENERALIZED_WITH_RECEIPT_CANDIDATE":
            findings.append(
                Finding("PRECISION_DISPOSITION_MISMATCH", "/disposition/outcome")
            )
        if "GENERALIZED_OUTPUT_REQUIRES_RECEIPT" not in reasons:
            findings.append(
                Finding(
                    "GENERALIZATION_REASON_REQUIRED", "/disposition/reason_codes"
                )
            )
        if receipt_ref is None:
            findings.append(
                Finding("GENERALIZATION_RECEIPT_REQUIRED", "/transform/receipt_ref")
            )
        if method_ref is None:
            findings.append(
                Finding(
                    "GENERALIZATION_METHOD_REQUIRED", "/transform/method_profile_ref"
                )
            )
        if target != "GENERALIZED":
            findings.append(
                Finding(
                    "GENERALIZATION_TARGET_MISMATCH", "/transform/target_precision"
                )
            )
        if generalized_candidate is not True:
            findings.append(
                Finding(
                    "GENERALIZATION_OUTPUT_CANDIDATE_REQUIRED",
                    "/output/generalized_output_candidate",
                )
            )

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


def materialize_case(
    document: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case.get("base")
    if (
        not isinstance(bases, Mapping)
        or base_name not in bases
        or not isinstance(bases[base_name], Mapping)
    ):
        raise ValueError("unknown fixture base")
    candidate = copy.deepcopy(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        if (
            not isinstance(mutation, Mapping)
            or not isinstance(mutation.get("path"), str)
            or "value" not in mutation
        ):
            raise ValueError("invalid mutation")
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["assessment_id"] = (
            "sensitive-location-parity-assessment:" + "0" * 24
        )
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _load_fixture_document()
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if (
            not isinstance(raw, dict)
            or not isinstance(raw.get("name"), str)
            or raw["name"] in names
        ):
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        result.append((raw, materialize_case(document, raw)))
    return result


def _serialize(
    result: ValidationResult, *, path: Path | None = None, case: str | None = None
) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [
            {"code": item.code, "path": item.path} for item in result.findings
        ],
        "scope": SCOPE,
        "authority": {
            "coordinate_access": False,
            "source_fetch": False,
            "policy_evaluation": False,
            "steward_decision": False,
            "transform_execution": False,
            "access_grant": False,
            "lifecycle_mutation": False,
            "promotion": False,
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
        result = ValidationResult(
            "ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),)
        )
        print(_serialize(result, case="fixture_manifest"))
        return 2
    mismatches = 0
    for raw, candidate in cases:
        result = validate_payload(candidate)
        actual = [item.code for item in result.findings]
        if (
            result.outcome != raw.get("expected_outcome")
            or actual != raw.get("expected_findings")
        ):
            mismatches += 1
        print(_serialize(result, case=raw["name"]))
    return 1 if mismatches else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-only sensitive-location parity assessment."
    )
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
