"""Bounded public S3 capture of NOAA monthly normals; no admission or publication."""
from __future__ import annotations

from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .climate_normals import INVENTORY_KEY, NormalsError, object_url, parse_inventory, station_key

MAX_STATION_BYTES = 128 * 1024
MAX_INVENTORY_BYTES = 2 * 1024 * 1024
MAX_TOTAL_BYTES = 32 * 1024 * 1024
MAX_STATIONS = 1000
MAX_WORKERS = 8
MAX_DURATION_SECONDS = 240


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, file_pointer, code, message, headers, new_url):
        return None


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _digest(raw: bytes) -> str:
    return "sha256:" + sha256(raw).hexdigest()


def canonical_bytes(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()


def fetch_object(key: str, limit: int) -> tuple[bytes, dict]:
    """Fetch only a planner-created key; error bodies and redirects are rejected."""
    url = object_url(key)
    opener = build_opener(_NoRedirect)
    for attempt in range(2):
        try:
            with opener.open(Request(url, headers={"Accept-Encoding": "identity"}), timeout=15) as response:
                if response.status != 200 or response.geturl() != url:
                    raise NormalsError("PROVIDER_STATUS_OR_REDIRECT")
                media = response.headers.get_content_type()
                if media not in {"application/octet-stream", "text/plain", "text/csv"}:
                    raise NormalsError("PROVIDER_MEDIA_TYPE")
                declared = response.headers.get("Content-Length")
                if declared and (not declared.isdigit() or int(declared) > limit):
                    raise NormalsError("PROVIDER_SIZE")
                raw = response.read(limit + 1)
                if not raw or len(raw) > limit or (declared and len(raw) != int(declared)):
                    raise NormalsError("PROVIDER_SIZE")
                if raw.startswith((b"<?xml", b"<html", b"<!DOCTYPE")):
                    raise NormalsError("PROVIDER_ERROR_BODY")
                return raw, {"retrieved_at": _utc(), "etag": response.headers.get("ETag"),
                             "last_modified": response.headers.get("Last-Modified"),
                             "media_type": media, "status": response.status}
        except (HTTPError, URLError, TimeoutError, OSError):
            if attempt == 0:
                time.sleep(0.2)
    raise NormalsError("PROVIDER_UNAVAILABLE") from None


@dataclass(frozen=True)
class Capture:
    manifest: dict
    objects: dict[str, bytes]


def capture(*, fetcher=fetch_object) -> Capture:
    """Capture all Kansas stations in NOAA inventory or mark the result incomplete."""
    started = time.monotonic()
    inventory, metadata = fetcher(INVENTORY_KEY, MAX_INVENTORY_BYTES)
    if len(inventory) > MAX_INVENTORY_BYTES or len(inventory) > MAX_TOTAL_BYTES:
        raise NormalsError("CAPTURE_BYTE_LIMIT")
    stations = parse_inventory(inventory)
    if len(stations) > MAX_STATIONS:
        raise NormalsError("STATION_LIMIT")
    inventory_hash = _digest(inventory)
    objects = {inventory_hash: inventory}
    entries, failures = [], []
    acquired_bytes = len(inventory)
    def bounded_fetch(key, limit):
        if time.monotonic() - started >= MAX_DURATION_SECONDS:
            raise NormalsError("CAPTURE_DEADLINE")
        return fetcher(key, limit)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        pending = {}
        remaining = iter(stations)
        def submit_available():
            while len(pending) < MAX_WORKERS:
                available = MAX_TOTAL_BYTES - acquired_bytes - sum(reserved for _, reserved in pending.values())
                # Wait for in-flight reservations to settle before reducing a station's limit.
                if available < 2 or (pending and available < MAX_STATION_BYTES + 1):
                    return
                try:
                    station = next(remaining)
                except StopIteration:
                    return
                reserved = min(MAX_STATION_BYTES + 1, available)
                future = pool.submit(bounded_fetch, station_key(station["station_id"]), reserved - 1)
                pending[future] = (station, reserved)
        submit_available()
        while pending:
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                station, reserved = pending.pop(future)
                key = station_key(station["station_id"])
                try:
                    raw, head = future.result()
                    if not raw or len(raw) >= reserved:
                        raise NormalsError("CAPTURE_BYTE_LIMIT" if reserved < MAX_STATION_BYTES + 1
                                           else "PROVIDER_SIZE")
                    acquired_bytes += len(raw)
                    digest = _digest(raw)
                    objects[digest] = raw
                    entries.append({"station_id": station["station_id"], "key": key,
                                    "sha256": digest, "bytes": len(raw), **head})
                except NormalsError as exc:
                    if reserved < MAX_STATION_BYTES + 1 and str(exc) in {"PROVIDER_SIZE", "CAPTURE_BYTE_LIMIT"}:
                        raise NormalsError("CAPTURE_BYTE_LIMIT") from None
                    failures.append(station["station_id"])
                except (OSError, ValueError):
                    failures.append(station["station_id"])
            submit_available()
        if len(entries) + len(failures) < len(stations):
            raise NormalsError("CAPTURE_BYTE_LIMIT")
    entries.sort(key=lambda item: item["station_id"])
    complete = not failures and len(entries) == len(stations) and time.monotonic() - started <= MAX_DURATION_SECONDS
    manifest = {"profile": "kfm.noaa-monthly-normals-capture/v1", "source_id": "noaa-ncei-climate-normals",
                "period": "1991-2020", "product": "normals-monthly", "state": "KS",
                "captured_at": _utc(), "inventory": {"key": INVENTORY_KEY, "sha256": inventory_hash,
                                                    "bytes": len(inventory), **metadata},
                "expected_stations": len(stations), "captured_stations": len(entries),
                "failed_station_ids": sorted(failures), "complete": complete,
                "reason_code": None if complete else "CAPTURE_INCOMPLETE",
                "station_objects": entries, "source_admission": "PENDING",
                "release_state": "UNRELEASED"}
    manifest["capture_id"] = _digest(canonical_bytes(manifest))
    return Capture(manifest, objects)
