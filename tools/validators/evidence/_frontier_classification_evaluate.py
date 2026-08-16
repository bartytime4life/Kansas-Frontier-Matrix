#!/usr/bin/env python3
"""Deterministic FrontierClassification fixture evaluation helpers."""
from __future__ import annotations

import copy
from collections.abc import Mapping, Sequence
from typing import Any

from tools.validators.evidence._frontier_classification_common import (
    FixtureContext,
    IDENTITY_PREFIX,
    METHOD_REF,
    _day,
    _digest_ref,
    _list,
    _mapping,
    seal,
)
from tools.validators.evidence._frontier_classification_inputs import (
    _build_access_observation,
    _build_frontier_definition,
    _build_population_observation,
)
from tools.validators.evidence._frontier_classification_registry import (
    _build_county_year_panel,
    _build_registry,
    _bundle_identity,
)

def _observation_state(
    slot: Mapping[str, Any], wrapper: Mapping[str, Any] | None
) -> str:
    availability = slot.get("availability")
    if availability == "MISSING":
        return "MISSING"
    if availability == "SUPPRESSED":
        return "SUPPRESSED"
    lifecycle = _mapping(wrapper).get("lifecycle_state")
    return lifecycle if lifecycle in {
        "CURRENT",
        "STALE",
        "SUPERSEDED",
        "WITHDRAWN",
        "CORRECTED_PENDING",
    } else "MISSING"


def _compare_interval(operator: str, low: float, high: float, threshold: float) -> str:
    if operator == "GREATER_THAN_OR_EQUAL":
        if low >= threshold:
            return "SATISFIED"
        if high < threshold:
            return "UNSATISFIED"
    elif operator == "GREATER_THAN":
        if low > threshold:
            return "SATISFIED"
        if high <= threshold:
            return "UNSATISFIED"
    elif operator == "LESS_THAN_OR_EQUAL":
        if high <= threshold:
            return "SATISFIED"
        if low > threshold:
            return "UNSATISFIED"
    elif operator == "LESS_THAN":
        if high < threshold:
            return "SATISFIED"
        if low >= threshold:
            return "UNSATISFIED"
    return "INDETERMINATE"


