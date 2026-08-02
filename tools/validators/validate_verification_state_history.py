#!/usr/bin/env python3
"""Validate and replay the bounded VerificationStateHistory profile."""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/verification_state_history.schema.json"
)
FIXTURES_ROOT = (
    REPO_ROOT / "fixtures/contracts/v1/evidence/verification_state_history"
)
SCOPE = "evidence.verification_state_history"
_SCHEMA_VALIDATOR = load_validator(SCHEMA_PATH)

_ALLOWED_TRANSITIONS = {
    "ACTIVE": frozenset({"CORRECTED", "SUPERSEDED", "REVOKED"}),
    "CORRECTED": frozenset({"REVERIFIED", "SUPERSEDED", "REVOKED"}),
    "REVOKED": frozenset({"REVERIFIED"}),
    "SUPERSEDED": frozenset(),
}


@dataclass(frozen=True)
class ReplayResult:
    """One deterministic bitemporal replay result."""

    state: str
    event_id: str | None
    event_type: str | None
    effective_at: str | None
    recorded_at: str | None
    answer_blocked: bool


def canonical_spec_hash(document: dict[str, object]) -> str:
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


def _json_path(error_path: Sequence[object]) -> str:
    result = "$"
    for part in error_path:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _parse_timestamp(value: str) -> datetime:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError) as exc:
        raise ValueError("timestamp must be a real UTC second") from exc
    return parsed.replace(tzinfo=timezone.utc)


def validate_document(candidate: object) -> list[Finding]:
    """Validate shape, hash, append order, time axes, and transition chain."""

    findings: set[Finding] = set()
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "VERIFICATION_HISTORY_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(
            findings,
            "VERIFICATION_HISTORY_HASH_MISMATCH",
            "$.spec_hash",
        )

    events = candidate["events"]
    assert isinstance(events, list)
    event_ids = [event["event_id"] for event in events]
    if len(event_ids) != len(set(event_ids)):
        add_finding(
            findings,
            "VERIFICATION_HISTORY_EVENT_ID_DUPLICATE",
            "$.events",
        )

    parsed_times: list[tuple[datetime, datetime]] = []
    for index, event in enumerate(events):
        try:
            effective_at = _parse_timestamp(event["effective_at"])
            recorded_at = _parse_timestamp(event["recorded_at"])
        except ValueError:
            add_finding(
                findings,
                "VERIFICATION_HISTORY_TIMESTAMP_INVALID",
                f"$.events[{index}]",
            )
            continue
        parsed_times.append((effective_at, recorded_at))
        if effective_at > recorded_at:
            add_finding(
                findings,
                "VERIFICATION_HISTORY_EFFECTIVE_AFTER_RECORDED",
                f"$.events[{index}].effective_at",
            )

    if len(parsed_times) == len(events):
        order_keys = [
            (parsed_times[index][1], event["event_id"])
            for index, event in enumerate(events)
        ]
        if order_keys != sorted(order_keys):
            add_finding(
                findings,
                "VERIFICATION_HISTORY_EVENT_ORDER_INVALID",
                "$.events",
            )

    first = events[0]
    if first["event_type"] != "VERIFIED":
        add_finding(
            findings,
            "VERIFICATION_HISTORY_INITIAL_EVENT_INVALID",
            "$.events[0].event_type",
        )

    for index in range(1, len(events)):
        previous = events[index - 1]
        event = events[index]
        if event.get("relates_to_event_id") != previous["event_id"]:
            add_finding(
                findings,
                "VERIFICATION_HISTORY_CHAIN_INVALID",
                f"$.events[{index}].relates_to_event_id",
            )
        allowed = _ALLOWED_TRANSITIONS[previous["state"]]
        if event["event_type"] not in allowed:
            add_finding(
                findings,
                "VERIFICATION_HISTORY_TRANSITION_INVALID",
                f"$.events[{index}].event_type",
            )

    return sorted(findings)


def validate_history_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def replay_state(
    document: dict[str, object],
    *,
    effective_as_of: str,
    recorded_as_of: str,
) -> ReplayResult:
    """Replay a validated history at independent effective and recorded times."""

    findings = validate_document(document)
    if findings:
        codes = ",".join(sorted({finding.code for finding in findings}))
        raise ValueError(f"invalid verification history: {codes}")
    try:
        effective_query = _parse_timestamp(effective_as_of)
        recorded_query = _parse_timestamp(recorded_as_of)
    except ValueError as exc:
        raise ValueError("invalid replay query timestamp") from exc

    events = document["events"]
    assert isinstance(events, list)
    eligible = [
        event
        for event in events
        if _parse_timestamp(event["effective_at"]) <= effective_query
        and _parse_timestamp(event["recorded_at"]) <= recorded_query
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


def _run_fixture_suite() -> int:
    ok = True
    for expected_valid, directory in (
        (True, FIXTURES_ROOT / "valid"),
        (False, FIXTURES_ROOT / "invalid"),
    ):
        files = sorted(directory.glob("*.json"))
        if not files:
            print(f"FAIL {directory}: no JSON fixtures found")
            ok = False
            continue
        for path in files:
            findings = validate_history_file(path)
            accepted = not findings
            if accepted == expected_valid:
                label = "OK" if expected_valid else "EXPECTED_FAIL"
                print(f"{label} {path}")
            else:
                print(serialize_result(SCOPE, path, findings))
                ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return _run_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate bounded VerificationStateHistory fixtures.",
        scope=SCOPE,
        validator=validate_history_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
