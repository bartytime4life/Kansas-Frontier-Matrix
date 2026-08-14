#!/usr/bin/env python3
"""Validate fixture-only Fauna-Habitat public-safe assignment candidates.

The profile composes the existing generic CrossLaneJoinAssessment and adds only
pair-specific semantics. It consumes synthetic references and metadata, never
coordinate or geometry bytes, and grants no evidence, policy, review, release,
publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
GENERIC_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
GENERIC_SPEC = importlib.util.spec_from_file_location(
    "kfm_cross_lane_join_candidates", GENERIC_PATH
)
if GENERIC_SPEC is None or GENERIC_SPEC.loader is None:
    raise RuntimeError("generic cross-lane join assessment module is unavailable")
GENERIC = importlib.util.module_from_spec(GENERIC_SPEC)
sys.modules[GENERIC_SPEC.name] = GENERIC
GENERIC_SPEC.loader.exec_module(GENERIC)

CASES_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/joins/"
    "fauna_habitat_public_safe_assignment/cases.json"
)
RELATION_PROFILE_REF = (
    "kfm:relation-profile:fauna-habitat-public-safe-assignment:v1"
)
SCOPE = "fauna-habitat-public-safe-assignment-fixture-only-v1"
FIXTURE_PREFIX = "kfm:fixture:"


@dataclass(frozen=True, order=True)
class Finding:
    """One stable pair-profile finding without candidate values."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Pair-profile validation result."""

    status: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.status == "PASS" and not self.findings


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _fixture_ref(value: object, *, nullable: bool = False) -> bool:
    if value is None:
        return nullable
    return isinstance(value, str) and value.startswith(FIXTURE_PREFIX)


def validate_document(candidate: object) -> ValidationResult:
    """Run the generic validator, then enforce the Fauna-Habitat profile."""

    generic = GENERIC.validate_document(candidate)
    generic_findings = tuple(
        Finding(code=finding.code, path=finding.path)
        for finding in generic.findings
    )
    if generic_findings:
        return ValidationResult("FAIL", tuple(sorted(generic_findings)))
    if not isinstance(candidate, Mapping):
        return ValidationResult("FAIL", (Finding("PAIR_DOCUMENT_INVALID", "/"),))

    findings: set[Finding] = set()
    request = _mapping(candidate.get("request"))
    endpoints = _mapping(candidate.get("endpoints"))
    left = _mapping(endpoints.get("left"))
    right = _mapping(endpoints.get("right"))
    decision = _mapping(candidate.get("decision"))

    if request.get("relation_profile_ref") != RELATION_PROFILE_REF:
        _add(findings, "RELATION_PROFILE_MISMATCH", "/request/relation_profile_ref")
    if request.get("predicate") != "SPATIAL_TEMPORAL":
        _add(findings, "PAIR_PREDICATE_MISMATCH", "/request/predicate")
    if request.get("temporal_tolerance_seconds") != 0:
        _add(
            findings,
            "PAIR_TEMPORAL_TOLERANCE_MISMATCH",
            "/request/temporal_tolerance_seconds",
        )

    if left.get("domain") != "fauna":
        _add(findings, "ENDPOINT_DOMAIN_MISMATCH", "/endpoints/left/domain")
    if right.get("domain") != "habitat":
        _add(findings, "ENDPOINT_DOMAIN_MISMATCH", "/endpoints/right/domain")

    required_refs = (
        ("left", left, "object_ref", False),
        ("left", left, "source_descriptor_ref", False),
        ("left", left, "evidence_ref", True),
        ("left", left, "spatial_cell_ref", False),
        ("right", right, "object_ref", False),
        ("right", right, "source_descriptor_ref", False),
        ("right", right, "evidence_ref", True),
        ("right", right, "spatial_cell_ref", False),
    )
    for side, endpoint, field, nullable in required_refs:
        if not _fixture_ref(endpoint.get(field), nullable=nullable):
            _add(
                findings,
                "NON_FIXTURE_REF_DENIED",
                f"/endpoints/{side}/{field}",
            )

    for side, endpoint in (("left", left), ("right", right)):
        if endpoint.get("living_person") is not False:
            _add(findings, "LIVING_PERSON_STATE_DENIED", f"/endpoints/{side}/living_person")

    outcome = decision.get("validator_outcome")
    if outcome == "ALLOW":
        if decision.get("status") != "JOIN_CANDIDATE" or decision.get("matched") is not True:
            _add(findings, "ALLOW_CANDIDATE_STATE_INVALID", "/decision")
        for side, endpoint in (("left", left), ("right", right)):
            if endpoint.get("sensitivity") != "PUBLIC_SAFE":
                _add(
                    findings,
                    "ALLOW_SENSITIVITY_NOT_PUBLIC_SAFE",
                    f"/endpoints/{side}/sensitivity",
                )
            if endpoint.get("geometry_precision") != "GENERALIZED":
                _add(
                    findings,
                    "ALLOW_GEOMETRY_NOT_GENERALIZED",
                    f"/endpoints/{side}/geometry_precision",
                )
            if endpoint.get("evidence_ref") is None:
                _add(
                    findings,
                    "ALLOW_EVIDENCE_REF_MISSING",
                    f"/endpoints/{side}/evidence_ref",
                )
        source_roles = _mapping(decision.get("source_roles"))
        if source_roles.get("output_role") != "CANDIDATE_RELATION":
            _add(findings, "ALLOW_OUTPUT_ROLE_INVALID", "/decision/source_roles/output_role")
        effects = _mapping(decision.get("effects"))
        if any(value is not False for value in effects.values()):
            _add(findings, "ALLOW_EFFECTS_NOT_ALL_FALSE", "/decision/effects")

    return ValidationResult(
        "FAIL" if findings else "PASS",
        tuple(sorted(findings)),
    )


