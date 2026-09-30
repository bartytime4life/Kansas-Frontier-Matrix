"""Bounded USGS v1 pilot acquisition. Preserves bytes; never normalizes or admits.

The only live destination is api.waterdata.usgs.gov. Curl supplies a total
request deadline, including DNS and slow response bodies; the shared connector
executor owns retries and response classification. No shell or redirects.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import shutil
import subprocess
import tempfile
import time
from urllib.parse import parse_qs, urlencode, urlsplit

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors_core.core import RetryPolicy, TransportCategory
from connectors_core.transport import (
    TransportProfile, TransportRequest, TransportResponse, execute_retrieval,
)

BASE = "https://api.waterdata.usgs.gov/ogcapi/v1/collections"
SOURCE_PROFILE = json.loads((Path(__file__).resolve().parents[3] / "configs/domains/hydrology/usgs-water-pilot.json").read_text())
if (SOURCE_PROFILE["profile"] != "kfm.usgs-water-pilot/v1"
        or SOURCE_PROFILE["station_ids"] != ["USGS-06892518", "USGS-07156900"]
        or SOURCE_PROFILE["parameter_code"] != "00060"
        or SOURCE_PROFILE["max_interval_seconds"] != 86400
        or SOURCE_PROFILE["stale_after_seconds"] != 7200):
    raise ValueError("UNSUPPORTED_SOURCE_PROFILE")
STATIONS = tuple(SOURCE_PROFILE["station_ids"])
STALE_AFTER_SECONDS = SOURCE_PROFILE["stale_after_seconds"]
MAX_PAGE_BYTES = 2 * 1024 * 1024
MAX_TOTAL_BYTES = 8 * 1024 * 1024
MAX_PAGES = 12
MAX_FEATURES = 4000
CAPTURE_DEADLINE_SECONDS = 180
PROFILE = TransportProfile(
    profile_id="usgs-water-pilot-v1", allowed_hosts=frozenset({"api.waterdata.usgs.gov"}),
    allowed_media_types=frozenset({"application/json", "application/geo+json"}),
    timeout_seconds=25, max_response_bytes=MAX_PAGE_BYTES,
)


class SystemClock:
    def now(self):
        return datetime.now(timezone.utc)

    def monotonic(self):
        return time.monotonic()

    def sleep(self, seconds):
        time.sleep(seconds)


class CurlTransport:
    """A fixed-host implementation of the existing caller-owned transport."""

    def __init__(self):
        self.executable = shutil.which("curl")
        if not self.executable:
            raise ValueError("CURL_UNAVAILABLE")

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        PROFILE.validate_request(request)
        if allow_redirects or request.method.value != "GET" or request.headers:
            raise ValueError("UNSUPPORTED_TRANSPORT_REQUEST")
        parsed = urlsplit(request.url)
        if not parsed.path.startswith("/ogcapi/v1/collections/"):
            raise ValueError("UNSUPPORTED_PROVIDER_PATH")
        with tempfile.TemporaryDirectory(prefix="kfm-usgs-") as directory:
            payload = Path(directory) / "body"
            headers = Path(directory) / "headers"
            command = [
                self.executable, "--disable", "--silent", "--show-error",
                "--proto", "=https", "--max-redirs", "0", "--max-time", str(timeout_seconds),
                "--connect-timeout", str(min(5, timeout_seconds)),
                "--max-filesize", str(max_response_bytes), "--header", "Accept: application/geo+json",
                "--header", "Accept-Encoding: identity", "--output", str(payload),
                "--dump-header", str(headers), "--write-out", "%{http_code}", "--url", request.url,
            ]
            try:
                result = subprocess.run(command, capture_output=True, timeout=timeout_seconds + 1, check=False)
            except subprocess.TimeoutExpired as exc:
                raise TimeoutError("REQUEST_DEADLINE") from exc
            if result.returncode == 28:
                raise TimeoutError("REQUEST_DEADLINE")
            if result.returncode:
                # Never expose provider body, URL, or subprocess stderr in errors.
                raise OSError("PROVIDER_TRANSPORT_FAILED")
            if not payload.is_file() or payload.stat().st_size > max_response_bytes:
                raise ValueError("RESPONSE_BYTE_LIMIT")
            if not headers.is_file() or headers.stat().st_size > 65536:
                raise ValueError("RESPONSE_HEADER_LIMIT")
            safe = {}
            for line in headers.read_text(encoding="iso-8859-1").splitlines():
                if line.startswith("HTTP/"):
                    safe = {}
                if ":" in line:
                    key, value = line.split(":", 1)
                    if key.lower() in {"content-type", "content-length", "etag", "last-modified", "retry-after", "date"}:
                        safe[key.lower()] = value.strip()
            return TransportResponse(int(result.stdout), safe, (payload.read_bytes(),), request.url)


def request_plan(start: str, end: str) -> list[dict]:
    start_time, end_time = utc_time(start), utc_time(end)
    if not 0 < (end_time - start_time).total_seconds() <= SOURCE_PROFILE["max_interval_seconds"]:
        raise ValueError("PILOT_INTERVAL_MUST_BE_AT_MOST_24_HOURS")
    requests = []
    for station in STATIONS:
        for collection in ("monitoring-locations", "continuous"):
            scope = {"f": "json", "limit": "1000"}
            if collection == "monitoring-locations":
                scope["monitoring_location_number"] = station.removeprefix("USGS-")
                scope["agency_code"] = "USGS"
            else:
                scope.update(monitoring_location_id=station, parameter_code="00060",
                             datetime=f"{timestamp(start_time)}/{timestamp(end_time)}")
            requests.append({"station_id": station, "collection": collection,
                             "query": scope, "url": f"{BASE}/{collection}/items?{urlencode(scope)}"})
    return requests


def safe_page_url(url: str, request: dict) -> None:
    if not isinstance(url, str) or len(url) > 2048:
        raise ValueError("UNSAFE_NEXT_LINK")
    parts = urlsplit(url)
    if (parts.scheme != "https" or parts.netloc != "api.waterdata.usgs.gov"
            or parts.fragment or parts.path != f"/ogcapi/v1/collections/{request['collection']}/items"):
        raise ValueError("UNSAFE_NEXT_LINK")
    query = parse_qs(parts.query, keep_blank_values=True, max_num_fields=16)
    if set(query) - (set(request["query"]) | {"offset"}):
        raise ValueError("NEXT_LINK_SCOPE_CHANGED")
    if any(query.get(key) != [value] for key, value in request["query"].items()):
        raise ValueError("NEXT_LINK_SCOPE_CHANGED")
    if "offset" in query and (len(query["offset"]) != 1 or not query["offset"][0].isdigit()):
        raise ValueError("UNSAFE_NEXT_OFFSET")


@dataclass
class Capture:
    manifest: dict
    objects: dict[str, bytes]


def capture(start: str, end: str, *, transport=None, clock=None) -> Capture:
    """Return a complete or quarantinable capture, retaining every successful page."""
    plan = request_plan(start, end)
    clock = clock or SystemClock()
    transport = transport or CurlTransport()
    began = clock.monotonic()
    pages, objects, attempts = [], {}, []
    byte_count = 0
    reason = None
    try:
        for request in plan:
            url = request["url"]
            seen = set()
            while url:
                if url in seen or len(pages) >= MAX_PAGES:
                    raise ValueError("PAGINATION_LIMIT")
                seen.add(url)
                safe_page_url(url, request)
                remaining = CAPTURE_DEADLINE_SECONDS - (clock.monotonic() - began)
                if remaining <= 0:
                    raise ValueError("CAPTURE_DEADLINE")
                result = execute_retrieval(
                    transport, TransportRequest("GET", url), profile=PROFILE,
                    retry_policy=RetryPolicy(max_attempts=2, deadline_seconds=min(50, remaining)),
                    clock=clock, sleeper=clock,
                )
                attempts.extend({"station_id": request["station_id"], "collection": request["collection"],
                                 "number": item.attempt_number, "outcome": item.category.value,
                                 "code": item.code, "status": item.status_code,
                                 "observed_at": timestamp(item.observed_at)}
                                for item in result.attempts)
                if result.category is not TransportCategory.SUCCESS or result.payload is None:
                    raise ValueError("ACQUISITION_" + result.category.value)
                raw = b"".join(result.payload.chunks)
                digest = digest_bytes(raw)
                # Preserve successful transport bytes even when parsing subsequently fails.
                objects[digest] = raw
                byte_count += len(raw)
                page = {"station_id": request["station_id"], "collection": request["collection"],
                        "url": url, "sha256": digest, "bytes": len(raw),
                        "retrieved_at": timestamp(clock.now()), "media_type": result.payload.media_type,
                        "response_metadata": {
                            "etag": ({"opaque": result.source_head.etag.opaque,
                                      "weak": result.source_head.etag.weak}
                                     if result.source_head.etag else None),
                            "last_modified": (timestamp(result.source_head.last_modified)
                                              if result.source_head.last_modified else None),
                            "content_length": result.source_head.content_length,
                            "status": result.attempts[-1].status_code,
                        }}
                pages.append(page)
                if byte_count > MAX_TOTAL_BYTES:
                    raise ValueError("CAPTURE_BYTE_LIMIT")
                value = decode_object(raw, limit=MAX_PAGE_BYTES)
                if (value.get("type") != "FeatureCollection" or not isinstance(value.get("features"), list)
                        or len(value["features"]) > MAX_FEATURES or not isinstance(value.get("links"), list)
                        or len(value["links"]) > 100):
                    raise ValueError("INVALID_FEATURE_COLLECTION")
                links = [link for link in value["links"] if isinstance(link, dict) and link.get("rel") == "next"]
                if len(links) > 1:
                    raise ValueError("AMBIGUOUS_PAGINATION")
                url = links[0].get("href") if links else None
                if links and not url:
                    raise ValueError("UNSAFE_NEXT_LINK")
    except (ValueError, OSError, TypeError, AttributeError):
        # Known safe reasons only; raw exception text can contain upstream content.
        reason = "ACQUISITION_INCOMPLETE"
    manifest = {
        "profile": "kfm.usgs-water-pilot-capture/v1", "source_id": "usgs-nwis",
        "parameter_code": "00060", "station_ids": list(STATIONS),
        "start": timestamp(utc_time(start)), "end": timestamp(utc_time(end)),
        "captured_at": timestamp(clock.now()), "complete": reason is None,
        "reason_code": reason, "pages": pages, "attempts": attempts,
        "source_admission": "PENDING", "release_state": "UNRELEASED",
    }
    manifest["capture_id"] = digest_bytes(canonical_bytes(manifest))
    return Capture(manifest, objects)
