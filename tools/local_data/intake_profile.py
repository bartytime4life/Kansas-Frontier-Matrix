"""Read-only, bounded profiling of one local file by content, not by extension.

The profiler identifies the format from magic bytes and extracts only the
metadata needed to decide where a file belongs: spatial extent and CRS,
content time coverage, structure (rows, features, bands, pages) and review
hints. It never executes, extracts to disk, follows links, or contacts a
network. Every read is bounded; anything larger is reported as an explicit
gap rather than estimated. A profile is analysis output, not source admission.
"""
from __future__ import annotations

import csv
import io
import json
import math
import os
import re
import sqlite3
import struct
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path, PurePosixPath

from tools.local_data import intake_crs
from tools.local_data.file_io import open_regular

PROFILE_SCHEMA = "kfm-intake-profile/v1"
ANALYZER_VERSION = "1"
SNIFF_BYTES = 64 * 1024
MAX_TEXT_PARSE_BYTES = 64 * 1024 * 1024
MAX_CSV_ROWS = 2_000_000
MAX_ZIP_MEMBERS = 20_000
MAX_MEMBER_HEADER = 1024 * 1024
MAX_FIELDS = 200
MAX_PDF_SCAN = 2 * 1024 * 1024

# Domains match pipeline_specs/ lanes. Rules are hints from names only.
DOMAIN_RULES = [
    ("hydrology", r"stream|gauge|gage|discharge|flow(line)?|river|hydro|watershed|huc\d*|nwm|nhd|flood|reservoir|lake|water[-_ ]?(level|use|right)"),
    ("geology", r"geolog|well|wwc5|aquifer|bedrock|strat|lithol|core|borehole|kgs|fault|seism|quake|oil|gas"),
    ("soil", r"soil|ssurgo|gssurgo|statsgo|horizon|isric|soilgrids"),
    ("atmosphere", r"prism|precip|temperat|climate|weather|ghcn|radar|nexrad|smoke|hms|aerosol|aod|goes|wind|normals"),
    ("air", r"airnow|aqs|ozone|pm2\.?5|pm10|air[-_ ]?quality"),
    ("hazards", r"hazard|tornado|storm|hail|fire|burn|drought|fema|nfhl|disaster"),
    ("agriculture", r"crop|cdl|casma|yield|agri|farm|irrigat|nass|cropland"),
    ("roads-rail-trade", r"road|highway|rail|route|trail|kdot|hpms|freight|bridge|airport"),
    ("settlements-infrastructure", r"county|city|town|place|census|tiger|boundary|parcel|plss|township|building|infrastructure|hifld|school"),
    ("habitat", r"habitat|landcover|land[-_ ]?cover|nlcd|vegetation|wetland|ndvi|prairie|ecoregion"),
    ("flora", r"plant|flora|tree|herbari|vascular|botan"),
    ("fauna", r"species|occurrence|gbif|ebird|bird|inaturalist|idigbio|fish|mammal|fauna|wildlife"),
    ("archaeology", r"archaeolog|artifact|excavat|cultural[-_ ]?resource|shpo"),
    ("people", r"genealog|census[-_ ]?record|obituar|famil|people|person|homestead|land[-_ ]?patent|glo"),
]

# Names that suggest sensitive content; each produces a review flag, never a denial.
REVIEW_RULES = [
    ("possible_cultural_sites", r"archaeolog|burial|cemeter|grave|sacred|shpo|site[-_ ]?(no|num|id)"),
    ("possible_living_persons", r"owner|first[-_ ]?name|last[-_ ]?name|surname|birth|ssn|phone|email|address|dna|genealog|obituar"),
    ("possible_rare_species", r"rare|endanger|threatened|nest|den\b|roost|sensitive[-_ ]?species|t&e|sgcn"),
    ("critical_infrastructure", r"pipeline|substation|transmission|dam[-_ ]?(id|name)|scada|hifld|critical"),
]

LAT_NAMES = {"lat", "latitude", "lat_dd", "latdd", "y_lat", "dec_lat", "decimallatitude", "lat_y"}
LON_NAMES = {"lon", "long", "lng", "longitude", "lon_dd", "londd", "x_lon", "dec_long", "decimallongitude", "lon_x"}
DATE_NAME = re.compile(r"(^|[_ -])(date|time|datetime|timestamp|year|yr|day|obs|observed|valid|period|start|end|eventdate)([_ -]|$)", re.I)
DATE_VALUE = re.compile(r"^\s*(\d{4})(?:[-/](\d{1,2})(?:[-/](\d{1,2}))?)?(?:[T ][\d:.]+(?:Z|[+-]\d{2}:?\d{2})?)?\s*$")
YEAR_IN_PATH = re.compile(r"(?<!\d)(1[6-9]\d{2}|20\d{2})(?!\d)")


