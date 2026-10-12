#!/usr/bin/env python3
"""Validate the draft KFM Fauna OccurrenceEvidence machine profile.

The validator is deterministic, no-network, fixture-first, and non-authoritative.
A PASS means only that the declared object satisfies the draft schema and the
bounded semantic checks in this module. It does not admit a source, resolve an
EvidenceBundle, approve policy or steward review, release data, or publish an
occurrence.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[5]
HASH_SRC = ROOT / "packages" / "hashing" / "src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

try:
    from hashing import JsonInputError, compute_spec_hash, load_json_file
except ImportError as exc:  # pragma: no cover - exercised as a fail-closed CLI path
    JsonInputError = ValueError  # type: ignore[assignment]
    _HASH_IMPORT_ERROR: Exception | None = exc
else:
    _HASH_IMPORT_ERROR = None

SCHEMA_PATH = (
    ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "domains"
    / "fauna"
    / "occurrence_evidence.schema.json"
)
FIXTURE_ROOT = ROOT / "fixtures" / "domains" / "fauna" / "occurrence_evidence"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
SCOPE = "fauna-occurrence-evidence-draft-v1"
MAX_SCHEMA_FINDINGS = 100

DIRECT_BASIS = frozenset(
    {
        "human_observation",
        "machine_observation",
        "preserved_specimen",
        "material_sample",
        "living_specimen",
        "fossil_specimen",
        "literature_record",
    }
)
ROLE_BASIS = {
    "regulatory": frozenset({"regulatory_record"}),
    "modeled": frozenset({"model_output"}),
    "aggregate": frozenset({"aggregate_summary"}),
    "administrative": frozenset({"administrative_record"}),
    "candidate": frozenset({"candidate_report"}),
    "synthetic": frozenset({"synthetic_reconstruction"}),
}
RAW_ARTIFACT_ROLES = frozenset(
    {"observed", "regulatory", "administrative", "candidate"}
)


@dataclass(frozen=True, order=True)
class Finding:
    """Stable machine-comparable validator finding."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite result for one occurrence-evidence candidate."""

    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        return "PASS" if self.ok else "ERROR"


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code=code, path=path)
    if finding not in findings:
        findings.append(finding)


def _load_schema() -> Mapping[str, Any]:
    if _HASH_IMPORT_ERROR is not None:
        raise RuntimeError("hashing package unavailable") from _HASH_IMPORT_ERROR
    schema = load_json_file(SCHEMA_PATH)
    if not isinstance(schema, Mapping):
        raise RuntimeError("schema root is not an object")
    Draft202012Validator.check_schema(schema)
    return schema