def validate_file(path: Path | str) -> ValidationResult:
    """Load through the generic bounded JSON reader and validate the profile."""

    try:
        candidate = GENERIC.load_json_file(path)
    except GENERIC.JsonInputError:
        return ValidationResult("FAIL", (Finding("INPUT_JSON_INVALID", "/"),))
    except (OSError, TypeError, ValueError, RecursionError):
        return ValidationResult("FAIL", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))
    return validate_document(candidate)


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
    ]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent: Any = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list):
        parent[int(parts[-1])] = copy.deepcopy(value)
    else:
        parent[parts[-1]] = copy.deepcopy(value)


def fixture_cases(
    path: Path = CASES_PATH,
) -> list[tuple[str, Mapping[str, Any], ValidationResult, Mapping[str, Any]]]:
    """Materialize and validate the frozen pair-profile case matrix."""

    matrix = GENERIC.load_json_file(path)
    if not isinstance(matrix, Mapping):
        raise ValueError("fixture matrix must be an object")
    base = matrix.get("base")
    cases = matrix.get("cases")
    if not isinstance(base, Mapping) or not isinstance(cases, list):
        raise ValueError("fixture matrix is missing base or cases")

    sealed_base = GENERIC.seal(GENERIC.derive_outputs(base))
    materialized = []
    for raw_case in cases:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise ValueError("fixture case is invalid")
        candidate = copy.deepcopy(sealed_base)
        mutations = raw_case.get("mutations", [])
        if not isinstance(mutations, list):
            raise ValueError("fixture mutations must be an array")
        for mutation in mutations:
            if (
                not isinstance(mutation, Mapping)
                or not isinstance(mutation.get("path"), str)
                or "value" not in mutation
            ):
                raise ValueError("fixture mutation is invalid")
            _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw_case.get("rederive", True) is True:
            candidate = GENERIC.derive_outputs(candidate)
        if raw_case.get("reseal", True) is True:
            candidate = GENERIC.seal(candidate)
        expected = raw_case.get("expected")
        if not isinstance(expected, Mapping):
            raise ValueError("fixture expectation is invalid")
        materialized.append(
            (raw_case["name"], candidate, validate_document(candidate), expected)
        )
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    """Run the frozen fixture matrix and emit one bounded summary."""

    try:
        cases = fixture_cases(path)
    except (
        GENERIC.JsonInputError,
        GENERIC.CanonicalizationFailure,
        KeyError,
        OSError,
        TypeError,
        ValueError,
        RecursionError,
    ):
        print(
            json.dumps(
                {"reason": "FIXTURE_MATRIX_INVALID", "scope": SCOPE, "status": "FAIL"},
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 1

    failures: list[str] = []
    for name, candidate, result, expected in cases:
        expected_findings = expected.get("findings")
        findings = [finding.code for finding in result.findings]
        decision = _mapping(candidate.get("decision"))
        if (
            result.status != expected.get("validation_status")
            or findings != expected_findings
            or decision.get("validator_outcome") != expected.get("validator_outcome")
            or decision.get("status") != expected.get("decision_status")
        ):
            failures.append(name)

    print(
        json.dumps(
            {
                "cases": len(cases),
                "failed_cases": failures,
                "scope": SCOPE,
                "status": "FAIL" if failures else "PASS",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 1 if failures else 0


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide assessment files or --fixtures")

    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        print(
            json.dumps(
                {
                    "file": _display(path),
                    "findings": [
                        {"code": finding.code, "path": finding.path}
                        for finding in result.findings
                    ],
                    "scope": SCOPE,
                    "status": result.status,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