class _Profile:
    def __init__(self):
        self.format = {"family": "unknown", "kind": "unknown", "media_type": "application/octet-stream"}
        self.spatial = {"crs": None, "native_bbox": None, "bbox_wgs84": None, "kansas": "unknown", "geometry_types": {}}
        self.temporal = {"content_start": None, "content_end": None, "time_fields": [], "file_metadata_time": None, "path_year_hint": None}
        self.structure = {}
        self.issues: set[str] = set()

    def kind(self, family, kind, media_type):
        self.format = {"family": family, "kind": kind, "media_type": media_type}

    def set_bbox(self, epsg, bbox, *, geographic_guess=False):
        if bbox is None or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in bbox):
            return
        bbox = [float(v) for v in bbox]
        self.spatial["native_bbox"] = [round(v, 7) for v in bbox]
        if epsg is None and geographic_guess and -180 <= bbox[0] <= bbox[2] <= 180 and -90 <= bbox[1] <= bbox[3] <= 90:
            epsg = 4326
            self.issues.add("crs_assumed_geographic")
        if epsg is not None:
            self.spatial["crs"] = f"EPSG:{epsg}"
        wgs = intake_crs.bbox_to_wgs84(epsg, bbox)
        if wgs is None:
            self.issues.add("crs_unknown" if epsg is None else "crs_not_transformable_offline")
        if epsg in (4267, 26713, 26714, 26715):
            self.issues.add("datum_nad27_approximate")
        self.spatial["bbox_wgs84"] = wgs
        self.spatial["kansas"] = intake_crs.kansas_relation(wgs)

    def times(self, values, field=None):
        values = [v for v in values if v]
        if not values:
            return
        lo, hi = min(values), max(values)
        start, end = self.temporal["content_start"], self.temporal["content_end"]
        self.temporal["content_start"] = lo if start is None or lo < start else start
        self.temporal["content_end"] = hi if end is None or hi > end else end
        if field and field not in self.temporal["time_fields"] and len(self.temporal["time_fields"]) < 20:
            self.temporal["time_fields"].append(field)


def _parse_date(value) -> str | None:
    """Return an ISO date for plausible calendar values; years alone become YYYY."""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return f"{int(value):04d}" if 1600 <= value <= 2100 and float(value).is_integer() else None
    if not isinstance(value, str) or len(value) > 40:
        return None
    match = DATE_VALUE.match(value)
    if not match:
        return None
    year, month, day = match.group(1), match.group(2), match.group(3)
    if not 1600 <= int(year) <= 2100:
        return None
    try:
        if day:
            return date(int(year), int(month), int(day)).isoformat()
        if month:
            return f"{year}-{int(month):02d}" if 1 <= int(month) <= 12 else None
    except ValueError:
        return None
    return year


# --- binary readers -------------------------------------------------------

_TIFF_TYPES = {1: ("B", 1), 2: ("s", 1), 3: ("H", 2), 4: ("I", 4), 5: ("II", 8), 6: ("b", 1), 7: ("B", 1),
               8: ("h", 2), 9: ("i", 4), 10: ("ii", 8), 11: ("f", 4), 12: ("d", 8), 16: ("Q", 8), 17: ("q", 8), 18: ("Q", 8)}


def _tiff_ifd(handle, data_limit=8 * 1024 * 1024):
    """Return (endian, tags) for the first IFD of a classic or BigTIFF file."""
    handle.seek(0)
    head = handle.read(16)
    endian = "<" if head[:2] == b"II" else ">"
    magic = struct.unpack(endian + "H", head[2:4])[0]
    big = magic == 43
    offset = struct.unpack(endian + ("Q" if big else "I"), head[8:16] if big else head[4:8])[0]
    handle.seek(offset)
    count_size, entry_size, value_size = (8, 20, 8) if big else (2, 12, 4)
    raw = handle.read(count_size)
    if len(raw) != count_size:
        raise ValueError("TIFF_TRUNCATED")
    count = struct.unpack(endian + ("Q" if big else "H"), raw)[0]
    if count > 4096:
        raise ValueError("TIFF_IFD_LIMIT")
    entries = handle.read(count * entry_size)
    tags = {}
    for i in range(count):
        entry = entries[i * entry_size:(i + 1) * entry_size]
        if len(entry) < entry_size:
            break
        tag, typ = struct.unpack(endian + "HH", entry[:4])
        n = struct.unpack(endian + ("Q" if big else "I"), entry[4:4 + (8 if big else 4)])[0]
        if typ not in _TIFF_TYPES or n > 1_000_000:
            continue
        fmt, size = _TIFF_TYPES[typ]
        total = size * n
        if total > data_limit:
            continue
        if total <= value_size:
            payload = entry[entry_size - value_size:entry_size - value_size + total]
        else:
            pointer = struct.unpack(endian + ("Q" if big else "I"), entry[entry_size - value_size:])[0]
            here = handle.tell()
            handle.seek(pointer)
            payload = handle.read(total)
            handle.seek(here)
        if len(payload) < total:
            continue
        if typ == 2:
            tags[tag] = payload.split(b"\0", 1)[0].decode("latin-1", "replace")
        elif typ in (5, 10):
            parts = struct.unpack(endian + fmt[0] * (2 * n), payload)
            tags[tag] = [parts[j] / parts[j + 1] if parts[j + 1] else 0.0 for j in range(0, len(parts), 2)]
        else:
            tags[tag] = list(struct.unpack(endian + fmt * n, payload))
    return endian, tags


