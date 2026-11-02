"""KGS feed: the Kansas Geological Survey's oil and gas wells, leases, tops and production, and WWC5 water wells.

Provider: Kansas Geological Survey, https://www.kgs.ku.edu/PRS/Ora_Archive/, the download archive of
the KGS databases. The oil and gas page, https://www.kgs.ku.edu/PRS/petroDB.html, says access is
subject to the KGS public disclaimer: no warranty, the data are distributed "as is", the user assumes
all risk, and KGS does not certify the completeness or accuracy of production records. Production is
received monthly from the Kansas Department of Revenue. Water well records come to KGS "for
archival and public access" from KDHE's Water Well Program
(https://www.kgs.ku.edu/Magellan/WaterWell/index.html). Every file is Kansas only.

Files, each a zip holding one CSV of the same name (UTF-8, CRLF), each loaded into its own table:

- ``ks_wells``: the oil and gas well header database, one row per well.
- ``all_kansas_leases``: one row per lease, with cumulative production and first and last year.
- ``ks_tops``: formation tops picked in each well.
- ``oil_leases_<decade>`` and ``gas_leases_<decade>``: monthly lease production, 1980_1989 through
  2010_2019 and 2020_present. KGS also leaves 2010_2017, 2010_2018 and oil 2020_2029 in the archive,
  dated March 2025. They are earlier, partial cuts that overlap these, and they are not loaded.
- ``wwc5_wells_full``: the WWC5 water well completion records, with casing, screen, gravel pack and
  grout. ``wwc5_wells`` is the same wells with 29 of its 66 columns, value for value (checked
  2026-11-02), so it is not loaded. The ``wwc5_<County>.txt`` files are a September 2025 snapshot of
  the same 29 columns, since corrected in the statewide files, and are not loaded either.
- ``wwc5_lith_log``: the drillers' lithologic logs, one row per interval.

Names: KGS's public records are kept whole under the owner's 2026-11-02 policy. That includes lease
and well names (often a landowner's), operators (companies and individuals), free-text comments, and
the WWC5 owner, driller and directions (sometimes a mailing address). Publication outside the PC is
a separate, governed decision.

KGS quotes every value and escapes nothing. A value can hold a quote (``.375"``, ``Mississippi "Chat"``)
or a line break, so a record is read as the lines that split into exactly the header's number of
values. A csv reader would merge or alter those values.

Kept raw copy: the provider's zip, byte for byte. It is streamed to a temp file, checked whole, then
kept. Its receipt records the SHA-256 of the CSV inside, which decides whether a new version changed.

Schedule, per run: read the listing. A file is due when it was never loaded, or when its listed
modification time differs from the one loaded or seen and its last download is at least
``RECHECK_DAYS`` (28) days old. KGS receives production monthly and refreshes the current files
together (last on 2026-10-09, with production through June 2026). The decade files date from March
2025 and are static. A run handles at most ``max_files`` (4) files, so the first backfill of 15 files
takes four runs.

Revisions: each file is a ``load_version`` key (its name), so a new version replaces the old in one
transaction. A new version whose CSV is unchanged is not stored again; its listing time is recorded
as seen. A listed file that goes missing stops the run with ``KGS_FILE_MISSING`` after the others are
done.

Tables, after file_id and row_number, use the provider's column names in snake_case. Coordinates,
TOP, BOTTOM, BASE and the leases' cumulative PRODUCTION are REAL, and an empty one is NULL; the rest
are TEXT as published.

- ``kfm_kgs_wells``: every ks_wells column, plus ``api_county``, the 3-digit county code from
  API_NUMBER (``15-ccc-…``; Kansas API county codes are the FIPS codes).
- ``kfm_kgs_leases``, ``kfm_kgs_tops``, ``kfm_kgs_wwc5_wells`` and ``kfm_kgs_wwc5_lithology``: every
  column.
- ``kfm_kgs_lease_production``: lease_kid, field, producing_zone, operator, county, month_year, year,
  month, product, wells and production. year, month and wells are INTEGER and production is REAL.
  KGS repeats each lease's other columns (name, DOR code, API list, location, URL) on every month,
  as of the file's date; the kept zip has them, and ``kfm_kgs_leases`` has the current ones. Each
  file also gives one operator per lease, its operator of record when KGS wrote that file. So the
  decade files show earlier operators, not a change from month to month.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
import hashlib
from pathlib import Path
import re
from typing import Callable
import zipfile
import zlib

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

ARCHIVE = "https://www.kgs.ku.edu/PRS/Ora_Archive/"
TERMS = "https://www.kgs.ku.edu/PRS/petroDB.html"
WWC5_TERMS = "https://www.kgs.ku.edu/Magellan/WaterWell/index.html"
LISTED = re.compile(r'<a href="([A-Za-z0-9_]+)\.zip">[^<]*</a></td><td[^>]*>\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')
RECHECK_DAYS = 28
FILE_LIMIT = 400_000_000
TEXT_LIMIT = 4_000_000_000
API_COUNTY = re.compile(r"15-(\d{3})-")
MONTH_YEAR = re.compile(r"(\d{1,2})-(\d{4})")
WELLS = ("KID API_NUMBER API_NUM_NODASH LEASE WELL FIELD LATITUDE LONGITUDE LONG_LAT_SOURCE TOWNSHIP TWN_DIR RANGE RANGE_DIR SECTION "
         "SPOT FEET_NORTH FEET_EAST FOOT_REF ORIG_OPERATOR CURR_OPERATOR ELEVATION ELEV_REF SURFACE_ELEVATION_LIDAR DEPTH "
         "FORMATION_AT_TOTAL_DEPTH PRODUCE_FORM IP_OIL IP_GAS IP_WATER PERMIT SPUD COMPLETION PLUGGING MODIFIED OIL_KID OIL_DOR_ID "
         "GAS_KID GAS_DOR_ID KCC_PERMIT STATUS STATUS2 COMMENTS LEASE_WELL_NAME").split()
LEASES = ("LEASE_KID LEASE DOR_CODE API_NUMBER OPERATOR COUNTY TOWNSHIP TWN_DIR RANGE RANGE_DIR SECTION SPOT LATITUDE LONGITUDE "
          "PRODUCES PRODUCTION YEAR_START YEAR_STOP URL").split()
TOPS = "KID API_NUMBER API_NUM_NODASH LONGITUDE LATITUDE ELEVATION ELEV_REF FORMATION TOP BASE SOURCE UPDATED OLD_FORMATION".split()
PRODUCTION = ("LEASE_KID LEASE DOR_CODE API_NUMBER FIELD PRODUCING_ZONE OPERATOR COUNTY TOWNSHIP TWN_DIR RANGE RANGE_DIR SECTION "
              "SPOT LATITUDE LONGITUDE MONTH-YEAR PRODUCT WELLS PRODUCTION URL").split()
WWC5 = ("WELL_ID COUNTY TOWNSHIP TWN_DIR RANGE RANGE_DIR SECTION SPOT LONGITUDE LATITUDE LONG_LAT_TYPE OWNER WELL_USE COMPLE_DATE "
        "STATUS OTHER_ID DWR_NUMBER DIRECTIONS WELL_DEPTH ELEV STATIC_DEPTH EST_YIELD DRILLER CASING_TYPE CASING_JOINTS CASING_DIAM_1 "
        "CASING_DEPTH_1 CASING_DIAM_2 CASING_DEPTH_2 CASING_DIAM_3 CASING_DEPTH_3 CASING_HEIGHT CASING_WEIGHT CASING_THICKNESS "
        "SCREEN_PERFORATION_MATERIAL SCREEN_OPENINGS_TYPE SCREEN_FROM_1 SCREEN_TO_1 SCREEN_FROM_2 SCREEN_TO_2 SCREEN_FROM_3 SCREEN_TO_3 "
        "SCREEN_FROM_4 SCREEN_TO_4 GRAVELPACK_1_FROM GRAVELPACK_1_TO GRAVELPACK_2_FROM GRAVELPACK_2_TO GRAVELPACK_3_FROM GRAVELPACK_3_TO "
        "GROUT_TYPE GROUT_FROM_1 GROUT_TO_1 GROUT_FROM_2 GROUT_TO_2 GROUT_FROM_3 GROUT_TO_3 CONTAMINATION_SOURCE_TYPE "
        "CONTAM_SOURCE_DIRECTION CONTAM_SOURCE_DISTANCE WELL_KID SCANNED URL NAD83_LONGITUDE NAD83_LATITUDE "
        "CONTRACTORS_LICENSE_NUMBER").split()
LITHOLOGY = "WELL_ID LONGITUDE LATITUDE TOP BOTTOM LOG SOURCE NAD83_LONGITUDE NAD83_LATITUDE".split()
COORDINATES = ("LATITUDE", "LONGITUDE", "NAD83_LATITUDE", "NAD83_LONGITUDE")


def _snake(column: str) -> str:
    return column.lower().replace("-", "_")


@dataclass(frozen=True)
class Kind:
    source_id: str
    table: str
    header: list            # the provider's columns
    columns: list           # (name, type) after file_id and row_number
    row: Callable           # provider values -> table values
    indexes: tuple
    without_rowid: bool = False
    terms: str = TERMS

    def schema(self) -> str:
        quoted = lambda names: ", ".join(f'"{n}"' for n in names)
        sql = (f"CREATE TABLE IF NOT EXISTS {self.table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "
               + ", ".join(f'"{n}" {t}' for n, t in self.columns)
               + f", PRIMARY KEY(file_id, row_number)){' WITHOUT ROWID' if self.without_rowid else ''};\n")
        return sql + "".join(f"CREATE INDEX IF NOT EXISTS {self.table}_{'_'.join(i)} ON {self.table}({quoted(i)});\n" for i in self.indexes)


def _whole(source_id, table, header, real, indexes, extra=(), **options):
    """A table of every provider column, with the real columns' empty values NULL, plus derived TEXT columns."""
    numeric = {header.index(c) for c in real if c in header}

    def row(values):
        return (*(None if i in numeric and v == "" else v for i, v in enumerate(values)), *(f(values) for _, f in extra))
    columns = [(_snake(c), "REAL" if i in numeric else "TEXT") for i, c in enumerate(header)] + [(name, "TEXT") for name, _ in extra]
    return Kind(source_id, table, header, columns, row, indexes, **options)


