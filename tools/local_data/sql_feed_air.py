"""Air-quality SQL feed for Kansas: EPA AirData pre-generated daily files (``air-quality``).

Source: https://aqs.epa.gov/aqsweb/airdata/download_files.html. Its machine-readable list is ``file_list.csv``
(Filename, Rows, Size in KB, Created), and the formats are at https://aqs.epa.gov/aqsweb/airdata/FileFormats.html.
EPA regenerates every file twice a year: in June, with the complete prior year, and in December, with the summer
ozone season. Agencies have up to six months to report.

Loaded, from the first year listed (1980) to the current year:
- ``daily_<code>_<year>.zip`` for ozone 44201, SO2 42401, CO 42101, NO2 42602, PM2.5 FRM/FEM 88101, PM2.5 non-FRM
  88502 and PM10 81102, into ``kfm_aqs_daily``.
- ``daily_aqi_by_county_<year>.zip``, into ``kfm_aqs_daily_aqi_county``.
- The ``aqs_sites.zip`` and ``aqs_monitors.zip`` descriptions, into ``kfm_aqs_sites`` and ``kfm_aqs_monitors``.

The files are national. Each is streamed to a temporary file, read through zipfile and csv without being held
decompressed (PM2.5 2024 is 285 MB of CSV), and cut to Kansas at once (State Code 20). The cut is the kept raw copy;
the zip is recorded by size and SHA-256. Each file is loaded with ``load_version`` keyed ``daily_<kind>/<year>``, so
a regenerated file replaces its earlier version.

Schedule, per run:
- Read file_list.csv.
- Fetch the site and monitor lists when the file generation (the newest Created date) changes.
- Fetch every file never fetched (the backfill, newest year first).
- Fetch a file of the current or two previous years whenever its Created date advances.
- Fetch an older file whose Created date advanced at most once a year.
- At most ``max_files`` downloads a run. A file EPA lists with 0 rows is recorded without a download. A Kansas cut
  with no rows is recorded in feed state, not as a source, and retires any version loaded before.

Columns are the provider's names in snake_case, except ``1st Max Value`` and ``1st Max Hour``, which become
``first_max_value`` and ``first_max_hour``. Counts, coordinates, means, maxima and AQI are numeric, with an empty
field stored as NULL. Codes keep their leading zeros as TEXT.

Rights: U.S. EPA data, public domain (https://edg.epa.gov/EPA_Data_License.html). The files describe monitoring
sites and agencies, not people.
"""
from __future__ import annotations

import csv
from datetime import date, timedelta
import io
import re
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

AIRDATA = "https://aqs.epa.gov/aqsweb/airdata/"
AQS_NAME = re.compile(r"daily_(44201|42401|42101|42602|88101|88502|81102|aqi_by_county)_(\d{4})\.zip")
AQS_RECENT_YEARS = 3
AQS_RECHECK_DAYS = 365
AQS_ZIP_LIMIT = 1_000_000_000
FILE_LIST_HEADER = ["Filename", "Rows", "Size", "Created"]
DAILY_HEADER = ["State Code", "County Code", "Site Num", "Parameter Code", "POC", "Latitude", "Longitude", "Datum", "Parameter Name",
                "Sample Duration", "Pollutant Standard", "Date Local", "Units of Measure", "Event Type", "Observation Count",
                "Observation Percent", "Arithmetic Mean", "1st Max Value", "1st Max Hour", "AQI", "Method Code", "Method Name",
                "Local Site Name", "Address", "State Name", "County Name", "City Name", "CBSA Name", "Date of Last Change"]
AQI_HEADER = ["State Name", "county Name", "State Code", "County Code", "Date", "AQI", "Category", "Defining Parameter", "Defining Site",
              "Number of Sites Reporting"]
SITES_HEADER = ["State Code", "County Code", "Site Number", "Latitude", "Longitude", "Datum", "Elevation", "Land Use", "Location Setting",
                "Site Established Date", "Site Closed Date", "Met Site State Code", "Met Site County Code", "Met Site Site Number",
                "Met Site Type", "Met Site Distance", "Met Site Direction", "GMT Offset", "Owning Agency", "Local Site Name", "Address",
                "Zip Code", "State Name", "County Name", "City Name", "CBSA Name", "Tribe Name", "Extraction Date"]
