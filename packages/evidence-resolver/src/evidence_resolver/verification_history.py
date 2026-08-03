"""Standard-library VerificationStateHistory validation and replay primitives.

The evidence resolver and the repository validator share this module so the
resolver cannot drift from the bounded replay semantics it consumes.  The
module performs no I/O and grants no evidence, policy, review, release, or
publication authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import re
from typing import Mapping


_DIGEST = re.compile(r"^sha256:[a-f0-9]{64}$")
_HISTORY_ID = re.compile(
    r"^kfm:verification-history:[a-z0-9][a-z0-9._:-]{0,127}$"
)
_KFM_REF = re.compile(r"^kfm://[A-Za-z0-9._~:/-]+$")
_EVENT_ID = re.compile(r"^evt:[a-z0-9][a-z0-9._-]{0,63}$")
_REASON_CODE = re.compile(r"^[A-Z][A-Z0-9_]{2,63}$")
_TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

_EVENT_TYPES = frozenset(
    {"VERIFIED", "REVERIFIED", "CORRECTED", "SUPERSEDED", "REVOKED"}
)
_STATES = frozenset({"ACTIVE", "CORRECTED", "SUPERSEDED", "REVOKED"})
_ALLOWED_TRANSITIONS = {
    "ACTIVE": frozenset({"CORRECTED", "SUPERSEDED", "REVOKED"}),
    "CORRECTED": frozenset({"REVERIFIED", "SUPERSEDED", "REVOKED"}),
    "REVOKED": frozenset({"REVERIFIED"}),
    "SUPERSEDED": frozenset(),
}
_EVENT_STATE = {
    "VERIFIED": "ACTIVE",
    "REVERIFIED": "ACTIVE",
    "CORRECTED": "CORRECTED",
    "SUPERSEDED": "SUPERSEDED",
    "REVOKED": "REVOKED",
}
_EVENT_FIELDS = frozenset(
    {
        "event_id",
        "event_type",
        "state",
        "effective_at",
        "recorded_at",
        "reason_code",
        "basis_refs",
        "relates_to_event_id",
        "correction_ref",
        "replacement_ref",
        "revocation_ref",
    }
)
_EVENT_REQUIRED = frozenset(
    {
        "event_id",
        "event_type",
        "state",
        "effective_at",
        "recorded_at",
        "reason_code",
        "basis_refs",
    }
)
_EVENT_EXTRAS = {
    "VERIFIED": frozenset(),
    "REVERIFIED": frozenset({"relates_to_event_id"}),
    "CORRECTED": frozenset({"relates_to_event_id", "correction_ref"}),
    "SUPERSEDED": frozenset({"relates_to_event_id", "replacement_ref"}),
    "REVOKED": frozenset({"relates_to_event_id", "revocation_ref"}),
}


@dataclass(frozen=True, order=True)
class HistoryFinding:
    """Stable verification-history finding without reflected input values."""

    code: str
    path: str


@dataclass(frozen=True)
class ReplayResult:
    """One deterministic bitemporal replay result."""

    state: str
    event_id: str | None
    event_type: str | None
    effective_at: str | None
    recorded_at: str | None
    answer_blocked: bool


def canonical_spec_hash(document: Mapping[str, object]) -> str:
    """Hash canonical JSON after removing the self-referential spec_hash."""

    identity_document = {
        key: value for key, value in document.items() if key != "spec_hash"
    }
    canonical = json.dumps(
        identity_document,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def parse_timestamp(value: str) -> datetime:
    """Parse one real UTC-second timestamp used by the bounded profile."""

    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError) as exc:
        raise ValueError("timestamp must be a real UTC second") from exc
    return parsed.replace(tzinfo=timezone.utc)


def _shape_finding(path: str) -> HistoryFinding:
    return HistoryFinding("VERIFICATION_HISTORY_SCHEMA_INVALID", path)


def validate_history_shape(candidate: object) -> tuple[HistoryFinding, ...]:
    """Mirror the closed v1 JSON shape for standard-library consumers."""

    if not isinstance(candidate, Mapping):
        return (_shape_finding("$"),)
    required = frozenset(
        {"schema_version", "history_id", "subject_ref", "profile_id", "spec_hash", "events"}
    )
    if set(candidate) != required:
        return (_shape_finding("$"),)
    if candidate["schema_version"] != "1.0.0":
        return (_shape_finding("$.schema_version"),)
    history_id = candidate["history_id"]
    if not isinstance(history_id, str) or not _HISTORY_ID.fullmatch(history_id):
        return (_shape_finding("$.history_id"),)
    subject_ref = candidate["subject_ref"]
    if (
        not isinstance(subject_ref, str)
        or not 7 <= len(subject_ref) <= 256
        or not _KFM_REF.fullmatch(subject_ref)
    ):
        return (_shape_finding("$.subject_ref"),)
    if candidate["profile_id"] != "kfm://profile/verification-state-replay/v1":
        return (_shape_finding("$.profile_id"),)
    spec_hash = candidate["spec_hash"]
    if not isinstance(spec_hash, str) or not _DIGEST.fullmatch(spec_hash):
        return (_shape_finding("$.spec_hash"),)

    events = candidate["events"]
    if not isinstance(events, list) or not 1 <= len(events) <= 128:
        return (_shape_finding("$.events"),)
    for index, event in enumerate(events):
        path = f"$.events[{index}]"
        if not isinstance(event, Mapping):
            return (_shape_finding(path),)
        keys = set(event)
        if not _EVENT_REQUIRED.issubset(keys) or not keys.issubset(_EVENT_FIELDS):
            return (_shape_finding(path),)
        event_type = event["event_type"]
        state = event["state"]
        if not isinstance(event_type, str) or event_type not in _EVENT_TYPES:
            return (_shape_finding(f"{path}.event_type"),)
        if not isinstance(state, str) or state not in _STATES:
            return (_shape_finding(f"{path}.state"),)
        if state != _EVENT_STATE[event_type]:
            return (_shape_finding(f"{path}.state"),)
        expected_keys = _EVENT_REQUIRED | _EVENT_EXTRAS[event_type]
        if keys != expected_keys:
            return (_shape_finding(path),)

        event_id = event["event_id"]
        if not isinstance(event_id, str) or not _EVENT_ID.fullmatch(event_id):
            return (_shape_finding(f"{path}.event_id"),)
        for field in ("effective_at", "recorded_at"):
            timestamp = event[field]
            if not isinstance(timestamp, str) or not _TIMESTAMP.fullmatch(timestamp):
                return (_shape_finding(f"{path}.{field}"),)
        reason_code = event["reason_code"]
        if not isinstance(reason_code, str) or not _REASON_CODE.fullmatch(reason_code):
            return (_shape_finding(f"{path}.reason_code"),)
        basis_refs = event["basis_refs"]
        if (
            not isinstance(basis_refs, list)
            or not 1 <= len(basis_refs) <= 8
            or any(
                not isinstance(ref, str)
                or not 7 <= len(ref) <= 256
                or not _KFM_REF.fullmatch(ref)
                for ref in basis_refs
            )
        ):
            return (_shape_finding(f"{path}.basis_refs"),)
        if len(basis_refs) != len(set(basis_refs)):
            return (_shape_finding(f"{path}.basis_refs"),)
        for field in _EVENT_EXTRAS[event_type]:
            ref = event[field]
            pattern = _EVENT_ID if field == "relates_to_event_id" else _KFM_REF
            if not isinstance(ref, str) or not pattern.fullmatch(ref):
                return (_shape_finding(f"{path}.{field}"),)
    return ()


def validate_history_semantics(
    document: Mapping[str, object],
) -> tuple[HistoryFinding, ...]:
    """Check hash, append order, time axes, chain, and transitions."""

    findings: set[HistoryFinding] = set()
    if document["spec_hash"] != canonical_spec_hash(document):
        findings.add(
            HistoryFinding("VERIFICATION_HISTORY_HASH_MISMATCH", "$.spec_hash")
        )

    events = document["events"]
    assert isinstance(events, list)
    event_ids = [event["event_id"] for event in events]
    if len(event_ids) != len(set(event_ids)):
        findings.add(
            HistoryFinding("VERIFICATION_HISTORY_EVENT_ID_DUPLICATE", "$.events")
        )

    parsed_times: list[tuple[datetime, datetime]] = []
    for index, event in enumerate(events):
        try:
            effective_at = parse_timestamp(event["effective_at"])
            recorded_at = parse_timestamp(event["recorded_at"])
        except ValueError:
            findings.add(
                HistoryFinding(
                    "VERIFICATION_HISTORY_TIMESTAMP_INVALID", f"$.events[{index}]"
                )
            )
            continue
        parsed_times.append((effective_at, recorded_at))
        if effective_at > recorded_at:
            findings.add(
                HistoryFinding(
                    "VERIFICATION_HISTORY_EFFECTIVE_AFTER_RECORDED",
                    f"$.events[{index}].effective_at",
                )
            )

    if len(parsed_times) == len(events):
        order_keys = [
            (parsed_times[index][1], event["event_id"])
            for index, event in enumerate(events)
        ]
        if order_keys != sorted(order_keys):
            findings.add(
                HistoryFinding("VERIFICATION_HISTORY_EVENT_ORDER_INVALID", "$.events")
            )

    first = events[0]
    if first["event_type"] != "VERIFIED":
        findings.add(
            HistoryFinding(
                "VERIFICATION_HISTORY_INITIAL_EVENT_INVALID",
                "$.events[0].event_type",
            )
        )

    for index in range(1, len(events)):
        previous = events[index - 1]
        event = events[index]
        if event.get("relates_to_event_id") != previous["event_id"]:
            findings.add(
                HistoryFinding(
                    "VERIFICATION_HISTORY_CHAIN_INVALID",
                    f"$.events[{index}].relates_to_event_id",
                )
            )
        if event["event_type"] not in _ALLOWED_TRANSITIONS[previous["state"]]:
            findings.add(
                HistoryFinding(
                    "VERIFICATION_HISTORY_TRANSITION_INVALID",
                    f"$.events[{index}].event_type",
                )
            )
    return tuple(sorted(findings))


def validate_history(candidate: object) -> tuple[HistoryFinding, ...]:
    """Validate the closed shape and replay semantics without external I/O."""

    shape_findings = validate_history_shape(candidate)
    if shape_findings:
        return shape_findings
    assert isinstance(candidate, Mapping)
    return validate_history_semantics(candidate)


def replay_state(
    document: Mapping[str, object],
    *,
    effective_as_of: str,
    recorded_as_of: str,
) -> ReplayResult:
    """Replay a validated history at independent effective and recorded times."""

    findings = validate_history(document)
    if findings:
        codes = ",".join(sorted({finding.code for finding in findings}))
        raise ValueError(f"invalid verification history: {codes}")
    try:
        effective_query = parse_timestamp(effective_as_of)
        recorded_query = parse_timestamp(recorded_as_of)
    except ValueError as exc:
        raise ValueError("invalid replay query timestamp") from exc

    events = document["events"]
    assert isinstance(events, list)
    eligible = [
        event
        for event in events
        if parse_timestamp(event["effective_at"]) <= effective_query
        and parse_timestamp(event["recorded_at"]) <= recorded_query
    ]
    if not eligible:
        return ReplayResult(
            state="UNKNOWN",
            event_id=None,
            event_type=None,
            effective_at=None,
            recorded_at=None,
            answer_blocked=True,
        )

    selected = eligible[-1]
    state = selected["state"]
    assert isinstance(state, str)
    return ReplayResult(
        state=state,
        event_id=selected["event_id"],
        event_type=selected["event_type"],
        effective_at=selected["effective_at"],
        recorded_at=selected["recorded_at"],
        answer_blocked=state != "ACTIVE",
    )
