"""SQL feeds for Kansas aviation and structures: FAA airports (NASR) and obstacles (DOF), USACE dams (NID), USGS and
MSHA mines, FRA grade crossings and the BTS/FRA rail network.

A rebuild of the lost ``sql_feed_things.py`` feeds of 2026-11-02, written against the data those feeds left on the
data volume: the same tables (their DDL copied exactly), the same ``kfm_sql_sources`` receipt keys and ``extra``
fields, the same kept-file names (``<name>-<sha12><ext>`` under the same subfolders) and the same ``kfm_feed_state``
shapes, so an unchanged provider answer is recognized as the version already loaded. Each provider answer is cut
to Kansas, kept gzipped under ``data/raw/sql-feeds/<feed>/`` and loaded with ``keep_version`` under a stable key:
a changed version replaces the one loaded before in one transaction, an unchanged one is not loaded again, and a
return to a version loaded before is reinstated from its kept copy. Network work runs outside the pipeline lock;
database writes inside it. All sources are public U.S. Government data without a key.

Kept forms (from the real kept files): the FAA CSVs, the DOF ``.DAT`` and MSHA's ``Mines.txt`` are kept as the
provider's own lines (header and Kansas lines, line endings as published), so a line the provider malformed is
kept too and loaded with only ``malformed_line`` set; NID, MRDS and FRA rows are re-written with ``csv_bytes``
(minimal quoting, LF); USMIN and NARN features are one canonical JSON object per line. Column names are the
provider's, lower-cased (NID: non-alphanumerics to ``_``). ``geometry_geojson`` is the canonical JSON of a GeoJSON
geometry. Receipt extras not derived from the download (``citation``, ``license``, ``terms``, ``kansas_test``, …)
are fixed strings copied from the existing receipts. The ``dropped_lines``/``dropped_rows`` counts (blank or
unparseable non-Kansas lines of the national file) are reconstructed from the receipts' names, not from code.

``airports``: FAA NASR 28-day subscription, the APT CSV extra (airport master records, 5010):
https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/. The current edition date is read
from FAA's APRA service (``external-api.faa.gov/apra/nasr/chart?edition=current``), or from the 28-day cycle calendar
when that service is gone (it answered 404 from 2026-11-03; ``NASR_CYCLE_ANCHOR``); the zip is
``nfdc.faa.gov/webContent/28DaySub/extra/<DD>_<Mon>_<YYYY>_APT_CSV.zip`` (8.5 MB). It is downloaded only when the
edition in the feed state changes; an edition whose zip is not posted yet (404) is retried next run. Seven members
(APT_BASE, APT_RWY, APT_RWY_END, APT_ATT, APT_RMK, APT_CON, APT_ARS) are cut on ``STATE_CODE`` = KS into seven
``kfm_nasr_*`` tables, each keyed by its member name (``APT_BASE``), kept as ``APT_BASE/APT_BASE-<edition>-KS``.
APT_BASE and APT_RWY_END get a point from their decimal coordinates. A problem in one member is reported after the
other members are done. 4,610 rows on 2026-11-03. License: public domain (17 U.S.C. 105).

``obstacles``: FAA Digital Obstacle File, the daily national zip ``aeronav.faa.gov/Obst_Data/DAILY_DOF_DAT.ZIP``
(15.6 MB; the faa.gov DOF page itself refuses our User-Agent). Its one ``DOF.DAT`` is fixed-width; the four header
lines and every line with state KS in columns 16-17 are kept (``dof-KS``, key ``KS``), the fields split by column
into ``kfm_faa_obstacles`` with heights as INTEGER, decimal coordinates (7 decimals) and a point. The currency date
of line 1 goes into the receipt and the feed state. Re-pulled every 28 days (24,308 obstacles on 2026-11-03).
Terms: https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dof/.

``dams``: USACE National Inventory of Dams, ``nid.sec.usace.army.mil/api/query?sy=@stateKey:KS&out=csv`` (4.8 MB,
no key). All 83 columns plus a point into ``kfm_nid_dams``; rows sorted by NID ID before keeping, so a re-ordered
answer is unchanged (``nid-dams-KS``, key ``KS``). Owner names are public and kept. Re-pulled every 7 days (6,491
dams on 2026-11-03). Terms: https://nid.sec.usace.army.mil/.

``mines``: three sources, each on its own schedule in the feed state (``mrds``, ``usmin``, ``msha`` = date last
pulled); a problem in one is reported after the others are done.
- USGS MRDS, ``mrdata.usgs.gov/mrds/mrds-csv.zip`` (25.8 MB; static since 2022, USGS stopped updating MRDS in 2011):
  rows with state Kansas into ``kfm_mrds_sites`` with a point (``mrds/mrds-KS``, key ``mrds``), every 182 days.
- USGS USMIN (prospect- and mine-related features from historical topographic maps,
  https://doi.org/10.5066/F78W3CHG) through its WFS 1.0.0 (GML) filtered to ``state = 'KS'``, layers ``points`` and
  ``polygons``, each a canonical JSON Lines file of ``{fid, geometry, properties}`` sorted by fid
  (``usmin/usmin-<layer>-KS``, key ``usmin/<layer>``) into ``kfm_usmin_features`` with a bbox; every 91 days.
- MSHA Mines data set, ``arlweb.msha.gov/OpenGovernmentData/DataSets/Mines.zip`` (7.3 MB): the pipe-delimited
  ``Mines.txt`` lines with STATE = KS into ``kfm_msha_mines`` (``msha/mines-KS``, key ``msha``), every 7 days.
  Coordinates are as reported, so a portable plant's can be out of state.
9,283 rows on 2026-11-03. Terms: https://mrdata.usgs.gov/usmin/, https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp,
https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits.

``grade-crossings``: FRA Crossing Inventory Data (Form 71), current, Socrata dataset ``m2f8-22s6`` on
data.transportation.gov: SODA CSV pages of 5,000 with ``statecode='20'`` ordered by ``:id``; the total must match
``count(*)``. All 263 columns plus a point into ``kfm_fra_crossings`` (``fra-crossings-KS``, key ``KS``); the
dataset's name, ``rowsUpdatedAt`` and license come from its metadata. Re-pulled every 28 days (15,418 on 2026-11-03).

``rail-lines``: BTS NTAD North American Rail Network Lines (FRA), the ArcGIS FeatureServer layer 0 queried with
``STATEAB='KS'``, ``outSR=4326``, GeoJSON pages of 2,000 by OBJECTID; the count is checked against
``returnCountOnly``. Features sorted by OBJECTID, one canonical ``{geometry, properties, type}`` per line
(``KS/rail-lines-KS-KS``, key ``KS``) into ``kfm_narn_rail_lines``, whose attribute columns are untyped so the
service's own value types are stored, with the line geometry and its bbox. Re-pulled every 28 days (6,364 segments
on 2026-11-03). License: U.S. Government work, unrestricted public use.
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
import gzip
import io
import json
from pathlib import Path
import re
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, csv_bytes, keep_version, number, read_csv, save_state
from tools.local_data.sql_feeds import FeedError

# --- Shared ----------------------------------------------------------------------------------------

PUBLIC_DOMAIN = "public domain (U.S. Government work, 17 U.S.C. 105)"
KANSAS = "KS"
LIMIT = 256_000_000


def ddl(table: str, columns, types: dict, indexes) -> str:
    """The exact DDL of the existing tables: quoted column names, TEXT unless typed ("" for an untyped column)."""
    quoted = lambda names: ", ".join('"' + n + '"' for n in names)
    body = ", ".join('"' + c + '"' + (f" {types.get(c, 'TEXT')}" if types.get(c, "TEXT") else "") for c in columns)
    return (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
            f"PRIMARY KEY(file_id, row_number));\n"
            + "".join(f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(i)} ON {table}({quoted(i)});\n" for i in indexes))


def point(lon, lat) -> str | None:
    return core.canonical({"type": "Point", "coordinates": [lon, lat]}) if lon is not None and lat is not None else None


def bbox(geometry: dict) -> tuple:
    """(min_lon, min_lat, max_lon, max_lat) of any GeoJSON geometry."""
    xs, ys = [], []

    def walk(value):
        if isinstance(value[0], (int, float)):
            xs.append(value[0])
            ys.append(value[1])
        else:
            for part in value:
                walk(part)
    walk(geometry["coordinates"])
    return (min(xs), min(ys), max(xs), max(ys))


def fetch(ctx, url: str, code: str, **options):
    """ctx.fetch with HTTP 429 reported as <CODE>_RATE_LIMITED."""
    try:
        return ctx.fetch(url, limit=options.pop("limit", LIMIT), **options)
    except FeedError as error:
        if str(error).startswith("HTTP_429"):
            raise FeedError(f"{code}_RATE_LIMITED {url}") from None
        raise


def member(archive: bytes, suffix: str, code: str) -> bytes:
    """The one member of a zip whose name ends with suffix (case-insensitive)."""
    try:
        with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
            names = [n for n in zipped.namelist() if n.upper().endswith(suffix.upper())]
            if len(names) != 1:
                raise FeedError(f"{code}_MEMBER_MISSING {suffix}")
            return zipped.read(names[0])
    except zipfile.BadZipFile:
        raise FeedError(f"{code}_ARCHIVE_UNREADABLE") from None


def _fields(text: str, delimiter: str) -> list:
    try:
        return next(csv.reader([text], delimiter=delimiter))
    except (csv.Error, StopIteration):
        return []


def cut_lines(body: bytes, header, *, state_at: int, code: str, encoding: str = "utf-8", delimiter: str = ","):
    """Cut a delimited text file to its Kansas lines, kept as published (header first, line endings as they are).

    A line of the header's width whose state field is KS is kept; a line of another width is kept when its
    state field still reads KS (loaded later with only malformed_line set) and counted in malformed, else it is
    dropped and counted. Returns (lines, malformed, dropped)."""
    lines = body.splitlines(keepends=True)
    if not lines or _fields(lines[0].decode(encoding, "replace").rstrip("\r\n"), delimiter) != list(header):
        raise FeedError(f"{code}_COLUMNS_CHANGED")
    kept, malformed, dropped = [lines[0]], 0, 0
    for line in lines[1:]:
        fields = _fields(line.decode(encoding, "replace").rstrip("\r\n"), delimiter)
        kansas = len(fields) > state_at and fields[state_at] == KANSAS
        if len(fields) == len(header) and kansas:
            kept.append(line)
        elif kansas:
            kept.append(line)
            malformed += 1
        elif len(fields) != len(header):
            dropped += 1
    return kept, malformed, dropped


def line_rows(path: Path, header, width: int, values, *, code: str, encoding: str = "utf-8", delimiter: str = ","):
    """The table rows of a kept line file: values(fields) for a well-formed line, else only malformed_line (last)."""
    with gzip.open(path, "rb") as handle:
        lines = handle.read().splitlines()
    if not lines or _fields(lines[0].decode(encoding, "replace"), delimiter) != list(header):
        raise FeedError(f"{code}_COLUMNS_CHANGED {path.name}")
    for line in lines[1:]:
        text = line.decode(encoding, "replace")
        fields = _fields(text, delimiter)
        yield (*values(fields), None) if len(fields) == len(header) else (*([None] * (width - 1)), text)


def jsonl(records) -> bytes:
    return core.gz("".join(core.canonical(r) + "\n" for r in records).encode())


def jsonl_records(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


# --- Airports: FAA NASR APT CSV, one version per member and edition -------------------------------

APRA = "https://external-api.faa.gov/apra/nasr/chart?edition=current"
NASR_ZIP = "https://nfdc.faa.gov/webContent/28DaySub/extra/{edition}_APT_CSV.zip"
NASR_TERMS = "https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/"
NASR_CITATION = "Federal Aviation Administration, NASR 28-day subscription, APT CSV"
NASR_SOURCE = "faa-nasr-kansas"
NASR_FILES = ("APT_BASE", "APT_RWY", "APT_RWY_END", "APT_ATT", "APT_RMK", "APT_CON", "APT_ARS")
NASR_TABLES = {"APT_BASE": "kfm_nasr_airports", "APT_RWY": "kfm_nasr_runways", "APT_RWY_END": "kfm_nasr_runway_ends",
               "APT_ATT": "kfm_nasr_attendance", "APT_RMK": "kfm_nasr_remarks", "APT_CON": "kfm_nasr_contacts",
               "APT_ARS": "kfm_nasr_arresting_systems"}
_NASR_COMMON = "eff_date site_no site_type_code state_code arpt_id city country_code"
NASR_COLUMNS = {stem: (_NASR_COMMON + " " + rest).split() for stem, rest in {
    "APT_BASE": """region_code ado_code state_name county_name county_assoc_state arpt_name ownership_type_code facility_use_code
        lat_deg lat_min lat_sec lat_hemis lat_decimal long_deg long_min long_sec long_hemis long_decimal survey_method_code elev
        elev_method_code mag_varn mag_hemis mag_varn_year tpa chart_name dist_city_to_airport direction_code acreage resp_artcc_id
        computer_id artcc_name fss_on_arpt_flag fss_id fss_name phone_no toll_free_no alt_fss_id alt_fss_name alt_toll_free_no
        notam_id notam_flag activation_date arpt_status far_139_type_code far_139_carrier_ser_code arff_cert_type_date nasp_code
        asp_anlys_dtrm_code cust_flag lndg_rights_flag joint_use_flag mil_lndg_flag inspect_method_code inspector_code
        last_inspection last_info_response fuel_types airframe_repair_ser_code pwr_plant_repair_ser bottled_oxy_type bulk_oxy_type
        lgt_sked bcn_lgt_sked twr_type_code seg_circle_mkr_flag bcn_lens_color lndg_fee_flag medical_use_flag arpt_psn_source
        position_src_date arpt_elev_source elevation_src_date contr_fuel_avbl trns_strg_buoy_flag trns_strg_hgr_flag
        trns_strg_tie_flag other_services wind_indcr_flag icao_id min_op_network user_fee_flag cta""",
    "APT_RWY": """rwy_id rwy_len rwy_width surface_type_code cond treatment_code pavement_classification pcn_pcr_number
        pavement_type_code subgrade_strength_code tire_pres_code dtrm_method_code rwy_lgt_code rwy_len_source length_source_date
        gross_wt_sw gross_wt_dw gross_wt_dtw gross_wt_ddtw""",
    "APT_RWY_END": """rwy_id rwy_end_id true_alignment ils_type right_hand_traffic_pat_flag rwy_marking_type_code rwy_marking_cond
        rwy_end_lat_deg rwy_end_lat_min rwy_end_lat_sec rwy_end_lat_hemis lat_decimal rwy_end_long_deg rwy_end_long_min
        rwy_end_long_sec rwy_end_long_hemis long_decimal rwy_end_elev thr_crossing_hgt visual_glide_path_angle displaced_thr_lat_deg
        displaced_thr_lat_min displaced_thr_lat_sec displaced_thr_lat_hemis lat_displaced_thr_decimal displaced_thr_long_deg
        displaced_thr_long_min displaced_thr_long_sec displaced_thr_long_hemis long_displaced_thr_decimal displaced_thr_elev
        displaced_thr_len tdz_elev vgsi_code rwy_visual_range_equip_code rwy_vsby_value_equip_flag apch_lgt_system_code
        rwy_end_lgts_flag cntrln_lgts_avbl_flag tdz_lgt_avbl_flag obstn_type obstn_mrkd_code far_part_77_code obstn_clnc_slope
        obstn_hgt dist_from_thr cntrln_offset cntrln_dir_code rwy_grad rwy_grad_direction rwy_end_psn_source rwy_end_psn_date
        rwy_end_elev_source rwy_end_elev_date dspl_thr_psn_source rwy_end_dspl_thr_psn_date dspl_thr_elev_source
        rwy_end_dspl_thr_elev_date tdz_elev_source rwy_end_tdz_elev_date tkof_run_avbl tkof_dist_avbl aclt_stop_dist_avbl
        lndg_dist_avbl lahso_ald rwy_end_intersect_lahso lahso_desc lahso_lat lat_lahso_decimal lahso_long long_lahso_decimal
        lahso_psn_source rwy_end_lahso_psn_date""",
    "APT_ATT": "sked_seq_no month day hour",
    "APT_RMK": "legacy_element_number tab_name ref_col_name element ref_col_seq_no remark",
    "APT_CON": "title name address1 address2 title_city state zip_code zip_plus_four phone_no",
    "APT_ARS": "rwy_id rwy_end_id arrest_device_code",
}.items()}
NASR_GEOMETRY = ("APT_BASE", "APT_RWY_END")
NASR_DDL = "".join(ddl(NASR_TABLES[stem], NASR_COLUMNS[stem] + (["geometry_geojson"] if stem in NASR_GEOMETRY else []) + ["malformed_line"],
                       {"lat_decimal": "REAL", "long_decimal": "REAL"},
                       [("site_no",)] if stem in ("APT_ATT", "APT_RMK", "APT_ARS") else [("name",), ("site_no",)] if stem == "APT_CON"
                       else [("arpt_id",), ("county_name",), ("site_no",)] if stem == "APT_BASE" else [("arpt_id",), ("site_no",)])
                   for stem in NASR_FILES)
EDITION_DATE = re.compile(r'editionDate["\s:=]+"?(\d{2})/(\d{2})/(\d{4})')
NASR_CYCLE_ANCHOR = date(2026, 10, 29)   # one effective date of the 28-day cycle (every edition is a whole number of cycles from it)
NASR_CYCLE_DAYS = 28


def nasr_edition(ctx) -> str:
    """The current NASR edition date (YYYY-MM-DD): from FAA's APRA service (JSON or XML) when it answers, else from
    the 28-day cycle calendar. APRA's ``nasr/chart`` query started answering 404 on 2026-11-03 while its sibling
    ``dtpp/chart`` still worked and the zips were still posted, so a missing service is not a failure: the edition
    in effect today is the latest cycle date not after today. An answer that cannot be read is still an error."""
    fetched = fetch(ctx, APRA, "NASR", limit=1_000_000, missing_ok=True)
    if fetched is not None:
        found = EDITION_DATE.search(fetched.body.decode("utf-8", "replace"))
        if not found:
            raise FeedError("NASR_EDITION_UNREADABLE")
        month, day, year = found.groups()
        return f"{year}-{month}-{day}"
    cycles = (ctx.now().date() - NASR_CYCLE_ANCHOR).days // NASR_CYCLE_DAYS
    return str(NASR_CYCLE_ANCHOR + timedelta(days=NASR_CYCLE_DAYS * cycles))


def _nasr_values(stem: str):
    columns = NASR_COLUMNS[stem]
    if stem not in NASR_GEOMETRY:
        return lambda fields: tuple(fields)
    lat, lon = columns.index("lat_decimal"), columns.index("long_decimal")

    def values(fields):
        values = list(fields)
        values[lat], values[lon] = number(fields[lat]), number(fields[lon])
        return (*values, point(values[lon], values[lat]))
    return values


def _nasr_rows(path: Path, stem: str):
    header = [c.upper() for c in NASR_COLUMNS[stem]]
    width = len(NASR_COLUMNS[stem]) + (2 if stem in NASR_GEOMETRY else 1)
    return line_rows(path, header, width, _nasr_values(stem), code="NASR")


def airports(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NASR_DDL)
        state = core.get_state(db, "airports")
        edition = nasr_edition(ctx)
        if state.get("edition") == edition:
            return {"state": "not_due", "edition": edition}
        url = NASR_ZIP.format(edition=datetime.strptime(edition, "%Y-%m-%d").strftime("%d_%b_%Y"))
        fetched = fetch(ctx, url, "NASR", timeout=600, missing_ok=True)
        if fetched is None:
            ctx.note("nasr_edition_not_posted", edition=edition, url=url)
            return {"state": "not_posted", "edition": edition}
        archive = {"bytes": len(fetched.body), "sha256": core.sha256(fetched.body)}
        summary, problems = {"edition": edition, "rows": 0, "loaded": [], "unchanged": []}, []
        for stem in NASR_FILES:
            try:
                header = [c.upper() for c in NASR_COLUMNS[stem]]
                lines, malformed, dropped = cut_lines(member(fetched.body, stem + ".csv", "NASR"), header, state_at=3, code="NASR")
                result = keep_version(ctx, db, feed="airports", source_id=NASR_SOURCE, key=stem, name=f"{stem}/{stem}-{edition}-KS", ext=".csv.gz",
                                      body=core.gz(b"".join(lines)), url=fetched.url, fetched=fetched, table=NASR_TABLES[stem],
                                      width=len(NASR_COLUMNS[stem]) + (2 if stem in NASR_GEOMETRY else 1), rows=lambda path, stem=stem: _nasr_rows(path, stem),
                                      extra={"archive": archive, "citation": NASR_CITATION, "dropped_lines": dropped, "edition": edition,
                                             "license": PUBLIC_DOMAIN, "malformed_lines": malformed, "rows": len(lines) - 1, "terms": NASR_TERMS})
            except FeedError as error:
                problems.append(f"{stem}: {error}")
                continue
            summary["unchanged" if result["state"] == "unchanged" else "loaded"].append(stem)
            summary["rows"] += result["rows"]
        if problems:
            raise FeedError("NASR_FILES_FAILED " + "; ".join(problems))
        save_state(ctx, db, "airports", {"edition": edition})
        return summary
    finally:
        db.close()


# --- Obstacles: the FAA Digital Obstacle File, cut to state KS ------------------------------------

DOF_ZIP = "https://aeronav.faa.gov/Obst_Data/DAILY_DOF_DAT.ZIP"
DOF_TERMS = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dof/"
DOF_CITATION = "Federal Aviation Administration, Digital Obstacle File (daily)"
DOF_SOURCE = "faa-dof-kansas"
DOF_TABLE = "kfm_faa_obstacles"
DOF_COLUMNS = ("oas_number oas_code obstacle_number verification_status country state city lat_degrees lat_minutes lat_seconds lat_hemisphere "
               "lon_degrees lon_minutes lon_seconds lon_hemisphere obstacle_type quantity agl_height_ft amsl_height_ft lighting "
               "horizontal_accuracy vertical_accuracy marking faa_study_number action julian_date latitude longitude geometry_geojson").split()
DOF_DDL = ddl(DOF_TABLE, DOF_COLUMNS, {"oas_number": "TEXT NOT NULL", "quantity": "INTEGER", "agl_height_ft": "INTEGER", "amsl_height_ft": "INTEGER",
                                       "latitude": "REAL", "longitude": "REAL"}, [("city",), ("oas_number",), ("obstacle_type",)])
DOF_FIELDS = (("oas_number", 0, 9), ("verification_status", 10, 11), ("country", 12, 14), ("state", 15, 17), ("city", 18, 34),
              ("lat_degrees", 35, 37), ("lat_minutes", 38, 40), ("lat_seconds", 41, 46), ("lat_hemisphere", 46, 47),
              ("lon_degrees", 48, 51), ("lon_minutes", 52, 54), ("lon_seconds", 55, 60), ("lon_hemisphere", 60, 61),
              ("obstacle_type", 62, 80), ("quantity", 81, 82), ("agl_height_ft", 83, 88), ("amsl_height_ft", 89, 94), ("lighting", 95, 96),
              ("horizontal_accuracy", 97, 98), ("vertical_accuracy", 99, 100), ("marking", 101, 102), ("faa_study_number", 103, 117),
              ("action", 118, 119), ("julian_date", 120, 127))
DOF_HEADER_LINES = 4
DOF_CURRENCY = re.compile(r"CURRENCY DATE\s*=\s*(\S+)")
DOF_KANSAS_TEST = "state KS (columns 16-17)"
DOF_RECHECK_DAYS = 28


def _dof_integer(text: str):
    text = text.strip()
    if not text:
        return None
    if not text.isdigit():
        raise FeedError(f"DOF_NOT_A_NUMBER {text!r}")
    return int(text)


def _dof_degrees(degrees: str, minutes: str, seconds: str, hemisphere: str):
    value = number(degrees.strip()) + number(minutes.strip()) / 60 + number(seconds.strip()) / 3600
    return round(-value if hemisphere in ("S", "W") else value, 7)


def dof_values(line: str) -> tuple:
    if len(line) < DOF_FIELDS[-1][2]:
        raise FeedError(f"DOF_LINE_SHORT {line[:20]!r}")
    field = {name: line[start:end].strip() for name, start, end in DOF_FIELDS}
    if not re.fullmatch(r"\d{2}-\d{6}", field["oas_number"]):
        raise FeedError(f"DOF_OAS_NUMBER {field['oas_number']!r}")
    code, serial = field["oas_number"].split("-")
    lat = _dof_degrees(field["lat_degrees"], field["lat_minutes"], field["lat_seconds"], field["lat_hemisphere"])
    lon = _dof_degrees(field["lon_degrees"], field["lon_minutes"], field["lon_seconds"], field["lon_hemisphere"])
    return tuple(_dof_integer(field[c]) if c in ("quantity", "agl_height_ft", "amsl_height_ft") else
                 code if c == "oas_code" else serial if c == "obstacle_number" else
                 lat if c == "latitude" else lon if c == "longitude" else point(lon, lat) if c == "geometry_geojson" else field[c]
                 for c in DOF_COLUMNS)


def _dof_lines(body: bytes) -> tuple[list, str]:
    """(kept lines, currency date): the four header lines and every Kansas line, as published."""
    lines = body.splitlines(keepends=True)
    head = [l.decode("latin-1").rstrip("\r\n") for l in lines[:DOF_HEADER_LINES]]
    found = DOF_CURRENCY.search(head[0]) if head else None
    if not found or len(head) < DOF_HEADER_LINES or not head[-1].startswith("---") or "OAS#" not in head[2]:
        raise FeedError("DOF_FORMAT_CHANGED")
    kept = lines[:DOF_HEADER_LINES] + [l for l in lines[DOF_HEADER_LINES:] if l[15:17] == b"KS"]
    return kept, found.group(1)


def _dof_rows(path: Path):
    with gzip.open(path, "rb") as handle:
        lines, _ = _dof_lines(handle.read())
    for line in lines[DOF_HEADER_LINES:]:
        yield dof_values(line.decode("latin-1").rstrip("\r\n"))


def obstacles(ctx, recheck_days: int = DOF_RECHECK_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(DOF_DDL)
        state, today = core.get_state(db, "obstacles"), ctx.now().date()
        age = age_days(state, "fetched", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "fetched": state["fetched"], "currency_date": state.get("currency_date")}
        fetched = fetch(ctx, DOF_ZIP, "DOF", timeout=600)
        lines, currency = _dof_lines(member(fetched.body, ".DAT", "DOF"))
        if len(lines) == DOF_HEADER_LINES:
            raise FeedError("DOF_NO_KANSAS_ROWS")
        for line in lines[DOF_HEADER_LINES:]:
            dof_values(line.decode("latin-1").rstrip("\r\n"))
        result = keep_version(ctx, db, feed="obstacles", source_id=DOF_SOURCE, key=KANSAS, name="dof-KS", ext=".dat.gz", body=core.gz(b"".join(lines)),
                              url=fetched.url, fetched=fetched, original=fetched.body, table=DOF_TABLE, width=len(DOF_COLUMNS), rows=_dof_rows,
                              extra={"citation": DOF_CITATION, "currency_date": currency, "kansas_test": DOF_KANSAS_TEST, "license": PUBLIC_DOMAIN,
                                     "rows": len(lines) - DOF_HEADER_LINES, "terms": DOF_TERMS})
        save_state(ctx, db, "obstacles", {"currency_date": currency, "fetched": str(today)})
        return {**result, "currency_date": currency, "obstacles": len(lines) - DOF_HEADER_LINES}
    finally:
        db.close()


# --- Dams: the National Inventory of Dams, Kansas query -------------------------------------------

NID_URL = "https://nid.sec.usace.army.mil/api/query?sy=@stateKey:KS&out=csv"
NID_TERMS = "https://nid.sec.usace.army.mil/"
NID_CITATION = "U.S. Army Corps of Engineers, National Inventory of Dams"
NID_SOURCE = "usace-nid-kansas"
NID_TABLE = "kfm_nid_dams"
NID_COLUMNS = """dam_name other_names former_names nid_id other_structure_id federal_id owner_names owner_types primary_owner_type
    number_of_associated_structures is_associated_structure designer_names non_federal_dam_on_federal_property primary_purpose purposes
    source_agency state_or_federal_agency_id latitude longitude state county city distance_to_nearest_city_miles river_or_stream_name
    congressional_district state_regulated_dam state_jurisdictional_dam state_regulatory_agency state_permitting_authority
    state_inspection_authority state_enforcement_authority federally_regulated_dam federal_agency_owners federal_agency_involvement_funding
    federal_agency_involvement_design federal_agency_involvement_construction federal_agency_involvement_regulatory
    federal_agency_involvement_inspection federal_agency_involvement_operation federal_agency_involvement_other
    built_under_the_authority_of_the_secretary_of_agriculture nrcs_watershed_dam_authorization primary_dam_type dam_types core_types foundation
    dam_height_ft hydraulic_height_ft structural_height_ft nid_height_ft nid_height_category dam_length_ft volume_cubic_yards year_completed
    year_completed_category years_modified nid_storage_acre_ft max_storage_acre_ft normal_storage_acre_ft surface_area_acres
    drainage_area_sq_miles max_discharge_cubic_ft_second spillway_type spillway_width_ft number_of_locks length_of_locks_ft lock_width_ft
    length_of_secondary_lock_ft secondary_lock_width_ft outlet_gate_type data_last_updated last_inspection_date inspection_frequency
    hazard_potential_classification eap_prepared eap_last_revision_date website_url operational_status operational_status_date
    inundation_maps_added_to_nid american_indian_alaska_native_native_hawaiian has_photo
    non_usace_dam_with_usace_flood_control_storage_authority_section_7_flood_control_act_of_1944""".split()
NID_DDL = ddl(NID_TABLE, NID_COLUMNS + ["geometry_geojson"], {"latitude": "REAL", "longitude": "REAL"}, [("county",), ("dam_name",), ("nid_id",)])
NID_RECHECK_DAYS = 7


def column_name(header: str) -> str:
    """A provider's column title as a table column: lower case, runs of non-alphanumerics as one underscore."""
    return re.sub(r"[^a-z0-9]+", "_", header.lower()).strip("_")


