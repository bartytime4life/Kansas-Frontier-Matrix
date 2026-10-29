"""Prepare internal, quarantined OccurrenceEvidence without moving data."""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any, Mapping

from .identity import compute_occurrence_spec_hash
from .taxonomy import TaxonomyCatalog
from .validation import Finding, validate_candidate


@dataclass(frozen=True)
class NormalizationResult:
    outcome: str
    # Internal payload can contain exact locations; never include it in repr/logs.
    occurrence: dict[str, Any] | None = field(default=None, repr=False)
    taxonomy_snapshot_ref: str | None = None
    findings: tuple[Finding, ...] = ()


def normalize_occurrence(
    candidate: object, *, taxonomy: TaxonomyCatalog,
    schema: Mapping[str, Any], validated_at: str,
) -> NormalizationResult:
    """Normalize a source-shaped occurrence into the existing draft schema.

    The input uses OccurrenceEvidence fields. Old identity/validation assertions
    are recomputed. Exact internal coordinates and source-native values remain
    intact. Public geometry is always withheld, review is always pending, and
    every successful output remains in quarantine. Nothing writes lifecycle
    data or evaluates a release/policy decision.
    """
    if not isinstance(candidate, Mapping):
        return NormalizationResult(
            "error", findings=(Finding("schema.root_not_object", "/"),)
        )
    prior_validation = candidate.get("validation")
    prior_reasons: list[str] = []
    if "validation" in candidate and not isinstance(prior_validation, Mapping):
        return NormalizationResult(
            "error", findings=(Finding("schema.invalid", "/validation"),)
        )
    if isinstance(prior_validation, Mapping):
        prior_state = prior_validation.get("validator_result")
        if prior_state == "deny" or prior_state == "error":
            return NormalizationResult(
                prior_state,
                findings=(Finding("obs.upstream_disposition_preserved", "/validation/validator_result"),),
            )
        if prior_state not in ("pass", "quarantine"):
            return NormalizationResult(
                "error", findings=(Finding("schema.invalid", "/validation/validator_result"),)
            )
        prior_reasons = prior_validation.get("reason_codes", [])
        if not isinstance(prior_reasons, list) or not all(
            isinstance(reason, str) for reason in prior_reasons
        ):
            return NormalizationResult(
                "error", findings=(Finding("schema.invalid", "/validation/reason_codes"),)
            )
    taxon = candidate.get("taxon")
    if not isinstance(taxon, Mapping):
        return NormalizationResult(
            "error", findings=(Finding("schema.invalid", "/taxon"),)
        )
    resolution = taxonomy.resolve(taxon.get("scientific_name"))
    if resolution.concept is None:
        return NormalizationResult(
            "quarantine", taxonomy_snapshot_ref=taxonomy.snapshot_ref,
            findings=resolution.findings,
        )
    try:
        record = copy.deepcopy(dict(candidate))
        concept = resolution.concept
        record["taxon"]["accepted_scientific_name"] = concept.accepted_scientific_name
        record["taxon"]["taxon_rank"] = concept.taxon_rank
        # These fields must exist in the input; no zero coordinates, dates,
        # source roles, licenses or sensitivity classifications are inferred.
        if not isinstance(record.get("geometry"), dict) or not isinstance(
            record.get("sensitivity"), dict
        ):
            return NormalizationResult(
                "error", findings=(Finding("schema.invalid", "/geometry"),)
            )
        record["geometry"]["public_safe_geometry"] = {
            "geometry_type": "withheld", "coordinates": None,
            "precision_class": "withheld", "generalization_method": None,
        }
        record["sensitivity"].update({
            "exact_location_public_safe": False,
            "withhold_required": True,
            "review_required": True,
        })
        # Taxonomy evidence must travel with the normalized claim. Resolution
        # within a snapshot still does not resolve an EvidenceBundle.
        evidence = record["provenance"]["evidence_refs"]
        if not isinstance(evidence, list) or not evidence:
            raise TypeError
        record["provenance"]["evidence_refs"] = sorted(
            set([*evidence, taxonomy.snapshot_ref, *concept.evidence_refs])
        )
        record["spec_hash"] = compute_occurrence_spec_hash(record)
        record["occurrence_evidence_id"] = (
            "kfm://occurrence/" + record["spec_hash"].removeprefix("sha256:")
        )
        record["validation"] = {
            "validator_result": "quarantine",
            "reason_codes": sorted(set([
                *prior_reasons, "prov.evidence_closure_unverified", "sens.steward_review_required"
            ])),
            "checks": {
                "schema_valid": True, "provenance_complete": True,
                "rights_resolved": True, "sensitivity_evaluated": True,
                "geometry_public_safe": True, "taxonomy_normalized": True,
                "spec_hash_stable": True,
            },
            "evidence_strength": "unreviewed", "validator_version": "0.1.0",
            "validated_at": validated_at,
        }
        result = validate_candidate(record, schema=schema)
    except (KeyError, TypeError, ValueError, RuntimeError, RecursionError):
        return NormalizationResult(
            "error", findings=(Finding("schema.input_invalid", "/"),)
        )
    if not result.ok:
        return NormalizationResult(
            "error", taxonomy_snapshot_ref=taxonomy.snapshot_ref,
            findings=result.findings,
        )
    return NormalizationResult("quarantine", record, taxonomy.snapshot_ref)
