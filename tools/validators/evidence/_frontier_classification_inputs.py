#!/usr/bin/env python3
"""Synthetic dependency fixture builders for FrontierClassification validation."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from tools.validators.evidence._frontier_classification_common import (
    _digest_ref,
    _list,
    _mapping,
    _seal_access_observation,
    _seal_frontier_definition,
    _seal_population_observation,
)


def _build_frontier_definition(scenario: Mapping[str, Any]) -> dict[str, Any]:
    definition_cfg = _mapping(scenario.get("definition"))
    subject = _mapping(scenario.get("subject"))
    criteria_cfg = [_mapping(item) for item in _list(scenario.get("criteria"))]
    criteria = [
        {
            "criterion_key": item["criterion_key"],
            "indicator_definition_ref": item["indicator_definition_ref"],
            "comparison_operator": item["comparison_operator"],
            "threshold_policy_ref": _mapping(item.get("threshold_policy"))["ref"],
            "missing_data_action": "ABSTAIN",
            "uncertainty_action": "ABSTAIN",
        }
        for item in criteria_cfg
    ]
    indicator_refs = sorted(item["indicator_definition_ref"] for item in criteria_cfg)
    value = {
        "object_type": "FrontierDefinition",
        "schema_version": "1.0.0",
        "profile": "kfm.frontier-definition.fixture.v1",
        "definition_id": "kfm:frontier-definition:" + "0" * 24,
        "frontier": {
            "definition_key": "synthetic_frontier_classification",
            "version_key": "v1",
            "label": "Synthetic frontier classification fixture definition",
            "description": (
                "Fixture-only definition with opaque indicator and threshold-policy "
                "references for deterministic local validation."
            ),
            "lifecycle_status": "PROPOSED_INACTIVE",
            "unit_level": "COUNTY",
            "jurisdiction_code": "US-KS-SYNTHETIC",
            "intended_use": "RESEARCH_AND_REVIEW",
        },
        "temporal": {
            "valid_from": definition_cfg["valid_from"],
            "valid_to": definition_cfg["valid_to"],
            "reference_period_kind": "CALENDAR_YEAR",
            "observation_valid_time_required": True,
            "geography_valid_time_alignment_required": True,
            "definition_valid_time_required": True,
        },
        "classification": {
            "combination_rule": definition_cfg["combination_rule"],
            "criteria": criteria,
            "threshold_resolution_state": "REFERENCED_NOT_RESOLVED",
            "rule_execution_state": "NOT_EXECUTED",
            "satisfied_result": "FRONTIER",
            "unsatisfied_result": "NOT_FRONTIER",
            "indeterminate_result": "UNCLASSIFIED",
        },
        "support": {
            "geography_version_ref": subject["geography_version_ref"],
            "geography_version_profile": "kfm.geography-version.fixture.v1",
            "indicator_definition_refs": indicator_refs,
            "evidence_refs": [
                "kfm://evidence-ref/frontier/synthetic-method@sha256:"
                + "6" * 64,
                "kfm://evidence-ref/frontier/synthetic-scope@sha256:"
                + "7" * 64,
            ],
            "references_state": "REFERENCED_NOT_RESOLVED",
            "different_version_join_policy": "CROSSWALK_REQUIRED",
        },
        "uncertainty": {
            "uncertainty_method_ref": (
                "kfm://method/uncertainty/synthetic-frontier@sha256:" + "8" * 64
            ),
            "classification_uncertainty_required": True,
            "missingness_disclosure_required": True,
            "provenance_required": True,
            "source_role_preservation_required": True,
        },
        "disclosure": {
            "assumption_refs": [
                "kfm://assumption/frontier/synthetic-limits@sha256:" + "a" * 64,
                "kfm://assumption/frontier/synthetic-purpose@sha256:" + "b" * 64,
            ],
            "interpretation_limits": [
                "NOT_CLASSIFICATION_RESULT",
                "NOT_OBSERVATION",
                "NO_CAUSAL_CLAIM",
                "NO_INDIVIDUAL_DECISION",
                "NO_POLICY_DECISION",
                "NO_PUBLICATION_AUTHORITY",
                "SCOPE_BOUND",
                "VERSION_BOUND",
            ],
        },
        "governance": {
            "execution_mode": "FIXTURE_ONLY",
            "network_attempted": False,
            "source_data_accessed": False,
            "geography_resolved": False,
            "indicator_definitions_resolved": False,
            "thresholds_resolved": False,
            "evidence_resolved": False,
            "rule_executed": False,
            "county_classified": False,
            "policy_evaluated": False,
            "review_approved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "public_use_allowed": False,
            "publication_authorized": False,
        },
        "spec_hash": "sha256:" + "0" * 64,
    }
    return _seal_frontier_definition(value)


def _build_access_observation(
    criterion: Mapping[str, Any],
) -> tuple[str, dict[str, Any]] | None:
    observation = _mapping(criterion.get("observation"))
    availability = observation.get("availability")
    if availability == "MISSING":
        return None
    year = int(observation["reference_year"])
    result_state = observation.get("result_state")
    corrected = observation.get("correction_state") == "CORRECTED"
    if result_state == "OBSERVED":
        measure_value = observation.get("value")
        missing_reason = "NOT_APPLICABLE"
        suppression = {"status": "NOT_APPLICABLE", "reason": None, "method_ref": None}
    elif result_state == "SUPPRESSED":
        measure_value = None
        missing_reason = "SOURCE_SUPPRESSED"
        suppression = {
            "status": "SOURCE_SUPPRESSED",
            "reason": "Synthetic fixture suppression",
            "method_ref": (
                "kfm://method/suppression/synthetic-access@sha256:" + "9" * 64
            ),
        }
    else:
        measure_value = None
        missing_reason = "SOURCE_MISSING"
        suppression = {"status": "NOT_APPLICABLE", "reason": None, "method_ref": None}
    value = {
        "object_type": "AccessObservation",
        "profile": "kfm.access-observation.fixture.v1",
        "observation_id": "kfm:access-observation:" + "0" * 24,
        "subject": {
            "geography_version_ref": observation["geography_version_ref"],
            "geography_version_profile": "kfm.geography-version.fixture.v1",
            "geography_feature_key": "99000",
            "unit_level": "COUNTY",
            "jurisdiction_code": "US-KS",
            "identity_scope": "VERSION_LOCAL",
        },
        "temporal": {
            "reference_period_kind": "CALENDAR_YEAR",
            "reference_year": year,
            "reference_period_start": f"{year:04d}-01-01",
            "reference_period_end": f"{year:04d}-12-31",
            "source_released_at": f"{year + 1:04d}-06-01T00:00:00Z",
            "retrieved_at": f"{year + 1:04d}-06-15T00:00:00Z",
            "corrected_at": f"{year + 1:04d}-07-01T00:00:00Z" if corrected else None,
        },
        "measure": {
            "measure_key": "synthetic_access_travel_time",
            "measure_family": "TRAVEL_TIME",
            "unit": "MINUTES",
            "service_domain": "HEALTHCARE",
            "source_service_ref": None,
            "result_state": result_state,
            "value": measure_value,
            "missing_reason": missing_reason,
        },
        "method": {
            "method_ref": (
                "kfm://method/synthetic-network-travel-time@sha256:" + "b" * 64
            ),
            "method_family": "NETWORK_TRAVEL_TIME",
            "origin_scope": "POPULATION_WEIGHTED",
            "destination_scope": "NEAREST_SERVICE",
            "aggregation_method": "MEDIAN",
            "threshold_ref": None,
            "network_or_model_ref": (
                "kfm://network/synthetic-road-network@sha256:" + "c" * 64
            ),
        },
        "suppression": suppression,
        "source": {
            "source_descriptor_ref": (
                "kfm://source/synthetic-service-access@sha256:" + "d" * 64
            ),
            "dataset_version_ref": (
                "kfm://dataset/synthetic-service-access@sha256:" + "e" * 64
            ),
            "source_table_ref": (
                "kfm://source-table/synthetic-county-access@sha256:" + "f" * 64
            ),
            "source_variable_ref": (
                "kfm://source-variable/synthetic-access-time@sha256:" + "1" * 64
            ),
            "source_role": "OFFICIAL_ACCESS_OR_SERVICE_AGGREGATE",
            "source_state": "REFERENCED_NOT_RESOLVED",
            "evidence_refs": [
                "kfm://evidence/access/source@sha256:" + "2" * 64,
                "kfm://evidence/access/table@sha256:" + "3" * 64,
            ],
            "rights_state": "REFERENCED_NOT_EVALUATED",
            "sensitivity_state": "REFERENCED_NOT_EVALUATED",
        },
        "lineage": {
            "correction_state": "CORRECTED" if corrected else "ORIGINAL",
            "predecessor_ref": (
                "kfm://observation/access/prior@sha256:" + "4" * 64
                if corrected
                else None
            ),
            "correction_record_ref": (
                "kfm://correction/access/synthetic@sha256:" + "5" * 64
                if corrected
                else None
            ),
        },
        "disclosure": {
            "interpretation_limits": [
                "AGGREGATE_ONLY",
                "METHOD_BOUND",
                "NO_CAUSAL_CLAIM",
                "NO_PROVIDER_ELIGIBILITY_GUARANTEE",
                "NO_PUBLICATION_AUTHORITY",
                "NO_ROUTING_OR_EMERGENCY_GUIDANCE",
                "SOURCE_ROLE_PRESERVED",
                "VERSION_BOUND",
            ]
        },
        "governance": {
            "execution_mode": "FIXTURE_ONLY",
            "network_attempted": False,
            "source_data_accessed": False,
            "geography_resolved": False,
            "evidence_resolved": False,
            "method_executed": False,
            "provider_identity_resolved": False,
            "route_computed": False,
            "rights_evaluated": False,
            "sensitivity_evaluated": False,
            "policy_evaluated": False,
            "review_approved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "public_use_allowed": False,
            "publication_authorized": False,
        },
        "spec_hash": "sha256:" + "0" * 64,
    }
    sealed = _seal_access_observation(value)
    reference = _digest_ref(
        f"observation/access/synthetic-{year}", sealed["spec_hash"]
    )
    return reference, sealed


def _build_population_observation(
    criterion: Mapping[str, Any],
) -> tuple[str, dict[str, Any]] | None:
    observation = _mapping(criterion.get("observation"))
    availability = observation.get("availability")
    if availability == "MISSING":
        return None
    year = int(observation["reference_year"])
    result_state = observation.get("result_state")
    corrected = observation.get("correction_state") == "CORRECTED"
    if result_state == "OBSERVED":
        measure_value = observation.get("value")
        missing_reason = "NOT_APPLICABLE"
        uncertainty = {
            "state": "REPORTED",
            "kind": "MARGIN_OF_ERROR",
            "value": 120,
            "confidence_level": 0.9,
            "method_ref": (
                "kfm://method/uncertainty/synthetic-population-moe@sha256:"
                + "b" * 64
            ),
        }
    elif result_state == "SUPPRESSED":
        measure_value = None
        missing_reason = "SOURCE_SUPPRESSED"
        uncertainty = {
            "state": "NOT_APPLICABLE",
            "kind": None,
            "value": None,
            "confidence_level": None,
            "method_ref": None,
        }
    else:
        measure_value = None
        missing_reason = "SOURCE_MISSING"
        uncertainty = {
            "state": "NOT_APPLICABLE",
            "kind": None,
            "value": None,
            "confidence_level": None,
            "method_ref": None,
        }
    value = {
        "object_type": "PopulationObservation",
        "schema_version": "1.0.0",
        "profile": "kfm.population-observation.fixture.v1",
        "observation_id": "kfm:population-observation:" + "0" * 24,
        "subject": {
            "geography_version_ref": observation["geography_version_ref"],
            "geography_version_profile": "kfm.geography-version.fixture.v1",
            "geography_feature_key": "99000",
            "unit_level": "COUNTY",
            "jurisdiction_code": "US-KS",
            "identity_scope": "VERSION_LOCAL",
        },
        "temporal": {
            "reference_period_kind": "CALENDAR_YEAR",
            "reference_year": year,
            "observation_date": f"{year:04d}-04-01",
            "source_released_at": f"{year + 1:04d}-01-15T00:00:00Z",
            "retrieved_at": f"{year + 1:04d}-02-01T00:00:00Z",
            "corrected_at": f"{year + 1:04d}-03-01T00:00:00Z" if corrected else None,
        },
        "measure": {
            "measure_key": "resident_population",
            "population_scope": "TOTAL_RESIDENT_POPULATION",
            "unit": "PERSONS",
            "result_state": result_state,
            "value": measure_value,
            "missing_reason": missing_reason,
        },
        "uncertainty": uncertainty,
        "source": {
            "source_descriptor_ref": (
                "kfm://source/synthetic-population@sha256:" + "c" * 64
            ),
            "dataset_version_ref": (
                "kfm://dataset/synthetic-population@sha256:" + "d" * 64
            ),
            "source_table_ref": (
                "kfm://source-table/synthetic-population-total@sha256:" + "e" * 64
            ),
            "source_variable_ref": (
                "kfm://source-variable/synthetic-resident-population@sha256:"
                + "f" * 64
            ),
            "source_role": "OFFICIAL_STATISTICAL_AGGREGATE",
            "source_state": "REFERENCED_NOT_RESOLVED",
            "evidence_refs": [
                "kfm://evidence/population/source@sha256:" + "1" * 64,
                "kfm://evidence/population/table@sha256:" + "2" * 64,
            ],
            "rights_state": "REFERENCED_NOT_EVALUATED",
            "sensitivity_state": "REFERENCED_NOT_EVALUATED",
        },
        "lineage": {
            "correction_state": "CORRECTED" if corrected else "ORIGINAL",
            "predecessor_ref": (
                "kfm://observation/population/prior@sha256:" + "3" * 64
                if corrected
                else None
            ),
            "correction_record_ref": (
                "kfm://correction/population/synthetic@sha256:" + "4" * 64
                if corrected
                else None
            ),
        },
        "disclosure": {
            "interpretation_limits": [
                "AGGREGATE_ONLY",
                "NO_CAUSAL_CLAIM",
                "NO_INDIVIDUAL_INFERENCE",
                "NO_PUBLICATION_AUTHORITY",
                "SOURCE_ROLE_PRESERVED",
                "VERSION_BOUND",
            ]
        },
        "governance": {
            "execution_mode": "FIXTURE_ONLY",
            "network_attempted": False,
            "source_data_accessed": False,
            "geography_resolved": False,
            "evidence_resolved": False,
            "rights_evaluated": False,
            "sensitivity_evaluated": False,
            "policy_evaluated": False,
            "review_approved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "public_use_allowed": False,
            "publication_authorized": False,
        },
        "spec_hash": "sha256:" + "0" * 64,
    }
    sealed = _seal_population_observation(value)
    reference = _digest_ref(
        f"observation/population/synthetic-{year}", sealed["spec_hash"]
    )
    return reference, sealed