def _nid_values(fields):
    lat, lon = number(fields[NID_COLUMNS.index("latitude")]), number(fields[NID_COLUMNS.index("longitude")])
    values = list(fields)
    values[NID_COLUMNS.index("latitude")], values[NID_COLUMNS.index("longitude")] = lat, lon
    return (*values, point(lon, lat))


def _nid_rows(path: Path, header: list):
    for row in read_csv(path, header, "NID"):
        yield _nid_values(row)


def dams(ctx, recheck_days: int = NID_RECHECK_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NID_DDL)
        state, today = core.get_state(db, "dams"), ctx.now().date()
        age = age_days(state, "fetched", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "fetched": state["fetched"], "records": state.get("records")}
        fetched = fetch(ctx, NID_URL, "NID", timeout=600)
        rows = list(csv.reader(io.StringIO(fetched.body.decode("utf-8-sig"), newline="")))
        if not rows or [column_name(h) for h in rows[0]] != NID_COLUMNS:
            raise FeedError("NID_COLUMNS_CHANGED")
        header, records = rows[0], rows[1:]
        if any(len(r) != len(header) for r in records):
            raise FeedError("NID_ROW_SHAPE")
        if not records:
            raise FeedError("NID_NO_KANSAS_ROWS")
        if any(r[NID_COLUMNS.index("state")] != "Kansas" for r in records):
            raise FeedError("NID_NOT_KANSAS")
        records.sort(key=lambda r: r[NID_COLUMNS.index("nid_id")])
        for record in records:
            _nid_values(record)
        result = keep_version(ctx, db, feed="dams", source_id=NID_SOURCE, key=KANSAS, name="nid-dams-KS", ext=".csv.gz",
                              body=core.gz(csv_bytes([header, *records])), url=fetched.url, original=fetched.body, table=NID_TABLE,
                              width=len(NID_COLUMNS) + 1, rows=lambda path: _nid_rows(path, header),
                              extra={"citation": NID_CITATION, "license": PUBLIC_DOMAIN, "rows": len(records), "terms": NID_TERMS})
        save_state(ctx, db, "dams", {"fetched": str(today), "records": len(records)})
        return {**result, "records": len(records)}
    finally:
        db.close()


