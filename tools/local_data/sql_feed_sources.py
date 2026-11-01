"""SQL feeds that need only the standard library: captures, IEM wind, GHCN-Daily, Storm Events, ASOS.

Each function takes a ``sql_feeds.Context``, does its network work outside the pipeline lock and its
database writes inside it, and returns a short summary. See ``sql_feeds`` for the shared rules.
"""
from __future__ import annotations

from collections import defaultdict
import csv
from datetime import date, timedelta
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

# --- Captures: automatic review of the owner-approved hourly sources, then SQL ---------------------

CAPTURE_SOURCES = {
    "usgs-streamflow": ("hydrology", "https://www.usgs.gov/faqs/are-usgs-reportspublications-copyrighted"),
    "nws-alerts": ("atmosphere", "https://www.weather.gov/disclaimer"),
    "usgs-earthquakes": ("geology", "https://www.usgs.gov/data-management/data-licensing"),
}
CAPTURE_REVIEWER = "sql-feeds automatic capture policy"
CAPTURE_NOTE = ("Automatic review under the owner's 2026-11-01 approval for these three sources: verified the capture receipt, "
                "SHA-256, byte count, GeoJSON structure and {n} features. Public provider environmental data; no personal records. "
                "Accepted for local SQL processing and the owner-approved public local-data API. Provisional values, source clocks, "
                "empty responses and original properties are preserved.")


def _capture_receipts(ctx):
    receipts = defaultdict(list)
    for path in (ctx.root / "data/receipts/ingest/pc-pipeline").glob("*.json"):
        r = json.loads(path.read_text())
        receipts[(r.get("sourceId"), r.get("sha256"))].append(r)
    return receipts


def _feature_collection(raw: bytes) -> dict:
    payload = json.loads(raw)
    if payload.get("type") != "FeatureCollection" or not isinstance(payload.get("features"), list):
        raise ValueError("invalid feature collection")
    if any(not isinstance(f, dict) or f.get("type") != "Feature" or not isinstance(f.get("properties"), dict) for f in payload["features"]):
        raise ValueError("invalid feature")
    return payload


def review_captures(ctx) -> dict:
    """Record the review the Oct 31 one-off script recorded by hand, for every new capture that passes."""
    from tools.local_data import intake, intake_review, intake_route

    receipts, budget, reviewed, held = _capture_receipts(ctx), intake_route.load_budget(), 0, []
    with intake.open_index(ctx.root, read_only=True) as conn:
        ids = [r[0] for r in conn.execute("SELECT id FROM items WHERE present=1 AND status='review'")]
    for identity in ids:
        item = intake.get_item(ctx.root, identity, read_only=True)
        source = item["relative_path"].split("/")[0]
        if source not in CAPTURE_SOURCES:
            continue
        try:
            if item["decision"]["blocking_issues"]:
                raise ValueError("file blockers")
            matching = receipts[(source, item["sha256"])]
            if not matching or any(r.get("byteLength") != item["size_bytes"] for r in matching):
                raise ValueError("missing matching provenance receipt")
            raw = (ctx.root / item["store_path"]).read_bytes()
            if hashlib.sha256(raw).hexdigest() != item["sha256"]:
                raise ValueError("capture digest mismatch")
            payload = _feature_collection(raw)
            with intake.open_index(ctx.root, read_only=True) as conn:
                history = intake_review.history(conn, identity)
            domain, reference = CAPTURE_SOURCES[source]
            intake_review.save(ctx.root, {
                "id": identity, "sha256": item["sha256"], "revision": history[0]["revision"] if history else 0,
                "decision": "local", "domain": domain, "rights": "allowed", "sensitivity": "public", "reference": reference,
                "reviewer": CAPTURE_REVIEWER, "confirmed": True, "note": CAPTURE_NOTE.format(n=len(payload["features"])),
            }, budget)
            reviewed += 1
        except (ValueError, KeyError) as error:
            held.append({"id": identity, "reason": str(error)})
    return {"reviewed": reviewed, "held": len(held), "held_reasons": sorted({h["reason"] for h in held})}


