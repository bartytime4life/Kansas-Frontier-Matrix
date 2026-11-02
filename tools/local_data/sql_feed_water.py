"""SQL feeds for Kansas water: USGS daily values, annual peaks and field measurements, and Water Quality Portal results.

Services. USGS retires WaterServices (waterservices.usgs.gov /dv, /iv, /site, /gwlevels) and the last
NWISWeb pages, the nwis.waterdata.usgs.gov peak pages among them, in NWISWeb Decommission Campaign 3,
November 2026 to February 2027. WaterServices shuts down on 2027-02-22, with intentional slowdowns and
outages from January 2027 (https://waterservices.usgs.gov, https://waterdata.usgs.gov/blog/nwisweb-decommission-summary/).
So the USGS feeds use only the Water Data OGC APIs (``OGC``). That is version 1, the one the API's own
documentation and queryables link to; v0 still answers, with older formatting. The APIs include an
annual ``peaks`` collection. No key is needed. USGS limits anonymous use per IP address per hour, but
publishes no figure and sends anonymous callers no X-RateLimit headers. A 403 or 429 stops a run with
``USGS_RATE_LIMITED``, and what the run loaded stays. Requests go one at a time, with a pause between
them, and a run makes a few hundred at most. A page holds at most 50,000 rows, and a CSV page has no
next-page link, so each request is shaped to fit one page: one time series, one year, or one
modification window. A full page is split, never loaded.

usgs-daily, ``kfm_usgs_daily_values``: every daily-value series of every Kansas site, with all
parameters and statistics. ``combined-metadata`` (time-series-metadata joined to monitoring-locations;
of the three, only it filters by state) is read weekly into ``kfm_usgs_series`` and ``kfm_usgs_sites``.
Steps in each run:
1. Load every Kansas value USGS modified since the last run, from one statewide ``last_modified``
   window that overlaps the last window by a day. A full page is cut at the sample's modification-time
   quartiles; a page full at one instant is cut by day. These windows bring new days, provisional
   edits, and approvals and corrections of any age, since each of them changes ``last_modified``.
2. Backfill the full records of up to ``max_records`` series: 1,810 series, so about 13 runs.
3. After the backfill, re-read ``ROTATION_PER_RUN`` records a run, so values USGS deleted go within a
   year.
A value is one row per (time_series_id, time), the API's own identity. Each load replaces the row
(INSERT OR REPLACE, keeping the newest load's file_id). A full record also drops that series' rows it
no longer has. Rows are upserted rather than versioned because revisions arrive a few days at a time
across many series: a version per revision would re-read up to 48,000 rows to change a handful.
Approval status and qualifiers (ESTIMATED, ICE, EQUIP, ...) are kept as given.

usgs-peaks, ``kfm_usgs_peaks``: annual peak discharge and gage height of every Kansas site, in one
statewide request (33,201 rows at 461 sites in November 2026), every 30 days. A changed answer replaces
the version loaded before (load_version).

usgs-groundwater, ``kfm_usgs_field_measurements``: discrete field measurements at Kansas sites, one
file per calendar year (load_version, key ``year/YYYY``), backfilled oldest first from 1860.
``kind`` is one of:
- ``groundwater_level``: 72019 depth below land surface; 62610 and 62611, elevations above NGVD 1929
  and NAVD 1988; 72020;
- ``discharge`` and ``gage_height``: stream measurements, cheap to keep;
- ``other``.
Each run asks which years have rows USGS modified since the last run, from one ``last_modified`` page,
and fetches those years again. Every year is also read again at least yearly, for deletions. A field
visit can hold several readings at the same time, so rows have no natural key, and whole years are
replaced instead.

water-quality, ``kfm_wqp_results`` and ``kfm_wqp_stations``: the Water Quality Portal's Kansas results
(statecode US:20), one file per year of activity start date (key ``results/YYYY``). The backfill runs
oldest first from 1901, the first year with Kansas results, at most ``max_years`` years or
``row_budget`` rows a run. After that:
- the current and previous years are fetched again weekly, since labs and states submit months late;
- the three years before those, monthly;
- older years, yearly;
- the stations, monthly.
The feed uses the legacy WQX 2.2 profile, which is quick and reports counts; the WQX 3.0 endpoint took
minutes for one month. That profile has no USGS (NWIS) results after March 2024, when USGS moved its
samples to WQX 3.0 and its own samples API. Later Kansas results come from other organizations (KDHE,
EPA Region 7, tribes). The kept raw copy is the provider's CSV, gzipped, and the zip download is
recorded by size and SHA-256. Results keep a curated column set (``WQP_RESULT_COLUMNS``): what is
needed to read a value, less some columns repeated per row or rarely filled, which stay in the raw
copy. Stations keep every column. Free text (activity, result and lab comments, station descriptions)
is kept as published, names and contact details of samplers included, under the owner's 2026-11-02
policy for this local database: public records are kept whole.

Rights: USGS data are public domain (https://www.usgs.gov/data-management/data-licensing), and
provisional values may be revised. The Water Quality Portal (USGS, EPA and NWQMC) serves its
providers' public data (https://www.waterqualitydata.us/portal_userguide/).
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timedelta, timezone
import gzip
import io
from pathlib import Path
import re
import shutil
import time
import urllib.parse
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

OGC = "https://api.waterdata.usgs.gov/ogcapi/v1/collections/"
PAGE = 50_000   # the API's largest page
KANSAS = "20"
EARLIEST = date(1800, 1, 1)
STAMP = "%Y-%m-%dT%H:%M:%S.%fZ"
MICRO = timedelta(microseconds=1)


# --- Shared: CSV pages from the USGS Water Data OGC APIs --------------------------------------------

def _url(collection: str, params: dict) -> str:
    query = urllib.parse.urlencode({"f": "csv", "limit": PAGE, **params}, safe=",/:.", quote_via=urllib.parse.quote)
    return f"{OGC}{collection}/items?{query}"


def _page(ctx, collection: str, params: dict, needed, reason: str):
    """(fetched, header, rows) of one request. The header must name every column in needed."""
    url = _url(collection, params)
    try:
        fetched = ctx.fetch(url, limit=64_000_000, timeout=600)
    except FeedError as error:
        if str(error).startswith(("HTTP_403", "HTTP_429")):
            raise FeedError(f"USGS_RATE_LIMITED {url}") from None
        raise
    finally:
        time.sleep(getattr(ctx, "pause", 1.0))
    text = fetched.body.decode("utf-8")
    if not text.strip():
        # A query with no rows is answered with an empty body, without even a header.
        return fetched, [], []
    reader = csv.reader(io.StringIO(text, newline=""))
    header = next(reader, None) or []
    missing = [c for c in needed if c not in header]
    if missing:
        raise FeedError(f"{reason} missing {','.join(missing)}; the answer began {text[:80]!r}")
    rows = [r for r in reader if r]
    if any(len(r) != len(header) for r in rows):
        raise FeedError(f"USGS_ROW_SHAPE {collection}")
    return fetched, header, rows


def _dated(ctx, collection: str, params: dict, start: date, end: date, needed, reason: str):
    """Every row with ``time`` in start..end (inclusive dates), halving a window whose answer fills a page.

    Returns (body, header, rows, fetched, requests): body is the provider's bytes when one page held all."""
    windows, pages, requests, fetched = [(start, end)], [], 0, None
    while windows:
        a, b = windows.pop(0)
        fetched, header, rows = _page(ctx, collection, {**params, "time": f"{a}/{b}"}, needed, reason)
        requests += 1
        if not rows:
            continue
        if len(rows) >= PAGE:
            if a == b:
                raise FeedError(f"USGS_PAGE_FULL {collection} {a}")
            mid = a + (b - a) // 2
            windows[:0] = [(a, mid), (mid + timedelta(days=1), b)]
            continue
        if pages and header != pages[0][1]:
            raise FeedError(f"{reason} header changed between pages")
        pages.append((fetched, header, rows))
    if not pages:
        return b"", [], [], fetched, requests
    header, rows = pages[0][1], [r for _, _, page in pages for r in page]
    return (pages[0][0].body if len(pages) == 1 else _csv(header, rows)), header, rows, pages[0][0], requests


