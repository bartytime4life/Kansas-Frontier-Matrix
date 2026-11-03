"""SQL feeds for Kansas institutions and records: FDIC banks, IRS exempt organizations, IMLS museums and
libraries, NCES schools and colleges, the USGS historical topographic map inventory and USGS water samples.

This module rebuilds the lost ``sql_feed_records.py`` (``banks``, ``exempt-orgs``, ``museums-libraries``,
``schools``, ``historical-topo-maps``) and the ``usgs-samples`` feed of the lost ``sql_feed_biodiversity.py``
against the data they loaded: the same tables (DDL and indexes copied from the database), the same receipt
keys and kept-file names, the same feed-state fields. Each provider file is cut to Kansas at once; the Kansas
part is kept gzipped under ``data/raw/sql-feeds/<feed>/`` as ``<name>-<sha12><ext>``, its receipt records the
full download, and it loads with ``load_version`` under a stable key, so a changed version replaces the one
loaded before and an unchanged one is not loaded again. Network work runs outside the pipeline lock, database
writes inside it. NCES and IMLS change their columns from year to year, so their rows keep key columns in
snake_case beside ``record_json``, every provider column under the provider's own name (the FEMA pattern);
the FDIC rows do the same; the topoView, IRS and USGS samples tables carry every column directly.

``banks``: FDIC BankFind Suite (https://api.fdic.gov/banks, no key; terms
https://www.fdic.gov/about/website-policies). Five endpoints, each kept as sorted canonical JSON Lines
(records in ID order) under its own key: ``institutions`` (STALP:KS, 803 on 2026-11-03, inactive banks and
their founding dates back to the 1850s), ``locations`` (STALP:KS, 1,343 offices), ``history``
(institution or office in Kansas before or after the change, 10,111 structure changes), ``failures``
(PSTALP:KS, 124 since 1935) and ``summary`` (STNAME:"Kansas", 134 annual aggregates from 1934). A request
returns at most 10,000 records and the ID field cannot sort, so ``history`` is fetched in four EFFDATE
ranges whose totals must add up (``FDIC_PARTS_MISMATCH``). Each run probes every endpoint (``limit=1``) for
its index name and total; an endpoint is extracted again when its index name or total changed, at most
every 6 days and at least every 28. A pull that differs only in ``RUNDATE`` (``volatile``) has the same
``content_sha256`` as the loaded version and is not kept again. Key columns carry ISO dates (``established``,
``ended``, ``effective``, ``failed``); FDIC writes unknown dates as 01/01/1800 and 12/31/9999 means "not
ended" (``ended`` NULL).

``exempt-orgs``: IRS Exempt Organizations Business Master File, Kansas extract ``eo_ks.csv``
(https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf, public
record; 18,568 organizations). Fetched every 7 days (``recheck_days``); the Kansas rows (STATE = KS) are kept
as CSV under key ``eo_ks``, and an unchanged file is not kept again. ``kfm_irs_eo_bmf`` has every column.

``museums-libraries``: IMLS public-use files (https://www.imls.gov/research-evaluation/data-collection;
terms https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls). The Museum Data Files
2018 release (the newest), three files, Kansas rows by address, physical or geocoded state (503 museums), keys
``mudf/<member stem>``; the Public Libraries Survey FY1992 onward, each year's zip (``PLS_FILES``) giving
the administrative-entity, outlet and state-summary members (STABR = KS; about 325, 380 and 1 rows a year),
keys ``pls/<FY>/ae``, ``pls/<FY>/outlet``, ``pls/<FY>/state``. A zip is downloaded again every 91 days (the
museum file every 182) or when its URL changes; at most 10 zips a run. A member in a changed format stops
that file with ``IMLS_COLUMNS_CHANGED`` or ``IMLS_KANSAS_EMPTY``; the other files continue and the run then
fails with every reason. A new fiscal year is added to ``PLS_FILES`` by hand (IMLS names each zip
differently).

``schools``: NCES public-use files (public domain; terms https://nces.ed.gov/ccd/files.asp). CCD school
directory files 2014-15 on, found through the CCD file API (``/ccd/datatables/api/File/0/0/0/11/0/0``,
read every 7 days), keys ``ccd/<school year>``; EDGE public-school geocodes 2015-16 on, read from each zip's
``.dbf`` (in a folder or a nested zip; field names carry year suffixes such as LAT1516), keys ``edge/<school
year>``; IPEDS directory files IC1980 … FA2001HD, then HD2002 to the current year, keys ``ipeds/<file>``;
PSS private-school files 1989-90 on (``PSS_FILES``), keys ``pss/<school year>``. A file is due when new, when
its URL changes, or every 91 days; a 404 (EDGE's next year, the next HD file) is recorded ``missing`` and
retried weekly; at most 10 files or 300 MB a run. Founding years exist only in IC1980 (ESTMOYR) and IC1984-86
(ESTYR/ESTMO) and are kept in ``established``. The PSS state column changed names over the years; a PSS file
with no state column is cut by its state FIPS column instead (the original feed stopped on 1991-92 with
``NCES_COLUMNS_CHANGED``; whether its later fix matched this is unknown).

``historical-topo-maps``: the USGS Historical Topographic Map Collection inventory ``historicaltopo.zip``
on The National Map's bucket (https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/Metadata/, public domain;
https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits). One bucket listing
request a run; the 17 MB zip is fetched when its ETag changed and the last pull is at least 28 days old. The
maps whose bbox overlaps the Kansas box (lon -102.06..-94.58, lat 36.99..40.01; 3,613 of 186,060) are kept as
CSV under key ``htmc`` with every column, plus ``geometry_geojson`` from the WKT and the bbox. Metadata only.

``usgs-samples``: USGS Samples Data (https://api.waterdata.usgs.gov/samples-data/, WQX 3.0
``fullphyschem`` profile; terms https://www.usgs.gov/data-management/data-licensing), the discrete
water-quality results the Water Quality Portal's legacy profile no longer carries after March 2024. One key
per month from 2024-01 (``results/YYYY-MM``), each pulled as four weekly requests (stateFips US:20) whose
rows are sorted and kept as one CSV. Months of the current and previous year are pulled again every 7 days,
older months every 91; at most ``max_months`` a run (48 requests, well under USGS's 1,000 an hour), and a
429 or 403 stops the run with ``USGS_RATE_LIMITED``, keeping what loaded. A month with no results is marked
checked and keeps no file; a loaded month that comes back empty stops with ``USGS_SAMPLES_MONTH_EMPTIED``.
"""
from __future__ import annotations

import calendar
import csv
from datetime import date
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.parse
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, csv_bytes, keep_version, loaded_keys, read_csv, save_state
from tools.local_data.sql_feeds import FeedError

KANSAS_BOX = (-102.06, 36.99, -94.58, 40.01)   # west, south, east, north


# --- Shared ----------------------------------------------------------------------------------------

def _ddl(table: str, columns: str, indexes=(), without_rowid: bool = False) -> str:
    """The table exactly as the database holds it: quoted columns ("name:TYPE" tokens, TEXT by default)
    after file_id and row_number, plus its indexes (table_col1_col2)."""
    body = ", ".join(f'"{n}" {(t or "TEXT").replace("TEXT_NOT_NULL", "TEXT NOT NULL")}'
                     for n, _, t in (c.partition(":") for c in columns.split()))
    out = (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
           f"PRIMARY KEY(file_id, row_number)){' WITHOUT ROWID' if without_rowid else ''};\n")
    for cols in indexes:
        out += f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(cols)} ON {table}({', '.join(chr(34) + c + chr(34) for c in cols)});\n"
    return out


def _columns(spec: str) -> list[str]:
    return [c.partition(":")[0] for c in spec.split()]


def _real(value):
    """A provider's number as REAL; an empty, absent or non-numeric value as NULL."""
    if value is None:
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def _int(value):
    if value is None or value == "":
        return None
    try:
        return int(value) if not isinstance(value, float) else int(value)
    except (TypeError, ValueError):
        return int(float(value))


def _text(value):
    return None if value is None else str(value)


def _decode(data: bytes) -> tuple[str, str]:
    """A provider's text as str and the encoding that read it: UTF-8, else Windows-1252."""
    try:
        return data.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return data.decode("cp1252"), "cp1252"


def _delimited(text: str) -> list[list[str]]:
    """The rows of a comma, tab or pipe delimited text file (the first line decides)."""
    first = text.split("\n", 1)[0]
    delimiter = "\t" if "\t" in first else "|" if "|" in first and "," not in first else ","
    rows = list(csv.reader(io.StringIO(text.lstrip("﻿"), newline=""), delimiter=delimiter))
    return [r for r in rows if r]


def _zip_members(path: Path) -> list[str]:
    try:
        with zipfile.ZipFile(path) as z:
            return [n for n in z.namelist() if not n.endswith("/") and "__MACOSX/" not in n]
    except zipfile.BadZipFile:
        raise FeedError(f"ZIP_UNREADABLE {path.name}") from None


class Picker:
    """Key columns of a provider row by the first alias present. Names are matched without case, and
    a trailing two- or four-digit year suffix (LAT1516, CNTY15) is ignored when nothing matches directly."""

    def __init__(self, header: list[str]):
        self.exact = {h.upper(): i for i, h in enumerate(header)}
        self.loose = {}
        for h, i in self.exact.items():
            self.loose.setdefault(re.sub(r"(\d{4}|\d{2})$", "", h), i)

    def index(self, aliases) -> int | None:
        for alias in aliases:
            if alias in self.exact:
                return self.exact[alias]
        for alias in aliases:
            if alias in self.loose:
                return self.loose[alias]
        return None

    def has(self, aliases) -> bool:
        return self.index(aliases) is not None

    def value(self, row, aliases):
        i = self.index(aliases)
        return None if i is None or i >= len(row) else row[i].strip()