def _derive_trace(
    definition_criterion: Mapping[str, Any],
    slot: Mapping[str, Any],
    scenario_criterion: Mapping[str, Any],
    scenario: Mapping[str, Any],
    definition: Mapping[str, Any],
    panel: Mapping[str, Any],
    registry: Mapping[str, Any],
) -> dict[str, Any]:
    reasons: set[str] = set()
    observation_ref = slot.get("observation_ref")
    wrapper = _mapping(_mapping(registry.get("observations")).get(observation_ref))
    document = _mapping(wrapper.get("document"))
    observation_state = _observation_state(slot, wrapper)
    if observation_state == "MISSING":
        reasons.add("OBSERVATION_MISSING")
    elif observation_state == "SUPPRESSED":
        reasons.add("OBSERVATION_SUPPRESSED")
    elif observation_state == "STALE":
        reasons.add("OBSERVATION_STALE")
    elif observation_state == "SUPERSEDED":
        reasons.add("OBSERVATION_SUPERSEDED")
    elif observation_state == "WITHDRAWN":
        reasons.add("OBSERVATION_WITHDRAWN")
    elif observation_state == "CORRECTED_PENDING":
        reasons.add("CORRECTION_LINEAGE_UNRESOLVED")

    source_role_ref = slot.get("source_role_ref")
    source_role = _mapping(document.get("source")).get("source_role") if document else None
    expected_role = scenario_criterion.get("expected_source_role")
    if observation_state == "CURRENT" and (
        source_role_ref != scenario_criterion.get("source_role_ref")
        or source_role != expected_role
        or scenario_criterion.get("source_role_mirror_state") != "MATCH"
    ):
        reasons.add("SOURCE_ROLE_MISMATCH")

    geo_alignment = slot.get("geography_alignment", "UNRESOLVED")
    crosswalk_ref = slot.get("geography_crosswalk_ref")
    panel_geo = _mapping(panel.get("panel_scope")).get("geography_version_ref")
    observation_geo = slot.get("observation_geography_version_ref")
    if geo_alignment == "SAME_VERSION":
        if observation_geo != panel_geo:
            reasons.add("GEOGRAPHY_VERSION_MISMATCH")
    elif geo_alignment == "CROSSWALK_REFERENCED":
        crosswalk = _mapping(_mapping(registry.get("crosswalks")).get(crosswalk_ref))
        if not crosswalk:
            reasons.add("GEOGRAPHY_CROSSWALK_MISSING")
        elif (
            crosswalk.get("source_geography_version_ref") != observation_geo
            or crosswalk.get("target_geography_version_ref") != panel_geo
            or crosswalk.get("calendar_year")
            != _mapping(panel.get("panel_scope")).get("calendar_year")
        ):
            reasons.add("GEOGRAPHY_CROSSWALK_MISMATCH")
        elif crosswalk.get("admitted_for_fixture") is not True:
            reasons.add("GEOGRAPHY_CROSSWALK_NOT_ADMITTED")
    else:
        reasons.add("GEOGRAPHY_ALIGNMENT_UNRESOLVED")

    panel_year = _mapping(panel.get("panel_scope")).get("calendar_year")
    observation_year = _mapping(document.get("temporal")).get("reference_year") if document else None
    valid_from = _day(_mapping(definition.get("temporal")).get("valid_from"))
    valid_to = _day(_mapping(definition.get("temporal")).get("valid_to"))
    time_alignment = "ALIGNED"
    if observation_state in {"MISSING", "SUPPRESSED"}:
        time_alignment = "UNRESOLVED"
    elif observation_year != panel_year:
        time_alignment = "OUTSIDE_PANEL_YEAR"
        reasons.add("OBSERVATION_YEAR_MISMATCH")
    elif valid_from is None or valid_to is None or not (
        valid_from.year <= int(panel_year) <= valid_to.year
    ):
        time_alignment = "OUTSIDE_DEFINITION_INTERVAL"
        reasons.add("DEFINITION_TIME_SUPPORT_MISMATCH")

    evidence_ref_value = next(iter(_list(slot.get("evidence_refs"))), None)
    evidence_posture = "VERIFIED"
    evidence_ref_obj = _mapping(
        _mapping(registry.get("evidence_refs")).get(evidence_ref_value)
    )
    bundle_id = evidence_ref_obj.get("bundle_ref") if evidence_ref_obj else None
    bundle = _mapping(_mapping(registry.get("evidence_bundles")).get(bundle_id))
    bundle_hash = _mapping(bundle.get("spec_hash")).get("value") if bundle else None
    if evidence_ref_value is None or not evidence_ref_obj:
        evidence_posture = "MISSING"
        reasons.add("EVIDENCE_REF_MISSING")
    elif not bundle:
        evidence_posture = "UNRESOLVED"
        reasons.add("EVIDENCE_BUNDLE_UNRESOLVED")
    else:
        exact_member = evidence_ref_obj in _list(bundle.get("evidence_refs"))
        if bundle_hash != _bundle_identity(bundle) or not exact_member:
            evidence_posture = "MISMATCHED"
            reasons.add("EVIDENCE_BUNDLE_MISMATCH")

    uncertainty_ref = slot.get("uncertainty_ref")
    uncertainty = _mapping(
        _mapping(registry.get("uncertainties")).get(uncertainty_ref)
    )
    uncertainty_posture = "ADMITTED"
    if uncertainty_ref is None or not uncertainty:
        uncertainty_posture = "MISSING"
        reasons.add("UNCERTAINTY_SUPPORT_MISSING")
    elif uncertainty.get("state") != "ADMITTED":
        uncertainty_posture = "UNRESOLVED"
        reasons.add("UNCERTAINTY_SUPPORT_UNRESOLVED")
    elif (
        uncertainty.get("indicator_definition_ref")
        != definition_criterion.get("indicator_definition_ref")
        or uncertainty.get("observation_ref") != observation_ref
    ):
        uncertainty_posture = "UNRESOLVED"
        reasons.add("UNCERTAINTY_BINDING_MISMATCH")
    else:
        low = uncertainty.get("lower")
        high = uncertainty.get("upper")
        maximum_width = uncertainty.get("maximum_width")
        if not all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in (low, high, maximum_width)) or low > high:
            uncertainty_posture = "UNRESOLVED"
            reasons.add("UNCERTAINTY_INTERVAL_INVALID")
        elif high - low > maximum_width:
            uncertainty_posture = "EXCEEDS_ADMITTED"
            reasons.add("UNCERTAINTY_EXCEEDS_ADMITTED_POSTURE")

    threshold_ref = definition_criterion.get("threshold_policy_ref")
    policy = _mapping(
        _mapping(registry.get("threshold_policies")).get(threshold_ref)
    )
    threshold_posture = "ADMITTED"
    if not threshold_ref or not policy:
        threshold_posture = "MISSING"
        reasons.add("THRESHOLD_POLICY_MISSING")
    elif (
        policy.get("indicator_definition_ref")
        != definition_criterion.get("indicator_definition_ref")
        or policy.get("comparison_operator")
        != definition_criterion.get("comparison_operator")
    ):
        threshold_posture = "MISMATCHED"
        reasons.add("THRESHOLD_POLICY_MISMATCH")
    elif policy.get("admitted_for_fixture") is not True:
        threshold_posture = "NOT_ADMITTED"
        reasons.add("THRESHOLD_POLICY_NOT_ADMITTED")
    else:
        policy_from = _day(policy.get("valid_from"))
        policy_to = _day(policy.get("valid_to"))
        if policy_from is None or policy_to is None or not (
            policy_from.year <= int(panel_year) <= policy_to.year
        ):
            threshold_posture = "MISMATCHED"
            reasons.add("THRESHOLD_POLICY_TIME_MISMATCH")

    comparison_state = "INDETERMINATE"
    if not reasons:
        low = float(uncertainty["lower"])
        high = float(uncertainty["upper"])
        threshold = float(policy["value"])
        comparison_state = _compare_interval(
            str(definition_criterion["comparison_operator"]), low, high, threshold
        )
        if comparison_state == "INDETERMINATE":
            uncertainty_posture = "CROSSES_THRESHOLD"
            reasons.add("UNCERTAINTY_CROSSES_THRESHOLD")
        elif comparison_state == "SATISFIED":
            reasons.add("CRITERION_SATISFIED")
        else:
            reasons.add("CRITERION_NOT_SATISFIED")

    return {
        "criterion_key": definition_criterion["criterion_key"],
        "indicator_definition_ref": definition_criterion["indicator_definition_ref"],
        "observation_kind": slot["observation_kind"],
        "panel_observation_ref": observation_ref,
        "source_role_ref": source_role_ref,
        "source_role": source_role,
        "observation_identity": document.get("observation_id") if document else None,
        "observation_spec_hash": document.get("spec_hash") if document else None,
        "observation_state": observation_state,
        "uncertainty_ref": uncertainty_ref,
        "uncertainty_posture": uncertainty_posture,
        "evidence_ref": evidence_ref_value,
        "evidence_bundle_id": bundle_id,
        "evidence_bundle_spec_hash": bundle_hash,
        "evidence_posture": evidence_posture,
        "geography_alignment": geo_alignment,
        "geography_crosswalk_ref": crosswalk_ref,
        "time_alignment": time_alignment,
        "threshold_policy_ref": threshold_ref,
        "threshold_policy_posture": threshold_posture,
        "comparison_operator": definition_criterion["comparison_operator"],
        "comparison_state": comparison_state,
        "reason_codes": sorted(reasons),
    }


