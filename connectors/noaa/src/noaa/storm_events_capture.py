"""Bounded NCEI Storm Events capture for one data year of the Kansas pilot.

Fetches the NCEI ``csvfiles/`` directory listing and the newest details file
it lists for the requested data year (NCEI reissues files under new ``_c``
creation dates, so the name is read from the listing, never guessed), through
a host-locked, size-bounded fetch that follows no redirects. Returns their
exact bytes with a digest-closed manifest. It parses, selects and admits
nothing: normalization and release are separate steps. The fatalities and
locations files are never fetched.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
import time
from urllib.request import HTTPRedirectHandler, Request, build_opener

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import storm_events

PROFILE = "kfm.storm-events-pilot-capture/v1"
SOURCE_ID = "noaa-storm-events"
STATE_FIPS = storm_events.KANSAS_FIPS
LISTING_KEY = "listing"
LISTING_URL = storm_events.HOST + storm_events.DIRECTORY
LISTING_BYTES = 512 * 1024
DETAILS_BYTES = 64 * 1024 * 1024
# Storm Events records every event type from 1996 onward.
FIRST_YEAR = 1996
HREF = re.compile(r'href="([^"]+)"')


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


def object_url(key: str) -> str:
    if key == LISTING_KEY:
        return LISTING_URL
    if not isinstance(key, str) or not storm_events.FILE_NAME.fullmatch(key):
        raise ValueError("SOURCE_KEY_NOT_ALLOWED")
    return LISTING_URL + key


def object_limit(key: str) -> int:
    return LISTING_BYTES if key == LISTING_KEY else DETAILS_BYTES


def latest_details(listing: bytes, year: int) -> str:
    """The details file name with the newest creation date for ``year`` in an NCEI listing."""
    data_year(year)
    try:
        text = listing.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("LISTING_ENCODING") from None
    best = None
    for name in sorted(set(HREF.findall(text))):
        match = storm_events.FILE_NAME.fullmatch(name)
        if not match or int(match.group(1)) != year:
            continue
        created = match.group(2)
        try:
            created_year = datetime.strptime(created, "%Y%m%d").year
        except ValueError:
            raise ValueError("LISTING_CREATION_DATE_INVALID") from None
        if created_year < year:
            raise ValueError("LISTING_CREATION_DATE_INVALID")
        if best is None or created > best[0]:
            best = (created, name)
    if best is None:
        raise ValueError("DATA_YEAR_NOT_LISTED")
    return best[1]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(key: str, limit: int):
    """One bounded, host-locked GET with no redirects; returns (bytes, metadata)."""
    url = object_url(key)
    if not 0 < limit <= object_limit(key):
        raise ValueError("SOURCE_LIMIT_INVALID")
    start = time.monotonic()
    with build_opener(NoRedirect).open(Request(url, headers={
            "Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas storm events capture"}), timeout=60) as response:
        if response.status != 200 or response.geturl() != url:
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
        if count == 0 or (declared is not None and count != int(declared)):
            raise ValueError("SOURCE_SIZE_MISMATCH")
        return b"".join(chunks), {"source_url": url, "retrieved_at": utc_now(),
                                   "last_modified": response.headers.get("Last-Modified"),
                                   "etag": response.headers.get("ETag")}


def _page(key: str, fetcher) -> tuple[dict, bytes]:
    try:
        raw, meta = fetcher(key, object_limit(key))
    except (OSError, ValueError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) and str(exc).isupper() else "SOURCE_FETCH_FAILED"
        raise ValueError(reason) from None
    if not isinstance(raw, bytes) or not 0 < len(raw) <= object_limit(key):
        raise ValueError("SOURCE_SIZE_LIMIT")
    if not isinstance(meta, dict) or meta.get("source_url") != object_url(key):
        raise ValueError("SOURCE_RESPONSE_INVALID")
    return ({"key": key, "url": meta["source_url"], "sha256": digest_bytes(raw), "bytes": len(raw),
             "retrieved_at": meta.get("retrieved_at"), "last_modified": meta.get("last_modified"),
             "etag": meta.get("etag")}, raw)


def capture(year: int, *, fetcher=fetch, clock=utc_now) -> Capture:
    """Fetch the listing and the year's newest details file, or raise; never a partial capture."""
    data_year(year)
    if year > int(clock()[:4]):
        raise ValueError("DATA_YEAR_IN_FUTURE")
    listing_page, listing = _page(LISTING_KEY, fetcher)
    details_page, details = _page(latest_details(listing, year), fetcher)
    manifest = {"profile": PROFILE, "source_id": SOURCE_ID, "state_fips": STATE_FIPS, "data_year": year,
                "pages": [listing_page, details_page], "captured_at": clock(), "complete": True}
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, {listing_page["sha256"]: listing, details_page["sha256"]: details})