def load_captures(ctx, db) -> int:
    """Reviewed captures into kfm_environmental_features, one transaction per capture file."""
    from tools.local_data import intake

    receipts, files = _capture_receipts(ctx), 0
    with intake.open_index(ctx.root, read_only=True) as conn:
        items = [dict(zip(("relative_path", "store_path", "sha256"), r)) for r in
                 conn.execute("SELECT relative_path, store_path, sha256 FROM items WHERE present=1 AND status IN ('reviewed','ready')")]
    for item in items:
        source = item["relative_path"].split("/")[0]
        matching = receipts.get((source, item["sha256"]))
        if source not in CAPTURE_SOURCES or not matching or core.loaded(db, item["sha256"]):
            continue
        path = ctx.root / item["store_path"]
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != item["sha256"]:
            raise FeedError(f"CAPTURE_CHANGED {item['store_path']}")
        payload, receipt = _feature_collection(raw), matching[0]
        file_id = core.begin_source(db, ctx, source, path, item["sha256"], receipt.get("sourceUrl", ""), receipt)
        try:
            for n, feature in enumerate(payload["features"], 1):
                body = core.canonical(feature)
                digest = hashlib.sha256(body.encode()).hexdigest()
                db.execute("INSERT OR IGNORE INTO kfm_environmental_features VALUES (?,?,?,?)", (source, digest, str(feature.get("id", "")), body))
                db.execute("INSERT INTO kfm_environmental_capture_features VALUES (?,?,?,?)", (file_id, n, source, digest))
            if len(payload["features"]) != receipt.get("featureCount", len(payload["features"])):
                raise FeedError("CAPTURE_FEATURE_COUNT_MISMATCH")
            core.finish_source(db, file_id, len(payload["features"]))
        except BaseException:
            db.execute("ROLLBACK")
            raise
        files += 1
    return files


def captures(ctx) -> dict:
    with core.pipeline_lock(ctx):
        review = review_captures(ctx)
        db = core.open_db(ctx)
        try:
            files = load_captures(ctx, db)
        finally:
            db.close()
    return {**review, "files_loaded": files}


# --- IEM wind: daily observations and summaries for the Kansas ASOS network --------------------------

IEM = "https://mesonet.agron.iastate.edu/cgi-bin/request/"
WIND_FIELDS = ["drct", "sknt", "gust", "peak_wind_gust", "peak_wind_drct", "peak_wind_time"]
WIND_INCREMENTAL_FROM = date(2026, 11, 1)   # the backfill covers 2003-01-01 through 2026-10-31
WIND_BACKFILL_FIRST = 2003
WIND_DAILY_THROUGH = date(2026, 9, 23)      # last day in the archived daily collection


def _wind_obs_url(stations, start: date, end_exclusive: date) -> str:
    params = [("station", s) for s in stations] + [("data", f) for f in WIND_FIELDS] + [
        ("year1", start.year), ("month1", start.month), ("day1", start.day),
        ("year2", end_exclusive.year), ("month2", end_exclusive.month), ("day2", end_exclusive.day),
        ("tz", "Etc/UTC"), ("format", "onlycomma"), ("latlon", "no"), ("elev", "no"), ("missing", "M"), ("trace", "T"),
        ("direct", "no"), ("report_type", 3), ("report_type", 4)]
    return IEM + "asos.py?" + urllib.parse.urlencode(params)


def _wind_daily_url(stations, start: date, end: date) -> str:
    params = [("network", "KS_ASOS")] + [("stations", s) for s in stations] + [
        ("year1", start.year), ("month1", start.month), ("day1", start.day), ("year2", end.year), ("month2", end.month), ("day2", end.day),
        ("var", "avg_wind_speed_kts"), ("var", "max_wind_speed_kts"), ("var", "max_wind_gust_kts"), ("na", "None"), ("format", "csv")]
    return IEM + "daily.py?" + urllib.parse.urlencode(params)


