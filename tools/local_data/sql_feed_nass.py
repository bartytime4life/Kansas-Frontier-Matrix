"""NASS feed: the USDA Quick Stats bulk files, cut to Kansas.

Provider: USDA National Agricultural Statistics Service, https://www.nass.usda.gov/datasets/. NASS
estimates are public domain; NASS asks to be acknowledged
(https://www.nass.usda.gov/Data_and_Statistics/Citation_Request/index.php). The files hold published
aggregate estimates only. NASS itself withholds a value that would disclose an operation, as "(D)",
so there are no personal records.

Files: ``qs.<kind>_YYYYMMDD.txt.gz`` for crops (1.1 GB), animals_products, economics, demographics
(about 0.5 GB each) and environmental (75 MB). Each holds one whole Quick Stats sector:
tab-separated, a header row of 39 columns, CRLF, single-byte text, read as Latin-1 so that every
byte is kept. Older rows carry a lone NUL byte as CV_%. NASS republishes every file under a new
date, sometimes on consecutive days, and removes the older file.

Kansas: the rows whose STATE_ALPHA is ``KS``, at state, district, county, ZIP and watershed level.
Each must agree with STATE_FIPS_CODE 20, or the run stops with ``NASS_STATE_MISMATCH``. National,
regional and multi-state rows are not Kansas. The kept raw copy is the Kansas lines byte for byte,
header included; its receipt records the national file by size and SHA-256. Nothing is held in
memory: the national file is streamed to a temp file and cut line by line, and it is deleted after
the load.

Schedule, per run: read the listing. A kind is due when its newest file is dated after the one
loaded or seen, and its last download is at least ``MIN_DAYS`` (30) days old. Most Kansas values
change with NASS's monthly and quarterly reports and its annual county estimates; the weekly crop
progress series is the exception. A monthly reload catches every monthly cycle, keeps the national
downloads near 2.7 GB a month, and adds about a dozen Kansas copies a kind a year. Following NASS's
own cadence could mean downloading crops' 1.1 GB on consecutive days. A run handles at most
``max_kinds`` (2) kinds and starts none after ``RUN_BYTES`` downloaded, so crops runs alone. The
first backfill takes three runs.

Revisions: each new file replaces its kind whole. The load is ``load_version`` with key
``qs.<kind>``, and the older version is superseded in the same transaction. A new file whose Kansas
lines are unchanged is not stored again; its date is recorded as seen. A file NASS removes between
the listing and the download is left for the next run.

Table ``kfm_nass_quickstats``: file_id, row_number, then the 39 provider columns lowercased, with
``CV_%`` as ``cv_pct``. year is INTEGER, and a CV_% that is a lone NUL is NULL. Everything else is the
provider's TEXT: VALUE keeps its commas and codes such as (D), (Z) and (NA).
"""
from __future__ import annotations

from datetime import date
import gzip
import hashlib
from pathlib import Path
import re
import zlib

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

NASS = "https://www.nass.usda.gov/datasets/"
KINDS = ("crops", "animals_products", "economics", "demographics", "environmental")
NAME = re.compile(r"qs\.(" + "|".join(KINDS) + r")_(\d{8})\.txt\.gz")
COLUMNS = ("SOURCE_DESC SECTOR_DESC GROUP_DESC COMMODITY_DESC CLASS_DESC PRODN_PRACTICE_DESC UTIL_PRACTICE_DESC STATISTICCAT_DESC "
           "UNIT_DESC SHORT_DESC DOMAIN_DESC DOMAINCAT_DESC AGG_LEVEL_DESC STATE_ANSI STATE_FIPS_CODE STATE_ALPHA STATE_NAME ASD_CODE "
           "ASD_DESC COUNTY_ANSI COUNTY_CODE COUNTY_NAME REGION_DESC ZIP_5 WATERSHED_CODE WATERSHED_DESC CONGR_DISTRICT_CODE COUNTRY_CODE "
           "COUNTRY_NAME LOCATION_DESC YEAR FREQ_DESC BEGIN_CODE END_CODE REFERENCE_PERIOD_DESC WEEK_ENDING LOAD_TIME VALUE CV_%").split()
FIPS, ALPHA = COLUMNS.index("STATE_FIPS_CODE"), COLUMNS.index("STATE_ALPHA")
SOURCE_ID = "usda-nass-quickstats"
TABLE = "kfm_nass_quickstats"
SCHEMA = (f"CREATE TABLE IF NOT EXISTS {TABLE} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "
          + ", ".join(f"{c.lower().replace('%', 'pct')} {'INTEGER' if c == 'YEAR' else 'TEXT'}" for c in COLUMNS)
          + ", PRIMARY KEY(file_id, row_number));\n"
          f"CREATE INDEX IF NOT EXISTS {TABLE}_commodity ON {TABLE}(commodity_desc, year);\n"
          f"CREATE INDEX IF NOT EXISTS {TABLE}_county ON {TABLE}(county_ansi, year);\n")
MIN_DAYS = 30
RUN_BYTES = 600_000_000
FILE_LIMIT = 4_000_000_000