def _derive_classification(
    combination_rule: str, traces: Sequence[Mapping[str, Any]]
) -> tuple[dict[str, Any], dict[str, Any]]:
    states = [trace.get("comparison_state") for trace in traces]
    if combination_rule == "ALL_CRITERIA":
        if "INDETERMINATE" in states:
            value = "UNCLASSIFIED"
            reason = "CRITERION_SUPPORT_INDETERMINATE"
        elif all(state == "SATISFIED" for state in states):
            value = "FRONTIER"
            reason = "ALL_CRITERIA_SATISFIED"
        else:
            value = "NOT_FRONTIER"
            reason = "ALL_CRITERIA_RULE_NOT_SATISFIED"
    else:
        if "SATISFIED" in states:
            value = "FRONTIER"
            reason = "ANY_CRITERION_SATISFIED"
        elif "INDETERMINATE" in states:
            value = "UNCLASSIFIED"
            reason = "CRITERION_SUPPORT_INDETERMINATE"
        else:
            value = "NOT_FRONTIER"
            reason = "NO_CRITERION_SATISFIED"
    classification = {
        "value": value,
        "combination_rule": combination_rule,
        "reason_codes": [reason],
    }
    if value == "UNCLASSIFIED":
        posture = {
            "execution": "ABSTAIN",
            "review": "HOLD",
            "obligations": sorted(
                [
                    "NO_PUBLICATION",
                    "PRESERVE_INPUT_LINEAGE",
                    "RESOLVE_INDETERMINATE_SUPPORT",
                ]
            ),
        }
    else:
        posture = {
            "execution": "CALCULATED",
            "review": "REVIEW_CANDIDATE",
            "obligations": sorted(
                [
                    "DISPLAY_CRITERION_TRACE",
                    "HUMAN_REVIEW_REQUIRED",
                    "NO_PUBLICATION",
                ]
            ),
        }
    return classification, posture


