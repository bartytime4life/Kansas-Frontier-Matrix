"""Bounded USGS ComCat capture for one data year of the Kansas earthquake pilot.

Fetches twelve FDSN event queries, one per calendar month of the requested
data year, each planned by ``earthquake.history_windows`` over the Kansas
context envelope, through a host-locked, size-bounded fetch that follows no
redirects. A month with no events answers 204 with no body. Returns the exact
bytes with a digest-closed manifest. It parses, selects and admits nothing:
normalization and release are separate steps.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
import time
from urllib.request import HTTPRedirectHandler, Request, build_opener

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.usgs.src.usgs import earthquake

PROFILE = "kfm.earthquake-pilot-capture/v1"
SOURCE_ID = "usgs-earthquakes"
BOUNDS = list(earthquake.KANSAS_CONTEXT)
# Per month; a page that reaches the limit may be truncated, so normalization refuses it.
QUERY_LIMIT = 5000
PAGE_BYTES = 8 * 1024 * 1024
# The ComCat catalog is consistent for the central U.S. from the 1973 NEIC compilation onward.
FIRST_YEAR = 1973
KEY = re.compile(r"([0-9]{4})-(0[1-9]|1[0-2])\Z")
EMPTY = digest_bytes(b"")


@dataclass(frozen=True)
class Capture:
    manifest: dict
    objects: dict


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def data_year(value) -> int:
    if type(value) is not int or not FIRST_YEAR <= value <= 2200:
        raise ValueError("DATA_YEAR_INVALID")
    return value


def month_keys(year: int) -> list[str]:
    data_year(year)
    return [f"{year:04d}-{month:02d}" for month in range(1, 13)]


def window(key: str) -> earthquake.HistoryWindow:
    """The one half-open FDSN window that owns calendar month ``key`` (YYYY-MM)."""
    match = KEY.fullmatch(key) if isinstance(key, str) else None
    if match is None:
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    year, month = data_year(int(match.group(1))), int(match.group(2))
    end = f"{year + 1:04d}-01" if month == 12 else f"{year:04d}-{month + 1:02d}"
    [plan] = earthquake.history_windows(f"{key}-01T00:00:00Z", f"{end}-01T00:00:00Z", bounds=BOUNDS,
                                        window_days=31, limit=QUERY_LIMIT, max_windows=1)
    return plan


def object_url(key: str) -> str:
    return window(key).query_url


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(key: str, limit: int):
    """One bounded, host-locked GET with no redirects; returns (bytes, metadata)."""
    url = object_url(key)
    if not 0 < limit <= PAGE_BYTES:
        raise ValueError("SOURCE_LIMIT_INVALID")
    start = time.monotonic()
    with build_opener(NoRedirect).open(Request(url, headers={
            "Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas earthquake capture"}), timeout=60) as response:
        if response.status not in (200, 204) or response.geturl() != url:
            raise ValueError("SOURCE_RESPONSE_INVALID")
        declared = response.headers.get("Content-Length")
        if declared is not None and (not declared.isdigit() or int(declared) > limit):
            raise ValueError("SOURCE_SIZE_LIMIT")
        chunks, count = [], 0
        while True:
            if time.monotonic() - start > 300:
                raise ValueError("SOURCE_DEADLINE")
            chunk = response.read(min(65536, limit - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > limit:
                raise ValueError("SOURCE_SIZE_LIMIT")
            chunks.append(chunk)
        # 204 means no events and carries no body; 200 always carries a FeatureCollection.
        if (count == 0) != (response.status == 204) or (declared is not None and count != int(declared)):
            raise ValueError("SOURCE_SIZE_MISMATCH")
        return b"".join(chunks), {"source_url": url, "status": response.status, "retrieved_at": utc_now(),
                                   "last_modified": response.headers.get("Last-Modified"),
                                   "etag": response.headers.get("ETag")}


def _page(key: str, fetcher) -> tuple[dict, bytes]:
    try:
        raw, meta = fetcher(key, PAGE_BYTES)
    except (OSError, ValueError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and str(exc).isupper() else "SOURCE_FETCH_FAILED"
        raise ValueError(reason) from None
    if not isinstance(meta, dict) or meta.get("source_url") != object_url(key) or meta.get("status") not in (200, 204):
        raise ValueError("SOURCE_RESPONSE_INVALID")
    if not isinstance(raw, bytes) or len(raw) > PAGE_BYTES or (len(raw) == 0) != (meta["status"] == 204):
        raise ValueError("SOURCE_SIZE_LIMIT")
    return ({"key": key, "url": meta["source_url"], "status": meta["status"], "sha256": digest_bytes(raw),
             "bytes": len(raw), "retrieved_at": meta.get("retrieved_at"), "last_modified": meta.get("last_modified"),
             "etag": meta.get("etag")}, raw)


def capture(year: int, *, fetcher=fetch, clock=utc_now) -> Capture:
    """Fetch every month of ``year``, or raise; never a partial capture."""
    data_year(year)
    if year > int(clock()[:4]):
        raise ValueError("DATA_YEAR_IN_FUTURE")
    pages, objects = [], {}
    for key in month_keys(year):
        page, raw = _page(key, fetcher)
        pages.append(page)
        if raw:
            objects[page["sha256"]] = raw
    manifest = {"profile": PROFILE, "source_id": SOURCE_ID, "data_year": year, "bounds": BOUNDS,
                "query_limit": QUERY_LIMIT, "pages": pages, "captured_at": clock(), "complete": True}
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, objects)