def _api_county(values, at=WELLS.index("API_NUMBER")):
    m = API_COUNTY.match(values[at])
    return m.group(1) if m else None


def _production_kind() -> Kind:
    lease, field, zone, operator, county, month_year, product, wells, amount = (PRODUCTION.index(c) for c in (
        "LEASE_KID", "FIELD", "PRODUCING_ZONE", "OPERATOR", "COUNTY", "MONTH-YEAR", "PRODUCT", "WELLS", "PRODUCTION"))

    def row(v):
        m = MONTH_YEAR.fullmatch(v[month_year])
        return (v[lease], v[field], v[zone], v[operator], v[county], v[month_year], int(m.group(2)) if m else None,
                int(m.group(1)) if m else None, v[product], v[wells] or None, v[amount] or None)
    columns = [("lease_kid", "TEXT"), ("field", "TEXT"), ("producing_zone", "TEXT"), ("operator", "TEXT"), ("county", "TEXT"),
               ("month_year", "TEXT"), ("year", "INTEGER"), ("month", "INTEGER"), ("product", "TEXT"), ("wells", "INTEGER"),
               ("production", "REAL")]
    return Kind("kgs-lease-production", "kfm_kgs_lease_production", PRODUCTION, columns, row, (("lease_kid", "year", "month"),), True)