def _csv(header, rows) -> bytes:
    out = io.StringIO()
    csv.writer(out, lineterminator="\n").writerows([header, *rows])
    return out.getvalue().encode()


def _picker(header, names):
    index = [header.index(n) for n in names]
    return lambda row: [row[i] or None for i in index]


def _known(db, digest: str):
    """The kept copy already recorded with these bytes, so a re-read that changed nothing keeps no second copy."""
    row = db.execute("SELECT source_path FROM kfm_sql_sources WHERE sha256=?", (digest,)).fetchone()
    return Path(row[0]) if row and Path(row[0]).is_file() else None


def _keep(ctx, db, feed: str, stem: str, body: bytes, fetched, **extra):
    """The kept raw copy, named by its content so a same-day rerun never collides."""
    data = core.gz(body)
    digest = core.sha256(data)
    known = _known(db, digest)
    if known is not None:
        return known, digest
    return core.store_raw(ctx, feed, f"{stem}-{digest[:12]}.csv.gz", data, url=fetched.url, fetched=fetched, extra=extra)


def _version(ctx, db, source_id: str, key: str, path, digest: str, url: str, table: str, rows, width: int) -> dict:
    with core.pipeline_lock(ctx):
        return core.load_version(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=url, table=table, rows=rows, width=width)


def _has_version(db, source_id: str, key: str) -> bool:
    return db.execute("SELECT 1 FROM kfm_sql_sources WHERE source_id=? AND state='complete' AND json_extract(receipt_json,'$.key')=?",
                      (source_id, key)).fetchone() is not None


def _save(ctx, db, feed: str, state: dict) -> dict:
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, feed, state)
    return state


def _schema(ctx, db, script: str) -> None:
    with core.pipeline_lock(ctx):
        db.executescript(script)