MONITORS_HEADER = ["State Code", "County Code", "Site Number", "Parameter Code", "Parameter Name", "POC", "Latitude", "Longitude", "Datum",
                   "First Year of Data", "Last Sample Date", "Monitor Type", "Networks", "Reporting Agency", "PQAO", "Collecting Agency",
                   "Exclusions", "Monitoring Objective", "Last Method Code", "Last Method", "Measurement Scale",
                   "Measurement Scale Definition", "NAAQS Primary Monitor", "QA Primary Monitor", "Local Site Name", "Address",
                   "State Name", "County Name", "City Name", "CBSA Name", "Tribe Name", "Extraction Date"]
NUMERIC = {"poc": "INTEGER", "latitude": "REAL", "longitude": "REAL", "observation_count": "INTEGER", "observation_percent": "REAL",
           "arithmetic_mean": "REAL", "first_max_value": "REAL", "first_max_hour": "INTEGER", "aqi": "INTEGER", "number_of_sites_reporting": "INTEGER"}


def column(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower().replace("1st ", "first ")).strip("_")


# kind: (table, source_id, header, rowid table, lookup index)
KINDS = {"daily": ("kfm_aqs_daily", "epa-aqs-daily", DAILY_HEADER, True, "county_code, site_num, parameter_code, date_local"),
         "aqi_by_county": ("kfm_aqs_daily_aqi_county", "epa-aqs-daily-aqi-county", AQI_HEADER, False, "county_code, date"),
         "aqs_sites": ("kfm_aqs_sites", "epa-aqs-sites", SITES_HEADER, True, "county_code, site_number"),
         "aqs_monitors": ("kfm_aqs_monitors", "epa-aqs-monitors", MONITORS_HEADER, True, "county_code, site_number, parameter_code")}


def tables() -> str:
    out = []
    for table, _, header, rowid, index in KINDS.values():
        names = [column(c) for c in header]
        out.append(f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "
                   + ", ".join(f"{c} {NUMERIC.get(c, 'TEXT')}" for c in names)
                   + f", PRIMARY KEY(file_id,row_number)){'' if rowid else ' WITHOUT ROWID'};\n"
                   f"CREATE INDEX IF NOT EXISTS {table}_lookup ON {table}({index});\n")
    return "".join(out)


def _versions(db, source_id: str, key: str) -> list:
    """[(file_id, sha256)] of the loaded version of key."""
    return db.execute("SELECT file_id, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                      "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()


def file_list(ctx) -> dict:
    """{(kind, year): (rows, created)} for the wanted daily files in EPA's file_list.csv."""
    reader = csv.reader(io.StringIO(ctx.fetch(AIRDATA + "file_list.csv", limit=20_000_000).body.decode("utf-8-sig"), newline=""))
    if next(reader, None) != FILE_LIST_HEADER:
        raise FeedError("AQS_FILE_LIST_CHANGED")
    files = {}
    for row in reader:
        m = AQS_NAME.fullmatch(row[0]) if len(row) == 4 else None
        if m:
            if not (row[1].isdigit() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", row[3])):
                raise FeedError(f"AQS_FILE_LIST_CHANGED {row[0]}")
            files[(m.group(1), int(m.group(2)))] = (int(row[1]), row[3])
    if not files:
        raise FeedError("AQS_FILE_LIST_EMPTY")
    return files


def due_files(files: dict, state: dict, today: date) -> list:
    """[(kind, year)] to fetch, in order: revised recent years, the backfill (newest first), then yearly re-checks."""
    seen, recent, backfill, older = state.get("files", {}), [], [], []
    for (kind, year), (_, created) in files.items():
        entry = seen.get(f"daily_{kind}/{year}")
        if entry is None:
            backfill.append((kind, year))
        elif created > entry["created"]:
            if year > today.year - AQS_RECENT_YEARS:
                recent.append((kind, year))
            elif date.fromisoformat(entry["fetched"]) <= today - timedelta(days=AQS_RECHECK_DAYS):
                older.append((kind, year))
    order = lambda item: (-item[1], item[0])
    return sorted(recent, key=order) + sorted(backfill, key=order) + sorted(older, key=order)


def kansas_rows(path, name: str, header: list) -> tuple[list, str]:
    """The Kansas rows of the one CSV in a zip, streamed. UTF-8, or Latin-1 for a file that is not."""
    with zipfile.ZipFile(path) as archive:
        members = [m for m in archive.infolist() if not m.is_dir()]
        if len(members) != 1 or not members[0].filename.endswith(".csv"):
            raise FeedError(f"AQS_ZIP_LAYOUT {name}")
        for encoding in ("utf-8", "latin-1"):
            try:
                with archive.open(members[0]) as raw:
                    reader = csv.reader(io.TextIOWrapper(raw, encoding=encoding, newline=""))
                    if next(reader, None) != header:
                        raise FeedError(f"AQS_COLUMNS_CHANGED {name}")
                    state, keep = header.index("State Code"), []
                    for n, row in enumerate(reader, 1):
                        if len(row) > state and row[state] == "20":
                            if len(row) != len(header):
                                raise FeedError(f"AQS_ROW_SHAPE {name} {n}")
                            keep.append(row)
                    return keep, encoding
            except UnicodeDecodeError:
                continue
    raise FeedError(f"AQS_ENCODING {name}")


def _convert(header: list):
    numeric = {i for i, c in enumerate(header) if column(c) in NUMERIC}
    return lambda row: tuple(None if i in numeric and v == "" else v for i, v in enumerate(row))


def _retire(ctx, db, kind: str, key: str) -> dict:
    """No Kansas rows: no source record (empty cuts would share a digest), and a version loaded before is retired."""
    table, source_id, _, _, _ = KINDS[kind]
    with core.pipeline_lock(ctx):
        previous = _versions(db, source_id, key)
        if previous:
            db.execute("BEGIN IMMEDIATE")
            try:
                for old, _ in previous:
                    db.execute(f"DELETE FROM {table} WHERE file_id=?", (old,))
                    db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))
                db.execute("COMMIT")
            except BaseException:
                db.execute("ROLLBACK")
                raise
    return {"state": "empty", "rows": 0, "superseded": len(previous)}


