#!/usr/bin/env python3
"""Derive or validate fixture-only, non-publishing cross-lane join reports.

EXACT_KEY uses parameterized in-memory SQLite. SPATIAL_TEMPORAL compares only
declared synthetic cell references and timezone-aware intervals. No mode writes
a file, contacts a network service, or authorizes a downstream effect.
"""
from __future__ import annotations

import argparse
import copy
import json
import sqlite3
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/joins/cross_lane_join_assessment/cases.json"
DOMAIN_LANE_REGISTER_PATH = REPO_ROOT / "control_plane/domain_lane_register.yaml"
IDENTITY_PREFIX = "kfm:cross-lane-join-assessment:"
CANDIDATE_PREFIX = "kfm:join-candidate:"
SCOPE = "cross-lane-join-assessment-fixture-only-v1"
RULE_ORDER = (
    "DEPENDENCIES_READY",
    "EVIDENCE_REFS_PRESENT",
    "JOIN_PREDICATE_MATCHED",
    "LIVING_PERSON_SAFE",
    "SENSITIVITY_SAFE",
    "SOURCE_ROLES_COMPATIBLE",
)
SENSITIVITY_RANK = {"PUBLIC_SAFE": 0, "INTERNAL": 1, "RESTRICTED": 2, "PROHIBITED": 3}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.status == "PASS" and not self.findings


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in candidate.items() if key not in {"assessment_id", "spec_hash"}}