# --- Mines: USGS MRDS, USGS USMIN and MSHA mines ----------------------------------------------------

MRDS_ZIP = "https://mrdata.usgs.gov/mrds/mrds-csv.zip"
MRDS_TERMS = "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits"
MRDS_CITATION = "U.S. Geological Survey, Mineral Resources Data System (MRDS), https://doi.org/10.5066/P9DYLWMP"
MRDS_SOURCE = "usgs-mrds-kansas"
MRDS_TABLE = "kfm_mrds_sites"
MRDS_COLUMNS = """dep_id url mrds_id mas_id site_name latitude longitude region country state county com_type commod1 commod2 commod3 oper_type
    dep_type prod_size dev_stat ore gangue other_matl orebody_fm work_type model alteration conc_proc names ore_ctrl reporter hrock_unit
    hrock_type arock_unit arock_type structure tectonic ref yfp_ba yr_fst_prd ylp_ba yr_lst_prd dy_ba disc_yr prod_yrs discr score""".split()
MRDS_DDL = ddl(MRDS_TABLE, MRDS_COLUMNS + ["geometry_geojson"], {"latitude": "REAL", "longitude": "REAL"}, [("commod1",), ("county",), ("dep_id",)])
MRDS_RECHECK_DAYS = 182

USMIN_WFS = ("https://mrdata.usgs.gov/services/wfs/usmin?request=GetFeature&service=WFS&typename={layer}&filter="
             + urllib.parse.quote("<Filter><PropertyIsEqualTo><PropertyName>state</PropertyName><Literal>KS</Literal></PropertyIsEqualTo></Filter>")
             + "&version=1.0.0")