def _profile_tiff(handle, p: _Profile, size):
    _endian, tags = _tiff_ifd(handle)
    width, height = (tags.get(256) or [None])[0], (tags.get(257) or [None])[0]
    p.structure.update(width=width, height=height, bands=(tags.get(277) or [1])[0],
                       bits_per_sample=(tags.get(258) or [None])[0])
    geokeys = tags.get(34735)
    if 33922 in tags or 34264 in tags or geokeys:
        p.kind("raster", "geotiff", "image/tiff; application=geotiff")
    else:
        p.kind("image", "tiff", "image/tiff")
    if 42113 in tags:
        p.structure["nodata"] = tags[42113].strip()[:40]
    if 306 in tags and isinstance(tags[306], str):
        stamp = re.match(r"(\d{4}):(\d{2}):(\d{2})", tags[306])
        if stamp:
            p.temporal["file_metadata_time"] = "-".join(stamp.groups())
    if 330 in tags or (width and height and size and width * height > 0 and 322 in tags):
        p.structure["tiled"] = 322 in tags
    epsg = None
    if geokeys and len(geokeys) >= 4:
        for i in range(4, min(len(geokeys), 4 + 4 * geokeys[3]), 4):
            key, location, _count, value = geokeys[i:i + 4]
            if location == 0 and key == 3072 and value not in (0, 32767):
                epsg = value
            elif location == 0 and key == 2048 and value not in (0, 32767) and epsg is None:
                epsg = value
            elif location == 0 and key == 1024:
                p.structure["model_type"] = {1: "projected", 2: "geographic", 3: "geocentric"}.get(value, "user-defined")
    if epsg is None and geokeys:
        p.issues.add("geotiff_user_defined_crs")
    if width and height:
        if 34264 in tags and len(tags[34264]) >= 16:
            m = tags[34264]
            corners = [(m[0] * c + m[1] * r + m[3], m[4] * c + m[5] * r + m[7]) for c, r in ((0, 0), (width, 0), (0, height), (width, height))]
            xs, ys = [c[0] for c in corners], [c[1] for c in corners]
            p.set_bbox(epsg, [min(xs), min(ys), max(xs), max(ys)])
        elif 33922 in tags and 33550 in tags and len(tags[33922]) >= 6 and len(tags[33550]) >= 2:
            i, j, _k, x, y, _z = tags[33922][:6]
            sx, sy = tags[33550][:2]
            x0, y0 = x - i * sx, y + j * sy
            p.set_bbox(epsg, [x0, y0 - height * sy, x0 + width * sx, y0])
            p.structure["pixel_size"] = [round(sx, 9), round(sy, 9)]


def _profile_las(handle, p: _Profile):
    handle.seek(0)
    head = handle.read(375)
    if len(head) < 227:
        raise ValueError("LAS_TRUNCATED")
    major, minor = head[24], head[25]
    p.kind("pointcloud", "las", "application/vnd.las")
    p.structure["las_version"] = f"{major}.{minor}"
    legacy = struct.unpack("<I", head[107:111])[0]
    count = legacy
    if (major, minor) >= (1, 4) and len(head) >= 255:
        count = struct.unpack("<Q", head[247:255])[0] or legacy
    p.structure["points"] = count
    max_x, min_x, max_y, min_y, max_z, min_z = struct.unpack("<6d", head[179:227])
    p.structure["z_range"] = [round(min_z, 3), round(max_z, 3)]
    p.set_bbox(None, [min_x, min_y, max_x, max_y], geographic_guess=True)
    if p.spatial["crs"] is None:
        p.issues.add("las_crs_in_vlr_not_read")


def _profile_pmtiles(handle, p: _Profile):
    handle.seek(0)
    head = handle.read(127)
    p.kind("tiles", "pmtiles", "application/vnd.pmtiles")
    if len(head) < 127 or head[7] != 3:
        p.issues.add("pmtiles_version_unsupported")
        return
    min_zoom, max_zoom = head[100], head[101]
    min_lon, min_lat, max_lon, max_lat = (v / 1e7 for v in struct.unpack("<4i", head[102:118]))
    p.structure.update(min_zoom=min_zoom, max_zoom=max_zoom, tile_type={1: "mvt", 2: "png", 3: "jpeg", 4: "webp", 5: "avif"}.get(head[99], "unknown"))
    p.set_bbox(4326, [min_lon, min_lat, max_lon, max_lat])


def _profile_png(head, p: _Profile):
    p.kind("image", "png", "image/png")
    if len(head) >= 24:
        p.structure.update(width=struct.unpack(">I", head[16:20])[0], height=struct.unpack(">I", head[20:24])[0])


