"""Shared validation and identity helpers for pipeline resilience planning."""

from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any, Mapping

PLANNER_VERSION = "v1"

_PIPELINE_ID = re.compile(r"^[a-z][a-z0-9._-]{0,127}$")
_STEP_ID = re.compile(r"^[a-z][a-z0-9._-]{0,127}$")
_CONTRACT_VERSION = re.compile(r"^v[1-9][0-9]*$")
_SAFE_CODE = re.compile(r"^[A-Z][A-Z0-9_]{0,127}$")
_SAFE_GROUP = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$")
_EVENT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,255}$")
_KFM_REF = re.compile(r"^kfm://[A-Za-z0-9][A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]{0,2047}$")

_TRIGGER_TYPES = {
    "push", "pull_request", "schedule", "workflow_dispatch",
    "repository_dispatch", "release", "workflow_call",
    "pipeline_handoff", "external_webhook",
}
_ENVIRONMENTS = {"fixture", "development", "staging", "production"}
_SECRET_SCOPES = {"NONE", "READ_ONLY", "DOMAIN_SCOPED", "ENVIRONMENT_SCOPED"}
_ERROR_CLASSES = {
    "NONE", "TRANSIENT", "RATE_LIMITED", "DETERMINISTIC",
    "POLICY_DENIED", "QUARANTINE", "OPERATOR_REQUIRED",
}
_PARTITIONS = {"CANARY", "FULL"}
_BREAKER_STATES = {"CLOSED", "OPEN", "HALF_OPEN"}
_DURABILITY_MODES = {"NONE", "TRANSACTIONAL_OUTBOX", "WAL"}
_REPLAY_ELIGIBILITY = {"ELIGIBLE", "INELIGIBLE", "REVIEW_REQUIRED"}
_KILL_SWITCH_MODES = {"RUNNING", "PAUSE_NEW_STARTS", "EMERGENCY_STOP"}
_IN_FLIGHT_POLICIES = {"CONTINUE", "CANCEL"}
_MANUAL_OR_EXTERNAL_TRIGGERS = {
    "workflow_dispatch", "repository_dispatch", "external_webhook",
}
_DIRECT_CODE_TRIGGERS = {"push", "pull_request"}

class PipelineResiliencePlanError(ValueError):
    """Raised when a request cannot produce a bounded deterministic plan."""

    def __init__(self, code: str, field: str) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


def _canonical_json(value: Any, *, field: str = "/") -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, RecursionError) as exc:
        raise PipelineResiliencePlanError("VALUE_NOT_CANONICAL_JSON", field) from exc


def _hash(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _require_mapping(value: object, field: str, keys: set[str]) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise PipelineResiliencePlanError("OBJECT_REQUIRED", field)
    if set(value) != keys:
        raise PipelineResiliencePlanError("OBJECT_KEYS_INVALID", field)
    return value


def _require_identifier(value: object, field: str, pattern: re.Pattern[str], code: str) -> str:
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise PipelineResiliencePlanError(code, field)
    return value


def _require_enum(value: object, field: str, allowed: set[str], code: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise PipelineResiliencePlanError(code, field)
    return value


def _require_bool(value: object, field: str) -> bool:
    if not isinstance(value, bool):
        raise PipelineResiliencePlanError("BOOLEAN_REQUIRED", field)
    return value


def _require_int(value: object, field: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise PipelineResiliencePlanError("INTEGER_INVALID", field)
    return value


def _require_number(
    value: object,
    field: str,
    *,
    minimum: float = 0.0,
    maximum: float | None = None,
    strictly_positive: bool = False,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PipelineResiliencePlanError("NUMBER_INVALID", field)
    number = float(value)
    if not math.isfinite(number):
        raise PipelineResiliencePlanError("NUMBER_NOT_FINITE", field)
    if strictly_positive and number <= 0:
        raise PipelineResiliencePlanError("NUMBER_NOT_POSITIVE", field)
    if not strictly_positive and number < minimum:
        raise PipelineResiliencePlanError("NUMBER_BELOW_MINIMUM", field)
    if maximum is not None and number > maximum:
        raise PipelineResiliencePlanError("NUMBER_ABOVE_MAXIMUM", field)
    return number


def _require_ref(value: object, field: str, *, nullable: bool = True) -> str | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or _KFM_REF.fullmatch(value) is None:
        raise PipelineResiliencePlanError("KFM_REF_INVALID", field)
    return value


def _dedupe_codes(*groups: list[str]) -> list[str]:
    return sorted({code for group in groups for code in group})


