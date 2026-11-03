"""Bulk-database SQL feeds: FHWA bridges, EPA facilities, OpenStreetMap Kansas and Chronicling America newspaper text.

These four feeds are ``BULK_FEEDS``: ``sql_feeds.main`` routes their ``ctx.db_path`` to ``--bulk-db``
(``bulk-sql/kfm-bulk.sqlite``, outside the per-file backup) and ``open_bulk_db`` refuses an unrouted context with
``BULK_DATABASE_REQUIRED``. Each provider file is kept under ``data/raw/sql-feeds/<feed>/`` as ``<name>-<sha12><ext>``
and loaded with ``load_version`` under a stable key, so a changed version replaces the one loaded before in one
transaction, an unchanged one is not loaded again, and a provider's return to an earlier version reinstates it from
its kept copy (``sql_feed_hazards.keep_version``). Network work runs outside the pipeline lock; writes inside it.
Rebuilt on 2026-11-03 from the data volume's receipts, kept files and loaded rows after the source was lost; the
tables, keys, kept names and receipt fields are those of the original loads.

``bridges``: FHWA National Bridge Inventory (https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm), the Kansas delimited
file of each year since 1992, ``nbi/<year>/delimited/KS<yy>.txt`` (about 25,000 structures a year, 1.7 MB gzipped).
Public domain (U.S. Government work); terms https://www.fhwa.dot.gov/bridge/nbi/disclaim.cfm. The whole file is
kept gzipped as ``<year>/KS<yy>-<sha12>.txt.gz`` (key ``year/YYYY``) and loaded into ``kfm_nbi_bridges``: every
column FHWA has used (1992-2018 files have 134-137 columns with ``date_last_update`` … ``cat29``; 2019 on have 123
with ``submitted_by`` … ``deck_area``), a column a year's file lacks is NULL, the single quotes FHWA puts around
text items are removed, and ``latitude``/``longitude`` are decoded from items 16 and 17 (DDMMSS.SS / DDDMMSS.SS,
NULL when blank, zero or with minutes or seconds of 60 and more; degrees are not range-checked, as loaded) with a
``geometry_geojson`` point when both decode. Each run checks years newest first: a year not loaded, or last
checked more than 365 days ago (the newest two years, which FHWA revises, every 28 days), is fetched again, at most
``max_years`` (7) a run; a year FHWA has not published is skipped. Feed state: ``checked`` {year: date}.

``epa-facilities``: EPA Facility Registry Service, the Kansas state combined CSV download
(https://www.epa.gov/frs/epa-state-combined-csv-download-files; ``state_combined_ks.zip``, 20 MB, 11 CSV members,
republished about monthly). Public domain. Each member is kept gzipped as ``<MEMBER>/<MEMBER>-<sha12>.csv.gz`` (key
``<MEMBER>``) and loaded into its ``kfm_frs_*`` table with the provider's columns; the facility and program-GIS
tables get ``latitude83``/``longitude83`` as REAL and a ``geometry_geojson`` point. A physical line that does not
parse to the header's width (EPA's export has one, two records run together) is kept whole in ``malformed_line``
with NULL columns, counted in the receipt. The zip is fetched again every ``FRS_RECHECK_DAYS`` (7); feed state
``fetched``.

``osm-kansas``: Geofabrik's Kansas extract (https://download.geofabrik.de/north-america/us/kansas.html), the
first-of-month files only (``kansas-YYMM01.osm.pbf`` and ``kansas-YYMM01-free.shp.zip``, kept by Geofabrik about four
months): ODbL 1.0, © OpenStreetMap contributors (https://www.openstreetmap.org/copyright), attribution and
share-alike recorded in every receipt. Each run (when due) reads the directory index, takes the newest month and
checks each download against its listed size and, where listed, its ``.md5``. The PBF (117 MB on 2026-11-01) is
kept whole as ``pbf/kansas-YYMM01-<sha12>.osm.pbf`` (key ``kansas-osm-pbf``) and read with the standard-library
protobuf reader below: every tagged node inside the Kansas box (36.99-40.01 N, 102.06-94.58 W), every way whose
line segments intersect it (as a LineString from its node coordinates, ``closed`` flagged), and tagged relations
linked to retained geometry, including nested relations (members only) become ``kfm_osm_elements`` rows with the full tag set as JSON and the common keys as columns.
The free shapefile zip (238 MB) is not kept (re-published daily, derived from the same data as the kept PBF): its
20 layers are cut to the Kansas box and loaded into ``kfm_osm_<layer>``; what is kept per layer is a small
manifest ``layers/<layer>/kansas-osm-<layer>-<sha12>.json`` (key ``<layer>``) with the fields, the counts and a hash
of the loaded rows, so an unchanged layer is recognized. The manifest's ``content_sha256`` is this rebuild's hash
of the canonical rows; the original hash basis is unknown, so the first run after the rebuild supersedes every
layer once (a monthly file would have anyway). Feed state: ``checked``, ``pbf`` and ``shp`` (file, sizes, sums,
header, counts, layers).

``newspaper-text``: Chronicling America (Library of Congress) OCR text of every Kansas newspaper page, from LOC's
per-batch bulk OCR archives (https://chroniclingamerica.loc.gov/data/ocr/<batch>.tar.bz2, listed by
https://www.loc.gov/collections/chronicling-america/datasets/?fo=json&at=datasets). Public domain or no known
copyright restrictions (https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/;
issues under 95 years old may hold copyrighted third-party material); terms https://www.loc.gov/legal/, which asks
for no more than 10 requests a minute (the feed pauses ``ctx.pause``, 6 s, between requests and stops with
``LOC_RATE_LIMITED`` on 429, 403 or an HTML answer). The Kansas title list (loc.gov JSON, ``fa=location_state:kansas
&dl=title``; 84 titles) is kept every 7 days as ``titles/chronam-kansas-titles-<sha12>.jsonl.gz`` (key ``titles``,
``kfm_newspaper_titles``); the dataset listing's Kansas batches (49 of about 3,000, any LCCN of a Kansas title) as
``listing/chronam-ocr-batches-kansas-<sha12>.jsonl.gz`` (key ``listing``, ``kfm_newspaper_batches``). Each run then
downloads unloaded or changed batches, newest first, within ``max_bytes`` (6 GB) and ``max_seconds`` (50 min):
the archive is streamed to a temp file, checked against the listed size and SHA-256, and its Kansas pages
(``<lccn>/<yyyy>/<mm>/<dd>/ed-N/seq-N/ocr.txt``) are kept sorted as
``batches/<stem>/<stem>-kansas-ocr-<sha12>.jsonl.gz`` (key ``batch/<stem>``, the batch name without ``_verNN``, so a
re-issued batch replaces its predecessor) and loaded into ``kfm_newspaper_pages`` with the FTS5 index
``kfm_newspaper_pages_fts`` kept by triggers. A page listed twice in one archive (LOC's ``khi_bender_ver01`` does
this) is loaded once, the later copy winning, and counted as ``duplicate_pages``. A batch that leaves the listing is
retired; a listing that shrank by more than one batch and 10 % stops the run (``CHRONAM_LISTING_SHRANK``).
``newspaper-text-rebuild`` reloads the kept title, listing and batch copies without network. Feed state:
``titles``, ``titles_checked``, ``listing`` {stem: entry}, ``listing_checked``.
"""
from __future__ import annotations

from array import array
from bisect import bisect_left
from collections import defaultdict, deque
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import io
from itertools import accumulate
import json
import lzma
from pathlib import Path
import re
import struct
import tarfile
import time
import zipfile
import zlib

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, keep_version, load_version, loaded_keys, retire, save_state
from tools.local_data.sql_feeds import FeedError

# --- Shared ----------------------------------------------------------------------------------------

KANSAS_BOX = (-102.06, 36.99, -94.58, 40.01)   # west, south, east, north
PUBLIC_DOMAIN = "public domain (U.S. Government work, 17 U.S.C. 105)"


def open_bulk_db(ctx):
    """The bulk database: ``sql_feeds.main`` routes a BULK_FEEDS feed's ``ctx.db_path`` to ``--bulk-db``. A context
    without one, or one left pointing at observations.sqlite, is refused rather than loaded there."""
    if ctx.bulk_db is None or Path(ctx.db_path) != Path(ctx.bulk_db):
        raise FeedError("BULK_DATABASE_REQUIRED")
    return core.open_db(ctx)


def _ddl(table: str, columns, indexes) -> str:
    """The quoted-column DDL the original loads used: ``"col" TYPE`` columns and ``<table>_<cols>`` indexes."""
    body = ", ".join(f'"{name}" {kind}' for name, kind in columns)
    out = (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
           f"PRIMARY KEY(file_id, row_number));\n")
    for index in indexes:
        quoted = ", ".join(f'"{c}"' for c in index)
        out += f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(index)} ON {table}({quoted});\n"
    return out


def _geojson(geometry) -> str:
    return json.dumps(geometry, separators=(",", ":"), ensure_ascii=False)


def _point(lon, lat) -> str:
    """A point as the canonical (sorted-key) JSON the bridge and FRS loads used."""
    return core.canonical({"type": "Point", "coordinates": [lon, lat]})


def _bbox(points):
    xs, ys = [x for x, _ in points], [y for _, y in points]
    return min(xs), min(ys), max(xs), max(ys)


def _overlaps(box, other) -> bool:
    return box[0] <= other[2] and other[0] <= box[2] and box[1] <= other[3] and other[1] <= box[3]


def _inside(box, x, y) -> bool:
    return box[0] <= x <= box[2] and box[1] <= y <= box[3]


def _line_intersects_box(coords, box) -> bool:
    """Test actual line segments; overlapping envelopes alone can be false positives."""
    if any(_inside(box, x, y) for x, y in coords):
        return True
    for (x, y), (end_x, end_y) in zip(coords, coords[1:]):
        dx, dy = end_x - x, end_y - y
        low, high = 0.0, 1.0
        for direction, distance in [(-dx, x - box[0]), (dx, box[2] - x),
                                    (-dy, y - box[1]), (dy, box[3] - y)]:
            if direction == 0:
                if distance < 0:
                    break
            elif direction < 0:
                low = max(low, distance / direction)
            else:
                high = min(high, distance / direction)
            if low > high:
                break
        else:
            return True
    return False


def _kansas_relations(rows, ids, lats, lons, way_ids):
    """Keep tagged relations touching retained geometry, including nested relations in any order."""
    parents, included = defaultdict(set), set()
    def contains(values, ident):
        at = bisect_left(values, ident)
        return at < len(values) and values[at] == ident
    for row in rows:
        ident = row[1]
        for kind, ref, role in json.loads(row[OSM_ELEMENT_COLUMNS.index('members_json')]):
            if kind == 'relation':
                parents[ref].add(ident)
            elif kind == 'way' and contains(way_ids, ref):
                included.add(ident)
            elif kind == 'node':
                at = bisect_left(ids, ref)
                if at < len(ids) and ids[at] == ref and _inside(KANSAS_BOX, lons[at] / 1e9, lats[at] / 1e9):
                    included.add(ident)
    queue = deque(included)
    while queue:
        for parent in parents[queue.popleft()] - included:
            included.add(parent)
            queue.append(parent)
    for row in rows:
        if row[1] in included and row[4] != '{}':
            yield row


