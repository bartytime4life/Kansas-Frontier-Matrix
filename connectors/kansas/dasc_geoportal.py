"""On-demand, unreleased capture of DASC's Kansas HUC12 Feature Service.

The ArcGIS transport and external candidate store are shared KFM components.
This source-specific profile does not admit the source or publish map geometry.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import re
import time
from urllib.parse import urlencode

from connectors_core.bounded_curl import BoundedCurlTransport
from connectors_core.core import ETag, RetryPolicy, TransportCategory
from connectors_core.transport import TransportProfile, TransportRequest, TransportResponse, execute_retrieval
from tools.local_data.candidate_capture import create_candidate, write_candidate

ITEM_ID = "0d15901ab05142bd8e8346bbf7ee59f7"
SERVICE = "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/WBDHU12/FeatureServer"
LAYER = f"{SERVICE}/0"
ITEM = f"https://www.arcgis.com/sharing/rest/content/items/{ITEM_ID}"
WHERE = "states LIKE '%KS%'"
FIELDS = ("FID", "huc12", "states", "name", "tohuc", "hutype", "humod")
PAGE_SIZE = 25
MAX_PAGES = 100
MAX_ROWS = 5000
MAX_PAGE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 256 * 1024 * 1024
MAX_SECONDS = 900
SERVICE_PROFILE = TransportProfile(
    profile_id="dasc-huc12-service-v1",
    allowed_hosts=frozenset({"services2.arcgis.com"}),
    allowed_media_types=frozenset({"application/json", "application/geo+json"}),
    timeout_seconds=30,
    max_response_bytes=MAX_PAGE_BYTES,
)
ITEM_PROFILE = TransportProfile(
    profile_id="dasc-huc12-item-v1",
    allowed_hosts=frozenset({"www.arcgis.com"}),
    allowed_media_types=frozenset({"application/json"}),
    timeout_seconds=30,
    max_response_bytes=1_048_576,
)


class CaptureError(ValueError):
    """Safe, bounded reason code for an incomplete capture."""


class Clock:
    def now(self):
        return datetime.now(timezone.utc)

    def monotonic(self):
        return time.monotonic()

    def sleep(self, seconds):
        time.sleep(seconds)


class ServiceTransport(BoundedCurlTransport):
    def __init__(self):
        super().__init__(SERVICE_PROFILE, path_prefix="/ZOdjAzAQ2B0f85zi/arcgis/rest/services/WBDHU12/FeatureServer/")

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        response = super().send(request, timeout_seconds=timeout_seconds,
                                max_response_bytes=max_response_bytes, allow_redirects=allow_redirects)
        # ArcGIS currently emits unquoted ETags, which are not valid HTTP entity
        # tags. Ignore an invalid tag rather than inventing a quoted value;
        # exact response bytes and ArcGIS's edit revision are checked separately.
        etag = response.headers.get("etag")
        try:
            if etag is not None:
                ETag.parse(etag)
        except ValueError:
            headers = {key: value for key, value in response.headers.items() if key != "etag"}
            return TransportResponse(response.status_code, headers, response.body_chunks,
                                     response.final_url, response.complete)
        return response


class ItemTransport(BoundedCurlTransport):
    def __init__(self):
        super().__init__(ITEM_PROFILE, path_prefix=f"/sharing/rest/content/items/{ITEM_ID}")


def _digest(body: bytes) -> str:
    return "sha256:" + sha256(body).hexdigest()


def _stamp(clock) -> str:
    return clock.now().astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _url(path: str, values: dict[str, str]) -> str:
    return path + "?" + urlencode(values)


def count_url() -> str:
    return _url(LAYER + "/query", {"where": WHERE, "returnCountOnly": "true", "f": "json"})


def page_url(offset: int) -> str:
    if type(offset) is not int or offset < 0 or offset >= MAX_ROWS or offset % PAGE_SIZE:
        raise CaptureError("PAGE_OFFSET")
    return _url(LAYER + "/query", {
        "where": WHERE, "outFields": ",".join(FIELDS), "returnGeometry": "true",
        "outSR": "4326", "orderByFields": "FID", "resultOffset": str(offset),
        "resultRecordCount": str(PAGE_SIZE), "f": "geojson",
    })


def _json(body: bytes, limit: int) -> dict:
    if not isinstance(body, bytes) or len(body) > limit:
        raise CaptureError("RESPONSE_BOUND")
    try:
        value = json.loads(body.decode("utf-8"), parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
    except (UnicodeError, ValueError, RecursionError):
        raise CaptureError("INVALID_JSON") from None
    if not isinstance(value, dict) or "error" in value:
        raise CaptureError("SERVICE_ERROR")
    return value


def parse_item(body: bytes) -> tuple[int, str]:
    value = _json(body, 1_048_576)
    if (value.get("id") != ITEM_ID or value.get("access") != "public"
            or value.get("url") != SERVICE or not isinstance(value.get("owner"), str)
            or not isinstance(value.get("licenseInfo"), str)
            or not value["licenseInfo"].strip()
            or type(value.get("modified")) is not int):
        raise CaptureError("ITEM_IDENTITY")
    return value["modified"], value["owner"]


def parse_layer(body: bytes) -> tuple[int | None, str]:
    value = _json(body, 1_048_576)
    capabilities = value.get("advancedQueryCapabilities")
    fields = value.get("fields")
    if (value.get("name") != "WBDHU12" or value.get("objectIdField") != "FID"
            or value.get("geometryType") != "esriGeometryPolygon"
            or type(value.get("maxRecordCount")) is not int
            or value["maxRecordCount"] < PAGE_SIZE
            or not isinstance(capabilities, dict)
            or capabilities.get("supportsPagination") is not True
            or capabilities.get("supportsOrderBy") is not True
            or not isinstance(fields, list)):
        raise CaptureError("LAYER_CAPABILITY")
    types = {field.get("name"): field.get("type") for field in fields if isinstance(field, dict)}
    if types.get("FID") != "esriFieldTypeOID" or types.get("huc12") != "esriFieldTypeString" or any(
            field not in types for field in FIELDS):
        raise CaptureError("LAYER_SCHEMA")
    edit = value.get("editingInfo", {})
    if not isinstance(edit, dict):
        raise CaptureError("LAYER_SCHEMA")
    revision = edit.get("dataLastEditDate")
    if revision is not None and type(revision) is not int:
        raise CaptureError("LAYER_SCHEMA")
    schema = json.dumps([(field, types[field]) for field in FIELDS], separators=(",", ":"))
    return revision, _digest(schema.encode("utf-8"))


def parse_count(body: bytes) -> int:
    count = _json(body, 1_048_576).get("count")
    if type(count) is not int or not 0 <= count <= MAX_ROWS:
        raise CaptureError("COUNT_BOUND")
    return count


def _rings(geometry: object):
    if not isinstance(geometry, dict) or geometry.get("type") not in {"Polygon", "MultiPolygon"}:
        raise CaptureError("GEOMETRY_SHAPE")
    coordinates = geometry.get("coordinates")
    polygons = [coordinates] if geometry["type"] == "Polygon" else coordinates
    if not isinstance(polygons, list) or not polygons:
        raise CaptureError("GEOMETRY_SHAPE")
    for polygon in polygons:
        if not isinstance(polygon, list) or not polygon:
            raise CaptureError("GEOMETRY_SHAPE")
        for ring in polygon:
            if not isinstance(ring, list) or len(ring) < 4 or len(ring) > 100_000:
                raise CaptureError("GEOMETRY_SHAPE")
            if ring[0] != ring[-1]:
                raise CaptureError("RING_OPEN")
            yield ring


def parse_page(body: bytes, *, expected: int, previous_id: int, seen_hucs: set[str]) -> tuple[int, set[str]]:
    value = _json(body, MAX_PAGE_BYTES)
    features = value.get("features")
    if value.get("type") != "FeatureCollection" or not isinstance(features, list) or len(features) != expected:
        raise CaptureError("PAGE_COUNT_CHANGED")
    properties = value.get("properties", {})
    if not isinstance(properties, dict) or type(properties.get("exceededTransferLimit", False)) is not bool:
        raise CaptureError("PAGE_SHAPE")
    new_hucs: set[str] = set()
    vertices = 0
    for feature in features:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise CaptureError("FEATURE_SHAPE")
        attributes = feature.get("properties")
        if not isinstance(attributes, dict) or set(attributes) != set(FIELDS):
            raise CaptureError("FEATURE_FIELDS")
        oid, huc, states = attributes.get("FID"), attributes.get("huc12"), attributes.get("states")
        if type(oid) is not int or oid <= previous_id:
            raise CaptureError("ID_ORDER")
        if not isinstance(huc, str) or not re.fullmatch(r"[0-9]{12}", huc) or huc in seen_hucs or huc in new_hucs:
            raise CaptureError("HUC_IDENTITY")
        if not isinstance(states, str) or "KS" not in re.split(r"[,;\s]+", states.upper()):
            raise CaptureError("STATE_SCOPE")
        for ring in _rings(feature.get("geometry")):
            vertices += len(ring)
            if vertices > 500_000:
                raise CaptureError("VERTEX_BOUND")
            for point in ring:
                if (not isinstance(point, list) or len(point) not in (2, 3)
                        or any(type(n) not in (int, float) or not math.isfinite(n) for n in point)
                        or not -180 <= point[0] <= 180 or not -90 <= point[1] <= 90):
                    raise CaptureError("GEOMETRY_COORDINATE")
        previous_id = oid
        new_hucs.add(huc)
    return previous_id, new_hucs


def capture(destination: Path, *, service_transport=None, item_transport=None, clock=None) -> dict:
    """Preserve source bytes in a new private directory; failure remains incomplete."""
    clock = clock or Clock()
    service_transport = service_transport or ServiceTransport()
    item_transport = item_transport or ItemTransport()
    create_candidate(destination)
    began = clock.monotonic()
    manifest = {
        "profile": "kfm.dasc-huc12-capture/v1", "source_id": "src:dasc-huc12", "item_id": ITEM_ID,
        "service": LAYER, "where": WHERE, "state": "INCOMPLETE", "reason_code": "CAPTURE_INTERRUPTED",
        "source_admission": "NOT_ADMITTED", "release_state": "UNRELEASED", "started_at": _stamp(clock),
        "finished_at": None, "count_before": None, "count_after": None, "feature_count": 0,
        "total_bytes": 0, "objects": [],
    }

    def get(url: str, transport, name: str, profile: TransportProfile) -> bytes:
        remaining = MAX_SECONDS - (clock.monotonic() - began)
        if remaining <= 0:
            raise CaptureError("CAPTURE_DEADLINE")
        result = execute_retrieval(
            transport, TransportRequest("GET", url), profile=profile,
            retry_policy=RetryPolicy(max_attempts=2, deadline_seconds=min(65, remaining)),
            clock=clock, sleeper=clock,
        )
        if result.category is not TransportCategory.SUCCESS or result.payload is None:
            raise CaptureError("UPSTREAM_UNAVAILABLE")
        body = b"".join(result.payload.chunks)
        write_candidate(destination, name, body)
        head = result.source_head
        manifest["objects"].append({
            "file": name, "url": url, "sha256": _digest(body), "bytes": len(body),
            "media_type": result.payload.media_type, "retrieved_at": _stamp(clock),
            "last_modified": head.last_modified.isoformat() if head and head.last_modified else None,
            "etag": head.etag.render() if head and head.etag else None,
        })
        manifest["total_bytes"] += len(body)
        if manifest["total_bytes"] > MAX_TOTAL_BYTES:
            raise CaptureError("TOTAL_BYTE_LIMIT")
        return body

    try:
        first_item = parse_item(get(_url(ITEM, {"f": "json"}), item_transport, "item-before.json", ITEM_PROFILE))
        first_layer = parse_layer(get(_url(LAYER, {"f": "json"}), service_transport, "layer-before.json", SERVICE_PROFILE))
        expected = parse_count(get(count_url(), service_transport, "count-before.json", SERVICE_PROFILE))
        manifest["count_before"] = expected
        if math.ceil(expected / PAGE_SIZE) > MAX_PAGES:
            raise CaptureError("PAGE_LIMIT")
        previous_id, seen_hucs = -1, set()
        for number, offset in enumerate(range(0, expected, PAGE_SIZE)):
            body = get(page_url(offset), service_transport, f"page-{number:04d}.geojson", SERVICE_PROFILE)
            previous_id, new_hucs = parse_page(body, expected=min(PAGE_SIZE, expected - offset),
                                               previous_id=previous_id, seen_hucs=seen_hucs)
            seen_hucs.update(new_hucs)
            manifest["feature_count"] += len(new_hucs)
        manifest["count_after"] = parse_count(get(count_url(), service_transport, "count-after.json", SERVICE_PROFILE))
        last_layer = parse_layer(get(_url(LAYER, {"f": "json"}), service_transport, "layer-after.json", SERVICE_PROFILE))
        last_item = parse_item(get(_url(ITEM, {"f": "json"}), item_transport, "item-after.json", ITEM_PROFILE))
        if first_item != last_item or first_layer != last_layer:
            raise CaptureError("SOURCE_REVISION_CHANGED")
        if manifest["count_after"] != expected or manifest["feature_count"] != expected:
            raise CaptureError("COUNT_CHANGED")
        manifest.update({"state": "COMPLETE_CANDIDATE", "reason_code": None,
                         "item_modified_ms": first_item[0], "item_owner": first_item[1],
                         "layer_data_edit_ms": first_layer[0], "field_schema_digest": first_layer[1]})
    except CaptureError as error:
        manifest["reason_code"] = str(error)
    manifest["finished_at"] = _stamp(clock)
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    manifest["capture_id"] = _digest(canonical)
    write_candidate(destination, "manifest.json", json.dumps(manifest, sort_keys=True, indent=2).encode("utf-8") + b"\n")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture unreleased Kansas DASC HUC12 candidate")
    parser.add_argument("destination", type=Path, help="new private directory under KFM_DATA_ROOT/data/raw or /tmp")
    args = parser.parse_args()
    result = capture(args.destination)
    print(json.dumps({key: result[key] for key in ("state", "capture_id", "feature_count", "reason_code")}, sort_keys=True))
    return 0 if result["state"] == "COMPLETE_CANDIDATE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