def _dbf(data: bytes) -> tuple[list[str], list[list[str]], str]:
    """The field names and records (text, stripped; deleted records left out) of a dBase file."""
    if len(data) < 32:
        raise FeedError("DBF_UNREADABLE")
    count = int.from_bytes(data[4:8], "little")
    header_len, record_len = int.from_bytes(data[8:10], "little"), int.from_bytes(data[10:12], "little")
    fields, pos = [], 32
    while pos + 32 <= header_len and data[pos] != 0x0D:
        name = data[pos:pos + 11].split(b"\0")[0].decode("ascii", "replace")
        fields.append((name, data[pos + 16]))
        pos += 32
    if not fields or header_len + count * record_len > len(data) + 1:
        raise FeedError("DBF_UNREADABLE")
    body = data[header_len:]
    try:
        body.decode("utf-8")
        encoding = "utf-8"
    except UnicodeDecodeError:
        encoding = "cp1252"
    rows = []
    for n in range(count):
        record = body[n * record_len:(n + 1) * record_len]
        if record[:1] == b"*":
            continue
        values, at = [], 1
        for _, length in fields:
            values.append(record[at:at + length].decode(encoding).strip())
            at += length
        rows.append(values)
    return [f for f, _ in fields], rows, encoding


def _record_json(header, row) -> str:
    return core.canonical(dict(zip(header, row)))


