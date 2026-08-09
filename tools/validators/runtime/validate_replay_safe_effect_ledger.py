"""Validate fixture-only replay-safe event/effect ledger candidates.

A PASS proves only bounded local shape, deterministic identity, attempt lineage,
and recorded duplicate suppression. It does not execute an effect or create
lifecycle, review, release, deployment, publication, or public-use authority.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for search_path in (REPO_ROOT, PACKAGE_SRC):
    if str(search_path) not in sys.path:
        sys.path.insert(0, str(search_path))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "replay_safe_effect_ledger.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "runtime"
    / "replay_safe_effect_ledger"
)
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "runtime.replay_safe_effect_ledger_candidate"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    ledger_id: str | None = None


def _object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_depth_exceeded(value: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in value:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                return True
        elif character in "]}":
            depth -= 1
    return False


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _read_bounded_regular_file(path: Path) -> tuple[str | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/")]
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
        )
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/")]
        if metadata.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        encoded = os.read(descriptor, MAX_FILE_BYTES + 1)
        if len(encoded) > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/")]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    text, findings = _read_bounded_regular_file(path)
    if text is None:
        return None, findings
    if _json_depth_exceeded(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/")]
    return value, []


def _json_pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    return "/" + "/".join(
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    )


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(
    validator: Draft202012Validator, candidate: Mapping[str, object]
) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _json_pointer(tuple(error.absolute_path)))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_json_pointer(tuple(item.absolute_path)), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _list(value: object) -> list[Mapping[str, object]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _strings(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _event_projection(event: Mapping[str, object]) -> dict[str, object]:
    return {
        "event_type": event["event_type"],
        "subject_ref": event["subject_ref"],
        "occurred_at": event["occurred_at"],
        "payload_digest": event["payload_digest"],
    }


def _expected_event_id(event: Mapping[str, object]) -> str:
    return "kfm:event:" + compute_spec_hash(_event_projection(event))


def _effect_projection(
    event: Mapping[str, object], effect: Mapping[str, object]
) -> dict[str, object]:
    return {
        "event_id": event["event_id"],
        "subject_ref": event["subject_ref"],
        "effect_type": effect["effect_type"],
        "idempotency_scope": effect["idempotency_scope"],
    }


def _identity_projection(candidate: Mapping[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in candidate.items()
        if key not in {"ledger_id", "spec_hash"}
    }


def expected_identity(candidate: Mapping[str, object]) -> tuple[str, str]:
    digest = compute_spec_hash(_identity_projection(candidate))
    return digest, "kfm://runtime/replay-safe-effect-ledger/" + digest.removeprefix("sha256:")[:24]


def _semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    event = _mapping(candidate["event"])
    effect = _mapping(candidate["effect_intent"])
    reservation = _mapping(candidate["reservation"])
    result = _mapping(candidate["result"])
    deliveries = _list(candidate["deliveries"])
    entries = _list(candidate["ledger_entries"])

    try:
        if event["event_id"] != _expected_event_id(event):
            findings.add(Finding("EVENT_ID_MISMATCH", "/event/event_id"))
        effect_digest = compute_spec_hash(_effect_projection(event, effect))
        if effect["effect_key"] != effect_digest:
            findings.add(Finding("EFFECT_KEY_MISMATCH", "/effect_intent/effect_key"))
        if effect["intent_id"] != "kfm:effect-intent:" + effect_digest:
            findings.add(Finding("INTENT_ID_MISMATCH", "/effect_intent/intent_id"))
        digest, ledger_id = expected_identity(candidate)
        if candidate["spec_hash"] != digest:
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate["ledger_id"] != ledger_id:
            findings.add(Finding("LEDGER_ID_MISMATCH", "/ledger_id"))
    except (CanonicalizationFailure, KeyError, TypeError, ValueError):
        findings.add(Finding("IDENTITY_EVALUATION_ERROR", "/"))

    delivery_ids = [str(item.get("delivery_id", "")) for item in deliveries]
    attempts = [item.get("attempt") for item in deliveries]
    if len(set(delivery_ids)) != len(delivery_ids):
        findings.add(Finding("DELIVERY_ID_DUPLICATE", "/deliveries"))
    if attempts != list(range(1, len(deliveries) + 1)):
        findings.add(Finding("DELIVERY_ATTEMPT_ORDER_INVALID", "/deliveries"))
    for index, delivery in enumerate(deliveries):
        expected_predecessor = None if index == 0 else delivery_ids[index - 1]
        if delivery.get("predecessor_delivery_ref") != expected_predecessor:
            findings.add(
                Finding(
                    "DELIVERY_PREDECESSOR_INVALID",
                    f"/deliveries/{index}/predecessor_delivery_ref",
                )
            )

    occurred = _time(event.get("occurred_at"))
    delivery_times = [_time(item.get("received_at")) for item in deliveries]
    delivery_time_by_id = dict(zip(delivery_ids, delivery_times))
    requested = _time(effect.get("requested_at"))
    reserved_at = _time(reservation.get("reserved_at"))
    completed_at = _time(reservation.get("effect_completed_at"))
    entry_times = [_time(item.get("recorded_at")) for item in entries]
    ordered_times = [item for item in delivery_times if item is not None]
    if occurred and any(item < occurred for item in ordered_times):
        findings.add(Finding("DELIVERY_TIME_INVALID", "/deliveries"))
    if ordered_times != sorted(ordered_times):
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/deliveries"))
    if occurred and requested and requested < occurred:
        findings.add(Finding("INTENT_TIME_INVALID", "/effect_intent/requested_at"))
    if requested and reserved_at and reserved_at < requested:
        findings.add(Finding("RESERVATION_TIME_INVALID", "/reservation/reserved_at"))
    if reserved_at and completed_at and completed_at < reserved_at:
        findings.add(Finding("COMPLETION_TIME_INVALID", "/reservation/effect_completed_at"))
    comparable_entry_times = [item for item in entry_times if item is not None]
    if comparable_entry_times != sorted(comparable_entry_times):
        findings.add(Finding("LEDGER_TIME_ORDER_INVALID", "/ledger_entries"))

    entry_ids = [str(item.get("entry_id", "")) for item in entries]
    if entry_ids != sorted(entry_ids) or len(set(entry_ids)) != len(entry_ids):
        findings.add(Finding("LEDGER_ENTRY_ORDER_INVALID", "/ledger_entries"))
    for index, entry in enumerate(entries):
        delivery_ref = str(entry.get("delivery_ref", ""))
        if delivery_ref not in delivery_ids:
            findings.add(
                Finding("LEDGER_DELIVERY_REF_UNBOUND", f"/ledger_entries/{index}/delivery_ref")
            )
        entry_time = entry_times[index]
        delivery_time = delivery_time_by_id.get(delivery_ref)
        if entry_time and delivery_time and entry_time < delivery_time:
            findings.add(
                Finding("LEDGER_ENTRY_BEFORE_DELIVERY", f"/ledger_entries/{index}/recorded_at")
            )
        if entry.get("state") == "RESERVED" and requested and entry_time and entry_time < requested:
            findings.add(
                Finding("RESERVATION_TIME_INVALID", f"/ledger_entries/{index}/recorded_at")
            )
        if entry.get("state") == "COMPLETED" and reserved_at and entry_time and entry_time < reserved_at:
            findings.add(
                Finding("COMPLETION_TIME_INVALID", f"/ledger_entries/{index}/recorded_at")
            )
        reasons = _strings(entry.get("reason_codes"))
        if reasons != sorted(reasons):
            findings.add(
                Finding("REASON_CODE_ORDER_INVALID", f"/ledger_entries/{index}/reason_codes")
            )
    result_reasons = _strings(result.get("reason_codes"))
    if result_reasons != sorted(result_reasons):
        findings.add(Finding("REASON_CODE_ORDER_INVALID", "/result/reason_codes"))

    states = [entry.get("state") for entry in entries]
    completed_indexes = [index for index, state in enumerate(states) if state == "COMPLETED"]
    compensation_indexes = [index for index, state in enumerate(states) if state == "COMPENSATED"]
    completed = len(completed_indexes)
    duplicate_delivery_ids = [
        delivery_id
        for delivery_id, delivery in zip(delivery_ids, deliveries)
        if delivery.get("outcome") == "DUPLICATE"
    ]
    duplicate_deliveries = len(duplicate_delivery_ids)
    duplicate_suppression_refs = [
        str(entry.get("delivery_ref", ""))
        for entry in entries
        if entry.get("state") == "DUPLICATE_SUPPRESSED"
    ]
    expected_outcome: str | None
    if "COMPENSATED" in states:
        expected_outcome = "COMPENSATED"
    elif completed == 1 and duplicate_deliveries > 0:
        expected_outcome = "DUPLICATE_SUPPRESSED"
    elif completed == 1:
        expected_outcome = "EXECUTED_ONCE"
    elif "FAILED" in states:
        expected_outcome = "FAILED"
    else:
        expected_outcome = None

    if completed > 1:
        findings.add(Finding("EFFECT_EXECUTED_MORE_THAN_ONCE", "/ledger_entries"))
    if compensation_indexes and (
        completed != 1 or completed_indexes[0] > compensation_indexes[0]
    ):
        findings.add(Finding("COMPENSATION_WITHOUT_COMPLETION", "/ledger_entries"))
    if result.get("completed_effect_count") != min(completed, 1):
        findings.add(Finding("COMPLETED_EFFECT_COUNT_MISMATCH", "/result/completed_effect_count"))
    if result.get("duplicate_delivery_count") != duplicate_deliveries:
        findings.add(
            Finding(
                "DUPLICATE_DELIVERY_COUNT_MISMATCH",
                "/result/duplicate_delivery_count",
            )
        )
    if sorted(duplicate_delivery_ids) != sorted(duplicate_suppression_refs):
        findings.add(Finding("DUPLICATE_SUPPRESSION_INCOMPLETE", "/ledger_entries"))
    if expected_outcome is None or result.get("outcome") != expected_outcome:
        findings.add(Finding("RESULT_OUTCOME_MISMATCH", "/result/outcome"))

    expected_state = next(
        (
            state
            for state in reversed(states)
            if state in {"RESERVED", "COMPLETED", "RELEASED"}
        ),
        "NONE",
    )
    if reservation.get("state") != expected_state:
        findings.add(Finding("RESERVATION_STATE_MISMATCH", "/reservation/state"))
    token_fields = (
        reservation.get("reservation_token_digest"),
        reservation.get("reserved_by"),
        reservation.get("reserved_at"),
    )
    if reservation.get("state") == "NONE" and any(value is not None for value in token_fields):
        findings.add(Finding("RESERVATION_FIELDS_INCOHERENT", "/reservation"))
    if reservation.get("state") != "NONE" and any(value is None for value in token_fields):
        findings.add(Finding("RESERVATION_FIELDS_INCOHERENT", "/reservation"))
    if completed == 1 and reservation.get("effect_completed_at") is None:
        findings.add(Finding("COMPLETION_TIME_MISSING", "/reservation/effect_completed_at"))
    if completed == 0 and reservation.get("effect_completed_at") is not None:
        findings.add(Finding("COMPLETION_TIME_UNEXPECTED", "/reservation/effect_completed_at"))
    return findings


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _load_json_object(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(findings)))
    try:
        schema_findings = _schema_findings(_schema_validator(), candidate)
    except (OSError, json.JSONDecodeError, ValueError):
        return ValidationResult("ERROR", (Finding("SCHEMA_LOAD_ERROR", "/"),))
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(schema_findings)))
    semantic = tuple(sorted(_semantic_findings(candidate)))
    if semantic:
        return ValidationResult("DENY", semantic, str(candidate.get("ledger_id")))
    return ValidationResult("PASS", (), str(candidate.get("ledger_id")))


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, {"outcome": "ERROR", "reason": "MANIFEST_UNREADABLE"}
    mismatches: list[dict[str, object]] = []
    for case in manifest.get("cases", []):
        result = validate_file(FIXTURE_ROOT / case["file"])
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            mismatches.append(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": actual,
                }
            )
    payload = {
        "outcome": "PASS" if not mismatches else "DENY",
        "scope": SCOPE,
        "cases": len(manifest.get("cases", [])),
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "network_access": "NONE",
        "mismatches": mismatches,
    }
    return not mismatches, payload


def _result_payload(result: ValidationResult) -> dict[str, object]:
    return {
        "outcome": result.outcome,
        "scope": SCOPE,
        "ledger_id": result.ledger_id,
        "authority": "NONE",
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(json.dumps(_result_payload(result), sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