def _load_csv(ctx, db, source_id, path, digest, url, receipt, table, header, width_out, transform=lambda row: row) -> int:
    with gzip.open(path, "rt", newline="") as handle:
        reader = csv.reader(handle)
        if next(reader, None) != header:
            raise FeedError(f"COLUMNS_CHANGED {source_id}")
        file_id = core.begin_source(db, ctx, source_id, path, digest, url, receipt)
        if file_id is None:
            return 0
        try:
            rows, count = [], 0
            for n, row in enumerate(reader, 1):
                if len(row) != len(header):
                    raise FeedError(f"ROW_SHAPE {source_id} {n}")
                rows.append((file_id, n, *transform(row)))
                if len(rows) == 20000:
                    db.executemany(f"INSERT INTO {table} VALUES ({','.join('?' * (width_out + 2))})", rows)
                    count += len(rows)
                    rows = []
            if rows:
                db.executemany(f"INSERT INTO {table} VALUES ({','.join('?' * (width_out + 2))})", rows)
                count += len(rows)
            core.finish_source(db, file_id, count)
            return count
        except BaseException:
            db.execute("ROLLBACK")
            raise


def _wind_window(ctx, db, stations, start: date, end: date, *, label: str) -> int:
    fetched = ctx.fetch(_wind_obs_url(stations, start, end + timedelta(days=1)), limit=600_000_000, timeout=1200)
    path, digest = core.store_raw(ctx, "iem-wind", f"observations/{start.year}/obs-{start:%Y%m%d}-{end:%Y%m%d}.csv.gz",
                                  core.gz(fetched.body), url=fetched.url, fetched=fetched, extra={"window": [str(start), str(end)], "role": label})
    with core.pipeline_lock(ctx):
        return _load_csv(ctx, db, "iem-wind-observations", path, digest, fetched.url, core.receipt_for(ctx, path), "kfm_wind_observations",
                         ["station", "valid", *WIND_FIELDS], 8)


def _save(ctx, db, feed, state):
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, feed, state)
    return state


