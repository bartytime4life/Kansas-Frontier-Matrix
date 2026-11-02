"""Climate SQL feeds for Kansas: NOAA nClimDiv monthly series (``climdiv``) and U.S. Drought Monitor statistics (``drought``).

climdiv: NCEI nClimDiv, https://www.ncei.noaa.gov/pub/data/cirs/climdiv/ (it redirects to
monitoring-content/data/us/climdiv/monthly/current/; formats in county-, divisional-, state- and normals-readme.txt
there). Each monthly release (about the 6th to 8th) publishes every file again as
``climdiv-<element><cy|dv|st>-v1.0.0-YYYYMMDD``, revising at least the latest two years, and the whole record on a
version change. Each run reads the listing and fetches only files dated after the release handled for that file. Each
file is cut to Kansas and loaded with ``load_version`` keyed by its code (``pcpncy``, ``norm-tmpcst``), so a release
replaces the previous one. The ``norm-`` files are NCEI's period averages (1901-1930 ... 1991-2020, 1901-2000, 1895-2020).
NCEI numbers states alphabetically, so Kansas is 14 in the county and division files and 014 in the state files.
- Counties carry the county FIPS, stored as the GEOID (``14001`` is ``20001``).
- Divisions keep NCEI's id, 1401-1409; county-to-climdivs.txt is loaded beside them.
- The statewide series is area ``20``.
Rows are long form: one per area, element, year (normals: period) and month. Units are deg F, inches, deg F days, or
the index. A missing month (-9.99 precipitation, -99.90/-99.99 temperature, -9999. degree days, -99.99 Palmer and SPI)
is NULL, with the token kept in ``missing_token``. Regional series and station inventories are not loaded.

drought: U.S. Drought Monitor statistics service, https://usdmdataservices.unl.edu/api/ (documented at
https://droughtmonitor.unl.edu/DmData/DataDownload/WebServiceInfo.aspx). Weekly maps since 2000-01-04 are dated
Tuesday and released Thursday. Each year is eight requests, each loaded with ``load_version`` keyed like
``county/area_percent/1/2025``: county (aoi=KS) and state (aoi=20) percent of area and percent of population, as
statisticsType 1 ("traditional", cumulative: D1 includes D2-D4) and 2 (categorical). The service also returns the
previous year's last map (its validity week reaches into January), so only rows whose MapDate is in the year are
loaded. Absolute area and population, and DSCI, follow from these; climate-division statistics cost a request per
division. None of the three is loaded.
- A year is fetched again from the Thursday after its newest map until its last Tuesday's map is in.
- One complete year per run is checked again once a year, in case the service revises it.
- Backfill: at most ``max_years`` years a run, newest first.

Rights: NOAA NCEI data are U.S. government works, distributed without warranty
(https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00005). The U.S. Drought Monitor is
produced by the National Drought Mitigation Center with USDA and NOAA and asks for credit
(https://droughtmonitor.unl.edu/About/Permission.aspx). Neither names private individuals.
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
import gzip
import io
import re

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError


def _versions(db, source_id: str, key: str) -> set:
    """SHA-256 of the loaded version of key: an identical download is skipped before a raw copy is kept."""
    return {sha for (sha,) in db.execute("SELECT sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                                         "AND json_extract(receipt_json,'$.key')=?", (source_id, key))}


def _save(ctx, db, feed: str, state: dict) -> dict:
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, feed, state)
    return state


# --- nClimDiv: monthly county, division and state series, replaced by each new release ------------------------

CLIMDIV = "https://www.ncei.noaa.gov/monitoring-content/data/us/climdiv/monthly/current/"
CLIMDIV_NAME = re.compile(r"climdiv-(norm-)?([a-z]{4}|sp\d\d)(cy|dv|st)-v(\d+\.\d+\.\d+)-(\d{8})")
ELEMENTS = {"pcpn": "01", "tmpc": "02", "pdsi": "05", "phdi": "06", "zndx": "07", "pmdi": "08", "hddc": "25", "cddc": "26",
            "tmax": "27", "tmin": "28", "sp01": "71", "sp02": "72", "sp03": "73", "sp06": "74", "sp09": "75", "sp12": "76", "sp24": "77"}
NORMAL_ELEMENTS = ("pcpn", "tmpc", "tmax", "tmin", "hddc", "cddc")
MISSING = {"pcpn": {"-9.99"}, "tmpc": {"-99.90", "-99.99"}, "tmax": {"-99.90", "-99.99"}, "tmin": {"-99.90", "-99.99"},
           "hddc": {"-9999."}, "cddc": {"-9999."}}
PERIODS = {"0001": "1901-1930", "0002": "1911-1940", "0003": "1921-1950", "0004": "1931-1960", "0005": "1941-1970",
           "0006": "1951-1980", "0007": "1961-1990", "0008": "1971-2000", "0009": "1981-2010", "0010": "1991-2020",
           "0031": "1901-2000", "0032": "1895-2020"}
# Ends of the state, area, element and year fields; twelve 7-column values follow.
LAYOUT = {"cy": (2, 5, 7, 11), "dv": (2, 4, 6, 10), "st": (3, 4, 6, 10)}
KANSAS_PREFIX = {"cy": b"14", "dv": b"14", "st": b"014"}
AREA_TYPES = {"cy": "county", "dv": "division", "st": "state"}
TOKEN = re.compile(r"-?\d+\.\d*")
CLIMDIV_TABLES = """
CREATE TABLE IF NOT EXISTS kfm_climdiv_monthly (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, area_type TEXT NOT NULL, area_code TEXT NOT NULL, element TEXT NOT NULL,
  year INTEGER NOT NULL, month INTEGER NOT NULL, value REAL, missing_token TEXT, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_climdiv_monthly_series ON kfm_climdiv_monthly(area_code, element, year, month);
CREATE TABLE IF NOT EXISTS kfm_climdiv_normals (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, area_type TEXT NOT NULL, area_code TEXT NOT NULL, element TEXT NOT NULL,
  period_code TEXT NOT NULL, period TEXT, month INTEGER NOT NULL, value REAL, missing_token TEXT,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_climdiv_normals_series ON kfm_climdiv_normals(area_code, element, period_code, month);
CREATE TABLE IF NOT EXISTS kfm_climdiv_county_divisions (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, postal_fips_id TEXT NOT NULL, ncdc_fips_id TEXT NOT NULL,
  climdiv_id TEXT NOT NULL, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_climdiv_county_divisions_county ON kfm_climdiv_county_divisions(postal_fips_id);
"""


def climdiv_rows(lines, code: str, name: str):
    """Long-form rows from a file's Kansas lines: (area_type, area_code, element, year, month, value, missing_token),
    or for a normals file (area_type, area_code, element, period_code, period, month, value, missing_token)."""
    normals, element, area = code.startswith("norm-"), code[-6:-2], code[-2:]
    s, a, e, y = LAYOUT[area]
    missing = MISSING.get(element, {"-99.99"})
    for n, line in enumerate(lines, 1):
        text = line.rstrip()
        if len(text) != y + 84 or not text[:y].isdigit() or text[a:e] != ELEMENTS[element] or (area == "st" and text[s:a] != "0"):
            raise FeedError(f"CLIMDIV_FORMAT_CHANGED {name} {n}")
        area_code = {"cy": "20" + text[s:a], "dv": text[:a], "st": "20"}[area]
        for month in range(12):
            token = text[y + 7 * month:y + 7 * month + 7].strip()
            if token in missing:
                value, raw = None, token
            elif TOKEN.fullmatch(token):
                value, raw = float(token), None
            else:
                raise FeedError(f"CLIMDIV_FORMAT_CHANGED {name} {n}")
            yield ((AREA_TYPES[area], area_code, element, text[e:y], PERIODS.get(text[e:y]), month + 1, value, raw) if normals
                   else (AREA_TYPES[area], area_code, element, int(text[e:y]), month + 1, value, raw))


def _climdiv_listing(ctx) -> tuple[dict, list]:
    listing = ctx.fetch(CLIMDIV, limit=4_000_000).body.decode("latin-1")
    newest, skipped = {}, set()
    for href in set(re.findall(r'href="([^"/]+)"', listing)):
        m = CLIMDIV_NAME.fullmatch(href)
        if not m:
            continue
        norm, element, area, version, released = m.groups()
        code = (norm or "") + element + area
        if element not in (NORMAL_ELEMENTS if norm else ELEMENTS):
            skipped.add(code)
            continue
        newest[code] = max(newest.get(code, ("", "")), (released, version))
    if not newest:
        raise FeedError("CLIMDIV_LISTING_EMPTY")
    return newest, sorted(skipped)


def _climdiv_county_map(ctx, db, release: str) -> int:
    fetched = ctx.fetch(CLIMDIV + "county-to-climdivs.txt", limit=4_000_000)
    header = "POSTAL_FIPS_ID NCDC_FIPS_ID CLIMDIV_ID"
    parts = [line.split() for line in fetched.body.decode("latin-1").splitlines()]
    rows = [tuple(p) for p in parts if len(p) == 3 and p[0][:2] == "20" and p[1][:2] == "14"]
    if [header] != [" ".join(p) for p in parts if p[:1] == ["POSTAL_FIPS_ID"]] or not rows or \
            any(not (len(p[0]) == len(p[1]) == 5 and len(p[2]) == 4 and "".join(p).isdigit()) for p in rows):
        raise FeedError("CLIMDIV_COUNTY_MAP_CHANGED")
    body = core.gz((header + "\n" + "".join(" ".join(r) + "\n" for r in rows)).encode())
    if core.sha256(body) in _versions(db, "noaa-climdiv-county-map", "county-to-climdivs"):
        return 0
    path, digest = core.store_raw(ctx, "climdiv", f"{release}/county-to-climdivs-kansas-{core.sha256(body)[:12]}.txt.gz", body,
                                  url=fetched.url, fetched=fetched, original=fetched.body,
                                  extra={"key": "county-to-climdivs", "kansas_rows": len(rows)})
    with core.pipeline_lock(ctx):
        return core.load_version(db, ctx, source_id="noaa-climdiv-county-map", key="county-to-climdivs", path=path, digest=digest,
                                 url=fetched.url, table="kfm_climdiv_county_divisions", rows=rows, width=3)["rows"]


def climdiv(ctx, max_files: int = 80) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(CLIMDIV_TABLES)
        state = core.get_state(db, "climdiv")
        newest, skipped = _climdiv_listing(ctx)
        due = sorted(code for code, (released, _) in newest.items() if released > state.get("releases", {}).get(code, ""))
        release = max(r for r, _ in newest.values())
        summary = {"files": 0, "rows": 0, "unchanged": 0, "release": release, "pending": max(0, len(due) - max_files), "skipped": skipped}
        if due:
            summary["county_map_rows"] = _climdiv_county_map(ctx, db, release)
        for code in due[:max_files]:
            released, version = newest[code]
            name = f"climdiv-{code}-v{version}-{released}"
            fetched = ctx.fetch(CLIMDIV + name, limit=150_000_000, timeout=900)
            lines = [raw.decode("latin-1") for raw in io.BytesIO(fetched.body) if raw.startswith(KANSAS_PREFIX[code[-2:]])]
            if not lines:
                raise FeedError(f"CLIMDIV_KANSAS_MISSING {name}")
            body = core.gz("".join(lines).encode("latin-1"))
            source, table, width = (("noaa-climdiv-normals", "kfm_climdiv_normals", 8) if code.startswith("norm-")
                                    else ("noaa-climdiv", "kfm_climdiv_monthly", 7))
            if core.sha256(body) in _versions(db, source, code):
                # NCEI dated the file again but its Kansas lines are the same (often so for the normals).
                summary["unchanged"] += 1
            else:
                path, digest = core.store_raw(ctx, "climdiv", f"{released}/{name}-kansas-{core.sha256(body)[:12]}.txt.gz", body,
                                              url=fetched.url, fetched=fetched, original=fetched.body,
                                              extra={"key": code, "release": released, "version": version, "kansas_lines": len(lines)})
                with core.pipeline_lock(ctx):
                    result = core.load_version(db, ctx, source_id=source, key=code, path=path, digest=digest, url=fetched.url,
                                               table=table, rows=climdiv_rows(lines, code, name), width=width)
                summary["files"] += 1
                summary["rows"] += result["rows"]
            state = _save(ctx, db, "climdiv", {**state, "releases": {**state.get("releases", {}), code: released}})
        return summary
    finally:
        db.close()


# --- U.S. Drought Monitor: weekly county and state statistics, a year per key ---------------------------------

USDM = "https://usdmdataservices.unl.edu/api/"
USDM_FIRST_YEAR = 2000
USDM_AREAS = {"county": ("CountyStatistics", "KS"), "state": ("StateStatistics", "20")}
USDM_MEASURES = {"area_percent": "GetDroughtSeverityStatisticsByAreaPercent",
                 "population_percent": "GetDroughtSeverityStatisticsByPopulationPercent"}
USDM_VARIANTS = [(level, measure, kind) for level in USDM_AREAS for measure in USDM_MEASURES for kind in (1, 2)]
USDM_HEADERS = {"county": ["MapDate", "FIPS", "County", "State", "None", "D0", "D1", "D2", "D3", "D4", "ValidStart", "ValidEnd", "StatisticFormatID"],
                "state": ["MapDate", "StateAbbreviation", "None", "D0", "D1", "D2", "D3", "D4", "ValidStart", "ValidEnd", "StatisticFormatID"]}
USDM_TABLES = """
CREATE TABLE IF NOT EXISTS kfm_usdm_county_stats (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, measure TEXT NOT NULL, map_date TEXT NOT NULL, fips TEXT NOT NULL,
  county TEXT, state TEXT, none REAL, d0 REAL, d1 REAL, d2 REAL, d3 REAL, d4 REAL, valid_start TEXT, valid_end TEXT,
  statistic_format_id INTEGER NOT NULL, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usdm_county_stats_county ON kfm_usdm_county_stats(fips, map_date);
CREATE TABLE IF NOT EXISTS kfm_usdm_state_stats (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, measure TEXT NOT NULL, map_date TEXT NOT NULL, state_abbreviation TEXT,
  none REAL, d0 REAL, d1 REAL, d2 REAL, d3 REAL, d4 REAL, valid_start TEXT, valid_end TEXT, statistic_format_id INTEGER NOT NULL,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_usdm_state_stats_day ON kfm_usdm_state_stats(map_date);
"""


def _gz_named(data: bytes, name: str) -> bytes:
    out = io.BytesIO()
    with gzip.GzipFile(filename=name, mode="wb", fileobj=out, mtime=0) as handle:
        handle.write(data)
    return out.getvalue()


def usdm_url(level: str, measure: str, kind: int, year: int) -> str:
    area, aoi = USDM_AREAS[level]
    return f"{USDM}{area}/{USDM_MEASURES[measure]}?aoi={aoi}&startdate=1/1/{year}&enddate=12/31/{year}&statisticsType={kind}"


def _tuesdays(year: int) -> tuple[date, date]:
    first, last = date(year, 1, 1), date(year, 12, 31)
    return first + timedelta((1 - first.weekday()) % 7), last - timedelta((last.weekday() - 1) % 7)


def usdm_due(state: dict, today: date) -> list:
    """[(year, reason)]: a newer weekly map ("new"), never loaded ("backfill"), then at most one yearly "recheck"."""
    years, due, recheck = state.get("years", {}), [], []
    for year in range(USDM_FIRST_YEAR, today.year + 1):
        first, last = _tuesdays(year)
        entry = years.get(str(year))
        if entry is None:
            if today >= first + timedelta(days=2):
                due.append((year, "new" if year == today.year else "backfill"))
        elif entry["through"] < f"{last:%Y%m%d}":
            if today >= datetime.strptime(entry["through"], "%Y%m%d").date() + timedelta(days=9):
                due.append((year, "new"))
        elif date.fromisoformat(entry["checked"]) <= today - timedelta(days=365):
            recheck.append((entry["checked"], year))
    due.sort(key=lambda d: (d[1] != "new", -d[0]))
    return due + [(year, "recheck") for _, year in sorted(recheck)[:1]]


def _usdm_rows(text: str, level: str, kind: int, year: int, url: str) -> list:
    reader = csv.reader(io.StringIO(text, newline=""))
    header = USDM_HEADERS[level]
    if next(reader, None) != header:
        raise FeedError(f"USDM_COLUMNS_CHANGED {url}")
    rows = []
    for row in reader:
        if not row:
            continue
        if len(row) != len(header):
            raise FeedError(f"USDM_ROW_SHAPE {url}")
        if (row[3] != "KS" or len(row[1]) != 5 or row[1][:2] != "20") if level == "county" else row[1] != "KS":
            raise FeedError(f"USDM_NOT_KANSAS {url}")
        if row[-1] != str(kind) or not re.fullmatch(r"\d{8}", row[0]):
            raise FeedError(f"USDM_ROW_VALUES {url}")
        if row[0][:4] == str(year):
            rows.append(row)
    return rows


def _usdm_year(ctx, db, year: int, known: bool) -> tuple[str | None, dict]:
    """Fetch and load the eight answers for a year. Returns the newest map date and counts."""
    through, counts = None, {"files": 0, "rows": 0, "unchanged": 0}
    for level, measure, kind in USDM_VARIANTS:
        url = usdm_url(level, measure, kind, year)
        fetched = ctx.fetch(url, limit=20_000_000, timeout=300)
        text = fetched.body.decode("utf-8-sig")
        if not text.strip():
            # The service answers an empty body for a period with no maps: only a new year may be empty.
            if known or year < ctx.now().year:
                raise FeedError(f"USDM_EMPTY_ANSWER {url}")
            continue
        rows = _usdm_rows(text, level, kind, year, url)
        if (level, measure, kind) == USDM_VARIANTS[0]:
            through = max((r[0] for r in rows), default=None)
        if not rows:
            continue
        # The gzip header names the answer, so two keys whose answers are byte-identical (area and population
        # percent agree when no county is split between categories) keep distinct raw objects.
        key, body = f"{level}/{measure}/{kind}/{year}", _gz_named(fetched.body, f"{level}-{measure}-{kind}-{year}.csv")
        if core.sha256(body) in _versions(db, f"usdm-{level}-statistics", key):
            counts["unchanged"] += 1
            continue
        path, digest = core.store_raw(ctx, "drought", f"{level}/{year}/{measure}-{kind}-{year}-{max(r[0] for r in rows)}-{core.sha256(body)[:12]}.csv.gz",
                                      body, url=url, fetched=fetched, extra={"key": key, "rows": len(rows)})
        with core.pipeline_lock(ctx):
            result = core.load_version(db, ctx, source_id=f"usdm-{level}-statistics", key=key, path=path, digest=digest, url=url,
                                       table=f"kfm_usdm_{level}_stats", rows=((measure, *r) for r in rows), width=len(USDM_HEADERS[level]) + 1)
        counts["files"] += 1
        counts["rows"] += result["rows"]
    return through, counts


def drought(ctx, max_years: int = 10) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(USDM_TABLES)
        state, today = core.get_state(db, "drought"), ctx.now().date()
        due = usdm_due(state, today)
        summary = {"years": [], "files": 0, "rows": 0, "unchanged": 0, "pending": max(0, len(due) - max_years)}
        for year, _ in due[:max_years]:
            entry = state.get("years", {}).get(str(year))
            through, counts = _usdm_year(ctx, db, year, entry is not None)
            for name, value in counts.items():
                summary[name] += value
            if through is None and entry is None:
                continue
            through = max(through or "", (entry or {}).get("through", ""))
            state = _save(ctx, db, "drought", {**state, "years": {**state.get("years", {}), str(year): {"through": through, "checked": str(today)}}})
            summary["years"].append(year)
        return {**summary, "through": max((e["through"] for e in state.get("years", {}).values()), default=None)}
    finally:
        db.close()
