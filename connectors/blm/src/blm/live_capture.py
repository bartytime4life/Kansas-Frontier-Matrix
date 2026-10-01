"""Bounded live BLM PLSS capture into a new, unreleased candidate directory.

This connector preserves provider bytes and validation receipts. It neither admits a
source nor prepares public map tiles; a complete capture is still review-required.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time

from connectors_core.bounded_curl import BoundedCurlTransport
from connectors_core.core import RetryPolicy, TransportCategory
from connectors_core.transport import TransportProfile, TransportRequest, execute_retrieval

from . import plss_cadnsdi as plss

MAX_PAGE_BYTES = 32 * 1024 * 1024
MAX_TOTAL_BYTES = 2 * 1024 * 1024 * 1024
MAX_PAGES = 180
MAX_SECONDS = 1800
PROFILE = TransportProfile(
    profile_id="blm-plss-live-capture-v1", allowed_hosts=frozenset({"gis.blm.gov"}),
    allowed_media_types=frozenset({"application/json", "application/geo+json"}),
    timeout_seconds=35, max_response_bytes=MAX_PAGE_BYTES,
)


class SystemClock:
    def now(self):
        return datetime.now(timezone.utc)

    def monotonic(self):
        return time.monotonic()

    def sleep(self, seconds):
        time.sleep(seconds)


class LiveTransport(BoundedCurlTransport):
    def __init__(self):
        super().__init__(PROFILE, path_prefix=f"{plss.SERVICE}/")


@dataclass(frozen=True)
class CaptureResult:
    directory: Path
    manifest: dict


def _stamp(clock) -> str:
    return clock.now().astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _digest(body: bytes) -> str:
    return "sha256:" + sha256(body).hexdigest()


def _write_new(path: Path, body: bytes) -> None:
    with path.open("xb") as target:
        target.write(body)
        target.flush()


def capture(layer: str, destination: Path, *, transport=None, clock=None) -> CaptureResult:
    """Capture a whole Kansas layer or leave an explicit incomplete candidate.

    The destination must not already exist. Count before and after, strict page order,
    unique provider IDs, page digests, byte/deadline limits, and parser checks prevent
    an interrupted or drifting run from masquerading as complete.
    """
    plss.count_url(layer)
    if not isinstance(destination, Path):
        raise ValueError("DESTINATION_PATH")
    clock = clock or SystemClock()
    transport = transport or LiveTransport()
    destination.mkdir(mode=0o700, parents=False, exist_ok=False)
    began = clock.monotonic()
    manifest = {
        "profile": "kfm.blm-plss-capture/v1", "source_id": "blm.plss-cadnsdi",
        "service": f"{plss.HOST}{plss.SERVICE}", "layer": layer,
        "state": "INCOMPLETE", "source_admission": "PENDING", "release_state": "UNRELEASED",
        "started_at": _stamp(clock), "finished_at": None, "count_before": None,
        "count_after": None, "feature_count": 0, "total_bytes": 0, "pages": [],
        "reason_code": "CAPTURE_INTERRUPTED",
    }

    def get(url: str) -> bytes:
        remaining = MAX_SECONDS - (clock.monotonic() - began)
        if remaining <= 0:
            raise ValueError("CAPTURE_DEADLINE")
        result = execute_retrieval(
            transport, TransportRequest("GET", url), profile=PROFILE,
            retry_policy=RetryPolicy(max_attempts=2, deadline_seconds=min(70, remaining)),
            clock=clock, sleeper=clock,
        )
        if result.category is not TransportCategory.SUCCESS or result.payload is None:
            raise ValueError("UPSTREAM_UNAVAILABLE")
        return b"".join(result.payload.chunks)

    try:
        count_body = get(plss.count_url(layer))
        _write_new(destination / "count-before.json", count_body)
        expected = plss.parse_count(count_body, status=200, layer=layer)
        manifest["count_before"] = expected
        if expected > plss.MAX_PAGE * MAX_PAGES:
            raise ValueError("PAGE_LIMIT")
        previous_id = -1
        for page_number, offset in enumerate(range(0, expected, plss.MAX_PAGE)):
            if page_number >= MAX_PAGES:
                raise ValueError("PAGE_LIMIT")
            url = plss.query_url(layer, offset=offset)
            body = get(url)
            name = f"page-{page_number:04d}.geojson"
            _write_new(destination / name, body)
            manifest["total_bytes"] += len(body)
            manifest["pages"].append({"file": name, "url": url, "sha256": _digest(body),
                                      "bytes": len(body), "retrieved_at": _stamp(clock),
                                      "offset": offset})
            if manifest["total_bytes"] > MAX_TOTAL_BYTES:
                raise ValueError("TOTAL_BYTE_LIMIT")
            parsed = plss.parse_page(body, status=200, source_url=url, retrieved_at=_stamp(clock),
                                     max_bytes=MAX_PAGE_BYTES)
            if len(parsed.features) != min(plss.MAX_PAGE, expected - offset):
                raise ValueError("PAGE_COUNT_CHANGED")
            if any(feature.route != "RAW_CANDIDATE" for feature in parsed.features):
                raise ValueError("QUARANTINED_GEOMETRY")
            if parsed.features and parsed.features[0].object_id <= previous_id:
                raise ValueError("PAGE_ID_ORDER")
            if parsed.features:
                previous_id = parsed.features[-1].object_id
            manifest["feature_count"] += len(parsed.features)
        after_body = get(plss.count_url(layer))
        _write_new(destination / "count-after.json", after_body)
        manifest["count_after"] = plss.parse_count(after_body, status=200, layer=layer)
        if manifest["feature_count"] != expected or manifest["count_after"] != expected:
            raise ValueError("COUNT_CHANGED")
        manifest["state"], manifest["reason_code"] = "COMPLETE_CANDIDATE", None
    except (ValueError, plss.PlssInputError) as error:
        allowed = {"CAPTURE_DEADLINE", "UPSTREAM_UNAVAILABLE", "PAGE_LIMIT", "TOTAL_BYTE_LIMIT",
                   "PAGE_COUNT_CHANGED", "QUARANTINED_GEOMETRY", "PAGE_ID_ORDER", "COUNT_CHANGED",
                   "DUPLICATE_IDENTIFIER", "SERVICE_ERROR", "STATE_SCOPE", "FEATURE_SHAPE",
                   "COLLECTION_SHAPE", "OBJECT_ID_ORDER", "IDENTIFIER", "RESPONSE_BOUND"}
        manifest["reason_code"] = str(error) if str(error) in allowed else "PROVIDER_RESPONSE_INVALID"
    manifest["finished_at"] = _stamp(clock)
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    manifest["capture_id"] = _digest(canonical)
    _write_new(destination / "manifest.json", json.dumps(manifest, sort_keys=True, indent=2).encode("utf-8") + b"\n")
    return CaptureResult(destination, manifest)


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture an unreleased Kansas BLM PLSS layer")
    parser.add_argument("layer", choices=tuple(plss.LAYERS))
    parser.add_argument("destination", type=Path, help="new directory outside the repository")
    args = parser.parse_args()
    result = capture(args.layer, args.destination)
    print(json.dumps({"state": result.manifest["state"], "capture_id": result.manifest["capture_id"],
                      "feature_count": result.manifest["feature_count"],
                      "reason_code": result.manifest["reason_code"]}, sort_keys=True))
    return 0 if result.manifest["state"] == "COMPLETE_CANDIDATE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