def occurrence_identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return the exact Pass-3 identity subject for RFC 8785 + SHA-256."""

    observation = candidate.get("observation")
    geometry = candidate.get("geometry")
    taxon = candidate.get("taxon")
    if not isinstance(observation, Mapping):
        observation = {}
    if not isinstance(geometry, Mapping):
        geometry = {}
    if not isinstance(taxon, Mapping):
        taxon = {}

    normalized_geometry = {
        "geoprivacy_status": geometry.get("geoprivacy_status"),
        "latitude": geometry.get("latitude"),
        "longitude": geometry.get("longitude"),
        "precision_class": geometry.get("precision_class"),
        "public_safe_geometry": geometry.get("public_safe_geometry"),
    }
    return {
        "accepted_taxon_name": taxon.get("accepted_scientific_name"),
        "event_date": observation.get("event_date"),
        "normalized_geometry": normalized_geometry,
        "source_record_id": candidate.get("source_record_id"),
    }


def compute_occurrence_spec_hash(candidate: Mapping[str, Any]) -> str:
    """Compute the deterministic occurrence identity digest."""

    if _HASH_IMPORT_ERROR is not None:
        raise RuntimeError("hashing package unavailable") from _HASH_IMPORT_ERROR
    return compute_spec_hash(occurrence_identity_subject(candidate))


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        validator = Draft202012Validator(
            _load_schema(),
            format_checker=FormatChecker(),
        )
        errors = list(
            islice(
                validator.iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, ValueError, RuntimeError, RecursionError):
        return [Finding("schema.unavailable", "/")]

    findings = [
        Finding("schema.invalid", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("schema.findings_truncated", "/"))
    return findings


def _rights_resolved(rights: Mapping[str, Any]) -> bool:
    license_value = rights.get("license")
    return (
        isinstance(license_value, str)
        and license_value.strip().upper() not in {"", "UNKNOWN", "UNRESOLVED"}
        and isinstance(rights.get("redistribution_allowed"), bool)
        and isinstance(rights.get("commercial_use_allowed"), bool)
        and isinstance(rights.get("attribution_required"), bool)
    )


def _taxonomy_normalized(taxon: Mapping[str, Any]) -> bool:
    accepted = taxon.get("accepted_scientific_name")
    return (
        isinstance(accepted, str)
        and accepted.strip()
        and accepted.strip().upper() not in {"UNKNOWN", "UNRESOLVED"}
    )


def _role_matches_basis(role: object, basis: object) -> bool:
    if role == "observed":
        return basis in DIRECT_BASIS
    accepted = ROLE_BASIS.get(role)
    return accepted is not None and basis in accepted


def _geometry_findings(
    candidate: Mapping[str, Any],
    findings: list[Finding],
) -> bool:
    geometry = candidate["geometry"]
    sensitivity = candidate["sensitivity"]
    assert isinstance(geometry, Mapping)
    assert isinstance(sensitivity, Mapping)

    before = len(findings)
    geoprivacy = geometry.get("geoprivacy_status")
    public_safe = geometry.get("public_safe_geometry")
    generalization = sensitivity.get("generalization_required") is True
    withhold = sensitivity.get("withhold_required") is True
    exact_safe = sensitivity.get("exact_location_public_safe") is True

    if (geoprivacy != "open" or generalization or withhold) and not isinstance(
        public_safe, Mapping
    ):
        _add(findings, "geom.public_safe_geometry_required", "/geometry/public_safe_geometry")

    if isinstance(public_safe, Mapping):
        public_precision = public_safe.get("precision_class")
        public_type = public_safe.get("geometry_type")
        if generalization and public_precision == "exact":
            _add(
                findings,
                "geom.public_safe_precision_invalid",
                "/geometry/public_safe_geometry/precision_class",
            )
        if withhold and public_type != "withheld":
            _add(
                findings,
                "geom.withheld_geometry_required",
                "/geometry/public_safe_geometry/geometry_type",
            )
        if public_type == "withheld" and public_safe.get("coordinates") is not None:
            _add(
                findings,
                "geom.withheld_coordinates_forbidden",
                "/geometry/public_safe_geometry/coordinates",
            )

    if exact_safe:
        if geoprivacy != "open" or generalization or withhold:
            _add(
                findings,
                "sens.exact_location_public_safe_conflict",
                "/sensitivity/exact_location_public_safe",
            )
        if not isinstance(public_safe, Mapping) or public_safe.get("precision_class") != "exact":
            _add(
                findings,
                "geom.exact_public_geometry_required",
                "/geometry/public_safe_geometry",
            )

    if sensitivity.get("sensitive_species_flag") is True and sensitivity.get(
        "review_required"
    ) is not True:
        _add(findings, "sens.review_required", "/sensitivity/review_required")

    return len(findings) == before


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    taxon = candidate["taxon"]
    observation = candidate["observation"]
    rights = candidate["rights"]
    sensitivity = candidate["sensitivity"]
    provenance = candidate["provenance"]
    validation = candidate["validation"]
    assert isinstance(taxon, Mapping)
    assert isinstance(observation, Mapping)
    assert isinstance(rights, Mapping)
    assert isinstance(sensitivity, Mapping)
    assert isinstance(provenance, Mapping)
    assert isinstance(validation, Mapping)

    try:
        computed_hash = compute_occurrence_spec_hash(candidate)
    except (TypeError, ValueError, RuntimeError, RecursionError):
        _add(findings, "identity.hash_unavailable", "/spec_hash")
        computed_hash = None

    declared_hash = candidate.get("spec_hash")
    hash_stable = computed_hash is not None and declared_hash == computed_hash
    if not hash_stable:
        _add(findings, "identity.spec_hash_mismatch", "/spec_hash")

    expected_id = (
        f"kfm://occurrence/{computed_hash.removeprefix('sha256:')}"
        if computed_hash is not None
        else None
    )
    if expected_id is None or candidate.get("occurrence_evidence_id") != expected_id:
        _add(
            findings,
            "identity.occurrence_id_mismatch",
            "/occurrence_evidence_id",
        )

    role = candidate.get("source_role")
    basis = observation.get("basis_of_record")
    role_matches = _role_matches_basis(role, basis)
    if not role_matches:
        _add(findings, "obs.source_role_mismatch", "/observation/basis_of_record")

    rights_resolved = _rights_resolved(rights)
    if not rights_resolved:
        _add(findings, "rights.unresolved", "/rights")

    taxonomy_normalized = _taxonomy_normalized(taxon)
    if not taxonomy_normalized:
        _add(
            findings,
            "taxon.accepted_name_unresolved",
            "/taxon/accepted_scientific_name",
        )

    raw_required = role in RAW_ARTIFACT_ROLES
    raw_present = isinstance(provenance.get("raw_artifact_ref"), str) and bool(
        str(provenance.get("raw_artifact_ref")).strip()
    )
    provenance_complete = not raw_required or raw_present
    if not provenance_complete:
        _add(
            findings,
            "prov.raw_artifact_ref_required",
            "/provenance/raw_artifact_ref",
        )

    geometry_before = len(findings)
    _geometry_findings(candidate, findings)
    geometry_public_safe = len(findings) == geometry_before

    evidence_strength = validation.get("evidence_strength")
    review_pending = (
        sensitivity.get("review_required") is True
        and evidence_strength != "steward_reviewed"
    )
    declared_reasons = validation.get("reason_codes")
    if not isinstance(declared_reasons, list):
        declared_reasons = []
    if declared_reasons != sorted(set(declared_reasons)):
        _add(findings, "schema.reason_codes_not_canonical", "/validation/reason_codes")

    expected_hold_reason = "sens.steward_review_required"
    if review_pending and expected_hold_reason not in declared_reasons:
        _add(
            findings,
            "sens.review_reason_required",
            "/validation/reason_codes",
        )
    if not review_pending and expected_hold_reason in declared_reasons:
        _add(
            findings,
            "sens.review_reason_stale",
            "/validation/reason_codes",
        )

    sensitivity_evaluated = not (
        sensitivity.get("withhold_required") is True
        and sensitivity.get("exact_location_public_safe") is True
    )

    actual_checks = {
        "schema_valid": True,
        "provenance_complete": provenance_complete,
        "rights_resolved": rights_resolved,
        "sensitivity_evaluated": sensitivity_evaluated,
        "geometry_public_safe": geometry_public_safe,
        "taxonomy_normalized": taxonomy_normalized,
        "spec_hash_stable": hash_stable,
    }
    declared_checks = validation.get("checks")
    if isinstance(declared_checks, Mapping):
        for check_name, actual in actual_checks.items():
            if declared_checks.get(check_name) is not actual:
                _add(
                    findings,
                    "schema.validation_check_mismatch",
                    f"/validation/checks/{check_name}",
                )

    result = validation.get("validator_result")
    all_gates = all(actual_checks.values()) and role_matches
    if result == "pass":
        if review_pending or not all_gates or declared_reasons:
            _add(
                findings,
                "schema.pass_gate_failed",
                "/validation/validator_result",
            )
    else:
        if not declared_reasons:
            _add(
                findings,
                "schema.reason_code_required",
                "/validation/reason_codes",
            )
        if review_pending and result not in {"quarantine", "deny"}:
            _add(
                findings,
                "sens.review_result_invalid",
                "/validation/validator_result",
            )

    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    """Validate one in-memory candidate without reading network or lifecycle stores."""

    if not isinstance(candidate, Mapping):
        return ValidationResult((Finding("schema.root_not_object", "/"),))

    findings = _schema_findings(candidate)
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))

    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path | str) -> ValidationResult:
    """Load and validate one bounded JSON file."""

    if _HASH_IMPORT_ERROR is not None:
        return ValidationResult((Finding("schema.hashing_unavailable", "/"),))
    try:
        candidate = load_json_file(Path(path))
    except JsonInputError:
        return ValidationResult((Finding("schema.input_invalid", "/"),))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.input_error", "/"),))
    return validate_candidate(candidate)


def validate_fixture_manifest() -> ValidationResult:
    """Replay every declared fixture and compare exact expected findings."""

    if _HASH_IMPORT_ERROR is not None:
        return ValidationResult((Finding("schema.hashing_unavailable", "/"),))
    try:
        manifest = load_json_file(MANIFEST_PATH)
    except (JsonInputError, OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/"),))
    if not isinstance(manifest, Mapping):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/"),))

    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/cases"),))

    findings: list[Finding] = []
    declared_paths: list[str] = []
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            _add(findings, "schema.fixture_case_invalid", f"/cases/{index}")
            continue
        relative_path = case.get("path")
        expected = case.get("expected_findings")
        if not isinstance(relative_path, str) or not isinstance(expected, list):
            _add(findings, "schema.fixture_case_invalid", f"/cases/{index}")
            continue
        declared_paths.append(relative_path)
        fixture_path = FIXTURE_ROOT / relative_path
        actual = validate_file(fixture_path).findings
        expected_pairs: list[Finding] = []
        for expected_index, item in enumerate(expected):
            if not isinstance(item, Mapping):
                _add(
                    findings,
                    "schema.fixture_expectation_invalid",
                    f"/cases/{index}/expected_findings/{expected_index}",
                )
                continue
            code = item.get("code")
            path = item.get("path")
            if not isinstance(code, str) or not isinstance(path, str):
                _add(
                    findings,
                    "schema.fixture_expectation_invalid",
                    f"/cases/{index}/expected_findings/{expected_index}",
                )
                continue
            expected_pairs.append(Finding(code, path))
        if tuple(sorted(expected_pairs)) != actual:
            _add(
                findings,
                "schema.fixture_outcome_mismatch",
                f"/cases/{index}",
            )

    if declared_paths != sorted(set(declared_paths)):
        _add(findings, "schema.fixture_paths_not_canonical", "/cases")

    actual_paths = sorted(
        str(path.relative_to(FIXTURE_ROOT))
        for folder in (FIXTURE_ROOT / "valid", FIXTURE_ROOT / "semantic_invalid")
        for path in folder.glob("*.json")
    )
    if declared_paths != actual_paths:
        _add(findings, "schema.fixture_inventory_mismatch", "/cases")

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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate draft Fauna OccurrenceEvidence JSON without network."
    )
    parser.add_argument("paths", nargs="*", help="JSON files to validate")
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="replay the exact fixture manifest",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        result = validate_fixture_manifest()
        print(json.dumps(_payload("fixture-manifest", result), sort_keys=True))
        return 0 if result.ok else 1
    if not args.paths:
        build_parser().error("provide at least one path or --fixtures")

    exit_code = 0
    for raw_path in args.paths:
        result = validate_file(Path(raw_path))
        print(json.dumps(_payload(raw_path, result), sort_keys=True))
        if not result.ok:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
