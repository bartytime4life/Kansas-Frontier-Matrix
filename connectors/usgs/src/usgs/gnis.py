"""Bounded, on-demand GNIS Kansas name capture; never admits or releases records."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from tools.local_data.candidate_capture import create_candidate, write_candidate

SERVICE = "https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/3/query"
NAME = re.compile(r"[A-Za-z0-9 .-]{1,120}\Z")
MAX_BYTES = 256 * 1024
MAX_MATCHES = 20
Fetch = Callable[[str], tuple[int, bytes, str]]


def query_url(name: str) -> str:
    if not NAME.fullmatch(name) or name != name.strip() or "  " in name:
        raise ValueError("NAME_OUT_OF_SCOPE")
    params = {
        "where": f"gaz_name = '{name}' AND state_alpha = 'KS'",
        "outFields": "gaz_id,gaz_name,gaz_featureclass,state_alpha,county_name",
        "outSR": "4326",
        "resultRecordCount": str(MAX_MATCHES + 1),
        "f": "geojson",
    }
    return SERVICE + "?" + urllib.parse.urlencode(params)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def fetch(url: str) -> tuple[int, bytes, str]:
    opener = urllib.request.build_opener(NoRedirect)
    request = urllib.request.Request(url, headers={"Accept": "application/geo+json, application/json", "User-Agent": "KFM-GNIS-candidate/1.0"})
    try:
        with opener.open(request, timeout=12) as response:
            if response.status != 200:
                raise ValueError("PROVIDER_HTTP_ERROR")
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("PROVIDER_SIZE_LIMIT")
            return response.status, data, response.headers.get("Content-Type", "")
    except urllib.error.HTTPError as error:
        raise ValueError("PROVIDER_HTTP_ERROR") from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise ValueError("PROVIDER_UNAVAILABLE") from error


def parse(body: bytes, name: str) -> tuple[str, list[dict]]:
    if not body or len(body) > MAX_BYTES:
        raise ValueError("PROVIDER_SIZE_LIMIT")
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise ValueError("PROVIDER_JSON_INVALID") from error
    if not isinstance(payload, dict) or "error" in payload or payload.get("type") != "FeatureCollection" or not isinstance(payload.get("features"), list):
        raise ValueError("PROVIDER_RESPONSE_INVALID")
    if payload.get("exceededTransferLimit") or len(payload["features"]) > MAX_MATCHES:
        raise ValueError("PROVIDER_TRUNCATED")
    seen: set[int] = set()
    records: list[dict] = []
    for feature in payload["features"]:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise ValueError("FEATURE_INVALID")
        attrs, geometry = feature.get("properties"), feature.get("geometry")
        if not isinstance(attrs, dict) or attrs.get("state_alpha") != "KS" or attrs.get("gaz_name") != name or attrs.get("gaz_featureclass") != "Populated Place":
            raise ValueError("FEATURE_SCOPE")
        identifier = attrs.get("gaz_id")
        if not isinstance(identifier, int) or isinstance(identifier, bool) or identifier <= 0 or identifier in seen:
            raise ValueError("FEATURE_ID_INVALID")
        seen.add(identifier)
        if not isinstance(geometry, dict) or geometry.get("type") not in ("Point", "MultiPoint"):
            raise ValueError("GEOMETRY_INVALID")
        coordinates = geometry.get("coordinates")
        points = [coordinates] if geometry["type"] == "Point" else coordinates
        if not isinstance(points, list) or not points or len(points) > 50:
            raise ValueError("GEOMETRY_INVALID")
        for point in points:
            if not isinstance(point, list) or len(point) not in (2, 3) or any(not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) for v in point):
                raise ValueError("GEOMETRY_INVALID")
            lon, lat = point[:2]
            if not (-102.2 <= lon <= -94.4 and 36.8 <= lat <= 40.2):
                raise ValueError("GEOMETRY_OUTSIDE_KANSAS_WINDOW")
        records.append({"feature_id": identifier, "name": name, "feature_class": attrs["gaz_featureclass"], "state": "KS", "county": attrs.get("county_name"), "geometry_role": "GNIS representative location; not a place boundary", "geometry": geometry})
    return ("EMPTY" if not records else "CANDIDATE" if len(records) == 1 else "AMBIGUOUS_HOLD"), records


def capture(name: str, directory: Path, transport: Fetch = fetch, now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)) -> dict:
    url = query_url(name)
    create_candidate(directory)
    retrieved_at = now().astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    status = "INCOMPLETE"
    records: list[dict] = []
    reason: str | None = None
    body = b""
    content_type = ""
    http_status: int | None = None
    try:
        http_status, body, content_type = transport(url)
        if http_status != 200:
            raise ValueError("PROVIDER_HTTP_ERROR")
        if len(body) > MAX_BYTES:
            raise ValueError("PROVIDER_SIZE_LIMIT")
        write_candidate(directory, "source.geojson", body)
        status, records = parse(body, name)
    except ValueError as error:
        reason = str(error)
    manifest = {
        "profile": "kfm.gnis-kansas-name-capture/v1", "source": SERVICE, "request_url": url,
        "requested_name": name, "retrieved_at": retrieved_at, "http_status": http_status,
        "content_type": content_type, "source_bytes": len(body),
        "source_sha256": "sha256:" + hashlib.sha256(body).hexdigest() if body else None,
        "state": status, "reason_code": reason, "records": records,
        "source_admission": "PENDING", "rights_review": "PENDING", "sensitivity_review": "PENDING",
        "release_state": "UNRELEASED",
    }
    write_candidate(directory, "manifest.json", (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    manifest = capture(args.name, args.output)
    print(json.dumps({"state": manifest["state"], "reason_code": manifest["reason_code"], "record_count": len(manifest["records"]), "source_sha256": manifest["source_sha256"]}))


if __name__ == "__main__":
    main()
