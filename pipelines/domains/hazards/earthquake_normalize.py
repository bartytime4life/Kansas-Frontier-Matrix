"""Pure, deterministic USGS ComCat earthquake normalization from verified captured bytes.

Produces review candidates only: a complete capture is neither source admission
nor release. Each month's page is parsed by the existing offline parser; a page
that reaches the query limit may be truncated and refuses the whole capture.
Events are assigned to the half-open month window that owns their origin time,
so an event at a month boundary, returned by both inclusive FDSN queries, is
kept once. Events ComCat marks deleted are withheld and counted. Selection is
the Kansas context envelope, not a state-boundary join: records outside a
coarse Kansas rectangle carry CONTEXT_MARGIN. A parsed catalog proves neither
completeness nor that the absence of a record means no earthquake.
"""
from __future__ import annotations

from datetime import datetime, timedelta
import json
import re

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.usgs.src.usgs import earthquake
from connectors.usgs.src.usgs.earthquake_capture import (
    BOUNDS, EMPTY, PAGE_BYTES, PROFILE, QUERY_LIMIT, SOURCE_ID, data_year, month_keys, object_url, window,
)

CANDIDATE_PROFILE = "kfm.earthquake-candidate/v1"
RECORD_PROFILE = "kfm.earthquake-record/v1"
DIGEST = re.compile(r"sha256:[a-f0-9]{64}\Z")
WITHHELD = ("STATUS_DELETED",)
FLAGS = ("MAGNITUDE_ABSENT", "DEPTH_ABSENT", "REVIEW_AUTOMATIC", "REVIEW_STATUS_UNKNOWN", "CONTEXT_MARGIN")
# Coarse Kansas rectangle (west, south, east, north): 102°03'W, 37°N, 94°35'W, 40°N. Outside it the
# epicenter is in the envelope's margin; inside it is not proof of Kansas (the Missouri River bounds
# the northeast corner).
KANSAS_RECTANGLE = (-102.0517, 37.0, -94.5884, 40.0)
MAX_EVENTS = 20_000
PLACE_LENGTH = 256


def identity(event_id: str) -> str:
    return digest_bytes(canonical_bytes([SOURCE_ID, event_id])).split(":")[1]


def number(value: float | None):
    """Four decimal places, whole values as integers, so the JSON text is the same in Python and JavaScript."""
    if value is None:
        return None
    rounded = round(value, 4) + 0.0
    return int(rounded) if rounded.is_integer() else rounded


def iso_ms(milliseconds: int | None) -> str | None:
    if milliseconds is None:
        return None
    moment = earthquake.EPOCH + timedelta(milliseconds=milliseconds)
    return moment.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def in_margin(longitude: float, latitude: float) -> bool:
    west, south, east, north = KANSAS_RECTANGLE
    return not (west <= longitude <= east and south <= latitude <= north)


def expected_flags(record: dict) -> list[str]:
    """The review flags of a kept record, in FLAGS order."""
    flags = []
    if record["magnitude"] is None:
        flags.append("MAGNITUDE_ABSENT")
    if record["depth_km"] is None:
        flags.append("DEPTH_ABSENT")
    if record["review_status"] == "automatic":
        flags.append("REVIEW_AUTOMATIC")
    elif record["review_status"] != "reviewed":
        flags.append("REVIEW_STATUS_UNKNOWN")
    if in_margin(record["longitude"], record["latitude"]):
        flags.append("CONTEXT_MARGIN")
    return flags


def _optional_text(value, limit: int) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not 0 < len(value) <= limit or any(ord(c) < 32 for c in value):
        raise ValueError("FEATURE_TEXT_INVALID")
    return value


def record(event: earthquake.EventCandidate, page: dict) -> dict:
    """A closed candidate record; the raw feature stays out and is bound by feature_sha256."""
    props = json.loads(event.raw_feature_json)["properties"]
    key = identity(event.event_id)
    value = {"profile": RECORD_PROFILE, "id": "kfm:quake:" + key, "event_id": event.event_id,
             "aliases": list(event.aliases), "origin_utc": iso_ms(event.origin_ms), "updated_utc": iso_ms(event.updated_ms),
             "longitude": number(event.longitude), "latitude": number(event.latitude), "depth_km": number(event.depth_km),
             "magnitude": number(event.magnitude), "magnitude_type": _optional_text(event.magnitude_type, 16),
             "review_status": _optional_text(event.review_status, 16), "net": _optional_text(props.get("net"), 16),
             "place": _optional_text(props.get("place"), PLACE_LENGTH), "flags": [],
             "feature_sha256": event.feature_sha256, "page_digest": page["sha256"],
             "retrieved_at": page["retrieved_at"], "evidence_ref": "kfm:evidence:quake:" + key}
    value["flags"] = expected_flags(value)
    value["record_digest"] = digest_bytes(canonical_bytes(value))
    return value


