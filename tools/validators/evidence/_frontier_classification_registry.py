#!/usr/bin/env python3
"""Sealed local panel and evidence registry helpers for FrontierClassification fixtures."""
from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any

from tools.validators.evidence._frontier_classification_common import (
    _digest_ref,
    _list,
    _mapping,
    _seal_county_year_panel,
    compute_spec_hash,
)

def _panel_slot(
    criterion: Mapping[str, Any], observation_ref: str | None
) -> dict[str, Any]:
    observation = _mapping(criterion.get("observation"))
    availability = observation.get("availability")
    source_role_ref = criterion.get("source_role_ref")
    if criterion.get("source_role_mirror_state") == "MISMATCH":
        source_role_ref = (
            "kfm://source-role/synthetic-mismatch@sha256:" + "d" * 64
        )
    uncertainty = _mapping(criterion.get("uncertainty"))
    evidence = _mapping(criterion.get("evidence"))
    if availability == "MISSING":
        reason = (
            "GEOGRAPHY_ALIGNMENT_UNRESOLVED"
            if observation.get("geography_alignment") == "UNRESOLVED"
            else "SOURCE_MISSING"
        )
        return {
            "observation_kind": criterion["observation_kind"],
            "indicator_definition_ref": criterion["indicator_definition_ref"],
            "source_role_ref": source_role_ref,
            "observation_geography_version_ref": observation["geography_version_ref"],
            "geography_alignment": observation["geography_alignment"],
            "geography_crosswalk_ref": observation.get("geography_crosswalk_ref"),
            "availability": "MISSING",
            "observation_ref": None,
            "uncertainty_ref": None,
            "evidence_refs": [],
            "reason_code": reason,
        }
    if availability == "SUPPRESSED":
        return {
            "observation_kind": criterion["observation_kind"],
            "indicator_definition_ref": criterion["indicator_definition_ref"],
            "source_role_ref": source_role_ref,
            "observation_geography_version_ref": observation["geography_version_ref"],
            "geography_alignment": observation["geography_alignment"],
            "geography_crosswalk_ref": observation.get("geography_crosswalk_ref"),
            "availability": "SUPPRESSED",
            "observation_ref": None,
            "uncertainty_ref": None,
            "evidence_refs": [evidence["ref"]],
            "reason_code": "POLICY_SUPPRESSED",
        }
    return {
        "observation_kind": criterion["observation_kind"],
        "indicator_definition_ref": criterion["indicator_definition_ref"],
        "source_role_ref": source_role_ref,
        "observation_geography_version_ref": observation["geography_version_ref"],
        "geography_alignment": observation["geography_alignment"],
        "geography_crosswalk_ref": observation.get("geography_crosswalk_ref"),
        "availability": "AVAILABLE",
        "observation_ref": observation_ref,
        "uncertainty_ref": uncertainty["ref"],
        "evidence_refs": [evidence["ref"]],
        "reason_code": "NONE",
    }


def _fixed_panel_slot(kind: str, geo_ref: str) -> dict[str, Any]:
    values = {
        "AGRICULTURE": ("12", "23", "34", "45", "56"),
        "ECONOMIC": ("67", "78", "89", "90", "ab"),
    }[kind]
    return {
        "observation_kind": kind,
        "indicator_definition_ref": (
            f"kfm://indicator-definition/{kind.lower()}-fixture@sha256:" + values[0] * 32
        ),
        "source_role_ref": (
            f"kfm://source-role/synthetic-{kind.lower()}@sha256:" + values[1] * 32
        ),
        "observation_geography_version_ref": geo_ref,
        "geography_alignment": "SAME_VERSION",
        "geography_crosswalk_ref": None,
        "availability": "AVAILABLE",
        "observation_ref": (
            f"kfm://observation/{kind.lower()}/synthetic-2020@sha256:" + values[2] * 32
        ),
        "uncertainty_ref": (
            f"kfm://uncertainty/{kind.lower()}/synthetic-2020@sha256:" + values[3] * 32
        ),
        "evidence_refs": [
            f"kfm://evidence-ref/{kind.lower()}/synthetic-2020@sha256:"
            + values[4] * 32
        ],
        "reason_code": "NONE",
    }