def _build_candidate(
    scenario: Mapping[str, Any],
    definition: Mapping[str, Any],
    panel: Mapping[str, Any],
    traces: Sequence[Mapping[str, Any]],
    classification: Mapping[str, Any],
    posture: Mapping[str, Any],
    lineage: Mapping[str, Any],
) -> dict[str, Any]:
    subject = _mapping(scenario.get("subject"))
    definition_ref = _mapping(panel.get("panel_scope"))["frontier_definition_ref"]
    panel_ref = _digest_ref(
        "county-year-panel/synthetic-2020", panel["spec_hash"]
    )
    value = {
        "object_type": "FrontierClassification",
        "schema_version": "1.0.0",
        "profile": "kfm.frontier-classification.fixture.v1",
        "assessment_id": IDENTITY_PREFIX + "0" * 64,
        "method": {
            "method_ref": METHOD_REF,
            "method_profile": "kfm.frontier-classification.synthetic.v1",
            "method_version": "1.0.0",
            "combination_rule": _mapping(definition.get("classification"))["combination_rule"],
        },
        "subject": {
            "county_identifier_digest": subject["county_identifier_digest"],
            "calendar_year": subject["calendar_year"],
            "geography_version_ref": subject["geography_version_ref"],
            "synthetic_subject": subject.get("synthetic_subject"),
        },
        "inputs": {
            "county_year_panel_ref": panel_ref,
            "county_year_panel_id": panel["panel_id"],
            "county_year_panel_spec_hash": panel["spec_hash"],
            "frontier_definition_ref": definition_ref,
            "frontier_definition_id": definition["definition_id"],
            "frontier_definition_spec_hash": definition["spec_hash"],
            "dependency_validation_state": "VALIDATED_LOCAL_FIXTURES",
        },
        "criteria": [copy.deepcopy(dict(item)) for item in traces],
        "classification": copy.deepcopy(dict(classification)),
        "posture": copy.deepcopy(dict(posture)),
        "lineage": copy.deepcopy(dict(lineage)),
        "metadata": {"generated_at": scenario["generated_at"]},
        "governance": {
            "fixture_only": True,
            "no_network": True,
            "synthetic_inputs_only": True,
            "real_county_classified": False,
            "source_data_accessed": False,
            "source_activation": False,
            "threshold_policy_changed": False,
            "lifecycle_write": False,
            "policy_authority": False,
            "review_authority": False,
            "release_authority": False,
            "publication_authority": False,
            "deployment_authority": False,
            "public_api_output": False,
            "map_output": False,
        },
        "spec_hash": "sha256:" + "0" * 64,
    }
    return seal(value)