def _in_ring(ring, x, y) -> bool:
    inside = False
    for (ax, ay), (bx, by) in zip(ring, ring[1:]):
        if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay):
            inside = not inside
    return inside


def _crosses(box, a, b) -> bool:
    """Whether segment a-b passes through the box (Liang-Barsky)."""
    (x0, y0), (x1, y1) = a, b
    t0, t1, dx, dy = 0.0, 1.0, x1 - x0, y1 - y0
    for p, q in ((-dx, x0 - box[0]), (dx, box[2] - x0), (-dy, y0 - box[1]), (dy, box[3] - y0)):
        if p == 0:
            if q < 0:
                return False
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return False
    return True


def _in_kansas(geometry: dict) -> bool:
    """bbox overlaps the box, then a vertex inside it, an edge through it, or a box corner inside the polygon."""
    kind, coords = geometry["type"], geometry["coordinates"]
    if kind == "Point":
        return _inside(KANSAS_BOX, *coords)
    lines = ([coords] if kind == "LineString" else coords if kind in ("Polygon", "MultiLineString")
             else [ring for polygon in coords for ring in polygon])
    points = [p for line in lines for p in line]
    if not points or not _overlaps(KANSAS_BOX, _bbox(points)):
        return False
    if any(_inside(KANSAS_BOX, x, y) for x, y in points):
        return True
    if any(_crosses(KANSAS_BOX, a, b) for line in lines for a, b in zip(line, line[1:])):
        return True
    if kind in ("Polygon", "MultiPolygon"):
        outers = [coords[0]] if kind == "Polygon" else [polygon[0] for polygon in coords]
        corners = [(KANSAS_BOX[0], KANSAS_BOX[1]), (KANSAS_BOX[2], KANSAS_BOX[1]), (KANSAS_BOX[2], KANSAS_BOX[3]), (KANSAS_BOX[0], KANSAS_BOX[3])]
        return any(_in_ring(ring, x, y) for ring in outers for x, y in corners)
    return False


def _pause(ctx, seconds: float) -> None:
    time.sleep(getattr(ctx, "pause", seconds))


# --- Bridges: FHWA National Bridge Inventory, one version per year ---------------------------------

NBI_URL = "https://www.fhwa.dot.gov/bridge/nbi/{year}/delimited/KS{yy}.txt"
NBI_FIRST = 1992
NBI_SOURCE = "fhwa-nbi-kansas"
NBI_TABLE = "kfm_nbi_bridges"
NBI_CITATION = "Federal Highway Administration, National Bridge Inventory, Kansas delimited file"
NBI_TERMS = "https://www.fhwa.dot.gov/bridge/nbi/disclaim.cfm"
NBI_RECHECK_DAYS, NBI_RECENT_DAYS, NBI_RECENT_YEARS = 365, 28, 2
NBI_PROVIDER = [
    "state_code_001", "structure_number_008", "record_type_005a", "route_prefix_005b",
    "service_level_005c", "route_number_005d", "direction_005e", "highway_district_002", "county_code_003",
    "place_code_004", "features_desc_006a", "critical_facility_006b", "facility_carried_007", "location_009",
    "min_vert_clr_010", "kilopoint_011", "base_hwy_network_012", "lrs_inv_route_013a", "subroute_no_013b", "lat_016",
    "long_017", "detour_kilos_019", "toll_020", "maintenance_021", "owner_022", "functional_class_026",
    "year_built_027", "traffic_lanes_on_028a", "traffic_lanes_und_028b", "adt_029", "year_adt_030", "design_load_031",
    "appr_width_mt_032", "median_code_033", "degrees_skew_034", "structure_flared_035", "railings_036a",
    "transitions_036b", "appr_rail_036c", "appr_rail_end_036d", "history_037", "navigation_038",
    "nav_vert_clr_mt_039", "nav_horr_clr_mt_040", "open_closed_posted_041", "service_on_042a", "service_und_042b",
    "structure_kind_043a", "structure_type_043b", "appr_kind_044a", "appr_type_044b", "main_unit_spans_045",
    "appr_spans_046", "horr_clr_mt_047", "max_span_len_mt_048", "structure_len_mt_049", "left_curb_mt_050a",
    "right_curb_mt_050b", "roadway_width_mt_051", "deck_width_mt_052", "vert_clr_over_mt_053",
    "vert_clr_und_ref_054a", "vert_clr_und_054b", "lat_und_ref_055a", "lat_und_mt_055b", "left_lat_und_mt_056",
    "deck_cond_058", "superstructure_cond_059", "substructure_cond_060", "channel_cond_061", "culvert_cond_062",
    "opr_rating_meth_063", "operating_rating_064", "inv_rating_meth_065", "inventory_rating_066",
    "structural_eval_067", "deck_geometry_eval_068", "undclrence_eval_069", "posting_eval_070", "waterway_eval_071",
    "appr_road_eval_072", "work_proposed_075a", "work_done_by_075b", "imp_len_mt_076", "date_of_inspect_090",
    "inspect_freq_months_091", "fracture_092a", "undwater_look_see_092b", "spec_inspect_092c",
    "fracture_last_date_093a", "undwater_last_date_093b", "spec_last_date_093c", "bridge_imp_cost_094",
    "roadway_imp_cost_095", "total_imp_cost_096", "year_of_imp_097", "other_state_code_098a", "other_state_pcnt_098b",
    "othr_state_struc_no_099", "strahnet_highway_100", "parallel_structure_101", "traffic_direction_102",
    "temp_structure_103", "highway_system_104", "federal_lands_105", "year_reconstructed_106",
    "deck_structure_type_107", "surface_type_108a", "membrane_type_108b", "deck_protection_108c",
    "percent_adt_truck_109", "national_network_110", "pier_protection_111", "bridge_len_ind_112",
    "scour_critical_113", "future_adt_114", "year_of_future_adt_115", "min_nav_clr_mt_116", "fed_agency",
    "date_last_update", "type_last_update", "deduct_code", "remarks", "program_code", "proj_no", "proj_suffix",
    "nbi_type_of_imp", "dtl_type_of_imp", "special_code", "step_code", "status_with_10yr_rule", "sufficiency_asterc",
    "sufficiency_rating", "status_no_10yr_rule", "cat10", "cat23", "cat29", "submitted_by", "bridge_condition",
    "lowest_rating", "deck_area"]
NBI_COLUMNS = ["nbi_year", *NBI_PROVIDER, "latitude", "longitude", "geometry_geojson"]
NBI_DDL = _ddl(NBI_TABLE, [(c, {"nbi_year": "INTEGER NOT NULL", "latitude": "REAL", "longitude": "REAL"}.get(c, "TEXT")) for c in NBI_COLUMNS],
               [("nbi_year", "county_code_003"), ("structure_number_008", "nbi_year"), ("year_built_027",)])
NBI_INDEX = {c: i for i, c in enumerate(NBI_PROVIDER)}


def _nbi_degrees(text: str, degree_digits: int):
    """Item 16/17 (DDMMSS.SS without the point) as decimal degrees, or None when blank, zero or not a position."""
    if len(text) != degree_digits + 6 or not text.isdigit():
        return None
    degrees, minutes, seconds = int(text[:degree_digits]), int(text[degree_digits:degree_digits + 2]), int(text[degree_digits + 2:]) / 100
    if minutes >= 60 or seconds >= 60 or not (degrees or minutes or seconds):
        return None
    return round(degrees + minutes / 60 + seconds / 3600, 7)


def _nbi_parse(body: bytes, name: str) -> tuple[list[int], list[list[str]]]:
    """The file's rows after its header: (the table position of each column, rows). Text items lose their quotes."""
    rows = list(csv.reader(io.StringIO(body.decode("latin-1"), newline="")))
    if not rows:
        raise FeedError(f"NBI_FILE_EMPTY {name}")
    header = [h.strip().lower() for h in rows[0]]
    if not header or any(h not in NBI_INDEX for h in header) or len(set(header)) != len(header):
        raise FeedError(f"NBI_COLUMNS_CHANGED {name}")
    if any(len(r) != len(header) for r in rows[1:]):
        raise FeedError(f"NBI_ROW_SHAPE {name}")
    if len(rows) < 2:
        raise FeedError(f"NBI_FILE_EMPTY {name}")
    return [NBI_INDEX[h] for h in header], rows[1:]


def _nbi_rows(path: Path, year: int):
    positions, rows = _nbi_parse(gzip.decompress(path.read_bytes()), path.name)
    for row in rows:
        values = [None] * len(NBI_PROVIDER)
        for position, value in zip(positions, row):
            values[position] = value[1:-1] if len(value) >= 2 and value[0] == value[-1] == "'" else value
        lat, lon = _nbi_degrees(values[NBI_INDEX["lat_016"]] or "", 2), _nbi_degrees(values[NBI_INDEX["long_017"]] or "", 3)
        lon = -lon if lon is not None else None
        yield (year, *values, lat, lon, _point(lon, lat) if lat is not None and lon is not None else None)


def bridges(ctx, max_years: int = 7) -> dict:
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NBI_DDL)
        state, today = core.get_state(db, "bridges"), ctx.now().date()
        checked, loaded = dict(state.get("checked", {})), loaded_keys(db, NBI_SOURCE)
        newest = max([int(y) for y in checked] + [NBI_FIRST - 1])
        summary = {"loaded": [], "unchanged": [], "unpublished": [], "rows": 0}
        due = []
        for year in range(max(today.year, newest + 1), NBI_FIRST - 1, -1):
            age = age_days(checked, str(year), today) if f"year/{year}" in loaded else None
            recent = year >= max(newest, today.year - 1) - NBI_RECENT_YEARS + 1
            if age is None or age >= (NBI_RECENT_DAYS if recent else NBI_RECHECK_DAYS):
                due.append(year)
        for year in due[:max_years]:
            url = NBI_URL.format(year=year, yy=f"{year % 100:02d}")
            fetched = ctx.fetch(url, limit=64_000_000, timeout=600, missing_ok=True)
            if fetched is None:
                summary["unpublished"].append(year)
                continue
            _, rows = _nbi_parse(fetched.body, url)
            result = keep_version(ctx, db, feed="bridges", source_id=NBI_SOURCE, key=f"year/{year}", name=f"{year}/KS{year % 100:02d}",
                                  ext=".txt.gz", body=core.gz(fetched.body), url=url, fetched=fetched,
                                  extra={"citation": NBI_CITATION, "license": PUBLIC_DOMAIN, "terms": NBI_TERMS, "rows": len(rows), "year": year},
                                  table=NBI_TABLE, width=len(NBI_COLUMNS), rows=lambda path, year=year: _nbi_rows(path, year))
            summary["unchanged" if result["state"] == "unchanged" else "loaded"].append(year)
            summary["rows"] += result["rows"]
            checked[str(year)] = str(today)
            state = save_state(ctx, db, "bridges", {**state, "checked": checked})
        return {**summary, "pending": len(due) - len(due[:max_years])}
    finally:
        db.close()