def iem_wind(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        state = core.get_state(db, "iem-wind")
        stations = [r[0] for r in db.execute("SELECT station_id FROM kfm_wind_stations ORDER BY station_id")]
        if not stations:
            raise FeedError("WIND_STATIONS_MISSING")
        yesterday = ctx.now().date() - timedelta(days=1)
        summary = {"observation_rows": 0, "daily_rows": 0, "backfill_year": None}
        # New readings, at most 31 days per request.
        through = date.fromisoformat(state.get("obs_through", str(WIND_INCREMENTAL_FROM - timedelta(days=1))))
        while through < yesterday:
            start, end = through + timedelta(days=1), min(yesterday, through + timedelta(days=31))
            summary["observation_rows"] += _wind_window(ctx, db, stations, start, end, label="incremental")
            through = end
            state = _save(ctx, db, "iem-wind", {**state, "obs_through": str(through)})
        # New daily summaries.
        daily = date.fromisoformat(state.get("daily_through", str(WIND_DAILY_THROUGH)))
        while daily < yesterday:
            start, end = daily + timedelta(days=1), min(yesterday, daily + timedelta(days=366))
            fetched = ctx.fetch(_wind_daily_url(stations, start, end), limit=200_000_000, timeout=900)
            path, digest = core.store_raw(ctx, "iem-wind", f"daily/{start.year}/daily-{start:%Y%m%d}-{end:%Y%m%d}.csv.gz",
                                          core.gz(fetched.body), url=fetched.url, fetched=fetched, extra={"window": [str(start), str(end)]})
            with core.pipeline_lock(ctx):
                summary["daily_rows"] += _load_csv(ctx, db, "iem-wind-daily", path, digest, fetched.url, core.receipt_for(ctx, path), "kfm_wind_daily",
                                                   ["station", "day", "avg_wind_speed_kts", "max_wind_speed_kts", "max_wind_gust_kts", "network"], 5,
                                                   transform=lambda row: row[:5])
            daily = end
            state = _save(ctx, db, "iem-wind", {**state, "daily_through": str(daily)})
        # Backfill: one year of readings per run, oldest first, so IEM is asked for a year at a time.
        year = int(state.get("obs_backfill_next", WIND_BACKFILL_FIRST))
        if year <= WIND_INCREMENTAL_FROM.year:
            end = min(date(year, 12, 31), WIND_INCREMENTAL_FROM - timedelta(days=1))
            summary["observation_rows"] += _wind_window(ctx, db, stations, date(year, 1, 1), end, label="backfill")
            summary["backfill_year"] = year
            state = _save(ctx, db, "iem-wind", {**state, "obs_backfill_next": year + 1})
        return {**summary, "obs_through": state.get("obs_through"), "daily_through": state.get("daily_through")}
    finally:
        db.close()


# --- GHCN-Daily: NOAA's daily update files, kept as a Kansas revision overlay -----------------------

GHCN = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/"
GHCN_DIFF = re.compile(r"superghcnd_diff_(\d{8})_to_(\d{8})\.tar\.gz")
GHCN_FIRST_FROM = "20261006"   # the archived station files were captured 2026-10-07
GHCN_REVISIONS = """
CREATE TABLE IF NOT EXISTS kfm_ghcnd_daily_revisions (
  station_id TEXT NOT NULL, observation_day INTEGER NOT NULL, element TEXT NOT NULL, file_id INTEGER NOT NULL,
  row_number INTEGER NOT NULL, action TEXT NOT NULL CHECK(action IN ('insert','update','delete')), raw_value INTEGER NOT NULL,
  measurement_flag TEXT NOT NULL, quality_flag TEXT NOT NULL, source_flag TEXT NOT NULL, observation_time TEXT NOT NULL,
  PRIMARY KEY(station_id, observation_day, element, file_id, row_number)) WITHOUT ROWID;
"""


def _ghcnd_stations(ctx, db, state) -> dict:
    """Refresh Kansas station metadata from ghcnd-stations.txt every 30 days; new stations are added."""
    today = ctx.now().date()
    if state.get("stations_checked") and date.fromisoformat(state["stations_checked"]) > today - timedelta(days=30):
        return state
    fetched = ctx.fetch(GHCN + "ghcnd-stations.txt", limit=32_000_000, timeout=300)
    kansas = [line for line in fetched.body.decode("latin-1").splitlines() if line[38:40] == "KS"]
    if not kansas:
        raise FeedError("GHCN_STATION_LIST_EMPTY")
    body = ("\n".join(kansas) + "\n").encode("latin-1")
    path, digest = core.store_raw(ctx, "ghcnd", f"stations/ghcnd-stations-KS-{today:%Y%m%d}.txt.gz", core.gz(body), url=fetched.url,
                                  fetched=fetched, original=fetched.body, extra={"kansas_lines": len(kansas)})
    with core.pipeline_lock(ctx):
        file_id = core.begin_source(db, ctx, "noaa-ghcnd-stations", path, digest, fetched.url, core.receipt_for(ctx, path))
        added = 0
        if file_id is not None:
            try:
                for line in kansas:
                    sid = line[0:11]
                    meta = {"station_id": sid, "name": line[41:71].strip(), "latitude": float(line[12:20]), "longitude": float(line[21:30]),
                            "elevation_m": float(line[31:37]), "state": "KS", "source": "ghcnd-stations.txt", "added_by": "sql-feeds"}
                    added += db.execute("INSERT OR IGNORE INTO kfm_ghcnd_stations VALUES (?,?,?,?,?,?)",
                                        (sid, meta["name"], meta["latitude"], meta["longitude"], meta["elevation_m"], core.canonical(meta))).rowcount
                core.finish_source(db, file_id, added)
            except BaseException:
                db.execute("ROLLBACK")
                raise
        state = {**state, "stations_checked": str(today), "stations_added": state.get("stations_added", 0) + added}
        core.set_state(db, ctx, "ghcnd", state)
    return state


def ghcnd(ctx, max_files: int = 40) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(GHCN_REVISIONS)
        state = _ghcnd_stations(ctx, db, core.get_state(db, "ghcnd"))
        kansas = {r[0] for r in db.execute("SELECT station_id FROM kfm_ghcnd_stations")}
        listing = ctx.fetch(GHCN + "superghcnd/", limit=4_000_000).body.decode("latin-1")
        applied = state.get("applied_through", GHCN_FIRST_FROM)
        diffs = sorted({(m.group(1), m.group(2)) for m in GHCN_DIFF.finditer(listing) if m.group(1) >= applied})
        summary = {"files": 0, "kansas_rows": 0}
        for start, end in diffs[:max_files]:
            name = f"superghcnd_diff_{start}_to_{end}.tar.gz"
            fetched = ctx.fetch(GHCN + "superghcnd/" + name, limit=256_000_000, timeout=600)
            rows = []
            with tarfile.open(fileobj=io.BytesIO(fetched.body), mode="r:gz") as tar:
                for member in tar.getmembers():
                    action = Path(member.name).stem
                    if not member.isfile() or action not in ("insert", "update", "delete"):
                        continue
                    for record in csv.reader(io.TextIOWrapper(tar.extractfile(member), encoding="latin-1", newline="")):
                        if record and record[0] in kansas:
                            if len(record) != 8 or len(record[1]) != 8:
                                raise FeedError(f"GHCN_DIFF_ROW_SHAPE {name}")
                            rows.append([action, *record])
            body = "".join(",".join(r) + "\n" for r in [["action", "station", "date", "element", "value", "mflag", "qflag", "sflag", "obstime"], *rows]).encode("latin-1")
            path, digest = core.store_raw(ctx, "ghcnd", f"diffs/{start[:4]}/kansas-{start}-to-{end}.csv.gz", core.gz(body), url=fetched.url,
                                          fetched=fetched, original=fetched.body, extra={"kansas_rows": len(rows), "window": [start, end]})
            with core.pipeline_lock(ctx):
                file_id = core.begin_source(db, ctx, "noaa-ghcnd-diff", path, digest, fetched.url, core.receipt_for(ctx, path))
                if file_id is not None:
                    try:
                        db.executemany("INSERT INTO kfm_ghcnd_daily_revisions VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                                       [(r[1], int(r[2]), r[3], file_id, n, r[0], int(r[4]), r[5], r[6], r[7], r[8]) for n, r in enumerate(rows, 1)])
                        core.finish_source(db, file_id, len(rows))
                    except BaseException:
                        db.execute("ROLLBACK")
                        raise
                state = {**state, "applied_through": end}
                core.set_state(db, ctx, "ghcnd", state)
            summary["files"] += 1
            summary["kansas_rows"] += len(rows)
        return {**summary, "applied_through": state.get("applied_through", applied), "pending": max(0, len(diffs) - max_files)}
    finally:
        db.close()


# --- Storm Events: newer NCEI yearly files replace the version loaded before ------------------------

STORM = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
STORM_NAME = re.compile(r"StormEvents_(details|locations|fatalities)-ftp_v1\.0_d(\d{4})_c(\d{8})\.csv\.gz")
STORM_KINDS = ("details", "locations", "fatalities")


def _storm_loaded(db, year: str, kind: str):
    """[(file_id, created, sha256)] of the loaded versions of one year's file."""
    rows = db.execute("SELECT file_id, source_path, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' AND source_path LIKE ?",
                      (f"noaa-storm-events-{kind}", f"%_d{year}_c%")).fetchall()
    return [(fid, STORM_NAME.search(p).group(3), sha) for fid, p, sha in rows if STORM_NAME.search(p)]


def _storm_current(db, state: dict, year: str, kind: str) -> str:
    """The newest NCEI publication date handled: loaded, or seen with Kansas rows already loaded."""
    return max([c for _, c, _ in _storm_loaded(db, year, kind)] + [state.get("seen", {}).get(f"{year}|{kind}", "")], default="")


def storm_events(ctx, max_years: int = 6) -> dict:
    db = core.open_db(ctx)
    try:
        state = core.get_state(db, "storm-events")
        listing = ctx.fetch(STORM, limit=2_000_000).body.decode("latin-1")
        newest = {}
        for m in STORM_NAME.finditer(listing):
            key = (m.group(2), m.group(1))
            newest[key] = max(newest.get(key, ""), m.group(3))
        # A year is due when any of its three files is newer than the version loaded.
        years = sorted({y for (y, kind), c in newest.items() if int(y) >= 1950 and c > _storm_current(db, state, y, kind)})
        summary = {"years": [], "rows": 0}
        for year in years[:max_years]:
            for kind in STORM_KINDS:
                created = newest.get((year, kind))
                previous = _storm_loaded(db, year, kind)
                if not created or created <= _storm_current(db, state, year, kind):
                    continue
                name = f"StormEvents_{kind}-ftp_v1.0_d{year}_c{created}.csv.gz"
                fetched = ctx.fetch(STORM + name, limit=256_000_000, timeout=900)
                text = gzip.decompress(fetched.body).decode("utf-8")
                reader = csv.reader(io.StringIO(text, newline=""))
                header = next(reader)
                columns = [c.lower() for c in header]
                existing = [r[1] for r in db.execute(f"PRAGMA table_info(kfm_storm_event_{kind})")][2:]
                # NCEI adds columns at the end now and then (2026: event_yearmonth in fatalities): add them
                # as TEXT. A removed or renamed column stops the feed.
                if columns[:len(existing)] != existing or any(not re.fullmatch(r"[a-z0-9_]{1,64}", c) for c in columns):
                    raise FeedError(f"STORM_COLUMNS_CHANGED {name}")
                added = columns[len(existing):]
                if kind == "details":
                    state_col = header.index("STATE_FIPS")
                    keep = [r for r in reader if len(r) == len(header) and r[state_col] == "20"]
                else:
                    with core.pipeline_lock(ctx):
                        events = {r[0] for r in db.execute("SELECT event_id FROM kfm_storm_event_details WHERE year=?", (year,))}
                    event_col = header.index("EVENT_ID")
                    keep = [r for r in reader if len(r) == len(header) and r[event_col] in events]
                out = io.StringIO()
                csv.writer(out, lineterminator="\n").writerows([header, *keep])
                path, digest = core.store_raw(ctx, "storm-events", f"{year}/kansas-{name}", core.gz(out.getvalue().encode()), url=fetched.url,
                                              fetched=fetched, original=fetched.body, extra={"kansas_rows": len(keep), "supersedes": [c for _, c, _ in previous]})
                with core.pipeline_lock(ctx):
                    file_id = core.begin_source(db, ctx, f"noaa-storm-events-{kind}", path, digest, fetched.url, core.receipt_for(ctx, path))
                    if file_id is None:
                        # These exact Kansas rows are already loaded (an NCEI re-release with no Kansas change,
                        # or a header-only subset shared with another year). Record the publication date so
                        # the year stops being due; if this year's loaded version differed, it is now empty.
                        if keep and digest not in {sha for _, _, sha in previous}:
                            raise FeedError(f"STORM_CONTENT_SHARED {name}")
                        db.execute("BEGIN IMMEDIATE")
                        if digest not in {sha for _, _, sha in previous}:
                            for old, _, _ in previous:
                                db.execute(f"DELETE FROM kfm_storm_event_{kind} WHERE file_id=?", (old,))
                                db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))
                        state = {**state, "seen": {**state.get("seen", {}), f"{year}|{kind}": created}}
                        core.set_state(db, ctx, "storm-events", state)
                        db.execute("COMMIT")
                        continue
                    try:
                        for column in added:
                            db.execute(f'ALTER TABLE kfm_storm_event_{kind} ADD COLUMN "{column}" TEXT')
                        # A newer NCEI file is a full replacement of that year's rows.
                        for old, _, _ in previous:
                            db.execute(f"DELETE FROM kfm_storm_event_{kind} WHERE file_id=?", (old,))
                            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))
                        db.executemany(f"INSERT INTO kfm_storm_event_{kind} VALUES ({','.join('?' * (len(header) + 2))})",
                                       [(file_id, n, *r) for n, r in enumerate(keep, 1)])
                        core.finish_source(db, file_id, len(keep))
                    except BaseException:
                        db.execute("ROLLBACK")
                        raise
                summary["rows"] += len(keep)
            summary["years"].append(year)
        return {**summary, "pending_years": max(0, len(years) - max_years)}
    finally:
        db.close()


