"""Select and stream one exact Kansas topoView GeoTIFF from the official TNM API.

The worker owns RAW persistence; this connector never publishes a map or
accepts a client-supplied download URL.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from collections.abc import Callable
from urllib.parse import urlencode, urlparse
from urllib.request import Request, build_opener, HTTPRedirectHandler

TNM_API = "https://tnmaccess.nationalmap.gov/api/v1/products"
MAX_CAPTURE_BYTES = 500_000_000
MAX_CATALOG_BYTES = 3_000_000


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


OPENER = build_opener(NoRedirect())


def fetch_json(url: str) -> dict:
    with OPENER.open(Request(url, headers={"Accept": "application/json", "User-Agent": "KFM-historical-topo-capture/1.0"}), timeout=20) as response:
        if response.status != 200 or "json" not in response.headers.get("Content-Type", "").lower():
            raise ValueError("TNM product catalog returned an unexpected response")
        body = response.read(MAX_CATALOG_BYTES + 1)
        if len(body) > MAX_CATALOG_BYTES:
            raise ValueError("TNM product catalog exceeded its byte limit")
        value = json.loads(body)
        if not isinstance(value, dict) or not isinstance(value.get("items"), list):
            raise ValueError("TNM product catalog changed shape")
        return value


def product_for_request(item: dict) -> dict:
    if item.get("version") != 1 or item.get("state") != "KS":
        raise ValueError("request is not a Kansas topoView request")
    scan, year, scale, name = (item.get(k) for k in ("scanId", "year", "scale", "name"))
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (scan, year, scale)) or not isinstance(name, str):
        raise ValueError("request identity is incomplete")
    if not re.fullmatch(r"[\w .'-]{1,120}", name) or not (1800 <= year <= 2100 and 1 <= scale <= 10_000_000 and 1 <= scan <= 10_000_000_000):
        raise ValueError("request identity is invalid")
    points = [p for ring in item.get("footprint", []) for p in ring]
    if not 4 <= len(points) <= 4000 or not all(isinstance(p, list) and len(p) >= 2 and all(isinstance(n, (int, float)) for n in p[:2]) for p in points):
        raise ValueError("request footprint is invalid")
    west, east = min(p[0] for p in points), max(p[0] for p in points)
    south, north = min(p[1] for p in points), max(p[1] for p in points)
    if west < -125 or east > -66 or south < 24 or north > 50 or east < -102.1 or west > -94.5 or north < 37 or south > 40.1:
        raise ValueError("request footprint is outside Kansas context")
    bbox = f"{west:.6f},{south:.6f},{east:.6f},{north:.6f}"
    candidates: list[dict] = []
    expected_suffix = f"_{scan}_{year}_{scale}_geo.tif"
    for offset in range(0, 10_000, 500):
        query = urlencode({"datasets": "Historical Topographic Maps", "bbox": bbox, "max": 500, "offset": offset})
        result = fetch_json(f"{TNM_API}?{query}")
        for product in result["items"]:
            url = product.get("urls", {}).get("GeoTIFF") if isinstance(product, dict) else None
            if not isinstance(url, str):
                continue
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.netloc != "prd-tnm.s3.amazonaws.com" or not parsed.path.startswith("/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_") or parsed.query or parsed.fragment:
                continue
            if not parsed.path.endswith(expected_suffix):
                continue
            title = product.get("title", "")
            if f"for {name}, KS {year}" not in title or f"1:{scale}-scale" not in title:
                continue
            candidates.append(product)
        if offset + len(result["items"]) >= result.get("total", 0):
            break
    if len(candidates) != 1:
        raise ValueError(f"expected one exact official GeoTIFF match; found {len(candidates)}")
    return candidates[0]


def stream_geotiff(item: dict, emit: Callable[[bytes], None]) -> dict:
    """Transport validated source chunks to a caller-owned RAW writer."""
    product = product_for_request(item)
    url = product["urls"]["GeoTIFF"]
    sha = hashlib.sha256()
    size = 0
    with OPENER.open(Request(url, headers={"Accept": "image/tiff", "User-Agent": "KFM-historical-topo-capture/1.0"}), timeout=45) as response:
        if response.status != 200 or response.headers.get("Content-Type", "").split(";")[0] != "image/tiff":
            raise ValueError("official download did not return a GeoTIFF")
        declared = int(response.headers.get("Content-Length", "0"))
        if not 1024 <= declared <= MAX_CAPTURE_BYTES:
            raise ValueError("official GeoTIFF size is outside the capture limit")
        while chunk := response.read(1 << 20):
            size += len(chunk)
            if size > MAX_CAPTURE_BYTES:
                raise ValueError("official GeoTIFF exceeded the capture limit")
            sha.update(chunk)
            emit(chunk)
        if size != declared:
            raise ValueError("official GeoTIFF download was incomplete")
    return {"version": 1, "sheet": {k: item[k] for k in ("id", "scanId", "name", "year", "scale", "state")},
            "geotiff": {"url": url, "sha256": sha.hexdigest(), "bytes": size}, "retrievedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "tnmSourceId": product.get("sourceId"), "tnmMetadataUrl": product.get("vendorMetaUrl")}
