"""Trigger admission and retry decisions for the resilience planner."""

from __future__ import annotations

from typing import Any, Mapping

from ._pipeline_resilience_common import (
    PipelineResiliencePlanError,
    _DIRECT_CODE_TRIGGERS,
    _ENVIRONMENTS,
    _ERROR_CLASSES,
    _MANUAL_OR_EXTERNAL_TRIGGERS,
    _SAFE_GROUP,
    _SECRET_SCOPES,
    _TRIGGER_TYPES,
    _require_enum,
    _require_identifier,
    _require_int,
    _require_number,
    _require_ref,
)

def _trigger_decision(trigger: Mapping[str, Any]) -> dict[str, Any]:
    trigger_type = _require_enum(
        trigger["type"], "/trigger/type", _TRIGGER_TYPES, "TRIGGER_TYPE_INVALID"
    )
    environment = _require_enum(
        trigger["environment"],
        "/trigger/environment",
        _ENVIRONMENTS,
        "TRIGGER_ENVIRONMENT_INVALID",
    )
    authorization_ref = _require_ref(
        trigger["authorization_ref"], "/trigger/authorization_ref"
    )
    environment_gate_ref = _require_ref(
        trigger["environment_gate_ref"], "/trigger/environment_gate_ref"
    )
    concurrency_group = _require_identifier(
        trigger["concurrency_group"],
        "/trigger/concurrency_group",
        _SAFE_GROUP,
        "CONCURRENCY_GROUP_INVALID",
    )
    secret_scope = _require_enum(
        trigger["secret_scope"],
        "/trigger/secret_scope",
        _SECRET_SCOPES,
        "SECRET_SCOPE_INVALID",
    )

    reasons: list[str] = []
    decision = "ALLOW"

    if trigger_type in _MANUAL_OR_EXTERNAL_TRIGGERS and authorization_ref is None:
        decision = "DENY"
        reasons.append("TRIGGER_AUTHORIZATION_REQUIRED")

    if environment == "production" and environment_gate_ref is None:
        decision = "DENY"
        reasons.append("PRODUCTION_ENVIRONMENT_GATE_REQUIRED")

    if environment == "production" and trigger_type in _DIRECT_CODE_TRIGGERS:
        decision = "DENY"
        reasons.append("DIRECT_CODE_TRIGGER_TO_PRODUCTION_DENIED")

    if trigger_type == "external_webhook" and secret_scope == "ENVIRONMENT_SCOPED":
        decision = "DENY"
        reasons.append("EXTERNAL_TRIGGER_ENVIRONMENT_SECRET_SCOPE_DENIED")

    if not reasons:
        reasons.append("TRIGGER_MATRIX_ALLOW")

    return {
        "type": trigger_type,
        "environment": environment,
        "concurrency_group": concurrency_group,
        "secret_scope": secret_scope,
        "decision": decision,
        "reason_codes": sorted(reasons),
    }