KINDS = {
    "wells": _whole("kgs-wells", "kfm_kgs_wells", WELLS, COORDINATES, (("api_number",), ("api_county",)), extra=(("api_county", _api_county),)),
    "leases": _whole("kgs-leases", "kfm_kgs_leases", LEASES, (*COORDINATES, "PRODUCTION"), (("lease_kid",), ("county",))),
    "tops": _whole("kgs-tops", "kfm_kgs_tops", TOPS, (*COORDINATES, "TOP", "BASE"), (("api_number",), ("formation",))),
    "production": _production_kind(),
    "wwc5_wells": _whole("kgs-wwc5-wells", "kfm_kgs_wwc5_wells", WWC5, COORDINATES,
                         (("well_id",), ("county",), ("township", "range", "range_dir", "section")), terms=WWC5_TERMS),
    "wwc5_lithology": _whole("kgs-wwc5-lithology", "kfm_kgs_wwc5_lithology", LITHOLOGY, (*COORDINATES, "TOP", "BOTTOM"), (("well_id",),),
                             without_rowid=True, terms=WWC5_TERMS),
}
DECADES = ("1980_1989", "1990_1999", "2000_2009", "2010_2019")
FILES = {"ks_wells": "wells", "all_kansas_leases": "leases", "ks_tops": "tops", "oil_leases_2020_present": "production",
         "gas_leases_2020_present": "production", "wwc5_wells_full": "wwc5_wells", "wwc5_lith_log": "wwc5_lithology",
         **{f"{p}_leases_{d}": "production" for p in ("oil", "gas") for d in DECADES}}


