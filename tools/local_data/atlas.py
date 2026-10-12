"""Bounded, offline map previews of explicit local captures and completed PRISM grids.

No source admission, release, copying of source holdings, or network access.
Browser requests name catalog IDs, never paths. Originals remain authoritative.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import os
import re
import sqlite3
import subprocess
import threading
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path, PurePosixPath

from tools.local_data import intake
from tools.local_data.file_io import open_regular, read_regular
from tools.local_data.intake_profile import LAT_NAMES, LON_NAMES

SCHEMA = "kfm-local-atlas-preview/v1"
FEATURE_LIMIT = 5000
VERTEX_LIMIT = 180_000
TEXT_LIMIT = 64 * 1024 * 1024
RESPONSE_LIMIT = 12 * 1024 * 1024
ID = re.compile(r"[a-f0-9]{32}\Z")
PRISM_ROOT = Path("data/raw/PRISM data/Kansas")
COUNTIES = Path("data/processed/kfm-local-curation-20260925/tiger/kansas_counties_2025.geojson")
AUTHORITY = {"admission": False, "evidence": False, "release": False}
PRISM_LIMITATIONS = [
    "PRISM modeled grid estimates; county means use valid cell centers, not area-weighted totals or station measurements.",
    "Only completed local grids are offered. Missing periods and missing counties are not zero.",
    "Normals describe 1991–2020, not weather observed in 2020. Daily periods end at 12:00 UTC.",
    "County geometry: Census TIGER/Line 2025. Local exploratory display does not change source admission.",
]


def identity(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:32]


def finite(value):
    if isinstance(value, bool):
        return None
    try:
        v = float(value)
        return v if math.isfinite(v) else None
    except (ValueError, TypeError, OverflowError):
        return None


def safe_path(root: Path, relative: str) -> Path:
    p = PurePosixPath(relative)
    if not relative or p.is_absolute() or any(v in ("..", ".", "") for v in relative.split("/")) or "\\" in relative:
        raise ValueError("ATLAS_PATH_INVALID")
    result = root / p
    fd = open_regular(result)  # includes every ancestor; no symlinks or special files
    os.close(fd)
    return result


@contextmanager
def readonly(path: Path):
    fd = open_regular(path)
    os.close(fd)
    conn = sqlite3.connect(path.absolute().as_uri() + "?mode=ro", uri=True, timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA query_only=ON")
    conn.execute("BEGIN")
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def readonly_intake(root: Path):
    """Keep the same legacy-binding hold as every other intake read surface."""
    with readonly(root / "data/work/intake/index.sqlite") as conn:
        version = conn.execute("SELECT value FROM meta WHERE key='quarantine_binding_version'").fetchone()
        if ((version is None or version[0] != intake.QUARANTINE_BINDING_VERSION)
                and conn.execute("SELECT 1 FROM items WHERE lane='quarantine' LIMIT 1").fetchone()):
            raise ValueError("INTAKE_REANALYSIS_REQUIRED")
        yield conn


def scalar_properties(props: dict) -> dict:
    out = {}
    for key, value in list(props.items())[:80]:
        if not isinstance(key, str) or len(key) > 100:
            continue
        if value is None or isinstance(value, bool):
            out[key] = value
        elif isinstance(value, (int, float)):
            out[key] = finite(value)
        elif isinstance(value, str):
            out[key] = value[:500]
    return out


def normalize_geometry(g: dict, budget: list[int]):
    dimensions = {"Point": 0, "MultiPoint": 1, "LineString": 1, "MultiLineString": 2, "Polygon": 2, "MultiPolygon": 3}
    if not isinstance(g, dict) or g.get("type") not in dimensions:
        raise ValueError("ATLAS_GEOMETRY_UNSUPPORTED")
    def walk(coords, depth):
        if not isinstance(coords, (list, tuple)) or not coords:
            raise ValueError("ATLAS_GEOMETRY_INVALID")
        if depth:
            return [walk(c, depth - 1) for c in coords]
        if len(coords) < 2 or isinstance(coords[0], bool) or isinstance(coords[1], bool):
            raise ValueError("ATLAS_GEOMETRY_INVALID")
        x, y = finite(coords[0]), finite(coords[1])
        if x is None or y is None or not (-180 <= x <= 180 and -85.051129 <= y <= 85.051129):
            raise ValueError("ATLAS_COORDINATES_NOT_WGS84")
        budget[0] += 1
        if budget[0] > VERTEX_LIMIT:
            raise ValueError("ATLAS_VERTEX_LIMIT")
        return [x, y]
    return {"type": g["type"], "coordinates": walk(g.get("coordinates"), dimensions[g["type"]])}


def vector_data(features: list, *, total=None) -> dict:
    out, budget, skipped, exhausted = [], [0], 0, False
    for i, feature in enumerate(features[:FEATURE_LIMIT]):
        try:
            g = normalize_geometry(feature.get("geometry"), budget)
        except (ValueError, AttributeError) as error:
            if str(error) == "ATLAS_VERTEX_LIMIT":
                exhausted = True
                break
            skipped += 1
            continue
        props = feature.get("properties") or {}
        out.append({"type": "Feature", "id": i, "geometry": g, "properties": scalar_properties(props if isinstance(props, dict) else {})})
    if not out:
        raise ValueError("ATLAS_NO_DISPLAYABLE_FEATURES")
    bounds = [180.0, 90.0, -180.0, -90.0]
    def extent(c):
        if isinstance(c[0], (int, float)):
            bounds[0] = min(bounds[0], c[0]); bounds[1] = min(bounds[1], c[1])
            bounds[2] = max(bounds[2], c[0]); bounds[3] = max(bounds[3], c[1])
        else:
            for child in c:
                extent(child)
    for f in out:
        extent(f["geometry"]["coordinates"])
    numeric = sorted({k for f in out for k, v in f["properties"].items() if isinstance(v, (int, float)) and not isinstance(v, bool)})
    total = len(features) if total is None else total
    return {"data": {"type": "FeatureCollection", "features": out}, "bounds": bounds,
            "displayedCount": len(out), "totalCount": total, "truncated": exhausted or total > len(out),
            "numericFields": numeric, "skipped": skipped}


def csv_features(content: bytes) -> tuple[list, int]:
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    fields = reader.fieldnames or []
    if len(fields) > 200:
        raise ValueError("ATLAS_CSV_FIELD_LIMIT")
    lat = next((f for f in fields if f.lower().strip() in LAT_NAMES), None)
    lon = next((f for f in fields if f.lower().strip() in LON_NAMES), None)
    if lat is None or lon is None:
        raise ValueError("ATLAS_CSV_COORDINATES_REQUIRED")
    features, count = [], 0
    for row in reader:
        count += 1
        if count > 2_000_000:
            raise ValueError("ATLAS_CSV_ROW_LIMIT")
        y, x = finite(row.get(lat)), finite(row.get(lon))
        if x is None or y is None or not -180 <= x <= 180 or not -85.051129 <= y <= 85.051129:
            continue
        if len(features) >= FEATURE_LIMIT:
            continue
        props = {k: (finite(v) if finite(v) is not None else v) for k, v in row.items() if k is not None}
        features.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [x, y]}, "properties": props})
    return features, count


def classify_prism(path: str, units: str | None, version: str | None = None):
    parts = path.split("/")
    if not units:
        return None
    if len(parts) >= 6 and parts[:2] == ["normals", "us"]:
        resolution, variable, period, series = parts[2], parts[3], parts[4], "Normals 1991–2020"
    elif len(parts) >= 8 and parts[:2] == ["time_series", "us"]:
        resolution, variable, period, series = parts[3], parts[4], parts[5], "Time series " + parts[2]
    elif len(parts) >= 4 and parts[0] == "prior_versions":
        variable, series = parts[1], "Prior version " + parts[2]
        period = parts[2].split("_")[0]
        match = re.search(r"_(4km|800m)", parts[-1])
        if not match:
            return None
        resolution = match[1]
    else:
        return None
    if period not in {"daily", "monthly", "annual"}:
        return None
    # PRISM publishes annual aggregates alongside monthly grids; the four-digit
    # source key identifies an annual frame, not an unavailable month.
    if period == "monthly" and re.search(r"_\d{4}(?:_avg_30y)?\.zip$", parts[-1]):
        period = "annual"
    expected = {"daily": 8, "monthly": 6, "annual": 4}[period]
    match = re.search(r"_(\d{" + str(expected) + r"})(?:_|\.zip)", parts[-1])
    if not match:
        return None
    key = match[1]
    try:
        when = datetime.strptime(key, {4: "%Y", 6: "%Y%m", 8: "%Y%m%d"}[len(key)])
    except ValueError:
        return None
    normal = series.startswith("Normals")
    if normal and not key.startswith("2020"):
        return None
    label = (when.strftime("%b %d") if period == "daily" else when.strftime("%B") if period == "monthly" else "Annual") + " · normal 1991–2020" if normal else when.strftime({"daily": "%Y-%m-%d", "monthly": "%Y-%m", "annual": "%Y"}[period])
    if period == "daily" and not normal:
        label += " · ends 12:00 UTC"
    series += " · " + (version or "version unspecified")
    group_key = "|".join([series, variable, resolution, period, units])
    return {"group": identity(group_key), "series": series, "variable": variable, "resolution": resolution,
            "period": period, "units": units, "key": key, "label": label, "normal": normal}


class Atlas:
    def __init__(self, root: Path, *, raster_python: Path | None = None):
        self.root = root
        self.raster_python = raster_python
        self.lock = threading.Lock()
        self.render_lock = threading.Lock()
        self.cached_at = 0.0
        self.frame_index: dict = {}
        self.group_index: dict = {}

    def _item(self, identity):
        with readonly_intake(self.root) as conn:
            row = conn.execute("SELECT " + ",".join(intake.ITEM_COLUMNS) + " FROM items WHERE id=?", (identity,)).fetchone()
        if row is None:
            raise ValueError("ATLAS_ITEM_NOT_FOUND")
        return intake._row_item(row, intake.ITEM_COLUMNS)

    def catalog(self, **query):
        where, args = ["items.present=1"], []
        for key in ("status", "domain", "family", "lane"):
            if query.get(key):
                where.append("items." + key + "=?")
                args.append(query[key])
        if query.get("text"):
            where.append("(items.relative_path LIKE ? ESCAPE '\\' OR items.declared_json LIKE ? ESCAPE '\\')")
            text = "%" + query["text"][:100].replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
            args += [text, text]
        join = ""
        if query.get("bbox"):
            box = query["bbox"]
            join = " JOIN item_extent ON item_extent.rid=items.rowid"
            where += ["item_extent.max_x>=? AND item_extent.min_x<=? AND item_extent.max_y>=? AND item_extent.min_y<=?"]
            args += [box[0],box[2],box[1],box[3]]
        clause = join + " WHERE " + " AND ".join(where)
        limit, offset = max(1,min(500,query.get("limit",50))), max(0,query.get("offset",0))
        with readonly_intake(self.root) as conn:
            total = conn.execute("SELECT COUNT(*) FROM items" + clause,args).fetchone()[0]
            rows = conn.execute("SELECT " + ",".join("items."+c for c in intake.ITEM_COLUMNS) + " FROM items" + clause + " ORDER BY items.relative_path LIMIT ? OFFSET ?",args+[limit,offset]).fetchall()
        listing = {"total":total,"offset":offset,"limit":limit,"items":[intake._summary(intake._row_item(r,intake.ITEM_COLUMNS)) for r in rows]}
        for item in listing["items"]:
            kind = item["kind"]
            if kind in {"geojson", "csv", "csv-points", "zipped-shapefile", "shapefile"}:
                preview = "vector"
            elif kind in {"geotiff", "bigtiff", "tiff", "zipped-geotiff", "zip"}:
                preview = "raster"
            else:
                preview = "unsupported"
            item["preview"] = preview
            item["reason"] = "Use the historical-map tools for PDF sheets; other formats need a prepared spatial derivative." if preview == "unsupported" else None
            if kind == "zip":
                item["reason"] = "Preview supports archives containing exactly one GeoTIFF; other contents need a prepared derivative."
            if item["status"] == "blocked" or item["lane"] == "inbox":
                item.update(preview="unsupported", reason="This file is held by intake or has not been captured into the local store.")
        listing["schema"] = "kfm-local-atlas-catalog/v1"
        return listing

    def _refresh(self):
        with self.lock:
            if self.cached_at and time.monotonic() - self.cached_at < 60:
                return
            groups, frames = {}, {}
            path = self.root / PRISM_ROOT / "catalog.sqlite"
            if not path.exists():
                raise ValueError("ATLAS_PRISM_NOT_AVAILABLE")
            with readonly(path) as conn:
                cursor = conn.execute("SELECT path,unit,processed_utc,json_extract(source_metadata,'$.PRISM_DATASET_VERSION') AS version FROM grids WHERE status='complete' LIMIT 500001")
                for n, row in enumerate(cursor):
                    if n == 500_000:
                        raise ValueError("ATLAS_PRISM_CATALOG_LIMIT")
                    c = classify_prism(row["path"], row["unit"], row["version"])
                    if c is None:
                        continue
                    fid = identity("prism:" + row["path"])
                    frame = {"id": fid, "path": row["path"], "processedAt": row["processed_utc"], **c}
                    frames[fid] = frame
                    gid = c["group"]
                    if gid not in groups:
                        groups[gid] = {"id": gid, **{k: c[k] for k in ("series", "variable", "resolution", "period", "units")}, "frameCount": 0, "start": c["key"], "end": c["key"]}
                        groups[gid]["title"] = " · ".join([c["variable"].upper(), c["period"], c["resolution"], c["series"]])
                    g = groups[gid]
                    g["frameCount"] += 1; g["start"] = min(g["start"], c["key"]); g["end"] = max(g["end"], c["key"])
            self.group_index, self.frame_index, self.cached_at = groups, frames, time.monotonic()

    def groups(self):
        self._refresh()
        return {"schema": "kfm-local-atlas-prism-groups/v1", "groups": sorted(self.group_index.values(), key=lambda g: g["title"]), "limitations": PRISM_LIMITATIONS}

    def frames(self, group, *, year=None, offset=0, limit=366):
        self._refresh()
        if group not in self.group_index:
            raise ValueError("ATLAS_GROUP_NOT_FOUND")
        if year is not None and not re.fullmatch(r"\d{4}", year):
            raise ValueError("ATLAS_YEAR_INVALID")
        if not 0 <= offset <= 500000 or not 1 <= limit <= 366:
            raise ValueError("ATLAS_PAGING_INVALID")
        rows = sorted((f for f in self.frame_index.values() if f["group"] == group and (not year or f["key"].startswith(year))), key=lambda f: f["key"], reverse=True)
        return {"schema": "kfm-local-atlas-prism-frames/v1", "group": self.group_index[group], "total": len(rows), "offset": offset, "limit": limit,
                "frames": [{k: f[k] for k in ("id", "label", "key", "units", "processedAt")} for f in rows[offset:offset + limit]]}

    def preview(self, request):
        if not isinstance(request, dict) or set(request) - {"kind", "id", "compareId", "representation", "band"}:
            raise ValueError("ATLAS_REQUEST_INVALID")
        if not isinstance(request.get("kind"), str) or request["kind"] not in {"prism", "file"} or not isinstance(request.get("id"), str) or not ID.fullmatch(request["id"]):
            raise ValueError("ATLAS_REQUEST_INVALID")
        representation = request.get("representation", "counties")
        if not isinstance(representation, str) or representation not in {"counties", "raster"}:
            raise ValueError("ATLAS_REPRESENTATION_INVALID")
        compare = request.get("compareId")
        if compare is not None and (not isinstance(compare, str) or not ID.fullmatch(compare)):
            raise ValueError("ATLAS_REQUEST_INVALID")
        band = request.get("band", 1)
        if isinstance(band, bool) or not isinstance(band, int) or not 1 <= band <= 100:
            raise ValueError("ATLAS_BAND_INVALID")
        if not self.render_lock.acquire(blocking=False):
            raise ValueError("ATLAS_PREVIEW_BUSY")
        try:
            result = self._prism(request) if request["kind"] == "prism" else self._file(request)
            result.update(schema=SCHEMA, authority=dict(AUTHORITY))
            encoded = json.dumps(result, allow_nan=False, separators=(",", ":"))
            if len(encoded.encode()) > RESPONSE_LIMIT:
                raise ValueError("ATLAS_RESPONSE_LIMIT")
            return result
        finally:
            self.render_lock.release()

    def _worker(self, path: Path, kind: str, band=1):
        if self.raster_python is None or not self.raster_python.is_file():
            raise ValueError("ATLAS_SPATIAL_RUNTIME_UNAVAILABLE")
        stat_before = path.stat()
        env = {k: v for k, v in os.environ.items() if k in {"PATH", "LANG", "SYSTEMROOT"}}
        env.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", PROJ_NETWORK="OFF", GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR")
        try:
            process = subprocess.run([str(self.raster_python), "-I", str(Path(__file__).with_name("atlas_worker.py"))],
                                     input=json.dumps({"path": str(path), "kind": kind, "band": band}), text=True,
                                     capture_output=True, env=env, timeout=28, check=False)
        except subprocess.TimeoutExpired:
            raise ValueError("ATLAS_PREVIEW_TIMEOUT") from None
        if len(process.stdout) > RESPONSE_LIMIT or process.returncode:
            raise ValueError("ATLAS_SPATIAL_READER_FAILED")
        value = json.loads(process.stdout)
        if value.get("error"):
            raise ValueError(value["error"])
        if stat_before != path.stat():
            raise ValueError("ATLAS_SOURCE_CHANGED")
        return value

    def _file(self, request):
        if request.get("compareId"):
            raise ValueError("ATLAS_DIFFERENCE_REQUIRES_PRISM")
        item = self._item(request["id"])
        if not item["present"] or item["status"] == "blocked" or item["lane"] not in {"raw", "quarantine"} or not item.get("store_path"):
            raise ValueError("ATLAS_ITEM_HELD")
        if item["store_path"] != f"data/{item['lane']}/{item['relative_path']}":
            raise ValueError("ATLAS_PATH_INVALID")
        path = safe_path(self.root, item["store_path"])
        before = path.stat()
        if before.st_size != item["size_bytes"] or before.st_mtime_ns != item["mtime_ns"]:
            raise ValueError("ATLAS_SOURCE_CHANGED_REANALYZE")
        fmt = item["profile"]["format"]["kind"]
        limits = ["Local exploratory preview; intake review holds remain in effect.", "Numeric attributes retain their source meaning; units are unknown unless explicitly recorded."]
        base = {"id": item["id"], "title": Path((item.get("declared") or {}).get("relative_path") or item["relative_path"]).name,
                "kind": "vector", "source": {"role": "local capture", "attribution": (item.get("declared") or {}).get("source_id") or "Local file; see Intake Desk for source details", "sourceUrl": None, "sha256": item.get("sha256")},
                "time": {"kind": "source content" if item["time_start"] else "unknown", "label": " — ".join(filter(None, [item["time_start"], item["time_end"]])) or "Source period not established", "start": item["time_start"], "end": item["time_end"], "processedAt": None},
                "units": None, "valueField": None, "limitations": limits}
        if fmt == "geojson":
            raw = read_regular(path, TEXT_LIMIT)
            if item.get("sha256") and hashlib.sha256(raw).hexdigest() != item["sha256"]:
                raise ValueError("ATLAS_SOURCE_CHANGED_REANALYZE")
            content = json.loads(raw)
            crs = content.get("crs")
            if crs and crs.get("properties", {}).get("name") not in {"urn:ogc:def:crs:OGC:1.3:CRS84", "EPSG:4326", "urn:ogc:def:crs:EPSG::4326"}:
                raise ValueError("ATLAS_GEOJSON_CRS_UNSUPPORTED")
            features = content.get("features") if content.get("type") == "FeatureCollection" else [content] if content.get("type") == "Feature" else None
            if not isinstance(features, list):
                raise ValueError("ATLAS_GEOJSON_INVALID")
            base.update(vector_data(features))
        elif fmt in {"csv", "csv-points"}:
            raw = read_regular(path, TEXT_LIMIT)
            if item.get("sha256") and hashlib.sha256(raw).hexdigest() != item["sha256"]:
                raise ValueError("ATLAS_SOURCE_CHANGED_REANALYZE")
            features, total = csv_features(raw)
            base.update(vector_data(features, total=total))
            limits.append("Coordinates come from named latitude/longitude columns. Unlocatable rows are omitted; only the first 5,000 locatable rows are shown.")
        elif fmt in {"geotiff", "bigtiff", "tiff", "zipped-geotiff", "zip"}:
            base.update(kind="raster", **self._worker(path, "raster", request.get("band", 1)))
            base["units"] = base["data"].get("units") or None
            limits.append("Kansas-envelope, nearest-neighbor overview; color limits describe sampled display pixels, not full-resolution extremes. Source palette class codes are preserved when present.")
        elif fmt in {"shapefile", "zipped-shapefile"}:
            value = self._worker(path, "vector")
            base.update(vector_data(value["features"], total=value["total"]))
            limits.extend(value.get("limitations", []))
        else:
            raise ValueError("ATLAS_FORMAT_NEEDS_SPATIAL_DERIVATIVE")
        if before != path.stat():
            raise ValueError("ATLAS_SOURCE_CHANGED")
        if base.get("truncated"):
            limits.append("This is a bounded preview, not the complete dataset; omitted features and rows are not zero.")
        base.pop("skipped", None)
        return base

    def _prism(self, request):
        self._refresh()
        frame = self.frame_index.get(request["id"])
        prior = self.frame_index.get(request.get("compareId")) if request.get("compareId") else None
        if frame is None or (request.get("compareId") and prior is None):
            raise ValueError("ATLAS_FRAME_NOT_FOUND")
        if prior and (prior["group"] != frame["group"] or request.get("representation") == "raster"):
            raise ValueError("ATLAS_DIFFERENCE_INCOMPATIBLE")
        def rows(conn, f):
            grid = conn.execute("SELECT * FROM grids WHERE path=? AND status='complete'", (f["path"],)).fetchone()
            classification = classify_prism(grid["path"], grid["unit"], json.loads(grid["source_metadata"] or "{}").get("PRISM_DATASET_VERSION")) if grid else None
            if classification is None or classification["group"] != f["group"]:
                raise ValueError("ATLAS_FRAME_CHANGED_REFRESH")
            data = {r["county_geoid"]: dict(r) for r in conn.execute("SELECT * FROM county_stats WHERE path=?", (f["path"],))}
            return dict(grid), data
        with readonly(self.root / PRISM_ROOT / "catalog.sqlite") as conn:
            grid, values = rows(conn, frame)
            prev_grid, previous = rows(conn, prior) if prior else (None, {})
        title = "PRISM " + frame["variable"].upper() + " · " + frame["label"]
        base = {"id": frame["id"], "kind": "vector", "title": title, "source": {"role": "gridded climate estimate", "attribution": "PRISM Climate Group, Oregon State University; county geometry: Census TIGER/Line 2025", "sourceUrl": "https://prism.oregonstate.edu/", "sha256": grid["source_sha256"]},
                "time": {"kind": "climate normal" if frame["normal"] else "source period", "label": frame["label"], "start": None if frame["normal"] else frame["key"], "end": None if frame["normal"] else frame["key"], "processedAt": grid["processed_utc"]},
                "units": frame["units"], "limitations": list(PRISM_LIMITATIONS), "valueField": "value"}
        if request.get("representation") == "raster":
            path = safe_path(self.root / PRISM_ROOT, grid["tif_path"])
            base.update(kind="raster", **self._worker(path, "raster", request.get("band", 1)))
            base["limitations"].append("Kansas raster is a bounded, nearest-neighbor overview. Color limits describe sampled display pixels, not full-resolution extremes.")
            return base
        geometry = json.loads(read_regular(self.root / COUNTIES, 16 * 1024 * 1024))
        if geometry.get("type") != "FeatureCollection" or len(geometry.get("features", [])) != 105:
            raise ValueError("ATLAS_COUNTY_GEOMETRY_INVALID")
        features, geoids = [], set()
        for f in geometry["features"]:
            geoid = str(f["properties"].get("GEOID", ""))
            if not re.fullmatch(r"20\d{3}", geoid) or geoid in geoids:
                raise ValueError("ATLAS_COUNTY_GEOMETRY_INVALID")
            geoids.add(geoid)
            r, a = values.get(geoid, {}), previous.get(geoid, {})
            value = finite(r.get("mean")) if r.get("valid_pixels", 0) > 0 else None
            props = {"geoid": geoid, "name": f["properties"].get("NAME"), "value": value, "mean": value,
                     "minimum": finite(r.get("minimum")), "maximum": finite(r.get("maximum")), "valid_pixels": r.get("valid_pixels", 0)}
            if prior:
                av = finite(a.get("mean")) if a.get("valid_pixels", 0) > 0 else None
                props.update(valueB=value, valueA=av, value=value - av if value is not None and av is not None else None,
                             valid_pixels_A=a.get("valid_pixels", 0))
            features.append({"type": "Feature", "geometry": f["geometry"], "properties": props})
        base.update(vector_data(features))
        if base["displayedCount"] != 105:
            raise ValueError("ATLAS_COUNTY_GEOMETRY_INVALID")
        # Keep the choropleth legend tied to its physical quantity. Counts and
        # B-only statistics remain available in the inspector, not mislabeled as differences.
        base["numericFields"] = ["value"]
        base.pop("skipped", None)
        if prior:
            base["title"] = "PRISM " + frame["variable"].upper() + " · B − A"
            base["time"]["label"] = "B: " + frame["label"] + " − A: " + prior["label"]
            base["source"].update(sha256A=prev_grid["source_sha256"], sha256B=grid["source_sha256"])
            base["limitations"].append("B minus A compares the same variable, units, resolution, cadence and source version. Missing either value gives no difference.")
        return base
