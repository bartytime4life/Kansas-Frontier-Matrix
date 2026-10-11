"""Bounded GHCN-Daily capture for the fixed Kansas first-order station pilot.

Fetches the station list and four by_station files through ``ghcnd.fetch``
(host-locked, size-bounded, no redirects) and returns their exact bytes with a
digest-closed manifest. It selects nothing and admits nothing: normalization
and release are separate steps.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import ghcnd

PROFILE = "kfm.ghcnd-daily-pilot-capture/v1"
SOURCE_ID = "noaa-ghcnd"
# Federally operated first-order stations: Wichita, Dodge City, Topeka, Goodland.
STATIONS = ("USW00003928", "USW00013985", "USW00013996", "USW00023065")
ELEMENTS = ("PRCP", "TMAX", "TMIN")
WINDOW_DAYS = 30
STALE_AFTER_DAYS = 3
STATION_LIST_KEY = "ghcnd-stations.txt"


@dataclass(frozen=True)
class Capture:
    manifest: dict
    objects: dict


def capture_keys() -> list[str]:
    return [STATION_LIST_KEY] + [f"by_station/{station}.csv.gz" for station in STATIONS]


def object_limit(key: str) -> int:
    return ghcnd.METADATA[STATION_LIST_KEY] if key == STATION_LIST_KEY else ghcnd.STATION_BYTES


def window(end_date: str) -> tuple[str, str]:
    """The WINDOW_DAYS observation days ending on end_date (YYYY-MM-DD), inclusive."""
    try:
        end = date.fromisoformat(end_date)
    except (TypeError, ValueError):
        raise ValueError("WINDOW_END_INVALID") from None
    if end.isoformat() != end_date:
        raise ValueError("WINDOW_END_INVALID")
    return (end - timedelta(days=WINDOW_DAYS - 1)).isoformat(), end_date


def capture(end_date: str, *, fetcher=ghcnd.fetch, clock=ghcnd.utc_now) -> Capture:
    """Fetch every planned object or raise; a partial capture is never returned."""
    start, end = window(end_date)
    pages, objects = [], {}
    for key in capture_keys():
        try:
            raw, meta = fetcher(key, object_limit(key))
        except (OSError, ValueError) as exc:
            reason = str(exc) if isinstance(exc, ValueError) and str(exc).isupper() else "SOURCE_FETCH_FAILED"
            raise ValueError(reason) from None
        if not isinstance(raw, bytes) or not 0 < len(raw) <= object_limit(key):
            raise ValueError("SOURCE_SIZE_LIMIT")
        if not isinstance(meta, dict) or meta.get("source_url") != ghcnd.object_url(key):
            raise ValueError("SOURCE_RESPONSE_INVALID")
        digest = digest_bytes(raw)
        objects[digest] = raw
        pages.append({"key": key, "url": meta["source_url"], "sha256": digest, "bytes": len(raw),
                      "retrieved_at": meta.get("retrieved_at"), "last_modified": meta.get("last_modified"),
                      "etag": meta.get("etag")})
    if end > clock()[:10]:
        raise ValueError("WINDOW_END_IN_FUTURE")
    manifest = {"profile": PROFILE, "source_id": SOURCE_ID, "station_ids": list(STATIONS),
                "elements": list(ELEMENTS), "start": start, "end": end, "pages": pages,
                "captured_at": clock(), "complete": True}
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, objects)