def _split(line: bytes) -> list:
    text = line.rstrip(b"\r\n").decode("utf-8")
    return text[1:-1].split('","') if len(text) >= 2 and text[0] == text[-1] == '"' else [text]


def _records(member, key: str, width: int, digest=None):
    """KGS's CSV records after the header. A value holding '","' falls back to a csv parse."""
    buffer, parts, n = None, 0, 0
    for raw in member:
        if digest is not None:
            digest.update(raw)
        if buffer is None and not raw.strip():
            continue
        buffer, parts = (raw, 1) if buffer is None else (buffer + raw, parts + 1)
        values = _split(buffer)
        if len(values) > width:
            try:
                values = next(csv.reader([buffer.rstrip(b"\r\n").decode("utf-8")]))
            except csv.Error:
                pass
        if len(values) == width:
            n += 1
            yield values
            buffer = None
        elif len(values) > width or parts >= 10:
            raise FeedError(f"KGS_ROW_SHAPE {key} {n + 1}")
    if buffer is not None:
        raise FeedError(f"KGS_ROW_SHAPE {key} {n + 1}")


def _open(path: Path, key: str):
    """The one CSV member of a KGS zip, after its header is checked."""
    archive = zipfile.ZipFile(path)
    members = archive.infolist()
    if [m.filename for m in members] != [key + ".txt"]:
        archive.close()
        raise FeedError(f"KGS_ZIP_CHANGED {key}")
    if members[0].file_size > TEXT_LIMIT:
        archive.close()
        raise FeedError(f"KGS_FILE_TOO_LARGE {key}")
    return archive, archive.open(members[0])


def _check(path: Path, key: str, kind: Kind) -> tuple[int, str]:
    """Read the whole download once: (rows, SHA-256 of the CSV inside)."""
    try:
        archive, member = _open(path, key)
        with archive, member:
            digest = hashlib.sha256()
            header = member.readline()
            digest.update(header)
            if _split(header) != kind.header:
                raise FeedError(f"KGS_COLUMNS_CHANGED {key}")
            return sum(1 for _ in _records(member, key, len(kind.header), digest)), digest.hexdigest()
    except (zipfile.BadZipFile, zlib.error, EOFError):
        raise FeedError(f"KGS_ZIP_INVALID {key}") from None
    except UnicodeDecodeError:
        raise FeedError(f"KGS_ENCODING_CHANGED {key}") from None