def _load(ctx, db, kind: str, key: str, url: str, name: str, extra: dict) -> dict:
    """Download one zip, cut it to Kansas and load it as the new version of key."""
    table, source_id, header, _, _ = KINDS[kind]
    archive = core.temp_path(ctx, name)
    try:
        fetched = core.download(ctx, url, archive, limit=AQS_ZIP_LIMIT, timeout=1800)
        rows, encoding = kansas_rows(archive, name, header)
        previous = _versions(db, source_id, key)
        if not rows:
            return _retire(ctx, db, kind, key)
        out = io.StringIO()
        csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\n").writerows([header, *rows])
        body = core.gz(out.getvalue().encode("utf-8"))
        if core.sha256(body) in {sha for _, sha in previous}:
            return {"state": "unchanged", "rows": 0, "superseded": 0}
        path, digest = core.store_raw(ctx, "air-quality", f"{key}-kansas-{core.sha256(body)[:12]}.csv.gz", body, url=url, fetched=fetched,
                                      original=archive, extra={"key": key, "kansas_rows": len(rows), "encoding": encoding, **extra})
        with core.pipeline_lock(ctx):
            return core.load_version(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=url, table=table,
                                     rows=map(_convert(header), rows), width=len(header))
    finally:
        archive.unlink(missing_ok=True)


def _save(ctx, db, state: dict) -> dict:
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, "air-quality", state)
    return state


def air_quality(ctx, max_files: int = 60) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(tables())
        state, today = core.get_state(db, "air-quality"), ctx.now().date()
        files = file_list(ctx)
        generation = max(created for _, created in files.values())
        summary = {"files": 0, "rows": 0, "unchanged": 0, "empty": 0, "generation": generation, "lists": 0}
        budget = max_files
        if state.get("lists_generation") != generation:
            for name in ("aqs_sites", "aqs_monitors"):
                result = _load(ctx, db, name, name, AIRDATA + name + ".zip", name + ".zip", {"generation": generation})
                summary["lists"] += result["rows"]
                budget -= 1
            state = _save(ctx, db, {**state, "lists_generation": generation})
        due = due_files(files, state, today)
        summary["pending"] = 0
        for kind, year in due:
            listed_rows, created = files[(kind, year)]
            key, name, loader = f"daily_{kind}/{year}", f"daily_{kind}_{year}.zip", "aqi_by_county" if kind == "aqi_by_county" else "daily"
            if listed_rows == 0:
                # EPA lists the file as empty: nothing to download.
                result = _retire(ctx, db, loader, key)
            elif budget <= 0:
                summary["pending"] += 1
                continue
            else:
                budget -= 1
                result = _load(ctx, db, loader, key, AIRDATA + name, name, {"created": created})
                summary["files"] += result["state"] == "loaded"
                summary["rows"] += result["rows"]
            summary["unchanged"] += result["state"] == "unchanged"
            summary["empty"] += result["state"] == "empty"
            state = _save(ctx, db, {**state, "files": {**state.get("files", {}), key: {"created": created, "fetched": str(today)}}})
        return summary
    finally:
        db.close()