def _build_county_year_panel(
    scenario: Mapping[str, Any],
    definition: Mapping[str, Any],
    observations: Mapping[str, dict[str, Any]],
) -> dict[str, Any]:
    subject = _mapping(scenario.get("subject"))
    criteria = {_mapping(item)["observation_kind"]: _mapping(item) for item in _list(scenario.get("criteria"))}
    access_ref = next(
        (ref for ref, wrapper in observations.items() if wrapper["kind"] == "ACCESS"),
        None,
    )
    population_ref = next(
        (ref for ref, wrapper in observations.items() if wrapper["kind"] == "POPULATION"),
        None,
    )
    slots = [
        _panel_slot(criteria["ACCESS"], access_ref),
        _fixed_panel_slot("AGRICULTURE", subject["geography_version_ref"]),
        _fixed_panel_slot("ECONOMIC", subject["geography_version_ref"]),
        _panel_slot(criteria["POPULATION"], population_ref),
    ]
    unavailable = [item for item in slots if item["availability"] != "AVAILABLE"]
    reason_codes = ["OBSERVATION_GAPS_PRESENT"] if unavailable else ["ALL_REQUIRED_OBSERVATIONS_AVAILABLE"]
    if any(item["availability"] == "SUPPRESSED" for item in slots):
        reason_codes.append("SUPPRESSED_OBSERVATION_PRESENT")
    if any(item["geography_alignment"] == "UNRESOLVED" for item in slots):
        reason_codes.append("UNRESOLVED_GEOGRAPHY_ALIGNMENT")
    definition_ref = _digest_ref(
        "frontier-definition/synthetic-v1", definition["spec_hash"]
    )
    value = {
        "object_type": "CountyYearPanel",
        "schema_version": "1.0.0",
        "profile": "kfm.county-year-panel.fixture.v1",
        "panel_id": "kfm:county-year-panel:" + "0" * 24,
        "panel_scope": {
            "panel_key": "synthetic_county_2020",
            "county_identifier_digest": subject["county_identifier_digest"],
            "calendar_year": subject["calendar_year"],
            "geography_version_ref": subject["geography_version_ref"],
            "frontier_definition_ref": definition_ref,
        },
        "observations": slots,
        "summary": {
            "panel_state": "PARTIAL" if unavailable else "COMPLETE",
            "decision": "HOLD" if unavailable else "REVIEW_CANDIDATE",
            "reason_codes": sorted(reason_codes),
        },
        "support": {
            "source_roles_preserved": True,
            "evidence_state": "REFERENCED_NOT_RESOLVED",
            "panel_evidence_refs": [
                "kfm://evidence-ref/county-year-panel/definitions@sha256:"
                + "01" * 32,
                "kfm://evidence-ref/county-year-panel/scope@sha256:"
                + "02" * 32,
            ],
            "assumption_refs": [
                "kfm://assumption/county-year-panel/aggregate-only@sha256:"
                + "03" * 32,
                "kfm://assumption/county-year-panel/synthetic-only@sha256:"
                + "04" * 32,
            ],
            "rights_state": "REFERENCED_NOT_EVALUATED",
            "sensitivity_state": "REFERENCED_NOT_EVALUATED",
        },
        "disclosure": {
            "interpretation_limits": [
                "AGGREGATE_ONLY",
                "NO_CROSSWALK_INFERENCE",
                "NO_FRONTIER_CLASSIFICATION",
                "NO_PUBLICATION_AUTHORITY",
                "OBSERVATIONS_REFERENCED_NOT_RESOLVED",
                "SOURCE_ROLES_PRESERVED",
            ]
        },
        "governance": {
            "execution_mode": "FIXTURE_ONLY",
            "network_attempted": False,
            "observations_loaded": False,
            "values_computed": False,
            "geography_resolved": False,
            "crosswalk_executed": False,
            "evidence_resolved": False,
            "policy_evaluated": False,
            "frontier_classified": False,
            "review_approved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "public_use_allowed": False,
            "publication_authorized": False,
        },
        "spec_hash": "sha256:" + "0" * 64,
    }
    return _seal_county_year_panel(value)


def _bundle_identity(bundle: Mapping[str, Any]) -> str:
    projection = copy.deepcopy(dict(bundle))
    projection.pop("spec_hash", None)
    return compute_spec_hash(projection)