def _exif_gps(tiff: bytes):
    """Return ((lon, lat) | None, DateTimeOriginal | None) from a raw EXIF TIFF block."""
    endian = "<" if tiff[:2] == b"II" else ">"

    def ifd(offset):
        if offset + 2 > len(tiff):
            return {}
        n = struct.unpack(endian + "H", tiff[offset:offset + 2])[0]
        out = {}
        for i in range(min(n, 512)):
            at = offset + 2 + 12 * i
            if at + 12 > len(tiff):
                break
            tag, typ, count = struct.unpack(endian + "HHI", tiff[at:at + 8])
            out[tag] = (typ, count, tiff[at + 8:at + 12])
        return out

    def rationals(entry):
        typ, count, raw = entry
        pointer = struct.unpack(endian + "I", raw)[0]
        data = tiff[pointer:pointer + 8 * count]
        if typ != 5 or len(data) < 8 * count:
            return None
        parts = struct.unpack(endian + "I" * (2 * count), data)
        return [parts[k] / parts[k + 1] if parts[k + 1] else 0.0 for k in range(0, len(parts), 2)]

    def text(entry):
        typ, count, raw = entry
        data = raw[:count] if count <= 4 else tiff[struct.unpack(endian + "I", raw)[0]:][:count]
        return data.split(b"\0", 1)[0].decode("latin-1", "replace")

    if len(tiff) < 8:
        return None, None
    root = ifd(struct.unpack(endian + "I", tiff[4:8])[0])
    when = None
    if 0x8769 in root:
        sub = ifd(struct.unpack(endian + "I", root[0x8769][2])[0])
        if 0x9003 in sub:
            when = text(sub[0x9003])
    if when is None and 0x0132 in root:
        when = text(root[0x0132])
    point = None
    if 0x8825 in root:
        gps = ifd(struct.unpack(endian + "I", root[0x8825][2])[0])
        if all(k in gps for k in (1, 2, 3, 4)):
            lat, lon = rationals(gps[2]), rationals(gps[4])
            if lat and lon and len(lat) == 3 and len(lon) == 3:
                la = lat[0] + lat[1] / 60 + lat[2] / 3600
                lo = lon[0] + lon[1] / 60 + lon[2] / 3600
                if text(gps[1]).upper().startswith("S"):
                    la = -la
                if text(gps[3]).upper().startswith("W"):
                    lo = -lo
                if -90 <= la <= 90 and -180 <= lo <= 180:
                    point = (lo, la)
    return point, when


def _profile_jpeg(handle, p: _Profile):
    p.kind("image", "jpeg", "image/jpeg")
    handle.seek(2)
    for _ in range(64):
        marker = handle.read(4)
        if len(marker) < 4 or marker[0] != 0xFF:
            return
        kind, length = marker[1], struct.unpack(">H", marker[2:4])[0]
        if kind == 0xE1 and length > 8:
            block = handle.read(min(length - 2, 65533))
            if block.startswith(b"Exif\0\0"):
                point, when = _exif_gps(block[6:])
                if point:
                    p.set_bbox(4326, [point[0], point[1], point[0], point[1]])
                    p.issues.add("photo_exact_location")
                if when:
                    stamp = re.match(r"(\d{4}):(\d{2}):(\d{2})", when)
                    if stamp:
                        p.times([("-".join(stamp.groups()))], "exif:DateTimeOriginal")
            continue
        if kind in (0xC0, 0xC1, 0xC2) and length >= 7:
            block = handle.read(length - 2)
            p.structure.update(height=struct.unpack(">H", block[1:3])[0], width=struct.unpack(">H", block[3:5])[0])
            return
        handle.seek(length - 2, os.SEEK_CUR)


def _profile_pdf(handle, p: _Profile, size):
    p.kind("document", "pdf", "application/pdf")
    handle.seek(0)
    head = handle.read(min(size, MAX_PDF_SCAN))
    tail = b""
    if size > MAX_PDF_SCAN:
        handle.seek(max(0, size - MAX_PDF_SCAN))
        tail = handle.read(MAX_PDF_SCAN)
    blob = head + tail
    version = re.match(rb"%PDF-(\d\.\d)", head)
    if version:
        p.structure["pdf_version"] = version.group(1).decode()
    counts = [int(c) for c in re.findall(rb"/Type\s*/Pages\b[^>]*?/Count\s+(\d+)", blob)[:50]]
    counts += [int(c) for c in re.findall(rb"/Count\s+(\d+)[^>]*?/Type\s*/Pages\b", blob)[:50]]
    if counts:
        p.structure["pages"] = max(counts)
    if re.search(rb"/LGIDict|/Measure\s*<<[^>]*?/Subtype\s*/GEO|/GPTS\s*\[", blob):
        p.kind("document", "geopdf", "application/pdf")
        p.issues.add("geopdf_extent_not_parsed")
    created = re.search(rb"/CreationDate\s*\(D:(\d{4})(\d{2})?(\d{2})?", blob)
    if created:
        p.temporal["file_metadata_time"] = "-".join(g.decode() for g in created.groups() if g)
    if size > 2 * MAX_PDF_SCAN:
        p.issues.add("pdf_partially_scanned")


