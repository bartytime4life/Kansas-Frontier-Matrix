#!/usr/bin/env python3
"""Validate a bounded synthetic Fauna public-safe range carrier.

This executable is fixture-only and intentionally narrower than the proposed
RangePolygon schema. A pass proves only that a synthetic no-network candidate
keeps range support distinct from occurrence and absence truth while exposing
finite, explicitly generalized geometry. It is not source admission, policy or
review approval, a release decision, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[5]
FIXTURE_ROOT = ROOT / "fixtures" / "domains" / "fauna" / "range_polygon"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
SCOPE = "fauna-public-safe-range-fixture-v1"

ALLOWED_TOP_LEVEL_KEYS = frozenset(
    {
        "record_type",
        "range_id",
        "fixture_only",
        "reality_boundary",
        "network_access",
        "taxon_ref",
        "source_descriptor_ref",
        "source_role",
        "range_class",
        "claim_scope",
        "occurrence_truth",
        "absence_truth",
        "geometry",
        "sensitivity_state",
        "evidence_refs",
        "governance",
    }
)
ALLOWED_GEOMETRY_KEYS = frozenset(
    {"type", "coordinates", "precision_class", "derivation_method"}
)
ALLOWED_GOVERNANCE_KEYS = frozenset(
    {"policy_state", "review_state", "release_state", "promotion_state"}
)
MAX_RINGS = 16
MAX_POSITIONS = 4096


@dataclass(frozen=True, order=True)
class Finding:
    """Stable machine-comparable validation finding."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite result for one public-safe range candidate."""

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