def _stamp(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime(STAMP)


def _moment(text: str) -> datetime:
    return datetime.strptime(text, STAMP).replace(tzinfo=timezone.utc)


def _digits(text: str) -> str:
    return re.sub(r"\D", "", text)[:14]


# --- usgs-daily: Kansas daily values, upserted from modification windows and full records ----------

DAILY_FIELDS = ("time_series_id", "monitoring_location_id", "parameter_code", "statistic_id", "time", "value", "unit_of_measure",
                "approval_status", "qualifier", "last_modified")
SERIES_FIELDS = (("id", "time_series_id"), ("monitoring_location_id", "monitoring_location_id"), ("data_type", "data_type"),
                 ("parameter_code", "parameter_code"), ("parameter_name", "parameter_name"), ("statistic_id", "statistic_id"),
                 ("unit_of_measure", "unit_of_measure"), ("computation_identifier", "computation_identifier"),
                 ("sublocation_identifier", "sublocation_identifier"), ("primary", "primary_flag"), ("web_description", "web_description"),
                 ("parameter_description", "parameter_description"), ("begin", "period_begin"), ("end", "period_end"),
                 ("last_modified", "last_modified"), ("parent_time_series_id", "parent_time_series_id"), ("thresholds", "thresholds"))
SITE_FIELDS = (("x", "longitude"), ("y", "latitude"), ("monitoring_location_id", "monitoring_location_id"), ("agency_code", "agency_code"),
               ("monitoring_location_number", "site_no"), ("monitoring_location_name", "name"), ("state_code", "state_code"),
               ("county_code", "county_code"), ("county_name", "county_name"), ("site_type_code", "site_type_code"), ("site_type", "site_type"),
               ("hydrologic_unit_code", "hydrologic_unit_code"), ("basin_code", "basin_code"), ("drainage_area", "drainage_area"),
               ("contributing_drainage_area", "contributing_drainage_area"), ("altitude", "altitude"), ("altitude_accuracy", "altitude_accuracy"),
               ("vertical_datum", "vertical_datum"), ("horizontal_positional_accuracy", "horizontal_positional_accuracy"),
               ("original_horizontal_datum", "original_horizontal_datum"), ("time_zone_abbreviation", "time_zone_abbreviation"),
               ("uses_daylight_savings", "uses_daylight_savings"), ("district_code", "district_code"), ("aquifer_code", "aquifer_code"),
               ("national_aquifer_code", "national_aquifer_code"), ("aquifer_type_code", "aquifer_type_code"),
               ("well_constructed_depth", "well_constructed_depth"), ("hole_constructed_depth", "hole_constructed_depth"),
               ("construction_date", "construction_date"))
DAILY_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_usgs_series (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL,
  {', '.join(f'{c} TEXT' for _, c in SERIES_FIELDS)}, PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usgs_series_id ON kfm_usgs_series(time_series_id);
CREATE INDEX IF NOT EXISTS kfm_usgs_series_site ON kfm_usgs_series(monitoring_location_id, parameter_code);
CREATE TABLE IF NOT EXISTS kfm_usgs_sites (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, longitude REAL, latitude REAL,
  {', '.join(f'{c} TEXT' for _, c in SITE_FIELDS[2:])}, PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usgs_sites_site ON kfm_usgs_sites(site_no);
CREATE TABLE IF NOT EXISTS kfm_usgs_daily_values (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, time_series_id TEXT NOT NULL,
  monitoring_location_id TEXT, parameter_code TEXT, statistic_id TEXT, time TEXT NOT NULL, value TEXT, unit_of_measure TEXT,
  approval_status TEXT, qualifier TEXT, last_modified TEXT, PRIMARY KEY(time_series_id, time)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usgs_daily_values_file ON kfm_usgs_daily_values(file_id);
"""
DAILY_QUERY = {"skipGeometry": "true", "properties": ",".join(DAILY_FIELDS)}
METADATA_EVERY_DAYS = 7
MODIFIED_OVERLAP = timedelta(days=1)
ROTATION_PER_RUN = 6   # 1,810 series: each record is read again about every 300 days


def _metadata(ctx, db, today: date) -> dict:
    """Kansas daily-value and peak series, and their sites, from one combined-metadata page."""
    needed = [s for s, _ in SERIES_FIELDS] + [s for s, _ in SITE_FIELDS]
    fetched, header, rows = _page(ctx, "combined-metadata", {"state_code": KANSAS, "data_type": "Daily values,Peaks"}, needed,
                                  "USGS_METADATA_COLUMNS_CHANGED")
    if len(rows) >= PAGE:
        raise FeedError("USGS_METADATA_PAGE_FULL")
    if not rows:
        raise FeedError("USGS_METADATA_EMPTY")
    path, digest = _keep(ctx, db, "usgs-daily", f"metadata/{today.year}/combined-metadata-{today:%Y%m%d}", fetched.body, fetched,
                         key="series", rows=len(rows))
    pick = _picker(header, [s for s, _ in SERIES_FIELDS])
    series = _version(ctx, db, "usgs-series", "series", path, digest, fetched.url, "kfm_usgs_series", (pick(r) for r in rows), len(SERIES_FIELDS))
    # The site table is a cut of the same answer: one row per site, in the provider's column names.
    names, sites = [s for s, _ in SITE_FIELDS], {}
    index = [header.index(n) for n in names]
    for r in rows:
        values = [r[i] for i in index]
        sites[values[2]] = max(sites.get(values[2], values), values)
    cut = core.gz(_csv(names, [sites[k] for k in sorted(sites)]))
    digest = core.sha256(cut)
    path = _known(db, digest) or core.store_raw(
        ctx, "usgs-daily", f"metadata/{today.year}/kansas-sites-{today:%Y%m%d}-{digest[:12]}.csv.gz", cut,
        url=fetched.url, fetched=fetched, original=fetched.body, extra={"key": "sites", "sites": len(sites)})[0]
    loaded = _version(ctx, db, "usgs-sites", "sites", path, digest, fetched.url, "kfm_usgs_sites",
                      ([v or None for v in sites[k]] for k in sorted(sites)), len(SITE_FIELDS))
    return {"series": series["state"], "sites": loaded["state"], "series_rows": len(rows), "site_rows": len(sites)}


def _upsert(ctx, db, source_id: str, path, digest: str, url: str, header, rows, *, series: str | None = None) -> int | None:
    """Rows of one source file over what is there. A full record (series) also drops that series' rows it lacks.
    None if this exact file is loaded; else the number of rows dropped."""
    pick = _picker(header, DAILY_FIELDS)
    values = [pick(r) for r in rows]
    if any(not v[0] or not v[4] for v in values):
        raise FeedError(f"USGS_DAILY_ROW_INCOMPLETE {path.name}")
    with core.pipeline_lock(ctx):
        file_id = core.begin_source(db, ctx, source_id, path, digest, url, core.receipt_for(ctx, path))
        if file_id is None:
            return None
        try:
            db.executemany(f"INSERT OR REPLACE INTO kfm_usgs_daily_values VALUES ({','.join('?' * 12)})",
                           ((file_id, n, *v) for n, v in enumerate(values, 1)))
            dropped = 0
            if series:
                dropped = db.execute("DELETE FROM kfm_usgs_daily_values WHERE time_series_id=? AND file_id<>?", (series, file_id)).rowcount
                db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE source_id=? AND state='complete' AND file_id<>? "
                           "AND json_extract(receipt_json,'$.key')=?", (source_id, file_id, f"record/{series}"))
            core.finish_source(db, file_id, len(values))
        except BaseException:
            db.execute("ROLLBACK")
            raise
    return dropped


def _cut(window: list, header, rows) -> list[list]:
    """Split a modification window whose answer filled a page. The page is a random sample of the window
    (the API orders rows by record UUID): cut at its modification-time quartiles; at one instant, cut by day."""
    a, b, first, last = window
    lo, hi = _moment(a), _moment(b)
    column = header.index("last_modified")
    stamps = sorted(datetime.fromisoformat(r[column]) for r in rows if r[column])
    if lo < hi:
        cuts = sorted({stamps[len(stamps) * k // 4] for k in (1, 2, 3)} if stamps else set())
        cuts = [c for c in cuts if lo < c < hi]
        if stamps and stamps[0] == stamps[-1] and lo <= stamps[0] <= hi:
            edges = [(lo, stamps[0] - MICRO), (stamps[0], stamps[0]), (stamps[0] + MICRO, hi)]
        else:
            points = [lo, *(cuts or [lo + (hi - lo) / 2]), hi]
            edges = [(points[0] if i == 0 else points[i] + MICRO, points[i + 1]) for i in range(len(points) - 1)]
        return [[_stamp(s), _stamp(e), first, last] for s, e in edges if s <= e]
    start, end = date.fromisoformat(first or str(EARLIEST)), date.fromisoformat(last or str(date.max))
    if start == end:
        raise FeedError(f"USGS_DAILY_MODIFIED_TOO_DENSE {a} {start}")
    end = min(end, max(datetime.fromisoformat(r[header.index("time")]).date() for r in rows))
    mid = start + (end - start) // 2
    return [[a, b, str(start), str(mid)], [a, b, str(mid + timedelta(days=1)), last]]


def _modified(ctx, db, state: dict, max_requests: int) -> tuple[dict, dict]:
    """Load every Kansas daily value modified since the last window, statewide."""
    now = _stamp(ctx.now())
    summary = {"modified_files": 0, "modified_rows": 0, "modified_pending": 0}
    if "modified_through" not in state:
        # First run: the records about to be backfilled hold everything until now.
        return _save(ctx, db, "usgs-daily", {**state, "modified_through": now}), summary
    pending = state.get("modified_pending") or [[_stamp(_moment(state["modified_through"]) - MODIFIED_OVERLAP), now, None, None]]
    end = state.get("modified_window_end") or now
    requests = 0
    while pending and requests < max_requests:
        window = pending[0]
        params = {**DAILY_QUERY, "state_code": KANSAS, "last_modified": f"{window[0]}/{window[1]}"}
        if window[2] or window[3]:
            params["time"] = f"{window[2] or EARLIEST}/{window[3] or '..'}"
        fetched, header, rows = _page(ctx, "daily", params, DAILY_FIELDS, "USGS_DAILY_COLUMNS_CHANGED")
        requests += 1
        if len(rows) >= PAGE:
            pending[:1] = _cut(window, header, rows)
            continue
        if rows:
            stem = f"modified/{window[0][:4]}/modified-{_digits(window[0])}-{_digits(window[1])}"
            if window[2] or window[3]:
                stem += f"-days-{_digits(window[2] or '')}-{_digits(window[3] or '')}"
            path, digest = _keep(ctx, db, "usgs-daily", stem, fetched.body, fetched, window=window, rows=len(rows))
            if _upsert(ctx, db, "usgs-daily-modified", path, digest, fetched.url, header, rows) is not None:
                summary["modified_files"] += 1
                summary["modified_rows"] += len(rows)
        pending.pop(0)
        state = _save(ctx, db, "usgs-daily", {**state, "modified_pending": pending, "modified_window_end": end})
    if pending:
        summary["modified_pending"] = len(pending)
        return _save(ctx, db, "usgs-daily", {**state, "modified_pending": pending, "modified_window_end": end}), summary
    state = {k: v for k, v in state.items() if k not in ("modified_pending", "modified_window_end")}
    return _save(ctx, db, "usgs-daily", {**state, "modified_through": end}), summary


def _record(ctx, db, series: str, today: date) -> dict:
    body, header, rows, fetched, requests = _dated(ctx, "daily", {**DAILY_QUERY, "time_series_id": series}, EARLIEST, today + timedelta(days=1),
                                                   DAILY_FIELDS, "USGS_DAILY_COLUMNS_CHANGED")
    if not rows:
        return {"state": "empty", "rows": 0}
    path, digest = _keep(ctx, db, "usgs-daily", f"records/{series[:2]}/{series}-{today:%Y%m%d}", body, fetched,
                         key=f"record/{series}", rows=len(rows), requests=requests)
    dropped = _upsert(ctx, db, "usgs-daily-record", path, digest, fetched.url, header, rows, series=series)
    return {"state": "unchanged", "rows": 0} if dropped is None else {"state": "loaded", "rows": len(rows), "dropped": dropped}


def usgs_daily(ctx, max_records: int = 150, max_modified_requests: int = 40) -> dict:
    db = core.open_db(ctx)
    try:
        _schema(ctx, db, DAILY_SCHEMA)
        state = core.get_state(db, "usgs-daily")
        today = ctx.now().date()
        summary = {"metadata": None}
        if not state.get("metadata_checked") or (today - date.fromisoformat(state["metadata_checked"])).days >= METADATA_EVERY_DAYS:
            summary["metadata"] = _metadata(ctx, db, today)
            state = _save(ctx, db, "usgs-daily", {**state, "metadata_checked": str(today)})
        state, modified = _modified(ctx, db, state, max_modified_requests)
        summary.update(modified)
        series = [r[0] for r in db.execute("SELECT DISTINCT time_series_id FROM kfm_usgs_series WHERE data_type='Daily values' ORDER BY 1")]
        have = {r[0] for r in db.execute("SELECT DISTINCT json_extract(receipt_json,'$.key') FROM kfm_sql_sources WHERE source_id='usgs-daily-record'")}
        empty = set(state.get("empty_records", []))
        backfill = [s for s in series if f"record/{s}" not in have and s not in empty]
        if backfill:
            chosen, rotation = backfill[:max_records], None
        else:
            after = state.get("rotation_after", "")
            ring = [s for s in series if s > after] + [s for s in series if s <= after]
            chosen = ring[:min(ROTATION_PER_RUN, max_records)]
            rotation = chosen[-1] if chosen else after
        counts = {"records": 0, "record_rows": 0, "records_unchanged": 0, "records_empty": 0, "rows_dropped": 0}
        for s in chosen:
            result = _record(ctx, db, s, today)
            counts["records"] += 1
            counts["record_rows"] += result["rows"]
            counts["rows_dropped"] += result.get("dropped", 0)
            counts["records_unchanged"] += result["state"] == "unchanged"
            if result["state"] == "empty":
                counts["records_empty"] += 1
                empty.add(s)
                state = _save(ctx, db, "usgs-daily", {**state, "empty_records": sorted(empty)})
        if rotation is not None:
            state = _save(ctx, db, "usgs-daily", {**state, "rotation_after": rotation})
        return {**summary, **counts, "series": len(series), "backfill_pending": max(0, len(backfill) - len(chosen)),
                "modified_through": state.get("modified_through")}
    finally:
        db.close()


# --- usgs-peaks: annual peaks of every Kansas site, one statewide version ---------------------------

PEAK_FIELDS = ("time_series_id", "monitoring_location_id", "parameter_code", "value", "unit_of_measure", "time", "water_year", "year",
               "month", "day", "time_of_day", "peak_since", "qualifier", "last_modified")
PEAKS_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_usgs_peaks (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL,
  {', '.join(f'{c} INTEGER' if c == 'water_year' else f'{c} TEXT' for c in PEAK_FIELDS)}, longitude REAL, latitude REAL,
  PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usgs_peaks_site ON kfm_usgs_peaks(monitoring_location_id, water_year);
"""
PEAKS_EVERY_DAYS = 30


def usgs_peaks(ctx, every_days: int = PEAKS_EVERY_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        _schema(ctx, db, PEAKS_SCHEMA)
        state = core.get_state(db, "usgs-peaks")
        today = ctx.now().date()
        if state.get("checked") and (today - date.fromisoformat(state["checked"])).days < every_days:
            return {"state": "not_due", "checked": state["checked"]}
        body, header, rows, fetched, requests = _dated(ctx, "peaks", {"state_code": KANSAS, "properties": ",".join(PEAK_FIELDS)}, EARLIEST, today,
                                                       ("x", "y", *PEAK_FIELDS), "USGS_PEAKS_COLUMNS_CHANGED")
        if not rows:
            raise FeedError("USGS_PEAKS_EMPTY")
        path, digest = _keep(ctx, db, "usgs-peaks", f"{today.year}/kansas-peaks-{today:%Y%m%d}", body, fetched, key="peaks/kansas",
                             rows=len(rows), requests=requests)
        pick = _picker(header, (*PEAK_FIELDS, "x", "y"))
        result = _version(ctx, db, "usgs-peaks", "peaks/kansas", path, digest, fetched.url, "kfm_usgs_peaks", (pick(r) for r in rows),
                          len(PEAK_FIELDS) + 2)
        state = _save(ctx, db, "usgs-peaks", {**state, "checked": str(today), "rows": len(rows)})
        return {**result, "rows_in_file": len(rows), "sites": len({r[header.index("monitoring_location_id")] for r in rows})}
    finally:
        db.close()


# --- usgs-groundwater: Kansas field measurements, one version per calendar year ----------------------

GW_FIELDS = ("field_measurements_series_id", "field_visit_id", "monitoring_location_id", "reading_type", "parameter_code", "observing_procedure_code",
             "observing_procedure", "value", "unit_of_measure", "time", "time_of_day", "qualifier", "vertical_datum", "approval_status",
             "measuring_agency", "control_condition", "measurement_rated", "sublocation_identifier", "last_modified")
GW_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_usgs_field_measurements (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, kind TEXT NOT NULL,
  {', '.join(f'{c} TEXT' for c in GW_FIELDS)}, longitude REAL, latitude REAL, PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usgs_field_measurements_site ON kfm_usgs_field_measurements(monitoring_location_id, time);
"""
GW_LEVEL_CODES = frozenset({"72019", "72020", "62610", "62611", "30210"})
GW_FIRST_YEAR = 1860   # the earliest Kansas measurement, 1860-08-18
GW_REREAD_DAYS = 365


def _kind(reading_type, parameter_code) -> str:
    return {"Discharge": "discharge", "MeanGageHeight": "gage_height"}.get(reading_type) or (
        "groundwater_level" if parameter_code in GW_LEVEL_CODES else "gage_height" if parameter_code == "00065" else "other")


def _gw_year(ctx, db, year: int, today: date) -> dict:
    body, header, rows, fetched, requests = _dated(ctx, "field-measurements", {"state_code": KANSAS, "properties": ",".join(GW_FIELDS)},
                                                   date(year, 1, 1), date(year, 12, 31), ("x", "y", *GW_FIELDS), "USGS_GW_COLUMNS_CHANGED")
    if not rows:
        return {"state": "empty", "rows": 0}
    key = f"year/{year}"
    path, digest = _keep(ctx, db, "usgs-groundwater", f"{year // 10 * 10}s/kansas-field-measurements-{year}-{today:%Y%m%d}", body, fetched,
                         key=key, rows=len(rows), requests=requests)
    pick = _picker(header, (*GW_FIELDS, "x", "y"))

    def values():
        for r in rows:
            v = pick(r)
            yield (_kind(v[3], v[4]), *v)
    return {**_version(ctx, db, "usgs-field-measurements", key, path, digest, fetched.url, "kfm_usgs_field_measurements", values(),
                       len(GW_FIELDS) + 3), "rows_in_file": len(rows)}


def usgs_groundwater(ctx, max_years: int = 40, row_budget: int = 400_000) -> dict:
    db = core.open_db(ctx)
    try:
        _schema(ctx, db, GW_SCHEMA)
        state = core.get_state(db, "usgs-groundwater")
        now, today = ctx.now(), ctx.now().date()
        checked, due = dict(state.get("checked", {})), set(state.get("due", []))
        next_year = int(state.get("next_year", GW_FIRST_YEAR))
        summary = {"years": [], "rows": 0, "changed_years": [], "empty_but_loaded": []}
        if "modified_through" in state:
            # Which years hold rows USGS changed since the last run: one page of their dates.
            a = _stamp(_moment(state["modified_through"]) - MODIFIED_OVERLAP)
            _, header, rows = _page(ctx, "field-measurements", {"state_code": KANSAS, "skipGeometry": "true", "properties": "time,last_modified",
                                                                 "last_modified": f"{a}/{_stamp(now)}"}, ("time",), "USGS_GW_COLUMNS_CHANGED")
            column = header.index("time") if rows else 0
            changed = set(range(GW_FIRST_YEAR, next_year)) if len(rows) >= PAGE else {int(r[column][:4]) for r in rows if r[column][:4].isdigit()}
            summary["changed_years"] = sorted(y for y in changed if y < next_year)
            due |= set(summary["changed_years"])
        state = _save(ctx, db, "usgs-groundwater", {**state, "modified_through": _stamp(now), "due": sorted(due)})
        stale = sorted((d, int(y)) for y, d in checked.items() if (today - date.fromisoformat(d)).days >= GW_REREAD_DAYS)
        plan = sorted(due) + list(range(next_year, today.year + 1))
        plan += [y for _, y in stale if y not in plan]
        for year in plan:
            if len(summary["years"]) >= max_years or summary["rows"] >= row_budget:
                break
            result = _gw_year(ctx, db, year, today)
            summary["years"].append(year)
            summary["rows"] += result.get("rows_in_file", 0)
            if result["state"] == "empty" and _has_version(db, "usgs-field-measurements", f"year/{year}"):
                # An empty answer for a loaded year is kept for a retry, not taken as a deletion.
                summary["empty_but_loaded"].append(year)
                due.add(year)
            else:
                checked[str(year)] = str(today)
                due.discard(year)
            next_year = year + 1 if year >= next_year else next_year
            state = _save(ctx, db, "usgs-groundwater", {**state, "checked": checked, "due": sorted(due), "next_year": next_year})
        return {**summary, "next_year": next_year, "due": len(due), "backfill_pending": max(0, today.year + 1 - next_year)}
    finally:
        db.close()


# --- water-quality: Water Quality Portal results, one version per year -------------------------------

WQP = "https://www.waterqualitydata.us/data/"
WQP_FIRST_YEAR = 1901   # the first year with Kansas results
WQP_LIMIT = 2_000_000_000
WQP_ROW_BUDGET = 1_500_000
WQP_RESULT_COLUMNS = (
    ("OrganizationIdentifier", "organization_identifier"), ("ActivityIdentifier", "activity_identifier"), ("ActivityTypeCode", "activity_type_code"),
    ("ActivityMediaName", "activity_media_name"), ("ActivityMediaSubdivisionName", "activity_media_subdivision_name"),
    ("ActivityStartDate", "activity_start_date"), ("ActivityStartTime/Time", "activity_start_time"),
    ("ActivityStartTime/TimeZoneCode", "activity_start_time_zone_code"), ("ActivityDepthHeightMeasure/MeasureValue", "activity_depth_height_value"),
    ("ActivityDepthHeightMeasure/MeasureUnitCode", "activity_depth_height_unit_code"), ("ProjectIdentifier", "project_identifier"),
    ("MonitoringLocationIdentifier", "monitoring_location_identifier"), ("ActivityCommentText", "activity_comment_text"),
    ("HydrologicCondition", "hydrologic_condition"),
    ("HydrologicEvent", "hydrologic_event"), ("SampleCollectionMethod/MethodIdentifier", "sample_collection_method_identifier"),
    ("SampleCollectionMethod/MethodIdentifierContext", "sample_collection_method_identifier_context"),
    ("ResultDetectionConditionText", "result_detection_condition_text"), ("CharacteristicName", "characteristic_name"),
    ("ResultSampleFractionText", "result_sample_fraction_text"), ("ResultMeasureValue", "result_measure_value"),
    ("ResultMeasure/MeasureUnitCode", "result_measure_unit_code"), ("MeasureQualifierCode", "measure_qualifier_code"),
    ("ResultStatusIdentifier", "result_status_identifier"), ("StatisticalBaseCode", "statistical_base_code"),
    ("ResultValueTypeName", "result_value_type_name"), ("ResultWeightBasisText", "result_weight_basis_text"),
    ("ResultTimeBasisText", "result_time_basis_text"), ("ResultTemperatureBasisText", "result_temperature_basis_text"),
    ("ResultParticleSizeBasisText", "result_particle_size_basis_text"), ("PrecisionValue", "precision_value"),
    ("ResultCommentText", "result_comment_text"), ("USGSPCode", "usgs_pcode"), ("ResultDepthHeightMeasure/MeasureValue", "result_depth_height_value"),
    ("ResultDepthHeightMeasure/MeasureUnitCode", "result_depth_height_unit_code"), ("SubjectTaxonomicName", "subject_taxonomic_name"),
    ("SampleTissueAnatomyName", "sample_tissue_anatomy_name"), ("ResultAnalyticalMethod/MethodIdentifier", "result_analytical_method_identifier"),
    ("ResultAnalyticalMethod/MethodIdentifierContext", "result_analytical_method_identifier_context"),
    ("ResultAnalyticalMethod/MethodName", "result_analytical_method_name"), ("LaboratoryName", "laboratory_name"),
    ("AnalysisStartDate", "analysis_start_date"), ("ResultLaboratoryCommentText", "result_laboratory_comment_text"),
    ("DetectionQuantitationLimitTypeName", "detection_quantitation_limit_type_name"),
    ("DetectionQuantitationLimitMeasure/MeasureValue", "detection_quantitation_limit_value"),
    ("DetectionQuantitationLimitMeasure/MeasureUnitCode", "detection_quantitation_limit_unit_code"), ("ProviderName", "provider_name"))
WQP_STATION_COLUMNS = (
    ("OrganizationIdentifier", "organization_identifier"), ("OrganizationFormalName", "organization_formal_name"),
    ("MonitoringLocationIdentifier", "monitoring_location_identifier"), ("MonitoringLocationName", "monitoring_location_name"),
    ("MonitoringLocationTypeName", "monitoring_location_type_name"),
    ("MonitoringLocationDescriptionText", "monitoring_location_description_text"), ("HUCEightDigitCode", "huc_eight_digit_code"),
    ("DrainageAreaMeasure/MeasureValue", "drainage_area_value"), ("DrainageAreaMeasure/MeasureUnitCode", "drainage_area_unit_code"),
    ("ContributingDrainageAreaMeasure/MeasureValue", "contributing_drainage_area_value"),
    ("ContributingDrainageAreaMeasure/MeasureUnitCode", "contributing_drainage_area_unit_code"), ("LatitudeMeasure", "latitude"),
    ("LongitudeMeasure", "longitude"), ("SourceMapScaleNumeric", "source_map_scale_numeric"),
    ("HorizontalAccuracyMeasure/MeasureValue", "horizontal_accuracy_value"), ("HorizontalAccuracyMeasure/MeasureUnitCode", "horizontal_accuracy_unit_code"),
    ("HorizontalCollectionMethodName", "horizontal_collection_method_name"),
    ("HorizontalCoordinateReferenceSystemDatumName", "horizontal_coordinate_reference_system_datum_name"),
    ("VerticalMeasure/MeasureValue", "vertical_value"), ("VerticalMeasure/MeasureUnitCode", "vertical_unit_code"),
    ("VerticalAccuracyMeasure/MeasureValue", "vertical_accuracy_value"), ("VerticalAccuracyMeasure/MeasureUnitCode", "vertical_accuracy_unit_code"),
    ("VerticalCollectionMethodName", "vertical_collection_method_name"),
    ("VerticalCoordinateReferenceSystemDatumName", "vertical_coordinate_reference_system_datum_name"), ("CountryCode", "country_code"),
    ("StateCode", "state_code"), ("CountyCode", "county_code"), ("AquiferName", "aquifer_name"), ("LocalAqfrName", "local_aqfr_name"),
    ("FormationTypeText", "formation_type_text"), ("AquiferTypeName", "aquifer_type_name"), ("ConstructionDateText", "construction_date_text"),
    ("WellDepthMeasure/MeasureValue", "well_depth_value"), ("WellDepthMeasure/MeasureUnitCode", "well_depth_unit_code"),
    ("WellHoleDepthMeasure/MeasureValue", "well_hole_depth_value"), ("WellHoleDepthMeasure/MeasureUnitCode", "well_hole_depth_unit_code"),
    ("ProviderName", "provider_name"))
WQP_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_wqp_results (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL,
  {', '.join(f'{c} TEXT' for _, c in WQP_RESULT_COLUMNS)}, PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_wqp_results_site ON kfm_wqp_results(monitoring_location_identifier, activity_start_date);
CREATE INDEX IF NOT EXISTS kfm_wqp_results_characteristic ON kfm_wqp_results(characteristic_name, activity_start_date);
CREATE TABLE IF NOT EXISTS kfm_wqp_stations (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL,
  {', '.join(f'{c} REAL' if c in ('latitude', 'longitude') else f'{c} TEXT' for _, c in WQP_STATION_COLUMNS)},
  PRIMARY KEY(file_id, row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_wqp_stations_site ON kfm_wqp_stations(monitoring_location_identifier);
"""
WQP_STATIONS_EVERY_DAYS = 30


def _wqp_due(year: int, checked: str, today: date) -> bool:
    age = today.year - year
    return (today - date.fromisoformat(checked)).days >= (7 if age <= 1 else 30 if age <= 4 else 365)


def _wqp_file(ctx, db, url: str, *, key: str, stem: str, table: str, columns, source_id: str) -> dict:
    """Download one zipped WQP answer, keep its CSV gzipped, and load it as the newest version of key."""
    zipped, kept = core.temp_path(ctx, f"wqp-{key.replace('/', '-')}.zip"), core.temp_path(ctx, f"wqp-{key.replace('/', '-')}.csv.gz")
    try:
        fetched = core.download(ctx, url, zipped, limit=WQP_LIMIT, timeout=3600)
        try:
            with zipfile.ZipFile(zipped) as archive:
                members = [m for m in archive.namelist() if m.endswith(".csv")]
                if len(members) != 1:
                    raise FeedError(f"WQP_ARCHIVE_CHANGED {key}")
                with archive.open(members[0]) as handle:
                    reader = csv.reader(io.TextIOWrapper(handle, encoding="utf-8", newline=""))
                    header = next(reader, [])
                    missing = [p for p, _ in columns if p not in header]
                    if missing:
                        raise FeedError(f"WQP_COLUMNS_CHANGED {key} missing {','.join(missing)}")
                    count = 0
                    for count, row in enumerate(reader, 1):
                        if len(row) != len(header):
                            raise FeedError(f"WQP_ROW_SHAPE {key} {count}")
                if not count:
                    return {"state": "empty", "rows_in_file": 0}
                with archive.open(members[0]) as handle, open(kept, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as out:
                    shutil.copyfileobj(handle, out, 1 << 20)
        except (zipfile.BadZipFile, EOFError, UnicodeDecodeError) as error:
            raise FeedError(f"WQP_ARCHIVE_DAMAGED {key}: {error}") from None
        digest = core.file_sha256(kept)
        path = _known(db, digest) or core.store_raw(ctx, "water-quality", f"{stem}-{digest[:12]}.csv.gz", kept, url=fetched.url,
                                                    fetched=fetched, original=zipped, extra={"key": key, "rows": count})[0]
        index = [header.index(p) for p, _ in columns]

        def rows():
            with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle)
                next(reader)
                for row in reader:
                    yield tuple(row[i] or None for i in index)
        return {**_version(ctx, db, source_id, key, path, digest, fetched.url, table, rows(), len(columns)), "rows_in_file": count}
    finally:
        zipped.unlink(missing_ok=True)
        kept.unlink(missing_ok=True)


def water_quality(ctx, max_years: int = 25, row_budget: int = WQP_ROW_BUDGET) -> dict:
    db = core.open_db(ctx)
    try:
        _schema(ctx, db, WQP_SCHEMA)
        state = core.get_state(db, "water-quality")
        today = ctx.now().date()
        summary = {"stations": None, "years": [], "rows": 0, "loaded": 0, "unchanged": 0, "empty_but_loaded": []}
        if not state.get("stations_checked") or (today - date.fromisoformat(state["stations_checked"])).days >= WQP_STATIONS_EVERY_DAYS:
            result = _wqp_file(ctx, db, WQP + "Station/search?statecode=US%3A20&mimeType=csv&zip=yes", key="stations",
                               stem=f"stations/kansas-stations-{today:%Y%m%d}", table="kfm_wqp_stations", columns=WQP_STATION_COLUMNS,
                               source_id="wqp-stations")
            if result["state"] == "empty":
                raise FeedError("WQP_STATIONS_EMPTY")
            summary["stations"] = result["state"]
            state = _save(ctx, db, "water-quality", {**state, "stations_checked": str(today)})
        checked = dict(state.get("checked", {}))
        next_year = int(state.get("next_year", WQP_FIRST_YEAR))
        # Recent years first (small, most often revised), then the backfill, oldest first.
        refresh = sorted((int(y) for y, d in checked.items() if _wqp_due(int(y), d, today)), reverse=True)
        for year in refresh + list(range(next_year, today.year + 1)):
            if len(summary["years"]) >= max_years or summary["rows"] >= row_budget:
                break
            url = (WQP + f"Result/search?statecode=US%3A20&startDateLo=01-01-{year}&startDateHi=12-31-{year}&mimeType=csv&zip=yes")
            result = _wqp_file(ctx, db, url, key=f"results/{year}", stem=f"results/{year}/kansas-results-{year}-{today:%Y%m%d}",
                               table="kfm_wqp_results", columns=WQP_RESULT_COLUMNS, source_id="wqp-results")
            summary["years"].append(year)
            summary["rows"] += result["rows_in_file"]
            summary["loaded"] += result["state"] == "loaded"
            summary["unchanged"] += result["state"] == "unchanged"
            if result["state"] == "empty" and _has_version(db, "wqp-results", f"results/{year}"):
                summary["empty_but_loaded"].append(year)   # kept and retried next run, not taken as a deletion
            else:
                checked[str(year)] = str(today)
            next_year = year + 1 if year >= next_year else next_year
            state = _save(ctx, db, "water-quality", {**state, "checked": checked, "next_year": next_year})
        return {**summary, "next_year": next_year, "backfill_pending": max(0, today.year + 1 - next_year)}
    finally:
        db.close()