def _profile_parquet(handle, p: _Profile, size):
    p.kind("table", "parquet", "application/vnd.apache.parquet")
    if size < 12:
        return
    handle.seek(size - 8)
    footer_len = struct.unpack("<I", handle.read(4))[0]
    if footer_len > 8 * 1024 * 1024 or footer_len > size:
        p.issues.add("parquet_footer_not_read")
        return
    handle.seek(size - 8 - footer_len)
    footer = handle.read(footer_len)
    at = footer.find(b'"primary_column"')
    if at < 0:
        return
    start = footer.rfind(b"{", 0, at)
    depth = 0
    for end in range(start, min(len(footer), start + 1_000_000)):
        depth += footer[end:end + 1] == b"{"
        depth -= footer[end:end + 1] == b"}"
        if depth == 0:
            break
    try:
        geo = json.loads(footer[start:end + 1])
    except ValueError:
        return
    p.kind("vector", "geoparquet", "application/vnd.apache.parquet")
    column = geo.get("columns", {}).get(geo.get("primary_column"), {})
    if isinstance(column.get("geometry_types"), list):
        p.spatial["geometry_types"] = {str(t): None for t in column["geometry_types"][:20]}
    epsg = 4326
    crs = column.get("crs")
    if isinstance(crs, dict):
        ident = crs.get("id") or {}
        epsg = ident.get("code") if ident.get("authority") == "EPSG" and isinstance(ident.get("code"), int) else None
    bbox = column.get("bbox")
    if isinstance(bbox, list) and len(bbox) == 4:
        p.set_bbox(epsg, bbox)


def _profile_sqlite(path: Path, p: _Profile):
    """Open a GeoPackage/SQLite read-only, immutable and defensively; read catalogue tables only."""
    uri = path.absolute().as_uri().replace("file://", "file:", 1) + "?mode=ro&immutable=1"
    conn = sqlite3.connect(uri, uri=True, timeout=1)
    try:
        if hasattr(conn, "setconfig") and hasattr(sqlite3, "SQLITE_DBCONFIG_DEFENSIVE"):
            conn.setconfig(sqlite3.SQLITE_DBCONFIG_DEFENSIVE, True)
            conn.setconfig(sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA, False)
        budget = [200_000]

        def guard():
            budget[0] -= 1
            return 1 if budget[0] < 0 else 0
        conn.set_progress_handler(guard, 100)
        names = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 5000")}
        p.structure["tables"] = len(names)
        if "gpkg_contents" not in names:
            p.kind("table", "sqlite", "application/vnd.sqlite3")
            return
        p.kind("vector", "geopackage", "application/geopackage+sqlite3")
        layers, boxes = [], []
        srs = {}
        if "gpkg_spatial_ref_sys" in names:
            for srs_id, org, code in conn.execute("SELECT srs_id, organization, organization_coordsys_id FROM gpkg_spatial_ref_sys LIMIT 1000"):
                if isinstance(org, str) and org.upper() == "EPSG" and isinstance(code, int):
                    srs[srs_id] = code
        for row in conn.execute("SELECT table_name, data_type, min_x, min_y, max_x, max_y, srs_id FROM gpkg_contents LIMIT 1000"):
            layers.append({"name": str(row[0])[:120], "type": str(row[1])[:40]})
            if None not in row[2:6]:
                boxes.append((srs.get(row[6], row[6] if row[6] in (4326,) else None), row[2:6]))
        p.structure["layers"] = layers[:50]
        codes = {b[0] for b in boxes}
        if boxes and len(codes) == 1:
            p.set_bbox(boxes[0][0], [min(b[1][0] for b in boxes), min(b[1][1] for b in boxes),
                                     max(b[1][2] for b in boxes), max(b[1][3] for b in boxes)])
        elif boxes:
            p.issues.add("geopackage_mixed_crs")
    finally:
        conn.close()


# --- text readers ---------------------------------------------------------

def _walk_coords(value, acc):
    stack = [value]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            if len(item) >= 2 and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in item[:2]):
                x, y = item[0], item[1]
                if math.isfinite(x) and math.isfinite(y):
                    acc[0], acc[1] = min(acc[0], x), min(acc[1], y)
                    acc[2], acc[3] = max(acc[2], x), max(acc[3], y)
            else:
                stack.extend(item)


def _geojson_crs(doc) -> int | None:
    crs = doc.get("crs") if isinstance(doc, dict) else None
    if isinstance(crs, dict):
        name = str((crs.get("properties") or {}).get("name", ""))
        match = re.search(r"EPSG:+(\d{4,6})", name)
        if match:
            return int(match.group(1))
        if "CRS84" in name:
            return 4326
    return 4326


def _profile_json(raw: bytes, p: _Profile):
    try:
        doc = json.loads(raw)
    except ValueError:
        p.kind("document", "text", "text/plain")
        p.issues.add("json_invalid")
        return
    kind = doc.get("type") if isinstance(doc, dict) else None
    if kind in ("FeatureCollection", "Feature", "GeometryCollection", "Point", "MultiPoint", "LineString",
                "MultiLineString", "Polygon", "MultiPolygon"):
        p.kind("vector", "geojson", "application/geo+json")
        features = doc.get("features", [doc]) if kind == "FeatureCollection" else [doc]
        if not isinstance(features, list):
            features = []
        acc = [math.inf, math.inf, -math.inf, -math.inf]
        types, keys, temporal = {}, [], {}
        for feature in features:
            geometry = feature.get("geometry") if isinstance(feature, dict) and feature.get("type") == "Feature" else feature
            if isinstance(geometry, dict):
                gtype = str(geometry.get("type"))[:30]
                types[gtype] = types.get(gtype, 0) + 1
                _walk_coords(geometry.get("coordinates"), acc)
                for sub in geometry.get("geometries", []) if isinstance(geometry.get("geometries"), list) else []:
                    if isinstance(sub, dict):
                        _walk_coords(sub.get("coordinates"), acc)
            props = feature.get("properties") if isinstance(feature, dict) else None
            if isinstance(props, dict):
                for key, value in props.items():
                    if len(keys) < MAX_FIELDS and key not in keys:
                        keys.append(str(key)[:80])
                    if DATE_NAME.search(str(key)):
                        parsed = _parse_date(value)
                        if parsed:
                            temporal.setdefault(str(key)[:80], []).append(parsed)
        p.structure.update(features=len(features), fields=keys)
        p.spatial["geometry_types"] = types
        if acc[0] != math.inf:
            p.set_bbox(_geojson_crs(doc), acc)
        for field, values in temporal.items():
            p.times(values, field)
    else:
        p.kind("table", "json", "application/json")
        if isinstance(doc, dict):
            p.structure["fields"] = [str(k)[:80] for k in list(doc)[:MAX_FIELDS]]
        elif isinstance(doc, list):
            p.structure["records"] = len(doc)