def _is_fixture_ref(value: object, prefix: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    return (
        value == value.strip()
        and value.startswith(prefix)
        and all(
            character.islower() or character.isdigit() or character in ":-"
            for character in value
        )
    )


def _is_finite_number(value: object) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


def _geometry_findings(geometry: object) -> list[Finding]:
    findings: list[Finding] = []
    if not isinstance(geometry, Mapping):
        return [Finding("geom.object_required", "/geometry")]

    for key in sorted(set(geometry) - ALLOWED_GEOMETRY_KEYS, key=str):
        _add(findings, "geom.field_forbidden", f"/geometry/{key}")

    if geometry.get("type") != "Polygon":
        _add(findings, "geom.polygon_required", "/geometry/type")
    if geometry.get("precision_class") != "public-safe-synthetic":
        _add(
            findings,
            "geom.public_safe_precision_required",
            "/geometry/precision_class",
        )
    if geometry.get("derivation_method") != "synthetic-generalization-fixture":
        _add(
            findings,
            "geom.derivation_method_required",
            "/geometry/derivation_method",
        )

    coordinates = geometry.get("coordinates")
    if not isinstance(coordinates, list) or not coordinates:
        _add(findings, "geom.coordinates_invalid", "/geometry/coordinates")
        return findings
    if len(coordinates) > MAX_RINGS:
        _add(findings, "geom.ring_limit_exceeded", "/geometry/coordinates")
        return findings

    position_count = 0
    for ring_index, ring in enumerate(coordinates):
        ring_path = f"/geometry/coordinates/{ring_index}"
        if not isinstance(ring, list) or len(ring) < 4:
            _add(findings, "geom.ring_invalid", ring_path)
            continue
        position_count += len(ring)
        if position_count > MAX_POSITIONS:
            _add(findings, "geom.position_limit_exceeded", "/geometry/coordinates")
            break

        normalized_positions: list[tuple[float, float]] = []
        for position_index, position in enumerate(ring):
            position_path = f"{ring_path}/{position_index}"
            if not (
                isinstance(position, list)
                and len(position) == 2
                and all(_is_finite_number(value) for value in position)
            ):
                _add(findings, "geom.position_invalid", position_path)
                continue
            longitude, latitude = float(position[0]), float(position[1])
            if not (-180.0 <= longitude <= 180.0 and -90.0 <= latitude <= 90.0):
                _add(findings, "geom.position_out_of_bounds", position_path)
                continue
            normalized_positions.append((longitude, latitude))

        if len(normalized_positions) == len(ring) and (
            normalized_positions[0] != normalized_positions[-1]
        ):
            _add(findings, "geom.ring_not_closed", ring_path)

    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    """Validate one in-memory synthetic range candidate."""

    if not isinstance(candidate, Mapping):
        return ValidationResult((Finding("schema.root_not_object", "/"),))

    findings: list[Finding] = []
    for key in sorted(set(candidate) - ALLOWED_TOP_LEVEL_KEYS, key=str):
        _add(findings, "schema.field_forbidden", f"/{key}")

    exact_values = {
        "record_type": ("fauna_public_safe_range_candidate", "schema.record_type_invalid"),
        "fixture_only": (True, "schema.fixture_only_required"),
        "reality_boundary": ("synthetic-test-fixture", "schema.reality_boundary_required"),
        "network_access": ("forbidden", "schema.network_access_forbidden"),
        "source_role": ("synthetic", "range.source_role_invalid"),
        "range_class": ("synthetic", "range.class_invalid"),
        "claim_scope": ("range-support-only", "claim.scope_invalid"),
        "occurrence_truth": (False, "claim.occurrence_truth_forbidden"),
        "absence_truth": (False, "claim.absence_truth_forbidden"),
        "sensitivity_state": ("public-safe-synthetic", "sens.public_safe_required"),
    }
    for field, (expected, code) in exact_values.items():
        if candidate.get(field) != expected:
            _add(findings, code, f"/{field}")

    fixture_refs = {
        "range_id": "fixture:fauna:range:",
        "taxon_ref": "fixture:taxon:fauna:",
        "source_descriptor_ref": "fixture:source:fauna:",
    }
    for field, prefix in fixture_refs.items():
        if not _is_fixture_ref(candidate.get(field), prefix):
            _add(findings, "schema.fixture_ref_required", f"/{field}")

    evidence_refs = candidate.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        _add(findings, "evidence.fixture_ref_required", "/evidence_refs")
    else:
        for index, value in enumerate(evidence_refs):
            if not _is_fixture_ref(value, "fixture:evidence:fauna:"):
                _add(
                    findings,
                    "evidence.fixture_ref_required",
                    f"/evidence_refs/{index}",
                )

    findings.extend(_geometry_findings(candidate.get("geometry")))

    governance = candidate.get("governance")
    if not isinstance(governance, Mapping):
        _add(findings, "gov.object_required", "/governance")
    else:
        for key in sorted(set(governance) - ALLOWED_GOVERNANCE_KEYS, key=str):
            _add(findings, "gov.field_forbidden", f"/governance/{key}")
        expected_governance = {
            "policy_state": "not-evaluated-fixture",
            "review_state": "fixture-only",
            "release_state": "not-released",
            "promotion_state": "not-eligible",
        }
        for field, expected in expected_governance.items():
            if governance.get(field) != expected:
                _add(findings, "gov.state_invalid", f"/governance/{field}")

    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path | str) -> ValidationResult:
    """Load and validate one UTF-8 JSON fixture."""

    try:
        candidate = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.input_invalid", "/"),))
    return validate_candidate(candidate)


def validate_fixture_manifest() -> ValidationResult:
    """Replay the exact range fixture inventory and expected findings."""

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("fixture.manifest_invalid", "/"),))
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("cases"), list):
        return ValidationResult((Finding("fixture.manifest_invalid", "/cases"),))

    findings: list[Finding] = []
    declared_paths: list[str] = []
    for index, case in enumerate(manifest["cases"]):
        if not isinstance(case, Mapping):
            _add(findings, "fixture.case_invalid", f"/cases/{index}")
            continue
        relative_path = case.get("path")
        expected = case.get("expected_findings")
        if not isinstance(relative_path, str) or not isinstance(expected, list):
            _add(findings, "fixture.case_invalid", f"/cases/{index}")
            continue
        declared_paths.append(relative_path)
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
    if declared_paths != sorted(set(declared_paths)):
        _add(findings, "fixture.paths_not_canonical", "/cases")
    if declared_paths != actual_paths:
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
        description="Validate synthetic public-safe Fauna range fixtures."
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