USMIN_TERMS = "https://mrdata.usgs.gov/usmin/"
USMIN_CITATION = ("Horton, J.D., and San Juan, C.A., Prospect- and mine-related features from U.S. Geological Survey 7.5- and 15-minute "
                  "topographic quadrangle maps of the United States, https://doi.org/10.5066/F78W3CHG")
USMIN_SOURCE = "usgs-usmin-kansas"
USMIN_TABLE = "kfm_usmin_features"
USMIN_LAYERS = ("points", "polygons")
USMIN_PROPERTIES = "state county ftr_type ftr_name ftr_azimut topo_name topo_date topo_scale compiledby remarks gda_id scanid dir url".split()
USMIN_COLUMNS = ["layer", "fid", *USMIN_PROPERTIES, "geometry_geojson", "min_lon", "min_lat", "max_lon", "max_lat"]
USMIN_DDL = ddl(USMIN_TABLE, USMIN_COLUMNS, {"layer": "TEXT NOT NULL", "fid": "INTEGER NOT NULL", "min_lon": "REAL", "min_lat": "REAL",
                                             "max_lon": "REAL", "max_lat": "REAL"}, [("county",), ("ftr_type",), ("layer", "fid")])
USMIN_FILTER = "state = 'KS'"
USMIN_RECHECK_DAYS = 91
GML, WFS = "{http://www.opengis.net/gml}", "{http://www.opengis.net/wfs}"

