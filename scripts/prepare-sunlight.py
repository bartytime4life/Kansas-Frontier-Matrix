#!/usr/bin/env python3
"""Capture three fixed NASA POWER queries and reproduce daily solar display data.

No API runs in the website. Originals stay outside Git. These are modeled
provider-context estimates, not KFM-admitted observations or a released dataset.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://power.larc.nasa.gov/"
PERIOD = {"from": "2020-01-01", "to": "2025-12-31"}
POINTS = (
    {"id": "dodge-city", "name": "Dodge City area", "latitude": 37.7608, "longitude": -99.9689},
    {"id": "wichita", "name": "Wichita area", "latitude": 37.6544, "longitude": -97.4431},
    {"id": "topeka", "name": "Topeka area", "latitude": 39.0725, "longitude": -95.6261},
)
CODES = {"ALLSKY_SFC_SW_DWN": "allSky", "CLRSKY_SFC_SW_DWN": "clearSky"}
PARAMETERS = {
    code: {"units": "kW-hr/m^2/day", "longname": name}
    for code, name in zip(CODES, ("All Sky Surface Shortwave Downward Irradiance", "Clear Sky Surface Shortwave Downward Irradiance"))
}
DOCS = {
    "daily-api.html": BASE + "docs/services/api/temporal/daily/",
    "solar-methods.html": BASE + "docs/methodology/data/sources_fluxes/",
    "time-standard.html": BASE + "docs/faqs/other/",
    "data-faq.html": BASE + "docs/faqs/data/",
    "referencing.html": BASE + "docs/referencing/",
}
MAX_OBJECT, MAX_TOTAL = 1024**2, 4 * 1024**2


def source_url(point):
    return (BASE + "api/temporal/daily/point?parameters=" + ",".join(CODES)
            + f"&community=RE&longitude={point['longitude']}&latitude={point['latitude']}"
            + "&start=20200101&end=20251231&format=JSON&time-standard=LST")


PLAN = {**{p["id"] + ".json": source_url(p) for p in POINTS}, **DOCS}


def encoded(value):
    return (json.dumps(value, separators=(",", ":"), ensure_ascii=True, allow_nan=False) + "\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def strict_json(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("Duplicate JSON key.")
            out[key] = value
        return out

    def invalid(value):
        raise ValueError("Non-finite JSON number.")

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)


def private_path(folder):
    folder = Path(folder)
    if not folder.is_absolute() or folder.is_symlink():
        raise ValueError("Use an absolute, non-symlink capture directory outside Git.")
    resolved = folder.resolve()
    if any((parent / ".git").exists() for parent in (resolved, *resolved.parents)):
        raise ValueError("Original captures must stay outside Git checkouts.")
    return resolved


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("NASA capture redirects are not accepted.")


def capture(folder):
    folder = private_path(folder)
    if folder.exists():
        raise ValueError("Capture directory exists; preserve it and choose a new one.")
    folder.mkdir(parents=True, mode=0o700)
    opener = urllib.request.build_opener(NoRedirect())
    sources, total = {}, 0
    for name, url in PLAN.items():
        request = urllib.request.Request(url, headers={"User-Agent": "KFM-Sunlight/1.0 (bounded public research capture)", "Accept-Encoding": "identity"})
        deadline = time.monotonic() + 60
        with opener.open(request, timeout=20) as response:
            if response.url != url or response.status != 200:
                raise ValueError("Unexpected NASA capture response.")
            chunks, size = [], 0
            while chunk := response.read(64 * 1024):
                size += len(chunk)
                total += len(chunk)
                if size > MAX_OBJECT or total > MAX_TOTAL or time.monotonic() > deadline:
                    raise ValueError("NASA capture exceeded its byte or time budget.")
                chunks.append(chunk)
            raw = b"".join(chunks)
            if not raw:
                raise ValueError("NASA returned an empty source.")
            target = folder / name
            with target.open("xb") as stream:
                stream.write(raw)
            target.chmod(0o600)
            sources[name] = {"url": url, "bytes": len(raw), "sha256": sha(raw),
                             "capturedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
                             "lastModified": response.headers.get("Last-Modified")}
            print(f"Captured {name}: {len(raw):,} bytes", flush=True)
    target = folder / "capture.json"
    target.write_bytes(encoded({"schema": "kfm.sunlight-capture/v1", "sources": sources}))
    target.chmod(0o600)


def verified_sources(folder):
    folder = private_path(folder)
    receipt = folder / "capture.json"
    if receipt.is_symlink() or not receipt.is_file() or receipt.stat().st_size > 32 * 1024:
        raise ValueError("Missing or oversized capture receipt.")
    meta = strict_json(receipt.read_bytes())
    sources = meta.get("sources")
    if meta.get("schema") != "kfm.sunlight-capture/v1" or not isinstance(sources, dict) or set(sources) != set(PLAN):
        raise ValueError("Unexpected NASA capture plan.")
    out, total = {}, 0
    for name, url in PLAN.items():
        path, item = folder / name, sources[name]
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_OBJECT:
            raise ValueError(f"Missing, linked or oversized source: {name}")
        raw = path.read_bytes()
        total += len(raw)
        if (not raw or total > MAX_TOTAL or not isinstance(item, dict) or item.get("url") != url
                or item.get("bytes") != len(raw) or item.get("sha256") != sha(raw)):
            raise ValueError(f"Source integrity mismatch: {name}")
        if not isinstance(item.get("capturedAt"), str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", item["capturedAt"]):
            raise ValueError("Invalid capture time.")
        datetime.fromisoformat(item["capturedAt"].replace("Z", "+00:00"))
        if item.get("lastModified") is not None and (not isinstance(item["lastModified"], str) or len(item["lastModified"]) > 128):
            raise ValueError("Invalid source modification header.")
        out[name] = (raw, item)
    return out


def calendar():
    day, end = date.fromisoformat(PERIOD["from"]), date.fromisoformat(PERIOD["to"])
    out = []
    while day <= end:
        out.append(day.isoformat())
        day += timedelta(days=1)
    return out


def parse_point(raw, point, source):
    data = strict_json(raw)
    if not isinstance(data, dict) or data.get("type") != "Feature" or data.get("parameters") != PARAMETERS or data.get("messages") != []:
        raise ValueError("NASA response schema, units or messages changed.")
    header, geometry = data.get("header"), data.get("geometry")
    if (not isinstance(header, dict) or header.get("title") != "NASA/POWER Source Native Resolution Daily Data"
            or header.get("start") != "20200101" or header.get("end") != "20251231"
            or header.get("time_standard") != "LST" or header.get("fill_value") != -999
            or header.get("sources") != ["SYN1DEG"] or not isinstance(header.get("api"), dict)
            or header["api"].get("name") != "POWER Daily API"
            or not re.fullmatch(r"v2\.\d{1,3}\.\d{1,3}", str(header["api"].get("version")))):
        raise ValueError("NASA product, clock or period identity changed.")
    coordinates = geometry.get("coordinates") if isinstance(geometry, dict) else None
    if (not isinstance(geometry, dict) or geometry.get("type") != "Point" or not isinstance(coordinates, list) or len(coordinates) != 3
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in coordinates)
            or abs(coordinates[0] - point["longitude"]) > 0.001
            or abs(coordinates[1] - point["latitude"]) > 0.001 or not -500 <= coordinates[2] <= 9000):
        raise ValueError("NASA returned coordinate metadata changed.")
    properties = data.get("properties")
    values = properties.get("parameter") if isinstance(properties, dict) else None
    dates = calendar()
    keys = {day.replace("-", "") for day in dates}
    if not isinstance(values, dict) or set(values) != set(CODES):
        raise ValueError("NASA parameter identity changed.")
    for series in values.values():
        if not isinstance(series, dict) or set(series) != keys:
            raise ValueError("NASA calendar contains missing, extra or invalid date keys.")
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v)
               or (v != -999 and not 0 <= v <= 30) for v in series.values()):
            raise ValueError("NASA solar value is invalid; no clipping or zero replacement is allowed.")
    provider = {"api": header["api"], "sources": header["sources"], "fillValue": -999,
                "timeStandard": "LST", "returnedCoordinates": coordinates}
    records = [{"date": day, **{field: values[code][day.replace("-", "")] for code, field in CODES.items()}} for day in dates]
    return {"schema": "kfm.sunlight/v1", "scope": "provider-context", "point": point,
            "period": PERIOD, "source": source, "provider": provider, "parameters": PARAMETERS, "records": records}


def build(sources):
    outputs, points = [], []
    for point in POINTS:
        raw, source = sources[point["id"] + ".json"]
        snapshot = parse_point(raw, point, source)
        body = encoded(snapshot)
        digest = sha(body)
        descriptor = {**point, "url": f"/science-data/sunlight/{point['id']}-{digest[:16]}.json", "sha256": digest,
                      "bytes": len(body), "records": len(snapshot["records"]), "source": source, "provider": snapshot["provider"]}
        points.append(descriptor)
        outputs.append((descriptor["url"], body))
    manifest = {"schema": "kfm.sunlight-manifest/v1", "provider": "NASA POWER", "scope": "provider-context", "period": PERIOD,
                "grid": {"latitudeDegrees": 1, "longitudeDegrees": 1, "description": "Nominal primary CERES SYN1deg solar grid; query coordinates are not cell boundaries."},
                "timeStandard": "LST", "review": "PENDING", "admission": "PENDING", "release": "UNRELEASED",
                "documentation": DOCS["daily-api.html"], "methodology": DOCS["solar-methods.html"],
                "timeDocumentation": DOCS["time-standard.html"], "referencing": DOCS["referencing.html"],
                "rights": "https://science.nasa.gov/learn/entry-points-to-nasa-data/",
                "acknowledgment": "Source: NASA Langley Research Center POWER project, funded by NASA Earth Science Division. See each source for POWER Daily API version and access date.",
                "sources": {name: sources[name][1] for name in DOCS}, "points": points,
                "generatedAt": max(meta["capturedAt"] for _, meta in sources.values())}
    return outputs, manifest


def prepare(folder):
    outputs, manifest = build(verified_sources(folder))
    targets = [(ROOT / "public" / url.lstrip("/"), raw) for url, raw in outputs]
    targets.append((ROOT / "app/labs/sunlight-and-sky/snapshot-manifest.json", encoded(manifest)))
    # Validate every response before changing derived artifacts. Preserve old
    # content-hashed display files; original source captures are never replaced.
    for path, raw in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    print(f"Prepared {sum(p['records'] for p in manifest['points']):,} modeled point-days.")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--capture-dir", type=Path)
    group.add_argument("--source-dir", type=Path)
    args = parser.parse_args()
    folder = args.capture_dir or args.source_dir
    if args.capture_dir:
        capture(folder)
    prepare(folder)


if __name__ == "__main__":
    main()