# --- EPA facilities: the FRS Kansas state combined file, one version per member ---------------------

FRS_URL = "https://ordsext.epa.gov/FLA/www3/state_files/state_combined_ks.zip"
FRS_SOURCE = "epa-frs-kansas"
FRS_CITATION = "U.S. Environmental Protection Agency, Facility Registry Service, Kansas state combined file"
FRS_TERMS = "https://www.epa.gov/frs/epa-state-combined-csv-download-files"
FRS_RECHECK_DAYS = 7
FRS_LIMIT = 512_000_000
FRS_GEO = {"kfm_frs_facilities", "kfm_frs_program_gis"}
FRS_TABLES = {   # member stem: (table, provider columns, indexes)
    "KS_FACILITY_FILE": ("kfm_frs_facilities", [
        "frs_facility_detail_report_url", "registry_id", "primary_name", "location_address", "supplemental_location",
        "city_name", "county_name", "fips_code", "state_code", "state_name", "country_name", "postal_code",
        "federal_facility_code", "federal_agency_name", "tribal_land_code", "tribal_land_name", "congressional_dist_num",
        "census_block_code", "huc_code", "epa_region_code", "site_type_name", "location_description", "create_date",
        "update_date", "us_mexico_border_ind", "pgm_sys_acrnms", "latitude83", "longitude83", "conveyor", "collect_desc",
        "accuracy_value", "ref_point_desc", "hdatum_desc", "source_desc"], [("county_name",), ("primary_name",), ("registry_id",)]),
    "KS_PROGRAM_FILE": ("kfm_frs_programs", [
        "pgm_sys_acrnm", "pgm_sys_id", "registry_id", "primary_name", "location_address", "supplemental_location",
        "city_name", "county_name", "fips_code", "state_code", "state_name", "country_name", "postal_code",
        "federal_facility_code", "federal_agency_code", "tribal_land_code", "tribal_land_name", "legislative_dist_num",
        "huc_code_8", "huc_code_12", "epa_region_code", "site_type_name", "data_quality_code", "last_reported_date",
        "std_name", "std_loc_address", "std_house_number", "std_street_name", "std_base_name", "std_prefix", "std_suffix",
        "std_stype_before", "std_stype_after", "std_postal_code", "std_city_name", "std_county_name", "std_state_code",
        "std_county_fips", "std_country", "std_full_address", "addr_type", "link_mthd", "location_description",
        "create_date", "update_date", "user_id", "sensitive_ind", "user_comment", "public_ind", "refresh_date",
        "small_bus_ind", "env_justice_code", "parent_pgm_sys_id", "stand_alone_flag", "source_of_data"],
        [("pgm_sys_acrnm", "pgm_sys_id"), ("registry_id",)]),
    "KS_PROGRAM_GIS_FILE": ("kfm_frs_program_gis", [
        "pgm_sys_acrnm", "pgm_sys_id", "latitude83", "longitude83", "conveyor", "collect_desc", "accuracy_value",
        "ref_point_desc", "hdatum_desc", "source_desc", "state_code"], [("pgm_sys_acrnm", "pgm_sys_id")]),
    "KS_ENVIRONMENTAL_INTEREST_FILE": ("kfm_frs_environmental_interests", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "fed_state_code", "start_date",
        "start_date_qualifier", "end_date", "end_date_qualifier", "source_of_data", "last_reported_date", "create_date",
        "update_date", "active_status"], [("interest_type",), ("registry_id",)]),
    "KS_SUPP_INTEREST_FILE": ("kfm_frs_supplemental_interests", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "sup_pgm_sys_acrnm", "sup_pgm_sys_id",
        "sup_interest_type", "start_date", "start_date_qualifier", "end_date", "end_date_qualifier", "source_of_data",
        "last_reported_date", "reported_sup_interest_type", "create_date", "update_date"], [("registry_id",)]),
    "KS_ORGANIZATION_FILE": ("kfm_frs_organizations", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "affiliation_type", "start_date", "end_date",
        "org_name", "org_type", "duns_number", "division_name", "phone_number", "alternate_phone", "fax_number",
        "email_address", "ein", "state_business_id", "mailing_address", "supplemental_address", "city_name", "state_code",
        "state_name", "postal_code", "country_name"], [("org_name",), ("registry_id",)]),
    "KS_CONTACT_FILE": ("kfm_frs_contacts", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "affiliation_type", "start_date", "end_date",
        "full_name", "title", "phone_number", "alternate_phone", "fax_number", "email_address", "mailing_address",
        "supplemental_address", "city_name", "state_code", "state_name", "postal_code", "country_name"], [("registry_id",)]),
    "KS_MAILING_ADDRESS_FILE": ("kfm_frs_mailing_addresses", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "affiliation_type", "start_date", "end_date",
        "mailing_address", "supplemental_address", "city_name", "state_code", "state_name", "postal_code", "country_name"],
        [("registry_id",)]),
    "KS_ALTERNATIVE_NAME_FILE": ("kfm_frs_alternative_names", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "alternative_name", "alternative_name_type"],
        [("alternative_name",), ("registry_id",)]),
    "KS_NAICS_FILE": ("kfm_frs_naics", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "naics_code", "primary_indicator", "code_description"],
        [("naics_code",), ("registry_id",)]),
    "KS_SIC_FILE": ("kfm_frs_sic", [
        "registry_id", "pgm_sys_acrnm", "pgm_sys_id", "interest_type", "sic_code", "primary_indicator", "code_description"],
        [("registry_id",), ("sic_code",)]),
}


def _frs_columns(table: str, provider: list) -> list[tuple[str, str]]:
    columns = [(c, "REAL" if c in ("latitude83", "longitude83") else "TEXT") for c in provider]
    return columns + ([("geometry_geojson", "TEXT")] if table in FRS_GEO else []) + [("malformed_line", "TEXT")]


FRS_DDL = "".join(_ddl(table, _frs_columns(table, provider), indexes) for table, provider, indexes in FRS_TABLES.values())


def _frs_number(value: str):
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        raise FeedError(f"FRS_NOT_A_NUMBER {value[:40]!r}") from None


def _frs_rows(path: Path, member: str):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        yield from _frs_records(handle, member)


def _frs_records(handle, member: str):
    """Read complete CSV records, including quoted newlines; preserve malformed records with NULL columns."""
    table, provider, _ = FRS_TABLES[member]
    consumed = []
    def recording_lines():
        for line in handle:
            consumed.append(line)
            yield line
    reader = csv.reader(recording_lines())
    header = next(reader, [])
    if [h.lower() for h in header] != provider:
        raise FeedError(f"FRS_COLUMNS_CHANGED {member}")
    geo, width = table in FRS_GEO, len(provider)
    lat_at, lon_at = (provider.index("latitude83"), provider.index("longitude83")) if geo else (None, None)
    while True:
        consumed.clear()
        try:
            fields = next(reader)
        except StopIteration:
            break
        except csv.Error:
            raise FeedError(f"FRS_CSV_INVALID {member}") from None
        if not fields:
            continue
        if len(fields) != width:
            yield (*([None] * (width + geo)), "".join(consumed).rstrip("\r\n"))
            continue
        if geo:
            lat, lon = _frs_number(fields[lat_at]), _frs_number(fields[lon_at])
            fields[lat_at], fields[lon_at] = lat, lon
            yield (*fields, _point(lon, lat) if lat is not None and lon is not None else None, None)
        else:
            yield (*fields, None)


def _frs_member(z: zipfile.ZipFile, member: str) -> bytes:
    try:
        return z.read(member + ".CSV")
    except KeyError:
        raise FeedError(f"FRS_MEMBER_MISSING {member}") from None
    except (zipfile.BadZipFile, zlib.error, EOFError):
        raise FeedError(f"FRS_ARCHIVE_UNREADABLE {member}") from None


def epa_facilities(ctx) -> dict:
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(FRS_DDL)
        state, today = core.get_state(db, "epa-facilities"), ctx.now().date()
        age = age_days(state, "fetched", today)
        if age is not None and age < FRS_RECHECK_DAYS and loaded_keys(db, FRS_SOURCE) >= set(FRS_TABLES):
            return {"state": "not_due", "fetched": state["fetched"]}
        archive = core.temp_path(ctx, "frs-state_combined_ks.zip")
        summary = {"loaded": [], "unchanged": [], "rows": 0, "malformed_lines": 0}
        try:
            fetched = core.download(ctx, FRS_URL, archive, limit=FRS_LIMIT, timeout=1800)
            record = {"bytes": archive.stat().st_size, "sha256": core.file_sha256(archive)}
            if not zipfile.is_zipfile(archive):
                raise FeedError("FRS_ARCHIVE_UNREADABLE state_combined_ks.zip")
            with zipfile.ZipFile(archive) as z:
                for member, (table, provider, _) in FRS_TABLES.items():
                    raw = _frs_member(z, member)
                    rows, malformed = 0, 0
                    for row in _frs_records(io.StringIO(raw.decode("utf-8", "replace"), newline=""), member):
                        rows, malformed = rows + 1, malformed + (row[-1] is not None)
                    result = keep_version(ctx, db, feed="epa-facilities", source_id=FRS_SOURCE, key=member, name=f"{member}/{member}",
                                          ext=".csv.gz", body=core.gz(raw), url=FRS_URL, fetched=fetched,
                                          extra={"archive": record, "citation": FRS_CITATION, "license": PUBLIC_DOMAIN, "terms": FRS_TERMS,
                                                 "member": member + ".CSV", "rows": rows, "malformed_lines": malformed},
                                          table=table, width=len(_frs_columns(table, provider)), rows=lambda path, m=member: _frs_rows(path, m))
                    summary["unchanged" if result["state"] == "unchanged" else "loaded"].append(member)
                    summary["rows"] += result["rows"]
                    summary["malformed_lines"] += malformed
        finally:
            archive.unlink(missing_ok=True)
        save_state(ctx, db, "epa-facilities", {**state, "fetched": str(today)})
        return summary
    finally:
        db.close()


# --- OSM: Geofabrik's monthly Kansas extract, the PBF and the free shapefile layers ----------------

