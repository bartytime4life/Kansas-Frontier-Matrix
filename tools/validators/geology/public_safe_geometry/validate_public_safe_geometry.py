#!/usr/bin/env python3
"""Validate synthetic Geology public-safe geometry assessment metadata.

The profile accepts no coordinates or geometry bytes. It checks declarations
about exact/internal separation, generalized or withheld public posture, and
synthetic governance summaries. It performs no transform, evidence resolution,
policy evaluation, review, release, serving, export, or publication.
"""

from __future__ import annotations

import argparse
import copy
import hmac
import json
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for import_root in (REPO_ROOT, HASHING_SRC):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from hashing import compute_spec_hash  # noqa: E402
from tools.validators._common.public_safe_fixture import (  # noqa: E402
    validate_fixture_file,
)


SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/geology/"
    "public_safe_geometry_assessment.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/domains/geology/"
    "public_safe_geometry/cases.json"
)
PROFILE = "kfm-geology-public-safe-geometry-fixture-v1"
SCOPE = "geology-public-safe-geometry-metadata-only"
NON_EFFECTS = (
    "no_coordinate_or_geometry_byte_consumption",
    "no_geometry_transform_or_topology_operation",
    "no_source_rights_or_evidence_resolution",
    "no_live_policy_evaluation_or_review",
    "no_lifecycle_or_receipt_write",
    "no_release_map_api_export_or_publication",
)
LIMITATIONS = (
    "fixture_only",
    "metadata_only_no_geometry_bytes",
    "no_live_policy_evaluation",
    "no_release_or_publication",
    "no_review_performed",
    "no_transform_execution",
)
OBJECT_SENSITIVITY = {
    "BoreholeReference": "EXACT_SUBSURFACE",
    "GeochemistrySample": "SAMPLE_LOCALITY",
    "GeologyBoundaryVersion": "CANONICAL_BOUNDARY",
    "MineralOccurrence": "RESOURCE_TARGET",
    "ResourceDeposit": "RESOURCE_TARGET",
}
FORBIDDEN_LOCATION_FIELDS = frozenset(
    {
        "bbox",
        "centroid",
        "coordinate",
        "coordinates",
        "easting",
        "geojson",
        "geometry",
        "geometry_bytes",
        "lat",
        "latitude",
        "lng",
        "lon",
        "longitude",
        "northing",
        "wkb",
        "wkt",
        "x",
        "y",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic finding that never includes candidate values."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite assessment result."""

    outcome: str
    findings: tuple[Finding, ...]


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


@lru_cache(maxsize=1)
def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    """Return the deterministic hash for the declared assessment content."""

    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    """Derive a stable fixture assessment identifier from the spec hash."""

    return (
        "kfm:geology:public-safe-geometry:"
        + spec_hash.removeprefix("sha256:")[:24]
    )


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code, path))


def _schema_findings(document: object) -> set[Finding]:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    return {
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:100]
    }


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _find_location_fields(
    value: object,
    findings: set[Finding],
    path: str = "",
) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_path = f"{path}/{str(key).replace('~', '~0').replace('/', '~1')}"
            if key in FORBIDDEN_LOCATION_FIELDS:
                _add(findings, "LOCATION_FIELD_DENIED", child_path)
            _find_location_fields(child, findings, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _find_location_fields(child, findings, f"{path}/{index}")


def _canonical_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) and bool(item) for item in value)
        and value == sorted(set(value))
    )


def _expected_assessment(disposition: object) -> tuple[str, list[str], list[str]]:
    if disposition == "GENERALIZED":
        return (
            "HOLD",
            ["RELEASE_AUTHORITY_UNWIRED"],
            ["PUBLICATION_REVIEW", "RELEASE_MANIFEST"],
        )
    if disposition == "WITHHELD":
        return "DENY", ["PUBLIC_GEOMETRY_WITHHELD"], []
    return "DENY", ["EXACT_PUBLIC_GEOMETRY_DENIED"], []