def _kept_rows(path: Path, encoding: str):
    """(header, row) pairs of a kept Kansas CSV whose header is the provider's."""
    with gzip.open(path, "rt", encoding=encoding, newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        if not header:
            raise FeedError(f"KEPT_FILE_EMPTY {path.name}")
        for row in reader:
            if len(row) != len(header):
                raise FeedError(f"KEPT_ROW_SHAPE {path.name}")
            yield header, row


def _receipt_extra(db, source_id: str, key: str, field: str):
    """A field of the receipt of key's loaded version, or None."""
    row = db.execute("SELECT json_extract(receipt_json, ?) FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                     "AND json_extract(receipt_json,'$.key')=? ORDER BY file_id DESC LIMIT 1", (f"$.{field}", source_id, key)).fetchone()
    return row[0] if row else None


# --- Banks: FDIC BankFind, five endpoints --------------------------------------------------------------

FDIC_API = "https://api.fdic.gov/banks/"
FDIC_TERMS = "https://www.fdic.gov/about/website-policies"
FDIC_LIMIT = 10000                   # the API's maximum records per request
FDIC_VOLATILE = ["RUNDATE"]
FDIC_MIN_DAYS, FDIC_MAX_DAYS = 6, 28
FDIC_FILTERS = {
    "institutions": "STALP:KS",
    "locations": "STALP:KS",
    "history": "(PSTALP:KS OR OFF_PSTALP:KS OR FRM_PSTALP:KS OR FRM_OFF_PSTALP:KS)",
    "failures": "PSTALP:KS",
    "summary": 'STNAME:"Kansas"',
}
FDIC_PARTS = {"history": ["EFFDATE:[* TO 1979-12-31]", "EFFDATE:[1980-01-01 TO 1999-12-31]",
                          "EFFDATE:[2000-01-01 TO 2009-12-31]", "EFFDATE:[2010-01-01 TO *]"]}
FDIC_TABLES = {"institutions": "kfm_fdic_institutions", "locations": "kfm_fdic_locations", "history": "kfm_fdic_history",
               "failures": "kfm_fdic_failures", "summary": "kfm_fdic_summary"}
FDIC_COLUMNS = {
    "institutions": ("cert:INTEGER name city county stcnty active:INTEGER estymd endefymd insdate changec1 bkclass chrtagnt regagnt "
                     "fed_rssd latitude:REAL longitude:REAL established ended record_json:TEXT_NOT_NULL"),
    "locations": ("uninum:INTEGER cert:INTEGER offname offnum:INTEGER mainoff:INTEGER name address city county stcnty zip servtype_desc "
                  "estymd acqdate latitude:REAL longitude:REAL established record_json:TEXT_NOT_NULL"),
    "history": ("id cert:INTEGER instname changecode:INTEGER changecode_desc effdate procdate uninum:INTEGER off_name pcity cntyname "
                "pstalp off_pcity off_cntyname off_pstalp frm_pstalp frm_off_pstalp acq_uninum:INTEGER out_uninum:INTEGER effective "
                "record_json:TEXT_NOT_NULL"),
    "failures": ("cert:INTEGER name city pstalp faildate failyr restype restype1 savr cost:REAL qbfasset:REAL qbfdep:REAL bidname "
                 "bidcity failed record_json:TEXT_NOT_NULL"),
    "summary": "id year:INTEGER cb_si banks:INTEGER record_json:TEXT_NOT_NULL",
}
FDIC_INDEXES = {"institutions": [("cert",), ("name",), ("stcnty",)], "locations": [("cert",), ("stcnty",)],
                "history": [("cert", "effective"), ("changecode",), ("uninum",)], "failures": [("cert",)], "summary": [("year",)]}
FDIC_DDL = "".join(_ddl(FDIC_TABLES[ep], FDIC_COLUMNS[ep], FDIC_INDEXES[ep]) for ep in FDIC_TABLES)


def _iso_date(value) -> str | None:
    """FDIC's M/D/YYYY or YYYY-MM-DDT00:00:00 as YYYY-MM-DD; 12/31/9999 (not ended) and blanks as NULL."""
    if not value:
        return None
    value = str(value)
    found = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", value)
    if found:
        month, day, year = found.groups()
        return None if year == "9999" else f"{year}-{int(month):02d}-{int(day):02d}"
    if re.match(r"\d{4}-\d{2}-\d{2}", value):
        return value[:10]
    return None


def _fdic_values(endpoint: str, record: dict) -> tuple:
    g = record.get
    if endpoint == "institutions":
        return (_int(g("CERT")), _text(g("NAME")), _text(g("CITY")), _text(g("COUNTY")), _text(g("STCNTY")), _int(g("ACTIVE")),
                _text(g("ESTYMD")), _text(g("ENDEFYMD")), _text(g("INSDATE")), _text(g("CHANGEC1")), _text(g("BKCLASS")),
                _text(g("CHRTAGNT")), _text(g("REGAGNT")), _text(g("FED_RSSD")), _real(g("LATITUDE")), _real(g("LONGITUDE")),
                _iso_date(g("ESTYMD")), _iso_date(g("ENDEFYMD")))
    if endpoint == "locations":
        return (_int(g("UNINUM")), _int(g("CERT")), _text(g("OFFNAME")), _int(g("OFFNUM")), _int(g("MAINOFF")), _text(g("NAME")),
                _text(g("ADDRESS")), _text(g("CITY")), _text(g("COUNTY")), _text(g("STCNTY")), _text(g("ZIP")), _text(g("SERVTYPE_DESC")),
                _text(g("ESTYMD")), _text(g("ACQDATE")), _real(g("LATITUDE")), _real(g("LONGITUDE")), _iso_date(g("ESTYMD")))
    if endpoint == "history":
        return (_text(g("ID")), _int(g("CERT")), _text(g("INSTNAME")), _int(g("CHANGECODE")), _text(g("CHANGECODE_DESC")), _text(g("EFFDATE")),
                _text(g("PROCDATE")), _int(g("UNINUM")), _text(g("OFF_NAME")), _text(g("PCITY")), _text(g("CNTYNAME")), _text(g("PSTALP")),
                _text(g("OFF_PCITY")), _text(g("OFF_CNTYNAME")), _text(g("OFF_PSTALP")), _text(g("FRM_PSTALP")), _text(g("FRM_OFF_PSTALP")),
                _int(g("ACQ_UNINUM")), _int(g("OUT_UNINUM")), _iso_date(g("EFFDATE")))
    if endpoint == "failures":
        return (_int(g("CERT")), _text(g("NAME")), _text(g("CITY")), _text(g("PSTALP")), _text(g("FAILDATE")), _text(g("FAILYR")),
                _text(g("RESTYPE")), _text(g("RESTYPE1")), _text(g("SAVR")), _real(g("COST")), _real(g("QBFASSET")), _real(g("QBFDEP")),
                _text(g("BIDNAME")), _text(g("BIDCITY")), _iso_date(g("FAILDATE")))
    return (_text(g("ID")), _int(g("YEAR")), _text(g("CB_SI")), _int(g("BANKS")))


def _fdic_rows(path: Path, endpoint: str):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            yield (*_fdic_values(endpoint, record), core.canonical(record))


def _fdic_url(endpoint: str, filters: str, limit: int) -> str:
    return FDIC_API + endpoint + "?" + urllib.parse.urlencode({"filters": filters, "limit": limit, "offset": 0, "format": "json"})


def _fdic_answer(ctx, url: str) -> tuple[dict, list, int]:
    """(meta, records, bytes) of one BankFind answer."""
    fetched = ctx.fetch(url, limit=256_000_000, timeout=600)
    try:
        payload = json.loads(fetched.body)
        meta, data = payload["meta"], payload["data"]
        records = [item["data"] for item in data]
        if not isinstance(meta["total"], int) or not all(isinstance(r, dict) for r in records):
            raise TypeError
        index = meta["index"]["name"]
    except (ValueError, KeyError, TypeError):
        raise FeedError(f"FDIC_RESPONSE_SHAPE {url}") from None
    if not isinstance(index, str):
        raise FeedError(f"FDIC_RESPONSE_SHAPE {url}")
    return meta, records, len(fetched.body)


def _fdic_content(records) -> str:
    """SHA-256 of the JSON Lines without the volatile fields: a pull that differs only in RUNDATE is the same."""
    body = "".join(core.canonical({k: v for k, v in r.items() if k not in FDIC_VOLATILE}) + "\n" for r in records)
    return hashlib.sha256(body.encode()).hexdigest()


def banks(ctx, min_days: int = FDIC_MIN_DAYS, max_days: int = FDIC_MAX_DAYS) -> dict:
    """Kansas banks, offices, structure history, failures and annual summaries from FDIC BankFind."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(FDIC_DDL)
        state, today, summary = core.get_state(db, "banks"), ctx.now().date(), {"rows": 0}
        for endpoint, filters in FDIC_FILTERS.items():
            current = state.get(endpoint, {})
            age = age_days(current, "fetched", today)
            if age is not None and age < min_days:
                summary[endpoint] = "not_due"
                continue
            meta, _, _ = _fdic_answer(ctx, _fdic_url(endpoint, filters, 1))
            mark = {"index": meta["index"]["name"], "records": meta["total"]}
            if age is not None and age < max_days and {k: current.get(k) for k in mark} == mark:
                summary[endpoint] = "unchanged"
                continue
            parts = FDIC_PARTS.get(endpoint, [""])
            records, urls, downloaded, totals = [], [], 0, 0
            for part in parts:
                url = _fdic_url(endpoint, f"{filters} AND {part}" if part else filters, FDIC_LIMIT)
                part_meta, part_records, size = _fdic_answer(ctx, url)
                if part_meta["total"] > FDIC_LIMIT or len(part_records) != part_meta["total"]:
                    raise FeedError(f"FDIC_PART_TOO_LARGE {endpoint} {part or filters}")
                records.extend(part_records)
                urls.append(url)
                downloaded += size
                totals += part_meta["total"]
            if totals != mark["records"]:
                raise FeedError(f"FDIC_PARTS_MISMATCH {endpoint} {totals} of {mark['records']}")
            if not records:
                raise FeedError(f"FDIC_KANSAS_EMPTY {endpoint}")
            if any(not isinstance(r.get("ID"), str) for r in records) or len({r["ID"] for r in records}) != len(records):
                raise FeedError(f"FDIC_RECORD_IDS {endpoint}")
            records.sort(key=lambda r: r["ID"])
            content = _fdic_content(records)
            if content == _receipt_extra(db, f"fdic-{endpoint}", endpoint, "content_sha256"):
                summary[endpoint] = "unchanged"
            else:
                result = keep_version(ctx, db, feed="banks", source_id=f"fdic-{endpoint}", key=endpoint, name=f"{endpoint}/{endpoint}-KS",
                                      ext=".jsonl.gz", body=core.gz("".join(core.canonical(r) + "\n" for r in records).encode()), url=urls[0],
                                      extra={"content_sha256": content, "downloaded_bytes": downloaded, "endpoint": endpoint, "filter": filters,
                                             "index": mark["index"], "parts": parts, "records": len(records), "terms": FDIC_TERMS, "urls": urls,
                                             "volatile": FDIC_VOLATILE},
                                      table=FDIC_TABLES[endpoint], width=len(_columns(FDIC_COLUMNS[endpoint])),
                                      rows=lambda path, ep=endpoint: _fdic_rows(path, ep))
                summary[endpoint] = result["state"]
                summary["rows"] += result["rows"]
            state = save_state(ctx, db, "banks", {**state, endpoint: {**mark, "fetched": str(today)}})
        return summary
    finally:
        db.close()


# --- Exempt organizations: the IRS EO BMF Kansas file ----------------------------------------------------

EO_URL = "https://www.irs.gov/pub/irs-soi/eo_ks.csv"
EO_TERMS = "https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf"
EO_HEADER = ["EIN", "NAME", "ICO", "STREET", "CITY", "STATE", "ZIP", "GROUP", "SUBSECTION", "AFFILIATION", "CLASSIFICATION", "RULING",
             "DEDUCTIBILITY", "FOUNDATION", "ACTIVITY", "ORGANIZATION", "STATUS", "TAX_PERIOD", "ASSET_CD", "INCOME_CD", "FILING_REQ_CD",
             "PF_FILING_REQ_CD", "ACCT_PD", "ASSET_AMT", "INCOME_AMT", "REVENUE_AMT", "NTEE_CD", "SORT_NAME"]
EO_TABLE = "kfm_irs_eo_bmf"
EO_DDL = _ddl(EO_TABLE, " ".join(h.lower() for h in EO_HEADER), [("city",), ("ein",), ("name",), ("ntee_cd",)])
EO_RECHECK_DAYS = 7


def exempt_orgs(ctx, recheck_days: int = EO_RECHECK_DAYS) -> dict:
    """Kansas exempt organizations from the IRS Business Master File extract."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(EO_DDL)
        state, today = core.get_state(db, "exempt-orgs"), ctx.now().date()
        age = age_days(state, "fetched", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "fetched": state["fetched"]}
        fetched = ctx.fetch(EO_URL, limit=256_000_000, timeout=600)
        text, encoding = _decode(fetched.body)
        rows = _delimited(text)
        if not rows or rows[0] != EO_HEADER:
            raise FeedError("IRS_EO_COLUMNS_CHANGED")
        if any(len(r) != len(EO_HEADER) for r in rows[1:]):
            raise FeedError("IRS_EO_ROW_SHAPE")
        kansas = [r for r in rows[1:] if r[5] == "KS"]
        if not kansas:
            raise FeedError("IRS_EO_KANSAS_EMPTY")
        result = keep_version(ctx, db, feed="exempt-orgs", source_id="irs-eo-bmf", key="eo_ks", name="eo_ks/eo_ks", ext=".csv.gz",
                              body=core.gz(csv_bytes([EO_HEADER, *kansas], encoding)), url=fetched.url, fetched=fetched, original=fetched.body,
                              extra={"encoding": encoding, "kansas": len(kansas), "records": len(rows) - 1, "terms": EO_TERMS},
                              table=EO_TABLE, width=len(EO_HEADER), rows=lambda path: read_csv(path, EO_HEADER, "IRS_EO", encoding))
        save_state(ctx, db, "exempt-orgs", {"fetched": str(today), "last_modified": fetched.last_modified, "records": len(kansas)})
        return {**result, "records": len(kansas)}
    finally:
        db.close()


# --- Museums and libraries: IMLS public-use files -----------------------------------------------------------

IMLS_TERMS = "https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls"
IMLS_FILES = "https://www.imls.gov/sites/default/files/"
MUDF_URL = IMLS_FILES + "2018_csv_museum_data_files.zip"
MUDF_RELEASE = "2018"
PLS_FILES = {
    1992: "pupld92a_csv.zip", 1993: "pupld93a_csv.zip", 1994: "pupld94a_csv.zip", 1995: "pupld95a_csv.zip", 1996: "pupld96a_csv.zip",
    1997: "pupld97a_csv.zip", 1998: "pupldf98_csv.zip", 1999: "pupldf99_csv.zip", 2000: "pupldf00_csv.zip", 2001: "pupld01b_csv.zip",
    2002: "pupld02b_csv.zip", 2003: "pupld03a_csv.zip", 2004: "pupld04a_csv.zip", 2005: "pupld05a_csv.zip", 2006: "pupld06a_csv.zip",
    2007: "pupld07a_csv.zip", 2008: "pupld08a_csv.zip", 2009: "pupld09a_csv.zip", 2010: "pupld10a_csv.zip", 2011: "pupld11b_csv.zip",
    2012: "pupld12a_csv.zip", 2013: "pupld13a_csv.zip", 2014: "pls_fy2014_data_files_csv.zip", 2015: "pls_fy2015_data_files_csv.zip",
    2016: "pls_fy2016_data_files_csv.zip", 2017: "pls_fy2017_data_files_csv.zip", 2018: "pls_fy2018_data_files_csv.zip",
    2019: "2021-05/pls_fy2019_csv.zip", 2020: "2022-07/pls_fy2020_csv.zip", 2021: "2023-06/pls_fy2021_csv.zip",
    2022: "2024-06/pls_fy2022_csv.zip", 2023: "2025-08/pls_fy2023_csv.zip", 2024: "2026-06/pls_fy2024_csv.zip",
}
PLS_MEMBERS = {"ae": re.compile(r"(^|/)(pupld|pls_fy\d+_ae_)", re.I), "outlet": re.compile(r"(^|/)(puout|pls_fy\d+_outlet_)", re.I),
               "state": re.compile(r"(^|/)(pusum|pls_fy\d+_state_|pls_state_)", re.I)}
IMLS_RECHECK_DAYS, MUDF_RECHECK_DAYS, IMLS_MAX_ZIPS = 91, 182, 10
IMLS_ZIP_LIMIT = 256_000_000
MUSEUM_TABLE, PLS_TABLES = "kfm_imls_museums", {"ae": "kfm_imls_pls_libraries", "outlet": "kfm_imls_pls_outlets", "state": "kfm_imls_pls_state"}
MUSEUM_COLUMNS = ("data_file mid discipline common_name legal_name ein address_state physical_state geocoded_state state_fips county_fips city "
                  "latitude:REAL longitude:REAL ipeds record_json:TEXT_NOT_NULL")
PLS_COLUMNS = {
    "ae": "fiscal_year fscskey libid name address city zip county state population central_libraries branches bookmobiles record_json:TEXT_NOT_NULL",
    "outlet": ("fiscal_year fscskey fscs_seq libid name address city zip county state outlet_type square_feet latitude:REAL longitude:REAL "
               "record_json:TEXT_NOT_NULL"),
    "state": "fiscal_year state record_json:TEXT_NOT_NULL",
}
IMLS_DDL = (_ddl(MUSEUM_TABLE, MUSEUM_COLUMNS, [("common_name",), ("county_fips",), ("mid",)])
            + _ddl(PLS_TABLES["ae"], PLS_COLUMNS["ae"], [("fscskey",), ("name",)])
            + _ddl(PLS_TABLES["outlet"], PLS_COLUMNS["outlet"], [("fscskey", "fscs_seq"), ("name",)])
            + _ddl(PLS_TABLES["state"], PLS_COLUMNS["state"], [("state",)]))
MUSEUM_ALIASES = {"mid": ["MID"], "discipline": ["DISCIPLINE", "DISCIPL"], "common_name": ["COMMONNAME"], "legal_name": ["LEGALNAME"],
                  "ein": ["EIN"], "address_state": ["ADSTATE"], "physical_state": ["PHSTATE"], "geocoded_state": ["GSTATE"],
                  "state_fips": ["FIPSST"], "county_fips": ["FIPSCO"], "city": ["GCITY"], "latitude": ["LATITUDE"], "longitude": ["LONGITUDE"],
                  "ipeds": ["IPEDS"]}
PLS_ALIASES = {
    "ae": {"fscskey": ["FSCSKEY"], "libid": ["LIBID"], "name": ["LIBNAME"], "address": ["ADDRESS"], "city": ["CITY"], "zip": ["ZIP", "ZIP1"],
           "county": ["CNTY"], "state": ["STABR"], "population": ["POPU_LSA", "POPU"], "central_libraries": ["CENTLIB"], "branches": ["BRANLIB"],
           "bookmobiles": ["BKMOB"]},
    "outlet": {"fscskey": ["FSCSKEY"], "fscs_seq": ["FSCS_SEQ", "K_SEQ"], "libid": ["LIBID", "LIB_CODE"], "name": ["LIBNAME", "LIB_NAME"],
               "address": ["ADDRESS", "LIB_ADDR"], "city": ["CITY", "LIB_CITY"], "zip": ["ZIP", "LIB_ZIP"], "county": ["CNTY", "LIB_CNTY"],
               "state": ["STABR"], "outlet_type": ["C_OUT_TY", "C_OUT_TYP"], "square_feet": ["SQ_FEET"], "latitude": ["LATITUDE"],
               "longitude": ["LONGITUD"]},
    "state": {"state": ["STABR"]},
}
PLS_REAL = {"latitude", "longitude"}


def _imls_due(state: dict, key: str, url: str, today: date, recheck: int) -> bool:
    current = state["files"].get(key)
    if not current or current.get("url") != url:
        return True
    age = age_days(current, "checked", today)
    return age is None or age >= recheck


def _museum_rows(path: Path, encoding: str, data_file: str):
    for header, row in _kept_rows(path, encoding):
        pick = Picker(header)
        values = [data_file]
        for column in _columns(MUSEUM_COLUMNS)[1:-1]:
            value = pick.value(row, MUSEUM_ALIASES[column])
            values.append(_real(value) if column in PLS_REAL else value)
        yield (*values, _record_json(header, row))


def _pls_rows(path: Path, encoding: str, kind: str, fiscal_year: str):
    for header, row in _kept_rows(path, encoding):
        pick = Picker(header)
        values = [fiscal_year]
        for column in _columns(PLS_COLUMNS[kind])[1:-1]:
            value = pick.value(row, PLS_ALIASES[kind][column])
            values.append(_real(value) if column in PLS_REAL else value)
        yield (*values, _record_json(header, row))


def _imls_member(z, name: str, is_kansas, code: str) -> tuple[list, list, str]:
    """(header, Kansas rows, encoding) of one CSV member, with the whole member read once."""
    text, encoding = _decode(z.read(name))
    rows = _delimited(text)
    if len(rows) < 2 or len(set(rows[0])) != len(rows[0]):
        raise FeedError(f"{code}_COLUMNS_CHANGED {name}")
    header, pick = rows[0], Picker(rows[0])
    body = [r for r in rows[1:] if len(r) == len(header)]
    if len(body) != len(rows) - 1:
        raise FeedError(f"{code}_ROW_SHAPE {name}")
    try:
        kansas = [r for r in body if is_kansas(pick, r)]
    except KeyError as missing:
        raise FeedError(f"{code}_COLUMNS_CHANGED {name} {missing.args[0]}") from None
    if not kansas:
        raise FeedError(f"{code}_KANSAS_EMPTY {name}")
    return header, kansas, encoding


def _state_is(pick: Picker, row, aliases, state: str = "KS") -> bool:
    if not pick.has(aliases):
        raise KeyError(aliases[0].lower())
    return pick.value(row, aliases) == state


def _museum_is_kansas(pick: Picker, row) -> bool:
    return any(pick.value(row, [a]) == "KS" for a in ("ADSTATE", "PHSTATE", "GSTATE") if pick.has([a]))


def _imls_zip(ctx, db, key: str, url: str, summary: dict) -> None:
    archive = core.temp_path(ctx, "imls-" + key.replace("/", "-") + ".zip")
    try:
        fetched = core.download(ctx, url, archive, limit=IMLS_ZIP_LIMIT, timeout=1800)
        zip_sha256 = core.file_sha256(archive)
        members = _zip_members(archive)
        with zipfile.ZipFile(archive) as z:
            if key == "mudf":
                chosen = [m for m in members if m.lower().endswith(".csv") and "_nulls" in m.lower()] or [m for m in members if m.lower().endswith(".csv")]
                if not chosen:
                    raise FeedError(f"IMLS_MEMBER_MISSING {key}")
                for member in sorted(chosen):
                    stem = Path(member).stem
                    header, kansas, encoding = _imls_member(z, member, _museum_is_kansas, "IMLS")
                    result = keep_version(ctx, db, feed="museums-libraries", source_id="imls-museum-data-files", key=f"mudf/{stem}",
                                          name=f"mudf/{stem}", ext=".csv.gz", body=core.gz(csv_bytes([header, *kansas], encoding)), url=fetched.url,
                                          fetched=fetched, original=archive,
                                          extra={"encoding": encoding, "release": MUDF_RELEASE, "rows": len(kansas), "terms": IMLS_TERMS,
                                                 "zip_sha256": zip_sha256},
                                          table=MUSEUM_TABLE, width=len(_columns(MUSEUM_COLUMNS)),
                                          rows=lambda path, enc=encoding, s=stem: _museum_rows(path, enc, s))
                    summary["files"][f"mudf/{stem}"] = result["state"]
                    summary["rows"] += result["rows"]
                return
            fiscal_year = key.split("/")[1]
            for kind, pattern in PLS_MEMBERS.items():
                chosen = [m for m in members if m.lower().endswith(".csv") and pattern.search(m)]
                if kind == "state" and not chosen:
                    continue            # IMLS stopped publishing the state file after FY2020
                if len(chosen) != 1:
                    raise FeedError(f"IMLS_MEMBER_MISSING {key}/{kind}")
                member = chosen[0]
                header, kansas, encoding = _imls_member(z, member, lambda p, r: _state_is(p, r, ["STABR"]), "IMLS")
                result = keep_version(ctx, db, feed="museums-libraries", source_id=f"imls-pls-{'libraries' if kind == 'ae' else kind + 's' if kind == 'outlet' else 'state'}",
                                      key=f"{key}/{kind}", name=f"{key}/{kind}", ext=".csv.gz", body=core.gz(csv_bytes([header, *kansas], encoding)),
                                      url=fetched.url, fetched=fetched, original=archive,
                                      extra={"encoding": encoding, "member": member, "rows": len(kansas), "terms": IMLS_TERMS, "zip_sha256": zip_sha256},
                                      table=PLS_TABLES[kind], width=len(_columns(PLS_COLUMNS[kind])),
                                      rows=lambda path, enc=encoding, k=kind, fy=fiscal_year: _pls_rows(path, enc, k, fy))
                summary["files"][f"{key}/{kind}"] = result["state"]
                summary["rows"] += result["rows"]
    finally:
        archive.unlink(missing_ok=True)


def museums_libraries(ctx, max_zips: int = IMLS_MAX_ZIPS, recheck_days: int = IMLS_RECHECK_DAYS, mudf_recheck_days: int = MUDF_RECHECK_DAYS) -> dict:
    """Kansas museums (IMLS Museum Data Files) and public libraries, outlets and state summaries (IMLS PLS)."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(IMLS_DDL)
        state, today = core.get_state(db, "museums-libraries"), ctx.now().date()
        state = {**state, "files": dict(state.get("files", {}))}
        targets = [("mudf", MUDF_URL, mudf_recheck_days)] + [(f"pls/{fy}", IMLS_FILES + name, recheck_days) for fy, name in sorted(PLS_FILES.items())]
        due = [(k, u) for k, u, r in targets if _imls_due(state, k, u, today, r)]
        summary, failures = {"files": {}, "rows": 0, "due": len(due), "zips": 0}, []
        for key, url in due[:max_zips]:
            try:
                _imls_zip(ctx, db, key, url, summary)
            except FeedError as error:
                if not str(error).startswith(("IMLS_COLUMNS_CHANGED", "IMLS_KANSAS_EMPTY", "IMLS_MEMBER_MISSING", "IMLS_ROW_SHAPE")):
                    raise
                failures.append(f"{key} {error}")
                continue
            summary["zips"] += 1
            state = save_state(ctx, db, "museums-libraries", {**state, "files": {**state["files"], key: {"checked": str(today), "url": url}}})
        if failures:
            raise FeedError("; ".join(failures))
        return {**summary, "pending": max(0, len(due) - max_zips)}
    finally:
        db.close()


# --- Schools: NCES CCD, EDGE, IPEDS and PSS ------------------------------------------------------------------

NCES = "https://nces.ed.gov/"
NCES_TERMS = "https://nces.ed.gov/ccd/files.asp"
NCES_LICENSE = "public domain (U.S. Government work, public-use file)"
CCD_API = NCES + "ccd/datatables/api/File/0/0/0/11/0/0"     # file 11: Public Elementary/Secondary School Universe Survey Data
CCD_FILE = re.compile(r"ccd_sch_029_(\d{2})(\d{2})_w_.*\.zip$", re.I)
EDGE_URL = NCES + "programs/edge/data/EDGE_GEOCODE_PUBLICSCH_{yy}{yy2}.zip"
EDGE_FIRST = 2015
IPEDS_URL = NCES + "ipeds/datacenter/data/{name}.zip"
IPEDS_FILES = ["IC1980", "IC1984", "IC1985", "IC1986_A", "IC1987_A", "IC1988_A", "IC1989_A", "IC90HD", "IC1991_hdr", "IC1992_A", "IC1993_A",
               "IC1994_A", "ic9596_A", "ic9697_A", "ic9798_HDR", "IC98hdac", "IC99_HD", "FA2000HD", "FA2001HD"]
IPEDS_HD_FIRST = 2002
PSS_URL = NCES + "surveys/pss/zip/TXT_PSS{yy}{yy2}.zip"
PSS_FILES = [(y, y + 1) for y in range(1989, 2024, 2)]       # biennial surveys 1989-90 .. 2023-24
NCES_RECHECK_DAYS, NCES_MISSING_DAYS, NCES_LISTING_DAYS = 91, 7, 7
NCES_MAX_FILES, NCES_MAX_BYTES, NCES_ZIP_LIMIT = 10, 300_000_000, 256_000_000
CCD_TABLE, EDGE_TABLE, IPEDS_TABLE, PSS_TABLE = "kfm_nces_ccd_schools", "kfm_nces_edge_school_locations", "kfm_ipeds_institutions", "kfm_nces_pss_schools"
CCD_COLUMNS = ("school_year ncessch school_name lea_name leaid st_schid fipst city zip status updated_status effective_date school_type level "
               "lowest_grade highest_grade charter record_json:TEXT_NOT_NULL")
EDGE_COLUMNS = ("school_year ncessch leaid name street city state zip state_fips county_geoid county_name locale latitude:REAL longitude:REAL "
                "published_year record_json:TEXT_NOT_NULL")
IPEDS_COLUMNS = ("survey unitid name city state state_fips county sector control established established_month closed deleted_year opeid fice "
                 "latitude:REAL longitude:REAL record_json:TEXT_NOT_NULL")
PSS_COLUMNS = ("school_year ppin name city state location_state state_fips county zip latitude:REAL longitude:REAL religion orientation students "
               "record_json:TEXT_NOT_NULL")
NCES_DDL = (_ddl(CCD_TABLE, CCD_COLUMNS, [("leaid", "school_year"), ("ncessch",), ("school_name",)])
            + _ddl(EDGE_TABLE, EDGE_COLUMNS, [("county_geoid",), ("ncessch",)])
            + _ddl(IPEDS_TABLE, IPEDS_COLUMNS, [("name",), ("unitid",)])
            + _ddl(PSS_TABLE, PSS_COLUMNS, [("name",), ("ppin",)]))
CCD_ALIASES = {"ncessch": ["NCESSCH"], "school_name": ["SCH_NAME"], "lea_name": ["LEA_NAME"], "leaid": ["LEAID"], "st_schid": ["ST_SCHID"],
               "fipst": ["FIPST"], "city": ["LCITY"], "zip": ["LZIP"], "status": ["SY_STATUS_TEXT"], "updated_status": ["UPDATED_STATUS_TEXT"],
               "effective_date": ["EFFECTIVE_DATE"], "school_type": ["SCH_TYPE_TEXT"], "level": ["LEVEL"], "lowest_grade": ["GSLO"],
               "highest_grade": ["GSHI"], "charter": ["CHARTER_TEXT"]}
EDGE_ALIASES = {"ncessch": ["NCESSCH"], "leaid": ["LEAID"], "name": ["NAME"], "street": ["STREET", "LSTREE", "LSTREET"], "city": ["CITY", "LCITY"],
                "state": ["STATE", "LSTATE"], "zip": ["ZIP", "LZIP"], "state_fips": ["OPSTFIPS"], "county_geoid": ["CNTY"], "county_name": ["NMCNTY"],
                "locale": ["LOCALE"], "latitude": ["LAT"], "longitude": ["LON"], "published_year": ["SCHOOLYEAR", "SURVYEAR"]}
IPEDS_ALIASES = {"unitid": ["UNITID"], "name": ["INSTNM"], "city": ["CITY"], "state": ["STABBR"], "state_fips": ["FIPS"], "county": ["COUNTYNM", "CNTY"],
                 "sector": ["SECTOR"], "control": ["CONTROL"], "established": ["ESTYR", "ESTMOYR"], "established_month": ["ESTMO"],
                 "closed": ["CLOSEDAT"], "deleted_year": ["DEATHYR"], "opeid": ["OPEID"], "fice": ["FICE"], "latitude": ["LATITUDE"],
                 "longitude": ["LONGITUD"]}
PSS_ALIASES = {"ppin": ["PPIN", "EPIN"], "name": ["PINST", "SCHNAME", "SCHOOL_NAME"], "city": ["PCITY", "CITY"], "state": ["PSTABB", "STATE", "PSTATE", "PSTAB"],
               "location_state": ["PL_STABB"], "state_fips": ["PSTFIP", "ESTFIP", "STFIP"], "county": ["PCNTY"], "zip": ["PZIP", "EZIP"],
               "latitude": ["LATITUDE"], "longitude": ["LONGITUDE"], "religion": ["RELIG"], "orientation": ["ORIENT"], "students": ["NUMSTUDS"]}
NCES_REAL = {"latitude", "longitude"}


def _school_year(start: int) -> str:
    return f"{start}-{start + 1}"


def _ccd_listing(ctx) -> list[list[str]]:
    """[[school year, zip URL], ...] of the CCD school directory files, from the CCD file API."""
    body = ctx.fetch(CCD_API, limit=64_000_000).body
    try:
        groups = json.loads(body)["selectionGroupModels"]
        found = {}
        for group in groups:
            year = re.sub(r"\s*-\s*", "-", str(group["schoolYear"]))
            for title in group["titleGroups"]:
                for element in title["elementGroups"]:
                    for component in element["componentGroups"]:
                        if component["component"] != "Directory" or element["elementType"] != "Data File":
                            continue
                        for item in component["files"]:
                            url = urllib.parse.urljoin(NCES + "ccd/", item["fileURL"] or "")
                            if CCD_FILE.search(url) and not url.lower().endswith("_sas.zip"):
                                found.setdefault(year, url)
    except (ValueError, KeyError, TypeError, AttributeError):
        raise FeedError("CCD_LISTING_SHAPE") from None
    if not found:
        raise FeedError("CCD_LISTING_EMPTY")
    return [[year, found[year]] for year in sorted(found) if re.fullmatch(r"\d{4}-\d{4}", year)]


def _nces_targets(ctx, state: dict) -> list[tuple[str, str]]:
    year = ctx.now().date().year
    targets = [(f"ccd/{sy}", url) for sy, url in state["ccd_listing"]["files"]]
    targets += [(f"edge/{_school_year(y)}", EDGE_URL.format(yy=f"{y % 100:02d}", yy2=f"{(y + 1) % 100:02d}")) for y in range(EDGE_FIRST, year)]
    targets += [(f"ipeds/{name}", IPEDS_URL.format(name=name)) for name in IPEDS_FILES]
    targets += [(f"ipeds/HD{y}", IPEDS_URL.format(name=f"HD{y}")) for y in range(IPEDS_HD_FIRST, year + 1)]
    targets += [(f"pss/{_school_year(a)}", PSS_URL.format(yy=f"{a % 100:02d}", yy2=f"{b % 100:02d}")) for a, b in PSS_FILES if b < year]
    return targets


def _nces_due(state: dict, key: str, url: str, today: date) -> bool:
    current = state["files"].get(key)
    if not current or current.get("url") != url:
        return True
    age = age_days(current, "checked", today)
    return age is None or age >= (NCES_MISSING_DAYS if current.get("missing") else NCES_RECHECK_DAYS)


def _nces_member(archive: Path, family: str, name: str) -> tuple[str, bytes, int]:
    """(member name, bytes, member size) of the data member of an NCES zip: for EDGE the .dbf (in a folder
    or a nested zip), otherwise the text or CSV member named like the zip, else the largest one."""
    members = _zip_members(archive)
    with zipfile.ZipFile(archive) as z:
        if family == "edge":
            dbfs = [m for m in members if m.lower().endswith(".dbf")]
            if dbfs:
                info = z.getinfo(dbfs[0])
                return dbfs[0], z.read(dbfs[0]), info.file_size
            for nested in [m for m in members if m.lower().endswith(".zip")]:
                with zipfile.ZipFile(io.BytesIO(z.read(nested))) as inner:
                    inner_dbfs = [m for m in inner.namelist() if m.lower().endswith(".dbf") and "__MACOSX/" not in m]
                    if inner_dbfs:
                        return f"{nested}/{inner_dbfs[0]}", inner.read(inner_dbfs[0]), inner.getinfo(inner_dbfs[0]).file_size
        texts = [m for m in members if m.lower().endswith((".csv", ".txt"))]
        if not texts:
            raise FeedError(f"NCES_MEMBER_MISSING {name}")
        stem = Path(name).stem.lower()
        same = [m for m in texts if Path(m).stem.lower() == stem]
        member = same[0] if same else max(texts, key=lambda m: z.getinfo(m).file_size)
        return member, z.read(member), z.getinfo(member).file_size


def _nces_kansas(family: str, pick: Picker, row) -> bool:
    if family == "ccd":
        return _state_is(pick, row, ["FIPST"], "20")
    if family == "edge":
        return _state_is(pick, row, ["STFIP"], "20")
    if family == "ipeds":
        return _state_is(pick, row, ["STABBR"])
    if pick.has(PSS_ALIASES["state"]):
        return pick.value(row, PSS_ALIASES["state"]) == "KS"
    return _state_is(pick, row, PSS_ALIASES["state_fips"], "20")


def _nces_rows(path: Path, encoding: str, family: str, label: str):
    columns, aliases = {"ccd": (CCD_COLUMNS, CCD_ALIASES), "edge": (EDGE_COLUMNS, EDGE_ALIASES), "ipeds": (IPEDS_COLUMNS, IPEDS_ALIASES),
                        "pss": (PSS_COLUMNS, PSS_ALIASES)}[family]
    for header, row in _kept_rows(path, encoding):
        pick = Picker(header)
        values = [pick.value(row, ["SCHOOL_YEAR", "SURVYEAR"]) if family == "ccd" and pick.has(["SCHOOL_YEAR", "SURVYEAR"]) else label]
        for column in _columns(columns)[1:-1]:
            value = pick.value(row, aliases[column])
            values.append(_real(value) if column in NCES_REAL else value)
        yield (*values, _record_json(header, row))


def _nces_file(ctx, db, key: str, url: str, summary: dict) -> bool:
    """Download, cut and load one NCES file. False when NCES has no such file (404)."""
    family, label = key.split("/", 1)
    archive = core.temp_path(ctx, "nces-" + key.replace("/", "-") + ".zip")
    try:
        fetched = core.download(ctx, url, archive, limit=NCES_ZIP_LIMIT, timeout=1800, missing_ok=True)
        if fetched is None:
            return False
        summary["downloaded_bytes"] += archive.stat().st_size
        member, data, member_bytes = _nces_member(archive, family, Path(urllib.parse.urlparse(url).path).name)
        if member.lower().endswith(".dbf"):
            header, body, encoding = _dbf(data)
        else:
            text, encoding = _decode(data)
            rows = _delimited(text)
            if len(rows) < 2:
                raise FeedError(f"NCES_COLUMNS_CHANGED {key}")
            header, body = rows[0], rows[1:]
            if any(len(r) != len(header) for r in body):
                raise FeedError(f"NCES_ROW_SHAPE {key}")
        if len(set(h.upper() for h in header)) != len(header):
            raise FeedError(f"NCES_COLUMNS_CHANGED {key}")
        pick = Picker(header)
        try:
            kansas = [r for r in body if _nces_kansas(family, pick, r)]
        except KeyError as missing:
            raise FeedError(f"NCES_COLUMNS_CHANGED {key} {missing.args[0]}") from None
        if not kansas:
            raise FeedError(f"NCES_KANSAS_EMPTY {key}")
        source = {"ccd": "nces-ccd-directory", "edge": "nces-edge-school-locations", "ipeds": "nces-ipeds-directory", "pss": "nces-pss-schools"}[family]
        table, width = {"ccd": (CCD_TABLE, CCD_COLUMNS), "edge": (EDGE_TABLE, EDGE_COLUMNS), "ipeds": (IPEDS_TABLE, IPEDS_COLUMNS),
                        "pss": (PSS_TABLE, PSS_COLUMNS)}[family]
        result = keep_version(ctx, db, feed="schools", source_id=source, key=key, name=key, ext=".csv.gz",
                              body=core.gz(csv_bytes([header, *kansas], encoding)), url=fetched.url, fetched=fetched, original=archive,
                              extra={"encoding": encoding, "license": NCES_LICENSE, "member_bytes": member_bytes, "rows": len(kansas), "terms": NCES_TERMS},
                              table=table, width=len(_columns(width)), rows=lambda path, enc=encoding, f=family, lb=label: _nces_rows(path, enc, f, lb))
        summary["files"][key] = result["state"]
        summary["rows"] += result["rows"]
        return True
    finally:
        archive.unlink(missing_ok=True)


def schools(ctx, max_files: int = NCES_MAX_FILES, max_bytes: int = NCES_MAX_BYTES) -> dict:
    """Kansas public schools (CCD directory, EDGE locations), colleges (IPEDS) and private schools (PSS), by year."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NCES_DDL)
        state, today = core.get_state(db, "schools"), ctx.now().date()
        state = {**state, "files": dict(state.get("files", {}))}
        listing = state.get("ccd_listing")
        age = age_days(listing or {}, "checked", today)
        if not listing or age is None or age >= NCES_LISTING_DAYS:
            listing = {"checked": str(today), "files": _ccd_listing(ctx)}
            state = save_state(ctx, db, "schools", {**state, "ccd_listing": listing})
        due = [(k, u) for k, u in _nces_targets(ctx, state) if _nces_due(state, k, u, today)]
        summary, failures = {"files": {}, "rows": 0, "due": len(due), "downloaded_bytes": 0, "missing": []}, []
        done = 0
        for key, url in due:
            if done >= max_files or summary["downloaded_bytes"] >= max_bytes:
                break
            try:
                present = _nces_file(ctx, db, key, url, summary)
            except FeedError as error:
                if not str(error).startswith(("NCES_COLUMNS_CHANGED", "NCES_KANSAS_EMPTY", "NCES_MEMBER_MISSING", "NCES_ROW_SHAPE", "DBF_UNREADABLE")):
                    raise
                failures.append(str(error))
                done += 1
                continue
            done += 1
            mark = {"checked": str(today), "url": url, **({} if present else {"missing": True})}
            if not present:
                summary["missing"].append(key)
            state = save_state(ctx, db, "schools", {**state, "files": {**state["files"], key: mark}})
        if failures:
            raise FeedError("; ".join(failures))
        return {**summary, "pending": len(due) - done}
    finally:
        db.close()


# --- Historical topographic maps: the USGS HTMC inventory --------------------------------------------------

TNM_BUCKET = "https://prd-tnm.s3.amazonaws.com/"
HTMC_KEY = "StagedProducts/Maps/Metadata/historicaltopo.zip"
HTMC_URL = TNM_BUCKET + HTMC_KEY
HTMC_TERMS = "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits"
HTMC_HEADER = ["scan_id", "product_inventory_uuid", "series", "edition", "map_name", "primary_state", "westbc", "eastbc", "northbc", "southbc",
               "geom_wkt", "date_on_map", "imprint_year", "survey_year", "field_check_year", "edit_year", "aerial_photo_year",
               "photo_inspection_year", "photo_revision_year", "metadata_date", "print_releases", "variations", "hdatum_printed",
               "projection_printed", "publishers", "languages", "map_scale", "gnis_cell_id", "gnis_cell_name", "gnis_primary_state", "grid_size",
               "cell_type", "state_list", "county_list", "page_width_inches", "page_height_inches", "product_filename", "product_filesize",
               "product_url", "thumbnail_url", "geotiff_url", "metadata_url", "sciencebase_url"]
HTMC_TABLE = "kfm_usgs_htmc_maps"
HTMC_TYPES = {"scan_id": "INTEGER", "westbc": "REAL", "eastbc": "REAL", "northbc": "REAL", "southbc": "REAL"}
HTMC_COLUMNS = " ".join(f"{h}:{HTMC_TYPES[h]}" if h in HTMC_TYPES else h for h in HTMC_HEADER) + " geometry_geojson min_lon:REAL min_lat:REAL max_lon:REAL max_lat:REAL"
HTMC_DDL = _ddl(HTMC_TABLE, HTMC_COLUMNS, [("date_on_map",), ("map_name",), ("scan_id",)])
HTMC_RECHECK_DAYS = 28
HTMC_KANSAS_TEST = "bbox overlaps lon -102.06..-94.58, lat 36.99..40.01"
S3_ENTRY = re.compile(r"<Contents>.*?<Key>(.*?)</Key>.*?<LastModified>(.*?)</LastModified>.*?<ETag>(.*?)</ETag>.*?<Size>(\d+)</Size>.*?</Contents>", re.S)


def _s3_listing(ctx, key: str) -> dict:
    """{key, listed, etag, size} of one object from the bucket's listing."""
    body = ctx.fetch(TNM_BUCKET + "?prefix=" + urllib.parse.quote(key), limit=16_000_000).body.decode("utf-8", "replace")
    for found, listed, etag, size in S3_ENTRY.findall(body):
        if found == key:
            return {"key": key, "listed": listed, "etag": etag.replace("&quot;", "").strip('"'), "size": int(size)}
    raise FeedError(f"S3_OBJECT_NOT_LISTED {key}")


def _polygon_geojson(wkt: str) -> tuple:
    """A WKT POLYGON as canonical GeoJSON plus its bbox."""
    found = re.fullmatch(r"\s*POLYGON\s*\(\((.*)\)\)\s*", wkt or "", re.S)
    if not found:
        return None, None, None, None, None
    rings = []
    for ring in re.split(r"\)\s*,\s*\(", found.group(1)):
        points = [tuple(float(v) for v in p.split()) for p in ring.split(",")]
        rings.append([[x, y] for x, y, *_ in points])
    xs, ys = [x for ring in rings for x, _ in ring], [y for ring in rings for _, y in ring]
    return core.canonical({"type": "Polygon", "coordinates": rings}), min(xs), min(ys), max(xs), max(ys)


def _htmc_values(row):
    values = [int(v) if c == "scan_id" else float(v) if HTMC_TYPES.get(c) == "REAL" else v for c, v in zip(HTMC_HEADER, row)]
    return (*values, *_polygon_geojson(row[HTMC_HEADER.index("geom_wkt")]))


def _htmc_overlaps(row) -> bool:
    west, south, east, north = KANSAS_BOX
    w, e, n, s = (float(row[HTMC_HEADER.index(c)]) for c in ("westbc", "eastbc", "northbc", "southbc"))
    return w <= east and e >= west and s <= north and n >= south


def historical_topo_maps(ctx, recheck_days: int = HTMC_RECHECK_DAYS) -> dict:
    """The USGS historical topographic maps that overlap Kansas, from the HTMC inventory on The National Map."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(HTMC_DDL)
        state, today = core.get_state(db, "historical-topo-maps"), ctx.now().date()
        listing = _s3_listing(ctx, HTMC_KEY)
        age = age_days(state, "fetched", today)
        if state.get("etag") == listing["etag"] or (age is not None and age < recheck_days):
            return {"state": "unchanged" if state.get("etag") == listing["etag"] else "not_due", "etag": listing["etag"], "listed": listing["listed"]}
        archive = core.temp_path(ctx, "historicaltopo.zip")
        try:
            fetched = core.download(ctx, HTMC_URL, archive, limit=256_000_000, timeout=1800)
            members = _zip_members(archive)
            csvs, texts = [m for m in members if m.lower().endswith(".csv")], [m for m in members if m.lower().endswith(".txt")]
            if len(csvs) != 1:
                raise FeedError("HTMC_MEMBER_MISSING")
            kansas, total = [], 0
            with zipfile.ZipFile(archive) as z:
                report = z.read(texts[0]).decode("utf-8", "replace") if texts else None
                with z.open(csvs[0]) as handle:
                    reader = csv.reader(io.TextIOWrapper(handle, encoding="utf-8", newline=""))
                    header = next(reader, None)
                    if header != HTMC_HEADER:
                        raise FeedError("HTMC_COLUMNS_CHANGED")
                    for row in reader:
                        if len(row) != len(HTMC_HEADER):
                            raise FeedError("HTMC_ROW_SHAPE")
                        total += 1
                        try:
                            if _htmc_overlaps(row):
                                kansas.append(row)
                        except ValueError:
                            raise FeedError(f"HTMC_BBOX_INVALID {row[0]}") from None
            if not kansas:
                raise FeedError("HTMC_KANSAS_EMPTY")
            result = keep_version(ctx, db, feed="historical-topo-maps", source_id="usgs-htmc", key="htmc", name="htmc/historicaltopo-KS",
                                  ext=".csv.gz", body=core.gz(csv_bytes([HTMC_HEADER, *kansas])), url=fetched.url, fetched=fetched, original=archive,
                                  extra={"kansas_maps": len(kansas), "kansas_test": HTMC_KANSAS_TEST, "listed": listing["listed"], "maps": total,
                                         "report": report, "terms": HTMC_TERMS},
                                  table=HTMC_TABLE, width=len(_columns(HTMC_COLUMNS)),
                                  rows=lambda path: (_htmc_values(r) for r in read_csv(path, HTMC_HEADER, "HTMC")))
        finally:
            archive.unlink(missing_ok=True)
        save_state(ctx, db, "historical-topo-maps", {"etag": listing["etag"], "fetched": str(today), "kansas": len(kansas), "maps": total})
        return {**result, "maps": total, "kansas": len(kansas), "etag": listing["etag"]}
    finally:
        db.close()


# --- USGS samples: WQX 3.0 results since 2024, one key per month --------------------------------------------

SAMPLES_API = "https://api.waterdata.usgs.gov/samples-data/"
SAMPLES_DOCS = SAMPLES_API + "docs"
SAMPLES_TERMS = "https://www.usgs.gov/data-management/data-licensing"
SAMPLES_PROFILE = "fullphyschem"
SAMPLES_FIRST = (2024, 1)
SAMPLES_RECENT_DAYS, SAMPLES_RECHECK_DAYS, SAMPLES_MAX_MONTHS = 7, 91, 12
SAMPLES_HEADER = [
    "Org_Identifier", "Org_FormalName", "Project_Identifier", "Project_Name", "Project_QAPPApproved", "Project_QAPPApprovalAgency",
    "ProjectAttachment_FileName", "ProjectAttachment_FileType", "Location_Identifier", "Location_Name", "Location_Type", "Location_Description",
    "Location_State", "Location_CountryName", "Location_CountyName", "Location_CountryCode", "Location_StatePostalCode", "Location_CountyCode",
    "Location_HUCEightDigitCode", "Location_HUCTwelveDigitCode", "Location_TribalLandIndicator", "Location_TribalLand", "Location_Latitude",
    "Location_Longitude", "Location_HorzCoordReferenceSystemDatum", "Location_LatitudeStandardized", "Location_LongitudeStandardized",
    "Location_HorzCoordStandardizedDatum", "AlternateLocation_IdentifierCount", "Activity_ActivityIdentifier",
    "Activity_ActivityIdentifierUserSupplied", "Activity_TypeCode", "Activity_Media", "Activity_MediaSubdivision",
    "Activity_BottomDepthSamplingComponent", "ActivityBiological_AssemblageSampled", "ActivityBiological_ToxicityTestType",
    "Activity_ConductingOrganization", "Activity_Comment", "ActivityLocation_Latitude", "ActivityLocation_Longitude",
    "ActivityLocation_HorzCoordReferenceSystemDatum", "ActivityLocation_SourceMapScale", "ActivityLocation_LatitudeStandardized",
    "ActivityLocation_LongitudeStandardized", "ActivityLocation_HorzCoordStandardizedDatum", "ActivityLocation_HorzAccuracyMeasure",
    "ActivityLocation_HorzAccuracyMeasureUnit", "ActivityLocation_HorizontalAccuracyHorzCollectionMethod", "ActivityLocation_Description",
    "Activity_StartDate", "Activity_StartTime", "Activity_StartTimeZone", "Activity_EndDate", "Activity_EndTime", "Activity_EndTimeZone",
    "Activity_DepthHeightMeasure", "Activity_DepthHeightMeasureUnit", "Activity_BottomDepthAltitudeReferencePoint", "Activity_ActivityRelativeDepth",
    "Activity_TopDepthMeasure", "Activity_TopDepthMeasureUnit", "Activity_BottomDepthMeasure", "Activity_BottomDepthMeasureUnit",
    "SampleCollectionMethod_Identifier", "SampleCollectionMethod_IdentifierContext", "SampleCollectionMethod_Name",
    "SampleCollectionMethod_QualifierTypeName", "SampleCollectionMethod_Description", "SampleCollectionMethod_EquipmentName",
    "SampleCollectionMethod_EquipmentComment", "SamplePrepMethod_Identifier", "SamplePrepMethod_IdentifierContext", "SamplePrepMethod_Name",
    "SamplePrepMethod_QualifierType", "SamplePrepMethod_Description", "SamplePrepMethod_ContainerLabel", "SamplePrepMethod_ContainerType",
    "SamplePrepMethod_ContainerColor", "SamplePrepMethod_ChemicalPreservativeUsed", "SamplePrepMethod_ThermalPreservativeUsed",
    "SamplePrepMethod_TransportStorageDescription", "Activity_HydrologicCondition", "Activity_HydrologicEvent", "ActivityAttachment_FileName",
    "ActivityAttachment_FileType", "ActivityAttachment_FileDownload", "Result_DataLoggerLine", "Result_ResultDetectionCondition",
    "Result_Characteristic", "Result_CharacteristicUserSupplied", "Result_CASNumber", "Result_MethodSpeciation", "Result_SampleFraction",
    "ResultBiological_Intent", "ResultBiological_IndividualIdentifier", "ResultBiological_Taxon", "ResultBiological_TaxonUserSupplied",
    "ResultBiological_TaxonUserSuppliedReference", "ResultBiological_UnidentifiedSpeciesIdentifier", "ResultBiological_SampleTissueAnatomy",
    "ResultBiological_GroupSummaryCount", "GroupSummaryWeight_Measure", "GroupSummaryWeight_MeasureUnit", "ResultDepthHeight_Measure",
    "ResultDepthHeight_MeasureUnit", "ResultDepthHeight_AltitudeReferencePoint", "ResultDepthHeight_SamplingPointName",
    "ResultDepthHeight_SamplingPointType", "ResultDepthHeight_SamplingPointPlaceInSeries", "ResultDepthHeight_SamplingPointComment",
    "ResultDepthHeight_RecordIdentifierUserSupplied", "Result_MeasureIdentifier", "Result_Measure", "Result_MeasureUnit",
    "Result_MeasureQualifierCode", "Result_MeasureStatusIdentifier", "Result_StatisticalBase", "Result_StatisticalNValue", "Result_MeasureType",
    "Result_WeightBasis", "Result_TimeBasis", "Result_MeasureTemperatureBasis", "Result_MeasureParticleSizeBasis", "DataQuality_PrecisionValue",
    "DataQuality_BiasValue", "DataQuality_ConfidenceIntervalValue", "DataQuality_UpperConfidenceLimitValue",
    "DataQuality_LowerConfidenceLimitValue", "DataQuality_ResultComment", "DetectionLimit_TypeA", "DetectionLimit_MeasureA",
    "DetectionLimit_MeasureUnitA", "DetectionLimit_CommentA", "DetectionLimit_TypeB", "DetectionLimit_MeasureB", "DetectionLimit_MeasureUnitB",
    "DetectionLimit_CommentB", "LabInfo_LabSampleSplitRatio", "LabInfo_LabAccreditationIndicator", "LabInfo_LabAccreditationAuthority",
    "LabInfo_TaxonAccreditationIndicator", "LabInfo_TaxonAccreditationAuthority", "ResultAnalyticalMethod_Identifier",
    "ResultAnalyticalMethod_IdentifierContext", "ResultAnalyticalMethod_Name", "ResultAnalyticalMethod_QualifierType",
    "ResultAnalyticalMethod_Description", "Result_ComparableMethodIdentifier", "Result_ComparableMethodIdentifierContext",
    "Result_ComparableMethodModification", "LabInfo_Name", "LabInfo_AnalysisStartDate", "LabInfo_AnalysisStartTime",
    "LabInfo_AnalysisStartTimeZone", "LabInfo_AnalysisEndDate", "LabInfo_AnalysisEndTime", "LabInfo_AnalysisEndTimeZone",
    "LabInfo_LaboratoryComment", "LabSamplePrepMethod_Identifier", "LabSamplePrepMethod_IdentifierContext", "LabSamplePrepMethod_Name",
    "LabSamplePrepMethod_QualifierType", "LabSamplePrepMethod_Description", "LabSamplePrepMethod_StartDate", "LabSamplePrepMethod_StartTime",
    "LabSamplePrepMethod_StartTimeZone", "LabSamplePrepMethod_EndDate", "LabSamplePrepMethod_EndTime", "LabSamplePrepMethod_EndTimeZone",
    "LabSamplePrepMethod_DilutionFactor", "ResultAttachment_FileName", "ResultAttachment_FileType", "ResultAttachment_FileDownload",
    "ProviderName", "Result_CharacteristicComparable", "Result_CharacteristicGroup", "Org_Type", "LastChangeDate", "USGSpcode", "USGSSampleAquifer"]
SAMPLES_SPECIAL = {"USGSpcode": "usgs_pcode", "USGSSampleAquifer": "usgs_sample_aquifer", "ProviderName": "provider_name", "LastChangeDate": "last_change_date"}
SAMPLES_REAL = {"location_latitude", "location_longitude", "location_latitude_standardized", "location_longitude_standardized"}
SAMPLES_TABLE = "kfm_usgs_samples_results"


def _samples_column(name: str) -> str:
    """A WQX 3.0 column as snake_case: Location_HUCEightDigitCode -> location_huc_eight_digit_code."""
    if name in SAMPLES_SPECIAL:
        return SAMPLES_SPECIAL[name]
    parts = []
    for part in name.split("_"):
        part = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", part)
        part = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", part)
        parts.append(part.lower())
    return "_".join(parts)


SAMPLES_COLUMNS = [_samples_column(h) for h in SAMPLES_HEADER]
SAMPLES_DDL = _ddl(SAMPLES_TABLE, " ".join(f"{c}:REAL" if c in SAMPLES_REAL else c for c in SAMPLES_COLUMNS),
                   [("location_identifier", "activity_start_date"), ("usgs_pcode", "activity_start_date")], without_rowid=True)


def _samples_url(start: date, end: date) -> str:
    return f"{SAMPLES_API}results/{SAMPLES_PROFILE}?mimeType=text/csv&stateFips=US:20&activityStartDateLower={start}&activityStartDateUpper={end}"


def _samples_windows(year: int, month: int) -> list[tuple[date, date]]:
    last = calendar.monthrange(year, month)[1]
    return [(date(year, month, a), date(year, month, min(b, last))) for a, b in ((1, 7), (8, 14), (15, 21), (22, 31))]


def _samples_values(row):
    return tuple(None if v == "" else float(v) if c in SAMPLES_REAL else v for c, v in zip(SAMPLES_COLUMNS, row))


def _samples_month(ctx, db, year: int, month: int) -> dict:
    rows, queries, downloaded, first = [], [], 0, None
    for start, end in _samples_windows(year, month):
        url = _samples_url(start, end)
        try:
            fetched = ctx.fetch(url, limit=256_000_000, timeout=900)
        except FeedError as error:
            if str(error).startswith(("HTTP_403", "HTTP_429")):
                raise FeedError(f"USGS_RATE_LIMITED {url}") from None
            raise
        first = first or fetched
        queries.append(url)
        downloaded += len(fetched.body)
        text = fetched.body.decode("utf-8").lstrip("﻿")
        if not text.strip():
            continue
        parsed = [r for r in csv.reader(io.StringIO(text, newline="")) if r]
        if parsed[0] != SAMPLES_HEADER:
            raise FeedError(f"USGS_SAMPLES_COLUMNS_CHANGED {year}-{month:02d}")
        if any(len(r) != len(SAMPLES_HEADER) for r in parsed[1:]):
            raise FeedError(f"USGS_SAMPLES_ROW_SHAPE {year}-{month:02d}")
        rows.extend(parsed[1:])
    key = f"results/{year}-{month:02d}"
    if not rows:
        if key in loaded_keys(db, "usgs-samples-results"):
            raise FeedError(f"USGS_SAMPLES_MONTH_EMPTIED {year}-{month:02d}")
        return {"state": "empty", "rows": 0}
    rows.sort()
    window = [str(date(year, month, 1)), str(date(year, month, calendar.monthrange(year, month)[1]))]
    return keep_version(ctx, db, feed="usgs-samples", source_id="usgs-samples-results", key=key, name=f"results/{year}/kansas-results-{year}-{month:02d}",
                        ext=".csv.gz", body=core.gz(csv_bytes([SAMPLES_HEADER, *rows])), url=queries[0],
                        extra={"docs": SAMPLES_DOCS, "downloaded_bytes": downloaded, "profile": SAMPLES_PROFILE, "queries": queries, "rows": len(rows),
                               "terms": SAMPLES_TERMS, "window": window},
                        table=SAMPLES_TABLE, width=len(SAMPLES_COLUMNS),
                        rows=lambda path: (_samples_values(r) for r in read_csv(path, SAMPLES_HEADER, "USGS_SAMPLES")))


def usgs_samples(ctx, max_months: int = SAMPLES_MAX_MONTHS, recent_days: int = SAMPLES_RECENT_DAYS, recheck_days: int = SAMPLES_RECHECK_DAYS) -> dict:
    """Kansas discrete water-quality results since 2024 from USGS Samples Data, one version per month."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(SAMPLES_DDL)
        state, today = core.get_state(db, "usgs-samples"), ctx.now().date()
        checked = dict(state.get("checked", {}))
        months, year, month = [], *SAMPLES_FIRST
        while (year, month) <= (today.year, today.month):
            months.append((year, month))
            year, month = (year + 1, 1) if month == 12 else (year, month + 1)
        due = []
        for year, month in months:
            age = age_days(checked, f"{year}-{month:02d}", today)
            if age is None or age >= (recent_days if year >= today.year - 1 else recheck_days):
                due.append((year, month))
        summary = {"loaded": [], "unchanged": [], "empty": [], "rows": 0, "due": len(due)}
        for year, month in due[:max_months]:
            result = _samples_month(ctx, db, year, month)
            summary[result["state"] if result["state"] in ("unchanged", "empty") else "loaded"].append(f"{year}-{month:02d}")
            summary["rows"] += result["rows"]
            checked[f"{year}-{month:02d}"] = str(today)
            state = save_state(ctx, db, "usgs-samples", {**state, "checked": checked})
        return {**summary, "pending": max(0, len(due) - max_months)}
    finally:
        db.close()