def _build_registry(
    scenario: Mapping[str, Any], observations: Mapping[str, dict[str, Any]]
) -> dict[str, Any]:
    registry: dict[str, Any] = {
        "crosswalks": {},
        "threshold_policies": {},
        "uncertainties": {},
        "evidence_refs": {},
        "evidence_bundles": {},
        "observations": dict(observations),
    }
    panel_geo = _mapping(scenario.get("subject"))["geography_version_ref"]
    for raw in _list(scenario.get("criteria")):
        criterion = _mapping(raw)
        observation_cfg = _mapping(criterion.get("observation"))
        observation_ref = next(
            (
                ref
                for ref, wrapper in observations.items()
                if wrapper["kind"] == criterion["observation_kind"]
            ),
            None,
        )
        crosswalk_ref = observation_cfg.get("geography_crosswalk_ref")
        if crosswalk_ref and observation_cfg.get("crosswalk_state") != "MISSING":
            registry["crosswalks"][crosswalk_ref] = {
                "source_geography_version_ref": observation_cfg["geography_version_ref"],
                "target_geography_version_ref": panel_geo,
                "calendar_year": _mapping(scenario.get("subject"))["calendar_year"],
                "admitted_for_fixture": observation_cfg.get("crosswalk_state") == "ADMITTED",
            }
            if observation_cfg.get("crosswalk_state") == "MISMATCHED":
                registry["crosswalks"][crosswalk_ref]["target_geography_version_ref"] = (
                    "kfm://geography-version/synthetic-other@sha256:" + "f" * 64
                )

        uncertainty = _mapping(criterion.get("uncertainty"))
        if uncertainty.get("state") != "MISSING":
            registry["uncertainties"][uncertainty["ref"]] = {
                "state": uncertainty.get("state"),
                "indicator_definition_ref": criterion["indicator_definition_ref"],
                "observation_ref": observation_ref,
                "lower": uncertainty.get("lower"),
                "upper": uncertainty.get("upper"),
                "maximum_width": uncertainty.get("maximum_width"),
            }

        policy = _mapping(criterion.get("threshold_policy"))
        if policy.get("state") != "MISSING":
            registry["threshold_policies"][policy["ref"]] = {
                "indicator_definition_ref": policy.get("indicator_definition_ref"),
                "comparison_operator": policy.get("comparison_operator"),
                "value": policy.get("value"),
                "valid_from": policy.get("valid_from"),
                "valid_to": policy.get("valid_to"),
                "admitted_for_fixture": policy.get("state") == "ADMITTED",
            }

        evidence = _mapping(criterion.get("evidence"))
        if evidence.get("state") != "MISSING":
            bundle_id = evidence["bundle_id"]
            evidence_ref = {
                "ref": evidence["ref"],
                "kind": "measurement",
                "bundle_ref": bundle_id,
            }
            registry["evidence_refs"][evidence["ref"]] = evidence_ref
            if evidence.get("state") != "UNRESOLVED":
                bundle = {
                    "bundle_id": bundle_id,
                    "claim_scope": f"Synthetic {criterion['criterion_key']} observation support",
                    "evidence_refs": [copy.deepcopy(evidence_ref)],
                    "source_records": [
                        f"synthetic-source-record:{criterion['criterion_key']}"
                    ],
                    "citations": [
                        f"Synthetic fixture citation for {criterion['criterion_key']}"
                    ],
                    "rights": {"license": "CC0-1.0"},
                    "sensitivity": {
                        "level": "public",
                        "reason": "synthetic fixture",
                        "applied_at": "2026-08-16T00:00:00Z",
                    },
                    "transforms": ["synthetic_fixture_projection"],
                    "checksums": {
                        "observation": (
                            _mapping(observations.get(observation_ref, {}))
                            .get("document", {})
                            .get("spec_hash", "sha256:" + "0" * 64)
                        )
                    },
                }
                bundle["spec_hash"] = {"value": _bundle_identity(bundle)}
                if evidence.get("bundle_state") == "IDENTITY_MISMATCH":
                    bundle["spec_hash"]["value"] = "sha256:" + "f" * 64
                if evidence.get("bundle_state") == "MEMBER_MISMATCH":
                    bundle["evidence_refs"] = [
                        {
                            "ref": (
                                "kfm://evidence-ref/mismatch/synthetic@sha256:"
                                + "e" * 64
                            ),
                            "kind": "measurement",
                            "bundle_ref": bundle_id,
                        }
                    ]
                registry["evidence_bundles"][bundle_id] = bundle
    return registry
