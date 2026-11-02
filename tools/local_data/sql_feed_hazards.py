"""SQL feeds for Kansas hazards and health: USGS earthquakes, SPC tornadoes, NWS warnings (IEM) and CDC PLACES.

Each provider answer is cut to Kansas and kept gzipped under ``data/raw/sql-feeds/<feed>/``, named by the first
12 hex of its SHA-256 (an identical answer is the same kept file), then loaded with ``load_version`` under a
stable key: a changed version replaces the one loaded before in one transaction, an unchanged one is not
loaded again, and a provider's return to a version loaded before (A, B, then A) reinstates A from its kept
copy. Network work runs outside the pipeline lock; database writes inside it.

``earthquakes``: USGS ComCat (https://earthquake.usgs.gov/fdsnws/event/1/, CSV), every event since 1800 in the
box 36.99-40.01 N, 102.06-94.58 W (4,664 on 2026-11-02, from 1867). An epicentre inside a 2025 TIGER Kansas
county (``us_county`` in ``ctx.tiger``) gets that GEOID and ``in_kansas=1``. The few box events outside Kansas
(the Oklahoma, Nebraska and Colorado slivers, Missouri by Kansas City) are kept with ``in_kansas=0`` and no
county: they are felt in Kansas, belong to the same induced-seismicity sequences, and their location error is
often larger than their distance to the line. ComCat revises events of any age (the 1867 event was revised in
2026), merges duplicates under one id and deletes some, so a recent window would miss revisions and an upsert
by id would keep merged and deleted ids. Instead each run asks for events updated since two days before the
newest ``updated`` loaded (one small request); when any is new or revised, and at least every 30 days, the
whole box is fetched (one request, ~1 MB) and cut into years, and each year whose rows changed replaces its
loaded version (key ``year/YYYY``). A year left with no events is removed. Terms:
https://www.usgs.gov/data-management/data-licensing (public domain).

``tornadoes``: SPC Severe Weather Database (https://www.spc.noaa.gov/wcm/), the ``1950-YYYY_all_tornadoes.csv``
named on that page (the name changes when SPC adds a year). The "all" file is used, not "actual": it also has
the state segments of tornadoes that crossed a state line (ns,sn,sg = 2|3,1,2) and the rows that only continue
a county list (sg=-9), so a tornado that entered Kansas from another state (Udall, 1955) is present. Kept: rows
with st=KS (stf=20), as SPC's text. SPC's rules: state totals use sn=1; sg=1 rows summarize the whole track;
sg=-9 rows list more counties. The page is read each run; the file is fetched when its name changes or every
28 days, and a changed Kansas cut replaces the loaded one (key ``all-tornadoes``; SPC reprocesses past years in
a release). Terms: https://www.weather.gov/disclaimer.

``nws-warnings``: IEM's archive of NWS VTEC events (https://mesonet.agron.iastate.edu/json/vtec_events_bystate.py),
state KS, one request per year from 1986 (IEM refuses earlier years). Each run re-fetches the current year (and
the previous one in January), backfills up to 10 years, and once the backfill is done re-checks one older year
in rotation, so a correction IEM makes is picked up within about 40 runs. Key ``year/YYYY``. IEM lists an
event's ``locations`` ("Rush [KS], Ford [KS], ...") in no fixed order from one request to the next; the kept
copy sorts those entries, so an unchanged year is recognized as unchanged. Terms:
https://mesonet.agron.iastate.edu/disclaimer.php; the warnings are NWS products (https://www.weather.gov/disclaimer).

``cdc-places``: CDC PLACES model-based local health estimates (https://www.cdc.gov/places/), the county and
census-tract datasets on data.cdc.gov (Socrata), Kansas rows by SODA CSV with ``$limit``/``$offset``. License:
public domain (dataset metadata; https://www.cdc.gov/other/agencymaterials.html). CDC keeps the current release
at two ids created in 2020, ``swc5-untb`` (county) and ``cwsq-ngmh`` (tract), refilled each release (the 2025
release on 2025-12-04 and 12-12), and copies the previous release to new ids (2024: ``fu4u-a9bh``,
``ai6z-tcin``). The feed reads the release year from the dataset name and keys each release by id and year
(``swc5-untb/2025``): a release refilled at the same ids loads as a new key beside the old one, and a correction
within a release (``rowsUpdatedAt``) replaces its key. Checked every 28 days. To move to a release CDC
publishes under new ids instead, set ``PLACES_DATASETS`` to them; their names must still read "County Data,
YYYY release" and "Census Tract Data, YYYY release" (else ``CDC_PLACES_DATASET_CHANGED``).
"""
from __future__ import annotations

