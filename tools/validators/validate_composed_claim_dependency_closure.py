#!/usr/bin/env python3
"""Validate fixture-only composed-claim dependency closure records."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/composed_claim_dependency_closure.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/composed_claim_dependency_closure"
SCOPE = "evidence.composed_claim_dependency_closure"

FORBIDDEN_GEOMETRY_KEYS = frozenset(
    {"coordinate", "coordinates", "decimallatitude", "decimallongitude", "geometry", "geom", "latitude", "longitude", "wkt"}
)
FORBIDDEN_SECRET_KEYS = frozenset(
    {"api_key", "api_token", "credential", "credentials", "email", "password", "secret", "token", "username"}
)
INTERNAL_PATH_MARKERS = (
    "/data/raw/", "/data/work/", "/data/quarantine/", "/data/published/",
    "data/raw/", "data/work/", "data/quarantine/", "data/published/",
)

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


def _canonical(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_digest(value: object) -> str:
    return f"sha256:{hashlib.sha256(_canonical(value)).hexdigest()}"


def graph_projection(document: dict[str, object]) -> dict[str, object]:
    dependencies = document["dependencies"]
    assert isinstance(dependencies, list)
    return {
        "claim": document["claim"],
        "dependencies": [
            {
                "role_id": dependency["role_id"],
                "requirement": dependency["requirement"],
                "evidence_ref": dependency["evidence_ref"],
                "expected_spec_hash": dependency["expected_spec_hash"],
            }
            for dependency in dependencies
            if isinstance(dependency, dict)
        ],
        "alternative_groups": document["alternative_groups"],
        "exclusion_groups": document["exclusion_groups"],
    }


def canonical_graph_hash(document: dict[str, object]) -> str:
    return canonical_digest(graph_projection(document))


def canonical_closure_id(document: dict[str, object]) -> str:
    return f"kfm://candidate/evidence/composed-claim/{canonical_graph_hash(document).removeprefix('sha256:')}"


def canonical_spec_hash(document: dict[str, object]) -> str:
    return canonical_digest({key: value for key, value in document.items() if key != "spec_hash"})


def _json_path(parts: Sequence[object]) -> str:
    value = "$"
    for part in parts:
        value += f"[{part}]" if isinstance(part, int) else f".{part}"
    return value


def _parse_instant(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _scan_payload(value: object) -> list[Finding]:
    findings: set[Finding] = set()
    pending: list[tuple[object, str]] = [(value, "$")]
    while pending:
        current, path = pending.pop()
        if isinstance(current, dict):
            for key, item in current.items():
                child_path = f"{path}.{key}"
                normalized_key = key.lower()
                if normalized_key in FORBIDDEN_GEOMETRY_KEYS:
                    add_finding(findings, "COMPOSED_CLAIM_EXACT_GEOMETRY_DENIED", child_path)
                if normalized_key in FORBIDDEN_SECRET_KEYS:
                    add_finding(findings, "COMPOSED_CLAIM_SECRET_FIELD_DENIED", child_path)
                pending.append((item, child_path))
        elif isinstance(current, list):
            pending.extend((item, f"{path}[{index}]") for index, item in enumerate(current))
        elif isinstance(current, str):
            normalized = current.lower()
            if any(marker in normalized for marker in INTERNAL_PATH_MARKERS):
                add_finding(findings, "COMPOSED_CLAIM_INTERNAL_LIFECYCLE_PATH_DENIED", path)
    return sorted(findings)


def derive_closure_summary(candidate: dict[str, object]) -> dict[str, object]:
    dependencies = candidate["dependencies"]
    alternative_groups = candidate["alternative_groups"]
    exclusion_groups = candidate["exclusion_groups"]
    assert isinstance(dependencies, list)
    assert isinstance(alternative_groups, list)
    assert isinstance(exclusion_groups, list)

    role_state = {
        dependency["role_id"]: dependency["resolution"]["state"]
        for dependency in dependencies
        if isinstance(dependency, dict) and isinstance(dependency.get("resolution"), dict)
    }
    required = [
        dependency for dependency in dependencies
        if isinstance(dependency, dict) and dependency["requirement"] == "REQUIRED"
    ]
    optional = [
        dependency for dependency in dependencies
        if isinstance(dependency, dict) and dependency["requirement"] == "OPTIONAL"
    ]

    resolved_roles = sorted(role for role, state in role_state.items() if state == "RESOLVED")
    unresolved_roles = sorted(role for role, state in role_state.items() if state == "UNRESOLVED")
    denied_roles = sorted(role for role, state in role_state.items() if state == "DENIED")
    error_roles = sorted(role for role, state in role_state.items() if state == "ERROR")

    reasons: set[str] = set()
    outcome: str | None = None

    if error_roles:
        outcome = "ERROR"
        reasons.add("DEPENDENCY_EVALUATION_ERROR")

    alternative_maximum_exceeded = False
    alternative_unmet: list[str] = []
    alternative_all_denied: list[str] = []
    for group in alternative_groups:
        assert isinstance(group, dict)
        states = [role_state.get(role) for role in group["role_ids"]]
        resolved = sum(state == "RESOLVED" for state in states)
        if resolved > group["maximum_resolved"]:
            alternative_maximum_exceeded = True
        if resolved < group["minimum_resolved"]:
            alternative_unmet.append(group["group_id"])
            if states and all(state == "DENIED" for state in states):
                alternative_all_denied.append(group["group_id"])

    exclusion_violated = False
    for group in exclusion_groups:
        assert isinstance(group, dict)
        resolved = sum(role_state.get(role) == "RESOLVED" for role in group["role_ids"])
        if resolved > group["maximum_resolved"]:
            exclusion_violated = True

    if outcome is None and (alternative_maximum_exceeded or exclusion_violated):
        outcome = "ERROR"
        if alternative_maximum_exceeded:
            reasons.add("ALTERNATIVE_GROUP_MAXIMUM_EXCEEDED")
        if exclusion_violated:
            reasons.add("MUTUAL_EXCLUSION_VIOLATION")

    required_denied = any(
        isinstance(dependency, dict) and dependency["resolution"]["state"] == "DENIED"
        for dependency in required
    )
    required_unresolved = any(
        isinstance(dependency, dict) and dependency["resolution"]["state"] == "UNRESOLVED"
        for dependency in required
    )
    if outcome is None and required_denied:
        outcome = "DENY"
        reasons.add("REQUIRED_DEPENDENCY_DENIED")
    if outcome is None and required_unresolved:
        outcome = "ABSTAIN"
        reasons.add("REQUIRED_DEPENDENCY_UNRESOLVED")

    if outcome is None and alternative_unmet:
        if len(alternative_all_denied) == len(alternative_unmet):
            outcome = "DENY"
            reasons.add("ALTERNATIVE_GROUP_DENIED")
        else:
            outcome = "ABSTAIN"
            reasons.add("ALTERNATIVE_GROUP_UNRESOLVED")

    optional_unavailable = any(
        isinstance(dependency, dict)
        and dependency["resolution"]["state"] in {"UNRESOLVED", "DENIED"}
        for dependency in optional
    )
    if outcome is None and optional_unavailable:
        outcome = "QUALIFIED"
        reasons.add("OPTIONAL_DEPENDENCY_UNAVAILABLE")

    if outcome is None:
        outcome = "SUPPORTED"

    return {
        "outcome": outcome,
        "render_allowed": outcome in {"SUPPORTED", "QUALIFIED"},
        "reason_codes": sorted(reasons),
        "resolved_roles": resolved_roles,
        "unresolved_roles": unresolved_roles,
        "denied_roles": denied_roles,
        "error_roles": error_roles,
    }


def validate_document(candidate: object) -> list[Finding]:
    findings: set[Finding] = set(_scan_payload(candidate))
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "COMPOSED_CLAIM_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    claim = candidate["claim"]
    dependencies = candidate["dependencies"]
    alternative_groups = candidate["alternative_groups"]
    exclusion_groups = candidate["exclusion_groups"]
    summary = candidate["closure_summary"]
    assert isinstance(claim, dict)
    assert isinstance(dependencies, list)
    assert isinstance(alternative_groups, list)
    assert isinstance(exclusion_groups, list)
    assert isinstance(summary, dict)

    expected_graph_hash = canonical_graph_hash(candidate)
    if candidate["dependency_graph_hash"] != expected_graph_hash:
        add_finding(
            findings,
            "COMPOSED_CLAIM_GRAPH_HASH_MISMATCH",
            "$.dependency_graph_hash",
        )

    expected_closure_id = canonical_closure_id(candidate)
    if candidate["closure_id"] != expected_closure_id:
        add_finding(findings, "COMPOSED_CLAIM_ID_MISMATCH", "$.closure_id")

    expected_previous = (
        None
        if candidate["revision"] == 1
        else f"{expected_closure_id}/revision/{candidate['revision'] - 1}"
    )
    if candidate["previous_closure_ref"] != expected_previous:
        add_finding(
            findings,
            "COMPOSED_CLAIM_PREVIOUS_REF_MISMATCH",
            "$.previous_closure_ref",
        )

    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(findings, "COMPOSED_CLAIM_SPEC_HASH_MISMATCH", "$.spec_hash")

    valid_time = claim["scope"]["valid_time"]
    assert isinstance(valid_time, dict)
    start = _parse_instant(valid_time["start"])
    end = _parse_instant(valid_time["end"])
    if start is None or end is None or start > end:
        add_finding(
            findings,
            "COMPOSED_CLAIM_TIME_RANGE_INVALID",
            "$.claim.scope.valid_time",
        )

    role_ids = [
        dependency["role_id"]
        for dependency in dependencies
        if isinstance(dependency, dict)
    ]
    if role_ids != sorted(role_ids):
        add_finding(findings, "COMPOSED_CLAIM_ROLE_ORDER_INVALID", "$.dependencies")
    if len(set(role_ids)) != len(role_ids):
        add_finding(findings, "COMPOSED_CLAIM_ROLE_DUPLICATE", "$.dependencies")

    role_by_id = {
        dependency["role_id"]: dependency
        for dependency in dependencies
        if isinstance(dependency, dict)
    }
    alternative_role_ids = {
        dependency["role_id"]
        for dependency in dependencies
        if isinstance(dependency, dict) and dependency["requirement"] == "ALTERNATIVE"
    }

    alternative_group_ids = [
        group["group_id"]
        for group in alternative_groups
        if isinstance(group, dict)
    ]
    if alternative_group_ids != sorted(alternative_group_ids):
        add_finding(
            findings,
            "COMPOSED_CLAIM_ALTERNATIVE_GROUP_ORDER_INVALID",
            "$.alternative_groups",
        )
    if len(set(alternative_group_ids)) != len(alternative_group_ids):
        add_finding(
            findings,
            "COMPOSED_CLAIM_ALTERNATIVE_GROUP_DUPLICATE",
            "$.alternative_groups",
        )

    covered_alternatives: list[str] = []
    for index, group in enumerate(alternative_groups):
        assert isinstance(group, dict)
        group_roles = group["role_ids"]
        assert isinstance(group_roles, list)
        if group_roles != sorted(group_roles):
            add_finding(
                findings,
                "COMPOSED_CLAIM_GROUP_ROLE_ORDER_INVALID",
                f"$.alternative_groups[{index}].role_ids",
            )
        if group["minimum_resolved"] > group["maximum_resolved"]:
            add_finding(
                findings,
                "COMPOSED_CLAIM_GROUP_CARDINALITY_INVALID",
                f"$.alternative_groups[{index}]",
            )
        if group["maximum_resolved"] > len(group_roles):
            add_finding(
                findings,
                "COMPOSED_CLAIM_GROUP_CARDINALITY_INVALID",
                f"$.alternative_groups[{index}].maximum_resolved",
            )
        for role in group_roles:
            if role not in role_by_id:
                add_finding(
                    findings,
                    "COMPOSED_CLAIM_GROUP_ROLE_UNKNOWN",
                    f"$.alternative_groups[{index}].role_ids",
                )
                continue
            if role_by_id[role]["requirement"] != "ALTERNATIVE":
                add_finding(
                    findings,
                    "COMPOSED_CLAIM_GROUP_ROLE_NOT_ALTERNATIVE",
                    f"$.alternative_groups[{index}].role_ids",
                )
            covered_alternatives.append(role)

    if set(covered_alternatives) != alternative_role_ids:
        add_finding(
            findings,
            "COMPOSED_CLAIM_ALTERNATIVE_ROLE_COVERAGE_INVALID",
            "$.alternative_groups",
        )
    if len(covered_alternatives) != len(set(covered_alternatives)):
        add_finding(
            findings,
            "COMPOSED_CLAIM_ALTERNATIVE_ROLE_MULTIPLE_GROUPS",
            "$.alternative_groups",
        )

    exclusion_group_ids = [
        group["group_id"]
        for group in exclusion_groups
        if isinstance(group, dict)
    ]
    if exclusion_group_ids != sorted(exclusion_group_ids):
        add_finding(
            findings,
            "COMPOSED_CLAIM_EXCLUSION_GROUP_ORDER_INVALID",
            "$.exclusion_groups",
        )
    if len(set(exclusion_group_ids)) != len(exclusion_group_ids):
        add_finding(
            findings,
            "COMPOSED_CLAIM_EXCLUSION_GROUP_DUPLICATE",
            "$.exclusion_groups",
        )
    for index, group in enumerate(exclusion_groups):
        assert isinstance(group, dict)
        group_roles = group["role_ids"]
        assert isinstance(group_roles, list)
        if group_roles != sorted(group_roles):
            add_finding(
                findings,
                "COMPOSED_CLAIM_GROUP_ROLE_ORDER_INVALID",
                f"$.exclusion_groups[{index}].role_ids",
            )
        for role in group_roles:
            if role not in role_by_id:
                add_finding(
                    findings,
                    "COMPOSED_CLAIM_EXCLUSION_ROLE_UNKNOWN",
                    f"$.exclusion_groups[{index}].role_ids",
                )

    for index, dependency in enumerate(dependencies):
        assert isinstance(dependency, dict)
        resolution = dependency["resolution"]
        assert isinstance(resolution, dict)
        if (
            resolution["state"] == "RESOLVED"
            and resolution["actual_spec_hash"] != dependency["expected_spec_hash"]
        ):
            add_finding(
                findings,
                "COMPOSED_CLAIM_RESOLVED_SPEC_HASH_MISMATCH",
                f"$.dependencies[{index}].resolution.actual_spec_hash",
            )

    expected_summary = derive_closure_summary(candidate)
    summary_fields = {
        "outcome": "COMPOSED_CLAIM_OUTCOME_MISMATCH",
        "render_allowed": "COMPOSED_CLAIM_RENDER_MISMATCH",
        "reason_codes": "COMPOSED_CLAIM_REASON_CODES_MISMATCH",
        "resolved_roles": "COMPOSED_CLAIM_RESOLVED_ROLES_MISMATCH",
        "unresolved_roles": "COMPOSED_CLAIM_UNRESOLVED_ROLES_MISMATCH",
        "denied_roles": "COMPOSED_CLAIM_DENIED_ROLES_MISMATCH",
        "error_roles": "COMPOSED_CLAIM_ERROR_ROLES_MISMATCH",
    }
    for field, code in summary_fields.items():
        if summary[field] != expected_summary[field]:
            add_finding(findings, code, f"$.closure_summary.{field}")

    return sorted(findings)


def validate_closure_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _fixture_codes(path: Path) -> list[str]:
    return sorted({finding.code for finding in validate_closure_file(path)})


def validate_fixture_suite() -> int:
    valid_files = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
    semantic_files = sorted(
        (FIXTURES_ROOT / "semantic_invalid").glob("semantic_invalid_*.json")
    )
    schema_files = sorted((FIXTURES_ROOT / "invalid").glob("invalid_*.json"))
    semantic_expected = json.loads(
        (
            FIXTURES_ROOT
            / "semantic_invalid/expected_findings_manifest.json"
        ).read_text(encoding="utf-8")
    )
    schema_expected = json.loads(
        (
            FIXTURES_ROOT
            / "invalid/expected_findings_manifest.json"
        ).read_text(encoding="utf-8")
    )

    ok = bool(valid_files and semantic_files and schema_files)
    ok = ok and {path.name for path in semantic_files} == set(semantic_expected)
    ok = ok and {path.name for path in schema_files} == set(schema_expected)

    for path in valid_files:
        findings = validate_closure_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and not findings
    for path in semantic_files:
        findings = validate_closure_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and _fixture_codes(path) == sorted(semantic_expected[path.name])
    for path in schema_files:
        findings = validate_closure_file(path)
        print(serialize_result(SCOPE, path, findings))
        ok = ok and _fixture_codes(path) == sorted(schema_expected[path.name])

    if ok:
        outcomes = sorted(
            {
                json.loads(path.read_text(encoding="utf-8"))["closure_summary"]["outcome"]
                for path in valid_files
            }
        )
        print(
            f"COMPOSED_CLAIM_CLOSURE_FIXTURES_VALID valid={len(valid_files)} "
            f"semantic_invalid={len(semantic_files)} schema_invalid={len(schema_files)} "
            f"outcomes={','.join(outcomes)} no_network=true "
            "evidence_authority=false release_authority=false"
        )
        return 0
    print("COMPOSED_CLAIM_CLOSURE_FIXTURES_INVALID", file=sys.stderr)
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return validate_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate fixture-only composed-claim dependency closure records",
        scope=SCOPE,
        validator=validate_closure_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