def _profile_kml(text: str, p: _Profile, kind="kml"):
    p.kind("vector", kind, "application/vnd.google-earth.kml+xml" if kind == "kml" else "application/vnd.google-earth.kmz")
    acc = [math.inf, math.inf, -math.inf, -math.inf]
    count = 0
    for block in re.findall(r"<coordinates>(.*?)</coordinates>", text, re.S | re.I)[:500_000]:
        for triple in block.split():
            parts = triple.split(",")
            if len(parts) >= 2:
                try:
                    x, y = float(parts[0]), float(parts[1])
                except ValueError:
                    continue
                if math.isfinite(x) and math.isfinite(y):
                    acc = [min(acc[0], x), min(acc[1], y), max(acc[2], x), max(acc[3], y)]
                    count += 1
    p.structure["placemarks"] = len(re.findall(r"<Placemark\b", text, re.I))
    p.structure["coordinates"] = count
    if acc[0] != math.inf:
        p.set_bbox(4326, acc)
    p.times([_parse_date(v[:10]) for v in re.findall(r"<when>([^<]{4,40})</when>", text, re.I)[:100_000]], "kml:when")


def _sniff_dialect(sample: str):
    try:
        return csv.Sniffer().sniff(sample, delimiters=",\t;|")
    except csv.Error:
        return csv.excel


def _profile_csv(handle, p: _Profile, size, sample: str):
    p.kind("table", "csv", "text/csv")
    handle.seek(0)
    text = io.TextIOWrapper(handle, encoding="utf-8", errors="replace", newline="")
    reader = csv.reader(text, _sniff_dialect(sample))
    try:
        header = next(reader)
    except StopIteration:
        return
    header = [h.strip()[:80] for h in header[:MAX_FIELDS]]
    lowered = [h.lower().replace(" ", "_") for h in header]
    lat = next((i for i, h in enumerate(lowered) if h in LAT_NAMES), None)
    lon = next((i for i, h in enumerate(lowered) if h in LON_NAMES), None)
    date_cols = [i for i, h in enumerate(header) if DATE_NAME.search(h)]
    acc = [math.inf, math.inf, -math.inf, -math.inf]
    lows = {i: None for i in date_cols}
    highs = {i: None for i in date_cols}
    rows = 0
    consumed = 0
    for row in reader:
        rows += 1
        consumed += sum(len(c) for c in row) + len(row)
        if rows > MAX_CSV_ROWS or consumed > MAX_TEXT_PARSE_BYTES * 4:
            p.issues.add("csv_partially_scanned")
            break
        if lat is not None and lon is not None and max(lat, lon) < len(row):
            try:
                y, x = float(row[lat]), float(row[lon])
            except ValueError:
                pass
            else:
                if -90 <= y <= 90 and -180 <= x <= 180 and (x, y) != (0.0, 0.0):
                    acc = [min(acc[0], x), min(acc[1], y), max(acc[2], x), max(acc[3], y)]
        for i in date_cols:
            if i < len(row):
                parsed = _parse_date(row[i])
                if parsed:
                    lows[i] = parsed if lows[i] is None or parsed < lows[i] else lows[i]
                    highs[i] = parsed if highs[i] is None or parsed > highs[i] else highs[i]
    text.detach()
    p.structure.update(rows=rows, fields=header)
    if acc[0] != math.inf:
        p.kind("vector", "csv-points", "text/csv")
        p.set_bbox(4326, acc)
        p.structure["coordinate_columns"] = [header[lon], header[lat]]
    for i in date_cols:
        if lows[i]:
            p.times([lows[i], highs[i]], header[i])


# --- archives -------------------------------------------------------------

def _shp_header(data: bytes):
    if len(data) < 100 or struct.unpack(">i", data[:4])[0] != 9994:
        return None
    shape_type = struct.unpack("<i", data[32:36])[0]
    return shape_type, list(struct.unpack("<4d", data[36:68]))