from collections import defaultdict
import csv
from datetime import date, datetime, timedelta
import gzip
import io
import json
from pathlib import Path
import re
import sqlite3
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_prism import _wkb_polygons
from tools.local_data.sql_feeds import FeedError

# --- Shared ----------------------------------------------------------------------------------------

INTEGER = re.compile(r"-?\d+")


def snake(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name).lower()


def number(value: str):
    """A provider's numeric text as int or float, '' as None."""
    if value == "":
        return None
    try:
        return int(value) if INTEGER.fullmatch(value) else float(value)
    except ValueError:
        raise FeedError(f"NOT_A_NUMBER {value[:40]!r}") from None


def ddl(table: str, columns, types: dict, indexes) -> str:
    body = ", ".join(f"{c} {types.get(c, 'TEXT')}" for c in columns)
    return (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
            f"PRIMARY KEY(file_id, row_number));\n"
            + "".join(f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(i)} ON {table}({', '.join(i)});\n" for i in indexes))


def csv_bytes(rows, encoding: str = "utf-8") -> bytes:
    out = io.StringIO()
    csv.writer(out, lineterminator="\n").writerows(rows)
    return out.getvalue().encode(encoding)


def read_csv(path: Path, header: list, code: str, encoding: str = "utf-8"):
    """The rows of a kept CSV, after its header."""
    with gzip.open(path, "rt", encoding=encoding, newline="") as handle:
        reader = csv.reader(handle)
        if next(reader, None) != header:
            raise FeedError(f"{code}_COLUMNS_CHANGED {path.name}")
        for row in reader:
            if len(row) != len(header):
                raise FeedError(f"{code}_ROW_SHAPE {path.name}")
            yield row


def save_state(ctx, db, feed: str, state: dict) -> dict:
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, feed, state)
    return state


def age_days(state: dict, field: str, today: date):
    return (today - date.fromisoformat(state[field])).days if state.get(field) else None


def _keyed(db, source_id: str, key: str, state: str = "complete") -> list[int]:
    return [fid for (fid,) in db.execute("SELECT file_id FROM kfm_sql_sources WHERE source_id=? AND state=? "
                                         "AND json_extract(receipt_json,'$.key')=?", (source_id, state, key))]


def loaded_keys(db, source_id: str) -> set:
    return {k for (k,) in db.execute("SELECT json_extract(receipt_json,'$.key') FROM kfm_sql_sources "
                                      "WHERE source_id=? AND state='complete'", (source_id,))}


def _supersede(db, table: str, file_ids) -> None:
    for old in file_ids:
        db.execute(f"DELETE FROM {table} WHERE file_id=?", (old,))
        db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))


def load_version(db, ctx, *, source_id: str, key: str, path: Path, digest: str, url: str, table: str, rows, width: int) -> dict:
    """``core.load_version``; and where the provider returns to a version loaded before (A, B, then A), which
    core refuses as SOURCE_CONTENT_SHARED, that version is reinstated from its kept copy. Lock held."""
    old = db.execute("SELECT file_id FROM kfm_sql_sources WHERE sha256=? AND source_id=? AND state='superseded' "
                     "AND json_extract(receipt_json,'$.key')=?", (digest, source_id, key)).fetchone()
    if old is None:
        return core.load_version(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=url, table=table, rows=rows, width=width)
    core.guard(ctx)
    db.execute("BEGIN IMMEDIATE")
    try:
        current = _keyed(db, source_id, key)
        _supersede(db, table, current)
        sql, batch, count = f"INSERT INTO {table} VALUES ({','.join('?' * (width + 2))})", [], 0
        for row in rows:
            if len(row) != width:
                raise FeedError(f"ROW_SHAPE {key} {count + len(batch) + 1}")
            batch.append((old[0], count + len(batch) + 1, *row))
            if len(batch) == 20000:
                db.executemany(sql, batch)
                count += len(batch)
                batch = []
        db.executemany(sql, batch)
        count += len(batch)
        db.execute("UPDATE kfm_sql_sources SET state='complete', imported_rows=? WHERE file_id=?", (count, old[0]))
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"state": "reinstated", "rows": count, "superseded": len(current)}