MSHA_ZIP = "https://arlweb.msha.gov/OpenGovernmentData/DataSets/Mines.zip"
MSHA_TERMS = "https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp"
MSHA_CITATION = "Mine Safety and Health Administration, Mines data set"
MSHA_SOURCE = "msha-mines-kansas"
MSHA_TABLE = "kfm_msha_mines"
MSHA_COLUMNS = """mine_id current_mine_name coal_metal_ind current_mine_type current_mine_status current_status_dt current_controller_id
    current_controller_name current_operator_id current_operator_name state bom_state_cd fips_cnty_cd fips_cnty_nm cong_dist_cd company_type
    current_controller_begin_dt district office_cd office_name assess_ctrl_no primary_sic_cd primary_sic primary_sic_cd_1 primary_sic_cd_sfx
    secondary_sic_cd secondary_sic secondary_sic_cd_1 secondary_sic_cd_sfx primary_canvass_cd primary_canvass secondary_canvass_cd
    secondary_canvass current_103i current_103i_dt portable_operation portable_fips_st_cd days_per_week hours_per_shift prod_shifts_per_day
    maint_shifts_per_day no_employees part48_training longitude latitude avg_mine_height mine_gas_category_cd methane_liberation
    no_producing_pits no_nonproducing_pits no_tailing_ponds pillar_recovery_used highwall_miner_used multiple_pits miners_rep_ind
    safety_committee_ind miles_from_office directions_to_mine nearest_town""".split()
MSHA_HEADER = [c.upper() for c in MSHA_COLUMNS]
MSHA_DDL = ddl(MSHA_TABLE, MSHA_COLUMNS + ["geometry_geojson", "malformed_line"], {"longitude": "REAL", "latitude": "REAL"},
               [("current_mine_name",), ("fips_cnty_cd",), ("mine_id",)])
MSHA_ENCODING = "cp1252"
MSHA_RECHECK_DAYS = 7
MINES_DDL = MRDS_DDL + USMIN_DDL + MSHA_DDL


def _mrds_values(fields):
    lat, lon = number(fields[MRDS_COLUMNS.index("latitude")]), number(fields[MRDS_COLUMNS.index("longitude")])
    values = list(fields)
    values[MRDS_COLUMNS.index("latitude")], values[MRDS_COLUMNS.index("longitude")] = lat, lon
    return (*values, point(lon, lat))


def _mrds_rows(path: Path):
    for row in read_csv(path, MRDS_COLUMNS, "MRDS"):
        yield _mrds_values(row)


def _mrds(ctx, db) -> dict:
    fetched = fetch(ctx, MRDS_ZIP, "MRDS", timeout=900)
    rows = csv.reader(io.StringIO(member(fetched.body, ".csv", "MRDS").decode("utf-8", "replace"), newline=""))
    if next(rows, None) != MRDS_COLUMNS:
        raise FeedError("MRDS_COLUMNS_CHANGED")
    kept, dropped = [], 0
    for row in rows:
        if len(row) != len(MRDS_COLUMNS):
            dropped += 1
        elif row[MRDS_COLUMNS.index("state")] == "Kansas":
            kept.append(row)
    if not kept:
        raise FeedError("MRDS_NO_KANSAS_ROWS")
    for row in kept:
        _mrds_values(row)
    return keep_version(ctx, db, feed="mines", source_id=MRDS_SOURCE, key="mrds", name="mrds/mrds-KS", ext=".csv.gz",
                        body=core.gz(csv_bytes([MRDS_COLUMNS, *kept])), url=fetched.url, fetched=fetched, original=fetched.body, table=MRDS_TABLE,
                        width=len(MRDS_COLUMNS) + 1, rows=_mrds_rows,
                        extra={"citation": MRDS_CITATION, "dropped_rows": dropped, "license": PUBLIC_DOMAIN, "rows": len(kept), "terms": MRDS_TERMS})