def _rows(path: Path, key: str, kind: Kind):
    try:
        archive, member = _open(path, key)
        with archive, member:
            if _split(member.readline()) != kind.header:
                raise FeedError(f"KGS_COLUMNS_CHANGED {key}")
            for values in _records(member, key, len(kind.header)):
                yield kind.row(values)
    except (zipfile.BadZipFile, zlib.error, EOFError):
        raise FeedError(f"KGS_ZIP_INVALID {key}") from None
    except UnicodeDecodeError:
        raise FeedError(f"KGS_ENCODING_CHANGED {key}") from None


def _loaded(db, kind: Kind, key: str) -> tuple[str, str | None, str]:
    """(listed time, SHA-256 of the CSV, retrieval day) of the loaded version of one file."""
    row = db.execute("SELECT json_extract(receipt_json,'$.listed'), json_extract(receipt_json,'$.content_sha256'), "
                     "json_extract(receipt_json,'$.retrieved_at') FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                     "AND json_extract(receipt_json,'$.key')=?", (kind.source_id, key)).fetchone()
    return (row[0] or "", row[1], (row[2] or "")[:10]) if row else ("", None, "")


def _file(ctx, db, state: dict, key: str, listed: str, summary: dict) -> dict:
    kind = KINDS[FILES[key]]
    full = core.temp_path(ctx, f"kgs-{key}.zip")
    try:
        fetched = core.download(ctx, ARCHIVE + key + ".zip", full, limit=FILE_LIMIT, timeout=900)
        rows, content = _check(full, key, kind)
        if not rows:
            raise FeedError(f"KGS_FILE_EMPTY {key}")
        if content == _loaded(db, kind, key)[1]:
            summary["unchanged"].append(key)
        else:
            path, digest = core.store_raw(ctx, "kgs-oil-gas", f"{key}/{key}-{listed[:10].replace('-', '')}-{content[:12]}.zip", full,
                                          url=fetched.url, fetched=fetched,
                                          extra={"key": key, "listed": listed, "rows": rows, "content_sha256": content, "terms": kind.terms})
            with core.pipeline_lock(ctx):
                db.executescript(kind.schema())
                result = core.load_version(db, ctx, source_id=kind.source_id, key=key, path=path, digest=digest, url=fetched.url,
                                           table=kind.table, rows=_rows(path, key, kind), width=len(kind.columns))
            summary["files"].append(key)
            summary["rows"] += result["rows"]
        state = {**state, "listed": {**state.get("listed", {}), key: listed}, "checked": {**state.get("checked", {}), key: str(ctx.now().date())}}
        with core.pipeline_lock(ctx):
            core.set_state(db, ctx, "kgs-oil-gas", state)
        return state
    finally:
        full.unlink(missing_ok=True)


def kgs_oil_gas(ctx, max_files: int = 4, recheck_days: int = RECHECK_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        state = core.get_state(db, "kgs-oil-gas")
        listing = dict(LISTED.findall(ctx.fetch(ARCHIVE, limit=4_000_000).body.decode("utf-8", "replace")))
        if not listing:
            raise FeedError("KGS_LISTING_CHANGED")
        today, due = ctx.now().date(), []
        for n, key in enumerate(FILES):
            if key not in listing:
                continue
            loaded_listed, _, loaded_day = _loaded(db, KINDS[FILES[key]], key)
            last = max(loaded_day, state.get("checked", {}).get(key, ""))
            known = state.get("listed", {}).get(key) or loaded_listed
            if not last or (listing[key] != known and (today - date.fromisoformat(last)).days >= recheck_days):
                due.append((last, n, key))
        summary = {"files": [], "rows": 0, "unchanged": []}
        for _, _, key in sorted(due)[:max_files]:
            state = _file(ctx, db, state, key, listing[key], summary)
        missing = [key for key in FILES if key not in listing]
        if missing:
            raise FeedError("KGS_FILE_MISSING " + ",".join(missing))
        return {**summary, "pending": [k for _, _, k in sorted(due)][max_files:]}
    finally:
        db.close()