def _generalized_findings(
    source: Mapping[str, Any],
    public: Mapping[str, Any],
    governance: Mapping[str, Any],
    findings: set[Finding],
) -> None:
    if public.get("geometry_role") != "GENERALIZED_PUBLIC":
        _add(findings, "PUBLIC_GEOMETRY_ROLE_MISMATCH", "/public_derivative/geometry_role")
    public_ref = public.get("geometry_ref")
    if public_ref is None:
        _add(findings, "PUBLIC_GEOMETRY_REF_REQUIRED", "/public_derivative/geometry_ref")
    elif public_ref == source.get("geometry_ref"):
        _add(findings, "PUBLIC_GEOMETRY_REF_NOT_DERIVED", "/public_derivative/geometry_ref")
    if public.get("generalization_method") not in {
        "ADMINISTRATIVE_AREA",
        "SOURCE_SCALE",
    }:
        _add(
            findings,
            "GENERALIZATION_METHOD_REQUIRED",
            "/public_derivative/generalization_method",
        )
    source_scale = source.get("scale_denominator")
    public_scale = public.get("scale_denominator")
    if not (
        isinstance(source_scale, int)
        and not isinstance(source_scale, bool)
        and isinstance(public_scale, int)
        and not isinstance(public_scale, bool)
        and public_scale > source_scale
    ):
        _add(
            findings,
            "PUBLIC_SCALE_NOT_COARSER",
            "/public_derivative/scale_denominator",
        )
    if public.get("crs_ref") is None:
        _add(findings, "PUBLIC_CRS_REF_REQUIRED", "/public_derivative/crs_ref")
    if public.get("uncertainty_disclosed") is not True:
        _add(
            findings,
            "UNCERTAINTY_DISCLOSURE_REQUIRED",
            "/public_derivative/uncertainty_disclosed",
        )
    if governance.get("transform_receipt_ref") is None:
        _add(
            findings,
            "TRANSFORM_RECEIPT_REQUIRED",
            "/governance/transform_receipt_ref",
        )
    if governance.get("policy_decision_ref") is None:
        _add(findings, "POLICY_DECISION_REF_REQUIRED", "/governance/policy_decision_ref")
    if governance.get("review_record_ref") is None:
        _add(findings, "REVIEW_RECORD_REF_REQUIRED", "/governance/review_record_ref")
    if governance.get("rights_state") != "VERIFIED":
        _add(findings, "RIGHTS_NOT_VERIFIED", "/governance/rights_state")
    if governance.get("policy_outcome") != "ALLOW_GENERALIZED":
        _add(
            findings,
            "GENERALIZATION_POLICY_MISMATCH",
            "/governance/policy_outcome",
        )
    if governance.get("review_state") != "APPROVED":
        _add(
            findings,
            "GENERALIZATION_REVIEW_MISMATCH",
            "/governance/review_state",
        )


def _withheld_findings(
    public: Mapping[str, Any],
    governance: Mapping[str, Any],
    findings: set[Finding],
) -> None:
    expected = {
        "geometry_ref": None,
        "geometry_role": "WITHHELD",
        "generalization_method": "WITHHELD",
        "crs_ref": None,
        "scale_denominator": None,
    }
    for field, value in expected.items():
        if public.get(field) != value:
            _add(
                findings,
                "WITHHELD_DERIVATIVE_MISMATCH",
                f"/public_derivative/{field}",
            )
    if governance.get("transform_receipt_ref") is None:
        _add(
            findings,
            "TRANSFORM_RECEIPT_REQUIRED",
            "/governance/transform_receipt_ref",
        )
    if governance.get("policy_outcome") != "WITHHOLD":
        _add(findings, "WITHHOLD_POLICY_MISMATCH", "/governance/policy_outcome")


def _exact_request_findings(
    source: Mapping[str, Any],
    public: Mapping[str, Any],
    governance: Mapping[str, Any],
    findings: set[Finding],
) -> None:
    if public.get("geometry_role") != "EXACT_PUBLIC_REQUEST":
        _add(findings, "EXACT_REQUEST_ROLE_MISMATCH", "/public_derivative/geometry_role")
    if public.get("geometry_ref") is None:
        _add(findings, "EXACT_REQUEST_REF_REQUIRED", "/public_derivative/geometry_ref")
    if public.get("generalization_method") != "NONE":
        _add(
            findings,
            "EXACT_REQUEST_METHOD_MISMATCH",
            "/public_derivative/generalization_method",
        )
    if public.get("scale_denominator") != source.get("scale_denominator"):
        _add(findings, "EXACT_REQUEST_SCALE_MISMATCH", "/public_derivative/scale_denominator")
    if governance.get("transform_receipt_ref") is not None:
        _add(
            findings,
            "EXACT_REQUEST_TRANSFORM_RECEIPT_DENIED",
            "/governance/transform_receipt_ref",
        )
    if governance.get("policy_outcome") != "DENY":
        _add(findings, "EXACT_REQUEST_POLICY_MISMATCH", "/governance/policy_outcome")


