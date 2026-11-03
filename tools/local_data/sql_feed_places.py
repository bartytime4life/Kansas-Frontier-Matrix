"""SQL feeds for Kansas places and history: GNIS names, post offices, county boundaries, ceded lands, Atack
railroads, members of Congress, NPS places and the National Register.

A rebuild (2026-11-03) of eight feeds whose source was lost with the pipeline PC's system disk. Their data,
raw copies, receipts and feed state survived on the data volume, so this module reproduces them: the same
tables (DDL copied from the database), the same ``load_version`` keys, the same kept-file names
(``<name>-<sha12><ext>``), the same receipt fields and the same ``kfm_feed_state`` shape. Every kept copy
was checked byte for byte against the surviving raw files on 2026-11-03 (the GNIS cuts, the post-office cut,
the AHCB zip and its members, the two Kansas shapefile zips, the cession table, the Congress, NPS and NRHP
JSON Lines and the NRHP sheet cuts), so an unchanged provider file is recognized as ``unchanged`` and nothing
is loaded twice. The one thing the surviving files cannot show is how a few table columns were derived
(the ISO forms of dates, the chronology's ``subject``), noted on each feed below.

Shared rules: a provider's national file is cut to Kansas at once and only the cut is kept, with the full
download recorded in the receipt (``original``, ``kept: false``). Network work runs outside the pipeline
lock; database writes inside it, one transaction per source file, through ``sql_feed_hazards.keep_version``
(so a provider's return to an earlier version is reinstated rather than refused). An HTTP 429 stops a feed
with ``<SOURCE>_RATE_LIMITED`` and keeps what loaded. The Kansas box is lon -102.06..-94.58, lat
36.99..40.01; a geometry is Kansas when its bbox overlaps the box and then a vertex lies inside it, an edge
crosses it, or (polygons) a box corner lies inside the polygon. Shapefiles are read with the small
standard-library reader in this module (dBase C/N/F/D/L, shape types Point, PolyLine, Polygon, MultiPoint and
their Z/M variants; geographic NAD83/WGS84 ``.prj`` passes through, the ESRI Albers equal-area conic is
inverted with Snyder's ellipsoidal formulas; anything else stops with ``SHAPEFILE_PROJECTION_UNSUPPORTED``).
GeoJSON from a shapefile follows RFC 7946 ring orientation with coordinates rounded to 7 decimals; the kept
shapefile has the exact values. A Kansas-only shapefile is written with the records copied byte for byte,
a new ``.shx`` and bbox, the ``.prj``/``.cpg``/``.shp.xml`` carried along, stored in a zip with fixed
timestamps, so the same records always give the same bytes.

``gnis-names``: USGS Geographic Names Information System staged products in the public bucket
https://prd-tnm.s3.amazonaws.com/ under ``StagedProducts/GeographicNames/`` (public domain; USGS asks for
acknowledgment; https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits). Seven
files, each a ``load_version`` key (its S3 key), kept as the Kansas text gzipped (UTF-8 with BOM, ``|``
delimited, CRLF, records copied byte for byte): the current Kansas names file (``kfm_gnis_names``, whole, it
includes rivers whose primary point is in a neighbouring state); the 2021 archive Kansas file
(``kfm_gnis_names_2021``, whole; USGS no longer maintains cemeteries, churches, schools, post offices and
locales, so the archive is the only GNIS source for them); the national government units (state 20) and
historical features (state 20 or a Kansas feature id) files; and AllNames, FeatureDescriptionHistory and the
2021 Feature_Description_History cut by Kansas feature id. The Kansas ids are the feature ids in the two
names tables; the names files load first, and an id-cut file is cut again when the id set changes (its
SHA-256, ``kansas_ids_sha256``, is the sorted ids joined by commas). The current exports quote values that
hold quotes or line breaks; the 2021 archive never quotes, so its quotes are literal. ``feature_id`` and
elevations are INTEGER, decimal coordinates REAL with GNIS's 0 for unknown stored as NULL, all else TEXT as
published (dates stay MM/DD/YYYY). Each run: nothing until 6 days after the last complete check; then one
listing request per file (``?prefix=<key>``: Key, LastModified, ETag, Size) and a download only when the
ETag, size or time changed or the ids changed. A download must match the listed size, and its MD5 where the
ETag is not multipart (``GNIS_DOWNLOAD_MISMATCH``). At most ``max_files`` files a run (7: one run).

``post-offices``: Blevins, Cameron; Helbock, Richard W., 2021, "US Post Offices", Harvard Dataverse,
doi:10.7910/DVN/NUKCNA (CC0 1.0; https://cblevins.github.io/us-post-offices/). Each run, after 28 days, reads
the dataset's metadata (one small request); when the ``us-post-offices.tab`` file's MD5 changed, its original
CSV (``?format=original``, 31 MB, the authors' file whose MD5 Dataverse lists) is streamed, checked against
that MD5, and cut to the rows whose State is KS (4,260; 2,866 geocoded), header and rows copied byte for
byte, into ``kfm_blevins_post_offices`` (key ``us-post-offices``). Years, id, duration, the GNIS id and
elevation are INTEGER; coordinates and gnis_dist REAL; TRUE/FALSE flags and stamp_index TEXT. The
random-coords file is not loaded (it invents a point inside the county for ungeocoded offices). A licence
other than CC0 stops the run with ``POST_OFFICES_LICENSE_CHANGED``.

``county-boundaries``: Newberry Library, Atlas of Historical County Boundaries, Kansas,
https://digital.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip (CC BY-NC-SA 2.5, read from the deed in the
zip; the preferred citation from KS_Metadata1.htm; terms https://digital.newberry.org/ahcb/download). After
28 days the zip (2.1 MB) is downloaded again and compared by SHA-256. A new version is kept whole (key
``ks-historical-counties``) and loads the 341 dated county versions with geometry, bbox and ``in_kansas``
(the Kansas test; the Kansas Territory counties now in Colorado get 0) into ``kfm_ahcb_county_versions``;
the comprehensive database text (key ``ks-comprehensive-database``, dates kept as published) into
``kfm_ahcb_changes``; and the two chronology pages (keys ``chronology/consolidated`` and
``chronology/individual``) into ``kfm_ahcb_chronology`` as entries: the consolidated page gives one row per
event, sub-events listed under a date numbered from 1; the individual page one row per dated entry of each
county, plus a row for each heading that only points to another name ("BARBOUR (see BARBER)"). ``date_iso``
is derived from the entry date ("25 Aug 1855" -> 1855-08-25; "Jul 1887" -> 1887-07; "by 1959" -> 1959).
Not recoverable from the surviving files: whether the consolidated rows' ``subject`` was "Kansas" (used
here) and whether the versions' dBase dates were stored as ISO (used here).

``ceded-lands``: USDA Forest Service "Tribal Ceded Lands" (S_USA.TRIBALCEDEDLANDS, digitized from Charles C.
Royce, Indian Land Cessions in the United States, 1899), https://data.fs.usda.gov/geodata/edw/edw_resources/shp/
(public domain; informational, no warranty, not legal boundaries; terms
https://data.fs.usda.gov/geodata/edw/datasets.php). After 28 days the shapefile zip (1.6 MB, 718 polygons)
is downloaded and compared by SHA-256; a new version is cut to the polygons that intersect Kansas (58), kept
as a Kansas shapefile (key ``tribal-ceded-lands``) and loaded into ``kfm_usfs_ceded_lands``. The cession
table (tribes, treaty dates, Royce and Kappler links) is read from the Forest Service map service
(EDW_TribalCessionLands_01/MapServer/2, 725 rows, paged by OBJECTID), cut to the cessions with a kept
polygon or whose state list has KS, kept as canonical JSON (key ``tribal-ceded-lands-table``) and loaded
into ``kfm_usfs_ceded_land_cessions``; its ArcGIS dates (milliseconds at noon UTC) are stored as ISO days.

``railroads-history``: Jeremy Atack, "Historical Geographic Information Systems (GIS) database of U.S.
Railroads for 1826-1911" (no licence stated; a suggested citation and a request for corrections;
https://my.vanderbilt.edu/jeremyatack/data-downloads/). After 28 days the downloads page is read for the
newest ``RR1826-1911*.zip`` link and its "last edited" date; the zip (16 MB, 76,849 segments, USA Contiguous
Albers) is downloaded and compared by SHA-256; a new version is reprojected, cut to the segments that
intersect Kansas (3,439; 3,140 tagged Kansas, the rest neighbouring slivers), kept as a Kansas shapefile with
Atack's ``.shp.xml`` (key ``rr1826-1911``) and loaded into ``kfm_atack_railroads`` with all 12 dbf fields
(``in_op_by`` is the year in operation; ``exact_date`` is 0 for every Kansas segment).

``congress-kansas``: the unitedstates project's congress-legislators files (CC0 1.0),
https://unitedstates.github.io/congress-legislators/legislators-current.json and legislators-historical.json.
After 6 days each file is fetched and cut to the legislators with any term in state KS (150 on 2026-11-03),
sorted by bioguide id and kept as canonical JSON Lines (keys ``legislators-current`` and
``legislators-historical``), each loading ``kfm_congress_legislators`` (identifiers, names, bio, JSON for the
multi-valued parts, the record whole) and ``kfm_congress_terms`` (one row per Kansas term; ``term_index`` is
the term's position in the record). Fields outside the known set are listed in the receipt and the summary
(``unknown_fields``), never dropped from the JSON columns.

``nps-places``: National Park Service public layers in Kansas, from the NationalDatasets feature services on
mapservices.nps.gov (points of interest, buildings, parking lots, roads, trails) and the Land Resources
Division boundary and tract service (public domain, 17 U.S.C. 105; https://www.nps.gov/aboutus/disclaimer.htm).
Each layer is queried with the Kansas envelope (2,000 features a page, ordered by OBJECTID) after 28 days,
kept as canonical JSON Lines sorted by OBJECTID (key ``layer/<name>``) and loaded into ``kfm_nps_<name>``
with every attribute, the geometry and its bbox. A field the table does not have stops the run with
``NPS_FIELDS_CHANGED``.

``nrhp``: National Park Service, National Register of Historic Places (public domain;
https://www.nps.gov/aboutus/disclaimer.htm). Spreadsheets: each run reads
https://www.nps.gov/subjects/nationalregister/data-downloads.htm for the dated links of the six workbooks;
when a date changed, or 91 days after the last check, all six are fetched and read with the standard
library. "everything" is checked to hold every Kansas row of listed, removed, the NHLs and the federal DOEs;
then everything, federal-DOEs and the MPS covers are loaded (keys ``sheet/everything``, ``sheet/federal-does``,
``sheet/mps-covers``; ``basis`` "everything" in state). If that superset check fails, listed, removed and
NHLs are loaded instead (``basis`` "parts"), the everything key is retired and the uncovered references
go in the summary. Kansas rows have State KANSAS; MPS covers list states ("AL; AK; ...") and count when KS is
among them. The kept copy is the Kansas rows as CSV: shared and inline strings, booleans as 0/1 and numbers
and date serials as written. ``kfm_nrhp_properties`` holds every sheet column in snake_case plus
``listed_date_iso`` and ``nhl_designated_date_iso`` from the Excel serials. Locations: the nrhp_locations
map service, points (layer 0) and polygons (layer 1) with ``UPPER(STATE)='KANSAS'`` (restricted addresses
are not in it and nothing fills them in), paged at 2,000 and checked against ``returnCountOnly``, every 6
days, keys ``layer/0`` and ``layer/1``, into ``kfm_nrhp_locations`` (dates as the service's epoch
milliseconds). It joins properties on ``ref = nris_refnum``; the tables are not merged.
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timedelta, timezone
import email.utils
import gzip
import hashlib
import html
import io
import json
import math
from pathlib import Path
import re
import struct
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, csv_bytes, ddl, keep_version, loaded_keys, number, retire, save_state
from tools.local_data.sql_feeds import FeedError

# --- Shared ----------------------------------------------------------------------------------------

KANSAS_BOX = (-102.06, 36.99, -94.58, 40.01)
KANSAS_TEST = ("bbox overlaps lon -102.06..-94.58 lat 36.99..40.01, then a vertex inside the box, an edge through it, "
               "or a box corner inside the polygon")
GEOMETRY_COLUMNS = [("geometry_geojson", "TEXT"), ("min_lon", "REAL"), ("min_lat", "REAL"), ("max_lon", "REAL"), ("max_lat", "REAL")]
ARCGIS_PAGE = 2000
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def column(name: str) -> str:
    """A provider field name as a column: snake_case at lower-to-upper steps, dots as underscores, runs of
    underscores collapsed (VxCount -> vx_count, FID_1900St -> fid_1900st, Shape__Area -> shape_area)."""
    return re.sub(r"_+", "_", re.sub(r"(?<=[a-z])([A-Z])", r"_\1", name.replace(".", "_"))).lower()


def qddl(table: str, columns, indexes) -> str:
    """``CREATE TABLE`` with quoted column names: columns is [(name, type or None)]."""
    body = ", ".join(f'"{c}" {t}' if t else f'"{c}"' for c, t in columns)
    return (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
            f"PRIMARY KEY(file_id, row_number));\n"
            + "".join(f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(i)} ON {table}({', '.join(f'\"{c}\"' for c in i)});\n" for i in indexes))


def _fetch(ctx, url: str, code: str, **kw):
    try:
        return ctx.fetch(url, **kw)
    except FeedError as error:
        if str(error).startswith("HTTP_429"):
            raise FeedError(f"{code}_RATE_LIMITED {url}") from None
        raise


def _download(ctx, url: str, dest: Path, code: str, **kw):
    try:
        return core.download(ctx, url, dest, **kw)
    except FeedError as error:
        if str(error).startswith("HTTP_429"):
            raise FeedError(f"{code}_RATE_LIMITED {url}") from None
        raise


def _http_date(text):
    """An HTTP Last-Modified header as an ISO day, or None."""
    try:
        return email.utils.parsedate_to_datetime(text).date().isoformat() if text else None
    except (TypeError, ValueError):
        return None


def _ms_day(value):
    """An ArcGIS epoch-millisecond date as an ISO day."""
    return None if value is None else (EPOCH + timedelta(milliseconds=value)).date().isoformat()


def _points(coordinates):
    """Every (x, y) in a GeoJSON coordinate array."""
    if coordinates and isinstance(coordinates[0], (int, float)):
        yield coordinates[0], coordinates[1]
        return
    for part in coordinates:
        yield from _points(part)


def bbox(geometry) -> tuple:
    """(min_lon, min_lat, max_lon, max_lat) of a GeoJSON geometry, or four Nones."""
    xs, ys = [], []
    for x, y in _points(geometry["coordinates"] if geometry else []):
        xs.append(x)
        ys.append(y)
    return (min(xs), min(ys), max(xs), max(ys)) if xs else (None, None, None, None)


def _crosses(a, b, box) -> bool:
    """Whether segment a-b crosses the box's edges (Liang-Barsky)."""
    (x0, y0), (x1, y1) = a, b
    dx, dy, t0, t1 = x1 - x0, y1 - y0, 0.0, 1.0
    for p, q in ((-dx, x0 - box[0]), (dx, box[2] - x0), (-dy, y0 - box[1]), (dy, box[3] - y0)):
        if p == 0:
            if q < 0:
                return False
        else:
            t = q / p
            if p < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
    return t0 <= t1


