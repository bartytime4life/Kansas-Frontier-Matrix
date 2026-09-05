"""Bounded, renderer-independent temporal state primitives for KFM.

This module is deliberately local and deterministic. It validates temporal
state shape/semantics, preserves raw temporal values, derives reproducible
identities, and provides a small generation-guarded frame reducer. It does not
resolve evidence, run policy, admit sources, approve releases, or publish.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
import hashlib
import json
import re
from typing import Any, Mapping

TEMPORAL_VIEW_STATE_PROFILE = "kfm.temporal.view-state.v1"
TEMPORAL_VIEW_STATE_SCHEMA_VERSION = "1.0.0"
TEMPORAL_QUERY_DISCLOSURE_PROFILE = "kfm.governance.temporal-query-disclosure.v1"
TEMPORAL_FRAME_CONTEXT_PROFILE = "kfm.temporal.frame-context.v1"

QUERY_CLASSES = frozenset(
    {"CURRENT_STATE", "PRIOR_STATE", "SEQUENCED", "NONSEQUENCED", "TRACKING_LOG"}
)
TIME_BASES = frozenset({"VALID_TIME", "TRANSACTION_TIME", "BITEMPORAL", "RELEASE_TIME"})
INTERVAL_SEMANTICS = frozenset({"CLOSED", "HALF_OPEN", "OPEN"})
POINT_EVENT_SEMANTICS = frozenset({"AT_INSTANT", "CONTAINS_INSTANT", "UNKNOWN"})
MASTER_TIME_RULES = frozenset({"DECLARED_MASTER", "INDEPENDENT_TRACKS"})
MODES = frozenset({"SNAPSHOT", "MOVING_WINDOW", "ACCUMULATION", "EVENT_STEP", "COMPARISON"})
STEP_RULES = frozenset({"NONE", "REGULAR", "CALENDAR", "AVAILABLE_EVENT"})
AGGREGATES = frozenset(
    {"NONE", "EVENT_COUNT", "UNIQUE_ENTITY_COUNT", "INTEGRATED_QUANTITY", "CURRENT_STATE"}
)
BOUNDARY_PROFILES = frozenset(
    {"instant", "date_only", "month", "year", "uncertain_range", "geologic_age"}
)
AWARE_INSTANT = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
    r"(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$"
)
NAIVE_INSTANT = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?$"
)
CALENDAR_PATTERNS = {
    "date_only": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "month": re.compile(r"^\d{4}-\d{2}$"),
    "year": re.compile(r"^\d{4}$"),
}
REF_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$")


@dataclass(frozen=True)
class TemporalNormalization:
    status: str
    code: str
    profile: str
    raw: str
    normalized: str | None


@dataclass(frozen=True)
class NormalizedQuery:
    status: str
    code: str
    query_id: str | None
    canonical: str
    start: TemporalNormalization | None = None
    end: TemporalNormalization | None = None


@dataclass(frozen=True)
class TemporalFrameLayer:
    layer_id: str
    actual_time: str | None
    availability: str
    evidence_refs: tuple[str, ...]
    source_version_ref: str | None
    release_status: str


@dataclass(frozen=True)
class TemporalFrameContext:
    state_id: str
    query_id: str
    selected_support: Mapping[str, Any]
    layers: tuple[TemporalFrameLayer, ...]
    dataset_version_refs: tuple[str, ...]
    release_refs: tuple[str, ...]
    policy_status: str
    outcome: str = "ANSWER"
    profile: str = TEMPORAL_FRAME_CONTEXT_PROFILE


@dataclass(frozen=True)
class TemporalRuntimeState:
    generation: int
    status: str
    requested_state: Mapping[str, Any] | None
    requested_query_id: str | None
    committed_frame: TemporalFrameContext | None
    error_code: str | None = None


def _canonicalize(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _canonicalize(value[key]) for key in sorted(value)}
    if isinstance(value, (list, tuple)):
        return [_canonicalize(item) for item in value]
    return value


def canonical_json(value: Any) -> str:
    """Serialize JSON-shaped data deterministically without changing arrays."""

    return json.dumps(
        _canonicalize(value),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def compute_state_id(state: Mapping[str, Any]) -> str:
    payload = {key: value for key, value in state.items() if key != "state_id"}
    digest = hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()
    return "kfm:temporal-view-state:sha256:" + digest


def compute_query_id(state: Mapping[str, Any]) -> str:
    fields = (
        "profile",
        "schema_version",
        "query",
        "selection",
        "display",
        "as_of",
        "pins",
        "comparison",
    )
    payload = {key: state[key] for key in fields if key in state}
    digest = hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()
    return "kfm:temporal-query:sha256:" + digest


def _utc_string(value: datetime) -> str:
    result = value.astimezone(timezone.utc).isoformat(timespec="microseconds")
    if "." in result:
        result = result.rstrip("0").rstrip(".")
    return result.replace("+00:00", "Z")


def _parse_aware(raw: str) -> tuple[datetime | None, bool]:
    if not AWARE_INSTANT.fullmatch(raw):
        return None, bool(NAIVE_INSTANT.fullmatch(raw))
    candidate = raw[:-1] + "+00:00" if raw.endswith("Z") else raw
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        return None, False
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None, True
    return parsed.astimezone(timezone.utc), False


def normalize_boundary(boundary: Mapping[str, Any]) -> TemporalNormalization:
    """Validate one typed boundary without fabricating precision."""

    profile = boundary.get("profile")
    raw = boundary.get("raw")
    normalized = boundary.get("normalized")
    if not isinstance(profile, str) or profile not in BOUNDARY_PROFILES:
        return TemporalNormalization("ERROR", "BOUNDARY_PROFILE_INVALID", str(profile), str(raw), None)
    if not isinstance(raw, str) or not raw:
        return TemporalNormalization("ERROR", "BOUNDARY_RAW_REQUIRED", profile, str(raw), None)
    if normalized is not None and not isinstance(normalized, str):
        return TemporalNormalization("ERROR", "NORMALIZED_TYPE_INVALID", profile, raw, None)

    if profile == "geologic_age":
        if normalized is not None:
            return TemporalNormalization(
                "ERROR", "NORMALIZED_PRECISION_VIOLATION", profile, raw, None
            )
        return TemporalNormalization("UNSUPPORTED", "UNSUPPORTED_PROFILE", profile, raw, None)

    if profile == "instant":
        parsed, timezone_missing = _parse_aware(raw)
        if timezone_missing:
            return TemporalNormalization("UNSUPPORTED", "UNKNOWN_TIMEZONE", profile, raw, None)
        if parsed is None:
            return TemporalNormalization("ERROR", "INSTANT_SYNTAX_INVALID", profile, raw, None)
        expected = _utc_string(parsed)
        if normalized is None:
            return TemporalNormalization("ERROR", "NORMALIZED_INSTANT_MISSING", profile, raw, None)
        parsed_normalized, normalized_timezone_missing = _parse_aware(normalized)
        if normalized_timezone_missing or parsed_normalized is None:
            return TemporalNormalization(
                "ERROR", "NORMALIZED_INSTANT_INVALID", profile, raw, None
            )
        if _utc_string(parsed_normalized) != expected:
            return TemporalNormalization(
                "ERROR", "NORMALIZATION_MISMATCH", profile, raw, expected
            )
        return TemporalNormalization("SUPPORTED", "OK", profile, raw, expected)

    if normalized is not None:
        return TemporalNormalization(
            "ERROR", "NORMALIZED_PRECISION_VIOLATION", profile, raw, None
        )
    pattern = CALENDAR_PATTERNS.get(profile)
    if pattern is not None and not pattern.fullmatch(raw):
        return TemporalNormalization("ERROR", "CALENDAR_SYNTAX_INVALID", profile, raw, None)
    return TemporalNormalization("SUPPORTED", "CALENDAR_PRESERVED", profile, raw, None)


def _calendar_key(profile: str, raw: str) -> tuple[int, ...] | None:
    pattern = CALENDAR_PATTERNS.get(profile)
    if pattern is None or not pattern.fullmatch(raw):
        return None
    try:
        parts = tuple(int(part) for part in raw.split("-"))
    except ValueError:
        return None
    if profile == "year":
        return (parts[0],)
    if profile == "month":
        return (parts[0], parts[1])
    return (parts[0], parts[1], parts[2])


def _selection_boundary(
    selection: Mapping[str, Any],
    field: str,
) -> Mapping[str, Any] | None:
    value = selection.get(field)
    return value if isinstance(value, Mapping) else None


def _error_query(state: Mapping[str, Any], code: str, canonical: str) -> NormalizedQuery:
    return NormalizedQuery("ERROR", code, None, canonical)


def normalize_temporal_query(state: Mapping[str, Any]) -> NormalizedQuery:
    """Return a finite supported/unsupported/error query outcome."""

    canonical = canonical_json(
        {
            key: state.get(key)
            for key in (
                "profile",
                "schema_version",
                "query",
                "selection",
                "display",
                "as_of",
                "pins",
                "comparison",
            )
            if key in state
        }
    )
    query_id = compute_query_id(state)

    query = state.get("query")
    selection = state.get("selection")
    display = state.get("display")
    as_of = state.get("as_of")
    pins = state.get("pins")
    comparison = state.get("comparison")
    if not all(
        isinstance(item, Mapping)
        for item in (query, selection, display, as_of, pins, comparison)
    ):
        return _error_query(state, "QUERY_MEMBER_INVALID", canonical)

    if query.get("disclosure_profile") != TEMPORAL_QUERY_DISCLOSURE_PROFILE:
        return _error_query(state, "DISCLOSURE_PROFILE_INVALID", canonical)
    if query.get("query_class") not in QUERY_CLASSES:
        return _error_query(state, "QUERY_CLASS_INVALID", canonical)
    if query.get("time_basis") not in TIME_BASES:
        return _error_query(state, "TIME_BASIS_INVALID", canonical)
    if query.get("interval_semantics") not in INTERVAL_SEMANTICS:
        return _error_query(state, "INTERVAL_SEMANTICS_INVALID", canonical)
    if query.get("point_event_semantics") not in POINT_EVENT_SEMANTICS:
        return _error_query(state, "POINT_EVENT_SEMANTICS_INVALID", canonical)
    if query.get("master_time") not in MASTER_TIME_RULES:
        return _error_query(state, "MASTER_TIME_INVALID", canonical)
    controlling = query.get("controlling_layer_id")
    if controlling is not None and (
        not isinstance(controlling, str) or not REF_PATTERN.fullmatch(controlling)
    ):
        return _error_query(state, "CONTROLLING_LAYER_INVALID", canonical)

    start = _selection_boundary(selection, "start")
    end = _selection_boundary(selection, "end")
    if start is None:
        return _error_query(state, "SELECTION_START_REQUIRED", canonical)
    if selection.get("selection_mode") not in {"INSTANT", "WINDOW"}:
        return _error_query(state, "SELECTION_MODE_INVALID", canonical)
    if selection.get("anchor") not in {"START", "END", "CENTER"}:
        return _error_query(state, "SELECTION_ANCHOR_INVALID", canonical)
    support_ref = selection.get("support_ref")
    if support_ref is not None and (
        not isinstance(support_ref, str) or not REF_PATTERN.fullmatch(support_ref)
    ):
        return _error_query(state, "SUPPORT_REF_INVALID", canonical)

    start_result = normalize_boundary(start)
    end_result = normalize_boundary(end) if end is not None else None
    boundary_results = [start_result] + (
        [end_result] if end_result is not None else []
    )
    if any(result.status == "ERROR" for result in boundary_results):
        error = next(result for result in boundary_results if result.status == "ERROR")
        return _error_query(state, error.code, canonical)
    if any(result.status == "UNSUPPORTED" for result in boundary_results):
        unsupported = next(
            result for result in boundary_results if result.status == "UNSUPPORTED"
        )
        return NormalizedQuery(
            "UNSUPPORTED",
            unsupported.code,
            query_id,
            canonical,
            start_result,
            end_result,
        )

    if end_result is not None:
        if start_result.profile != end_result.profile:
            return _error_query(state, "MIXED_BOUNDARY_PROFILES", canonical)
        if start_result.normalized is not None and end_result.normalized is not None:
            start_time, _ = _parse_aware(start_result.normalized)
            end_time, _ = _parse_aware(end_result.normalized)
            if (
                (
                    start_time is not None
                    and end_time is not None
                    and start_time > end_time
                )
                or start_result.normalized > end_result.normalized
            ):
                return _error_query(state, "REVERSED_INTERVAL", canonical)
        elif start_result.profile in {"date_only", "month", "year"}:
            start_key = _calendar_key(start_result.profile, start_result.raw)
            end_key = _calendar_key(end_result.profile, end_result.raw)
            if start_key is not None and end_key is not None and start_key > end_key:
                return _error_query(state, "REVERSED_INTERVAL", canonical)
        elif (
            start_result.profile == "uncertain_range"
            and start_result.raw != end_result.raw
        ):
            return NormalizedQuery(
                "UNSUPPORTED",
                "UNCERTAIN_ORDERING",
                query_id,
                canonical,
                start_result,
                end_result,
            )

    mode = display.get("mode")
    step_rule = display.get("step_rule")
    direction = display.get("direction")
    missing_policy = display.get("missing_data_policy")
    aggregate = display.get("aggregate_semantics")
    window_duration = display.get("window_duration")
    if mode not in MODES:
        return _error_query(state, "DISPLAY_MODE_INVALID", canonical)
    if step_rule not in STEP_RULES:
        return _error_query(state, "STEP_RULE_INVALID", canonical)
    if direction not in {"FORWARD", "BACKWARD"}:
        return _error_query(state, "DIRECTION_INVALID", canonical)
    if missing_policy not in {"PAUSE", "WITHHOLD_LAYER", "PRESENTATION_SKIP"}:
        return _error_query(state, "MISSING_DATA_POLICY_INVALID", canonical)
    if aggregate not in AGGREGATES:
        return _error_query(state, "AGGREGATE_INVALID", canonical)
    if window_duration is not None and (
        not isinstance(window_duration, str) or not window_duration
    ):
        return _error_query(state, "WINDOW_DURATION_INVALID", canonical)

    if mode == "SNAPSHOT" and step_rule != "NONE":
        return _error_query(state, "SNAPSHOT_STEP_INVALID", canonical)
    if mode == "MOVING_WINDOW" and (
        step_rule not in {"REGULAR", "CALENDAR"}
        or selection.get("selection_mode") != "WINDOW"
        or window_duration is None
    ):
        return _error_query(state, "MOVING_WINDOW_CONFIGURATION_INVALID", canonical)
    if mode == "ACCUMULATION" and aggregate == "NONE":
        return _error_query(state, "ACCUMULATION_SEMANTICS_REQUIRED", canonical)
    if mode == "EVENT_STEP" and step_rule != "AVAILABLE_EVENT":
        return _error_query(state, "EVENT_STEP_RULE_REQUIRED", canonical)
    if mode == "COMPARISON":
        if (
            not comparison.get("enabled")
            or comparison.get("left") is None
            or comparison.get("right") is None
        ):
            return _error_query(state, "COMPARISON_SIDES_REQUIRED", canonical)
        if comparison.get("compatibility") == "INCOMPATIBLE":
            return _error_query(state, "COMPARISON_INCOMPATIBLE", canonical)
    elif comparison.get("enabled"):
        return _error_query(state, "COMPARISON_MODE_REQUIRED", canonical)

    if pins.get("pin_status") not in {"PINNED", "UNPINNED"}:
        return _error_query(state, "PIN_STATUS_INVALID", canonical)
    dataset_refs = pins.get("dataset_version_refs")
    release_refs = pins.get("release_refs")
    if not isinstance(dataset_refs, list) or not isinstance(release_refs, list):
        return _error_query(state, "PIN_REFS_INVALID", canonical)
    if pins.get("pin_status") == "PINNED" and not dataset_refs and not release_refs:
        return _error_query(state, "PIN_REQUIRED_FOR_PINNED", canonical)

    cutoff = as_of.get("knowledge_cutoff")
    if cutoff is not None:
        cutoff_result = normalize_boundary(
            {"profile": "instant", "raw": cutoff, "normalized": cutoff}
        )
        if cutoff_result.status != "SUPPORTED":
            return NormalizedQuery(
                cutoff_result.status,
                cutoff_result.code,
                query_id if cutoff_result.status == "UNSUPPORTED" else None,
                canonical,
                start_result,
                end_result,
            )

    return NormalizedQuery(
        "SUPPORTED",
        "OK",
        query_id,
        canonical,
        start_result,
        end_result,
    )


def validate_temporal_view_state(
    state: Mapping[str, Any],
) -> tuple[str, tuple[str, ...]]:
    """Run semantic checks after JSON Schema validation."""

    findings: list[str] = []
    if state.get("profile") != TEMPORAL_VIEW_STATE_PROFILE:
        findings.append("PROFILE_INVALID")
    if state.get("schema_version") != TEMPORAL_VIEW_STATE_SCHEMA_VERSION:
        findings.append("SCHEMA_VERSION_INVALID")
    active_layers = state.get("active_layer_ids")
    if not isinstance(active_layers, list) or len(set(active_layers)) != len(active_layers):
        findings.append("ACTIVE_LAYER_IDS_INVALID")
    spatial_scope = state.get("spatial_scope")
    if (
        not isinstance(spatial_scope, Mapping)
        or spatial_scope.get("public_safe") is not True
    ):
        findings.append("SPATIAL_SCOPE_NOT_PUBLIC_SAFE")
    if state.get("state_id") != compute_state_id(state):
        findings.append("STATE_ID_MISMATCH")

    query_result = normalize_temporal_query(state)
    if query_result.status == "ERROR":
        findings.append(query_result.code)
        return "ERROR", tuple(findings)
    if query_result.status == "UNSUPPORTED":
        findings.append(query_result.code)
        return "UNSUPPORTED", tuple(findings)
    return "SUPPORTED", tuple(findings)


def validate_frame_context(frame: TemporalFrameContext) -> tuple[str, str]:
    if frame.profile != TEMPORAL_FRAME_CONTEXT_PROFILE:
        return "ERROR", "FRAME_PROFILE_INVALID"
    if frame.outcome not in {"ANSWER", "ABSTAIN"}:
        return "ERROR", "FRAME_OUTCOME_BLOCKED"
    layer_ids = [layer.layer_id for layer in frame.layers]
    if len(layer_ids) != len(set(layer_ids)):
        return "ERROR", "DUPLICATE_LAYER_FRAME"
    for layer in frame.layers:
        if layer.availability == "AVAILABLE":
            if layer.actual_time is None or layer.release_status != "RELEASED":
                return "ERROR", "AVAILABLE_LAYER_INCOMPLETE"
        elif layer.availability == "WITHHELD":
            if layer.actual_time is not None or layer.evidence_refs:
                return "ERROR", "WITHHELD_DATA_LEAK"
        elif layer.availability in {
            "OUTSIDE_COVERAGE",
            "UNAVAILABLE",
            "EXPIRED",
            "CORRECTED",
        }:
            if layer.actual_time is not None:
                return "ERROR", "NONAVAILABLE_TIME_LEAK"
        else:
            return "ERROR", "AVAILABILITY_INVALID"
    return "SUPPORTED", "OK"


def create_runtime_state() -> TemporalRuntimeState:
    return TemporalRuntimeState(0, "IDLE", None, None, None, None)


def request_frame(
    state: Mapping[str, Any],
    previous: TemporalRuntimeState | None = None,
) -> TemporalRuntimeState:
    query_result = normalize_temporal_query(state)
    generation = (previous.generation + 1) if previous is not None else 1
    committed = previous.committed_frame if previous is not None else None
    if query_result.status == "SUPPORTED":
        return TemporalRuntimeState(
            generation,
            "LOADING",
            state,
            query_result.query_id,
            committed,
            None,
        )
    return TemporalRuntimeState(
        generation,
        query_result.status,
        state,
        query_result.query_id,
        committed,
        query_result.code,
    )


def commit_frame(
    runtime: TemporalRuntimeState,
    generation: int,
    frame: TemporalFrameContext,
) -> TemporalRuntimeState:
    """Commit only the current request and preserve prior pixels otherwise."""

    if generation != runtime.generation:
        return runtime
    if runtime.requested_state is None or runtime.requested_query_id is None:
        return runtime
    if frame.state_id != compute_state_id(runtime.requested_state):
        return runtime
    if frame.query_id != runtime.requested_query_id:
        return runtime
    frame_status, frame_code = validate_frame_context(frame)
    if frame_status != "SUPPORTED":
        return replace(runtime, status="ERROR", error_code=frame_code)
    return replace(runtime, status="COMMITTED", committed_frame=frame, error_code=None)


def fail_frame(
    runtime: TemporalRuntimeState,
    generation: int,
    code: str,
) -> TemporalRuntimeState:
    if generation != runtime.generation:
        return runtime
    return replace(runtime, status="ERROR", error_code=code)


__all__ = [
    "AGGREGATES",
    "BOUNDARY_PROFILES",
    "TEMPORAL_FRAME_CONTEXT_PROFILE",
    "TEMPORAL_QUERY_DISCLOSURE_PROFILE",
    "TEMPORAL_VIEW_STATE_PROFILE",
    "TEMPORAL_VIEW_STATE_SCHEMA_VERSION",
    "TemporalFrameContext",
    "TemporalFrameLayer",
    "TemporalNormalization",
    "TemporalRuntimeState",
    "NormalizedQuery",
    "canonical_json",
    "commit_frame",
    "compute_query_id",
    "compute_state_id",
    "create_runtime_state",
    "fail_frame",
    "normalize_boundary",
    "normalize_temporal_query",
    "request_frame",
    "validate_frame_context",
    "validate_temporal_view_state",
]