def year_state(year: int, retrieved_at: str) -> str:
    """CLOSED once the capture is after the data year; ComCat still revises closed years."""
    return "CLOSED" if int(retrieved_at[:4]) > year else "OPEN"


def _verified_pages(manifest: dict, objects: dict[str, bytes]) -> list[tuple[dict, bytes]]:
    body = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != digest_bytes(canonical_bytes(body)):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    if manifest.get("profile") != PROFILE or manifest.get("complete") is not True:
        raise ValueError("CAPTURE_INCOMPLETE")
    try:
        keys = month_keys(manifest.get("data_year"))
    except ValueError:
        raise ValueError("CAPTURE_SCOPE_MISMATCH") from None
    if (manifest.get("source_id") != SOURCE_ID or manifest.get("bounds") != BOUNDS
            or manifest.get("query_limit") != QUERY_LIMIT):
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    pages = manifest.get("pages")
    if (not isinstance(pages, list) or not all(isinstance(p, dict) for p in pages)
            or [p.get("key") for p in pages] != keys):
        raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
    verified = []
    for page in pages:
        status, sha = page.get("status"), page.get("sha256")
        raw = b"" if status == 204 else objects.get(sha)
        if (page.get("url") != object_url(page["key"]) or status not in (200, 204) or not DIGEST.fullmatch(str(sha))
                or raw is None or digest_bytes(raw) != sha or len(raw) != page.get("bytes")
                or len(raw) > PAGE_BYTES or (status == 204) != (sha == EMPTY)
                or not isinstance(page.get("retrieved_at"), str)
                or page["retrieved_at"] > manifest.get("captured_at", "")):
            raise ValueError("PAGE_DIGEST_MISMATCH")
        verified.append((page, raw))
    return verified


def normalize_capture(manifest: dict, objects: dict[str, bytes]) -> dict:
    """Check capture closure and scope, then keep each month's owned Kansas-envelope earthquakes."""
    pages = _verified_pages(manifest, objects)
    year = manifest["data_year"]
    records, months, seen = [], [], set()
    withheld = {reason: 0 for reason in WITHHELD}
    for page, raw in pages:
        plan = window(page["key"])
        try:
            snapshot = earthquake.parse_snapshot(raw, status=page["status"], source_url=page["url"],
                                                 retrieved_at=page["retrieved_at"], max_bytes=PAGE_BYTES)
            owned = earthquake.select_earthquakes(snapshot, start=plan.start, end=plan.end_exclusive, bounds=BOUNDS)
        except earthquake.EarthquakeInputError as exc:
            raise ValueError("QUERY_PAGE_" + str(exc)) from None
        if snapshot.query_limit_reached:
            raise ValueError("WINDOW_LIMIT_REACHED")
        boundary = (datetime.fromisoformat(plan.end_exclusive.replace("Z", "+00:00"))
                    - earthquake.EPOCH) // timedelta(milliseconds=1)
        # The FDSN query includes both endpoints; anything returned but not owned must be the next month's
        # boundary event. Any other event outside the window, envelope or type is upstream drift.
        owned_ids = {event.event_id for event in owned}
        for event in snapshot.events:
            if event.event_id not in owned_ids and (event.event_type != "earthquake" or event.origin_ms != boundary):
                raise ValueError("WINDOW_SCOPE_MISMATCH")
        kept = 0
        for event in owned:
            if seen.intersection(event.aliases):
                raise ValueError("IDENTITY_CONFLICT")
            seen.update(event.aliases)
            if event.review_status == "deleted":
                withheld["STATUS_DELETED"] += 1
                continue
            records.append(record(event, page))
            kept += 1
        months.append({"month": int(page["key"][5:]), "query_status": page["status"], "events": kept})
    if len(records) > MAX_EVENTS:
        raise ValueError("EVENT_COUNT_LIMIT")
    records.sort(key=lambda r: (r["origin_utc"], r["event_id"]))
    candidate = {"profile": CANDIDATE_PROFILE, "capture_id": manifest["capture_id"], "source_id": SOURCE_ID,
                 "data_year": data_year(year), "bounds": BOUNDS, "retrieved_at": manifest["captured_at"],
                 "months": months, "observations": records,
                 "latest_event_date": max((r["origin_utc"][:10] for r in records), default=None),
                 "withheld_counts": withheld, "year_state": year_state(year, manifest["captured_at"]),
                 "coverage": "NOT_ESTABLISHED", "review_state": "PENDING", "source_admission": "PENDING",
                 "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest_bytes(canonical_bytes(candidate))
    return candidate