def keep_version(ctx, db, *, feed: str, source_id: str, key: str, name: str, ext: str, body: bytes | Path, url: str, table: str,
                 rows, width: int, fetched=None, original=None, extra: dict | None = None) -> dict:
    """Keep body (bytes, or a temp_path file, which is moved) as ``<name>-<sha12><ext>`` and load it as key's
    version. rows(path) yields the table rows from the kept copy."""
    digest = core.file_sha256(body) if isinstance(body, Path) else core.sha256(body)
    path, digest = core.store_raw(ctx, feed, f"{name}-{digest[:12]}{ext}", body, url=url, fetched=fetched, original=original,
                                  extra={"key": key, **(extra or {})})
    with core.pipeline_lock(ctx):
        return load_version(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=url, table=table, rows=rows(path), width=width)


def retire(db, source_id: str, key: str, table: str) -> int:
    """Remove the loaded version of a key the provider no longer has: its rows go, its source is superseded. Lock held."""
    db.execute("BEGIN IMMEDIATE")
    try:
        old = _keyed(db, source_id, key)
        _supersede(db, table, old)
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return len(old)


# --- Earthquakes: the ComCat Kansas box, one version per year --------------------------------------

COMCAT = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1800-01-01"
          "&minlatitude=36.99&maxlatitude=40.01&minlongitude=-102.06&maxlongitude=-94.58")
QUAKE_HEADER = ["time", "latitude", "longitude", "depth", "mag", "magType", "nst", "gap", "dmin", "rms", "net", "id", "updated",
                "place", "type", "horizontalError", "depthError", "magError", "magNst", "status", "locationSource", "magSource"]
QUAKE_NUMBERS = {"latitude", "longitude", "depth", "mag", "nst", "gap", "dmin", "rms", "horizontalError", "depthError", "magError", "magNst"}
QUAKE_COLUMNS = [snake(c) for c in QUAKE_HEADER] + ["county_geoid", "in_kansas"]
QUAKE_TABLE = "kfm_usgs_earthquakes"
QUAKE_DDL = ddl(QUAKE_TABLE, QUAKE_COLUMNS, {**{snake(c): "REAL" for c in QUAKE_NUMBERS}, "nst": "INTEGER", "mag_nst": "INTEGER",
                                             "time": "TEXT NOT NULL", "id": "TEXT NOT NULL", "in_kansas": "INTEGER NOT NULL"},
                [("id",), ("county_geoid", "time"), ("time",)])
QUAKE_SOURCE = "usgs-comcat-kansas-box"
QUAKE_FULL_DAYS = 30
QUAKE_OVERLAP = timedelta(days=2)
QUAKE_LIMIT = 20000   # ComCat answers at most 20,000 events per query


def kansas_counties(tiger) -> list:
    """[(geoid, west, south, east, north, rings)] of the Kansas counties in the TIGER GeoPackage."""
    db = sqlite3.connect(f"file:{tiger}?mode=ro", uri=True)
    try:
        found = db.execute("SELECT GEOID, geom FROM us_county WHERE GEOID LIKE '20%' ORDER BY GEOID").fetchall()
    finally:
        db.close()
    counties = []
    for geoid, blob in found:
        rings = [ring for polygon in _wkb_polygons(bytes(blob)) for ring in polygon]
        xs, ys = [x for ring in rings for x, _ in ring], [y for ring in rings for _, y in ring]
        counties.append((geoid, min(xs), min(ys), max(xs), max(ys), rings))
    if not counties:
        raise FeedError("TIGER_KANSAS_COUNTIES_MISSING")
    return counties


def county_at(counties, lon: float, lat: float):
    """The GEOID of the county holding the point (even-odd over every ring, so holes count), else None."""
    for geoid, west, south, east, north, rings in counties:
        if west <= lon <= east and south <= lat <= north:
            inside = False
            for ring in rings:
                for (ax, ay), (bx, by) in zip(ring, ring[1:]):
                    if (ay > lat) != (by > lat) and lon < ax + (lat - ay) * (bx - ax) / (by - ay):
                        inside = not inside
            if inside:
                return geoid
    return None