def _assessment_ref(candidate: Mapping[str, Any]) -> str:
    digest = candidate["spec_hash"]
    return _digest_ref(
        "frontier-classification/assessment/" + digest.removeprefix("sha256:")[:24],
        digest,
    )


def materialize_scenario(scenario: Mapping[str, Any]) -> FixtureContext:
    definition = _build_frontier_definition(scenario)
    observations: dict[str, dict[str, Any]] = {}
    for raw in _list(scenario.get("criteria")):
        criterion = _mapping(raw)
        built = (
            _build_access_observation(criterion)
            if criterion.get("observation_kind") == "ACCESS"
            else _build_population_observation(criterion)
        )
        if built is not None:
            reference, document = built
            observations[reference] = {
                "kind": criterion["observation_kind"],
                "document": document,
                "source_role_ref": criterion["source_role_ref"],
                "lifecycle_state": _mapping(criterion.get("observation")).get(
                    "lifecycle_state"
                ),
                "accepted_current_lineage": _mapping(
                    criterion.get("observation")
                ).get("accepted_current_lineage"),
            }
    panel = _build_county_year_panel(scenario, definition, observations)
    registry = _build_registry(scenario, observations)
    scenario_by_key = {
        _mapping(item)["criterion_key"]: _mapping(item)
        for item in _list(scenario.get("criteria"))
    }
    slots_by_indicator = {
        _mapping(item)["indicator_definition_ref"]: _mapping(item)
        for item in _list(panel.get("observations"))
    }
    traces: list[dict[str, Any]] = []
    for raw in _list(_mapping(definition.get("classification")).get("criteria")):
        criterion = _mapping(raw)
        traces.append(
            _derive_trace(
                criterion,
                slots_by_indicator[criterion["indicator_definition_ref"]],
                scenario_by_key[criterion["criterion_key"]],
                scenario,
                definition,
                panel,
                registry,
            )
        )
    traces.sort(key=lambda item: item["criterion_key"])
    combination_rule = _mapping(definition.get("classification"))["combination_rule"]
    classification, posture = _derive_classification(combination_rule, traces)

    lineage = copy.deepcopy(dict(_mapping(scenario.get("lineage"))))
    prior: dict[str, Any] | None = None
    if lineage.get("state") == "CORRECTED":
        prior_lineage = {
            "state": "ORIGINAL",
            "supersedes_assessment_ref": None,
            "correction_record_ref": None,
            "corrected_input_refs": [],
        }
        prior = _build_candidate(
            scenario,
            definition,
            panel,
            traces,
            classification,
            posture,
            prior_lineage,
        )
        lineage["supersedes_assessment_ref"] = _assessment_ref(prior)
        lineage["corrected_input_refs"] = sorted(
            _list(lineage.get("corrected_input_refs"))
        )
    candidate = _build_candidate(
        scenario,
        definition,
        panel,
        traces,
        classification,
        posture,
        lineage,
    )
    return FixtureContext(
        candidate=candidate,
        registry=registry,
        definition=definition,
        panel=panel,
        observations=observations,
        expected_traces=traces,
        expected_classification=classification,
        expected_posture=posture,
        prior_assessment=prior,
    )