GEOFABRIK = "https://download.geofabrik.de/north-america/us/"
OSM_TERMS = GEOFABRIK + "kansas.html"
OSM_SOURCE_PBF, OSM_KEY_PBF = "osm-elements", "kansas-osm-pbf"
OSM_RECHECK_DAYS = 6
OSM_LIMIT = 2_000_000_000
OSM_LICENSE = {"license": "ODbL-1.0", "license_name": "Open Database License 1.0", "license_url": "https://opendatacommons.org/licenses/odbl/1-0/",
               "attribution": "© OpenStreetMap contributors", "copyright": "https://www.openstreetmap.org/copyright",
               "provider": "Geofabrik GmbH (download.geofabrik.de), from OpenStreetMap", "terms": OSM_TERMS,
               "share_alike": "A derived database used publicly must be offered under the ODbL; produced works must carry the attribution."}
OSM_FILE = re.compile(r'href="(kansas-(\d{4}01)(-free\.shp\.zip|\.osm\.pbf)(\.md5)?)"')
OSM_LISTED = re.compile(r"(\d{4})-(\w{3}|\d{2})-(\d{2})[ T](\d{2}:\d{2})")
OSM_SIZE = re.compile(r">\s*(\d+(?:\.\d+)?)\s*([KMG]?)B?\s*<")
OSM_MONTHS = {m: i for i, m in enumerate(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"), 1)}
OSM_TAG_COLUMNS = ["name", "place", "highway", "railway", "waterway", "building", "amenity", "shop", "tourism", "leisure", "historic", "heritage",
                   "start_date", "wikidata", "wikipedia"]
OSM_ELEMENT_COLUMNS = ["osm_type", "osm_id", "version", "timestamp", "tags_json", *OSM_TAG_COLUMNS, "members_json", "node_count", "closed",
                       "geometry_geojson", "min_lon", "min_lat", "max_lon", "max_lat"]
OSM_ELEMENTS_DDL = """
CREATE TABLE IF NOT EXISTS kfm_osm_elements (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "osm_type" TEXT NOT NULL, "osm_id" INTEGER NOT NULL, "version" INTEGER, "timestamp" TEXT, "tags_json" TEXT NOT NULL, "name" TEXT, "place" TEXT, "highway" TEXT, "railway" TEXT, "waterway" TEXT, "building" TEXT, "amenity" TEXT, "shop" TEXT, "tourism" TEXT, "leisure" TEXT, "historic" TEXT, "heritage" TEXT, "start_date" TEXT, "wikidata" TEXT, "wikipedia" TEXT, "members_json" TEXT, "node_count" INTEGER, "closed" INTEGER, "geometry_geojson" TEXT, "min_lon" REAL, "min_lat" REAL, "max_lon" REAL, "max_lat" REAL, PRIMARY KEY(file_id, row_number));
CREATE INDEX IF NOT EXISTS kfm_osm_elements_amenity ON kfm_osm_elements("amenity") WHERE "amenity" IS NOT NULL;
CREATE INDEX IF NOT EXISTS kfm_osm_elements_building ON kfm_osm_elements("building") WHERE "building" IS NOT NULL;
CREATE INDEX IF NOT EXISTS kfm_osm_elements_historic ON kfm_osm_elements("historic") WHERE "historic" IS NOT NULL;
CREATE INDEX IF NOT EXISTS kfm_osm_elements_name ON kfm_osm_elements("name") WHERE "name" IS NOT NULL;
CREATE INDEX IF NOT EXISTS kfm_osm_elements_osm_type_osm_id ON kfm_osm_elements(osm_type, osm_id);
CREATE INDEX IF NOT EXISTS kfm_osm_elements_place ON kfm_osm_elements("place") WHERE "place" IS NOT NULL;
CREATE INDEX IF NOT EXISTS kfm_osm_elements_wikidata ON kfm_osm_elements("wikidata") WHERE "wikidata" IS NOT NULL;
"""
OSM_LAYER_FIELDS = {   # the free shapefiles' DBF fields, in order; N fields are INTEGER
    "adminareas_a": ["osm_id", "code", "fclass", "name"], "buildings_a": ["osm_id", "code", "fclass", "name", "type"],
    "landuse_a": ["osm_id", "code", "fclass", "name"], "natural": ["osm_id", "code", "fclass", "name"], "natural_a": ["osm_id", "code", "fclass", "name"],
    "places": ["osm_id", "code", "fclass", "population", "name"], "places_a": ["osm_id", "code", "fclass", "population", "name"],
    "pofw": ["osm_id", "code", "fclass", "name"], "pofw_a": ["osm_id", "code", "fclass", "name"],
    "pois": ["osm_id", "code", "fclass", "name"], "pois_a": ["osm_id", "code", "fclass", "name"], "protected_areas_a": ["osm_id", "code", "fclass"],
    "railways": ["osm_id", "code", "fclass", "name", "layer", "bridge", "tunnel"],
    "roads": ["osm_id", "code", "fclass", "name", "ref", "oneway", "maxspeed", "layer", "bridge", "tunnel"],
    "traffic": ["osm_id", "code", "fclass", "name", "calming"], "traffic_a": ["osm_id", "code", "fclass", "name", "calming"],
    "transport": ["osm_id", "code", "fclass", "name"], "transport_a": ["osm_id", "code", "fclass", "name"],
    "water_a": ["osm_id", "code", "fclass", "name"], "waterways": ["osm_id", "code", "fclass", "width", "name"],
}
OSM_NUMBERS = {"code", "population", "layer", "maxspeed", "width"}
OSM_GEOMETRY = [("geometry_geojson", "TEXT"), ("min_lon", "REAL"), ("min_lat", "REAL"), ("max_lon", "REAL"), ("max_lat", "REAL")]
OSM_LAYERS_DDL = "".join(_ddl(f"kfm_osm_{layer}", [(f, "INTEGER" if f in OSM_NUMBERS else "TEXT") for f in fields] + OSM_GEOMETRY,
                              [(i,) for i in ("fclass", "name", "osm_id") if i in fields]) for layer, fields in OSM_LAYER_FIELDS.items())
OSM_MEMBER = re.compile(r"(?:^|/)gis_osm_(\w+?)_free_1\.(shp|shx|dbf|cpg|prj)$")
OSM_KANSAS_TEST = "bbox overlaps lon -102.06..-94.58 lat 36.99..40.01, then a vertex inside the box, an edge through it, or a box corner inside the polygon"
OSM_SHP_REASON = ("not kept: the free shapefile zip is re-published daily and is derived by Geofabrik from the same month's "
                  "OpenStreetMap data as the .osm.pbf this feed keeps monthly (pbf/)")


# ---- A protobuf reader for .osm.pbf (https://wiki.openstreetmap.org/wiki/PBF_Format), standard library only ----

def _varints(data) -> list[int]:
    """Every varint in a packed field, unsigned."""
    out, value, shift = [], 0, 0
    for byte in data:
        value |= (byte & 0x7F) << shift
        if byte < 0x80:
            out.append(value)
            value = shift = 0
        else:
            shift += 7
    if shift:
        raise FeedError("OSM_PBF_MALFORMED varint")
    return out


def _zigzag(values) -> list[int]:
    return [(v >> 1) ^ -(v & 1) for v in values]


def _fields(data):
    """(field number, wire type, value) for each field of a message; values are ints or memoryview slices."""
    view, at, end = memoryview(data), 0, len(data)
    while at < end:
        key, shift = 0, 0
        while True:
            byte = view[at]
            at += 1
            key |= (byte & 0x7F) << shift
            if byte < 0x80:
                break
            shift += 7
        number, wire = key >> 3, key & 7
        if wire == 0:
            value, shift = 0, 0
            while True:
                byte = view[at]
                at += 1
                value |= (byte & 0x7F) << shift
                if byte < 0x80:
                    break
                shift += 7
        elif wire == 2:
            length, shift = 0, 0
            while True:
                byte = view[at]
                at += 1
                length |= (byte & 0x7F) << shift
                if byte < 0x80:
                    break
                shift += 7
            value = view[at:at + length]
            at += length
        elif wire == 1:
            value = view[at:at + 8]
            at += 8
        elif wire == 5:
            value = view[at:at + 4]
            at += 4
        else:
            raise FeedError(f"OSM_PBF_MALFORMED wire type {wire}")
        yield number, wire, value
    if at != end:
        raise FeedError("OSM_PBF_MALFORMED truncated message")


def _message(data) -> dict:
    """A message as {field: [values]}, varints as ints and lengths as memoryviews."""
    out = {}
    for number, _, value in _fields(data):
        out.setdefault(number, []).append(value)
    return out


def _packed(message: dict, number: int) -> list[int]:
    values = []
    for value in message.get(number, []):
        values.extend(_varints(value) if isinstance(value, memoryview) else [value])
    return values


def _blobs(handle):
    """(type, payload bytes) for each blob of a PBF file."""
    while True:
        size = handle.read(4)
        if not size:
            return
        if len(size) != 4:
            raise FeedError("OSM_PBF_MALFORMED blob header length")
        header = _message(handle.read(struct.unpack(">I", size)[0]))
        kind = bytes(header[1][0]).decode("utf-8") if 1 in header else ""
        blob = _message(handle.read(header[3][0]))
        if 3 in blob:
            payload = zlib.decompress(blob[3][0])
        elif 1 in blob:
            payload = bytes(blob[1][0])
        elif 4 in blob:
            payload = lzma.decompress(blob[4][0])
        else:
            raise FeedError("OSM_PBF_COMPRESSION_UNSUPPORTED")
        if 2 in blob and len(payload) != blob[2][0]:
            raise FeedError("OSM_PBF_MALFORMED blob size")
        yield kind, payload


def _pbf_header(payload: bytes) -> dict:
    message = _message(payload)
    text = lambda number: bytes(message[number][0]).decode("utf-8") if number in message else None
    bbox = None
    if 1 in message:
        box = _message(message[1][0])
        bbox = [_zigzag([box[n][0]])[0] / 1e9 for n in (1, 4, 2, 3)]   # left, bottom, right, top
    stamp = message.get(32, [None])[0]
    return {"bbox": bbox, "required_features": [bytes(v).decode("utf-8") for v in message.get(4, [])],
            "optional_features": [bytes(v).decode("utf-8") for v in message.get(5, [])], "writing_program": text(16), "source": text(17),
            "replication_timestamp": _utc(stamp) if stamp is not None else None,
            "replication_sequence": message.get(33, [None])[0], "replication_url": text(34)}


def _utc(seconds: int) -> str:
    return datetime.fromtimestamp(seconds, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_pbf_header(path: Path) -> dict:
    """The file's OSMHeader, refusing a required feature this reader does not have."""
    with open(path, "rb") as handle:
        for kind, payload in _blobs(handle):
            if kind != "OSMHeader":
                raise FeedError("OSM_PBF_MALFORMED no header")
            header = _pbf_header(payload)
            break
        else:
            raise FeedError("OSM_PBF_MALFORMED empty file")
    unsupported = set(header["required_features"]) - {"OsmSchema-V0.6", "DenseNodes"}
    if unsupported:
        raise FeedError(f"OSM_PBF_FEATURE_UNSUPPORTED {' '.join(sorted(unsupported))}")
    if "Sort.Type_then_ID" not in header["optional_features"]:
        raise FeedError("OSM_PBF_UNSORTED")
    return header


def _tags(strings, keys, vals) -> dict:
    return {strings[k]: strings[v] for k, v in zip(keys, vals)}


def _element(kind, osm_id, version, stamp, tags, members=None, node_count=None, closed=None, geometry=None, box=None):
    return (kind, osm_id, version, stamp, core.canonical(tags), *(tags.get(c) for c in OSM_TAG_COLUMNS),
            _geojson(members) if members is not None else None, node_count, closed,
            _geojson(geometry) if geometry is not None else None, *(box if box else (None, None, None, None)))


def pbf_elements(path: Path, counts: dict):
    """kfm_osm_elements rows from a kept PBF: tagged nodes in the Kansas box, intersecting ways, and relations linked to retained geometry.
    counts is filled with nodes, tagged_nodes, kept_nodes, ways, kept_ways, unplaced_ways, unresolved_refs,
    relations, kept_relations."""
    counts.update(nodes=0, tagged_nodes=0, kept_nodes=0, ways=0, kept_ways=0, unplaced_ways=0, unresolved_refs=0, relations=0, kept_relations=0)
    ids, lats, lons, kept_ways, relations = array("q"), array("q"), array("q"), array("q"), []
    with open(path, "rb") as handle:
        blobs = _blobs(handle)
        kind, payload = next(blobs, (None, None))
        if kind != "OSMHeader":
            raise FeedError("OSM_PBF_MALFORMED no header")
        for kind, payload in blobs:
            if kind != "OSMData":
                continue
            block = _message(payload)
            strings = [bytes(s).decode("utf-8") for s in _message(block[1][0]).get(1, [])] if 1 in block else []
            granularity, lat_offset, lon_offset = block.get(17, [100])[0], block.get(19, [0])[0], block.get(20, [0])[0]
            date_granularity = block.get(18, [1000])[0]
            for group in block.get(2, []):
                group = _message(group)
                for node in group.get(1, []):   # plain nodes (rare)
                    node = _message(node)
                    yield from _plain_node(node, strings, granularity, lat_offset, lon_offset, date_granularity, ids, lats, lons, counts)
                for dense in group.get(2, []):
                    yield from _dense_nodes(_message(dense), strings, granularity, lat_offset, lon_offset, date_granularity, ids, lats, lons, counts)
                for way in group.get(3, []):
                    row = _way(_message(way), strings, date_granularity, ids, lats, lons, counts)
                    if row is not None:
                        if kept_ways and row[1] <= kept_ways[-1]:
                            raise FeedError('OSM_PBF_UNSORTED ways')
                        kept_ways.append(row[1])
                        yield row
                for relation in group.get(4, []):
                    row = _relation(_message(relation), strings, date_granularity, counts)
                    relations.append(row)
    for row in _kansas_relations(relations, ids, lats, lons, kept_ways):
        counts['kept_relations'] += 1
        yield row


def _info(message: dict, date_granularity: int):
    if 4 not in message:
        return None, None
    info = _message(message[4][0])
    stamp = info.get(2, [None])[0]
    return info.get(1, [None])[0], _utc(stamp * date_granularity // 1000) if stamp is not None else None


def _node_row(osm_id, lat_nano, lon_nano, version, stamp, tags, counts):
    counts["nodes"] += 1
    if not tags:
        return None
    counts["tagged_nodes"] += 1
    lon, lat = lon_nano / 1e9, lat_nano / 1e9
    if not _inside(KANSAS_BOX, lon, lat):
        return None
    counts["kept_nodes"] += 1
    return _element("node", osm_id, version, stamp, tags, geometry={"type": "Point", "coordinates": [lon, lat]}, box=(lon, lat, lon, lat))


def _plain_node(node, strings, granularity, lat_offset, lon_offset, date_granularity, ids, lats, lons, counts):
    osm_id = _zigzag([node[1][0]])[0]
    lat, lon = (lat_offset + granularity * _zigzag([node[8][0]])[0], lon_offset + granularity * _zigzag([node[9][0]])[0])
    if ids and osm_id <= ids[-1]:
        raise FeedError("OSM_PBF_UNSORTED nodes")
    ids.append(osm_id)
    lats.append(lat)
    lons.append(lon)
    row = _node_row(osm_id, lat, lon, *_info(node, date_granularity), _tags(strings, _packed(node, 2), _packed(node, 3)), counts)
    if row is not None:
        yield row


def _dense_nodes(dense, strings, granularity, lat_offset, lon_offset, date_granularity, ids, lats, lons, counts):
    block_ids = list(accumulate(_zigzag(_packed(dense, 1))))
    block_lats = [lat_offset + granularity * v for v in accumulate(_zigzag(_packed(dense, 8)))]
    block_lons = [lon_offset + granularity * v for v in accumulate(_zigzag(_packed(dense, 9)))]
    if len(block_lats) != len(block_ids) or len(block_lons) != len(block_ids):
        raise FeedError("OSM_PBF_MALFORMED dense nodes")
    if (ids and block_ids and block_ids[0] <= ids[-1]) or any(b <= a for a, b in zip(block_ids, block_ids[1:])):
        raise FeedError("OSM_PBF_UNSORTED nodes")
    versions = stamps = None
    if 5 in dense:
        info = _message(dense[5][0])
        versions = _packed(info, 1)
        stamps = [_utc(v * date_granularity // 1000) for v in accumulate(_zigzag(_packed(info, 2)))]
        if len(versions) != len(block_ids) or len(stamps) != len(block_ids):
            raise FeedError("OSM_PBF_MALFORMED dense info")
    keys_vals = _packed(dense, 10)
    ids.extend(block_ids)
    lats.extend(block_lats)
    lons.extend(block_lons)
    at, end = 0, len(keys_vals)
    for index, osm_id in enumerate(block_ids):
        tags = {}
        if at < end:
            while keys_vals[at]:
                tags[strings[keys_vals[at]]] = strings[keys_vals[at + 1]]
                at += 2
            at += 1
        row = _node_row(osm_id, block_lats[index], block_lons[index], versions[index] if versions else None, stamps[index] if stamps else None,
                        tags, counts)
        if row is not None:
            yield row


def _way(way, strings, date_granularity, ids, lats, lons, counts):
    counts["ways"] += 1
    refs = list(accumulate(_zigzag(_packed(way, 8))))
    coords, n = [], len(ids)
    for ref in refs:
        at = bisect_left(ids, ref)
        if at < n and ids[at] == ref:
            coords.append([lons[at] / 1e9, lats[at] / 1e9])
        else:
            counts["unresolved_refs"] += 1
    if not coords:
        counts["unplaced_ways"] += 1
        return None
    box = _bbox(coords)
    if not _overlaps(KANSAS_BOX, box) or not _line_intersects_box(coords, KANSAS_BOX):
        return None
    counts["kept_ways"] += 1
    return _element("way", way[1][0], *_info(way, date_granularity), _tags(strings, _packed(way, 2), _packed(way, 3)),
                    node_count=len(refs), closed=int(len(refs) >= 2 and refs[0] == refs[-1]),
                    geometry={"type": "LineString", "coordinates": coords}, box=box)


def _relation(relation, strings, date_granularity, counts):
    counts["relations"] += 1
    tags = _tags(strings, _packed(relation, 2), _packed(relation, 3))
    kinds = ("node", "way", "relation")
    members = [[kinds[t] if t < 3 else str(t), ref, strings[role]]
               for t, ref, role in zip(_packed(relation, 10), accumulate(_zigzag(_packed(relation, 9))), _packed(relation, 8))]
    return _element("relation", relation[1][0], *_info(relation, date_granularity), tags, members=members)


# ---- Shapefile and DBF readers (ESRI Shapefile Technical Description, 1998), standard library only ----

def read_dbf(data: bytes, encoding: str = "utf-8"):
    """(fields as [(name, type)], records as lists of values): C text stripped, N/F as int or float, blank None."""
    if len(data) < 32:
        raise FeedError("OSM_SHP_ARCHIVE_UNREADABLE dbf")
    count, header_length, record_length = struct.unpack_from("<IHH", data, 4)
    fields, at = [], 32
    while at < header_length - 1 and data[at] != 0x0D:
        name = data[at:at + 11].split(b"\x00", 1)[0].decode("ascii", "replace")
        fields.append((name, chr(data[at + 11]), data[at + 16], data[at + 17]))
        at += 32
    records = []
    for index in range(count):
        start = header_length + index * record_length
        record = data[start:start + record_length]
        if len(record) < record_length or record[:1] == b"*":
            continue
        values, at = [], 1
        for name, kind, length, _ in fields:
            raw = record[at:at + length]
            at += length
            if kind == "C":
                values.append(raw.decode(encoding, "replace").rstrip(" \x00"))
            elif kind in ("N", "F"):
                text = raw.decode("ascii", "replace").strip()
                values.append(None if text in ("", "*" * len(text)) else float(text) if "." in text or "e" in text.lower() else int(text))
            elif kind == "L":
                values.append(raw[:1] in (b"T", b"t", b"Y", b"y"))
            else:
                values.append(raw.decode(encoding, "replace").strip())
        records.append(values)
    return [(name, kind) for name, kind, _, _ in fields], records


def _rings_to_geojson(rings):
    """Shapefile rings (outer clockwise, holes counter-clockwise) as a Polygon or MultiPolygon with RFC 7946 winding."""
    def area(ring):
        return sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(ring, ring[1:])) / 2
    polygons, holes = [], []
    for ring in rings:
        (holes if area(ring) > 0 else polygons).append(ring)
    if not polygons:
        polygons, holes = holes, []
    polygons = [[list(reversed(ring))] for ring in polygons]
    for hole in holes:
        x, y = hole[0]
        for polygon in polygons:
            if _in_ring(polygon[0], x, y):
                polygon.append(list(reversed(hole)))
                break
        else:
            polygons.append([list(reversed(hole))])
    return {"type": "Polygon", "coordinates": polygons[0]} if len(polygons) == 1 else {"type": "MultiPolygon", "coordinates": polygons}


def read_shp(data: bytes):
    """Each record's GeoJSON geometry (None for a null shape): Point, PolyLine and Polygon, with their M and Z forms."""
    if len(data) < 100 or struct.unpack_from(">i", data, 0)[0] != 9994:
        raise FeedError("OSM_SHP_ARCHIVE_UNREADABLE shp")
    at, end = 100, min(len(data), struct.unpack_from(">i", data, 24)[0] * 2)
    while at + 8 <= end:
        length = struct.unpack_from(">i", data, at + 4)[0] * 2
        body, at = at + 8, at + 8 + length
        kind = struct.unpack_from("<i", data, body)[0]
        if kind == 0:
            yield None
        elif kind in (1, 11, 21):
            yield {"type": "Point", "coordinates": list(struct.unpack_from("<2d", data, body + 4))}
        elif kind in (3, 13, 23, 5, 15, 25):
            parts, points = struct.unpack_from("<2i", data, body + 36)
            starts = list(struct.unpack_from(f"<{parts}i", data, body + 44)) + [points]
            flat = struct.unpack_from(f"<{2 * points}d", data, body + 44 + 4 * parts)
            lines = [[[flat[2 * i], flat[2 * i + 1]] for i in range(starts[p], starts[p + 1])] for p in range(parts)]
            if kind in (3, 13, 23):
                yield {"type": "LineString", "coordinates": lines[0]} if len(lines) == 1 else {"type": "MultiLineString", "coordinates": lines}
            else:
                yield _rings_to_geojson(lines)
        else:
            raise FeedError(f"OSM_SHP_SHAPE_UNSUPPORTED {kind}")


def layer_features(z: zipfile.ZipFile, members: dict, layer: str):
    """(fields, total features, Kansas rows as a generator) of one layer of the free shapefile zip."""
    try:
        encoding = z.read(members["cpg"]).decode("ascii", "replace").strip() if "cpg" in members else "utf-8"
        fields, records = read_dbf(z.read(members["dbf"]), encoding or "utf-8")
        shp = z.read(members["shp"])
    except (KeyError, zipfile.BadZipFile, zlib.error, EOFError, struct.error, UnicodeError, LookupError):
        raise FeedError(f"OSM_SHP_ARCHIVE_UNREADABLE {layer}") from None
    if [f for f, _ in fields] != OSM_LAYER_FIELDS[layer]:
        raise FeedError(f"OSM_SHP_LAYER_FIELDS_CHANGED {layer}")

    def rows():
        """The Kansas rows, the shapes decoded again on each pass so a big layer is never held whole."""
        count = 0
        try:
            for values, geometry in zip(records, read_shp(shp)):
                count += 1
                if geometry is None or not _in_kansas(geometry):
                    continue
                points = ([geometry["coordinates"]] if geometry["type"] == "Point" else geometry["coordinates"] if geometry["type"] == "LineString"
                          else [p for line in geometry["coordinates"] for p in line] if geometry["type"] in ("Polygon", "MultiLineString")
                          else [p for polygon in geometry["coordinates"] for ring in polygon for p in ring])
                yield (*values, _geojson(geometry), *_bbox(points))
        except struct.error:
            raise FeedError(f"OSM_SHP_ARCHIVE_UNREADABLE {layer}") from None
        if count != len(records):
            raise FeedError(f"OSM_SHP_LAYER_FIELDS_CHANGED {layer} {count} shapes for {len(records)} records")
    return fields, len(records), rows


def _geofabrik_index(html: str) -> dict:
    """{file name: {"size": bytes or None, "listed": "YYYY-MM-DD HH:MM"}} for the Kansas monthly files and their .md5."""
    files = {}
    for row in re.split(r"(?i)<tr[ >]|\n", html):
        found = OSM_FILE.search(row)
        if not found:
            continue
        rest = row[found.end():]
        when = OSM_LISTED.search(rest)
        listed = None
        if when:
            year, month, day, clock = when.groups()
            month = OSM_MONTHS.get(month.title(), month) if not month.isdigit() else month
            listed = f"{year}-{int(month):02d}-{day} {clock}"
        size = OSM_SIZE.search(rest)
        exact = bool(size and size.group(2) == "" and "." not in size.group(1))
        size = round(float(size.group(1)) * {"": 1, "K": 1 << 10, "M": 1 << 20, "G": 1 << 30}[size.group(2)]) if size else None
        files[found.group(1)] = {"size": size, "exact": exact, "listed": listed, "stamp": found.group(2)}
    return files


def _osm_download(ctx, index: dict, name: str, dest: Path) -> dict:
    """Fetch one Geofabrik file to dest, checked against the listing's size and, where listed, its .md5."""
    fetched = core.download(ctx, GEOFABRIK + name, dest, limit=OSM_LIMIT, timeout=3600)
    size, entry = dest.stat().st_size, index[name]
    if entry["size"] and (size != entry["size"] if entry["exact"] else abs(size - entry["size"]) > entry["size"] * 0.03):
        raise FeedError(f"GEOFABRIK_SIZE_MISMATCH {name} {size} listed {entry['size']}")
    md5_listed, md5 = name + ".md5" in index, None
    if md5_listed:
        listed = re.search(r"\b([0-9a-f]{32})\b", ctx.fetch(GEOFABRIK + name + ".md5", limit=1_000_000).body.decode("ascii", "replace"))
        if not listed:
            raise FeedError(f"GEOFABRIK_MD5_UNREADABLE {name}")
        digest = hashlib.md5()
        with open(dest, "rb") as handle:
            for chunk in iter(lambda: handle.read(1 << 20), b""):
                digest.update(chunk)
        md5 = digest.hexdigest()
        if md5 != listed.group(1):
            raise FeedError(f"GEOFABRIK_MD5_MISMATCH {name}")
    return {"file": name, "url": GEOFABRIK + name, "bytes": size, "sha256": core.file_sha256(dest), "md5": md5, "md5_listed": md5_listed,
            "md5_checked": md5 is not None, "listed": entry["listed"], "etag": fetched.etag, "last_modified": fetched.last_modified}


def _osm_pbf(ctx, db, index: dict, name: str, state: dict, today) -> dict:
    temp = core.temp_path(ctx, name)
    try:
        record = _osm_download(ctx, index, name, temp)
        header = read_pbf_header(temp)
        record.update(header=header, data_as_of=header["replication_timestamp"])
        counts = {}
        result = keep_version(ctx, db, feed="osm-kansas", source_id=OSM_SOURCE_PBF, key=OSM_KEY_PBF, name=f"pbf/{name[:-8]}", ext=".osm.pbf",
                              body=temp, url=GEOFABRIK + name, fetched=core.Fetched(GEOFABRIK + name, b"", record["last_modified"], record["etag"]),
                              extra={**OSM_LICENSE, "file": name, "data_as_of": record["data_as_of"], "header": header, "listed": record["listed"],
                                     "md5": record["md5"], "citation": f"© OpenStreetMap contributors. Geofabrik GmbH, Kansas extract {name}, "
                                     f"data as of {record['data_as_of']}, {GEOFABRIK}{name}."},
                              table="kfm_osm_elements", width=len(OSM_ELEMENT_COLUMNS), rows=lambda path: pbf_elements(path, counts))
    finally:
        temp.unlink(missing_ok=True)
    if result["state"] == "unchanged":
        counts = dict(state.get("pbf", {}).get("counts", {}))
    return {**record, "counts": counts, "loaded": str(today), "result": result}


def _osm_shp(ctx, db, index: dict, name: str, data_as_of, today) -> dict:
    temp = core.temp_path(ctx, name)
    try:
        record = _osm_download(ctx, index, name, temp)
        if not zipfile.is_zipfile(temp):
            raise FeedError(f"OSM_SHP_ARCHIVE_UNREADABLE {name}")
        fetched = core.Fetched(GEOFABRIK + name, b"", record["last_modified"], record["etag"])
        layers, unknown, results = {}, [], {}
        with zipfile.ZipFile(temp) as z:
            for member in z.namelist():
                found = OSM_MEMBER.search(member)
                if found:
                    layers.setdefault(found.group(1), {})[found.group(2)] = member
            unknown = sorted(layer for layer in layers if layer not in OSM_LAYER_FIELDS)
            counts = {}
            for layer in OSM_LAYER_FIELDS:
                if layer not in layers:
                    continue
                fields, total, rows = layer_features(z, layers[layer], layer)
                digest, kept = hashlib.sha256(), 0
                for row in rows():
                    digest.update(core.canonical(row).encode() + b"\n")
                    kept += 1
                manifest = core.canonical({"content_sha256": digest.hexdigest(), "fields": fields, "format": "kfm-osm-layer-v1", "kansas_features": kept,
                                           "kansas_test": OSM_KANSAS_TEST, "layer": layer, "stem": f"gis_osm_{layer}_free_1"}) + "\n"
                results[layer] = keep_version(
                    ctx, db, feed="osm-kansas", source_id=f"osm-{layer.replace('_', '-')}", key=layer, name=f"layers/{layer}/kansas-osm-{layer}",
                    ext=".json", body=manifest.encode(), url=GEOFABRIK + name, fetched=fetched,
                    extra={**OSM_LICENSE, "file": name, "data_as_of": data_as_of, "features": total, "kansas_features": kept, "listed": record["listed"],
                           "citation": f"© OpenStreetMap contributors. Geofabrik GmbH, Kansas free shapefiles {name}, data as of {data_as_of}, {GEOFABRIK}{name}.",
                           "original": {"bytes": record["bytes"], "sha256": record["sha256"], "md5": record["md5"], "kept": False, "reason": OSM_SHP_REASON}},
                    table=f"kfm_osm_{layer}", width=len(OSM_LAYER_FIELDS[layer]) + len(OSM_GEOMETRY), rows=lambda path, r=rows: r())
                counts[layer] = kept
    finally:
        temp.unlink(missing_ok=True)
    return {**record, "data_as_of": data_as_of, "layers": counts, "unknown_layers": unknown, "loaded": str(today), "results": results}


def osm_kansas(ctx, max_products: int = 2, recheck_days: int = OSM_RECHECK_DAYS) -> dict:
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(OSM_ELEMENTS_DDL + OSM_LAYERS_DDL)
        state, today = core.get_state(db, "osm-kansas"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < recheck_days and state.get("pbf", {}).get("loaded") and state.get("shp", {}).get("loaded"):
            return {"state": "not_due", "checked": state["checked"]}
        index = _geofabrik_index(ctx.fetch(GEOFABRIK, limit=16_000_000).body.decode("utf-8", "replace"))
        stamps = sorted({v["stamp"] for k, v in index.items() if k.endswith(".osm.pbf")})
        if not stamps:
            raise FeedError("GEOFABRIK_LISTING_SHAPE no monthly kansas-YYMM01.osm.pbf listed")
        stamp = stamps[-1]
        summary, products = {"month": stamp}, 0
        pbf = f"kansas-{stamp}.osm.pbf"
        if products < max_products and (state.get("pbf", {}).get("file") != pbf or not state["pbf"].get("loaded")):
            _pause(ctx, 1.0)
            loaded = _osm_pbf(ctx, db, index, pbf, state, today)
            summary["pbf"] = loaded.pop("result")
            state = save_state(ctx, db, "osm-kansas", {**state, "pbf": loaded})
            products += 1
        shp = f"kansas-{stamp}-free.shp.zip"
        if products < max_products and shp in index and (state.get("shp", {}).get("file") != shp or not state["shp"].get("loaded")):
            _pause(ctx, 1.0)
            data_as_of = state.get("pbf", {}).get("data_as_of") if state.get("pbf", {}).get("file") == pbf else None
            loaded = _osm_shp(ctx, db, index, shp, data_as_of, today)
            summary["layers"] = {layer: r["state"] for layer, r in loaded.pop("results").items()}
            state = save_state(ctx, db, "osm-kansas", {**state, "shp": loaded})
            products += 1
        if products == 0:
            summary["state"] = "unchanged"
        save_state(ctx, db, "osm-kansas", {**state, "checked": str(today)})
        return summary
    finally:
        db.close()


# --- Newspaper text: Chronicling America titles, batch listing and per-batch OCR text --------------

CHRONAM_TITLES = ("https://www.loc.gov/collections/chronicling-america/?fa=location_state:kansas&dl=title&fo=json&c=1000&sp={page}"
                  "&at=results,pagination")
CHRONAM_DATASETS = "https://www.loc.gov/collections/chronicling-america/datasets/?fo=json&at=datasets"
CHRONAM_ARCHIVE = re.compile(r"^https://chroniclingamerica\.loc\.gov/data/ocr/[\w.-]+\.tar\.bz2$")
CHRONAM_PAGE = re.compile(r"(?:^|/)([a-z0-9]+)/(\d{4})/(\d{2})/(\d{2})/ed-(\d+)/seq-(\d+)/ocr\.txt$")
CHRONAM_PAGE_URL = "https://www.loc.gov/resource/{lccn}/{date}/ed-{edition}/?sp={sequence}"
CHRONAM_LICENSE = ("public domain or no known copyright restrictions (Library of Congress); issues under 95 years old may hold copyrighted "
                   "third-party material")
CHRONAM_TERMS = "https://www.loc.gov/legal/"
CHRONAM_RIGHTS = "https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/"
CHRONAM_CITATION = "Chronicling America: Historic American Newspapers. Library of Congress"
CHRONAM_PAUSE = 6.0   # https://www.loc.gov/legal/: at most 10 requests a minute
CHRONAM_TITLES_DAYS, CHRONAM_LISTING_DAYS = 7, 28
CHRONAM_LISTING_FIELDS = ("batch", "lccns", "url", "sha256", "size", "page_count", "issue_count", "ingested")
CHRONAM_STATE_FIELDS = ("batch", "ingested", "issue_count", "lccns", "page_count", "sha256", "size", "url")
CHRONAM_SOURCES = {"titles": "chronam-kansas-titles", "listing": "chronam-ocr-batches", "pages": "chronam-ocr-pages"}
CHRONAM_LOCATION = ("latlong", "location", "location_city", "location_country", "location_county", "location_state", "location_str", "lonlat")
TITLE_COLUMNS = ["lccn", "id", "title", "place", "start_year", "first_issue", "last_issue", "issue_count", "publication_frequency", "location_json",
                 "subject_json", "contributor_json", "description_json", "url", "source_modified_json"]
BATCH_COLUMNS = ["batch", "archive_name", "url", "sha256", "size", "page_count", "issue_count", "ingested", "archive_created", "identifier", "lccns_json"]
PAGE_COLUMNS = ["page_rowid", "lccn", "issue_date", "edition", "sequence", "page_url", "ocr_text", "char_count"]
NEWSPAPER_DDL = """
CREATE TABLE IF NOT EXISTS kfm_newspaper_titles (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, lccn TEXT NOT NULL, id TEXT, title TEXT, place TEXT, start_year TEXT, first_issue TEXT, last_issue TEXT, issue_count INTEGER, publication_frequency TEXT, location_json TEXT, subject_json TEXT, contributor_json TEXT, description_json TEXT, url TEXT, source_modified_json TEXT, PRIMARY KEY(file_id, row_number));
CREATE INDEX IF NOT EXISTS kfm_newspaper_titles_lccn ON kfm_newspaper_titles(lccn);
CREATE TABLE IF NOT EXISTS kfm_newspaper_batches (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, batch TEXT NOT NULL, archive_name TEXT, url TEXT, sha256 TEXT, size INTEGER, page_count INTEGER, issue_count INTEGER, ingested TEXT, archive_created TEXT, identifier TEXT, lccns_json TEXT, PRIMARY KEY(file_id, row_number));
CREATE INDEX IF NOT EXISTS kfm_newspaper_batches_batch ON kfm_newspaper_batches(batch);
CREATE TABLE IF NOT EXISTS kfm_newspaper_pages (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, page_rowid INTEGER PRIMARY KEY,
  lccn TEXT NOT NULL, issue_date TEXT NOT NULL, edition INTEGER NOT NULL, sequence INTEGER NOT NULL, page_url TEXT NOT NULL,
  ocr_text TEXT NOT NULL, char_count INTEGER NOT NULL);
CREATE UNIQUE INDEX IF NOT EXISTS kfm_newspaper_pages_file_id_row_number ON kfm_newspaper_pages(file_id, row_number);
CREATE INDEX IF NOT EXISTS kfm_newspaper_pages_lccn_issue ON kfm_newspaper_pages(lccn, issue_date, edition, sequence);
CREATE INDEX IF NOT EXISTS kfm_newspaper_pages_issue_date ON kfm_newspaper_pages(issue_date);
CREATE VIRTUAL TABLE IF NOT EXISTS kfm_newspaper_pages_fts USING fts5(ocr_text, content='kfm_newspaper_pages', content_rowid='page_rowid');
CREATE TRIGGER IF NOT EXISTS kfm_newspaper_pages_fts_insert AFTER INSERT ON kfm_newspaper_pages BEGIN
  INSERT INTO kfm_newspaper_pages_fts(rowid, ocr_text) VALUES (new.page_rowid, new.ocr_text); END;
CREATE TRIGGER IF NOT EXISTS kfm_newspaper_pages_fts_delete AFTER DELETE ON kfm_newspaper_pages BEGIN
  INSERT INTO kfm_newspaper_pages_fts(kfm_newspaper_pages_fts, rowid, ocr_text) VALUES ('delete', old.page_rowid, old.ocr_text); END;
CREATE TRIGGER IF NOT EXISTS kfm_newspaper_pages_fts_update AFTER UPDATE OF page_rowid, ocr_text ON kfm_newspaper_pages BEGIN
  INSERT INTO kfm_newspaper_pages_fts(kfm_newspaper_pages_fts, rowid, ocr_text) VALUES ('delete', old.page_rowid, old.ocr_text);
  INSERT INTO kfm_newspaper_pages_fts(rowid, ocr_text) VALUES (new.page_rowid, new.ocr_text); END;
"""


def _loc_json(ctx, url: str, limit: int):
    """A loc.gov JSON answer; an HTML page (Cloudflare challenge or block) or a 429/403 stops the run."""
    try:
        fetched = ctx.fetch(url, limit=limit, timeout=600)
    except FeedError as error:
        if str(error).startswith(("HTTP_429", "HTTP_403")):
            raise FeedError(f"LOC_RATE_LIMITED {url}") from None
        raise
    body = fetched.body.lstrip()
    if body[:1] not in (b"{", b"["):
        raise FeedError(f"LOC_RATE_LIMITED {url}" if body[:1] == b"<" else f"CHRONAM_LISTING_INVALID {url}")
    try:
        return fetched, json.loads(body)
    except ValueError:
        raise FeedError(f"CHRONAM_LISTING_INVALID {url}") from None


def _issue_date(urls):
    found = re.search(r"/(\d{4}-\d{2}-\d{2})/", (urls or [""])[0] or "") if isinstance(urls, list) else None
    return found.group(1) if found else None


def _first(values):
    return values[0] if isinstance(values, list) and values else values if isinstance(values, str) else None


def title_row(title: dict) -> tuple:
    """A kfm_newspaper_titles row from one loc.gov title result."""
    count = _first(title.get("number_issue_count"))
    return (_first(title.get("number_lccn")), title.get("id"), title.get("title"), title.get("location_str"), title.get("date"),
            _issue_date(title.get("number_first_issue")), _issue_date(title.get("number_last_issue")),
            int(count) if count is not None and str(count).isdigit() else None, _first(title.get("publication_frequency")),
            core.canonical({k: title[k] for k in CHRONAM_LOCATION if k in title}),
            *(core.canonical(title[k]) if k in title else None for k in ("subject", "contributor", "description")),
            title.get("url"), core.canonical(title["number_source_modified"]) if "number_source_modified" in title else None)


def _jsonl_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def _jsonl(entries) -> bytes:
    return core.gz("".join(core.canonical(e) + "\n" for e in entries).encode())


def batch_row(entry: dict) -> tuple:
    return (entry["batch"], entry.get("archive_name"), entry.get("url"), entry.get("sha256"), entry.get("size"), entry.get("page_count"),
            entry.get("issue_count"), entry.get("ingested"), entry.get("archive_created"), entry.get("identifier"),
            core.canonical(entry.get("lccns")) if "lccns" in entry else None)


def _stem(batch: str) -> str:
    return re.sub(r"_ver\d+$", "", batch)


def _chronam_titles(ctx, db) -> tuple[list[str], dict]:
    """Fetch, keep and load the Kansas title list; returns its LCCNs and the load result."""
    titles, page, first = {}, 1, None
    while True:
        url = CHRONAM_TITLES.format(page=page)
        _pause(ctx, CHRONAM_PAUSE)
        fetched, payload = _loc_json(ctx, url, 64_000_000)
        results = payload.get("results") if isinstance(payload, dict) else None
        if not isinstance(results, list):
            raise FeedError(f"CHRONAM_LISTING_SHAPE {url}")
        for title in results:
            lccn = _first(title.get("number_lccn")) if isinstance(title, dict) else None
            if lccn:
                titles.setdefault(lccn, title)
        first = first or fetched
        pagination = payload.get("pagination") or {}
        if not results or not pagination.get("next"):
            break
        page += 1
    if not titles:
        raise FeedError("CHRONAM_KANSAS_EMPTY titles")
    entries = [titles[k] for k in sorted(titles)]
    result = keep_version(ctx, db, feed="newspaper-text", source_id=CHRONAM_SOURCES["titles"], key="titles", name="titles/chronam-kansas-titles",
                          ext=".jsonl.gz", body=_jsonl(entries), url=CHRONAM_TITLES.format(page=1), fetched=first,
                          extra={"citation": CHRONAM_CITATION, "license": CHRONAM_LICENSE, "rights": CHRONAM_RIGHTS, "terms": CHRONAM_TERMS,
                                 "titles": len(entries)},
                          table="kfm_newspaper_titles", width=len(TITLE_COLUMNS), rows=lambda path: (title_row(t) for t in _jsonl_rows(path)))
    return sorted(titles), result


def _chronam_listing(ctx, db, lccns: set, previous: dict) -> tuple[dict, dict]:
    """Fetch the dataset listing, keep its Kansas batches and load them; returns {stem: entry} and the load result."""
    _pause(ctx, CHRONAM_PAUSE)
    fetched, payload = _loc_json(ctx, CHRONAM_DATASETS, 64_000_000)
    entries = payload.get("datasets") if isinstance(payload, dict) else payload
    if not isinstance(entries, list):
        raise FeedError("CHRONAM_LISTING_SHAPE datasets")
    kansas = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("lccns"), list):
            continue
        if any(f not in entry for f in CHRONAM_LISTING_FIELDS):
            raise FeedError("CHRONAM_LISTING_FIELDS_CHANGED")
        if set(entry["lccns"]) & lccns:
            if not CHRONAM_ARCHIVE.match(str(entry["url"])):
                raise FeedError(f"CHRONAM_LISTING_SHAPE {entry['url']}")
            kansas.append(entry)
    if not kansas:
        raise FeedError("CHRONAM_KANSAS_EMPTY listing")
    kansas.sort(key=lambda e: e["batch"])
    listing = {_stem(e["batch"]): {k: e[k] for k in CHRONAM_STATE_FIELDS} for e in kansas}
    gone = len(previous) - len(listing)
    if gone > 1 and gone > 0.1 * len(previous):
        raise FeedError(f"CHRONAM_LISTING_SHRANK {len(previous)} to {len(listing)}")
    result = keep_version(ctx, db, feed="newspaper-text", source_id=CHRONAM_SOURCES["listing"], key="listing", name="listing/chronam-ocr-batches-kansas",
                          ext=".jsonl.gz", body=_jsonl(kansas), url=CHRONAM_DATASETS, fetched=fetched, original=fetched.body,
                          extra={"license": CHRONAM_LICENSE, "terms": CHRONAM_TERMS, "batches": len(kansas)},
                          table="kfm_newspaper_batches", width=len(BATCH_COLUMNS), rows=lambda path: (batch_row(e) for e in _jsonl_rows(path)))
    return listing, result


def _archive_pages(archive: Path, batch: str, lccns: set) -> tuple[list[dict], dict]:
    """The Kansas pages of a batch archive, sorted; a page listed twice is taken once (the later copy)."""
    pages, counts = {}, {"pages": 0, "pages_skipped": 0, "duplicate_pages": 0}
    try:
        with tarfile.open(archive, "r|bz2") as tar:
            for member in tar:
                found = CHRONAM_PAGE.search(member.name)
                if not found or not member.isfile():
                    continue
                counts["pages"] += 1
                lccn, year, month, day, edition, sequence = found.groups()
                if lccn not in lccns:
                    counts["pages_skipped"] += 1
                    continue
                key = (lccn, f"{year}-{month}-{day}", int(edition), int(sequence))
                if key in pages:
                    counts["duplicate_pages"] += 1
                handle = tar.extractfile(member)
                pages[key] = handle.read().decode("utf-8", "replace") if handle else ""
    except (tarfile.TarError, EOFError, OSError, ValueError) as error:
        raise FeedError(f"CHRONAM_ARCHIVE_UNREADABLE {batch} {error}"[:200]) from None
    if not counts["pages"]:
        raise FeedError(f"CHRONAM_ARCHIVE_LAYOUT_CHANGED {batch}")
    entries = [{"lccn": k[0], "issue_date": k[1], "edition": k[2], "sequence": k[3], "text": pages[k]} for k in sorted(pages)]
    return entries, counts


def page_rows(path: Path):
    for page in _jsonl_rows(path):
        url = CHRONAM_PAGE_URL.format(lccn=page["lccn"], date=page["issue_date"], edition=page["edition"], sequence=page["sequence"])
        yield (None, page["lccn"], page["issue_date"], page["edition"], page["sequence"], url, page["text"], len(page["text"]))


def _archive_sha256(db, key: str):
    row = db.execute("SELECT json_extract(receipt_json, '$.archive.sha256') FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                     "AND json_extract(receipt_json, '$.key')=?", (CHRONAM_SOURCES["pages"], key)).fetchone()
    return row[0] if row else None


def _chronam_batch(ctx, db, stem: str, entry: dict, lccns: set) -> dict:
    name = entry["url"].rsplit("/", 1)[-1]
    archive = core.temp_path(ctx, name)
    try:
        _pause(ctx, CHRONAM_PAUSE)
        fetched = core.download(ctx, entry["url"], archive, limit=max(int(entry["size"]) + 1, 1 << 20), timeout=7200)
        size, digest = archive.stat().st_size, core.file_sha256(archive)
        if size != entry["size"] or digest != entry["sha256"]:
            raise FeedError(f"CHRONAM_ARCHIVE_CHANGED {entry['batch']} {size} bytes sha256 {digest[:12]}")
        pages, counts = _archive_pages(archive, entry["batch"], lccns)
    finally:
        archive.unlink(missing_ok=True)
    if not pages:
        raise FeedError(f"CHRONAM_KANSAS_EMPTY {entry['batch']}")
    result = keep_version(ctx, db, feed="newspaper-text", source_id=CHRONAM_SOURCES["pages"], key=f"batch/{stem}", name=f"batches/{stem}/{stem}-kansas-ocr",
                          ext=".jsonl.gz", body=_jsonl(pages), url=entry["url"], fetched=fetched,
                          extra={"archive": {"bytes": size, "sha256": digest}, "listing": entry, "kansas_pages": len(pages), "citation": CHRONAM_CITATION,
                                 "license": CHRONAM_LICENSE, "rights": CHRONAM_RIGHTS, "terms": CHRONAM_TERMS, **counts},
                          table="kfm_newspaper_pages", width=len(PAGE_COLUMNS), rows=page_rows)
    return {**result, "batch": entry["batch"], "bytes": size, **counts}


def newspaper_text(ctx, max_bytes: int = 6_000_000_000, max_seconds: int = 3000) -> dict:
    started = time.monotonic()
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NEWSPAPER_DDL)
        state, today = core.get_state(db, "newspaper-text"), ctx.now().date()
        summary = {"titles": "not_due", "listing": "not_due", "batches": [], "bytes": 0, "rows": 0, "retired": 0}
        age = age_days(state, "titles_checked", today)
        if age is None or age >= CHRONAM_TITLES_DAYS or "titles" not in loaded_keys(db, CHRONAM_SOURCES["titles"]):
            lccns, result = _chronam_titles(ctx, db)
            summary["titles"] = result["state"]
            state = save_state(ctx, db, "newspaper-text", {**state, "titles": lccns, "titles_checked": str(today)})
        lccns = set(state.get("titles", []))
        loaded = loaded_keys(db, CHRONAM_SOURCES["pages"])
        listing = dict(state.get("listing", {}))
        pending = [s for s, e in listing.items() if f"batch/{s}" not in loaded or _archive_sha256(db, f"batch/{s}") != e["sha256"]]
        age = age_days(state, "listing_checked", today)
        if age is None or pending or age >= CHRONAM_LISTING_DAYS or "listing" not in loaded_keys(db, CHRONAM_SOURCES["listing"]):
            listing, result = _chronam_listing(ctx, db, lccns, listing)
            summary["listing"] = result["state"]
            state = save_state(ctx, db, "newspaper-text", {**state, "listing": listing, "listing_checked": str(today)})
            with core.pipeline_lock(ctx):
                for key in sorted(loaded - {f"batch/{s}" for s in listing}):
                    summary["retired"] += retire(db, CHRONAM_SOURCES["pages"], key, "kfm_newspaper_pages")
            pending = [s for s, e in listing.items() if f"batch/{s}" not in loaded or _archive_sha256(db, f"batch/{s}") != e["sha256"]]
        for stem in sorted(pending, key=lambda s: (listing[s]["ingested"] or "", s), reverse=True):
            entry = listing[stem]
            if summary["batches"] and (summary["bytes"] + int(entry["size"]) > max_bytes or time.monotonic() - started > max_seconds):
                break
            result = _chronam_batch(ctx, db, stem, entry, lccns)
            summary["batches"].append({k: result[k] for k in ("batch", "state", "rows", "pages", "pages_skipped", "duplicate_pages")})
            summary["bytes"] += result["bytes"]
            summary["rows"] += result["rows"]
        return {**summary, "pending": len(pending) - len(summary["batches"])}
    finally:
        db.close()


def newspaper_text_rebuild(ctx) -> dict:
    """Reload the kept title list, listing and per-batch Kansas copies (newest kept file of each key) without network:
    an already loaded copy is unchanged, a missing one is loaded again."""
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NEWSPAPER_DDL)
        root, summary = ctx.root / "data/raw/sql-feeds/newspaper-text", {"titles": None, "listing": None, "batches": {}}
        jobs = [("titles", "titles/chronam-kansas-titles-*.jsonl.gz", CHRONAM_SOURCES["titles"], "kfm_newspaper_titles", TITLE_COLUMNS,
                 lambda path: (title_row(t) for t in _jsonl_rows(path))),
                ("listing", "listing/chronam-ocr-batches-kansas-*.jsonl.gz", CHRONAM_SOURCES["listing"], "kfm_newspaper_batches", BATCH_COLUMNS,
                 lambda path: (batch_row(e) for e in _jsonl_rows(path)))]
        for folder in sorted(root.glob("batches/*")):
            jobs.append((f"batch/{folder.name}", f"batches/{folder.name}/{folder.name}-kansas-ocr-*.jsonl.gz", CHRONAM_SOURCES["pages"],
                         "kfm_newspaper_pages", PAGE_COLUMNS, page_rows))
        for key, pattern, source_id, table, columns, rows in jobs:
            kept = sorted(root.glob(pattern), key=lambda p: core.receipt_for(ctx, p)["retrieved_at"])
            if not kept:
                continue
            path = kept[-1]
            with core.pipeline_lock(ctx):
                result = load_version(db, ctx, source_id=source_id, key=key, path=path, digest=core.file_sha256(path),
                                      url=core.receipt_for(ctx, path)["source_url"], table=table, rows=rows(path), width=len(columns))
            if key.startswith("batch/"):
                summary["batches"][key[6:]] = result["state"]
            else:
                summary[key] = result["state"]
        if summary["titles"] is None and summary["listing"] is None and not summary["batches"]:
            raise FeedError("CHRONAM_NOTHING_KEPT")
        return summary
    finally:
        db.close()