def _gml_coordinates(element) -> list:
    text = element.findtext(GML + "coordinates")
    if text is None:
        raise FeedError("USMIN_GEOMETRY_SHAPE")
    return [[float(x) for x in pair.split(",")] for pair in text.split()]


def _gml_polygon(polygon) -> list:
    rings = [_gml_coordinates(polygon.find(GML + "outerBoundaryIs/" + GML + "LinearRing"))]
    rings += [_gml_coordinates(inner.find(GML + "LinearRing")) for inner in polygon.findall(GML + "innerBoundaryIs")]
    return rings


def gml_geometry(element) -> dict:
    """A GML 2 geometry (Point, LineString, Polygon or their Multi forms) as a GeoJSON geometry."""
    kind = element.tag.removeprefix(GML)
    if kind == "Point":
        return {"type": "Point", "coordinates": _gml_coordinates(element)[0]}
    if kind == "LineString":
        return {"type": "LineString", "coordinates": _gml_coordinates(element)}
    if kind == "Polygon":
        return {"type": "Polygon", "coordinates": _gml_polygon(element)}
    if kind == "MultiPolygon":
        return {"type": "MultiPolygon", "coordinates": [_gml_polygon(p) for p in element.iter(GML + "Polygon")]}
    if kind == "MultiLineString":
        return {"type": "MultiLineString", "coordinates": [_gml_coordinates(l) for l in element.iter(GML + "LineString")]}
    if kind == "MultiPoint":
        return {"type": "MultiPoint", "coordinates": [_gml_coordinates(p)[0] for p in element.iter(GML + "Point")]}
    raise FeedError(f"USMIN_GEOMETRY_SHAPE {kind}")


def usmin_features(body: bytes, layer: str) -> list:
    """The features of a WFS 1.0.0 GML answer as {fid, geometry, properties}, sorted by fid."""
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        raise FeedError(f"USMIN_RESPONSE_SHAPE {layer}") from None
    if root.tag != WFS + "FeatureCollection":
        raise FeedError(f"USMIN_RESPONSE_SHAPE {layer} {root.tag.rpartition('}')[2]}")
    features = []
    for holder in root.iter(GML + "featureMember"):
        for feature in holder:
            fid = feature.get("fid", "")
            if not re.fullmatch(rf"{layer}\.\d+", fid):
                raise FeedError(f"USMIN_FEATURE_ID {layer} {fid!r}")
            geometry, properties = None, {}
            for child in feature:
                name = child.tag.rpartition("}")[2]
                if child.tag == GML + "boundedBy":
                    continue
                if name == "geometry":
                    geometry = gml_geometry(next(iter(child)))
                else:
                    properties[name] = child.text or ""
            if geometry is None or set(properties) - set(USMIN_PROPERTIES) or "state" not in properties:
                raise FeedError(f"USMIN_FIELDS_CHANGED {layer}")
            if properties["state"] != KANSAS:
                raise FeedError(f"USMIN_NOT_KANSAS {layer} {fid}")
            features.append({"fid": int(fid.rpartition(".")[2]), "geometry": geometry, "properties": properties})
    features.sort(key=lambda f: f["fid"])
    return features


def _usmin_rows(path: Path, layer: str):
    for feature in jsonl_records(path):
        properties = feature["properties"]
        yield (layer, feature["fid"], *(properties.get(c) for c in USMIN_PROPERTIES), core.canonical(feature["geometry"]), *bbox(feature["geometry"]))


def _usmin(ctx, db) -> dict:
    summary = {"rows": 0}
    for layer in USMIN_LAYERS:
        fetched = fetch(ctx, USMIN_WFS.format(layer=layer), "USMIN", timeout=900)
        features = usmin_features(fetched.body, layer)
        if not features:
            raise FeedError(f"USMIN_NO_KANSAS_ROWS {layer}")
        result = keep_version(ctx, db, feed="mines", source_id=USMIN_SOURCE, key=f"usmin/{layer}", name=f"usmin/usmin-{layer}-KS", ext=".jsonl.gz",
                              body=jsonl(features), url=fetched.url, original=fetched.body, table=USMIN_TABLE, width=len(USMIN_COLUMNS),
                              rows=lambda path, layer=layer: _usmin_rows(path, layer),
                              extra={"citation": USMIN_CITATION, "filter": USMIN_FILTER, "layer": layer, "license": PUBLIC_DOMAIN,
                                     "rows": len(features), "terms": USMIN_TERMS})
        summary[layer] = result["state"]
        summary["rows"] += result["rows"]
    return summary


def _msha_values(fields):
    lon, lat = number(fields[MSHA_COLUMNS.index("longitude")]), number(fields[MSHA_COLUMNS.index("latitude")])
    values = list(fields)
    values[MSHA_COLUMNS.index("longitude")], values[MSHA_COLUMNS.index("latitude")] = lon, lat
    return (*values, point(lon, lat))


def _msha_rows(path: Path):
    return line_rows(path, MSHA_HEADER, len(MSHA_COLUMNS) + 2, _msha_values, code="MSHA", encoding=MSHA_ENCODING, delimiter="|")


def _msha(ctx, db) -> dict:
    fetched = fetch(ctx, MSHA_ZIP, "MSHA", timeout=600)
    lines, malformed, dropped = cut_lines(member(fetched.body, "Mines.txt", "MSHA"), MSHA_HEADER, state_at=MSHA_COLUMNS.index("state"), code="MSHA",
                                          encoding=MSHA_ENCODING, delimiter="|")
    if len(lines) == 1:
        raise FeedError("MSHA_NO_KANSAS_ROWS")
    return keep_version(ctx, db, feed="mines", source_id=MSHA_SOURCE, key="msha", name="msha/mines-KS", ext=".txt.gz", body=core.gz(b"".join(lines)),
                        url=fetched.url, fetched=fetched, original=fetched.body, table=MSHA_TABLE, width=len(MSHA_COLUMNS) + 2, rows=_msha_rows,
                        extra={"citation": MSHA_CITATION, "dropped_lines": dropped, "license": PUBLIC_DOMAIN, "malformed_lines": malformed,
                               "rows": len(lines) - 1, "terms": MSHA_TERMS})


