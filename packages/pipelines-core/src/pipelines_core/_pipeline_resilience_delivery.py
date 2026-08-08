"""Durable delivery, dead-letter replay, and kill-switch decisions."""

from __future__ import annotations

from typing import Any, Mapping

from ._pipeline_resilience_common import (
    PipelineResiliencePlanError,
    _CONTRACT_VERSION,
    _DURABILITY_MODES,
    _EVENT_ID,
    _IN_FLIGHT_POLICIES,
    _KILL_SWITCH_MODES,
    _REPLAY_ELIGIBILITY,
    _SAFE_CODE,
    _require_bool,
    _require_enum,
    _require_identifier,
    _require_int,
    _require_mapping,
    _require_ref,
)

def _delivery_decision(delivery: Mapping[str, Any]) -> dict[str, Any]:
    emits_event = _require_bool(delivery["emits_event"], "/delivery/emits_event")
    durability_mode = _require_enum(
        delivery["durability_mode"],
        "/delivery/durability_mode",
        _DURABILITY_MODES,
        "DURABILITY_MODE_INVALID",
    )
    atomic_verified = _require_bool(
        delivery["atomic_commit_verified"],
        "/delivery/atomic_commit_verified",
    )
    consumer_idempotency = _require_bool(
        delivery["consumer_idempotency_verified"],
        "/delivery/consumer_idempotency_verified",
    )
    dead_letter = delivery["dead_letter"]

    if not emits_event:
        if (
            durability_mode != "NONE"
            or atomic_verified
            or consumer_idempotency
            or dead_letter is not None
        ):
            raise PipelineResiliencePlanError(
                "DELIVERY_NONE_SHAPE_INVALID", "/delivery"
            )
        return {
            "decision": "NOT_APPLICABLE",
            "durability_mode": durability_mode,
            "reason_codes": ["NO_EVENT_DELIVERY"],
        }

    reasons: list[str] = []
    if durability_mode == "NONE":
        reasons.append("DURABLE_EVENT_DELIVERY_REQUIRED")
    if not atomic_verified:
        reasons.append("ATOMIC_COMMIT_NOT_VERIFIED")
    if not consumer_idempotency:
        reasons.append("CONSUMER_IDEMPOTENCY_NOT_VERIFIED")
    if reasons:
        return {
            "decision": "QUARANTINE",
            "durability_mode": durability_mode,
            "reason_codes": sorted(reasons),
        }

    if dead_letter is None:
        return {
            "decision": "ALLOW",
            "durability_mode": durability_mode,
            "reason_codes": ["DURABLE_IDEMPOTENT_DELIVERY_VERIFIED"],
        }

    dead_letter = _require_mapping(
        dead_letter,
        "/delivery/dead_letter",
        {
            "event_id",
            "reason_code",
            "attempt_count",
            "contract_version",
            "replay_requested",
            "replay_eligibility",
            "authorization_ref",
            "admission_rechecked",
            "policy_rechecked",
            "target_contract_version",
        },
    )
    event_id = _require_identifier(
        dead_letter["event_id"],
        "/delivery/dead_letter/event_id",
        _EVENT_ID,
        "DEAD_LETTER_EVENT_ID_INVALID",
    )
    reason_code = _require_identifier(
        dead_letter["reason_code"],
        "/delivery/dead_letter/reason_code",
        _SAFE_CODE,
        "DEAD_LETTER_REASON_CODE_INVALID",
    )
    attempt_count = _require_int(
        dead_letter["attempt_count"],
        "/delivery/dead_letter/attempt_count",
        minimum=1,
    )
    original_contract = _require_identifier(
        dead_letter["contract_version"],
        "/delivery/dead_letter/contract_version",
        _CONTRACT_VERSION,
        "CONTRACT_VERSION_INVALID",
    )
    target_contract = _require_identifier(
        dead_letter["target_contract_version"],
        "/delivery/dead_letter/target_contract_version",
        _CONTRACT_VERSION,
        "CONTRACT_VERSION_INVALID",
    )
    replay_requested = _require_bool(
        dead_letter["replay_requested"],
        "/delivery/dead_letter/replay_requested",
    )
    eligibility = _require_enum(
        dead_letter["replay_eligibility"],
        "/delivery/dead_letter/replay_eligibility",
        _REPLAY_ELIGIBILITY,
        "REPLAY_ELIGIBILITY_INVALID",
    )
    authorization_ref = _require_ref(
        dead_letter["authorization_ref"],
        "/delivery/dead_letter/authorization_ref",
    )
    admission_rechecked = _require_bool(
        dead_letter["admission_rechecked"],
        "/delivery/dead_letter/admission_rechecked",
    )
    policy_rechecked = _require_bool(
        dead_letter["policy_rechecked"],
        "/delivery/dead_letter/policy_rechecked",
    )

    detail = {
        "event_id": event_id,
        "reason_code": reason_code,
        "attempt_count": attempt_count,
        "contract_version": original_contract,
        "target_contract_version": target_contract,
    }

    if not replay_requested:
        return {
            "decision": "HOLD",
            "durability_mode": durability_mode,
            "dead_letter": detail,
            "reason_codes": ["DEAD_LETTER_RETAINED"],
        }
    if eligibility == "INELIGIBLE":
        return {
            "decision": "DENY",
            "durability_mode": durability_mode,
            "dead_letter": detail,
            "reason_codes": ["DEAD_LETTER_REPLAY_INELIGIBLE"],
        }
    if eligibility == "REVIEW_REQUIRED":
        return {
            "decision": "HOLD",
            "durability_mode": durability_mode,
            "dead_letter": detail,
            "reason_codes": ["DEAD_LETTER_REPLAY_REVIEW_REQUIRED"],
        }

    replay_reasons: list[str] = []
    if authorization_ref is None:
        replay_reasons.append("DEAD_LETTER_REPLAY_AUTHORIZATION_REQUIRED")
    if not admission_rechecked:
        replay_reasons.append("DEAD_LETTER_ADMISSION_RECHECK_REQUIRED")
    if not policy_rechecked:
        replay_reasons.append("DEAD_LETTER_POLICY_RECHECK_REQUIRED")
    if replay_reasons:
        return {
            "decision": "HOLD",
            "durability_mode": durability_mode,
            "dead_letter": detail,
            "reason_codes": sorted(replay_reasons),
        }

    replay_reasons = ["DEAD_LETTER_REPLAY_ALLOWED"]
    if original_contract != target_contract:
        replay_reasons.append("DEAD_LETTER_CONTRACT_VERSION_CHANGED")
    return {
        "decision": "REPLAY",
        "durability_mode": durability_mode,
        "dead_letter": detail,
        "reason_codes": sorted(replay_reasons),
    }