def _cut(full: Path, cut: Path, name: str) -> tuple[int, int, str]:
    """Stream one national file's Kansas lines into a gzip file: (Kansas rows, malformed national rows, SHA-256 of the Kansas text)."""
    digest, rows, odd = hashlib.sha256(), 0, 0
    try:
        with gzip.open(full, "rb") as source, open(cut, "wb") as handle, gzip.GzipFile(filename="", mode="wb", fileobj=handle, mtime=0) as out:
            header = source.readline()
            if header.rstrip(b"\r\n").decode("latin-1").split("\t") != COLUMNS:
                raise FeedError(f"NASS_COLUMNS_CHANGED {name}")
            out.write(header)
            digest.update(header)
            for line in source:
                if b"\tKS\t" not in line and b"\t20\t" not in line:
                    continue
                fields = line.rstrip(b"\r\n").split(b"\t")
                if len(fields) != len(COLUMNS):
                    if b"\tKS\t" in line:
                        raise FeedError(f"NASS_ROW_SHAPE {name}")
                    odd += 1
                    continue
                kansas = fields[ALPHA] == b"KS"
                if kansas != (fields[FIPS] == b"20"):
                    raise FeedError(f"NASS_STATE_MISMATCH {name}")
                if kansas:
                    out.write(line)
                    digest.update(line)
                    rows += 1
    except (gzip.BadGzipFile, EOFError, zlib.error):
        raise FeedError(f"NASS_GZIP_INVALID {name}") from None
    return rows, odd, digest.hexdigest()


def _rows(path: Path):
    with gzip.open(path, "rb") as handle:
        if handle.readline().rstrip(b"\r\n").decode("latin-1").split("\t") != COLUMNS:
            raise FeedError(f"NASS_COLUMNS_CHANGED {path.name}")
        for line in handle:
            yield tuple(None if v == "\x00" else v for v in line.rstrip(b"\r\n").decode("latin-1").split("\t"))


def _loaded(db, kind: str) -> tuple[str, str | None, str]:
    """(file date, SHA-256 of the Kansas text, retrieval day) of the loaded version of one kind."""
    row = db.execute("SELECT json_extract(receipt_json,'$.file_date'), json_extract(receipt_json,'$.content_sha256'), "
                     "json_extract(receipt_json,'$.retrieved_at') FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                     "AND json_extract(receipt_json,'$.key')=?", (SOURCE_ID, "qs." + kind)).fetchone()
    return (row[0] or "", row[1], (row[2] or "")[:10]) if row else ("", None, "")


def _kind(ctx, db, state: dict, kind: str, dated: str, summary: dict) -> dict:
    name = f"qs.{kind}_{dated}.txt.gz"
    full, cut = core.temp_path(ctx, "nass-" + name), core.temp_path(ctx, "nass-kansas-" + name)
    try:
        fetched = core.download(ctx, NASS + name, full, limit=FILE_LIMIT, timeout=900, missing_ok=True)
        if fetched is None:
            summary["replaced"].append(kind)
            return state
        summary["downloaded_bytes"] += full.stat().st_size
        rows, odd, content = _cut(full, cut, name)
        if not rows:
            raise FeedError(f"NASS_KANSAS_EMPTY {name}")
        if content == _loaded(db, kind)[1]:
            summary["unchanged"].append(kind)
        else:
            path, digest = core.store_raw(ctx, "nass", f"{kind}/{dated[:4]}/kansas-{name[:-7]}-{content[:12]}.txt.gz", cut, url=fetched.url,
                                          fetched=fetched, original=full, extra={"key": "qs." + kind, "file_date": dated, "kansas_rows": rows,
                                                                                 "content_sha256": content, "malformed_national_rows": odd})
            with core.pipeline_lock(ctx):
                result = core.load_version(db, ctx, source_id=SOURCE_ID, key="qs." + kind, path=path, digest=digest, url=fetched.url,
                                           table=TABLE, rows=_rows(path), width=len(COLUMNS))
            summary["kinds"].append(kind)
            summary["rows"] += result["rows"]
        state = {**state, "seen": {**state.get("seen", {}), kind: dated}, "checked": {**state.get("checked", {}), kind: str(ctx.now().date())}}
        with core.pipeline_lock(ctx):
            core.set_state(db, ctx, "nass", state)
        return state
    finally:
        full.unlink(missing_ok=True)
        cut.unlink(missing_ok=True)


def nass(ctx, max_kinds: int = 2, run_bytes: int = RUN_BYTES, min_days: int = MIN_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(SCHEMA)
        state = core.get_state(db, "nass")
        newest = {}
        for m in NAME.finditer(ctx.fetch(NASS, limit=4_000_000).body.decode("latin-1")):
            newest[m.group(1)] = max(newest.get(m.group(1), ""), m.group(2))
        if not newest:
            raise FeedError("NASS_LISTING_CHANGED")
        today, due = ctx.now().date(), []
        for kind, dated in newest.items():
            loaded_date, _, loaded_day = _loaded(db, kind)
            last = max(loaded_day, state.get("checked", {}).get(kind, ""))
            if dated > max(loaded_date, state.get("seen", {}).get(kind, "")) and (not last or (today - date.fromisoformat(last)).days >= min_days):
                due.append((last, KINDS.index(kind), kind))
        summary = {"kinds": [], "rows": 0, "unchanged": [], "replaced": [], "downloaded_bytes": 0}
        done = 0
        for _, _, kind in sorted(due):
            if done >= max_kinds or summary["downloaded_bytes"] >= run_bytes:
                break
            state = _kind(ctx, db, state, kind, newest[kind], summary)
            done += 1
        return {**summary, "pending": [k for _, _, k in sorted(due)][done:], "newest": newest}
    finally:
        db.close()
