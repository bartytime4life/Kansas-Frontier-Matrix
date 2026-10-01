"""Bounded, unreleased Kansas Crop-CASMA 1 km WCS capture.

The provider's numeric EPSG:5070 GeoTIFF is preserved byte-for-byte. Map reprojection
and colorization belong to the soil pipeline, not this source connector.
"""
from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPRedirectHandler, Request
from xml.etree import ElementTree
import argparse
import json
import re
from tools.local_data.candidate_capture import create_candidate, write_candidate

BASE = "https://cloud.csiss.gmu.edu/smap_server/cgi-bin/mapserv"
KANSAS_BOUNDS_5070 = (-534000, 1549000, 125000, 1904000)
MAX_CAPABILITIES = 2_000_000
MAX_COVERAGE = 16_000_000
DAY = re.compile(r"20\d{2}-\d{2}-\d{2}\Z")


class CaptureError(ValueError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise CaptureError("REDIRECT_REJECTED")


def layer_name(day: str) -> str:
    if not DAY.fullmatch(day):
        raise CaptureError("DAY_INVALID")
    try:
        parsed = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        raise CaptureError("DAY_INVALID") from None
    if parsed > datetime.now(timezone.utc):
        raise CaptureError("DAY_IN_FUTURE")
    return f"SMAP-HYB-1KM-DAILY_{day[:4]}.{day[5:7]}.{day[8:]}_PM"


def request_urls(day: str) -> tuple[str, str]:
    name = layer_name(day)
    common = [("SERVICE", "WCS"), ("VERSION", "2.0.1"), ("MAP", f"/WMS/SMAP-HYB-1KM-DAILY_{day[:4]}.map")]
    capabilities = BASE + "?" + urlencode(common + [("REQUEST", "GetCapabilities")])
    west, south, east, north = KANSAS_BOUNDS_5070
    coverage = BASE + "?" + urlencode(common + [("REQUEST", "GetCoverage"), ("COVERAGEID", name),
        ("FORMAT", "image/tiff"), ("SUBSET", f"x({west},{east})"), ("SUBSET", f"y({south},{north})"),
        ("SUBSETTINGCRS", "http://www.opengis.net/def/crs/EPSG/0/5070")])
    return capabilities, coverage


def advertised(xml: bytes, day: str) -> bool:
    name = layer_name(day)
    if len(xml) > MAX_CAPABILITIES:
        raise CaptureError("CAPABILITIES_TOO_LARGE")
    try:
        root = ElementTree.fromstring(xml)
    except ElementTree.ParseError:
        raise CaptureError("CAPABILITIES_INVALID") from None
    return any(node.text == name for node in root.iter() if node.tag.endswith("CoverageId"))


def bounded_fetch(url: str, media: str, limit: int) -> bytes:
    opener = build_opener(NoRedirect)
    try:
        with opener.open(Request(url, headers={"Accept": media}), timeout=30) as response:
            if response.status != 200 or response.headers.get_content_type() != media:
                raise CaptureError("PROVIDER_RESPONSE_INVALID")
            length = response.headers.get("Content-Length")
            if length and (not length.isdecimal() or int(length) > limit):
                raise CaptureError("RESPONSE_TOO_LARGE")
            body = response.read(limit + 1)
    except CaptureError:
        raise
    except Exception:
        raise CaptureError("PROVIDER_UNAVAILABLE") from None
    if not body or len(body) > limit:
        raise CaptureError("RESPONSE_TOO_LARGE")
    return body


def capture(day: str, destination: Path) -> dict:
    capabilities_url, coverage_url = request_urls(day)
    create_candidate(destination)
    manifest = {"profile": "kfm.crop-casma-capture/v1", "day": day, "layer": layer_name(day),
        "state": "HOLD", "release_state": "UNRELEASED", "source_id": "usda-nass-crop-casma-1km",
        "bounds_5070": KANSAS_BOUNDS_5070, "capabilities_url": capabilities_url,
        "coverage_url": coverage_url, "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")}
    try:
        capabilities = bounded_fetch(capabilities_url, "text/xml", MAX_CAPABILITIES)
        write_candidate(destination, "capabilities.xml", capabilities)
        manifest["capabilities_sha256"] = "sha256:" + sha256(capabilities).hexdigest()
        if not advertised(capabilities, day):
            raise CaptureError("DAY_NOT_ADVERTISED")
        coverage = bounded_fetch(coverage_url, "image/tiff", MAX_COVERAGE)
        write_candidate(destination, "source.tif", coverage)
        manifest["source_sha256"] = "sha256:" + sha256(coverage).hexdigest()
        if coverage[:4] not in (b"II*\x00", b"MM\x00*"):
            raise CaptureError("NOT_TIFF")
        manifest["state"] = "CAPTURED_CANDIDATE"
        manifest["reason_code"] = None
    except CaptureError as error:
        manifest["reason_code"] = str(error)
    write_candidate(destination, "manifest.json", (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="exact UTC day advertised by the provider")
    parser.add_argument("destination", type=Path, help="new external candidate directory")
    args = parser.parse_args()
    manifest = capture(args.day, args.destination)
    print(json.dumps({key: manifest.get(key) for key in ("state", "day", "source_sha256", "reason_code")}, sort_keys=True))
    return 0 if manifest["state"] == "CAPTURED_CANDIDATE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
