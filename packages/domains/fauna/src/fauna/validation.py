"""No-network validation against an explicitly supplied canonical draft schema.

Schema and semantic conformance is separate from source admission, evidence
closure, review, release and publication. This library never resolves references.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
from referencing import Registry
from referencing.exceptions import Unresolvable

from .identity import compute_occurrence_spec_hash

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


def _schema_findings(candidate: Mapping[str, Any], schema: Mapping[str, Any]) -> list[Finding]:
    try:
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
            registry=Registry(),
        )
        errors = list(
            islice(
                validator.iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, TypeError, ValueError, RuntimeError, RecursionError, SchemaError, Unresolvable):
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


def validate_candidate(candidate: object, *, schema: Mapping[str, Any]) -> ValidationResult:
    """Validate one in-memory candidate without reading network or lifecycle stores."""

    if not isinstance(candidate, Mapping):
        return ValidationResult((Finding("schema.root_not_object", "/"),))

    findings = _schema_findings(candidate, schema)
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))

    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))