def _candidate_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {"request": copy.deepcopy(candidate.get("request")), "endpoints": copy.deepcopy(candidate.get("endpoints"))}


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["assessment_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _exact_key_match(left_key: object, right_key: object) -> bool:
    if not isinstance(left_key, str) or not isinstance(right_key, str):
        return False
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE left_endpoint (join_key TEXT NOT NULL)")
        connection.execute("CREATE TABLE right_endpoint (join_key TEXT NOT NULL)")
        connection.execute("INSERT INTO left_endpoint(join_key) VALUES (?)", (left_key,))
        connection.execute("INSERT INTO right_endpoint(join_key) VALUES (?)", (right_key,))
        count = connection.execute(
            "SELECT COUNT(*) FROM left_endpoint AS l JOIN right_endpoint AS r ON l.join_key = r.join_key"
        ).fetchone()[0]
        return count == 1
    finally:
        connection.close()


def _spatial_temporal_match(left: Mapping[str, Any], right: Mapping[str, Any], tolerance_seconds: object) -> bool:
    if left.get("spatial_cell_ref") is None or left.get("spatial_cell_ref") != right.get("spatial_cell_ref"):
        return False
    left_start, left_end = _time(left.get("valid_from")), _time(left.get("valid_to"))
    right_start, right_end = _time(right.get("valid_from")), _time(right.get("valid_to"))
    if None in {left_start, left_end, right_start, right_end}:
        return False
    tolerance = timedelta(seconds=tolerance_seconds if isinstance(tolerance_seconds, int) else 0)
    return left_start <= right_end + tolerance and right_start <= left_end + tolerance


def _temporal_boundary_ambiguous(
    left: Mapping[str, Any], right: Mapping[str, Any], tolerance_seconds: object
) -> bool:
    """Fail closed when zero-tolerance intervals only touch at one boundary.

    The shared temporal profile does not establish repository-wide boundary
    inclusivity. A positive tolerance is an explicit request to compare across
    a bounded gap; zero tolerance must not silently choose closed intervals.
    """
    if tolerance_seconds != 0:
        return False
    if left.get("spatial_cell_ref") is None or left.get("spatial_cell_ref") != right.get("spatial_cell_ref"):
        return False
    left_start, left_end = _time(left.get("valid_from")), _time(left.get("valid_to"))
    right_start, right_end = _time(right.get("valid_from")), _time(right.get("valid_to"))
    if None in {left_start, left_end, right_start, right_end}:
        return False
    return left_end == right_start or right_end == left_start


def _strictest_sensitivity(left: Mapping[str, Any], right: Mapping[str, Any]) -> str:
    values = [value for value in (left.get("sensitivity"), right.get("sensitivity")) if value in SENSITIVITY_RANK]
    return max(values, key=SENSITIVITY_RANK.get) if values else "PROHIBITED"


def _source_role_conflict(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    """Require pair/domain authority for every unequal role vector.

    KFM has no accepted repository-wide crosswalk that can declare two distinct
    source-role classes compatible at this generic seam. Preserve equal roles
    for candidate proof and route every unequal pair to source-role review.
    """
    return left.get("source_role") != right.get("source_role")


def _unresolved_domain_aliases(path: Path | None = None) -> Mapping[str, str]:
    """Read unresolved aliases as a fail-closed dependency, never identity authority.

    The domain-lane register is a projection-only review aid. If it cannot be
    read or parsed, the helper cannot safely prove that two raw domain names are
    distinct governed lanes, so the dependency failure must propagate instead
    of being treated as an empty alias set.
    """
    register_path = DOMAIN_LANE_REGISTER_PATH if path is None else path
    try:
        value = yaml.safe_load(register_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ValueError("domain lane register unavailable") from exc
    aliases = _mapping(value).get("unresolved_aliases")
    if not isinstance(aliases, Mapping) or not all(
        isinstance(key, str) and isinstance(target, str)
        for key, target in aliases.items()
    ):
        raise ValueError("domain lane alias projection invalid")
    return dict(aliases)


def _domain_alias_collision(left_domain: object, right_domain: object) -> bool:
    if not isinstance(left_domain, str) or not isinstance(right_domain, str) or left_domain == right_domain:
        return False
    aliases = _unresolved_domain_aliases()
    left_target = aliases.get(left_domain)
    right_target = aliases.get(right_domain)
    return (
        left_target == right_domain
        or right_target == left_domain
        or (isinstance(left_target, str) and left_target == right_target)
    )


def derive_decision(candidate: Mapping[str, Any]) -> dict[str, Any]:
    request = _mapping(candidate.get("request"))
    endpoints = _mapping(candidate.get("endpoints"))
    left, right = _mapping(endpoints.get("left")), _mapping(endpoints.get("right"))
    predicate = request.get("predicate")
    matched = (
        _exact_key_match(left.get("join_key"), right.get("join_key"))
        if predicate == "EXACT_KEY"
        else _spatial_temporal_match(left, right, request.get("temporal_tolerance_seconds"))
    )
    temporal_boundary_ambiguous = (
        predicate == "SPATIAL_TEMPORAL"
        and _temporal_boundary_ambiguous(left, right, request.get("temporal_tolerance_seconds"))
    )
    if temporal_boundary_ambiguous:
        matched = False
    same_domain = (
        isinstance(left.get("domain"), str)
        and isinstance(right.get("domain"), str)
        and left.get("domain") == right.get("domain")
    )
    try:
        domain_alias_collision = _domain_alias_collision(left.get("domain"), right.get("domain"))
        alias_dependency_error = False
    except ValueError:
        domain_alias_collision = False
        alias_dependency_error = True
    if same_domain or domain_alias_collision:
        matched = False
    inherited = _strictest_sensitivity(left, right)
    missing_evidence = sum(endpoint.get("evidence_ref") is None for endpoint in (left, right))
    living_count = sum(endpoint.get("living_person") is True for endpoint in (left, right))
    exact_sensitive_count = sum(
        endpoint.get("geometry_precision") == "EXACT"
        and endpoint.get("sensitivity") in {"RESTRICTED", "PROHIBITED"}
        for endpoint in (left, right)
    )
    source_conflict = _source_role_conflict(left, right)
    dependency_error = request.get("dependency_state") == "ERROR" or alias_dependency_error

    failures = {
        "DEPENDENCIES_READY": int(dependency_error),
        "EVIDENCE_REFS_PRESENT": missing_evidence,
        "JOIN_PREDICATE_MATCHED": int(not matched),
        "LIVING_PERSON_SAFE": living_count,
        "SENSITIVITY_SAFE": exact_sensitive_count + int(
            inherited in {"RESTRICTED", "PROHIBITED"} and exact_sensitive_count == 0
        ),
        "SOURCE_ROLES_COMPATIBLE": int(source_conflict),
    }

    if same_domain:
        outcome, status, reason, obligation = "ABSTAIN", "NO_JOIN_CANDIDATE", "CROSS_DOMAIN_PAIR_REQUIRED", "ROUTE_TO_DOMAIN_LOCAL_VALIDATOR"
    elif domain_alias_collision:
        outcome, status, reason, obligation = "ABSTAIN", "NO_JOIN_CANDIDATE", "DOMAIN_ALIAS_REVIEW_REQUIRED", "ROUTE_TO_DOMAIN_ALIAS_REVIEW"
    elif alias_dependency_error:
        outcome, status, reason, obligation = "ERROR", "VALIDATOR_SYSTEM_ERROR", "DOMAIN_ALIAS_REGISTER_UNAVAILABLE", "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY"
    elif request.get("dependency_state") == "ERROR":
        outcome, status, reason, obligation = "ERROR", "VALIDATOR_SYSTEM_ERROR", "VALIDATOR_DEPENDENCY_ERROR", "REPAIR_VALIDATOR_DEPENDENCY"
    elif living_count:
        outcome, status, reason, obligation = "DENY", "LIVING_PERSON_JOIN_DENIED", "LIVING_PERSON_JOIN_DENIED", "REQUIRE_CONSENT_AND_POLICY_REVIEW"
    elif exact_sensitive_count or inherited == "PROHIBITED":
        outcome, status, reason, obligation = "DENY", "GEOMETRY_PRECISION_BLOCKED", "GEOMETRY_PRECISION_BLOCKED", "GENERALIZE_OR_WITHHOLD_GEOMETRY"
    elif missing_evidence:
        outcome, status, reason, obligation = "ABSTAIN", "EVIDENCE_REF_MISSING", "EVIDENCE_REF_MISSING", "RESOLVE_EVIDENCE_REFS"
    elif temporal_boundary_ambiguous:
        outcome, status, reason, obligation = "ABSTAIN", "NO_JOIN_CANDIDATE", "TEMPORAL_BOUNDARY_AMBIGUOUS", "ROUTE_TO_PAIR_TEMPORAL_SEMANTICS"
    elif not matched:
        outcome, status, reason, obligation = "ABSTAIN", "NO_JOIN_CANDIDATE", "JOIN_PREDICATE_NOT_SATISFIED", "REVIEW_JOIN_BASIS"
    elif source_conflict:
        outcome, status, reason, obligation = "ABSTAIN", "SOURCE_ROLE_REVIEW_REQUIRED", "SOURCE_ROLE_CONFLICT", "RESOLVE_SOURCE_ROLE_COMPATIBILITY"
    elif inherited == "RESTRICTED":
        outcome, status, reason, obligation = "ABSTAIN", "SENSITIVITY_REVIEW_REQUIRED", "SENSITIVITY_REVIEW_REQUIRED", "ROUTE_TO_SENSITIVITY_REVIEW"
    else:
        outcome, status, reason, obligation = "ALLOW", "JOIN_CANDIDATE", "JOIN_PREDICATE_SATISFIED", "ROUTE_TO_PAIR_JOIN_VALIDATOR"

    candidate_digest = compute_spec_hash(_candidate_projection(candidate)).removeprefix("sha256:")
    return {
        "candidate_id": CANDIDATE_PREFIX + candidate_digest,
        "validator_outcome": outcome,
        "status": status,
        "matched": matched,
        "source_roles": {
            "left": left.get("source_role"),
            "right": right.get("source_role"),
            "output_role": "CANDIDATE_RELATION",
        },
        "inherited_sensitivity": inherited,
        "rule_results": [{"rule_code": code, "failure_count": failures[code]} for code in RULE_ORDER],
        "reason_codes": [reason],
        "obligations": ["DO_NOT_PUBLISH_FROM_JOIN_HELPER", "PRESERVE_ENDPOINT_SOURCE_ROLES", obligation],
        "effects": {
            "lifecycle_write": False,
            "evidence_bundle_created": False,
            "policy_decision_created": False,
            "review_decision_created": False,
            "release_decision_created": False,
            "publication": False,
            "public_use_authorized": False,
        },
    }


def derive_outputs(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    value["decision"] = derive_decision(value)
    return value


def validate_document(candidate: object) -> ValidationResult:
    findings: set[Finding] = set()
    try:
        schema = load_json_file(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (JsonInputError, ValueError, TypeError, RecursionError):
        return ValidationResult("FAIL", (Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings.update(Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path))) for error in errors[:100])
    if errors or not isinstance(candidate, Mapping):
        return ValidationResult("FAIL", tuple(sorted(findings)))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError):
        return ValidationResult("FAIL", (Finding("CANONICALIZATION_ERROR", "/"),))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    endpoints = _mapping(candidate.get("endpoints"))
    left, right = _mapping(endpoints.get("left")), _mapping(endpoints.get("right"))
    if left.get("endpoint_id") != "LEFT" or right.get("endpoint_id") != "RIGHT":
        findings.add(Finding("ENDPOINT_SIDE_MISMATCH", "/endpoints"))
    for side, endpoint in (("left", left), ("right", right)):
        start, end = _time(endpoint.get("valid_from")), _time(endpoint.get("valid_to"))
        if start is None or end is None or start >= end:
            findings.add(Finding("ENDPOINT_INTERVAL_INVALID", f"/endpoints/{side}"))
    evaluated = _time(candidate.get("evaluated_at"))
    ends = [_time(left.get("valid_to")), _time(right.get("valid_to"))]
    if evaluated is None or any(end is None or end > evaluated for end in ends):
        findings.add(Finding("JOIN_EVALUATION_TIME_INVALID", "/evaluated_at"))

    request = _mapping(candidate.get("request"))
    if request.get("predicate") == "EXACT_KEY" and (left.get("join_key") is None or right.get("join_key") is None):
        findings.add(Finding("EXACT_KEY_REQUIRED", "/endpoints"))
    if request.get("predicate") == "SPATIAL_TEMPORAL" and (left.get("spatial_cell_ref") is None or right.get("spatial_cell_ref") is None):
        findings.add(Finding("SPATIAL_CELL_REF_REQUIRED", "/endpoints"))

    try:
        expected_decision = derive_decision(candidate)
    except (CanonicalizationFailure, sqlite3.Error, TypeError, ValueError):
        findings.add(Finding("DECISION_DERIVATION_ERROR", "/decision"))
    else:
        if candidate.get("decision") != expected_decision:
            findings.add(Finding("JOIN_DECISION_MISMATCH", "/decision"))

    return ValidationResult("FAIL" if findings else "PASS", tuple(sorted(findings)))


def validate_file(path: Path | str) -> ValidationResult:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return ValidationResult("FAIL", (Finding("INPUT_JSON_INVALID", "/"),))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure, sqlite3.Error):
        return ValidationResult("FAIL", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/")]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent: Any = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list):
        parent[int(parts[-1])] = copy.deepcopy(value)
    else:
        parent[parts[-1]] = copy.deepcopy(value)


def fixture_cases(path: Path = CASES_PATH) -> list[tuple[Mapping[str, Any], ValidationResult, str, tuple[str, ...]]]:
    matrix = load_json_file(path)
    if not isinstance(matrix, Mapping) or not isinstance(matrix.get("base"), Mapping) or not isinstance(matrix.get("cases"), list):
        raise ValueError("fixture matrix is invalid")
    base = seal(derive_outputs(matrix["base"]))
    materialized = []
    for raw_case in matrix["cases"]:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise ValueError("fixture case is invalid")
        candidate = copy.deepcopy(base)
        for mutation in raw_case.get("mutations", []):
            if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
                raise ValueError("fixture mutation is invalid")
            _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw_case.get("rederive", True) is True:
            candidate = derive_outputs(candidate)
        if raw_case.get("reseal", True) is True:
            candidate = seal(candidate)
        expected_status = raw_case.get("expected_status")
        expected_findings = raw_case.get("expected_findings", [])
        if not isinstance(expected_status, str) or not isinstance(expected_findings, list) or not all(isinstance(code, str) for code in expected_findings):
            raise ValueError("fixture expectations are invalid")
        materialized.append((candidate, validate_document(candidate), expected_status, tuple(expected_findings)))
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    try:
        cases = fixture_cases(path)
    except (JsonInputError, ValueError, TypeError, KeyError, IndexError, CanonicalizationFailure, sqlite3.Error):
        print(json.dumps({"scope": SCOPE, "status": "FAIL", "reason": "FIXTURE_MATRIX_INVALID"}, sort_keys=True, separators=(",", ":")))
        return 1
    failures = []
    for index, (_candidate, result, expected_status, expected_findings) in enumerate(cases):
        codes = {finding.code for finding in result.findings}
        if result.status != expected_status or not set(expected_findings).issubset(codes):
            failures.append(index)
    print(json.dumps({"cases": len(cases), "failed_case_indexes": failures, "scope": SCOPE, "status": "FAIL" if failures else "PASS"}, sort_keys=True, separators=(",", ":")))
    return 1 if failures else 0


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--derive", type=Path, help="derive and print one sealed assessment; stdout only")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if args.derive is not None:
        try:
            value = load_json_file(args.derive)
            if not isinstance(value, Mapping):
                raise ValueError
            derived = seal(derive_outputs(value))
        except (JsonInputError, ValueError, TypeError, CanonicalizationFailure, sqlite3.Error):
            print(json.dumps({"scope": SCOPE, "status": "FAIL", "reason": "INPUT_OR_DERIVATION_ERROR"}, sort_keys=True, separators=(",", ":")))
            return 1
        result = validate_document(derived)
        if not result.coherent:
            print(
                json.dumps(
                    {
                        "findings": [
                            {"code": finding.code, "path": finding.path}
                            for finding in result.findings
                        ],
                        "scope": SCOPE,
                        "status": "FAIL",
                        "reason": "DERIVED_ASSESSMENT_INVALID",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            return 1
        print(json.dumps(derived, sort_keys=True, separators=(",", ":")))
        return 0
    if not args.files:
        parser.error("provide assessment files, --derive, or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        print(json.dumps({"file": _display(path), "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings], "scope": SCOPE, "status": result.status}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