def _inside(ring, x, y) -> bool:
    inside = False
    for (ax, ay), (bx, by) in zip(ring, ring[1:]):
        if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay):
            inside = not inside
    return inside


def in_kansas(geometry, box=KANSAS_BOX) -> bool:
    """The Kansas test of the module docstring, on a GeoJSON geometry."""
    if geometry is None:
        return False
    west, south, east, north = bbox(geometry)
    if west is None or west > box[2] or east < box[0] or south > box[3] or north < box[1]:
        return False
    if any(box[0] <= x <= box[2] and box[1] <= y <= box[3] for x, y in _points(geometry["coordinates"])):
        return True
    kind, coords = geometry["type"], geometry["coordinates"]
    lines = ([coords] if kind == "LineString" else coords if kind == "MultiLineString" else
             [r for r in coords] if kind == "Polygon" else [r for p in coords for r in p] if kind == "MultiPolygon" else [])
    if any(_crosses(a, b, box) for line in lines for a, b in zip(line, line[1:])):
        return True
    polygons = [coords] if kind == "Polygon" else coords if kind == "MultiPolygon" else []
    corners = [(box[0], box[1]), (box[2], box[1]), (box[2], box[3]), (box[0], box[3])]
    return any(_inside(polygon[0], x, y) and not any(_inside(hole, x, y) for hole in polygon[1:])
               for polygon in polygons for x, y in corners)


def _geometry_row(geometry) -> tuple:
    return (core.canonical(geometry) if geometry is not None else None, *bbox(geometry))


def _unknown(fields, known) -> list:
    return sorted(set(fields) - set(known))


# --- Shapefile reader and Kansas subsets ----------------------------------------------------------

class Albers:
    """Inverse of the ellipsoidal Albers equal-area conic (Snyder 1987, 14-19 to 14-21 and 3-16)."""

    def __init__(self, a: float, inverse_flattening: float, lat1: float, lat2: float, lat0: float, lon0: float,
                 false_easting: float = 0.0, false_northing: float = 0.0):
        f = 1.0 / inverse_flattening
        self.a, self.e2 = a, 2 * f - f * f
        self.e = math.sqrt(self.e2)
        self.lon0, self.x0, self.y0 = math.radians(lon0), false_easting, false_northing
        p1, p2, p0 = (math.radians(v) for v in (lat1, lat2, lat0))
        m1, m2 = self._m(p1), self._m(p2)
        q1, q2, q0 = self._q(p1), self._q(p2), self._q(p0)
        self.n = (m1 * m1 - m2 * m2) / (q2 - q1) if abs(p1 - p2) > 1e-12 else math.sin(p1)
        self.c = m1 * m1 + self.n * q1
        self.rho0 = a * math.sqrt(self.c - self.n * q0) / self.n

    def _m(self, phi):
        s = math.sin(phi)
        return math.cos(phi) / math.sqrt(1 - self.e2 * s * s)

    def _q(self, phi):
        s, e = math.sin(phi), self.e
        return (1 - self.e2) * (s / (1 - self.e2 * s * s) - math.log((1 - e * s) / (1 + e * s)) / (2 * e))

    def inverse(self, x: float, y: float) -> tuple:
        """(lon, lat) in degrees of a projected point in metres."""
        x, y, n = x - self.x0, y - self.y0, self.n
        rho = math.hypot(x, self.rho0 - y)
        theta = math.atan2(x * (1 if n >= 0 else -1), (self.rho0 - y) * (1 if n >= 0 else -1))
        q = (self.c - rho * rho * n * n / (self.a * self.a)) / n
        phi = math.asin(max(-1.0, min(1.0, q / 2)))
        e, e2 = self.e, self.e2
        for _ in range(30):
            s = math.sin(phi)
            if abs(abs(q) - (1 - (1 - e2) / (2 * e) * math.log((1 - e) / (1 + e)))) < 1e-12:
                phi = math.copysign(math.pi / 2, q)
                break
            step = ((1 - e2 * s * s) ** 2 / (2 * math.cos(phi))) * (q / (1 - e2) - s / (1 - e2 * s * s)
                                                                      + math.log((1 - e * s) / (1 + e * s)) / (2 * e))
            phi += step
            if abs(step) < 1e-12:
                break
        return math.degrees(self.lon0 + theta / n), math.degrees(phi)


def _prj_projection(text: str):
    """None for geographic NAD83/WGS84, an Albers for the ESRI Albers equal-area conic; else FeedError."""
    if not re.match(r'\s*GEOGCS\[', text):
        if not re.match(r'\s*PROJCS\[', text) or not re.search(r'PROJECTION\["Albers"\]', text):
            raise FeedError(f"SHAPEFILE_PROJECTION_UNSUPPORTED {text[:60]}")
    spheroid = re.search(r'SPHEROID\["[^"]*",([-0-9.eE]+),([-0-9.eE]+)\]', text)
    if not spheroid or not re.search(r'DATUM\["D_(North_American_1983|WGS_1984)"', text):
        raise FeedError(f"SHAPEFILE_DATUM_UNSUPPORTED {text[:60]}")
    if re.match(r'\s*GEOGCS\[', text):
        return None
    params = {m.group(1): float(m.group(2)) for m in re.finditer(r'PARAMETER\["([A-Za-z_0-9]+)",([-0-9.eE]+)\]', text)}
    try:
        return Albers(float(spheroid.group(1)), float(spheroid.group(2)), params["Standard_Parallel_1"], params["Standard_Parallel_2"],
                      params["Latitude_Of_Origin"], params["Central_Meridian"], params.get("False_Easting", 0.0),
                      params.get("False_Northing", 0.0))
    except KeyError as missing:
        raise FeedError(f"SHAPEFILE_PROJECTION_UNSUPPORTED missing {missing}") from None


def _ring_area(ring) -> float:
    return sum(ax * by - bx * ay for (ax, ay), (bx, by) in zip(ring, ring[1:])) / 2


def _polygons(rings) -> dict:
    """Shapefile rings (outer clockwise, holes counter-clockwise) as GeoJSON Polygon or MultiPolygon with RFC
    7946 orientation; each hole goes to the smallest outer ring that contains it."""
    outers, holes = [], []
    for ring in rings:
        (holes if _ring_area(ring) > 0 else outers).append(ring)
    if not outers:
        outers, holes = holes, []
    polygons = [[list(reversed(outer))] for outer in outers]
    for hole in holes:
        x, y = hole[0]
        inside = [i for i, outer in enumerate(outers) if _inside(outer, x, y)]
        if inside:
            polygons[min(inside, key=lambda i: abs(_ring_area(outers[i])))].append(list(reversed(hole)))
        else:
            polygons.append([hole])
    return {"type": "Polygon", "coordinates": polygons[0]} if len(polygons) == 1 else {"type": "MultiPolygon", "coordinates": polygons}