def _dbf_header(data: bytes):
    if len(data) < 32:
        return None, []
    records = struct.unpack("<I", data[4:8])[0]
    header_len = struct.unpack("<H", data[8:10])[0]
    fields = []
    for at in range(32, min(header_len, len(data)) - 1, 32):
        if data[at] == 0x0D:
            break
        name = data[at:at + 11].split(b"\0", 1)[0].decode("latin-1", "replace").strip()
        if name:
            fields.append(name[:20])
        if len(fields) >= MAX_FIELDS:
            break
    return records, fields


SHAPE_TYPES = {0: "Null", 1: "Point", 3: "LineString", 5: "Polygon", 8: "MultiPoint", 11: "PointZ", 13: "LineStringZ",
               15: "PolygonZ", 18: "MultiPointZ", 21: "PointM", 23: "LineStringM", 25: "PolygonM", 28: "MultiPointM", 31: "MultiPatch"}


def _apply_shapefile(p: _Profile, shp: bytes, prj: str | None, dbf: bytes | None):
    header = _shp_header(shp)
    if header is None:
        p.issues.add("shapefile_header_invalid")
        return
    shape_type, bbox = header
    p.kind("vector", "shapefile", "application/vnd.shp")
    p.spatial["geometry_types"] = {SHAPE_TYPES.get(shape_type, str(shape_type)): None}
    epsg = intake_crs.epsg_from_wkt(prj) if prj else None
    if prj is None:
        p.issues.add("shapefile_missing_prj")
    p.set_bbox(epsg, bbox, geographic_guess=prj is None)
    if dbf:
        records, fields = _dbf_header(dbf)
        p.structure.update(features=records, fields=fields)


def _profile_zip(handle, p: _Profile, size):
    p.kind("archive", "zip", "application/zip")
    try:
        archive = zipfile.ZipFile(handle)
    except zipfile.BadZipFile:
        p.issues.add("zip_invalid")
        return
    with archive:
        infos = archive.infolist()
        if len(infos) > MAX_ZIP_MEMBERS:
            p.issues.add("zip_member_limit")
            infos = infos[:MAX_ZIP_MEMBERS]
        names = [i.filename for i in infos if not i.is_dir()]
        expanded = sum(i.file_size for i in infos)
        p.structure.update(members=len(names), expanded_bytes=expanded)
        if size and expanded / max(size, 1) > 100:
            p.issues.add("zip_high_compression_ratio")
        if any(n.startswith("/") or ".." in PurePosixPath(n).parts or "\\" in n for n in names):
            p.issues.add("zip_unsafe_member_paths")
        extensions = {}
        for n in names:
            ext = PurePosixPath(n).suffix.lower()
            extensions[ext] = extensions.get(ext, 0) + 1
        p.structure["member_types"] = dict(sorted(extensions.items(), key=lambda kv: -kv[1])[:15])

        def head(name, limit=MAX_MEMBER_HEADER):
            info = archive.getinfo(name)
            if info.file_size > 64 * 1024 * 1024 and limit > 128:
                limit = 128
            with archive.open(info) as member:
                return member.read(limit)

        shps = sorted(n for n in names if n.lower().endswith(".shp"))
        if shps:
            stem = shps[0][:-4]
            lookup = {n.lower(): n for n in names}
            prj = lookup.get((stem + ".prj").lower())
            dbf = lookup.get((stem + ".dbf").lower())
            _apply_shapefile(p, head(shps[0], 100), head(prj, 64 * 1024).decode("latin-1", "replace") if prj else None,
                             head(dbf, 32 + 32 * (MAX_FIELDS + 1)) if dbf else None)
            p.structure["layers"] = [PurePosixPath(s).stem[:120] for s in shps[:50]]
            p.format["kind"] = "zipped-shapefile"
            return
        kmls = [n for n in names if n.lower().endswith(".kml")]
        if kmls:
            info = archive.getinfo(kmls[0])
            if info.file_size <= MAX_TEXT_PARSE_BYTES:
                _profile_kml(head(kmls[0], MAX_TEXT_PARSE_BYTES).decode("utf-8", "replace"), p, "kmz")
            return
        gis = [e for e in extensions if e in {".tif", ".tiff", ".gpkg", ".geojson", ".json", ".csv", ".las", ".laz", ".pdf", ".jpg", ".png", ".nc"}]
        if gis:
            p.structure["contains"] = sorted(gis)


# --- entry point ----------------------------------------------------------

def _hints(path_text: str, p: _Profile, declared_domain: str | None):
    fields = " ".join(p.structure.get("fields", []) if isinstance(p.structure.get("fields"), list) else [])
    haystack = (path_text + " " + fields).lower()
    scores = []
    for domain, pattern in DOMAIN_RULES:
        hits = re.findall(pattern, haystack)
        if hits:
            scores.append((len(hits), domain, sorted({h if isinstance(h, str) else h[0] for h in hits})[:5]))
    scores.sort(key=lambda s: (-s[0], s[1]))
    flags = sorted({flag for flag, pattern in REVIEW_RULES if re.search(pattern, haystack)})
    if "photo_exact_location" in p.issues:
        flags.append("exact_location")
    guess = declared_domain or (scores[0][1] if scores else None)
    basis = "declared" if declared_domain else ("name-and-field-keywords" if scores else "none")
    return {"domain": guess, "domain_basis": basis,
            "domain_candidates": [{"domain": d, "matches": m} for _n, d, m in scores[:3]],
            "review_flags": sorted(set(flags))}