def _kill_switch_decision(kill_switch: Mapping[str, Any]) -> dict[str, Any]:
    previous_mode = _require_enum(
        kill_switch["previous_mode"],
        "/kill_switch/previous_mode",
        _KILL_SWITCH_MODES,
        "KILL_SWITCH_MODE_INVALID",
    )
    mode = _require_enum(
        kill_switch["mode"],
        "/kill_switch/mode",
        _KILL_SWITCH_MODES,
        "KILL_SWITCH_MODE_INVALID",
    )
    activation_receipt_ref = _require_ref(
        kill_switch["activation_receipt_ref"],
        "/kill_switch/activation_receipt_ref",
    )
    reenable_review_ref = _require_ref(
        kill_switch["reenable_review_ref"],
        "/kill_switch/reenable_review_ref",
    )
    in_flight_policy = _require_enum(
        kill_switch["in_flight_policy"],
        "/kill_switch/in_flight_policy",
        _IN_FLIGHT_POLICIES,
        "IN_FLIGHT_POLICY_INVALID",
    )

    if mode != "RUNNING" and activation_receipt_ref is None:
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "DENY",
            "reason_codes": ["KILL_SWITCH_ACTIVATION_RECEIPT_REQUIRED"],
        }
    if mode == "PAUSE_NEW_STARTS" and in_flight_policy != "CONTINUE":
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "DENY",
            "reason_codes": ["PAUSE_NEW_STARTS_MUST_CONTINUE_IN_FLIGHT"],
        }
    if mode == "EMERGENCY_STOP" and in_flight_policy != "CANCEL":
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "DENY",
            "reason_codes": ["EMERGENCY_STOP_MUST_CANCEL_IN_FLIGHT"],
        }
    if (
        mode == "RUNNING"
        and previous_mode != "RUNNING"
        and reenable_review_ref is None
    ):
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "DENY",
            "reason_codes": ["KILL_SWITCH_REENABLE_REVIEW_REQUIRED"],
        }

    if mode == "RUNNING":
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "ALLOW",
            "reason_codes": ["KILL_SWITCH_RUNNING"],
        }
    if mode == "PAUSE_NEW_STARTS":
        return {
            "previous_mode": previous_mode,
            "mode": mode,
            "decision": "PAUSE_NEW_STARTS",
            "reason_codes": ["KILL_SWITCH_PAUSES_NEW_STARTS"],
        }
    return {
        "previous_mode": previous_mode,
        "mode": mode,
        "decision": "STOP_ALL",
        "reason_codes": ["KILL_SWITCH_EMERGENCY_STOP"],
    }