def _quake_values(row, counties=None):
    values = [number(v) if c in QUAKE_NUMBERS else v for c, v in zip(QUAKE_HEADER, row)]
    if counties is None:
        return values
    geoid = county_at(counties, values[2], values[1]) if values[1] is not None and values[2] is not None else None
    return (*values, geoid, int(geoid is not None))


def _comcat(ctx, url: str):
    fetched = ctx.fetch(url, limit=64_000_000, timeout=600)
    rows = list(csv.reader(io.StringIO(fetched.body.decode("utf-8"), newline="")))
    if not rows or rows[0] != QUAKE_HEADER:
        raise FeedError("COMCAT_COLUMNS_CHANGED")
    if any(len(r) != len(QUAKE_HEADER) for r in rows[1:]):
        raise FeedError("COMCAT_ROW_SHAPE")
    if len(rows) - 1 >= QUAKE_LIMIT:
        raise FeedError("COMCAT_SEARCH_LIMIT")
    return fetched, rows[1:]


def earthquakes(ctx) -> dict:
    if not ctx.tiger:
        raise FeedError("TIGER_GEOPACKAGE_REQUIRED")
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(QUAKE_DDL)
        state, today = core.get_state(db, "earthquakes"), ctx.now().date()
        summary = {"changed_events": None, "years_loaded": 0, "years_unchanged": 0, "years_removed": 0, "rows": 0}
        age = age_days(state, "full_checked", today)
        if age is not None and age < QUAKE_FULL_DAYS:
            since = datetime.fromisoformat(state["updated_through"].replace("Z", "+00:00")) - QUAKE_OVERLAP
            _, probe = _comcat(ctx, f"{COMCAT}&updatedafter={since:%Y-%m-%dT%H:%M:%S}")
            summary["changed_events"] = sum(1 for r in probe if not db.execute(
                f"SELECT 1 FROM {QUAKE_TABLE} WHERE id=? AND updated=?", (r[11], r[12])).fetchone())
            if not summary["changed_events"]:
                return {**summary, "full_checked": state["full_checked"], "updated_through": state["updated_through"]}
        fetched, rows = _comcat(ctx, COMCAT)
        if not rows:
            raise FeedError("COMCAT_BOX_EMPTY")
        counties, years = kansas_counties(ctx.tiger), defaultdict(list)
        for row in rows:
            _quake_values(row)
            years[row[0][:4]].append(row)
        for year, events in sorted(years.items()):
            events.sort(key=lambda r: (r[0], r[11]))
            result = keep_version(ctx, db, feed="earthquakes", source_id=QUAKE_SOURCE, key=f"year/{year}", name=f"{year}/comcat-kansas-box-{year}",
                                  ext=".csv.gz", body=core.gz(csv_bytes([QUAKE_HEADER, *events])), url=fetched.url, fetched=fetched,
                                  original=fetched.body, extra={"events": len(events)}, table=QUAKE_TABLE, width=len(QUAKE_COLUMNS),
                                  rows=lambda path: (_quake_values(r, counties) for r in read_csv(path, QUAKE_HEADER, "COMCAT")))
            summary["years_unchanged" if result["state"] == "unchanged" else "years_loaded"] += 1
            summary["rows"] += result["rows"]
        with core.pipeline_lock(ctx):
            for key in sorted(loaded_keys(db, QUAKE_SOURCE) - {f"year/{y}" for y in years}):
                summary["years_removed"] += retire(db, QUAKE_SOURCE, key, QUAKE_TABLE)
            state = {**state, "full_checked": str(today), "updated_through": max(r[12] for r in rows), "events": len(rows)}
            core.set_state(db, ctx, "earthquakes", state)
        return {**summary, "events": len(rows), "updated_through": state["updated_through"]}
    finally:
        db.close()


# --- Tornadoes: SPC's national file, cut to Kansas rows --------------------------------------------

SPC = "https://www.spc.noaa.gov/wcm/"
SPC_FILE = re.compile(r'href="(data/((\d{4})-(\d{4})_all_tornadoes)\.csv)"')
TORNADO_HEADER = ["om", "yr", "mo", "dy", "date", "time", "tz", "st", "stf", "stn", "mag", "inj", "fat", "loss", "closs", "slat", "slon",
                  "elat", "elon", "len", "wid", "ns", "sn", "sg", "f1", "f2", "f3", "f4", "fc", "edat", "etime"]