def profile_file(path: Path, *, display_path: str | None = None, declared: dict | None = None) -> dict:
    """Profile one regular file. Errors inside a format reader become issues."""
    p = _Profile()
    shown = display_path or path.name
    year_hints = sorted(set(YEAR_IN_PATH.findall(shown)))
    if year_hints:
        p.temporal["path_year_hint"] = [year_hints[0], year_hints[-1]]
    fd = open_regular(path)
    with os.fdopen(fd, "rb") as handle:
        size = os.fstat(handle.fileno()).st_size
        head = handle.read(SNIFF_BYTES)
        try:
            if head[:4] in (b"II*\0", b"MM\0*", b"II+\0", b"MM\0+"):
                _profile_tiff(handle, p, size)
            elif head[:4] == b"LASF":
                _profile_las(handle, p)
            elif head[:7] == b"PMTiles":
                _profile_pmtiles(handle, p)
            elif head[:8] == b"\x89PNG\r\n\x1a\n":
                _profile_png(head, p)
            elif head[:3] == b"\xff\xd8\xff":
                _profile_jpeg(handle, p)
            elif head[:5] == b"%PDF-":
                _profile_pdf(handle, p, size)
            elif head[:4] == b"PAR1":
                _profile_parquet(handle, p, size)
            elif head[:16] == b"SQLite format 3\0":
                _profile_sqlite(path, p)
            elif head[:4] == b"PK\x03\x04" or head[:4] == b"PK\x05\x06":
                handle.seek(0)
                _profile_zip(handle, p, size)
            elif head[:4] in (b"CDF\x01", b"CDF\x02", b"CDF\x05"):
                p.kind("array", "netcdf-classic", "application/x-netcdf")
                p.issues.add("array_metadata_not_parsed")
            elif head[:8] == b"\x89HDF\r\n\x1a\n":
                p.kind("array", "hdf5-or-netcdf4", "application/x-hdf5")
                p.issues.add("array_metadata_not_parsed")
            elif head[:4] == b"GRIB":
                p.kind("array", "grib", "application/x-grib")
                p.issues.add("array_metadata_not_parsed")
            elif head[:2] == b"\x1f\x8b":
                p.kind("archive", "gzip", "application/gzip")
                p.issues.add("compressed_contents_not_inspected")
            elif len(head) > 262 and head[257:262] == b"ustar":
                p.kind("archive", "tar", "application/x-tar")
                p.issues.add("compressed_contents_not_inspected")
            elif shown.lower().endswith(".shp") and _shp_header(head):
                sibling = path.with_suffix(".prj")
                dbf = path.with_suffix(".dbf")
                prj = sibling.read_bytes()[:65536].decode("latin-1", "replace") if sibling.is_file() and not sibling.is_symlink() else None
                dbf_head = dbf.open("rb").read(32 + 32 * (MAX_FIELDS + 1)) if dbf.is_file() and not dbf.is_symlink() else None
                _apply_shapefile(p, head, prj, dbf_head)
            elif b"\0" not in head[:8192]:
                text = head.decode("utf-8", "replace")
                stripped = text.lstrip("﻿ \t\r\n")
                if stripped[:1] in "{[":
                    if size > MAX_TEXT_PARSE_BYTES:
                        p.kind("table", "json", "application/json")
                        p.issues.add("json_too_large_for_inline_profile")
                    else:
                        handle.seek(0)
                        _profile_json(handle.read(MAX_TEXT_PARSE_BYTES + 1), p)
                elif re.match(r"<\?xml[^>]*>\s*<kml\b|<kml\b", stripped[:400], re.I):
                    if size <= MAX_TEXT_PARSE_BYTES:
                        handle.seek(0)
                        _profile_kml(handle.read(MAX_TEXT_PARSE_BYTES).decode("utf-8", "replace"), p)
                    else:
                        p.kind("vector", "kml", "application/vnd.google-earth.kml+xml")
                        p.issues.add("kml_too_large_for_inline_profile")
                elif "\n" in stripped and any(d in stripped.split("\n", 1)[0] for d in ",\t;|"):
                    _profile_csv(handle, p, size, text[:16384])
                else:
                    p.kind("document", "text", "text/plain")
        except (ValueError, struct.error, IndexError, KeyError, OSError, sqlite3.Error, zipfile.BadZipFile, RuntimeError, EOFError, UnicodeError):
            p.issues.add("format_reader_failed")
    if p.format["kind"] == "unknown":
        p.issues.add("format_unrecognized")
    if p.format["family"] in ("raster", "vector", "pointcloud", "tiles") and p.spatial["bbox_wgs84"] is None and "crs_not_transformable_offline" not in p.issues:
        p.issues.add("spatial_extent_unknown")
    if p.spatial["kansas"] == "outside":
        p.issues.add("outside_kansas")
    return {
        "schema": PROFILE_SCHEMA,
        "analyzer_version": ANALYZER_VERSION,
        "format": p.format,
        "spatial": p.spatial,
        "temporal": p.temporal,
        "structure": p.structure,
        "hints": _hints(shown, p, (declared or {}).get("domain")),
        "issues": sorted(p.issues),
        "profiled_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
