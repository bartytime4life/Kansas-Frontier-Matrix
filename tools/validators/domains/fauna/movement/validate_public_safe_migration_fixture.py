#!/usr/bin/env python3
"""Validate bounded synthetic Fauna migration-corridor fixtures.

This no-network executable is intentionally narrower than the proposed
MigrationRoute schema. A pass proves only that a synthetic generalized
corridor carrier keeps migration support distinct from telemetry and
individual-tracking truth. It grants no source, policy, review, release, or
publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[5]
FIXTURE_ROOT = ROOT / "fixtures" / "domains" / "fauna" / "migration_route"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
SCOPE = "fauna-public-safe-migration-fixture-v1"
MAX_POSITIONS = 4096
MAX_EVIDENCE_REFS = 64

TOP_LEVEL_KEYS = frozenset(
    {
        "record_type",
        "route_id",
        "fixture_only",
        "reality_boundary",
        "network_access",
        "taxon_ref",
        "source_descriptor_ref",
        "source_role",
        "claim_scope",
        "telemetry_truth",
        "individual_tracking_truth",
        "time_scope",
        "geometry",
        "sensitivity_state",
        "evidence_refs",
        "governance",
    }
)
TIME_KEYS = frozenset({"kind", "start_day_of_year", "end_day_of_year"})
GEOMETRY_KEYS = frozenset(
    {"type", "coordinates", "precision_class", "derivation_method"}
)
GOVERNANCE_KEYS = frozenset(
    {"policy_state", "review_state", "release_state", "promotion_state"}
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        return "PASS" if self.ok else "ERROR"


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code, path)
    if finding not in findings:
        findings.append(finding)


def _ascii_identity_character(character: str) -> bool:
    return "a" <= character <= "z" or "0" <= character <= "9"


def _fixture_ref(value: object, prefix: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    suffix = value[len(prefix) :] if value.startswith(prefix) else ""
    return (
        value == value.strip()
        and bool(suffix)
        and any(_ascii_identity_character(character) for character in suffix)
        and all(
            _ascii_identity_character(character) or character in ":-"
            for character in value
        )
    )


def _finite_number(value: object) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(float(value))
    except (OverflowError, ValueError):
        return False


def _time_findings(value: object) -> list[Finding]:
    if not isinstance(value, Mapping):
        return [Finding("time.object_required", "/time_scope")]
    findings: list[Finding] = []
    for key in sorted(set(value) - TIME_KEYS, key=str):
        _add(findings, "time.field_forbidden", f"/time_scope/{key}")
    if value.get("kind") != "synthetic-nonwrapping-season-window":
        _add(findings, "time.season_window_required", "/time_scope/kind")
    start = value.get("start_day_of_year")
    end = value.get("end_day_of_year")
    if not isinstance(start, int) or isinstance(start, bool) or not 1 <= start <= 366:
        _add(findings, "time.day_invalid", "/time_scope/start_day_of_year")
    if not isinstance(end, int) or isinstance(end, bool) or not 1 <= end <= 366:
        _add(findings, "time.day_invalid", "/time_scope/end_day_of_year")
    if (
        isinstance(start, int)
        and not isinstance(start, bool)
        and isinstance(end, int)
        and not isinstance(end, bool)
        and 1 <= start <= 366
        and 1 <= end <= 366
        and start > end
    ):
        _add(findings, "time.window_reversed", "/time_scope")
    return findings


def _geometry_findings(value: object) -> list[Finding]:
    if not isinstance(value, Mapping):
        return [Finding("geom.object_required", "/geometry")]
    findings: list[Finding] = []
    for key in sorted(set(value) - GEOMETRY_KEYS, key=str):
        _add(findings, "geom.field_forbidden", f"/geometry/{key}")
    if value.get("type") != "LineString":
        _add(findings, "geom.linestring_required", "/geometry/type")
    if value.get("precision_class") != "public-safe-synthetic":
        _add(
            findings,
            "geom.public_safe_precision_required",
            "/geometry/precision_class",
        )
    if value.get("derivation_method") != "synthetic-corridor-generalization":
        _add(
            findings,
            "geom.derivation_method_required",
            "/geometry/derivation_method",
        )

    coordinates = value.get("coordinates")
    if not isinstance(coordinates, list) or len(coordinates) < 2:
        _add(findings, "geom.positions_insufficient", "/geometry/coordinates")
        return findings
    if len(coordinates) > MAX_POSITIONS:
        _add(findings, "geom.position_limit_exceeded", "/geometry/coordinates")
        return findings
    normalized_positions: list[tuple[float, float]] = []
    for index, position in enumerate(coordinates):
        path = f"/geometry/coordinates/{index}"
        if not (
            isinstance(position, list)
            and len(position) == 2
            and all(_finite_number(item) for item in position)
        ):
            _add(findings, "geom.position_invalid", path)
            continue
        longitude, latitude = float(position[0]), float(position[1])
        if not (-180 <= longitude <= 180 and -90 <= latitude <= 90):
            _add(findings, "geom.position_out_of_bounds", path)
            continue
        normalized_positions.append((longitude, latitude))
    if (
        len(normalized_positions) == len(coordinates)
        and len(set(normalized_positions)) < 2
    ):
        _add(findings, "geom.route_degenerate", "/geometry/coordinates")
    elif len(normalized_positions) == len(coordinates):
        for index in range(1, len(normalized_positions)):
            if normalized_positions[index] == normalized_positions[index - 1]:
                _add(
                    findings,
                    "geom.consecutive_position_duplicate",
                    f"/geometry/coordinates/{index}",
                )
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    if not isinstance(candidate, Mapping):
        return ValidationResult((Finding("schema.root_not_object", "/"),))

    findings: list[Finding] = []
    for key in sorted(set(candidate) - TOP_LEVEL_KEYS, key=str):
        _add(findings, "schema.field_forbidden", f"/{key}")

    exact_values = {
        "record_type": (
            "fauna_public_safe_migration_candidate",
            "schema.record_type_invalid",
        ),
        "fixture_only": (True, "schema.fixture_only_required"),
        "reality_boundary": (
            "synthetic-test-fixture",
            "schema.reality_boundary_required",
        ),
        "network_access": ("forbidden", "schema.network_access_forbidden"),
        "source_role": ("synthetic", "migration.source_role_invalid"),
        "claim_scope": (
            "migration-corridor-support-only",
            "claim.scope_invalid",
        ),
        "telemetry_truth": (False, "claim.telemetry_truth_forbidden"),
        "individual_tracking_truth": (
            False,
            "claim.individual_tracking_truth_forbidden",
        ),
        "sensitivity_state": (
            "public-safe-synthetic",
            "sens.public_safe_required",
        ),
    }
    for field, (expected, code) in exact_values.items():
        actual = candidate.get(field)
        matches = (
            type(actual) is bool and actual is expected
            if isinstance(expected, bool)
            else actual == expected
        )
        if not matches:
            _add(findings, code, f"/{field}")

    for field, prefix in {
        "route_id": "fixture:fauna:migration:",
        "taxon_ref": "fixture:taxon:fauna:",
        "source_descriptor_ref": "fixture:source:fauna:",
    }.items():
        if not _fixture_ref(candidate.get(field), prefix):
            _add(findings, "schema.fixture_ref_required", f"/{field}")

    evidence_refs = candidate.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        _add(findings, "evidence.fixture_ref_required", "/evidence_refs")
    elif len(evidence_refs) > MAX_EVIDENCE_REFS:
        _add(findings, "evidence.reference_limit_exceeded", "/evidence_refs")
    else:
        seen_evidence_refs: set[str] = set()
        for index, item in enumerate(evidence_refs):
            if not _fixture_ref(item, "fixture:evidence:fauna:"):
                _add(
                    findings,
                    "evidence.fixture_ref_required",
                    f"/evidence_refs/{index}",
                )
            elif item in seen_evidence_refs:
                _add(
                    findings,
                    "evidence.reference_duplicate",
                    f"/evidence_refs/{index}",
                )
            else:
                seen_evidence_refs.add(item)

    findings.extend(_time_findings(candidate.get("time_scope")))
    findings.extend(_geometry_findings(candidate.get("geometry")))

    governance = candidate.get("governance")
    if not isinstance(governance, Mapping):
        _add(findings, "gov.object_required", "/governance")
    else:
        for key in sorted(set(governance) - GOVERNANCE_KEYS, key=str):
            _add(findings, "gov.field_forbidden", f"/governance/{key}")
        for field, expected in {
            "policy_state": "not-evaluated-fixture",
            "review_state": "fixture-only",
            "release_state": "not-released",
            "promotion_state": "not-eligible",
        }.items():
            if governance.get(field) != expected:
                _add(findings, "gov.state_invalid", f"/governance/{field}")

    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path | str) -> ValidationResult:
    try:
        candidate = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.input_invalid", "/"),))
    return validate_candidate(candidate)


def validate_fixture_manifest() -> ValidationResult:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("fixture.manifest_invalid", "/"),))
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("cases"), list):
        return ValidationResult((Finding("fixture.manifest_invalid", "/cases"),))

    findings: list[Finding] = []
    declared: list[str] = []
    for index, case in enumerate(manifest["cases"]):
        if not isinstance(case, Mapping):
            _add(findings, "fixture.case_invalid", f"/cases/{index}")
            continue
        relative_path = case.get("path")
        expected = case.get("expected_findings")
        if not isinstance(relative_path, str) or not isinstance(expected, list):
            _add(findings, "fixture.case_invalid", f"/cases/{index}")
            continue
        declared.append(relative_path)
        actual = validate_file(FIXTURE_ROOT / relative_path).findings
        expected_findings = tuple(
            sorted(
                Finding(item.get("code"), item.get("path"))
                for item in expected
                if isinstance(item, Mapping)
                and isinstance(item.get("code"), str)
                and isinstance(item.get("path"), str)
            )
        )
        if len(expected_findings) != len(expected) or expected_findings != actual:
            _add(findings, "fixture.outcome_mismatch", f"/cases/{index}")

    actual_paths = sorted(
        str(path.relative_to(FIXTURE_ROOT))
        for folder in (FIXTURE_ROOT / "valid", FIXTURE_ROOT / "invalid")
        for path in folder.glob("*.json")
    )
    if declared != sorted(set(declared)):
        _add(findings, "fixture.paths_not_canonical", "/cases")
    if declared != actual_paths:
        _add(findings, "fixture.inventory_mismatch", "/cases")
    return ValidationResult(tuple(sorted(set(findings))))


def _payload(path: str, result: ValidationResult) -> dict[str, Any]:
    return {
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "input": path,
        "outcome": result.outcome,
        "scope": SCOPE,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic public-safe Fauna migration fixtures."
    )
    parser.add_argument("paths", nargs="*", help="JSON fixtures to validate")
    parser.add_argument("--fixtures", action="store_true", help="replay fixture manifest")
    args = parser.parse_args(argv)
    if args.fixtures:
        result = validate_fixture_manifest()
        print(json.dumps(_payload("fixture-manifest", result), sort_keys=True))
        return 0 if result.ok else 1
    if not args.paths:
        parser.error("provide at least one path or --fixtures")
    exit_code = 0
    for raw_path in args.paths:
        result = validate_file(raw_path)
        print(json.dumps(_payload(raw_path, result), sort_keys=True))
        exit_code = max(exit_code, 0 if result.ok else 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