# --- ASOS 5-minute (TD-6401): backfill a year per run for the five archived airports ----------------

ASOS = "https://www.ncei.noaa.gov/pub/data/asos-fivemin/"
ASOS_STATIONS = ("KCNK", "KDDC", "KGLD", "KICT", "KTOP")
ASOS_FIRST = 2001
WIND_TOKEN = re.compile(r"^(\d{3}|VRB)(\d{2,3})(?:G(\d{2,3}))?KT$")
TEMP_TOKEN = re.compile(r"^(M?\d{2})/(M?\d{2})?$")
ALT_TOKEN = re.compile(r"^A(\d{4})$")


def _celsius(token):
    return None if token is None else (-int(token[1:]) if token.startswith("M") else int(token))


def decode_asos(line: str):
    """(wban, icao, local_time, utc_ddhhmmZ, wind_dir, wind_kt, gust_kt, vis_sm, temp_c, dew_c, altimeter_inhg).

    The same decoding as the 2000 load: values only from unambiguous METAR tokens, else None.
    """
    wban, icao, local = line[0:5], line[5:9], line[13:25]
    i = line.find("5-MIN ")
    tokens = line[i + 6:].split() if i >= 0 else []
    utc = next((t for t in tokens[1:3] if re.fullmatch(r"\d{6}Z", t)), None)
    wind = next((WIND_TOKEN.match(t) for t in tokens if WIND_TOKEN.match(t)), None)
    vis_i = next((n for n, t in enumerate(tokens) if t.endswith("SM") and re.fullmatch(r"[0-9/]+", t[:-2])), None)
    vis = None if vis_i is None else tokens[vis_i][:-2]
    if vis and "/" in vis and vis_i > 0 and tokens[vis_i - 1].isdigit():
        vis = f"{tokens[vis_i - 1]} {vis}"
    alt_i = next((n for n, t in enumerate(tokens) if ALT_TOKEN.match(t)), None)
    temp = TEMP_TOKEN.match(tokens[alt_i - 1]) if alt_i else None
    return (wban, icao, local, utc,
            wind.group(1) if wind else None, int(wind.group(2)) if wind else None, int(wind.group(3)) if wind and wind.group(3) else None,
            vis, _celsius(temp.group(1)) if temp else None, _celsius(temp.group(2)) if temp and temp.group(2) else None,
            int(ALT_TOKEN.match(tokens[alt_i]).group(1)) / 100 if alt_i is not None else None)