class Shapefile:
    """An ESRI shapefile set read from a zip (``read_shapefile``). Records are kept as bytes so a subset can be
    written back byte for byte."""

    SHAPES = {0: "Null", 1: "Point", 3: "PolyLine", 5: "Polygon", 8: "MultiPoint", 11: "Point", 13: "PolyLine", 15: "Polygon",
              18: "MultiPoint", 21: "Point", 23: "PolyLine", 25: "Polygon", 28: "MultiPoint"}

    def __init__(self, members: dict, stem: str, code: str):
        self.members, self.stem, self.code = members, stem, code
        for ext in (".shp", ".shx", ".dbf", ".prj"):
            if stem + ext not in members:
                raise FeedError(f"{code}_MEMBER_MISSING {ext}")
        shp, dbf = members[stem + ".shp"], members[stem + ".dbf"]
        if len(shp) < 100 or struct.unpack(">i", shp[:4])[0] != 9994:
            raise FeedError(f"{code}_SHAPEFILE_INVALID header")
        self.shape_type = struct.unpack("<i", shp[32:36])[0]
        if self.shape_type not in self.SHAPES:
            raise FeedError(f"{code}_SHAPEFILE_INVALID shape type {self.shape_type}")
        self.records, offset = [], 100
        while offset + 8 <= len(shp):
            _, words = struct.unpack(">ii", shp[offset:offset + 8])
            if offset + 8 + 2 * words > len(shp):
                raise FeedError(f"{code}_SHAPEFILE_INVALID truncated record")
            self.records.append(shp[offset + 8:offset + 8 + 2 * words])
            offset += 8 + 2 * words
        self.dbf_header, self.fields = dbf[:32], []
        count, header_length, record_length = struct.unpack("<IHH", dbf[4:12])
        position = 32
        while position < header_length - 1 and dbf[position] != 0x0D:
            name = dbf[position:position + 11].split(b"\0")[0].decode("ascii", "replace")
            self.fields.append((name, chr(dbf[position + 11]), dbf[position + 16], dbf[position + 17]))
            position += 32
        self.record_length = record_length
        self.rows = [dbf[header_length + i * record_length:header_length + (i + 1) * record_length] for i in range(count)]
        if len(self.rows) != len(self.records) or any(len(r) != record_length for r in self.rows):
            raise FeedError(f"{code}_SHAPEFILE_INVALID dbf and shp disagree")
        cpg = members.get(stem + ".cpg")
        self.encodings = [cpg.decode("ascii", "replace").strip()] if cpg else ["utf-8", "cp1252", "latin-1"]
        self.projection = _prj_projection(members[stem + ".prj"].decode("ascii", "replace"))

    def __len__(self):
        return len(self.records)

    def _text(self, raw: bytes) -> str:
        for encoding in self.encodings:
            try:
                return raw.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                continue
        raise FeedError(f"{self.code}_ENCODING_CHANGED")

    def attributes(self, index: int) -> dict:
        """The dBase values of record index: C text (right-trimmed, empty as None), N/F numbers, D ISO dates, L booleans."""
        row, position, out = self.rows[index], 1, {}
        for name, kind, length, _ in self.fields:
            raw = row[position:position + length]
            position += length
            if kind == "C":
                text = self._text(raw).rstrip()
                out[name] = text or None
            elif kind in ("N", "F"):
                text = raw.decode("ascii", "replace").strip()
                try:
                    out[name] = None if text in ("", "*" * len(text)) else int(text) if re.fullmatch(r"[-+]?\d+", text) else float(text)
                except ValueError:
                    raise FeedError(f"{self.code}_NOT_A_NUMBER {name} {text[:20]!r}") from None
            elif kind == "D":
                text = raw.decode("ascii", "replace").strip()
                out[name] = f"{text[:4]}-{text[4:6]}-{text[6:8]}" if re.fullmatch(r"\d{8}", text) else None
            elif kind == "L":
                flag = raw[:1].decode("ascii", "replace").upper()
                out[name] = True if flag in "TY" and flag else False if flag in "FN" and flag else None
            else:
                out[name] = self._text(raw).rstrip() or None
        return out

    def deleted(self, index: int) -> bool:
        return self.rows[index][:1] == b"*"

    def _coordinates(self, record: bytes, offset: int, count: int) -> list:
        values = struct.unpack_from(f"<{2 * count}d", record, offset)
        points = zip(values[0::2], values[1::2])
        if self.projection is not None:
            points = (self.projection.inverse(x, y) for x, y in points)
        return [[round(x, 7), round(y, 7)] for x, y in points]

    def geometry(self, index: int):
        """GeoJSON geometry of record index in lon/lat (7 decimals), None for a null shape."""
        record = self.records[index]
        kind = struct.unpack_from("<i", record, 0)[0]
        if kind == 0:
            return None
        if kind not in self.SHAPES:
            raise FeedError(f"{self.code}_SHAPEFILE_INVALID record shape type {kind}")
        name = self.SHAPES[kind]
        if name == "Point":
            return {"type": "Point", "coordinates": self._coordinates(record, 4, 1)[0]}
        if name == "MultiPoint":
            count = struct.unpack_from("<i", record, 36)[0]
            return {"type": "MultiPoint", "coordinates": self._coordinates(record, 40, count)}
        parts, count = struct.unpack_from("<ii", record, 36)
        starts = list(struct.unpack_from(f"<{parts}i", record, 44)) + [count]
        points = self._coordinates(record, 44 + 4 * parts, count)
        pieces = [points[a:b] for a, b in zip(starts, starts[1:])]
        if name == "PolyLine":
            return {"type": "LineString", "coordinates": pieces[0]} if len(pieces) == 1 else {"type": "MultiLineString", "coordinates": pieces}
        return _polygons(pieces)

    def subset(self, indices) -> bytes:
        """A zip holding the shapefile set of the given records (renumbered from 1, the records themselves copied
        byte for byte), with ``.prj``, ``.cpg`` and ``.shp.xml`` carried along, stored with fixed timestamps."""
        indices = list(indices)
        shp, shx, offset = [], [], 50
        for number_, index in enumerate(indices, 1):
            record = self.records[index]
            words = len(record) // 2
            shp.append(struct.pack(">ii", number_, words) + record)
            shx.append(struct.pack(">ii", offset, words))
            offset += 4 + words
        west = south = math.inf
        east = north = -math.inf
        for index in indices:
            record = self.records[index]
            kind = struct.unpack_from("<i", record, 0)[0]
            if kind == 0:
                continue
            if self.SHAPES[kind] == "Point":
                x, y = struct.unpack_from("<dd", record, 4)
                x0, y0, x1, y1 = x, y, x, y
            else:
                x0, y0, x1, y1 = struct.unpack_from("<4d", record, 4)
            west, south, east, north = min(west, x0), min(south, y0), max(east, x1), max(north, y1)
        if west is math.inf:
            west = south = east = north = 0.0

        def header(length_words: int) -> bytes:
            return (struct.pack(">i5i", 9994, 0, 0, 0, 0, 0) + struct.pack(">i", length_words) + struct.pack("<ii", 1000, self.shape_type)
                    + struct.pack("<8d", west, south, east, north, 0.0, 0.0, 0.0, 0.0))
        shp_bytes = header(50 + sum(len(r) // 2 for r in shp)) + b"".join(shp)
        shx_bytes = header(50 + 4 * len(shx)) + b"".join(shx)
        descriptors = b"".join(name.encode("ascii").ljust(11, b"\0") + kind.encode("ascii") + b"\0" * 4 + bytes([length, decimals]) + b"\0" * 14
                               for name, kind, length, decimals in self.fields)
        header_length = 32 + len(descriptors) + 1
        dbf_bytes = (self.dbf_header[:4] + struct.pack("<IHH", len(indices), header_length, self.record_length) + b"\0" * 20
                     + descriptors + b"\x0D" + b"".join(self.rows[i] for i in indices) + b"\x1A")
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as archive:
            for ext, data in ((".shp", shp_bytes), (".shx", shx_bytes), (".dbf", dbf_bytes), (".prj", None), (".cpg", None), (".shp.xml", None)):
                if data is None:
                    data = self.members.get(self.stem + ext)
                    if data is None:
                        continue
                info = zipfile.ZipInfo(self.stem + ext, (1980, 1, 1, 0, 0, 0))
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, data)
        return out.getvalue()


def read_shapefile(source, code: str = "SHAPEFILE") -> Shapefile:
    """The shapefile set in a zip (bytes or a path): the one ``.shp`` and its sidecars; ``__MACOSX`` entries ignored."""
    try:
        with zipfile.ZipFile(io.BytesIO(source) if isinstance(source, bytes) else source) as archive:
            members = {}
            for info in archive.infolist():
                name = info.filename
                if name.startswith("__MACOSX/") or Path(name).name.startswith("._") or name.endswith("/"):
                    continue
                members[name] = archive.read(name)
    except (zipfile.BadZipFile, OSError) as error:
        raise FeedError(f"{code}_ZIP_INVALID {error}") from None
    stems = [n[:-4] for n in members if n.endswith(".shp")]
    if len(stems) != 1:
        raise FeedError(f"{code}_ZIP_INVALID {len(stems)} shapefiles")
    return Shapefile(members, stems[0], code)


def _dbf_types(fields) -> dict:
    """Column types from dBase field descriptors."""
    return {column(name): ("REAL" if kind == "F" or decimals else "INTEGER") if kind in ("N", "F") else "TEXT" for name, kind, _, decimals in fields}


# --- GNIS: USGS Geographic Names Information System -----------------------------------------------

GNIS = "https://prd-tnm.s3.amazonaws.com/"
GNIS_PREFIX = "StagedProducts/GeographicNames/"
GNIS_TERMS = "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits"
GNIS_LICENSE = "Public domain (U.S. Government work); acknowledgment of the U.S. Geological Survey is requested"
GNIS_RECHECK_DAYS = 6
GNIS_LIMIT = 512_000_000
GNIS_NAMES_HEADER = ["feature_id", "feature_name", "feature_class", "state_name", "state_numeric", "county_name", "county_numeric", "map_name",
                     "date_created", "date_edited", "bgn_type", "bgn_authority", "bgn_date", "prim_lat_dms", "prim_long_dms", "prim_lat_dec",
                     "prim_long_dec", "source_lat_dms", "source_long_dms", "source_lat_dec", "source_long_dec"]
GNIS_2021_HEADER = ["FEATURE_ID", "FEATURE_NAME", "FEATURE_CLASS", "STATE_ALPHA", "STATE_NUMERIC", "COUNTY_NAME", "COUNTY_NUMERIC",
                    "PRIMARY_LAT_DMS", "PRIM_LONG_DMS", "PRIM_LAT_DEC", "PRIM_LONG_DEC", "SOURCE_LAT_DMS", "SOURCE_LONG_DMS", "SOURCE_LAT_DEC",
                    "SOURCE_LONG_DEC", "ELEV_IN_M", "ELEV_IN_FT", "MAP_NAME", "DATE_CREATED", "DATE_EDITED"]
GNIS_UNITS_HEADER = ["feature_id", "unit_type", "county_numeric", "county_name", "state_numeric", "state_alpha", "state_name", "country_alpha",
                     "country_name", "feature_name"]
GNIS_ALL_NAMES_HEADER = ["feature_id", "feature_name", "feature_name_official", "sourcecitationabbreviation", "sourceoriginator", "sourcereftype",
                         "title", "edition", "sourceurl", "publicationdate", "seriesname", "seriesissue", "ending_date", "date_created", "citation"]
GNIS_DESCRIPTION_HEADER = ["feature_id", "description", "history"]
GNIS_COORDINATES = {"prim_lat_dec", "prim_long_dec", "source_lat_dec", "source_long_dec"}
GNIS_TYPES = {"feature_id": "INTEGER", "elev_in_m": "INTEGER", "elev_in_ft": "INTEGER", **{c: "REAL" for c in GNIS_COORDINATES}}
# slug: (S3 key under GNIS_PREFIX, zip member or None for a plain text file, header, quoted values, kansas rule, table, indexes)
# kansas rule: "whole", "state" (state_numeric 20), "state_or_ids", "ids" (feature id in the names tables), "ids_2021"
GNIS_FILES = {
    "names": ("DomesticNames/DomesticNames_KS_Text.zip", "Text/DomesticNames_KS.txt", GNIS_NAMES_HEADER, True, "whole", "kfm_gnis_names",
              [("county_numeric", "feature_class"), ("feature_id",), ("feature_name",)]),
    "names-2021": ("Archive/MainDomestic/KS_Features_20210825.txt", None, GNIS_2021_HEADER, False, "whole", "kfm_gnis_names_2021",
                   [("county_numeric", "feature_class"), ("feature_id",), ("feature_name",)]),
    "government-units": ("Topical/GovernmentUnits_National_Text.zip", "Text/GovernmentUnits_National.txt", GNIS_UNITS_HEADER, True, "state",
                         "kfm_gnis_government_units", [("feature_id",)]),
    "historical-features": ("Topical/HistoricalFeatures_National_Text.zip", "Text/HistoricalFeatures_National.txt", GNIS_NAMES_HEADER, True,
                            "state_or_ids", "kfm_gnis_historical_features", [("feature_id",)]),
    "all-names": ("Topical/AllNames_National_Text.zip", "Text/AllNames_National.txt", GNIS_ALL_NAMES_HEADER, True, "ids", "kfm_gnis_all_names",
                  [("feature_id",), ("feature_name",)]),
    "descriptions": ("Topical/FeatureDescriptionHistory_National_Text.zip", "Text/FeatureDescriptionHistory_National.txt", GNIS_DESCRIPTION_HEADER,
                     True, "ids", "kfm_gnis_feature_descriptions", [("feature_id",)]),
    "descriptions-2021": ("Archive/TopicalGazetteers/Feature_Description_History.zip", "Feature_Description_History_20210825.txt",
                          [h.upper() for h in GNIS_DESCRIPTION_HEADER], False, "ids_2021", "kfm_gnis_feature_descriptions_2021", [("feature_id",)]),
}
GNIS_DDL = "".join(ddl(table, [column(h) for h in header], GNIS_TYPES, indexes) for _, _, header, _, _, table, indexes in GNIS_FILES.values())
GNIS_KANSAS = {"whole": "whole file (USGS's Kansas file)", "state": "state_numeric=20",
               "state_or_ids": "state_numeric=20 or feature_id in kfm_gnis_names, kfm_gnis_names_2021",
               "ids": "feature_id in kfm_gnis_names, kfm_gnis_names_2021", "ids_2021": "feature_id in kfm_gnis_names_2021"}
BOM = b"\xef\xbb\xbf"
S3 = "{http://s3.amazonaws.com/doc/2006-03-01/}"


def _gnis_listing(ctx, key: str) -> dict:
    """{bytes, etag, last_modified} of one object from the bucket listing, or None when it is not listed."""
    body = _fetch(ctx, f"{GNIS}?prefix={urllib.parse.quote(GNIS_PREFIX + key)}", "GNIS", limit=16_000_000).body
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        raise FeedError(f"GNIS_LISTING_CHANGED {key}") from None
    if root.tag != S3 + "ListBucketResult":
        raise FeedError(f"GNIS_LISTING_CHANGED {key}")
    for entry in root.iter(S3 + "Contents"):
        if entry.findtext(S3 + "Key") == GNIS_PREFIX + key:
            try:
                return {"bytes": int(entry.findtext(S3 + "Size")), "etag": entry.findtext(S3 + "ETag").strip('"'),
                        "last_modified": entry.findtext(S3 + "LastModified")}
            except (TypeError, ValueError, AttributeError):
                raise FeedError(f"GNIS_LISTING_CHANGED {key}") from None
    return None


def _gnis_records(handle, quoted: bool):
    """The CRLF-ended records of a GNIS text stream, bytes, a record spanning lines when a quoted value holds
    line breaks (the current exports); the 2021 archive never quotes."""
    pending = b""
    for line in handle:
        pending += line
        if not quoted or pending.count(b'"') % 2 == 0:
            yield pending
            pending = b""
    if pending:
        yield pending


def _gnis_fields(record: bytes, quoted: bool) -> list:
    text = record.removeprefix(BOM).decode("utf-8").rstrip("\r\n")
    if quoted:
        return next(csv.reader([text], delimiter="|", quotechar='"'))
    return text.split("|")


def _gnis_cut(handle, header: list, quoted: bool, keep) -> tuple:
    """(kept bytes, rows) of a GNIS text stream: the header record and the records keep() accepts, byte for byte."""
    records = _gnis_records(handle, quoted)
    first = next(records, None)
    if first is None or _gnis_fields(first, quoted) != header:
        raise FeedError("GNIS_COLUMNS_CHANGED")
    out, rows = [first], 0
    for record in records:
        fields = _gnis_fields(record, quoted)
        if len(fields) != len(header):
            raise FeedError(f"GNIS_ROW_SHAPE {fields[0][:20]!r}")
        if keep(fields):
            out.append(record)
            rows += 1
    return b"".join(out), rows


def _gnis_rows(path: Path, header: list, quoted: bool):
    columns = [column(h) for h in header]
    with gzip.open(path, "rb") as handle:
        records = _gnis_records(handle, quoted)
        if _gnis_fields(next(records, b""), quoted) != header:
            raise FeedError(f"GNIS_COLUMNS_CHANGED {path.name}")
        for record in records:
            fields = _gnis_fields(record, quoted)
            if len(fields) != len(header):
                raise FeedError(f"GNIS_ROW_SHAPE {path.name}")
            yield tuple(_gnis_value(c, v) for c, v in zip(columns, fields))


def _gnis_value(name: str, value: str):
    if name not in GNIS_TYPES:
        return value
    try:
        parsed = number(value)
    except FeedError:
        raise FeedError(f"GNIS_NOT_A_NUMBER {name} {value[:20]!r}") from None
    return None if name in GNIS_COORDINATES and parsed == 0 else parsed


def _gnis_ids(db, tables) -> tuple:
    """(sorted feature ids, their SHA-256 as 'id,id,...') from the loaded names tables."""
    ids = set()
    for table in tables:
        ids.update(i for (i,) in db.execute(f"SELECT feature_id FROM {table} WHERE feature_id IS NOT NULL"))
    ids = sorted(ids)
    return ids, hashlib.sha256(",".join(str(i) for i in ids).encode()).hexdigest()


def gnis_names(ctx, max_files: int = 7) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(GNIS_DDL)
        state, today = core.get_state(db, "gnis-names"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < GNIS_RECHECK_DAYS:
            return {"state": "not_due", "checked": state["checked"]}
        files, summary, missing, handled = dict(state.get("files", {})), {"files": [], "loaded": [], "unchanged": [], "empty": [], "rows": 0}, [], 0
        for slug, (key, member, header, quoted, rule, table, _) in GNIS_FILES.items():
            if handled >= max_files:
                break
            listed = _gnis_listing(ctx, key)
            if listed is None:
                missing.append(slug)
                continue
            ids, ids_sha = (None, None)
            if rule in ("state_or_ids", "ids", "ids_2021"):
                ids, ids_sha = _gnis_ids(db, ["kfm_gnis_names_2021"] if rule == "ids_2021" else ["kfm_gnis_names", "kfm_gnis_names_2021"])
                ids = set(ids)
            before = files.get(slug, {})
            if all(before.get(k) == listed[k] for k in ("bytes", "etag", "last_modified")) and before.get("ids") == ids_sha:
                summary["unchanged"].append(slug)
                continue
            handled += 1
            url = GNIS + GNIS_PREFIX + key
            full = core.temp_path(ctx, f"gnis-{slug}")
            try:
                fetched = _download(ctx, url, full, "GNIS", limit=GNIS_LIMIT, timeout=1800)
                if full.stat().st_size != listed["bytes"]:
                    raise FeedError(f"GNIS_DOWNLOAD_MISMATCH {key} size")
                if "-" not in listed["etag"] and hashlib.md5(full.read_bytes()).hexdigest() != listed["etag"]:
                    raise FeedError(f"GNIS_DOWNLOAD_MISMATCH {key} md5")
                keep = {"whole": lambda f: True, "state": lambda f: f[4] == "20",
                        "state_or_ids": lambda f: f[4] == "20" or (f[0].isdigit() and int(f[0]) in ids),
                        "ids": lambda f: f[0].isdigit() and int(f[0]) in ids, "ids_2021": lambda f: f[0].isdigit() and int(f[0]) in ids}[rule]
                if member is None:
                    with open(full, "rb") as handle:
                        kept, rows = _gnis_cut(handle, header, quoted, keep)
                else:
                    try:
                        with zipfile.ZipFile(full) as archive:
                            if member not in archive.namelist():
                                raise FeedError(f"GNIS_ZIP_CHANGED {key} {member}")
                            with archive.open(member) as handle:
                                kept, rows = _gnis_cut(handle, header, quoted, keep)
                    except zipfile.BadZipFile:
                        raise FeedError(f"GNIS_ZIP_INVALID {key}") from None
                if not rows:
                    if key in loaded_keys(db, f"gnis-{slug}"):
                        raise FeedError(f"GNIS_KANSAS_EMPTY {key}")
                    summary["empty"].append(slug)
                else:
                    stem = Path(member or key).name.split(".")[0]
                    name = f"{slug}/{stem}-{ctx_sha12(kept)}" if False else f"{slug}/{stem}{'' if rule == 'whole' else '-KS'}"
                    citation = (f"U.S. Geological Survey, Geographic Names Information System (GNIS), {Path(key).name}, "
                                f"{listed['last_modified'][:10]}, {url}")
                    result = keep_version(ctx, db, feed="gnis-names", source_id=f"gnis-{slug}", key=key, name=name, ext=".txt.gz",
                                          body=core.gz(kept), url=url, fetched=fetched, original=full, table=table, width=len(header),
                                          rows=lambda path, h=header, q=quoted: _gnis_rows(path, h, q),
                                          extra={"citation": citation, "kansas": GNIS_KANSAS[rule], "kansas_ids_sha256": ids_sha, "license": GNIS_LICENSE,
                                                 "listed": listed, "member": member, "rows": rows, "s3_key": GNIS_PREFIX + key, "terms": GNIS_TERMS})
                    summary["loaded" if result["state"] != "unchanged" else "unchanged"].append(slug)
                    summary["rows"] += result["rows"]
            finally:
                full.unlink(missing_ok=True)
            summary["files"].append(slug)
            files[slug] = {**listed, "fetched": str(today), "ids": ids_sha, "rows": rows}
            state = save_state(ctx, db, "gnis-names", {**state, "files": files})
        if missing:
            raise FeedError(f"GNIS_FILE_MISSING {' '.join(missing)}")
        if handled < max_files or len(summary["files"]) + len(summary["unchanged"]) == len(GNIS_FILES):
            state = save_state(ctx, db, "gnis-names", {**state, "checked": str(today)})
        return summary
    finally:
        db.close()


def ctx_sha12(data: bytes) -> str:   # kept for symmetry with keep_version's naming; the name is built by keep_version itself
    return core.sha256(data)[:12]


# --- Post offices: Blevins & Helbock on Harvard Dataverse -----------------------------------------

DATAVERSE = "https://dataverse.harvard.edu/api/"
POST_OFFICES_DOI = "doi:10.7910/DVN/NUKCNA"
POST_OFFICES_FILE = "us-post-offices.tab"
POST_OFFICES_ABOUT = "https://cblevins.github.io/us-post-offices/"
POST_OFFICES_RECHECK_DAYS = 28
POST_OFFICES_HEADER = ["Name", "AltName", "OrigName", "State", "County1", "County2", "County3", "OrigCounty", "Established", "Discontinued",
                       "Continuous", "StampIndex", "ID", "Coordinates", "Duration", "GNIS.Match", "GNIS.Name", "GNIS.County", "GNIS.State",
                       "GNIS.FEATURE_ID", "GNIS.Feature.Class", "GNIS.OrigName", "GNIS.OrigCounty", "GNIS.Latitude", "GNIS.Longitude",
                       "GNIS.ELEV_IN_M", "GNIS.Dist", "Latitude", "Longitude"]
POST_OFFICES_COLUMNS = [column(h) for h in POST_OFFICES_HEADER]
POST_OFFICES_TYPES = {"established": "INTEGER", "discontinued": "INTEGER", "id": "INTEGER", "duration": "INTEGER", "gnis_feature_id": "INTEGER",
                      "gnis_latitude": "REAL", "gnis_longitude": "REAL", "gnis_elev_in_m": "INTEGER", "gnis_dist": "REAL", "latitude": "REAL",
                      "longitude": "REAL"}
POST_OFFICES_TABLE = "kfm_blevins_post_offices"
POST_OFFICES_DDL = ddl(POST_OFFICES_TABLE, POST_OFFICES_COLUMNS, POST_OFFICES_TYPES, [("county1",), ("gnis_feature_id",), ("name",)])


def _post_office_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        if next(reader, None) != POST_OFFICES_HEADER:
            raise FeedError(f"POST_OFFICES_COLUMNS_CHANGED {path.name}")
        for row in reader:
            if len(row) != len(POST_OFFICES_HEADER):
                raise FeedError(f"POST_OFFICES_ROW_SHAPE {path.name}")
            values = []
            for name, value in zip(POST_OFFICES_COLUMNS, row):
                if name in POST_OFFICES_TYPES:
                    try:
                        value = number(value)
                    except FeedError:
                        raise FeedError(f"POST_OFFICES_NOT_A_NUMBER {name} {value[:20]!r}") from None
                values.append(value)
            yield tuple(values)


def post_offices(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(POST_OFFICES_DDL)
        state, today = core.get_state(db, "post-offices"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < POST_OFFICES_RECHECK_DAYS:
            return {"state": "not_due", "checked": state["checked"]}
        try:
            payload = json.loads(_fetch(ctx, f"{DATAVERSE}datasets/:persistentId?persistentId={POST_OFFICES_DOI}", "POST_OFFICES", limit=16_000_000).body)
            version = payload["data"]["latestVersion"]
            files = {f["dataFile"]["filename"]: f["dataFile"] for f in version["files"]}
            license_ = version.get("license") or {}
            dataset_version = f"{version['versionNumber']}.{version.get('versionMinorNumber', 0)}"
            published = str(version.get("publicationDate") or version.get("releaseTime") or "")[:4]
        except (ValueError, KeyError, TypeError, AttributeError):
            raise FeedError("POST_OFFICES_RESPONSE_SHAPE") from None
        if "zero/1.0" not in str(license_.get("uri", "")) and license_.get("name") != "CC0 1.0":
            raise FeedError(f"POST_OFFICES_LICENSE_CHANGED {license_.get('name')!r}")
        if POST_OFFICES_FILE not in files:
            raise FeedError(f"POST_OFFICES_FILE_MISSING {POST_OFFICES_FILE}")
        datafile = files[POST_OFFICES_FILE]
        checksum = datafile.get("checksum") or {"type": "MD5", "value": datafile.get("md5")}
        if state.get("checksum") == checksum.get("value") and state.get("datafile_id") == datafile.get("id"):
            save_state(ctx, db, "post-offices", {**state, "checked": str(today), "version": dataset_version})
            return {"state": "unchanged", "rows": 0, "checksum": checksum.get("value")}
        url = f"{DATAVERSE}access/datafile/{datafile['id']}?format=original"
        full = core.temp_path(ctx, "us-post-offices.csv")
        try:
            fetched = _download(ctx, url, full, "POST_OFFICES", limit=512_000_000, timeout=1800)
            if checksum.get("type") == "MD5" and hashlib.md5(full.read_bytes()).hexdigest() != checksum.get("value"):
                raise FeedError("POST_OFFICES_CHECKSUM_MISMATCH")
            out, rows, header = [], 0, None
            with open(full, "rb") as handle:
                for line in handle:
                    if header is None:
                        header = next(csv.reader([line.decode("utf-8").rstrip("\r\n")]))
                        if header != POST_OFFICES_HEADER:
                            raise FeedError("POST_OFFICES_COLUMNS_CHANGED")
                        out.append(line)
                        continue
                    if not line.strip():
                        continue
                    fields = next(csv.reader([line.decode("utf-8").rstrip("\r\n")]))
                    if len(fields) != len(POST_OFFICES_HEADER):
                        raise FeedError("POST_OFFICES_ROW_SHAPE")
                    if fields[3] == "KS":
                        out.append(line)
                        rows += 1
            if not rows:
                raise FeedError("POST_OFFICES_NO_KANSAS_ROWS")
            citation = (f'Blevins, Cameron; Helbock, Richard W., {published}, "US Post Offices", https://doi.org/10.7910/DVN/NUKCNA, '
                        f"Harvard Dataverse, V{version['versionNumber']}")
            result = keep_version(ctx, db, feed="post-offices", source_id="blevins-post-offices", key="us-post-offices",
                                  name="us-post-offices/us-post-offices-KS", ext=".csv.gz", body=core.gz(b"".join(out)), url=url, fetched=fetched,
                                  original=full, table=POST_OFFICES_TABLE, width=len(POST_OFFICES_HEADER), rows=_post_office_rows,
                                  extra={"about": POST_OFFICES_ABOUT, "checksum": checksum, "citation": citation, "datafile_id": datafile["id"],
                                         "dataset": POST_OFFICES_DOI, "dataset_version": dataset_version, "kansas": "State is KS",
                                         "license": license_.get("name", "CC0 1.0"), "rows": rows, "terms": "https://doi.org/10.7910/DVN/NUKCNA"})
        finally:
            full.unlink(missing_ok=True)
        save_state(ctx, db, "post-offices", {"checked": str(today), "checksum": checksum.get("value"), "datafile_id": datafile["id"],
                                             "rows": rows, "version": dataset_version})
        return {**result, "kansas": rows}
    finally:
        db.close()


# --- Zip-download feeds: a 28-day check by SHA-256 ---------------------------------------------------

SHAPES_RECHECK_DAYS = 28


def _due(state: dict, today: date, days: int = SHAPES_RECHECK_DAYS) -> bool:
    age = age_days(state, "checked", today)
    return age is None or age >= days


def _download_record(fetched, path: Path, url: str, digest: str) -> dict:
    return {"bytes": path.stat().st_size, "etag": fetched.etag, "last_modified": fetched.last_modified, "sha256": digest, "url": url}


# --- County boundaries: Newberry's Atlas of Historical County Boundaries, Kansas -----------------

AHCB_URL = "https://digital.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip"
AHCB_TERMS = "https://digital.newberry.org/ahcb/download"
AHCB_CITATION = ("Sinko, Peggy Tuck. Kansas Historical Counties. Data Set. Laura Rico-Beck, digital comp. Atlas of Historical County "
                 "Boundaries, ed. by John H. Long. Chicago: The Newberry Library, 2010. Available online from http://www.newberry.org/ahcbp.")
AHCB_STEM = "KS_AtlasHCB/KS_Historical_Counties/KS_Historical_Counties"
AHCB_DATABASE = "KS_AtlasHCB/KS_Comprehensive_Database/KS_Comprehensive_Database.txt"
AHCB_CHRONOLOGIES = {"consolidated": "KS_AtlasHCB/KS_Supplemental_Texts/KS_Consolidated_Chronology.htm",
                     "individual": "KS_AtlasHCB/KS_Supplemental_Texts/KS_Individual_County_Chronologies.htm"}
AHCB_DEED = "KS_AtlasHCB/zCreativeCommonsLicense/CreativeCommonsDeed.htm"
AHCB_METADATA = "KS_AtlasHCB/KS_Supplemental_Texts/KS_Metadata1.htm"
AHCB_VERSION_FIELDS = ["NAME", "ID", "STATE", "FIPS", "VERSION", "START_DATE", "END_DATE", "CHANGE", "CITATION", "START_N", "END_N", "AREA_SQMI",
                       "DATASET", "CNTY_TYPE", "FULL_NAME"]
AHCB_VERSION_TYPES = {"version": "INTEGER", "start_n": "INTEGER", "end_n": "INTEGER", "area_sqmi": "REAL"}
AHCB_CHANGE_HEADER = ["FIPS", "STATE", "NAME", "ID", "VERSION", "START_DATE", "END_DATE", "CREATION_OR_CHANGE", "CITATION", "START_N", "END_N", "DATASET"]
AHCB_CHANGE_TYPES = {"version": "INTEGER", "start_n": "INTEGER", "end_n": "INTEGER"}
AHCB_CHRONOLOGY_COLUMNS = ["chronology", "subject", "entry_date", "date_iso", "sub_entry", "change", "citation"]
AHCB_DDL = (qddl("kfm_ahcb_county_versions", [(column(f), AHCB_VERSION_TYPES.get(column(f), "TEXT")) for f in AHCB_VERSION_FIELDS]
                 + [("in_kansas", "INTEGER")] + GEOMETRY_COLUMNS, [("fips",), ("id", "version"), ("start_date", "end_date")])
            + qddl("kfm_ahcb_changes", [(column(f), AHCB_CHANGE_TYPES.get(column(f), "TEXT")) for f in AHCB_CHANGE_HEADER],
                   [("fips",), ("id", "version"), ("start_n",)])
            + qddl("kfm_ahcb_chronology", [(c, "INTEGER" if c == "sub_entry" else "TEXT") for c in AHCB_CHRONOLOGY_COLUMNS],
                   [("date_iso",), ("subject", "date_iso")]))
MONTHS = {m: i for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"), 1)}


def _plain(fragment: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def _page_text(raw: bytes) -> str:
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def date_iso(text: str):
    """"30 April 1803", "25 Aug 1855" -> 1803-04-30; "Jul 1887" -> 1887-07; "by 1959" -> 1959; else None."""
    found = re.fullmatch(r"(?:(\d{1,2}) )?([A-Za-z]+)\.? (\d{4})", text.strip())
    if found and found.group(2)[:3].lower() in MONTHS:
        day, month, year = found.group(1), MONTHS[found.group(2)[:3].lower()], found.group(3)
        return f"{year}-{month:02d}-{int(day):02d}" if day else f"{year}-{month:02d}"
    found = re.search(r"\b(\d{4})\b", text)
    return found.group(1) if found else None


def _ahcb_event(fragment: str) -> tuple:
    """(change, citation) of an event's inner HTML."""
    change, _, citation = fragment.partition("<span class='citation'>")
    change = change.split("<span class='change'>", 1)[-1]
    return _plain(change) or None, _plain(citation) or None


def ahcb_consolidated(raw: bytes) -> list:
    """Rows of the consolidated chronology: (chronology, subject, entry_date, date_iso, sub_entry, change, citation)."""
    text = _page_text(raw)
    rows, current, sub, depth = [], None, 0, 0
    for match in re.finditer(r"<p class='eventdate'>(.*?)</p>|<p class='event'>(.*?)(?=<p class=|<ul>|</ul>|</body>)|(<ul>)|(</ul>)", text, re.S):
        if match.group(1) is not None:
            current, sub = _plain(match.group(1)), 0
        elif match.group(3):
            depth += 1
        elif match.group(4):
            depth -= 1
        else:
            if current is None or depth not in (0, 1):
                raise FeedError("AHCB_CHRONOLOGY_CHANGED consolidated")
            if depth:
                sub += 1
            change, citation = _ahcb_event(match.group(2))
            rows.append(("consolidated", None, current, date_iso(current), sub if depth else 0, change, citation))
    if not rows or text.count("<p class='event'>") != len(rows):
        raise FeedError("AHCB_CHRONOLOGY_CHANGED consolidated")
    return rows


def ahcb_individual(raw: bytes) -> list:
    """Rows of the individual county chronologies; a heading that only points to another name gives one row."""
    text = _page_text(raw)
    sections = re.split(r"<p class='countyname'>", text)[1:]
    if not sections:
        raise FeedError("AHCB_CHRONOLOGY_CHANGED individual")
    rows = []
    for section in sections:
        heading, _, body = section.partition("</p>")
        subject = _plain(heading)
        entries = re.findall(r"<div class='date'>(.*?)</div>\s*<div class='change-citation'>(.*?)</div>", body, re.S)
        if len(entries) != body.count("<div class='date'>") or not subject:
            raise FeedError(f"AHCB_CHRONOLOGY_CHANGED individual {subject[:30]!r}")
        if not entries:
            rows.append(("individual", subject, None, None, 0, subject, None))
        for when, fragment in entries:
            when = _plain(when)
            change, citation = _ahcb_event(fragment)
            rows.append(("individual", subject, when, date_iso(when), 0, change, citation))
    return rows


def _ahcb_change_rows(path: Path):
    columns = [column(h) for h in AHCB_CHANGE_HEADER]
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        if next(reader, None) != AHCB_CHANGE_HEADER:
            raise FeedError("AHCB_COLUMNS_CHANGED database")
        for row in reader:
            if len(row) != len(AHCB_CHANGE_HEADER):
                raise FeedError("AHCB_ROW_SHAPE database")
            yield tuple(number(v) if c in AHCB_CHANGE_TYPES else v for c, v in zip(columns, row))


def _ahcb_version_rows(path: Path):
    shapefile = read_shapefile(path, "AHCB")
    if [f[0] for f in shapefile.fields] != AHCB_VERSION_FIELDS:
        raise FeedError("AHCB_COLUMNS_CHANGED shapefile")
    for index in range(len(shapefile)):
        if shapefile.deleted(index):
            continue
        attributes, geometry = shapefile.attributes(index), shapefile.geometry(index)
        yield (*(attributes[f] for f in AHCB_VERSION_FIELDS), int(in_kansas(geometry)), *_geometry_row(geometry))


def _ahcb_chronology_rows(path: Path, which: str):
    with gzip.open(path, "rb") as handle:
        return ahcb_consolidated(handle.read()) if which == "consolidated" else ahcb_individual(handle.read())


def _ahcb_license(members: dict) -> tuple:
    deed = _page_text(members.get(AHCB_DEED, b""))
    found = re.search(r'href="(https?://creativecommons\.org/licenses/by-nc-sa/(\d+\.\d+)/legalcode)"', deed)
    if not found:
        raise FeedError("AHCB_LICENSE_CHANGED")
    metadata = _plain(_page_text(members.get(AHCB_METADATA, b"")))
    citation = re.search(r"Citation\.PreferredStyle (Sinko, Peggy Tuck\..*?ahcbp\.)", metadata)
    return f"CC BY-NC-SA {found.group(2)}", found.group(1), re.sub(r"\s+\.", ".", citation.group(1)) if citation else AHCB_CITATION


def county_boundaries(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(AHCB_DDL)
        state, today = core.get_state(db, "county-boundaries"), ctx.now().date()
        if not _due(state, today):
            return {"state": "not_due", "checked": state["checked"]}
        full = core.temp_path(ctx, "KS_AtlasHCB.zip")
        try:
            fetched = _download(ctx, AHCB_URL, full, "AHCB", limit=256_000_000, timeout=1800)
            digest = core.file_sha256(full)
            record = _download_record(fetched, full, AHCB_URL, digest)
            if state.get("download", {}).get("sha256") == digest:
                save_state(ctx, db, "county-boundaries", {**state, "checked": str(today), "download": record})
                return {"state": "unchanged", "rows": 0}
            try:
                with zipfile.ZipFile(full) as archive:
                    names = archive.namelist()
                    wanted = [AHCB_DATABASE, AHCB_DEED, AHCB_METADATA, *AHCB_CHRONOLOGIES.values()]
                    missing = [n for n in wanted if n not in names] + [AHCB_STEM + e for e in (".shp", ".dbf") if AHCB_STEM + e not in names]
                    if missing:
                        raise FeedError(f"AHCB_MEMBER_MISSING {missing[0]}")
                    members = {n: archive.read(n) for n in wanted}
            except zipfile.BadZipFile:
                raise FeedError("AHCB_ZIP_INVALID") from None
            license_, license_url, citation = _ahcb_license(members)
            shapefile = read_shapefile(full, "AHCB")
            if [f[0] for f in shapefile.fields] != AHCB_VERSION_FIELDS:
                raise FeedError("AHCB_COLUMNS_CHANGED shapefile")
            common = {"citation": citation, "license": license_, "license_url": license_url, "terms": AHCB_TERMS}
            summary = {"rows": 0, "loaded": [], "unchanged": []}

            def note(key, result):
                summary["loaded" if result["state"] != "unchanged" else "unchanged"].append(key)
                summary["rows"] += result["rows"]
            note("ks-historical-counties", keep_version(
                ctx, db, feed="county-boundaries", source_id="ahcb-county-versions", key="ks-historical-counties", name="KS_AtlasHCB/KS_AtlasHCB",
                ext=".zip", body=full, url=AHCB_URL, fetched=fetched, extra={**common, "features": len(shapefile)},
                table="kfm_ahcb_county_versions", width=len(AHCB_VERSION_FIELDS) + 6, rows=_ahcb_version_rows))
            database = members[AHCB_DATABASE]
            rows = max(0, database.count(b"\r\n") - 1)
            note("ks-comprehensive-database", keep_version(
                ctx, db, feed="county-boundaries", source_id="ahcb-changes", key="ks-comprehensive-database",
                name="KS_Comprehensive_Database/KS_Comprehensive_Database", ext=".txt.gz", body=core.gz(database), url=AHCB_URL, fetched=fetched,
                extra={**common, "member": AHCB_DATABASE, "rows": rows}, table="kfm_ahcb_changes", width=len(AHCB_CHANGE_HEADER),
                rows=_ahcb_change_rows))
            for which, member in AHCB_CHRONOLOGIES.items():
                entries = ahcb_consolidated(members[member]) if which == "consolidated" else ahcb_individual(members[member])
                note(f"chronology/{which}", keep_version(
                    ctx, db, feed="county-boundaries", source_id="ahcb-chronology", key=f"chronology/{which}",
                    name=f"KS_Supplemental_Texts/{Path(member).stem}", ext=".htm.gz", body=core.gz(members[member]), url=AHCB_URL, fetched=fetched,
                    extra={**common, "member": member, "rows": len(entries)}, table="kfm_ahcb_chronology", width=len(AHCB_CHRONOLOGY_COLUMNS),
                    rows=lambda path, w=which: _ahcb_chronology_rows(path, w)))
        finally:
            full.unlink(missing_ok=True)
        save_state(ctx, db, "county-boundaries", {"checked": str(today), "download": record})
        return summary
    finally:
        db.close()


# --- Ceded lands: USFS Tribal Ceded Lands (Royce) -------------------------------------------------

USFS_URL = "https://data.fs.usda.gov/geodata/edw/edw_resources/shp/S_USA.TRIBALCEDEDLANDS.zip"
USFS_METADATA = "https://data.fs.usda.gov/geodata/edw/edw_resources/meta/S_USA.TRIBALCEDEDLANDS.xml"
USFS_TABLE_URL = "https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_TribalCessionLands_01/MapServer/2"
USFS_TERMS = "https://data.fs.usda.gov/geodata/edw/datasets.php"
USFS_LICENSE = "public domain (U.S. Government work, USDA Forest Service); informational, no warranty, not legal boundary descriptions"
USFS_STEM = "S_USA.TRIBALCEDEDLANDS"
CEDED_FIELDS = ["CESSNUM", "CESSNUMSOR", "SHAPE_AREA", "SHAPE_LEN"]
CEDED_TYPES = {"cessnum": "TEXT", "cessnumsor": "INTEGER", "shape_area": "REAL", "shape_len": "REAL"}
CESSION_FIELDS = ["objectid", "cessnum", "cessnumsort", "presdaytrb", "citation1", "citation2", "cessdate1", "date1link_royce_schedule",
                  "date1link_kappler_treaty", "cessdate2", "date2link_royce_schedule", "date2link_kappler_treaty", "cessdate3",
                  "date3link_royce_schedule", "date3link_kappler_treaty", "cessdate4", "date4link_royce_schedule", "date4link_kappler_treaty",
                  "cessdate5", "date5link_royce_schedule", "date5link_kappler_treaty", "mapname1", "mapname2", "mapname3", "mapname4", "mapname5",
                  "mapname6", "mapurl1", "mapurl2", "mapurl3", "mapurl4", "mapurl5", "mapurl6", "link_federal_statute", "link_executive_order",
                  "link_other_treaty", "mapname", "state", "county", "statecounty", "schdtrb"]
CESSION_TYPES = {"objectid": "INTEGER", "cessnumsort": "INTEGER"}
CEDED_DDL = (qddl("kfm_usfs_ceded_lands", [(column(f), CEDED_TYPES[column(f)]) for f in CEDED_FIELDS] + GEOMETRY_COLUMNS, [("cessnum",)])
             + qddl("kfm_usfs_ceded_land_cessions", [(f, CESSION_TYPES.get(f, "TEXT")) for f in CESSION_FIELDS], [("cessdate1",), ("cessnum",)]))


def _usfs_citation(last_modified) -> str:
    return (f'USDA Forest Service, "Tribal Ceded Lands" (S_USA.TRIBALCEDEDLANDS, refreshed {_http_date(last_modified) or "date unknown"}), '
            "digitized from Charles C. Royce, Indian Land Cessions in the United States, Eighteenth Annual Report of the Bureau of American "
            "Ethnology, part 2 (1899).")


def _ceded_rows(path: Path):
    shapefile = read_shapefile(path, "USFS")
    if [f[0] for f in shapefile.fields] != CEDED_FIELDS:
        raise FeedError("USFS_COLUMNS_CHANGED")
    for index in range(len(shapefile)):
        if not shapefile.deleted(index):
            attributes, geometry = shapefile.attributes(index), shapefile.geometry(index)
            yield (*(attributes[f] for f in CEDED_FIELDS), *_geometry_row(geometry))


def _cession_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        payload = json.load(handle)
    names = [name for name, _ in payload["fields"]]
    dates = {name for name, kind in payload["fields"] if kind == "esriFieldTypeDate"}
    if names != CESSION_FIELDS:
        raise FeedError("USFS_CESSION_FIELDS_CHANGED kept copy")
    for feature in payload["features"]:
        yield tuple(_ms_day(feature.get(n)) if n in dates else feature.get(n) for n in names)


def _arcgis_pages(ctx, layer_url: str, params: dict, code: str, *, safe: str = "", page: int = ARCGIS_PAGE):
    """(first page URL, [page bodies], [features]) of a layer query, following resultOffset paging."""
    bodies, features, offset, first = [], [], 0, None
    while True:
        url = f"{layer_url}/query?" + urllib.parse.urlencode({**params, "resultOffset": offset, "resultRecordCount": page, **{"f": params["f"]}}, safe=safe)
        first = first or url
        body = _fetch(ctx, url, code, limit=256_000_000, timeout=600).body
        try:
            payload = json.loads(body)
        except ValueError:
            raise FeedError(f"{code}_RESPONSE_SHAPE {url}") from None
        if not isinstance(payload, dict) or "error" in payload or not isinstance(payload.get("features"), list):
            raise FeedError(f"{code}_RESPONSE_SHAPE {url}")
        bodies.append(body)
        features.extend(payload["features"])
        if len(payload["features"]) < page and not payload.get("exceededTransferLimit"):
            break
        if len(payload["features"]) == 0:
            break
        offset += len(payload["features"])
        if offset > 2_000_000:
            raise FeedError(f"{code}_PAGING_RUNAWAY {layer_url}")
    return first, bodies, features


def ceded_lands(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(CEDED_DDL)
        state, today = core.get_state(db, "ceded-lands"), ctx.now().date()
        if not _due(state, today):
            return {"state": "not_due", "checked": state["checked"]}
        summary = {"rows": 0}
        full = core.temp_path(ctx, USFS_STEM + ".zip")
        try:
            fetched = _download(ctx, USFS_URL, full, "USFS", limit=256_000_000, timeout=1800)
            digest = core.file_sha256(full)
            record = _download_record(fetched, full, USFS_URL, digest)
            citation = _usfs_citation(fetched.last_modified)
            common = {"citation": citation, "license": USFS_LICENSE, "metadata": USFS_METADATA, "terms": USFS_TERMS}
            if state.get("download", {}).get("sha256") == digest:
                summary["polygons"] = "unchanged"
            else:
                shapefile = read_shapefile(full, "USFS")
                if [f[0] for f in shapefile.fields] != CEDED_FIELDS:
                    raise FeedError("USFS_COLUMNS_CHANGED")
                kept = [i for i in range(len(shapefile)) if not shapefile.deleted(i) and in_kansas(shapefile.geometry(i))]
                if not kept:
                    raise FeedError("USFS_NO_KANSAS_POLYGONS")
                result = keep_version(ctx, db, feed="ceded-lands", source_id="usfs-ceded-lands", key="tribal-ceded-lands",
                                      name=f"{USFS_STEM}/kansas-{USFS_STEM}", ext=".zip", body=shapefile.subset(kept), url=USFS_URL, fetched=fetched,
                                      original=full, extra={**common, "features": len(shapefile), "kansas_features": len(kept), "kansas_test": KANSAS_TEST},
                                      table="kfm_usfs_ceded_lands", width=len(CEDED_FIELDS) + 5, rows=_ceded_rows)
                summary["polygons"] = result["state"]
                summary["rows"] += result["rows"]
        finally:
            full.unlink(missing_ok=True)
        cessnums = {c for (c,) in db.execute("SELECT cessnum FROM kfm_usfs_ceded_lands")}
        _, bodies, features = _arcgis_pages(ctx, USFS_TABLE_URL, {"where": "1=1", "outFields": "*", "orderByFields": "OBJECTID", "f": "json"}, "USFS")
        first = json.loads(bodies[0])
        fields = [[str(f.get("name", "")).lower(), f.get("type")] for f in first.get("fields", [])]
        if [n for n, _ in fields] != CESSION_FIELDS:
            raise FeedError("USFS_CESSION_FIELDS_CHANGED")
        rows = []
        for feature in features:
            attributes = {str(k).lower(): v for k, v in feature.get("attributes", {}).items()}
            states = [s.strip() for s in str(attributes.get("state") or "").split(";")]
            if attributes.get("cessnum") in cessnums or "KS" in states:
                rows.append(attributes)
        if not rows:
            raise FeedError("USFS_NO_KANSAS_CESSIONS")
        body = (core.canonical({"features": rows, "fields": fields}) + "\n").encode()
        result = keep_version(ctx, db, feed="ceded-lands", source_id="usfs-ceded-land-cessions", key="tribal-ceded-lands-table",
                              name="cessions/kansas-cessions", ext=".json.gz", body=core.gz(body), url=USFS_TABLE_URL, original=b"".join(bodies),
                              extra={**common, "kansas_rows": len(rows), "kansas_test": "cessnum of a kept polygon, or state lists KS",
                                     "rows": len(features)},
                              table="kfm_usfs_ceded_land_cessions", width=len(CESSION_FIELDS), rows=_cession_rows)
        summary["table"] = result["state"]
        summary["rows"] += result["rows"]
        save_state(ctx, db, "ceded-lands", {"checked": str(today), "download": record, "table_rows": len(features)})
        return summary
    finally:
        db.close()


# --- Railroads: Atack's historical railroads, 1826-1911 -------------------------------------------

ATACK_PAGE = "https://my.vanderbilt.edu/jeremyatack/data-downloads/"
ATACK_LINK = re.compile(r'href="(https?://[^"]*/(\d{4})/(\d{2})/(RR1826-1911[^"/]*)\.zip)"')
ATACK_EDITED = re.compile(r"last edited:\s*([A-Z][a-z]+\.? \d{1,2}, \d{4})")
ATACK_LICENSE = "none stated; offered for download with a suggested citation (see the downloads page)"
ATACK_FIELDS = ["FID_RR1826", "track", "VxCount", "Gauge", "RRname", "InOpBy", "ExactDate", "FIDAll", "Edited", "Miles", "FID_1900St", "STATENAM"]
ATACK_TYPES = {"fid_rr1826": "INTEGER", "track": "REAL", "vx_count": "INTEGER", "gauge": "REAL", "rrname": "TEXT", "in_op_by": "INTEGER",
               "exact_date": "INTEGER", "fidall": "INTEGER", "edited": "INTEGER", "miles": "REAL", "fid_1900st": "INTEGER", "statenam": "TEXT"}
ATACK_DDL = qddl("kfm_atack_railroads", [(column(f), ATACK_TYPES[column(f)]) for f in ATACK_FIELDS] + GEOMETRY_COLUMNS,
                 [("in_op_by",), ("rrname",), ("statenam",)])


def _atack_rows(path: Path):
    shapefile = read_shapefile(path, "ATACK")
    if [f[0] for f in shapefile.fields] != ATACK_FIELDS:
        raise FeedError("ATACK_COLUMNS_CHANGED")
    for index in range(len(shapefile)):
        if not shapefile.deleted(index):
            attributes, geometry = shapefile.attributes(index), shapefile.geometry(index)
            yield (*(attributes[f] for f in ATACK_FIELDS), *_geometry_row(geometry))


def railroads_history(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(ATACK_DDL)
        state, today = core.get_state(db, "railroads-history"), ctx.now().date()
        if not _due(state, today):
            return {"state": "not_due", "checked": state["checked"]}
        page = _fetch(ctx, ATACK_PAGE, "ATACK", limit=16_000_000).body.decode("utf-8", "replace")
        links = sorted(ATACK_LINK.finditer(page), key=lambda m: (m.group(2), m.group(3), m.group(4)))
        if not links:
            raise FeedError("ATACK_FILE_NOT_LISTED")
        link, stem = links[-1].group(1), links[-1].group(4)
        edited = ATACK_EDITED.search(_plain(page[links[-1].end():links[-1].end() + 2000]))
        edited = edited.group(1) if edited else None
        full = core.temp_path(ctx, stem + ".zip")
        try:
            fetched = _download(ctx, link, full, "ATACK", limit=512_000_000, timeout=1800)
            digest = core.file_sha256(full)
            record = _download_record(fetched, full, link, digest)
            if state.get("download", {}).get("sha256") == digest:
                save_state(ctx, db, "railroads-history", {"checked": str(today), "download": record, "edited": edited, "link": link})
                return {"state": "unchanged", "rows": 0, "link": link}
            shapefile = read_shapefile(full, "ATACK")
            if [f[0] for f in shapefile.fields] != ATACK_FIELDS:
                raise FeedError("ATACK_COLUMNS_CHANGED")
            kept = [i for i in range(len(shapefile)) if not shapefile.deleted(i) and in_kansas(shapefile.geometry(i))]
            if not kept:
                raise FeedError("ATACK_NO_KANSAS_SEGMENTS")
            citation = ('Jeremy Atack, "Historical Geographic Information Systems (GIS) database of U.S. Railroads for 1826-1911" '
                        f"(May 2016{'; revised ' + edited if edited else ''}); the years are selected by the .dbf fields InOpBy or ExactDate.")
            result = keep_version(ctx, db, feed="railroads-history", source_id="atack-railroads", key="rr1826-1911", name=f"{stem}/kansas-{stem}",
                                  ext=".zip", body=shapefile.subset(kept), url=link, fetched=fetched, original=full,
                                  extra={"citation": citation, "edited": edited, "kansas_segments": len(kept), "kansas_test": KANSAS_TEST,
                                         "license": ATACK_LICENSE, "segments": len(shapefile), "terms": ATACK_PAGE},
                                  table="kfm_atack_railroads", width=len(ATACK_FIELDS) + 5, rows=_atack_rows)
        finally:
            full.unlink(missing_ok=True)
        save_state(ctx, db, "railroads-history", {"checked": str(today), "download": record, "edited": edited, "link": link})
        return {**result, "link": link, "kansas_segments": len(kept)}
    finally:
        db.close()


# --- Congress: unitedstates/congress-legislators, Kansas members ---------------------------------

CONGRESS = "https://unitedstates.github.io/congress-legislators/"
CONGRESS_FILES = ("legislators-current", "legislators-historical")
CONGRESS_TERMS = "https://github.com/unitedstates/congress-legislators"
CONGRESS_CITATION = "unitedstates/congress-legislators (https://github.com/unitedstates/congress-legislators), CC0 1.0"
CONGRESS_RECHECK_DAYS = 6
CONGRESS_IDS = ["bioguide", "thomas", "lis", "govtrack", "opensecrets", "votesmart", "fec", "cspan", "wikipedia", "house_history", "ballotpedia",
                "maplight", "icpsr", "wikidata", "google_entity_id", "pictorial", "bioguide_previous", "house_history_alternate"]
CONGRESS_NAMES = ["first", "middle", "last", "suffix", "nickname", "official_full"]
CONGRESS_BIO = ["birthday", "gender"]
CONGRESS_RECORD_KEYS = ["id", "name", "bio", "terms", "other_names", "leadership_roles", "family"]
CONGRESS_TERM_FIELDS = ["type", "start", "end", "state", "party", "district", "class", "state_rank", "how", "end_type", "caucus",
                        "party_affiliations", "url", "address", "phone", "fax", "contact_form", "office", "rss_url"]
LEGISLATOR_COLUMNS = (["bioguide", "source_file"] + CONGRESS_IDS[1:] + CONGRESS_NAMES + ["other_names_json"] + CONGRESS_BIO
                      + ["leadership_roles_json", "family_json", "kansas_terms", "first_kansas_start", "last_kansas_end", "record_json"])
LEGISLATOR_TYPES = {"bioguide": "TEXT NOT NULL", "govtrack": "INTEGER", "votesmart": "INTEGER", "cspan": "INTEGER", "house_history": "INTEGER",
                    "maplight": "INTEGER", "icpsr": "INTEGER", "pictorial": "INTEGER", "house_history_alternate": "INTEGER", "kansas_terms": "INTEGER",
                    "record_json": "TEXT NOT NULL"}
TERM_COLUMNS = ["bioguide", "term_index"] + [f + "_json" if f == "party_affiliations" else f for f in CONGRESS_TERM_FIELDS] + ["term_json"]
TERM_TYPES = {"bioguide": "TEXT NOT NULL", "term_index": "INTEGER", "district": "INTEGER", "class": "INTEGER", "term_json": "TEXT NOT NULL"}
CONGRESS_DDL = (ddl("kfm_congress_legislators", LEGISLATOR_COLUMNS, LEGISLATOR_TYPES, [("bioguide",), ("wikidata",)])
                + ddl("kfm_congress_terms", TERM_COLUMNS, TERM_TYPES, [("bioguide",), ("start",)]))


def _json_or_none(value):
    return None if value is None else core.canonical(value) if isinstance(value, (list, dict)) else value


def _legislator_row(record: dict, source: str) -> tuple:
    ids, name, bio = record.get("id", {}), record.get("name", {}), record.get("bio", {})
    kansas = [t for t in record.get("terms", []) if t.get("state") == "KS"]
    return (ids.get("bioguide"), source, *(_json_or_none(ids.get(k)) for k in CONGRESS_IDS[1:]), *(name.get(k) for k in CONGRESS_NAMES),
            _json_or_none(record.get("other_names")), *(bio.get(k) for k in CONGRESS_BIO), _json_or_none(record.get("leadership_roles")),
            _json_or_none(record.get("family")), len(kansas), min((t.get("start") for t in kansas if t.get("start")), default=None),
            max((t.get("end") for t in kansas if t.get("end")), default=None), core.canonical(record))


def _term_rows(record: dict):
    for index, term in enumerate(record.get("terms", []), start=1):
        if term.get("state") == "KS":
            yield (record["id"]["bioguide"], index, *(_json_or_none(term.get(f)) for f in CONGRESS_TERM_FIELDS), core.canonical(term))


def _congress_records(path: Path) -> list:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _load_tables(db, ctx, *, source_id: str, key: str, path: Path, digest: str, url: str, tables) -> dict:
    """``load_version`` for one source file that fills several tables ([(table, width, rows)]), with the
    reinstatement of a version loaded before (A, B, then A) as in ``sql_feed_hazards.load_version``. Lock held."""
    receipt = core.receipt_for(ctx, path)
    if receipt.get("key") != key:
        raise FeedError(f"RECEIPT_KEY_MISMATCH {key}")
    current = db.execute("SELECT file_id, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                         "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()
    if digest in {sha for _, sha in current}:
        return {"state": "unchanged", "rows": 0, "superseded": 0}
    old = db.execute("SELECT file_id FROM kfm_sql_sources WHERE sha256=? AND source_id=? AND state='superseded' "
                     "AND json_extract(receipt_json,'$.key')=?", (digest, source_id, key)).fetchone()
    if old is None and core.loaded(db, digest):
        raise FeedError(f"SOURCE_CONTENT_SHARED {key}")
    if old is None:
        file_id = core.begin_source(db, ctx, source_id, path, digest, url, receipt)
    else:
        core.guard(ctx)
        db.execute("BEGIN IMMEDIATE")
        file_id = old[0]
    try:
        for previous, _ in current:
            for table, _, _ in tables:
                db.execute(f"DELETE FROM {table} WHERE file_id=?", (previous,))
            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (previous,))
        total = 0
        for table, width, rows in tables:
            sql, batch, count = f"INSERT INTO {table} VALUES ({','.join('?' * (width + 2))})", [], 0
            for row in rows:
                if len(row) != width:
                    raise FeedError(f"ROW_SHAPE {key} {table} {count + len(batch) + 1}")
                batch.append((file_id, count + len(batch) + 1, *row))
                if len(batch) == 20000:
                    db.executemany(sql, batch)
                    count += len(batch)
                    batch = []
            db.executemany(sql, batch)
            total += count + len(batch)
        db.execute("UPDATE kfm_sql_sources SET imported_rows=?, state='complete' WHERE file_id=?", (total, file_id))
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"state": "loaded" if old is None else "reinstated", "rows": total, "superseded": len(current)}


def congress_kansas(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(CONGRESS_DDL)
        state, today = core.get_state(db, "congress-kansas"), ctx.now().date()
        summary = {"rows": 0, "unknown_fields": []}
        for source in CONGRESS_FILES:
            file_state = dict(state.get(source, {}))
            age = age_days(file_state, "checked", today)
            if age is not None and age < CONGRESS_RECHECK_DAYS:
                summary[source] = "not_due"
                continue
            url = f"{CONGRESS}{source}.json"
            fetched = _fetch(ctx, url, "CONGRESS", limit=256_000_000, timeout=600)
            try:
                records = json.loads(fetched.body)
                if not isinstance(records, list):
                    raise ValueError
                kansas = sorted((r for r in records if any(t.get("state") == "KS" for t in r.get("terms", []))), key=lambda r: r["id"]["bioguide"])
            except (ValueError, KeyError, TypeError, AttributeError):
                raise FeedError(f"CONGRESS_RESPONSE_SHAPE {source}") from None
            unknown = set()
            for record in kansas:
                unknown.update(_unknown(record, CONGRESS_RECORD_KEYS))
                unknown.update(f"id.{k}" for k in _unknown(record.get("id", {}), CONGRESS_IDS))
                unknown.update(f"name.{k}" for k in _unknown(record.get("name", {}), CONGRESS_NAMES))
                unknown.update(f"bio.{k}" for k in _unknown(record.get("bio", {}), CONGRESS_BIO))
                unknown.update(f"terms.{k}" for t in record.get("terms", []) for k in _unknown(t, CONGRESS_TERM_FIELDS))
            kansas_terms = sum(1 for r in kansas for t in r.get("terms", []) if t.get("state") == "KS")
            body = "".join(core.canonical(r) + "\n" for r in kansas).encode()
            path, digest = core.store_raw(ctx, "congress-kansas", f"{source}/kansas-{source}-{core.sha256(body)[:12]}.jsonl.gz", core.gz(body),
                                          url=url, fetched=fetched, original=fetched.body,
                                          extra={"citation": CONGRESS_CITATION, "kansas_terms": kansas_terms, "key": source, "legislators": len(kansas),
                                                 "license": "CC0-1.0", "terms": CONGRESS_TERMS, "unknown_fields": sorted(unknown)})
            with core.pipeline_lock(ctx):
                kept = _congress_records(path)
                result = _load_tables(db, ctx, source_id="congress-legislators", key=source, path=path, digest=digest, url=url, tables=[
                    ("kfm_congress_legislators", len(LEGISLATOR_COLUMNS), (_legislator_row(r, source) for r in kept)),
                    ("kfm_congress_terms", len(TERM_COLUMNS), (row for r in kept for row in _term_rows(r)))])
            summary[source] = result["state"]
            summary["rows"] += result["rows"]
            summary["unknown_fields"] = sorted(set(summary["unknown_fields"]) | unknown)
            state = save_state(ctx, db, "congress-kansas", {**state, source: {"checked": str(today), "kansas_terms": kansas_terms,
                                                                               "last_modified": fetched.last_modified, "legislators": len(kansas)}})
        return summary
    finally:
        db.close()


# --- NPS places: National Park Service public layers in Kansas ------------------------------------

NPS_NATIONAL = "https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/"
NPS_LANDS = "https://services1.arcgis.com/fBc8EJBxQRMcHlei/arcgis/rest/services/NPS_Land_Resources_Division_Boundary_and_Tract_Data_Service/FeatureServer/"
NPS_TERMS = "https://www.nps.gov/aboutus/disclaimer.htm"
NPS_LICENSE = "public domain (U.S. Government work, 17 U.S.C. 105)"
NPS_CITATION = "National Park Service, NationalDatasets and Land Resources Division services"
NPS_RECHECK_DAYS = 28
NPS_ENVELOPE = ",".join(str(v) for v in KANSAS_BOX)
NPS_SHARED = ["maplabel", "seasonal", "seasdesc", "isextant", "publicdisplay", "dataaccess", "accessnotes", "originator", "unitcode", "unitname",
              "unittype", "groupcode", "groupname", "regioncode", "createdate", "editdate", "mapmethod", "mapsource", "sourcedate", "xyaccuracy",
              "geometryid", "featureid", "faclocid", "facassetid", "imlocid", "observable", "opentopublic", "altlangname", "altlang", "maintainer", "notes"]
NPS_LAYERS = {   # name: (layer URL, columns in the table's order, index columns)
    "pois": (NPS_NATIONAL + "NPS_Public_POIs_Geographic/FeatureServer/0",
             ["objectid", "poiname", "poialtname", "maplabel", "poitype", "poistatus", "publicdisplay", "dataaccess", "accessnotes", "originator",
              "unitcode", "unitname", "unittype", "groupcode", "groupname", "regioncode", "createdate", "editdate", "pointtype", "mapmethod",
              "mapsource", "sourcedate", "xyaccuracy", "geometryid", "featureid", "faclocid", "facassetid", "imlocid", "observable", "isextant",
              "opentopublic", "altlangname", "altlang", "seasonal", "seasdesc", "maintainer", "notes"], [("poiname",), ("poitype",), ("unitcode",)]),
    "buildings": (NPS_NATIONAL + "NPS_Public_Buildings_Geographic/FeatureServer/0",
                  ["objectid", "bldgname", "bldgaltname", "maplabel", "bldgstatus", "bldgcode", "bldgtype", "facowner", "facoccupant", "facmaintain",
                   "facuse", "seasonal", "seasdesc", "isextant", "polygontype", "publicdisplay", "dataaccess", "unitcode", "unitname", "groupcode",
                   "groupname", "regioncode", "createdate", "editdate", "mapmethod", "mapsource", "sourcedate", "xyaccuracy", "faclocid", "facassetid",
                   "crid", "asmisid", "cliid", "lcsid", "firebldgid", "parkbldgid", "featureid", "geometryid", "notes", "shape_area", "shape_length"],
                  [("bldgname",), ("unitcode",)]),
    "parking_lots": (NPS_NATIONAL + "NPS_Public_ParkingLots_Geographic/FeatureServer/0",
                     ["objectid", "maplabel", "seasonal", "seasdesc", "isextant", "polygontype", "publicdisplay", "dataaccess", "unitcode", "unitname",
                      "groupcode", "groupname", "regioncode", "createdate", "editdate", "mapmethod", "mapsource", "sourcedate", "xyaccuracy", "faclocid",
                      "facassetid", "featureid", "geometryid", "notes", "shape_area", "shape_length", "lotname", "lotaltname", "lottype", "opentopublic",
                      "accessnotes", "originator", "unittype", "imlocid", "observable", "altlangname", "altlang", "maintainer"], [("unitcode",)]),
    "roads": (NPS_NATIONAL + "NPS_Public_Roads_Geographic/FeatureServer/0",
              ["rdmaintainer", "objectid", "rdname", "rdaltname", "maplabel", "rdstatus", "rdclass", "rdsurface", "rdoneway", "rdlanes", "rtenumber",
               "seasonal", "seasdesc", "rdhiclear", "isextant", "publicdisplay", "dataaccess", "accessnotes", "originator", "unitcode", "unitname",
               "unittype", "groupcode", "groupname", "regioncode", "createdate", "editdate", "linetype", "mapmethod", "mapsource", "sourcedate",
               "xyaccuracy", "routeid", "geometryid", "featureid", "faclocid", "facassetid", "imlocid", "observable", "opentopublic", "altlangname",
               "altlang", "notes", "shape_length"], [("rdname",), ("unitcode",)]),
    "trails": (NPS_NATIONAL + "NPS_Public_Trails_Geographic/FeatureServer/0",
               ["trlfeattype", "objectid", "trlname", "trlaltname", "maplabel", "trlstatus", "trlsurface", "trltype", "trlclass", "trluse",
                "publicdisplay", "dataaccess", "accessnotes", "originator", "unitcode", "unitname", "unittype", "groupcode", "groupname", "regioncode",
                "createdate", "editdate", "linetype", "mapmethod", "mapsource", "sourcedate", "xyaccuracy", "geometryid", "featureid", "faclocid",
                "facassetid", "imlocid", "observable", "isextant", "opentopublic", "altlangname", "altlang", "seasonal", "seasdesc", "maintainer",
                "notes", "shape_length"], [("trlname",), ("unitcode",)]),
    "boundaries": (NPS_LANDS + "2",
                   ["objectid", "unit_code", "unit_name", "date_edit", "state", "region", "unit_type", "metadata", "parkname", "creation_date",
                    "creator", "edit_date", "editor", "global_id", "area_id", "status", "irmareference", "shape_area", "shape_length"], [("unit_code",)]),
    "tracts": (NPS_LANDS + "1",
               ["objectid", "tract_id", "alpha", "alpha_tract", "statename", "area_tract", "estate", "status", "region", "interest", "global_id",
                "area_id", "nps_dateup", "convey_date", "shape_area", "shape_length"], [("alpha",), ("tract_id",)]),
}
NPS_DDL = "".join(qddl(f"kfm_nps_{name}", [(c, "INTEGER" if c == "objectid" else None) for c in columns] + GEOMETRY_COLUMNS, indexes)
                  for name, (_, columns, indexes) in NPS_LAYERS.items())


def _feature_rows(path: Path, columns: list, code: str, leading=()):
    """Rows of a kept GeoJSON Lines file: leading values, the properties by column, the geometry and its bbox."""
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            feature = json.loads(line)
            properties = {column(k): v for k, v in feature.get("properties", {}).items()}
            extra = _unknown(properties, columns)
            if extra:
                raise FeedError(f"{code}_FIELDS_CHANGED {' '.join(extra)}")
            yield (*leading, *(properties.get(c) for c in columns), *_geometry_row(feature.get("geometry")))


def _kept_features(features, code: str) -> tuple:
    """(JSON Lines bytes, count) of GeoJSON features sorted by OBJECTID, without the feature id."""
    try:
        features = sorted(({k: v for k, v in f.items() if k != "id"} for f in features), key=lambda f: f["properties"]["OBJECTID"])
    except (KeyError, TypeError):
        raise FeedError(f"{code}_RESPONSE_SHAPE no OBJECTID") from None
    for feature in features:
        if sorted(feature) != ["geometry", "properties", "type"]:
            raise FeedError(f"{code}_RESPONSE_SHAPE feature keys")
    return "".join(core.canonical(f) + "\n" for f in features).encode(), len(features)


def nps_places(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NPS_DDL)
        state, today = core.get_state(db, "nps-places"), ctx.now().date()
        summary = {"rows": 0, "loaded": [], "unchanged": [], "empty": [], "not_due": []}
        for name, (layer_url, columns, _) in NPS_LAYERS.items():
            age = age_days(state, name, today)
            if age is not None and age < NPS_RECHECK_DAYS:
                summary["not_due"].append(name)
                continue
            params = {"where": "1=1", "geometry": NPS_ENVELOPE, "geometryType": "esriGeometryEnvelope", "inSR": 4326,
                      "spatialRel": "esriSpatialRelIntersects", "outFields": "*", "outSR": 4326, "orderByFields": "OBJECTID", "f": "geojson"}
            first, bodies, features = _arcgis_pages(ctx, layer_url, params, "NPS")
            features = [f for f in features if in_kansas(f.get("geometry"))]
            if not features:
                if f"layer/{name}" in loaded_keys(db, "nps-kansas-layers"):
                    raise FeedError(f"NPS_LAYER_EMPTIED {name}")
                summary["empty"].append(name)
            else:
                body, count = _kept_features(features, "NPS")
                result = keep_version(ctx, db, feed="nps-places", source_id="nps-kansas-layers", key=f"layer/{name}", name=f"{name}/nps-places-{name}-KS",
                                      ext=".jsonl.gz", body=core.gz(body), url=first, original=b"".join(bodies),
                                      extra={"citation": NPS_CITATION, "kansas_test": "envelope intersects the Kansas box", "layer": name,
                                             "license": NPS_LICENSE, "rows": count, "terms": NPS_TERMS, "where": "1=1"},
                                      table=f"kfm_nps_{name}", width=len(columns) + 5, rows=lambda path, c=columns: _feature_rows(path, c, "NPS"))
                summary["loaded" if result["state"] != "unchanged" else "unchanged"].append(name)
                summary["rows"] += result["rows"]
            state = save_state(ctx, db, "nps-places", {**state, name: str(today)})
        return summary
    finally:
        db.close()


# --- NRHP: National Register of Historic Places, sheets and locations -----------------------------

NRHP_PAGE = "https://www.nps.gov/subjects/nationalregister/data-downloads.htm"
NRHP_UPLOAD = "https://www.nps.gov/subjects/nationalregister/upload/"
NRHP_LINK = re.compile(r'href="(?:https?://www\.nps\.gov)?/subjects/nationalregister/upload/([A-Za-z-]+)_(\d{8})\.xlsx"')
NRHP_LOCATIONS = "https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/"
NRHP_WHERE = "UPPER(STATE)='KANSAS'"
NRHP_TERMS = "https://www.nps.gov/aboutus/disclaimer.htm"
NRHP_LICENSE = "public domain (U.S. Government work)"
NRHP_SHEETS = ["national-register-everything", "national-register-listed", "national-register-removed", "national-historic-landmarks",
               "federal-does", "mps-covers"]   # lower-case slugs of the page's file names
NRHP_SHEETS_RECHECK_DAYS = 91
NRHP_LOCATIONS_RECHECK_DAYS = 6
PROPERTY_COLUMNS = ["sheet", "ref", "prefix", "property_name", "status", "request_type", "restricted_address", "state", "county", "city",
                    "street_and_number", "acreage_of_property", "area_of_significance", "category_of_property", "external_link",
                    "level_of_significance_international", "level_of_significance_national", "level_of_significance_state",
                    "level_of_significance_local", "level_of_significance_not_indicated", "listed_date", "listed_date_iso", "nhl_designated_date",
                    "nhl_designated_date_iso", "other_names", "park_name", "property_id", "federal_agencies"]
PROPERTY_TYPES = {"sheet": "TEXT NOT NULL", "restricted_address": "INTEGER", "acreage_of_property": "REAL"}
LOCATION_COLUMNS = ["objectid", "nris_refnum", "resname", "res_type", "cert_date", "address", "city", "county", "state", "vicinity", "multi_name",
                    "num_cbldg", "num_cobj", "num_csite", "num_cstru", "is_nhl", "bnd_type", "bnd_other", "is_extant", "extant_oth", "createdate",
                    "edit_date", "map_method", "map_mth_ot", "source", "src_date", "src_scale", "src_accu", "src_coord", "originator", "constrant",
                    "cr_id", "geom_id", "property_id", "status", "nara_url", "shape_length", "shape_area"]
LOCATION_TYPES = {"layer": "INTEGER NOT NULL", "objectid": "INTEGER", "num_cbldg": "INTEGER", "num_cobj": "INTEGER", "num_csite": "INTEGER",
                  "num_cstru": "INTEGER", "createdate": "INTEGER", "edit_date": "INTEGER", "src_date": "INTEGER", "shape_length": "REAL",
                  "shape_area": "REAL", "geometry_geojson": "TEXT", "min_lon": "REAL", "min_lat": "REAL", "max_lon": "REAL", "max_lat": "REAL"}
NRHP_DDL = (ddl("kfm_nrhp_properties", PROPERTY_COLUMNS, PROPERTY_TYPES, [("county", "city"), ("listed_date_iso",), ("ref",)])
            + ddl("kfm_nrhp_locations", ["layer", *LOCATION_COLUMNS, *(c for c, _ in GEOMETRY_COLUMNS)], LOCATION_TYPES, [("county",), ("nris_refnum",)]))
XL = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
XL_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
EXCEL_EPOCH = date(1899, 12, 30)


def _short(slug: str) -> str:
    return slug.removeprefix("national-register-")


def sheet_column(header: str) -> str:
    """"Ref#" -> ref, "Street & Number" -> street_and_number, "Level of Significance - Local" -> level_of_significance_local."""
    return re.sub(r"[^a-z0-9]+", "_", header.strip().lower().replace("&", "and").replace("#", "")).strip("_")


def excel_day(value):
    """An Excel date serial as an ISO day (the time of day dropped), else None."""
    try:
        serial = float(value)
    except (TypeError, ValueError):
        return None
    return (EXCEL_EPOCH + timedelta(days=int(serial))).isoformat() if 1 <= serial < 300000 else None


def read_xlsx(body: bytes, name: str) -> list:
    """The first worksheet as rows of text (shared and inline strings, booleans as 0/1, numbers as written), read
    with the standard library and padded to the header's width."""
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            shared = ([] if "xl/sharedStrings.xml" not in archive.namelist() else
                      ["".join(t.text or "" for t in si.iter(XL + "t")) for si in ET.fromstring(archive.read("xl/sharedStrings.xml")).iter(XL + "si")])
            targets = {r.get("Id"): r.get("Target") for r in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
            sheet = next(ET.fromstring(archive.read("xl/workbook.xml")).iter(XL + "sheet"))
            target = targets[sheet.get(XL_REL)]
            rows = []
            with archive.open(target.lstrip("/") if target.startswith("/") else "xl/" + target) as handle:
                for _, row in ET.iterparse(handle):
                    if row.tag != XL + "row":
                        continue
                    cells = {}
                    for cell in row.iter(XL + "c"):
                        letters = re.match(r"[A-Z]+", cell.get("r")).group()
                        index = 0
                        for letter in letters:
                            index = index * 26 + ord(letter) - 64
                        kind, value = cell.get("t"), cell.find(XL + "v")
                        cells[index - 1] = ("".join(t.text or "" for t in cell.iter(XL + "t")) if kind == "inlineStr" else
                                            "" if value is None else shared[int(value.text)] if kind == "s" else value.text or "")
                    width = max(cells) + 1 if cells else 0
                    rows.append([cells.get(i, "") for i in range(width)])
                    row.clear()
    except (zipfile.BadZipFile, KeyError, ET.ParseError, IndexError, ValueError, AttributeError, TypeError, StopIteration) as error:
        raise FeedError(f"NRHP_SHEET_UNREADABLE {name}: {error}") from None
    if not rows or not rows[0]:
        raise FeedError(f"NRHP_SHEET_UNREADABLE {name}: empty")
    width = len(rows[0])
    return [row[:width] + [""] * (width - len(row)) for row in rows]


def _kansas_sheet_rows(rows: list, slug: str) -> list:
    header = rows[0]
    try:
        state = header.index("State")
    except ValueError:
        raise FeedError(f"NRHP_COLUMNS_CHANGED {slug} State") from None
    if slug == "mps-covers":
        return [r for r in rows[1:] if "KS" in [s.strip() for s in r[state].split(";")]]
    return [r for r in rows[1:] if r[state].strip().upper() == "KANSAS"]


def _property_rows(path: Path, short: str):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = [sheet_column(h) for h in next(reader, [])]
        extra = _unknown(header, PROPERTY_COLUMNS)
        if extra or "ref" not in header:
            raise FeedError(f"NRHP_COLUMNS_CHANGED {short} {' '.join(extra)}")
        for row in reader:
            if len(row) != len(header):
                raise FeedError(f"NRHP_ROW_SHAPE {short}")
            values = {name: value or None for name, value in zip(header, row)}
            values["sheet"] = short
            values["listed_date_iso"] = excel_day(values.get("listed_date"))
            values["nhl_designated_date_iso"] = excel_day(values.get("nhl_designated_date"))
            for name in ("restricted_address", "acreage_of_property"):
                if name in values:
                    try:
                        values[name] = number(values[name]) if values[name] is not None else None
                    except FeedError:
                        raise FeedError(f"NRHP_NOT_A_NUMBER {short} {name} {values[name][:20]!r}") from None
            yield tuple(values.get(c) for c in PROPERTY_COLUMNS)


def _location_rows(path: Path, layer: int):
    return _feature_rows(path, LOCATION_COLUMNS, "NRHP", (layer,))


def _superset(everything: list, parts: dict) -> list:
    """Reference numbers of rows in listed, removed, NHL or DOE sheets that "everything" lacks (its columns compared)."""
    columns = everything[0]
    index = {c: i for i, c in enumerate(columns)}
    have = {tuple(r) for r in everything[1:]}
    missing = []
    for slug, rows in parts.items():
        shared = [c for c in rows[0] if c in index]
        positions = [rows[0].index(c) for c in shared]
        have_shared = {tuple(r[index[c]] for c in shared) for r in have}
        for row in rows[1:]:
            if tuple(row[p] for p in positions) not in have_shared:
                missing.append(f"{slug}:{row[0]}")
    return missing


def _nrhp_sheets(ctx, db, state: dict, listed: dict, today: date, summary: dict) -> dict:
    sheets = {}
    for slug in NRHP_SHEETS:
        name = next((n for n in listed if n.lower() == slug), None)
        if name is None:
            raise FeedError(f"NRHP_FILE_NOT_LISTED {slug}")
        url = f"{NRHP_UPLOAD}{name}_{listed[name]}.xlsx"
        fetched = _fetch(ctx, url, "NRHP", limit=256_000_000, timeout=900)
        sheets[slug] = (read_xlsx(fetched.body, name), fetched, name)
    kansas = {slug: [rows[0], *_kansas_sheet_rows(rows, slug)] for slug, (rows, _, _) in sheets.items()}
    uncovered = _superset(kansas["national-register-everything"], {s: kansas[s] for s in NRHP_SHEETS[1:5]})
    basis = "everything" if not uncovered else "parts"
    load = (["national-register-everything"] if basis == "everything" else NRHP_SHEETS[1:4]) + ["federal-does", "mps-covers"]
    for slug in load:
        rows, fetched, name = sheets[slug]
        cut = kansas[slug]
        short = _short(slug)
        result = keep_version(ctx, db, feed="nrhp", source_id="nps-nrhp-spreadsheets", key=f"sheet/{short}", name=f"sheets/{short}/{slug}-KS",
                              ext=".csv.gz", body=core.gz(csv_bytes(cut)), url=fetched.url, fetched=fetched, original=fetched.body,
                              extra={"basis": basis, "citation": f"National Park Service, National Register of Historic Places, NRIS data downloads, "
                                                                 f"{name}_{listed[name]}.xlsx", "file_date": listed[name], "kansas_rows": len(cut) - 1,
                                     "license": NRHP_LICENSE, "terms": NRHP_TERMS},
                              table="kfm_nrhp_properties", width=len(PROPERTY_COLUMNS), rows=lambda path, s=short: _property_rows(path, s))
        summary["sheets"][short] = result["state"]
        summary["rows"] += result["rows"]
    with core.pipeline_lock(ctx):
        for key in sorted(loaded_keys(db, "nps-nrhp-spreadsheets") - {f"sheet/{_short(s)}" for s in load}):
            summary["retired"] += retire(db, "nps-nrhp-spreadsheets", key, "kfm_nrhp_properties")
    summary["uncovered"] = uncovered
    return {"basis": basis, "sheets": {slug: listed[next(n for n in listed if n.lower() == slug)] for slug in NRHP_SHEETS}, "sheets_checked": str(today)}


def _nrhp_locations(ctx, db, summary: dict) -> None:
    for layer in (0, 1):
        layer_url = f"{NRHP_LOCATIONS}{layer}"
        count_url = f"{layer_url}/query?" + urllib.parse.urlencode({"where": NRHP_WHERE, "returnCountOnly": "true", "f": "json"}, safe="*")
        try:
            count = int(json.loads(_fetch(ctx, count_url, "NRHP", limit=1_000_000).body)["count"])
        except (ValueError, KeyError, TypeError):
            raise FeedError(f"NRHP_RESPONSE_SHAPE count {layer}") from None
        params = {"where": NRHP_WHERE, "outFields": "*", "outSR": 4326, "orderByFields": "OBJECTID", "f": "geojson"}
        first, bodies, features = _arcgis_pages(ctx, layer_url, params, "NRHP", safe="*")
        if len(features) != count or len({f.get("id") for f in features}) != count:
            raise FeedError(f"NRHP_RESULTS_SHIFTED layer {layer} {len(features)} of {count}")
        if not features:
            if f"layer/{layer}" in loaded_keys(db, "nps-nrhp-locations"):
                raise FeedError(f"NRHP_LAYER_EMPTIED {layer}")
            summary["locations"][str(layer)] = "empty"
            continue
        body, _ = _kept_features(features, "NRHP")
        result = keep_version(ctx, db, feed="nrhp", source_id="nps-nrhp-locations", key=f"layer/{layer}", name=f"locations/layer-{layer}/nrhp-locations-{layer}-KS",
                              ext=".jsonl.gz", body=core.gz(body), url=first, original=b"".join(bodies),
                              extra={"citation": "National Park Service, Cultural Resources GIS, nrhp_locations MapServer", "features": count, "layer": layer,
                                     "license": NRHP_LICENSE, "terms": NRHP_TERMS, "where": NRHP_WHERE},
                              table="kfm_nrhp_locations", width=len(LOCATION_COLUMNS) + 6, rows=lambda path, n=layer: _location_rows(path, n))
        summary["locations"][str(layer)] = result["state"]
        summary["rows"] += result["rows"]


def nrhp(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NRHP_DDL)
        state, today = core.get_state(db, "nrhp"), ctx.now().date()
        summary = {"rows": 0, "sheets": {}, "locations": {}, "retired": 0, "uncovered": []}
        page = _fetch(ctx, NRHP_PAGE, "NRHP", limit=16_000_000).body.decode("utf-8", "replace")
        listed = {}
        for name, when in NRHP_LINK.findall(page):
            listed[name] = max(listed.get(name, ""), when)
        age = age_days(state, "sheets_checked", today)
        known = state.get("sheets", {})
        changed = [slug for slug in NRHP_SHEETS if known.get(slug) != next((listed[n] for n in listed if n.lower() == slug), None)]
        if changed or age is None or age >= NRHP_SHEETS_RECHECK_DAYS:
            state = save_state(ctx, db, "nrhp", {**state, **_nrhp_sheets(ctx, db, state, listed, today, summary)})
            summary["basis"] = state["basis"]
        else:
            summary["sheets"] = "not_due"
        age = age_days(state, "locations_checked", today)
        if age is None or age >= NRHP_LOCATIONS_RECHECK_DAYS:
            _nrhp_locations(ctx, db, summary)
            save_state(ctx, db, "nrhp", {**state, "locations_checked": str(today)})
        else:
            summary["locations"] = "not_due"
        return summary
    finally:
        db.close()