def validate_payload(document: object) -> ValidationResult:
    """Validate a materialized assessment and derive its finite outcome."""

    schema_findings = _schema_findings(document)
    if schema_findings:
        return ValidationResult("DENY", tuple(sorted(schema_findings)))
    assert isinstance(document, Mapping)

    findings: set[Finding] = set()
    _find_location_fields(document, findings)

    expected_hash = expected_spec_hash(document)
    spec_hash = document.get("spec_hash")
    if not (
        isinstance(spec_hash, str)
        and hmac.compare_digest(spec_hash, expected_hash)
    ):
        _add(findings, "SPEC_HASH_MISMATCH", "/spec_hash")
    expected_id = expected_assessment_id(expected_hash)
    assessment_id = document.get("assessment_id")
    if not (
        isinstance(assessment_id, str)
        and hmac.compare_digest(assessment_id, expected_id)
    ):
        _add(findings, "ASSESSMENT_ID_MISMATCH", "/assessment_id")

    if document.get("limitations") != list(LIMITATIONS):
        _add(findings, "LIMITATIONS_MISMATCH", "/limitations")

    source = _mapping(document.get("source_geometry"))
    public = _mapping(document.get("public_derivative"))
    governance = _mapping(document.get("governance"))
    assessment = _mapping(document.get("assessment"))

    if source.get("coordinate_material_present") is not False:
        _add(
            findings,
            "SOURCE_COORDINATE_MATERIAL_DENIED",
            "/source_geometry/coordinate_material_present",
        )
    if public.get("coordinate_material_present") is not False:
        _add(
            findings,
            "PUBLIC_COORDINATE_MATERIAL_DENIED",
            "/public_derivative/coordinate_material_present",
        )
    if source.get("geometry_role") != "INTERNAL_EXACT":
        _add(findings, "SOURCE_GEOMETRY_ROLE_INVALID", "/source_geometry/geometry_role")
    if source.get("storage_class") != "RESTRICTED":
        _add(findings, "EXACT_SOURCE_STORAGE_DENIED", "/source_geometry/storage_class")

    expected_sensitivity = OBJECT_SENSITIVITY.get(document.get("object_family"))
    if source.get("sensitivity_class") != expected_sensitivity:
        _add(
            findings,
            "SENSITIVITY_CLASS_MISMATCH",
            "/source_geometry/sensitivity_class",
        )

    evidence_refs = governance.get("evidence_refs")
    if not _canonical_string_list(evidence_refs) or not _list(evidence_refs):
        _add(findings, "EVIDENCE_REFS_NOT_CANONICAL", "/governance/evidence_refs")
    if governance.get("release_manifest_ref") is not None:
        _add(
            findings,
            "RELEASE_MANIFEST_REF_DENIED",
            "/governance/release_manifest_ref",
        )
    if governance.get("release_state") != "NOT_RELEASED":
        _add(findings, "RELEASE_STATE_DENIED", "/governance/release_state")
    if governance.get("publication_authorized") is not False:
        _add(
            findings,
            "PUBLICATION_AUTHORITY_DENIED",
            "/governance/publication_authorized",
        )

    disposition = public.get("disposition")
    if disposition == "GENERALIZED":
        _generalized_findings(source, public, governance, findings)
    elif disposition == "WITHHELD":
        _withheld_findings(public, governance, findings)
    else:
        _exact_request_findings(source, public, governance, findings)

    expected_outcome, expected_reasons, expected_gates = _expected_assessment(
        disposition
    )
    if assessment.get("outcome") != expected_outcome:
        _add(findings, "ASSESSMENT_OUTCOME_MISMATCH", "/assessment/outcome")
    if assessment.get("reason_codes") != expected_reasons:
        _add(
            findings,
            "ASSESSMENT_REASON_CODES_MISMATCH",
            "/assessment/reason_codes",
        )
    if assessment.get("required_next_gates") != expected_gates:
        _add(
            findings,
            "ASSESSMENT_NEXT_GATES_MISMATCH",
            "/assessment/required_next_gates",
        )

    return ValidationResult(
        "DENY" if findings else expected_outcome,
        tuple(sorted(findings)),
    )


def load_fixtures() -> dict[str, Any]:
    """Load the frozen case manifest."""

    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest must be an object")
    return value


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be a JSON pointer")
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    """Apply one frozen mutation set and recompute identity fields."""

    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    return document


def validate_file(path: Path | str) -> ValidationResult:
    """Use shared bounded parsing mechanics, then validate one assessment."""

    captured: list[object] = []

    def capture(candidate: object) -> list[Any]:
        captured.append(candidate)
        return []

    parser_findings = validate_fixture_file(path, capture)
    if parser_findings:
        converted = tuple(Finding(item.code, item.path) for item in parser_findings)
        return ValidationResult("ERROR", converted)
    if len(captured) != 1:
        return ValidationResult("ERROR", (Finding("FIXTURE_JSON_INVALID", "/"),))
    return validate_payload(captured[0])


def render_result(result: ValidationResult) -> str:
    payload = {
        "authority": "NONE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "non_effects": list(NON_EFFECTS),
        "outcome": result.outcome,
        "scope": SCOPE,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _run_fixture_suite() -> int:
    manifest = load_fixtures()
    rows = []
    suite_match = True
    for case in manifest["cases"]:
        document = materialize_case(manifest, case)
        result = validate_payload(document)
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        case_match = (
            result.outcome == case["expected_outcome"]
            and actual_findings == case["expected_findings"]
        )
        suite_match = suite_match and case_match
        rows.append(
            {
                "case_id": case["case_id"],
                "match": case_match,
                "outcome": result.outcome,
            }
        )
    payload = {
        "authority": "NONE",
        "case_count": len(rows),
        "cases": rows,
        "non_effects": list(NON_EFFECTS),
        "profile_id": PROFILE,
        "suite_match": suite_match,
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0 if suite_match else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="validate the frozen synthetic case matrix",
    )
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("path cannot be combined with --fixtures")
        return _run_fixture_suite()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(render_result(result))
    if result.outcome == "ERROR":
        return 2
    return 0 if result.outcome == "HOLD" else 1


if __name__ == "__main__":
    raise SystemExit(main())
