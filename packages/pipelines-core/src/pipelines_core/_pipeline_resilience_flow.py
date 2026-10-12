"""Backpressure and circuit-breaker decisions for the resilience planner."""

from __future__ import annotations

from typing import Any, Mapping

from ._pipeline_resilience_common import (
    PipelineResiliencePlanError,
    _BREAKER_STATES,
    _PARTITIONS,
    _require_bool,
    _require_enum,
    _require_int,
    _require_number,
)

def _backpressure_decision(
    queue: Mapping[str, Any], policy: Mapping[str, Any]
) -> dict[str, Any]:
    partition = _require_enum(
        queue["partition"],
        "/queue/partition",
        _PARTITIONS,
        "QUEUE_PARTITION_INVALID",
    )
    depth = _require_int(queue["depth"], "/queue/depth")
    oldest_age = _require_number(
        queue["oldest_age_seconds"], "/queue/oldest_age_seconds"
    )
    in_flight = _require_int(queue["in_flight"], "/queue/in_flight")
    isolated_outputs = _require_bool(
        queue["isolated_outputs"], "/queue/isolated_outputs"
    )
    public_side_effects = _require_bool(
        queue["public_side_effects"], "/queue/public_side_effects"
    )
    contracts_match = _require_bool(
        queue["contracts_match_production"],
        "/queue/contracts_match_production",
    )
    schemas_match = _require_bool(
        queue["schemas_match_production"],
        "/queue/schemas_match_production",
    )
    policies_match = _require_bool(
        queue["policies_match_production"],
        "/queue/policies_match_production",
    )

    max_depth = _require_int(
        policy["max_queue_depth"],
        "/policy/backpressure/max_queue_depth",
        minimum=1,
    )
    max_age = _require_number(
        policy["max_oldest_age_seconds"],
        "/policy/backpressure/max_oldest_age_seconds",
        strictly_positive=True,
    )
    max_in_flight = _require_int(
        policy["max_in_flight"],
        "/policy/backpressure/max_in_flight",
        minimum=1,
    )
    shed_allowed = _require_bool(
        policy["shed_allowed"], "/policy/backpressure/shed_allowed"
    )

    reasons: list[str] = []
    if partition == "CANARY":
        if not isolated_outputs:
            reasons.append("CANARY_OUTPUT_ISOLATION_REQUIRED")
        if public_side_effects:
            reasons.append("CANARY_PUBLIC_SIDE_EFFECTS_DENIED")
        if not contracts_match:
            reasons.append("CANARY_CONTRACT_PARITY_REQUIRED")
        if not schemas_match:
            reasons.append("CANARY_SCHEMA_PARITY_REQUIRED")
        if not policies_match:
            reasons.append("CANARY_POLICY_PARITY_REQUIRED")
        if reasons:
            return {
                "partition": partition,
                "decision": "DENY",
                "reason_codes": sorted(reasons),
            }

    if depth > max_depth or oldest_age > max_age:
        reasons = []
        if depth > max_depth:
            reasons.append("QUEUE_DEPTH_LIMIT_EXCEEDED")
        if oldest_age > max_age:
            reasons.append("QUEUE_AGE_LIMIT_EXCEEDED")
        return {
            "partition": partition,
            "decision": "SHED" if shed_allowed else "HOLD",
            "reason_codes": sorted(
                reasons + (["LOAD_SHEDDING_ALLOWED"] if shed_allowed else ["LOAD_SHEDDING_DENIED"])
            ),
        }

    if in_flight >= max_in_flight:
        return {
            "partition": partition,
            "decision": "THROTTLE",
            "reason_codes": ["IN_FLIGHT_LIMIT_REACHED"],
        }

    return {
        "partition": partition,
        "decision": "ACCEPT",
        "reason_codes": ["QUEUE_WITHIN_BOUNDS"],
    }


def _breaker_decision(
    breaker: Mapping[str, Any], policy: Mapping[str, Any]
) -> dict[str, Any]:
    state = _require_enum(
        breaker["state"],
        "/breaker/state",
        _BREAKER_STATES,
        "BREAKER_STATE_INVALID",
    )
    failures = _require_int(
        breaker["consecutive_failures"], "/breaker/consecutive_failures"
    )
    cooldown_elapsed = _require_bool(
        breaker["cooldown_elapsed"], "/breaker/cooldown_elapsed"
    )
    probe_raw = breaker["probe_succeeded"]
    if probe_raw is not None and not isinstance(probe_raw, bool):
        raise PipelineResiliencePlanError(
            "BREAKER_PROBE_RESULT_INVALID", "/breaker/probe_succeeded"
        )
    threshold = _require_int(
        policy["failure_threshold"],
        "/policy/breaker/failure_threshold",
        minimum=1,
    )

    if state == "CLOSED":
        if failures >= threshold:
            return {
                "current_state": state,
                "next_state": "OPEN",
                "decision": "DENY",
                "reason_codes": ["BREAKER_FAILURE_THRESHOLD_REACHED"],
            }
        return {
            "current_state": state,
            "next_state": "CLOSED",
            "decision": "ALLOW",
            "reason_codes": ["BREAKER_CLOSED"],
        }

    if state == "OPEN":
        if cooldown_elapsed:
            return {
                "current_state": state,
                "next_state": "HALF_OPEN",
                "decision": "PROBE",
                "reason_codes": ["BREAKER_COOLDOWN_ELAPSED"],
            }
        return {
            "current_state": state,
            "next_state": "OPEN",
            "decision": "DENY",
            "reason_codes": ["BREAKER_OPEN"],
        }

    # HALF_OPEN
    if probe_raw is None:
        return {
            "current_state": state,
            "next_state": "HALF_OPEN",
            "decision": "PROBE",
            "reason_codes": ["BREAKER_PROBE_REQUIRED"],
        }
    if probe_raw:
        return {
            "current_state": state,
            "next_state": "CLOSED",
            "decision": "ALLOW",
            "reason_codes": ["BREAKER_PROBE_SUCCEEDED"],
        }
    return {
        "current_state": state,
        "next_state": "OPEN",
        "decision": "DENY",
        "reason_codes": ["BREAKER_PROBE_FAILED"],
    }


