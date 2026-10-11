"""Bounded USCRN daily01 capture for the two Kansas reference stations.

Fetches NOAA's headers.txt and each station-year file the 30-day window needs
(two years when the window crosses New Year) through ``uscrn_daily.fetch``
(host-locked, size-bounded, no redirects) and returns their exact bytes with a
digest-closed manifest. It selects nothing and admits nothing: normalization
and release are separate steps.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import uscrn_daily

PROFILE = "kfm.uscrn-daily-pilot-capture/v1"
SOURCE_ID = "noaa-uscrn"
STATIONS = tuple(uscrn_daily.STATIONS)
VARIABLES = ("SOIL_MOISTURE", "SOIL_TEMP")
WINDOW_DAYS = 30
STALE_AFTER_DAYS = 3


@dataclass(frozen=True)
class Capture:
    manifest: dict
    objects: dict


def window(end_date: str) -> tuple[str, str]:
    """The WINDOW_DAYS local-standard-time days ending on end_date (YYYY-MM-DD), inclusive."""
    try:
        end = date.fromisoformat(end_date)
    except (TypeError, ValueError):
        raise ValueError("WINDOW_END_INVALID") from None
    if end.isoformat() != end_date:
        raise ValueError("WINDOW_END_INVALID")
    return (end - timedelta(days=WINDOW_DAYS - 1)).isoformat(), end_date


def capture_keys(end_date: str) -> list[str]:
    start, end = window(end_date)
    years = sorted({int(start[:4]), int(end[:4])})
    return [uscrn_daily.HEADERS_KEY] + [uscrn_daily.station_year_key(year, wban) for wban in STATIONS for year in years]


def object_limit(key: str) -> int:
    return uscrn_daily.object_limit(key)


def capture(end_date: str, *, fetcher=uscrn_daily.fetch, clock=uscrn_daily.utc_now) -> Capture:
    """Fetch every planned object or raise; a partial capture is never returned."""
    start, end = window(end_date)
    pages, objects = [], {}
    for key in capture_keys(end_date):
        try:
            raw, meta = fetcher(key, object_limit(key))
        except (OSError, ValueError) as exc:
            reason = str(exc) if isinstance(exc, ValueError) and str(exc).isupper() else "SOURCE_FETCH_FAILED"
            raise ValueError(reason) from None
        if not isinstance(raw, bytes) or not 0 < len(raw) <= object_limit(key):
            raise ValueError("SOURCE_SIZE_LIMIT")
        if not isinstance(meta, dict) or meta.get("source_url") != uscrn_daily.object_url(key):
            raise ValueError("SOURCE_RESPONSE_INVALID")
        if key == uscrn_daily.HEADERS_KEY:
            uscrn_daily.check_headers(raw)
        digest = digest_bytes(raw)
        objects[digest] = raw
        pages.append({"key": key, "url": meta["source_url"], "sha256": digest, "bytes": len(raw),
                      "retrieved_at": meta.get("retrieved_at"), "last_modified": meta.get("last_modified"),
                      "etag": meta.get("etag")})
    if end > clock()[:10]:
        raise ValueError("WINDOW_END_IN_FUTURE")
    manifest = {"profile": PROFILE, "source_id": SOURCE_ID, "station_ids": list(STATIONS),
                "variables": list(VARIABLES), "depths_cm": list(uscrn_daily.DEPTHS_CM),
                "start": start, "end": end, "pages": pages, "captured_at": clock(), "complete": True}
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, objects)