def mines(ctx, mrds_days: int = MRDS_RECHECK_DAYS, usmin_days: int = USMIN_RECHECK_DAYS, msha_days: int = MSHA_RECHECK_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(MINES_DDL)
        state, today = core.get_state(db, "mines"), ctx.now().date()
        summary, problems = {}, []
        for name, days, pull in (("mrds", mrds_days, _mrds), ("usmin", usmin_days, _usmin), ("msha", msha_days, _msha)):
            age = age_days(state, name, today)
            if age is not None and age < days:
                summary[name] = "not_due"
                continue
            try:
                summary[name] = pull(ctx, db)
            except FeedError as error:
                problems.append(f"{name}: {error}")
                continue
            state = save_state(ctx, db, "mines", {**state, name: str(today)})
        if problems:
            raise FeedError("MINES_SOURCES_FAILED " + "; ".join(problems))
        return summary
    finally:
        db.close()


# --- Grade crossings: FRA's crossing inventory on Socrata, Kansas rows ----------------------------

FRA_HOST = "https://data.transportation.gov/"
FRA_DATASET = "m2f8-22s6"
FRA_WHERE = "statecode='20'"
FRA_SOURCE = "fra-crossings-kansas"
FRA_TABLE = "kfm_fra_crossings"
FRA_COLUMNS = """revisiondate railroadcode railroadname reportingagencytypecode reportingagencytype reasoncode reasondescription crossingid
    crossingidsuffix reportingagencycode reportingagencyname statecode statename countycode countyname innearcode innear citycode cityname
    citydescription street blocknumber highwayname separatetrack separatetrackrailroad1 separatetrackrailroad2 separatetrackrailroad3
    separatetrackrailroad4 sametrack sametrackrailroad1 sametrackrailroad2 sametrackrailroad3 sametrackrailroad4 railroaddivision
    railroadsubdivision branchname railroadmilepostprefix railroadmilepostnumber railroadmilepostsuffix linesegment nearesttimetablestation
    timetablestation parentrailroadcode crossingownercode crossingtypecode crossingtype crossingpurposecode crossingpurpose
    crossingpositioncode crossingposition publicaccess typeoftrainserviceids typeoftrainserviceid1 typeoftrainservice1 typeoftrainserviceid2
    typeoftrainservice2 typeoftrainserviceid3 typeoftrainservice3 typeoftrainserviceid4 typeoftrainservice4 typeoftrainserviceid5
    typeoftrainservice5 typeoftrainserviceid6 typeoftrainservice6 ltpassengertrainperday numberpassengertrainperday developmenttypecode
    developmenttype adjacentcrossing adjacentcrossingnumber whistlebancode whistleban whistledate hsrcorridoridsuffix hsrcorridorid latitude
    longitude latlongsourcecode latlongsource railroadnarrativebase railroadnarrative statenarrativebase statenarrative
    emergencytelephonenumber railroadcontacttelephonenumber statecontacttelephonenumber totaldaylightthrutrains totalnighttimethrutrains
    totalswitchingtrains totaltransittrains movementsperdaycode movementsperday trainsperweek trainsperyear maximumtimetablespeed
    minimumspeedrangeovercrossing maximumspeedrangeovercrossing numberofmaintracks numberofsidingtracks numberofyardtracks
    numberoftransittracks numberofindustrytracks othertrack othertrackdescription traindetectionids traindetectionid1 traindetection1
    traindetectionid2 traindetection2 traindetectionid3 traindetection3 tracksignaled eventrecorder remotehealthmonitoring signsorsignals
    numbercrossbuckassemblies numberstopsigns numberyieldsigns advancewarnings advancewarning1 advancewarningtext1 advancewarning2
    advancewarningtext2 advancewarning3 advancewarningtext3 advancewarning4 advancewarningtext4 advancewarning5 advancewarningtext5
    advancewarning6 advancewarningtext6 advancewarning7 advancewarningtext7 countadvw10_1 countadvw10_2 countadvw10_3 countadvw10_4
    countadvw10_11 countadvw10_12 lowgroundclearancesigns numberlowgroundclearancesigns pavementmarkingids pavementmarkingid1
    pavementmarking1 pavementmarkingid2 pavementmarking2 pavementmarkingid3 pavementmarking3 pavementmarkingid4 pavementmarking4
    channeldevicemediancode channeldevicemedian exemptsigns enssigndisplayed othermutcdsigns numberothermutcdsigns1 othermutcdsignstype1
    othermutcdsignstypetext1 numberothermutcdsigns2 othermutcdsignstype2 othermutcdsignstypetext2 numberothermutcdsigns3
    othermutcdsignstype3 othermutcdsignstypetext3 privatecrossingsigns ledenhancedsigns countroadwaygatearms countpedestriangatearms
    gateconfigurationcode gateconfiguration gateconfigurationtypecode gateconfigurationtype countcantileveroverlane countcantilevernolane
    cantileveredtypestructurecode cantileveredtypestructure countmastmountedflashinglight mastmountedflashinglightcode
    mastmountedflashinglighttype mastmountedflashingbacklight mastmountedflashingsidelight countflashinglightpair
    installationdateactivewa waysidehorn installationdatewaysidehorn highwaytrafficsignal numberofbells nontrainactivewarningcode
    nontrainactivewarning countotherflashinglights otherflashinglightstype nearbyhighwaytrafficsignals hwytrafficsgnlinterconncode
    hwytrafficsgnlinterconn hwytrafficsgnlprecode hwytrafficsgnlpre highwaytrafficpresignals stoplinedistance storagedistance
    highwaymonitoringdevicescode highwaymonitoringdevices trafficlane trafficlanetypecode trafficlanetypedescription highwaypaved
    trackrundownstreet crossingilluminated crossingsurfaceinstalldate crossingsurfacewidth crossingsurfacelength crossingsurfaceids
    crossingsurfaceid1 crossingsurfacedescription1 crossingsurfaceid2 crossingsurfacedescription2 crossingsurfaceid3
    crossingsurfacedescription3 othercrossingsurface highwaynear intersectingroadwaydistance smallestcrossinganglecode
    smallestcrossingangle compower highwaysystemcode highwaysystem roadatcrossingcode roadatcrossing roadatcrossingtypecode
    roadatcrossingtype crossingonstatehighwaysystem highwayspeedlimit highwayspeedlimittypecode highwayspeedlimittype
    linearreferencingsystemrouteid linearrefsystemmilepost annualaveragedailytrafficcount annualaveragedailytrafficyear
    estimatedpercenttrucks schoolbusroute schoolbusaveragecount emergencyservicesroute ccmqzid thrrequestno reporttype crossingclosed
    reportstatus agencyid reporting_railroad_class reporting_railroad_smt_grouping reporting_parent_railroad_code
    reporting_parent_railroad_name reporting_railroad_holding_company wdcode multipleformsfiled geocoded_lat_long url
    reporting_railroad_individual_class reporting_railroad_passenger reporting_railroad_commuter reporting_railroad_switching_terminal
    reporting_railroad_tourist reporting_railroad_freight reporting_railroad_short_line""".split()
FRA_DDL = ddl(FRA_TABLE, FRA_COLUMNS + ["geometry_geojson"], {"latitude": "REAL", "longitude": "REAL"}, [("countycode",), ("crossingid",), ("railroadcode",)])
FRA_PAGE = 5000
FRA_RECHECK_DAYS = 28


def soda(host: str, dataset: str, fmt: str, **params) -> str:
    return f"{host}resource/{dataset}.{fmt}?" + "&".join(f"${k}={urllib.parse.quote(str(v), safe='')}" for k, v in params.items())


def _fra_values(fields):
    lat, lon = number(fields[FRA_COLUMNS.index("latitude")]), number(fields[FRA_COLUMNS.index("longitude")])
    values = list(fields)
    values[FRA_COLUMNS.index("latitude")], values[FRA_COLUMNS.index("longitude")] = lat, lon
    return (*values, point(lon, lat))


def _fra_rows(path: Path):
    for row in read_csv(path, FRA_COLUMNS, "FRA_CROSSINGS"):
        yield _fra_values(row)


def _fra_extract(ctx, page_size: int) -> tuple[list, str]:
    count = json.loads(fetch(ctx, soda(FRA_HOST, FRA_DATASET, "json", select="count(*)", where=FRA_WHERE), "FRA_CROSSINGS", limit=1_000_000).body)
    count = int(count[0]["count"])
    rows, first, offset = [], None, 0
    while True:
        url = soda(FRA_HOST, FRA_DATASET, "csv", where=FRA_WHERE, order=":id", limit=page_size, offset=offset)
        page = list(csv.reader(io.StringIO(fetch(ctx, url, "FRA_CROSSINGS", timeout=600).body.decode("utf-8-sig"), newline="")))
        if not page or page[0] != FRA_COLUMNS:
            raise FeedError("FRA_CROSSINGS_COLUMNS_CHANGED")
        rows.extend(page[1:])
        first = first or url
        if len(page) - 1 < page_size:
            break
        offset += page_size
        if offset > count:
            raise FeedError(f"FRA_CROSSINGS_EXTRACT_MISMATCH more than {count} rows")
    if len(rows) != count or any(len(r) != len(FRA_COLUMNS) for r in rows):
        raise FeedError(f"FRA_CROSSINGS_EXTRACT_MISMATCH {len(rows)} of {count}")
    if not rows:
        raise FeedError("FRA_CROSSINGS_NO_KANSAS_ROWS")
    if any(r[FRA_COLUMNS.index("statecode")] != "20" for r in rows):
        raise FeedError("FRA_CROSSINGS_NOT_KANSAS")
    for row in rows:
        _fra_values(row)
    return rows, first


def grade_crossings(ctx, recheck_days: int = FRA_RECHECK_DAYS, page_size: int = FRA_PAGE) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(FRA_DDL)
        state, today = core.get_state(db, "grade-crossings"), ctx.now().date()
        age = age_days(state, "fetched", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "fetched": state["fetched"], "records": state.get("records")}
        view_url = f"{FRA_HOST}api/views/{FRA_DATASET}.json"
        view = json.loads(fetch(ctx, view_url, "FRA_CROSSINGS", limit=16_000_000).body)
        name = str(view.get("name", ""))
        if "Crossing Inventory" not in name:
            raise FeedError(f"FRA_CROSSINGS_DATASET_CHANGED {name[:80]!r}")
        license_name = (view.get("license") or {}).get("name") if isinstance(view.get("license"), dict) else view.get("license")
        rows, url = _fra_extract(ctx, page_size)
        result = keep_version(ctx, db, feed="grade-crossings", source_id=FRA_SOURCE, key=KANSAS, name="fra-crossings-KS", ext=".csv.gz",
                              body=core.gz(csv_bytes([FRA_COLUMNS, *rows])), url=url, table=FRA_TABLE, width=len(FRA_COLUMNS) + 1, rows=_fra_rows,
                              extra={"citation": f"Federal Railroad Administration, {name}", "dataset": FRA_DATASET,
                                     "license": f"{license_name or 'unknown'} (dataset license)", "rows": len(rows),
                                     "rows_updated_at": view.get("rowsUpdatedAt"), "terms": view_url, "where": FRA_WHERE})
        save_state(ctx, db, "grade-crossings", {"fetched": str(today), "records": len(rows)})
        return {**result, "records": len(rows)}
    finally:
        db.close()


# --- Rail lines: the North American Rail Network, Kansas segments ---------------------------------

NARN_LAYER = ("https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0")
NARN_CITATION = ("Federal Railroad Administration and Bureau of Transportation Statistics, National Transportation Atlas Database, "
                 "North American Rail Network Lines")
NARN_LICENSE = "U.S. Government work, unrestricted public use"
NARN_SOURCE = "bts-narn-rail-lines-kansas"
NARN_TABLE = "kfm_narn_rail_lines"
NARN_WHERE = "STATEAB='KS'"
NARN_COLUMNS = """objectid fraarcid frfranode tofranode stfips cntyfips stcntyfips stateab country fradistrct rrowner1 rrowner2 rrowner3 trkrghts1
    trkrghts2 trkrghts3 trkrghts4 trkrghts5 trkrghts6 trkrghts7 trkrghts8 trkrghts9 division subdiv branch yardname passngr stracnet tracks net
    miles km timezone shape_length""".split()
NARN_PROPERTIES = {c: "Shape__Length" if c == "shape_length" else c.upper() for c in NARN_COLUMNS}
NARN_DDL = ddl(NARN_TABLE, NARN_COLUMNS + ["geometry_geojson", "min_lon", "min_lat", "max_lon", "max_lat"],
               {**{c: "" for c in NARN_COLUMNS}, "objectid": "INTEGER", "min_lon": "REAL", "min_lat": "REAL", "max_lon": "REAL", "max_lat": "REAL"},
               [("fraarcid",), ("rrowner1",), ("stcntyfips",), ("subdiv",)])
NARN_PAGE = 2000
NARN_RECHECK_DAYS = 28
RAIL_LAYERS = {"KS": NARN_WHERE}


def arcgis_query(layer: str, **params) -> str:
    return f"{layer}/query?" + urllib.parse.urlencode(params)


def _narn_rows(path: Path):
    for feature in jsonl_records(path):
        properties = feature["properties"]
        yield (*(properties[NARN_PROPERTIES[c]] for c in NARN_COLUMNS), core.canonical(feature["geometry"]), *bbox(feature["geometry"]))


def _narn_extract(ctx, where: str, page_size: int) -> tuple[list, str]:
    count = json.loads(fetch(ctx, arcgis_query(NARN_LAYER, where=where, returnCountOnly="true", f="json"), "NARN", limit=1_000_000).body)
    if not isinstance(count, dict) or not isinstance(count.get("count"), int):
        raise FeedError("NARN_RESPONSE_SHAPE count")
    count, features, first, offset = count["count"], [], None, 0
    while True:
        url = arcgis_query(NARN_LAYER, where=where, outFields="*", outSR=4326, orderByFields="OBJECTID", resultOffset=offset,
                           resultRecordCount=page_size, f="geojson")
        page = json.loads(fetch(ctx, url, "NARN", timeout=600).body)
        if not isinstance(page, dict) or not isinstance(page.get("features"), list):
            raise FeedError("NARN_RESPONSE_SHAPE page")
        for feature in page["features"]:
            properties, geometry = feature.get("properties"), feature.get("geometry")
            if not isinstance(properties, dict) or set(properties) != set(NARN_PROPERTIES.values()):
                raise FeedError("NARN_FIELDS_CHANGED")
            if not isinstance(geometry, dict) or geometry.get("type") not in ("LineString", "MultiLineString"):
                raise FeedError("NARN_GEOMETRY_SHAPE")
            if properties["STATEAB"] != KANSAS:
                raise FeedError(f"NARN_NOT_KANSAS {properties['OBJECTID']}")
            features.append({"type": "Feature", "geometry": geometry, "properties": properties})
        first = first or url
        if len(page["features"]) < page_size:
            break
        offset += page_size
        if offset > count:
            raise FeedError(f"NARN_EXTRACT_MISMATCH more than {count} features")
    if len(features) != count or len({f["properties"]["OBJECTID"] for f in features}) != count:
        raise FeedError(f"NARN_EXTRACT_MISMATCH {len(features)} of {count}")
    if not features:
        raise FeedError("NARN_NO_KANSAS_ROWS")
    features.sort(key=lambda f: f["properties"]["OBJECTID"])
    return features, first


def rail_lines(ctx, recheck_days: int = NARN_RECHECK_DAYS, page_size: int = NARN_PAGE) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NARN_DDL)
        state, today, summary = core.get_state(db, "rail-lines"), ctx.now().date(), {"rows": 0}
        for layer, where in RAIL_LAYERS.items():
            age = age_days(state, layer, today)
            if age is not None and age < recheck_days:
                summary[layer] = "not_due"
                continue
            features, url = _narn_extract(ctx, where, page_size)
            result = keep_version(ctx, db, feed="rail-lines", source_id=NARN_SOURCE, key=layer, name=f"{layer}/rail-lines-KS-{layer}", ext=".jsonl.gz",
                                  body=jsonl(features), url=url, table=NARN_TABLE, width=len(NARN_COLUMNS) + 5, rows=_narn_rows,
                                  extra={"citation": NARN_CITATION, "kansas_test": where, "layer": layer, "license": NARN_LICENSE,
                                         "rows": len(features), "terms": NARN_LAYER, "where": where})
            state = save_state(ctx, db, "rail-lines", {**state, layer: str(today)})
            summary[layer] = result["state"]
            summary["rows"] += result["rows"]
        return summary
    finally:
        db.close()