def asos_fivemin(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        state = core.get_state(db, "asos-5min")
        year = int(state.get("next_year", ASOS_FIRST))
        listing = ctx.fetch(ASOS, limit=1_000_000).body.decode("latin-1")
        available = {int(y) for y in re.findall(r"6401-(\d{4})/", listing)}
        if year not in available:
            return {"year": None, "rows": 0, "note": f"NCEI has no 6401-{year} folder yet; the archive ends {max(available, default=0)}"}
        summary = {"year": year, "files": 0, "missing": 0, "rows": 0}
        for icao in ASOS_STATIONS:
            for month in range(1, 13):
                name = f"6401-{year}/64010{icao}{year}{month:02d}.dat"
                fetched = ctx.fetch(ASOS + name, limit=64_000_000, timeout=300, missing_ok=True)
                if fetched is None:
                    summary["missing"] += 1
                    continue
                path, digest = core.store_raw(ctx, "asos-5min", name + ".gz", core.gz(fetched.body), url=fetched.url, fetched=fetched)
                lines = [l for l in fetched.body.decode("latin-1").splitlines()]
                with core.pipeline_lock(ctx):
                    file_id = core.begin_source(db, ctx, "noaa-asos-fivemin", path, digest, fetched.url, core.receipt_for(ctx, path))
                    if file_id is None:
                        continue
                    try:
                        rows = [(file_id, n, *decode_asos(raw), raw) for n, raw in enumerate(lines, 1) if raw.strip()]
                        db.executemany("INSERT INTO kfm_asos_fivemin VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
                        core.finish_source(db, file_id, len(rows))
                    except BaseException:
                        db.execute("ROLLBACK")
                        raise
                summary["files"] += 1
                summary["rows"] += len(rows)
        with core.pipeline_lock(ctx):
            core.set_state(db, ctx, "asos-5min", {**state, "next_year": year + 1})
        return summary
    finally:
        db.close()