TORNADO_TABLE = "kfm_spc_tornadoes"
TORNADO_DDL = ddl(TORNADO_TABLE, TORNADO_HEADER, {}, [("date",), ("yr", "om")])
TORNADO_RECHECK_DAYS = 28


def tornadoes(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(TORNADO_DDL)
        state, today = core.get_state(db, "tornadoes"), ctx.now().date()
        files = sorted({(int(m.group(4)), int(m.group(3)), m.group(1), m.group(2))
                        for m in SPC_FILE.finditer(ctx.fetch(SPC, limit=8_000_000).body.decode("latin-1"))})
        if not files:
            raise FeedError("SPC_TORNADO_FILE_NOT_LISTED")
        *_, link, stem = files[-1]
        age = age_days(state, "checked", today)
        if link == state.get("file") and age is not None and age < TORNADO_RECHECK_DAYS:
            return {"file": link, "state": "not_due", "checked": state["checked"]}
        fetched = ctx.fetch(SPC + link, limit=256_000_000, timeout=900)
        rows = list(csv.reader(io.StringIO(fetched.body.decode("latin-1"), newline="")))
        if not rows or rows[0] != TORNADO_HEADER:
            raise FeedError(f"SPC_TORNADO_COLUMNS_CHANGED {link}")
        keep = [r for r in rows[1:] if r[7:8] == ["KS"] or r[8:9] == ["20"]]
        if any(len(r) != len(TORNADO_HEADER) for r in keep):
            raise FeedError(f"SPC_TORNADO_ROW_SHAPE {link}")
        if not keep:
            raise FeedError(f"SPC_TORNADO_NO_KANSAS_ROWS {link}")
        result = keep_version(ctx, db, feed="tornadoes", source_id="spc-tornadoes", key="all-tornadoes", name=f"{stem}/kansas-{stem}",
                              ext=".csv.gz", body=core.gz(csv_bytes([TORNADO_HEADER, *keep], "latin-1")), url=fetched.url, fetched=fetched,
                              original=fetched.body, extra={"kansas_rows": len(keep)}, table=TORNADO_TABLE, width=len(TORNADO_HEADER),
                              rows=lambda path: read_csv(path, TORNADO_HEADER, "SPC_TORNADO", "latin-1"))
        save_state(ctx, db, "tornadoes", {"file": link, "checked": str(today), "kansas_rows": len(keep)})
        return {"file": link, **result}
    finally:
        db.close()


# --- NWS warnings: IEM's VTEC events for Kansas, one version per year ------------------------------

VTEC = "https://mesonet.agron.iastate.edu/json/vtec_events_bystate.py?state=KS&year={year}"
VTEC_FIRST = 1986
VTEC_FIELDS = ["wfo", "phenomena", "significance", "eventid", "ph_name", "sig_name", "hvtec_nwsli", "area", "locations", "issue",
               "product_issue", "expire", "init_expire", "uri"]
VTEC_TABLE = "kfm_iem_vtec_events"
VTEC_DDL = ddl(VTEC_TABLE, ["year", *VTEC_FIELDS], {"year": "INTEGER NOT NULL", "eventid": "INTEGER", "area": "REAL"},
               [("phenomena", "significance", "issue"), ("year", "wfo", "phenomena", "significance", "eventid")])
VTEC_SOURCE = "iem-vtec-events"
VTEC_BACKFILL = 10
VTEC_LOCATION = re.compile(r"(?<=\]), ")   # between "Name [ST]" entries


def _vtec_rows(path: Path, year: int):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            event = json.loads(line)
            yield (year, *(event[f] for f in VTEC_FIELDS))


def _vtec_year(ctx, db, year: int) -> dict:
    fetched = ctx.fetch(VTEC.format(year=year), limit=128_000_000, timeout=600)
    try:
        payload = json.loads(fetched.body)
    except ValueError:
        raise FeedError(f"IEM_VTEC_RESPONSE_SHAPE {year}") from None
    events = payload.get("events") if isinstance(payload, dict) else None
    if not isinstance(events, list) or payload.get("state") != "KS" or str(payload.get("year")) != str(year):
        raise FeedError(f"IEM_VTEC_RESPONSE_SHAPE {year}")
    if any(not isinstance(e, dict) or sorted(e) != sorted(VTEC_FIELDS) for e in events):
        raise FeedError(f"IEM_VTEC_FIELDS_CHANGED {year}")
    if not events:
        if f"year/{year}" in loaded_keys(db, VTEC_SOURCE):
            raise FeedError(f"IEM_VTEC_YEAR_EMPTIED {year}")
        return {"state": "empty", "rows": 0}
    for event in events:
        if isinstance(event["locations"], str):
            event["locations"] = ", ".join(sorted(VTEC_LOCATION.split(event["locations"])))
    events.sort(key=lambda e: (e["wfo"] or "", e["phenomena"] or "", e["significance"] or "", e["eventid"] or 0, core.canonical(e)))
    return keep_version(ctx, db, feed="nws-warnings", source_id=VTEC_SOURCE, key=f"year/{year}", name=f"{year}/vtec-events-KS-{year}",
                        ext=".jsonl.gz", body=core.gz("".join(core.canonical(e) + "\n" for e in events).encode()), url=fetched.url,
                        fetched=fetched, original=fetched.body, extra={"events": len(events)}, table=VTEC_TABLE,
                        width=len(VTEC_FIELDS) + 1, rows=lambda path: _vtec_rows(path, year))


def nws_warnings(ctx, max_backfill: int = VTEC_BACKFILL) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(VTEC_DDL)
        state, today = core.get_state(db, "nws-warnings"), ctx.now().date()
        current = [today.year] + ([today.year - 1] if today.month == 1 else [])
        start = int(state.get("backfill_next", VTEC_FIRST))
        pending = [y for y in range(start, today.year) if y not in current]
        backfill, revisit = pending[:max_backfill], None
        if not pending and min(current) - 1 >= VTEC_FIRST:
            revisit = int(state.get("revisit_next", VTEC_FIRST))
            revisit = revisit if VTEC_FIRST <= revisit < min(current) else VTEC_FIRST
        summary = {"loaded": [], "unchanged": [], "empty": [], "rows": 0}
        for year in [*current, *backfill, *([revisit] if revisit else [])]:
            result = _vtec_year(ctx, db, year)
            summary[result["state"] if result["state"] in ("unchanged", "empty") else "loaded"].append(year)
            summary["rows"] += result["rows"]
            if year in backfill:
                state = save_state(ctx, db, "nws-warnings", {**state, "backfill_next": year + 1})
        if revisit:
            state = save_state(ctx, db, "nws-warnings", {**state, "revisit_next": revisit + 1})
        return {**summary, "backfill_next": state.get("backfill_next", start), "revisited": revisit}
    finally:
        db.close()


# --- CDC PLACES: county and census-tract estimates, one version per release ------------------------

PLACES_DATASETS = {"county": "swc5-untb", "tract": "cwsq-ngmh"}   # the 2025 release on 2026-11-02
PLACES_NAMES = {"county": "County Data", "tract": "Census Tract Data"}
PLACES_COLUMNS = {
    "county": ["year", "stateabbr", "statedesc", "locationname", "datasource", "category", "measure", "data_value_unit", "data_value_type",
               "data_value", "data_value_footnote_symbol", "data_value_footnote", "low_confidence_limit", "high_confidence_limit",
               "totalpopulation", "totalpop18plus", "locationid", "categoryid", "measureid", "datavaluetypeid", "short_question_text",
               "geolocation"],
    "tract": ["year", "stateabbr", "statedesc", "countyname", "countyfips", "locationname", "datasource", "category", "measure",
              "data_value_unit", "data_value_type", "data_value", "data_value_footnote_symbol", "data_value_footnote", "low_confidence_limit",
              "high_confidence_limit", "totalpopulation", "totalpop18plus", "geolocation", "locationid", "categoryid", "measureid",
              "datavaluetypeid", "short_question_text"],
}
PLACES_NUMBERS = {"data_value": "REAL", "low_confidence_limit": "REAL", "high_confidence_limit": "REAL", "totalpopulation": "INTEGER",
                  "totalpop18plus": "INTEGER"}
PLACES_TABLES = {"county": "kfm_cdc_places_county", "tract": "kfm_cdc_places_tract"}
PLACES_DDL = (ddl(PLACES_TABLES["county"], ["release", *PLACES_COLUMNS["county"]], PLACES_NUMBERS, [("locationid", "measureid"), ("measureid",)])
              + ddl(PLACES_TABLES["tract"], ["release", *PLACES_COLUMNS["tract"]], PLACES_NUMBERS,
                    [("countyfips", "measureid"), ("locationid", "measureid")]))
PLACES_VIEW = "https://data.cdc.gov/api/views/{dataset}.json"
PLACES_PAGE = 20000
PLACES_RECHECK_DAYS = 28


def _soda(dataset: str, fmt: str, **params) -> str:
    return f"https://data.cdc.gov/resource/{dataset}.{fmt}?" + "&".join(f"${k}={urllib.parse.quote(str(v), safe='')}" for k, v in params.items())


def _places_rows(path: Path, level: str, release: str):
    columns = PLACES_COLUMNS[level]
    for row in read_csv(path, columns, "CDC_PLACES"):
        yield (release, *(number(v) if c in PLACES_NUMBERS else v for c, v in zip(columns, row)))


def _places_extract(ctx, dataset: str, columns: list) -> tuple[list, str]:
    count = json.loads(ctx.fetch(_soda(dataset, "json", select="count(*)", where="stateabbr='KS'"), limit=1_000_000).body)
    count = int(count[0]["count"])
    rows, first, offset = [], None, 0
    while True:
        url = _soda(dataset, "csv", where="stateabbr='KS'", order=":id", limit=PLACES_PAGE, offset=offset)
        page = list(csv.reader(io.StringIO(ctx.fetch(url, limit=256_000_000, timeout=600).body.decode("utf-8"), newline="")))
        if not page or page[0] != columns:
            raise FeedError(f"CDC_PLACES_COLUMNS_CHANGED {dataset}")
        rows.extend(page[1:])
        first = first or url
        if len(page) - 1 < PLACES_PAGE:
            break
        offset += PLACES_PAGE
        if offset > count:
            raise FeedError(f"CDC_PLACES_EXTRACT_MISMATCH {dataset} more than {count} rows")
    if len(rows) != count or any(len(r) != len(columns) or r[1] != "KS" for r in rows):
        raise FeedError(f"CDC_PLACES_EXTRACT_MISMATCH {dataset} {len(rows)} of {count}")
    if not rows:
        raise FeedError(f"CDC_PLACES_NO_KANSAS_ROWS {dataset}")
    for row in rows:
        for c, v in zip(columns, row):
            if c in PLACES_NUMBERS:
                number(v)
    return rows, first


def cdc_places(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(PLACES_DDL)
        state, today = core.get_state(db, "cdc-places"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < PLACES_RECHECK_DAYS:
            return {"state": "not_due", "checked": state["checked"]}
        summary, seen = {"rows": 0}, dict(state.get("datasets", {}))
        for level, dataset in PLACES_DATASETS.items():
            view = json.loads(ctx.fetch(PLACES_VIEW.format(dataset=dataset), limit=16_000_000).body)
            name = str(view.get("name", ""))
            found = re.search(r"\b(\d{4}) release\b", name)
            if PLACES_NAMES[level] not in name or not found:
                raise FeedError(f"CDC_PLACES_DATASET_CHANGED {dataset} {name[:80]!r}")
            release, mark = found.group(1), {"release": found.group(1), "rows_updated_at": view.get("rowsUpdatedAt")}
            if seen.get(dataset) == mark:
                summary[level] = f"unchanged {release}"
                continue
            columns = PLACES_COLUMNS[level]
            rows, url = _places_extract(ctx, dataset, columns)
            result = keep_version(ctx, db, feed="cdc-places", source_id=f"cdc-places-{level}", key=f"{dataset}/{release}",
                                  name=f"{level}/{release}/places-{level}-{dataset}-KS", ext=".csv.gz", body=core.gz(csv_bytes([columns, *rows])),
                                  url=url, extra={"dataset_name": name, "release": release, "rows_updated_at": mark["rows_updated_at"],
                                                  "kansas_rows": len(rows)},
                                  table=PLACES_TABLES[level], width=len(columns) + 1, rows=lambda path: _places_rows(path, level, release))
            seen[dataset] = mark
            state = save_state(ctx, db, "cdc-places", {**state, "datasets": seen})
            summary[level] = f"{result['state']} {release}"
            summary["rows"] += result["rows"]
        save_state(ctx, db, "cdc-places", {**state, "checked": str(today)})
        return summary
    finally:
        db.close()