def _retry_decision(
    retry_context: Mapping[str, Any], retry_policy: Mapping[str, Any]
) -> dict[str, Any]:
    error_class = _require_enum(
        retry_context["error_class"],
        "/retry_context/error_class",
        _ERROR_CLASSES,
        "ERROR_CLASS_INVALID",
    )
    attempt_number = _require_int(
        retry_context["attempt_number"], "/retry_context/attempt_number", minimum=1
    )
    elapsed_seconds = _require_number(
        retry_context["elapsed_seconds"], "/retry_context/elapsed_seconds"
    )
    retry_after_raw = retry_context["retry_after_seconds"]
    retry_after_seconds = (
        None
        if retry_after_raw is None
        else _require_number(
            retry_after_raw, "/retry_context/retry_after_seconds"
        )
    )
    jitter_unit = _require_number(
        retry_context["jitter_unit"],
        "/retry_context/jitter_unit",
        minimum=0.0,
        maximum=1.0,
    )

    max_attempts = _require_int(
        retry_policy["max_attempts"], "/policy/retry/max_attempts", minimum=1
    )
    base_delay = _require_number(
        retry_policy["base_delay_seconds"],
        "/policy/retry/base_delay_seconds",
    )
    multiplier = _require_number(
        retry_policy["multiplier"],
        "/policy/retry/multiplier",
        strictly_positive=True,
    )
    if multiplier < 1.0:
        raise PipelineResiliencePlanError(
            "RETRY_MULTIPLIER_BELOW_ONE", "/policy/retry/multiplier"
        )
    max_delay = _require_number(
        retry_policy["max_delay_seconds"],
        "/policy/retry/max_delay_seconds",
    )
    deadline = _require_number(
        retry_policy["deadline_seconds"],
        "/policy/retry/deadline_seconds",
        strictly_positive=True,
    )
    jitter_fraction = _require_number(
        retry_policy["jitter_fraction"],
        "/policy/retry/jitter_fraction",
        minimum=0.0,
        maximum=1.0,
    )
    retention = _require_int(
        retry_policy["idempotency_retention_seconds"],
        "/policy/retry/idempotency_retention_seconds",
        minimum=1,
    )

    if max_delay < base_delay:
        raise PipelineResiliencePlanError(
            "RETRY_MAX_DELAY_BELOW_BASE", "/policy/retry/max_delay_seconds"
        )

    if error_class == "NONE":
        return {
            "classification": error_class,
            "decision": "NO_ACTION",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["NO_FAILURE_TO_RETRY"],
        }

    if error_class == "DETERMINISTIC":
        return {
            "classification": error_class,
            "decision": "STOP",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["DETERMINISTIC_FAILURE_NOT_RETRIED"],
        }

    if error_class == "POLICY_DENIED":
        return {
            "classification": error_class,
            "decision": "STOP",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["POLICY_DENIAL_NOT_RETRIED"],
        }

    if error_class == "QUARANTINE":
        return {
            "classification": error_class,
            "decision": "QUARANTINE",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["QUARANTINE_REQUIRED"],
        }

    if error_class == "OPERATOR_REQUIRED":
        return {
            "classification": error_class,
            "decision": "OPERATOR_REQUIRED",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["OPERATOR_INTERVENTION_REQUIRED"],
        }

    # TRANSIENT and RATE_LIMITED are the only retriable classes.
    if attempt_number >= max_attempts:
        return {
            "classification": error_class,
            "decision": "STOP",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["RETRY_ATTEMPT_LIMIT_REACHED"],
        }
    if elapsed_seconds >= deadline:
        return {
            "classification": error_class,
            "decision": "STOP",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["RETRY_DEADLINE_REACHED"],
        }

    exponential = base_delay * (multiplier ** (attempt_number - 1))
    delay_base = min(exponential, max_delay)
    reasons = ["TRANSIENT_RETRY"]
    if error_class == "RATE_LIMITED":
        reasons = ["RATE_LIMIT_RETRY"]
        if retry_after_seconds is not None:
            delay_base = max(delay_base, min(retry_after_seconds, max_delay))
            reasons.append("RETRY_AFTER_HONORED")
        else:
            reasons.append("RETRY_AFTER_ABSENT")

    jitter_factor = 1.0 + jitter_fraction * ((2.0 * jitter_unit) - 1.0)
    delay = max(0.0, min(delay_base * jitter_factor, max_delay))
    remaining = deadline - elapsed_seconds
    if delay >= remaining:
        return {
            "classification": error_class,
            "decision": "STOP",
            "delay_seconds": 0.0,
            "next_attempt": None,
            "idempotency_retention_seconds": retention,
            "reason_codes": ["RETRY_DEADLINE_WOULD_BE_EXCEEDED"],
        }

    return {
        "classification": error_class,
        "decision": "RETRY",
        "delay_seconds": delay,
        "next_attempt": attempt_number + 1,
        "idempotency_retention_seconds": retention,
        "reason_codes": sorted(reasons),
    }


