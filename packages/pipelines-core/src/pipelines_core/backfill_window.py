"""Deterministic, side-effect-free backfill-window planning primitives."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import UTC, datetime, timedelta
from typing import Any, Mapping

PLANNER_VERSION = "v1"
MAX_WINDOW = timedelta(days=366)
_DATASET_ID = re.compile(r"^[a-z][a-z0-9._-]{0,127}$")
_SHA256 = re.compile(r"^sha256:[a-f0-9]{64}$")


class BackfillPlanError(ValueError):
    """Raised when a request cannot produce a bounded deterministic plan."""

    def __init__(self, code: str, field: str) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


def _canonical_json(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, RecursionError) as exc:
        raise BackfillPlanError("MANIFEST_NOT_CANONICAL_JSON", "/manifest") from exc


def _parse_utc(value: object, field: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise BackfillPlanError("WINDOW_NOT_UTC_Z", field)
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise BackfillPlanError("WINDOW_DATETIME_INVALID", field) from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise BackfillPlanError("WINDOW_NOT_UTC_Z", field)
    if parsed.microsecond:
        raise BackfillPlanError("WINDOW_SUBSECOND_UNSUPPORTED", field)
    return parsed.astimezone(UTC)


def _iso_z(value: datetime) -> str:
    return value.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _compact(value: datetime) -> str:
    return value.astimezone(UTC).strftime("%Y%m%dT%H%M%SZ")


def _hash(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def plan_backfill_window(request: Mapping[str, Any]) -> dict[str, Any]:
    """Return a deterministic plan without fetching or writing anything."""

    if not isinstance(request, Mapping):
        raise BackfillPlanError("REQUEST_NOT_OBJECT", "/")

    expected_keys = {
        "dataset_id",
        "source_uri",
        "window",
        "manifest",
        "current_published_spec_hash",
    }
    if set(request) != expected_keys:
        raise BackfillPlanError("REQUEST_KEYS_INVALID", "/")

    dataset_id = request["dataset_id"]
    if not isinstance(dataset_id, str) or not _DATASET_ID.fullmatch(dataset_id):
        raise BackfillPlanError("DATASET_ID_INVALID", "/dataset_id")

    source_uri = request["source_uri"]
    if (
        not isinstance(source_uri, str)
        or len(source_uri) > 2048
        or any(char.isspace() for char in source_uri)
        or not source_uri.startswith(("https://", "kfm://"))
    ):
        raise BackfillPlanError("SOURCE_URI_INVALID", "/source_uri")

    window = request["window"]
    if not isinstance(window, Mapping) or set(window) != {"start", "end"}:
        raise BackfillPlanError("WINDOW_SHAPE_INVALID", "/window")
    start = _parse_utc(window["start"], "/window/start")
    end = _parse_utc(window["end"], "/window/end")
    if start >= end:
        raise BackfillPlanError("WINDOW_ORDER_INVALID", "/window")
    if end - start > MAX_WINDOW:
        raise BackfillPlanError("WINDOW_TOO_LARGE", "/window")

    manifest = request["manifest"]
    if not isinstance(manifest, Mapping) or not manifest:
        raise BackfillPlanError("MANIFEST_EMPTY_OR_INVALID", "/manifest")
    canonical_manifest = _canonical_json(manifest)
    spec_hash = _hash(canonical_manifest)

    current = request["current_published_spec_hash"]
    if current is not None and (not isinstance(current, str) or not _SHA256.fullmatch(current)):
        raise BackfillPlanError("CURRENT_SPEC_HASH_INVALID", "/current_published_spec_hash")

    normalized_window = {"start": _iso_z(start), "end": _iso_z(end), "semantics": "half-open"}
    dedupe_payload = {
        "dataset_id": dataset_id,
        "source_uri": source_uri,
        "window": normalized_window,
        "spec_hash": spec_hash,
    }
    dedupe_key = _hash(_canonical_json(dedupe_payload))
    label = f"{_compact(start)}_{_compact(end)}"
    digest = spec_hash.removeprefix("sha256:")

    if current == spec_hash:
        decision = "NOOP"
        reason_codes = ["CURRENT_SPEC_MATCH"]
    elif current is None:
        decision = "REBUILD"
        reason_codes = ["CURRENT_SPEC_ABSENT"]
    else:
        decision = "REBUILD"
        reason_codes = ["CURRENT_SPEC_CHANGED"]

    return {
        "plan_id": f"backfill:{dataset_id}:{label}:{dedupe_key[-16:]}",
        "planner_version": PLANNER_VERSION,
        "dataset_id": dataset_id,
        "source_uri": source_uri,
        "window": normalized_window,
        "spec_hash": spec_hash,
        "dedupe_key": dedupe_key,
        "artifact_uri": f"data/processed/{dataset_id}/window={label}/artifact-{digest}.json",
        "current_published_spec_hash": current,
        "decision": decision,
        "reason_codes": reason_codes,
        "required_gates": {
            "policy_check": True,
            "signature_verification": True,
            "promotion_review": True,
        },
        "write_authority": False,
    }
