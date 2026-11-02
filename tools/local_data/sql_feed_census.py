"""Census and EIA feeds: ACS 5-year estimates, the 2020 Census (P.L. 94-171 and DHC) and EIA SEDS, for Kansas.

Providers and terms: the U.S. Census Bureau (open data policy https://www.census.gov/about/policies/open-gov/open-data.html,
citation https://www.census.gov/about/policies/citation.html) and the U.S. Energy Information Administration
(https://www.eia.gov/about/copyrights_reuse.php). Both are public-domain U.S. government data and ask for a source
acknowledgment. All are published aggregates with no personal records (the Census Bureau's disclosure avoidance is
already applied), and every public column of the files read is kept. The Census API wants a key, so these feeds read
the no-key bulk files on www2.census.gov.

census-acs: ACS 5-year table-based summary files, ``summary_file/<year>/table-based-SF/``, where year ends the five
(2024 is 2020-2024). ``data/5YRData/acsdt5y<year>-<table>.dat`` is one national file per table: pipe-delimited,
GEO_ID then estimate and margin pairs (``B19013_E001|B19013_M001``), every geography (616,690 in 2024). Beside it,
``documentation/Geos<year>5YR.txt`` (45 columns, 90.7 MB) names each GEO_ID and
``ACS<year>5YR_Table_Shells.txt`` gives the table titles, universes and variable labels. Kansas is the Geos rows with
STATE 20: 9,944 in 2024, at 48 summary levels and components (state 0400000US20 and its components 040C201US20 and
so on, counties 0500000US20…, county subdivisions 0600000US20…, places 1600000US20…, tracts 1400000US20…, block
groups 1500000US20…, congressional districts 5001900US20…, state legislative districts 610U900US20… and
620L900US20…, unified school districts 9700000US20…, PUMAs, and the Kansas parts of metro areas, urban areas and
reservations), plus the 704 ZCTAs (860Z200US…) in Kansas's ZIP prefixes 66 and 67, which the Geos file does not
assign to a state. A table with every geography has 10,648 Kansas rows, 1.6% of its bytes. The Census Bureau's
negative nine-digit annotation values (-666666666, -555555555 and so on) are kept as published.
Size, measured 2026-11-02 (about 100 bytes a value row with its index): all 1,198 tables are 46.1 GB to download and
about 110 million Kansas values (about 11 GB) per vintage; the curated ``ACS_TABLES`` (76 tables) are 4.2 GB and about
9.8 million values (about 1 GB), so the curated set is the default. ``tables=None`` loads every table.
Schedule, per run: read the two listings of each vintage in ``ACS_VINTAGES``. A file is due when its listed time
differs from the one recorded, so a re-published file is fetched again and a rerun fetches nothing. Each national file
is streamed to a temp file and cut to the Kansas lines, kept byte for byte with the header (its receipt records the
national file). A run starts at most ``max_tables`` (40) tables and none after ``run_bytes`` (2 GB) downloaded, so a
vintage takes three runs. Add an older vintage (2021-2023 use the same format) or the next release (2025, due
December 2026) to ``ACS_VINTAGES``; a vintage the Census Bureau has not published is reported, not an error. Each
vintage is its own dataset, never a replacement.
Revisions: every file is ``load_version`` keyed ``acs5/<year>/<table>`` (and ``…/geos``, ``…/shells``); a changed
Kansas cut replaces that version, an unchanged one is recorded as checked.
Tables: ``kfm_census_acs_values`` (vintage, table_id, geo_id, variable as ``B19013_001``, estimate, margin_of_error;
numbers as INTEGER or REAL), ``kfm_census_acs_geographies`` (vintage and the 45 Geos columns) and
``kfm_census_acs_variables`` (vintage and the 8 shell columns).

census-decennial: the 2020 Census Kansas files, ``ks2020.pl.zip`` (P.L. 94-171 redistricting, 23.4 MB, 3 segments)
and ``ks2020.dhc.zip`` (Demographic and Housing Characteristics, 172 MB, 44 segments, 2.1 GB unzipped). Each holds a
97-column geographic header ``ksgeo2020.<pl|dhc>`` and segment files ``ks000NN2020.<pl|dhc>``: pipe-delimited, no
header, five identifiers then the cells, joined on LOGRECNO. The layouts come from the Census Bureau's own workbooks,
read with the standard library: ``2020_PLSummaryFile_FieldNames.xlsx`` and ``2020-dhc-table-matrix.xlsx`` (table,
segment, field order, labels, titles and universes), and the cell counts must match every line, or the run stops with
``DEC_COLUMNS_CHANGED``. Geographies kept (``DEC_LEVELS``, total component 00): state, 105 counties, 1,531 county
subdivisions, 829 tracts, 2,461 block groups, 740 places, AIANNH, congressional and legislative districts, 286
unified school districts, and in the DHC 710 ZCTAs and the Kansas parts of metro areas: 6,127 PL and 6,860 DHC
geographies. Blocks are not modest: PL's 172,529 blocks times 301 cells are 51.9 million values (about 4.6 GB), and
the DHC's are larger, so block cell values are not loaded. PL's block rows are kept in the geography table, with their
POP100 and HU100 counts and internal points. PL loads all six tables (1.8 million values, 0.2 GB). The DHC's 249
tables are 46.2 million values (about 4.6 GB) at these geographies; by default it loads the base tables and their
race and Hispanic-origin iterations A-I, except PCT12's single-year-of-age iterations: 183 tables, 22.8 million values
(about 2.3 GB). Set ``DEC_ITERATIONS = None`` for every table, or ``""`` for the 66 base tables (8.6 million). Values are
NUMERIC (so a published 37.0 is the integer 37); a median the Census Bureau could not compute is published as ``.`` and
kept as that TEXT.
Schedule: the data are static, so a product is loaded once and rechecked every ``DEC_RECHECK_DAYS`` (365). A run
loads at most ``max_segments`` (24) segments, so the first load takes two runs (the zip is fetched again for the
second); after that a run makes no request until the yearly recheck. Each segment's Kansas cut keeps the selected
cells of the kept geographies, with a header row; the receipt records the zip.
Revisions: ``load_version`` keyed ``<pl|dhc>2020/geo``, ``…/segment-NN`` and ``…/labels``. A changed zip, or a changed
selection, reloads every segment, and an unchanged segment is recorded as unchanged.
Tables: ``kfm_census_decennial_values`` (product, vintage, table_id, geoid, variable as ``P0010001``, value),
``kfm_census_decennial_geographies`` (product, vintage and the 97 header columns; arealand, areawatr, pop100 and hu100
as INTEGER) and ``kfm_census_decennial_variables`` (product, vintage, table_id, variable, segment, position, label,
title, universe).

eia-seds: the State Energy Data System bulk file, https://www.eia.gov/opendata/bulk/SEDS.zip (9.5 MB; 63 MB of
JSON lines, one object per line: 48,046 series, 970 categories, and geoset and relation lines, documented at
https://www.eia.gov/opendata/bulkfiles.php). Kansas is the series with geography USA-KS, whose ids are
``SEDS.<code>.KS.A``: 923 annual series, 49,064 values, 1960-2024. The kept copy is those lines and the category lines,
byte for byte. Schedule: every run reads the 28 KB bulk manifest; the zip is fetched when its SEDS ``last_updated``
changes, and at least every ``min_days`` (30) days to compare digests. EIA revises past years with each annual
release (June). Revisions: one ``key`` ("SEDS") whose new version replaces the old in one transaction across the four
tables. Tables: ``kfm_eia_seds_series`` (the 13 series fields), ``kfm_eia_seds_values`` (series_id, period, value),
``kfm_eia_seds_categories`` and ``kfm_eia_seds_category_series`` (the category tree and its Kansas series).
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import date
import gzip
import io
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

BOM = b"\xef\xbb\xbf"
LISTING = re.compile(r'href="([^"/?]+)">[^<]*</a></td><td[^>]*>\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')
INTEGER, DECIMAL = re.compile(r"-?\d+"), re.compile(r"-?\d*\.\d+")


def _text(line: bytes) -> str:
    line = line.rstrip(b"\r\n").removeprefix(BOM)
    try:
        return line.decode("utf-8")
    except UnicodeDecodeError:
        return line.decode("latin-1")


def _num(value: str):
    """A published number as INTEGER or REAL, an empty cell as NULL, anything else as the provider's text."""
    if INTEGER.fullmatch(value):
        return int(value)
    if DECIMAL.fullmatch(value):
        return float(value)
    return value or None


def _listing(body: bytes) -> dict[str, str]:
    """name -> listed modification time, from a www2.census.gov directory page."""
    return dict(LISTING.findall(body.decode("latin-1")))


@contextmanager
def _gz_out(path: Path):
    """A gzip writer with no name or time in its header, so the same content always gives the same bytes."""
    with open(path, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as out:
        yield out


def _cut_rows(path: Path):
    """The rows of a kept pipe-delimited cut, header first."""
    with gzip.open(path, "rb") as handle:
        for line in handle:
            yield _text(line).split("|")


def _save(ctx, db, feed: str, state: dict) -> dict:
    with core.pipeline_lock(ctx):
        core.set_state(db, ctx, feed, state)
    return state


def _days_since(ctx, day: str | None) -> int | None:
    return None if not day else (ctx.now().date() - date.fromisoformat(day)).days


def _load_cut(ctx, db, *, feed, url, temp, limit, cut, raw_name, key, source_id, table, rows, width, extra, summary):
    """Stream url to a temp file, cut it to Kansas with cut(full, kept) -> rows kept, keep the cut and load it.
    None when the provider no longer has the file; {"state": "empty"} when nothing in it is Kansas."""
    full, kept_path = core.temp_path(ctx, temp), core.temp_path(ctx, temp + ".kansas.gz")
    try:
        fetched = core.download(ctx, url, full, limit=limit, timeout=1800, missing_ok=True)
        if fetched is None:
            return None
        summary["downloaded_bytes"] += full.stat().st_size
        kept = cut(full, kept_path)
        if not kept:
            return {"state": "empty", "rows": 0}
        path, digest = core.store_raw(ctx, feed, raw_name(core.file_sha256(kept_path)[:12]), kept_path, url=fetched.url, fetched=fetched,
                                      original=full, extra={"key": key, "kansas_rows": kept, **extra})
        with core.pipeline_lock(ctx):
            return core.load_version(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=fetched.url, table=table,
                                     rows=rows(path), width=width)
    finally:
        full.unlink(missing_ok=True)
        kept_path.unlink(missing_ok=True)


def _replace(db, ctx, *, source_id, key, path, digest, url, tables) -> dict:
    """``load_version`` for one source file that fills several tables: tables is [(table, width, rows)], and each
    table's row_number starts at 1. Call with the pipeline lock held."""
    receipt = core.receipt_for(ctx, path)
    if receipt.get("key") != key:
        raise FeedError(f"RECEIPT_KEY_MISMATCH {key}")
    previous = db.execute("SELECT file_id, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                          "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()
    if digest in {sha for _, sha in previous}:
        return {"state": "unchanged", "rows": 0, "superseded": 0}
    if core.loaded(db, digest):
        raise FeedError(f"SOURCE_CONTENT_SHARED {key}")
    file_id = core.begin_source(db, ctx, source_id, path, digest, url, receipt)
    try:
        for old, _ in previous:
            for table, _, _ in tables:
                db.execute(f"DELETE FROM {table} WHERE file_id=?", (old,))
            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))
        total = 0
        for table, width, rows in tables:
            sql, batch, count = f"INSERT INTO {table} VALUES ({','.join('?' * (width + 2))})", [], 0
            for row in rows:
                if len(row) != width:
                    raise FeedError(f"ROW_SHAPE {key} {table} {count + len(batch) + 1}")
                batch.append((file_id, count + len(batch) + 1, *row))
                if len(batch) == 20000:
                    db.executemany(sql, batch)
                    count += len(batch)
                    batch = []
            db.executemany(sql, batch)
            total += count + len(batch)
        core.finish_source(db, file_id, total)
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"state": "loaded", "rows": total, "superseded": len(previous)}


def _retire(db, *, source_id: str, key: str, table: str) -> int:
    """Remove the loaded version of key: its rows go and its source is superseded. Call with the pipeline lock held."""
    old = [fid for (fid,) in db.execute("SELECT file_id FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                                        "AND json_extract(receipt_json,'$.key')=?", (source_id, key))]
    if old:
        db.execute("BEGIN IMMEDIATE")
        try:
            for fid in old:
                db.execute(f"DELETE FROM {table} WHERE file_id=?", (fid,))
                db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (fid,))
            db.execute("COMMIT")
        except BaseException:
            db.execute("ROLLBACK")
            raise
    return len(old)


# --- ACS 5-year table-based summary files -----------------------------------------------------------------------

ACS = "https://www2.census.gov/programs-surveys/acs/summary_file/{vintage}/table-based-SF/"
ACS_VINTAGES = (2024,)   # 5-year releases by end year; 2021-2023 use the same format, 2025 is due December 2026
ACS_TABLES = (
    # population by age, sex, race and Hispanic origin
    "B01001", "B01001A", "B01001B", "B01001C", "B01001D", "B01001E", "B01001F", "B01001G", "B01001H", "B01001I",
    "B01002", "B01003", "B02001", "B03002",
    # households, families, marital status
    "B11001", "B11003", "B11005", "B11016", "B25010", "B12001",
    # income and assistance
    "B19001", "B19013", "B19025", "B19049", "B19083", "B19113", "B19301", "B19055", "B19057", "B22010",
    # poverty
    "B17001", "B17010", "C17002",
    # school enrollment and educational attainment
    "B14001", "B15003",
    # employment, occupation, class of worker, earnings, industry
    "B23025", "C24010", "B24080", "B20017", "C24030",
    # commuting
    "B08301", "B08303", "B08013",
    # housing units, occupancy, tenure, structure, value, rent and costs
    "B25001", "B25002", "B25003", "B25004", "B25014", "B25018", "B25024", "B25034", "B25035", "B25040", "B25058",
    "B25064", "B25070", "B25071", "B25075", "B25077", "B25088", "B25091", "B25105",
    # vehicles, computers and internet
    "B25044", "B28001", "B28002",
    # health insurance, disability, veterans
    "B27001", "C27007", "B18101", "C18120", "B21001", "B21002",
    # language, nativity and migration
    "C16001", "C16002", "B05002", "B05012", "B07003",
)
ACS_GEOS_COLUMNS = tuple("FILEID STUSAB SUMLEVEL COMPONENT US REGION DIVISION STATE COUNTY COUSUB PLACE TRACT BLKGRP CONCIT "
                         "AIANHH AIANHHFP AIHHTLI AITS AITSFP ANRC CBSA CSA METDIV MACC MEMI NECTA CNECTA NECTADIV UA CDCURR "
                         "SLDU SLDL ZCTA5 SUBMCD SDELM SDSEC SDUNI UR PCI PUMA5 GEO_ID NAME BTTR BTBG TL_GEO_ID".split())
ACS_SHELLS_COLUMNS = ("Table ID", "Line", "Indent", "Unique ID", "Label", "Title", "Universe", "Type")
ACS_STATE, ACS_SUMLEVEL, ACS_ZCTA5 = (ACS_GEOS_COLUMNS.index(c) for c in ("STATE", "SUMLEVEL", "ZCTA5"))
ACS_ZCTA_PREFIXES = (b"66", b"67")   # Kansas's USPS ZIP prefixes
ACS_TABLE_LIMIT, ACS_GEOS_LIMIT, ACS_SHELLS_LIMIT, ACS_LISTING_LIMIT = 1_000_000_000, 400_000_000, 64_000_000, 8_000_000
ACS_RUN_BYTES = 2_000_000_000
ACS_GEO_COLUMNS_SQL = ", ".join(c.lower() + " TEXT" for c in ACS_GEOS_COLUMNS)
ACS_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_census_acs_values (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, vintage INTEGER NOT NULL, table_id TEXT NOT NULL, geo_id TEXT NOT NULL,
  variable TEXT NOT NULL, estimate NUMERIC, margin_of_error NUMERIC, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_acs_values_geo ON kfm_census_acs_values(geo_id, table_id);
CREATE TABLE IF NOT EXISTS kfm_census_acs_geographies (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, vintage INTEGER NOT NULL, {ACS_GEO_COLUMNS_SQL},
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_acs_geographies_geo ON kfm_census_acs_geographies(geo_id, vintage);
CREATE TABLE IF NOT EXISTS kfm_census_acs_variables (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, vintage INTEGER NOT NULL, table_id TEXT NOT NULL, line TEXT, indent INTEGER,
  unique_id TEXT, label TEXT, title TEXT, universe TEXT, type TEXT, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_acs_variables_id ON kfm_census_acs_variables(unique_id, vintage);
"""


def _acs_variables(columns: list[str], table: str, name: str) -> list[str]:
    """B19013_001… from the header GEO_ID|B19013_E001|B19013_M001|…; any other header stops the feed."""
    if columns[0] != "GEO_ID" or len(columns) < 3 or len(columns) % 2 == 0:
        raise FeedError(f"ACS_COLUMNS_CHANGED {name}")
    variables = []
    for e, m in zip(columns[1::2], columns[2::2]):
        me, mm = re.fullmatch(re.escape(table) + r"_E(\d+)", e), re.fullmatch(re.escape(table) + r"_M(\d+)", m)
        if not me or not mm or me.group(1) != mm.group(1):
            raise FeedError(f"ACS_COLUMNS_CHANGED {name}")
        variables.append(f"{table}_{me.group(1)}")
    return variables


def _acs_geos_cut(name: str):
    def cut(full: Path, kept_path: Path) -> int:
        with open(full, "rb") as src, _gz_out(kept_path) as out:
            head = src.readline()
            if _text(head).split("|") != list(ACS_GEOS_COLUMNS):
                raise FeedError(f"ACS_GEOS_COLUMNS_CHANGED {name}")
            out.write(head)
            kept = 0
            for line in src:
                p = line.rstrip(b"\r\n").split(b"|")
                if len(p) != len(ACS_GEOS_COLUMNS):
                    raise FeedError(f"ACS_ROW_SHAPE {name}")
                if p[ACS_STATE] == b"20" or (p[ACS_SUMLEVEL] == b"860" and p[ACS_ZCTA5][:2] in ACS_ZCTA_PREFIXES):
                    out.write(line)
                    kept += 1
        return kept
    return cut


def _acs_geos_rows(vintage: int):
    def rows(path: Path):
        lines = _cut_rows(path)
        next(lines)
        for p in lines:
            yield (vintage, *p)
    return rows


def _acs_table_cut(name: str, table: str, kansas: set[bytes]):
    def cut(full: Path, kept_path: Path) -> int:
        with open(full, "rb") as src, _gz_out(kept_path) as out:
            head = src.readline()
            columns = _text(head).split("|")
            _acs_variables(columns, table, name)
            out.write(head)
            kept = 0
            for line in src:
                if line.split(b"|", 1)[0] in kansas:
                    if line.count(b"|") != len(columns) - 1:
                        raise FeedError(f"ACS_ROW_SHAPE {name}")
                    out.write(line)
                    kept += 1
        return kept
    return cut


def _acs_table_rows(vintage: int, table: str):
    def rows(path: Path):
        lines = _cut_rows(path)
        variables = _acs_variables(next(lines), table, path.name)
        for p in lines:
            for i, variable in enumerate(variables):
                yield (vintage, table, p[0], variable, _num(p[2 * i + 1]), _num(p[2 * i + 2]))
    return rows


def _acs_shells(body: bytes, vintage: int, name: str) -> list[tuple]:
    lines = [_text(line) for line in body.splitlines() if line.strip()]
    if not lines or lines[0].split("|") != list(ACS_SHELLS_COLUMNS):
        raise FeedError(f"ACS_SHELLS_COLUMNS_CHANGED {name}")
    rows = []
    for line in lines[1:]:
        p = line.split("|")
        if len(p) != len(ACS_SHELLS_COLUMNS):
            raise FeedError(f"ACS_ROW_SHAPE {name}")
        rows.append((vintage, p[0], p[1], int(p[2]) if p[2].isdigit() else p[2] or None, *(v or None for v in p[3:])))
    return rows


def _acs_vintage(ctx, db, state: dict, vintage: int, tables, summary: dict, budget: dict) -> dict:
    base = ACS.format(vintage=vintage)
    docs, data = (ctx.fetch(base + folder, limit=ACS_LISTING_LIMIT, missing_ok=True) for folder in ("documentation/", "data/5YRData/"))
    if docs is None or data is None:
        summary["unpublished"].append(vintage)
        return state
    docs, data = _listing(docs.body), _listing(data.body)
    vs = state.get("vintages", {}).get(str(vintage), {})
    geos, shells = f"Geos{vintage}5YR.txt", f"ACS{vintage}5YR_Table_Shells.txt"
    if geos not in docs or shells not in docs:
        if vs:
            raise FeedError(f"ACS_LISTING_CHANGED {vintage}")
        summary["unpublished"].append(vintage)   # the 1-year files come first, under the same folders
        return state
    vs = state.setdefault("vintages", {}).setdefault(str(vintage), {})
    vs.setdefault("tables", {})
    if vs.get("geos") != docs[geos] and (budget["tables"] <= 0 or summary["downloaded_bytes"] >= budget["bytes"]):
        summary["pending_vintages"].append(vintage)
        return state
    if vs.get("geos") != docs[geos]:
        key = f"acs5/{vintage}/geos"
        result = _load_cut(ctx, db, feed="census-acs", url=base + "documentation/" + geos, temp=f"acs-{geos}", limit=ACS_GEOS_LIMIT,
                           cut=_acs_geos_cut(geos), raw_name=lambda h: f"acs5/{vintage}/kansas-{geos[:-4]}-{h}.txt.gz", key=key,
                           source_id="census-acs5-geos", table="kfm_census_acs_geographies", rows=_acs_geos_rows(vintage),
                           width=len(ACS_GEOS_COLUMNS) + 1, extra={"vintage": vintage, "listed": docs[geos]}, summary=summary)
        if result is None or result["state"] == "empty":
            raise FeedError(f"ACS_GEOS_MISSING {geos}")
        vs["geos"] = docs[geos]
        summary["geographies"] += result["rows"]
        state = _save(ctx, db, "census-acs", state)
    if vs.get("shells") != docs[shells]:
        fetched = ctx.fetch(base + "documentation/" + shells, limit=ACS_SHELLS_LIMIT, timeout=600)
        rows, key = _acs_shells(fetched.body, vintage, shells), f"acs5/{vintage}/shells"
        path, digest = core.store_raw(ctx, "census-acs", f"acs5/{vintage}/{shells[:-4]}-{core.sha256(fetched.body)[:12]}.txt.gz",
                                      core.gz(fetched.body), url=fetched.url, fetched=fetched,
                                      extra={"key": key, "vintage": vintage, "listed": docs[shells]})
        with core.pipeline_lock(ctx):
            summary["variables"] += core.load_version(db, ctx, source_id="census-acs5-shells", key=key, path=path, digest=digest,
                                                      url=fetched.url, table="kfm_census_acs_variables", rows=rows, width=9)["rows"]
            vs["shells"] = docs[shells]
            core.set_state(db, ctx, "census-acs", state)
    kansas = {g.encode() for (g,) in db.execute("SELECT geo_id FROM kfm_census_acs_geographies WHERE vintage=?", (vintage,))}
    if not kansas:
        raise FeedError(f"ACS_GEOS_MISSING {vintage}")
    prefix = f"acsdt5y{vintage}-"
    listed = {n[len(prefix):-4].upper(): t for n, t in data.items() if n.startswith(prefix) and n.endswith(".dat")}
    wanted = sorted(listed) if tables is None else [t.upper() for t in tables if t.upper() in listed]
    summary["absent"] += [] if tables is None else [f"{vintage}/{t}" for t in tables if t.upper() not in listed]
    for table in [t for t in wanted if vs["tables"].get(t) != listed[t]]:
        if budget["tables"] <= 0 or summary["downloaded_bytes"] >= budget["bytes"]:
            break
        budget["tables"] -= 1
        name, key = f"{prefix}{table.lower()}.dat", f"acs5/{vintage}/{table}"
        result = _load_cut(ctx, db, feed="census-acs", url=base + "data/5YRData/" + name, temp="acs-" + name, limit=ACS_TABLE_LIMIT,
                           cut=_acs_table_cut(name, table, kansas), raw_name=lambda h: f"acs5/{vintage}/kansas-{name[:-4]}-{h}.dat.gz",
                           key=key, source_id="census-acs5", table="kfm_census_acs_values", rows=_acs_table_rows(vintage, table),
                           width=6, extra={"vintage": vintage, "table_id": table, "listed": listed[table]}, summary=summary)
        if result is None:
            summary["missing"].append(key)
            continue
        summary[{"loaded": "tables", "unchanged": "unchanged", "empty": "empty"}[result["state"]]].append(key)
        summary["rows"] += result["rows"]
        vs["tables"][table] = listed[table]
        state = _save(ctx, db, "census-acs", state)
    summary["pending"] += sum(1 for t in wanted if vs["tables"].get(t) != listed[t])
    return state


def census_acs(ctx, vintages=ACS_VINTAGES, tables=ACS_TABLES, max_tables: int = 40, run_bytes: int = ACS_RUN_BYTES) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(ACS_SCHEMA)
        state = core.get_state(db, "census-acs")
        summary = {"tables": [], "unchanged": [], "empty": [], "missing": [], "absent": [], "unpublished": [], "pending_vintages": [],
                   "rows": 0, "geographies": 0, "variables": 0, "downloaded_bytes": 0, "pending": 0}
        budget = {"tables": max_tables, "bytes": run_bytes}
        for vintage in vintages:
            state = _acs_vintage(ctx, db, state, vintage, tables, summary, budget)
        return {**summary, "tables_loaded": len(summary["tables"])}
    finally:
        db.close()


# --- 2020 Census: P.L. 94-171 and DHC ---------------------------------------------------------------------------

DEC = "https://www2.census.gov/programs-surveys/decennial/"
DEC_SOURCES = {   # product: (Kansas zip, layout workbook, FILEID)
    "pl": (DEC + "2020/data/01-Redistricting_File--PL_94-171/Kansas/ks2020.pl.zip",
           DEC + "rdo/about/2020-census-program/Phase3/SupportMaterials/2020_PLSummaryFile_FieldNames.xlsx", b"PLST"),
    "dhc": (DEC + "2020/data/demographic-and-housing-characteristics-file/Kansas/ks2020.dhc.zip",
            DEC + "2020/technical-documentation/complete-tech-docs/demographic-and-housing-characteristics-file-and-demographic-profile/"
                  "2020-dhc-table-matrix.xlsx", b"DHCST"),
}
DEC_GEO_COLUMNS = tuple("FILEID STUSAB SUMLEV GEOVAR GEOCOMP CHARITER CIFSN LOGRECNO GEOID GEOCODE REGION DIVISION STATE STATENS "
                        "COUNTY COUNTYCC COUNTYNS COUSUB COUSUBCC COUSUBNS SUBMCD SUBMCDCC SUBMCDNS ESTATE ESTATECC ESTATENS CONCIT "
                        "CONCITCC CONCITNS PLACE PLACECC PLACENS TRACT BLKGRP BLOCK AIANHH AIHHTLI AIANHHFP AIANHHCC AIANHHNS AITS "
                        "AITSFP AITSCC AITSNS TTRACT TBLKGRP ANRC ANRCCC ANRCNS CBSA MEMI CSA METDIV NECTA NMEMI CNECTA NECTADIV "
                        "CBSAPCI NECTAPCI UA UATYPE UR CD116 CD118 CD119 CD120 CD121 SLDU18 SLDU22 SLDU24 SLDU26 SLDU28 SLDL18 "
                        "SLDL22 SLDL24 SLDL26 SLDL28 VTD VTDI ZCTA SDELM SDSEC SDUNI PUMA AREALAND AREAWATR BASENAME NAME FUNCSTAT "
                        "GCUNI POP100 HU100 INTPTLAT INTPTLON LSADC PARTFLAG UGA".split())
DEC_INTEGERS = {DEC_GEO_COLUMNS.index(c) for c in ("AREALAND", "AREAWATR", "POP100", "HU100")}
DEC_LEADING = ("FILEID", "STUSAB", "CHARITER", "CIFSN", "LOGRECNO")
# state, county, county subdivision, tract, block group, place, AIANNH, metro and combined area parts, 119th-Congress
# and 2024 legislative districts, ZCTA (DHC), unified school district
DEC_LEVELS = ("040", "050", "060", "140", "150", "160", "280", "320", "340", "500", "610", "620", "871", "970")
DEC_GEOGRAPHY_ONLY = {"pl": ("750",)}   # PL blocks: geography rows (POP100, HU100) without cell values
DEC_ITERATIONS = "ABCDEFGHI"            # race and Hispanic-origin iterations kept; None keeps every table, "" none
DEC_ITERATIONS_SKIP = ("PCT12",)        # single-year age by sex: 9 iterations of 209 cells
DEC_RECHECK_DAYS = 365
DEC_ZIP_LIMIT, DEC_META_LIMIT = 1_000_000_000, 32_000_000
DEC_GEO_COLUMNS_SQL = ", ".join(c.lower() + (" INTEGER" if i in DEC_INTEGERS else " TEXT") for i, c in enumerate(DEC_GEO_COLUMNS))
DEC_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_census_decennial_values (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, product TEXT NOT NULL, vintage INTEGER NOT NULL, table_id TEXT NOT NULL,
  geoid TEXT NOT NULL, variable TEXT NOT NULL, value NUMERIC, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_decennial_values_geo ON kfm_census_decennial_values(geoid, table_id);
CREATE TABLE IF NOT EXISTS kfm_census_decennial_geographies (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, product TEXT NOT NULL, vintage INTEGER NOT NULL,
  {DEC_GEO_COLUMNS_SQL},
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_decennial_geographies_geo ON kfm_census_decennial_geographies(geoid, product);
CREATE TABLE IF NOT EXISTS kfm_census_decennial_variables (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, product TEXT NOT NULL, vintage INTEGER NOT NULL, table_id TEXT NOT NULL,
  variable TEXT NOT NULL, segment INTEGER NOT NULL, position INTEGER NOT NULL, label TEXT, title TEXT, universe TEXT,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_census_decennial_variables_id ON kfm_census_decennial_variables(variable, product);
"""
XL = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
XL_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
FIELD = re.compile(r"(PCT|PCO|HCT|P|H)\d{2,3}[A-Z0-9]+")
PL_TITLE = re.compile(r"([A-Z]+\d+[A-Z]*)\. (.+?)(?: \[\d+\])?")


def _xlsx(body: bytes, name: str) -> dict[str, list[dict[str, str]]]:
    """Sheet name -> rows ({column letter: text}) of a workbook, read with the standard library."""
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as z:
            shared = ([] if "xl/sharedStrings.xml" not in z.namelist() else
                      ["".join(t.text or "" for t in si.iter(XL + "t")) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(XL + "si")])
            targets = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
            sheets = {}
            for sheet in ET.fromstring(z.read("xl/workbook.xml")).iter(XL + "sheet"):
                target = targets[sheet.get(XL_ID)]
                rows = []
                for row in ET.fromstring(z.read(target.lstrip("/") if target.startswith("/") else "xl/" + target)).iter(XL + "row"):
                    cells = {}
                    for c in row.iter(XL + "c"):
                        v, kind = c.find(XL + "v"), c.get("t")
                        cells[re.match(r"[A-Z]+", c.get("r")).group()] = (
                            "".join(t.text or "" for t in c.iter(XL + "t")) if kind == "inlineStr" else
                            "" if v is None else shared[int(v.text)] if kind == "s" else v.text or "")
                    rows.append(cells)
                sheets[sheet.get("name")] = rows
            return sheets
    except (zipfile.BadZipFile, KeyError, ET.ParseError, IndexError, ValueError, AttributeError, TypeError) as error:
        raise FeedError(f"DEC_LAYOUT_UNREADABLE {name}: {error}") from None


def _pl_fields(sheets) -> list[tuple]:
    """[(segment, table, variable, label, title, universe)] in file order, from the PL field-names workbook."""
    found, info = [], {}
    for sheet, rows in sheets.items():
        m = re.fullmatch(r"2020 P\.L\. Segment (\d+) Definitions", sheet)
        table = None
        for r in rows[1:] if m else []:
            name, notes = r.get("B", "").strip(), r.get("F", "").strip()
            if title := PL_TITLE.fullmatch(notes):
                table = title.group(1)
                info[table] = [title.group(2), None]
            elif notes.startswith("Universe:") and table:
                info[table][1] = notes[9:].strip()
            elif notes and table and info[table][1] is None:   # a title that wraps onto the next row
                info[table][0] = re.sub(r"\s*\[\d+\]$", "", f"{info[table][0]} {notes}")
            if FIELD.fullmatch(name):
                if table is None:
                    raise FeedError(f"DEC_LAYOUT_CHANGED pl {name}")
                found.append((int(m.group(1)), table, name, r.get("A", "").strip()))
    if not found:
        raise FeedError("DEC_LAYOUT_CHANGED pl")
    return [(seg, table, name, label, *info[table]) for seg, table, name, label in found]


def _dhc_fields(sheets) -> list[tuple]:
    """The same from the DHC table matrix: its fields in each table, its Table_Segments for the table order."""
    if "DHC Table Matrix" not in sheets or "DHC Table_Segments" not in sheets:
        raise FeedError("DEC_LAYOUT_CHANGED dhc sheets")
    order, cells, info = {}, {}, {}
    for r in sheets["DHC Table_Segments"][1:]:
        if table := r.get("A", "").strip():
            order[table] = (int(float(r["B"])), int(float(r["D"])), int(float(r["C"])))
    for r in sheets["DHC Table Matrix"]:
        table, name, text = r.get("B", "").strip(), r.get("C", "").strip(), r.get("F", "").strip()
        if not table or table == "Table number":
            continue
        if FIELD.fullmatch(name):
            cells.setdefault(table, []).append((name, text, int(float(r["D"]))))
        elif text.startswith("Universe:"):
            info.setdefault(table, [None, None])[1] = text[9:].strip()
        elif text and info.get(table, [None])[0] is None and table not in cells:
            info.setdefault(table, [None, None])[0] = re.sub(r"\s*\[\d+\]$", "", text)
    if not order or set(cells) != set(order):
        raise FeedError("DEC_LAYOUT_CHANGED dhc tables")
    # The crosswalk sheet names each table too; it fills a title row the matrix left without its table number.
    crosswalk = {r.get("A", "").strip(): r.get("C", "").strip() for r in sheets.get("DHC Table ID Crosswalk", [])}
    fields = []
    for table, (seg, _, total) in sorted(order.items(), key=lambda item: item[1][:2]):
        if len(cells[table]) != total or any(s != seg for _, _, s in cells[table]):
            raise FeedError(f"DEC_LAYOUT_CHANGED dhc {table}")
        title, universe = info.get(table, [None, None])
        fields += [(seg, table, name, label, title or crosswalk.get(table) or None, universe) for name, label, _ in cells[table]]
    return fields


def _dec_selected(table: str) -> bool:
    base, suffix = re.fullmatch(r"([A-Z]+\d+)([A-Z]*)", table).groups()
    return not suffix or DEC_ITERATIONS is None or (len(suffix) == 1 and suffix in DEC_ITERATIONS and base not in DEC_ITERATIONS_SKIP)


def _dec_signature() -> str:
    return core.sha256(core.canonical([DEC_LEVELS, DEC_GEOGRAPHY_ONLY, DEC_ITERATIONS, DEC_ITERATIONS_SKIP]).encode())[:16]


def _dec_geo_cut(z, product: str, fileid: bytes, kept_path: Path) -> tuple[int, dict]:
    """Kept geography lines, with a header row; returns (lines kept, LOGRECNO -> GEOID of the geographies with values)."""
    member, kept, with_values = f"ksgeo2020.{product}", 0, {}
    extra = DEC_GEOGRAPHY_ONLY.get(product, ())
    try:
        src = z.open(member)
    except KeyError:
        raise FeedError(f"DEC_MEMBER_MISSING {member}") from None
    with src, _gz_out(kept_path) as out:
        out.write(("|".join(DEC_GEO_COLUMNS) + "\n").encode())
        for line in src:
            p = line.rstrip(b"\r\n").split(b"|")
            if len(p) != len(DEC_GEO_COLUMNS) or p[0] != fileid or p[1] != b"KS":
                raise FeedError(f"DEC_GEO_COLUMNS_CHANGED {member}")
            level = p[2].decode("latin-1")
            if p[4] != b"00" or (level not in DEC_LEVELS and level not in extra):
                continue
            if level in DEC_LEVELS:
                with_values[p[7].decode("latin-1")] = _text(p[8])
            out.write(line)
            kept += 1
    return kept, with_values


def _dec_geo_rows(product: str):
    def rows(path: Path):
        lines = _cut_rows(path)
        if next(lines) != list(DEC_GEO_COLUMNS):
            raise FeedError(f"DEC_GEO_COLUMNS_CHANGED {path.name}")
        for p in lines:
            yield (product, 2020, *(int(v) if i in DEC_INTEGERS and v.isdigit() else v for i, v in enumerate(p)))
    return rows


def _dec_segment_cut(z, member: str, fileid: bytes, seg: int, names: list[str], keep: list[int], logrecnos: set[bytes],
                     kept_path: Path) -> int:
    """The selected cells of the kept geographies, with a header row."""
    width, cifsn, kept = len(DEC_LEADING) + len(names), f"{seg:02d}".encode(), 0
    try:
        src = z.open(member)
    except KeyError:
        raise FeedError(f"DEC_MEMBER_MISSING {member}") from None
    with src, _gz_out(kept_path) as out:
        out.write(("|".join([*DEC_LEADING, *(names[i] for i in keep)]) + "\n").encode())
        for line in src:
            if line.count(b"|") != width - 1:
                raise FeedError(f"DEC_COLUMNS_CHANGED {member}")
            p = line.rstrip(b"\r\n").split(b"|")
            if p[0] != fileid or p[1] != b"KS" or p[3] != cifsn:
                raise FeedError(f"DEC_COLUMNS_CHANGED {member}")
            if p[4] in logrecnos:
                out.write(b"|".join([*p[:5], *(p[5 + i] for i in keep)]) + b"\n")
                kept += 1
    return kept


def _dec_value_rows(product: str, geo: dict, tables: dict):
    def rows(path: Path):
        lines = _cut_rows(path)
        names = next(lines)[len(DEC_LEADING):]
        for p in lines:
            geoid = geo[p[4]]
            for name, value in zip(names, p[len(DEC_LEADING):]):
                yield (product, 2020, tables[name], geoid, name, _num(value))
    return rows


def _dec_product(ctx, db, state: dict, product: str, summary: dict, budget: dict) -> dict:
    zip_url, layout_url, fileid = DEC_SOURCES[product]
    ps, signature = state.setdefault(product, {}), _dec_signature()
    recheck = _days_since(ctx, ps.get("checked"))
    if ps.get("complete") and ps.get("selection") == signature and recheck is not None and recheck < DEC_RECHECK_DAYS:
        return state
    if budget["segments"] <= 0:
        summary["pending"].append(product)
        return state
    meta = ctx.fetch(layout_url, limit=DEC_META_LIMIT, timeout=300)
    try:
        fields = (_pl_fields if product == "pl" else _dhc_fields)(_xlsx(meta.body, layout_url.rsplit("/", 1)[1]))
    except (KeyError, ValueError, IndexError) as error:
        raise FeedError(f"DEC_LAYOUT_CHANGED {product}: {error}") from None
    archive, work = core.temp_path(ctx, f"census-{product}2020.zip"), core.temp_path(ctx, f"census-{product}2020-cut.gz")
    try:
        fetched = core.download(ctx, zip_url, archive, limit=DEC_ZIP_LIMIT, timeout=1800)
        zip_sha = core.file_sha256(archive)
        if not zipfile.is_zipfile(archive):
            raise FeedError(f"DEC_ZIP_UNREADABLE {product}")
        if ps.get("zip_sha256") != zip_sha or ps.get("selection") != signature:
            ps.update(zip_sha256=zip_sha, selection=signature, segments_done=[], complete=False, last_modified=fetched.last_modified)
        if ps["complete"]:
            ps["checked"] = str(ctx.now().date())
            summary["unchanged"].append(product)
            return _save(ctx, db, "census-decennial", state)
        stem = f"{product}2020"
        segments, position = {}, {}
        for seg, table, name, *_ in fields:
            segments.setdefault(seg, []).append((table, name))
        labels = []
        for seg, table, name, label, title, universe in fields:
            position[seg] = position.get(seg, 0) + 1
            labels.append((product, 2020, table, name, seg, position[seg], label or None, title, universe))
        key = f"{stem}/labels"
        path, digest = core.store_raw(ctx, "census-decennial", f"{stem}/{layout_url.rsplit('/', 1)[1][:-5]}-{core.sha256(meta.body)[:12]}.xlsx",
                                      meta.body, url=meta.url, fetched=meta, extra={"key": key, "fields": len(labels)})
        with core.pipeline_lock(ctx):
            summary["variables"] += core.load_version(db, ctx, source_id=f"census-{stem}-labels", key=key, path=path, digest=digest,
                                                      url=meta.url, table="kfm_census_decennial_variables", rows=labels, width=9)["rows"]
        with zipfile.ZipFile(archive) as z:
            kept, geo = _dec_geo_cut(z, product, fileid, work)
            if not geo:
                raise FeedError(f"DEC_KANSAS_EMPTY {stem}")
            key = f"{stem}/geo"
            path, digest = core.store_raw(ctx, "census-decennial", f"{stem}/kansas-ksgeo2020.{product}-{core.file_sha256(work)[:12]}.txt.gz",
                                          work, url=fetched.url, fetched=fetched, original=archive,
                                          extra={"key": key, "member": f"ksgeo2020.{product}", "kansas_rows": kept, "levels": DEC_LEVELS})
            with core.pipeline_lock(ctx):
                summary["geographies"] += core.load_version(db, ctx, source_id=f"census-{stem}-geo", key=key, path=path, digest=digest,
                                                            url=fetched.url, table="kfm_census_decennial_geographies",
                                                            rows=_dec_geo_rows(product)(path), width=len(DEC_GEO_COLUMNS) + 2)["rows"]
            logrecnos, tables = {g.encode() for g in geo}, {name: table for _, table, name, *_ in fields}
            for seg in sorted(segments):
                if seg in ps["segments_done"]:
                    continue
                cells = segments[seg]
                keep = [i for i, (table, _) in enumerate(cells) if _dec_selected(table)]
                member, key, kept = f"ks{seg:05d}2020.{product}", f"{stem}/segment-{seg:02d}", 0
                if keep:
                    if budget["segments"] <= 0:
                        break
                    budget["segments"] -= 1
                    kept = _dec_segment_cut(z, member, fileid, seg, [n for _, n in cells], keep, logrecnos, work)
                    if kept:
                        path, digest = core.store_raw(ctx, "census-decennial", f"{stem}/kansas-{member}-{core.file_sha256(work)[:12]}.txt.gz",
                                                      work, url=fetched.url, fetched=fetched, original=archive,
                                                      extra={"key": key, "member": member, "kansas_rows": kept,
                                                             "tables": sorted({cells[i][0] for i in keep})})
                        with core.pipeline_lock(ctx):
                            result = core.load_version(db, ctx, source_id=f"census-{stem}-segment", key=key, path=path, digest=digest,
                                                       url=fetched.url, table="kfm_census_decennial_values",
                                                       rows=_dec_value_rows(product, geo, tables)(path), width=6)
                        summary["segments" if result["state"] == "loaded" else "unchanged"].append(key)
                        summary["rows"] += result["rows"]
                if not kept:
                    # Nothing of this segment is selected now: values an earlier selection loaded go with it.
                    with core.pipeline_lock(ctx):
                        if _retire(db, source_id=f"census-{stem}-segment", key=key, table="kfm_census_decennial_values"):
                            summary["retired"].append(key)
                ps["segments_done"].append(seg)
                state = _save(ctx, db, "census-decennial", state)
        if set(segments) <= set(ps["segments_done"]):
            ps.update(complete=True, checked=str(ctx.now().date()))
        else:
            summary["pending"].append(product)
        return _save(ctx, db, "census-decennial", state)
    finally:
        archive.unlink(missing_ok=True)
        work.unlink(missing_ok=True)


def census_decennial(ctx, max_segments: int = 24) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(DEC_SCHEMA)
        state = core.get_state(db, "census-decennial")
        summary = {"segments": [], "unchanged": [], "retired": [], "pending": [], "rows": 0, "geographies": 0, "variables": 0}
        budget = {"segments": max_segments}
        for product in DEC_SOURCES:
            state = _dec_product(ctx, db, state, product, summary, budget)
        return {**summary, "complete": [p for p in DEC_SOURCES if state.get(p, {}).get("complete")]}
    finally:
        db.close()


# --- EIA State Energy Data System -------------------------------------------------------------------------------

SEDS_URL = "https://www.eia.gov/opendata/bulk/SEDS.zip"
SEDS_MANIFEST = "https://www.eia.gov/opendata/bulk/manifest.txt"
SEDS_SERIES = ("series_id", "name", "units", "f", "description", "copyright", "source", "iso3166", "geography", "start", "end",
               "last_updated", "geoset_id")
SEDS_LIMIT = 200_000_000
SEDS_SERIES_SQL = ", ".join('"' + c + '" TEXT' for c in SEDS_SERIES)
SEDS_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS kfm_eia_seds_series (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {SEDS_SERIES_SQL},
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_eia_seds_series_id ON kfm_eia_seds_series(series_id);
CREATE TABLE IF NOT EXISTS kfm_eia_seds_values (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, series_id TEXT NOT NULL, period TEXT NOT NULL, value NUMERIC,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_eia_seds_values_series ON kfm_eia_seds_values(series_id, period);
CREATE TABLE IF NOT EXISTS kfm_eia_seds_categories (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, category_id TEXT NOT NULL, parent_category_id TEXT, name TEXT, notes TEXT,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS kfm_eia_seds_category_series (
  file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, category_id TEXT NOT NULL, series_id TEXT NOT NULL,
  PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS kfm_eia_seds_category_series_id ON kfm_eia_seds_category_series(series_id);
"""


def _seds_cut(archive: Path, kept_path: Path) -> tuple[list, list, list, list]:
    """Kansas series and every category line, byte for byte; returns (series, values, categories, category series)."""
    series, values, categories, children = [], [], [], []
    try:
        z = zipfile.ZipFile(archive)
        src = z.open("SEDS.txt")
    except (zipfile.BadZipFile, KeyError):
        raise FeedError("SEDS_FORMAT_CHANGED") from None
    with z, src, _gz_out(kept_path) as out:
        for n, line in enumerate(src, 1):
            try:
                item = json.loads(line)
            except ValueError:
                raise FeedError(f"SEDS_FORMAT_CHANGED line {n}") from None
            if "series_id" in item:
                if {"series_id", "name", "units", "data"} - item.keys() or not isinstance(item["data"], list):
                    raise FeedError(f"SEDS_COLUMNS_CHANGED {item.get('series_id')}")
                parts = str(item["series_id"]).split(".")
                kansas = item.get("geography") == "USA-KS"
                if kansas != (len(parts) == 4 and parts[2] == "KS"):
                    raise FeedError(f"SEDS_STATE_MISMATCH {item['series_id']}")
                if not kansas:
                    continue
                out.write(line)
                series.append(tuple(item.get(c) for c in SEDS_SERIES))
                for point in item["data"]:
                    if not isinstance(point, list) or len(point) != 2:
                        raise FeedError(f"SEDS_COLUMNS_CHANGED {item['series_id']}")
                    values.append((item["series_id"], str(point[0]), point[1]))
            elif "category_id" in item:
                out.write(line)
                categories.append((str(item["category_id"]), item.get("parent_category_id"), item.get("name"), item.get("notes")))
                children += [(str(item["category_id"]), sid) for sid in item.get("childseries") or []]
    kansas_ids = {s[0] for s in series}
    return series, values, categories, [c for c in children if c[1] in kansas_ids]


def eia_seds(ctx, min_days: int = 30) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(SEDS_SCHEMA)
        state = core.get_state(db, "eia-seds")
        try:
            updated = json.loads(ctx.fetch(SEDS_MANIFEST, limit=4_000_000).body)["dataset"]["SEDS"]["last_updated"]
        except (ValueError, KeyError, TypeError):
            raise FeedError("SEDS_MANIFEST_CHANGED") from None
        checked = _days_since(ctx, state.get("checked"))
        if updated == state.get("last_updated") and checked is not None and checked < min_days:
            return {"state": "current", "last_updated": updated, "checked": state["checked"]}
        archive, kept_path = core.temp_path(ctx, "SEDS.zip"), core.temp_path(ctx, "SEDS-kansas.txt.gz")
        try:
            fetched = core.download(ctx, SEDS_URL, archive, limit=SEDS_LIMIT, timeout=900)
            series, values, categories, members = _seds_cut(archive, kept_path)
            if not series:
                raise FeedError("SEDS_KANSAS_EMPTY")
            path, digest = core.store_raw(ctx, "eia-seds", f"seds/kansas-SEDS-{core.file_sha256(kept_path)[:12]}.txt.gz", kept_path,
                                          url=fetched.url, fetched=fetched, original=archive,
                                          extra={"key": "SEDS", "manifest_last_updated": updated, "kansas_series": len(series),
                                                 "kansas_values": len(values)})
            with core.pipeline_lock(ctx):
                result = _replace(db, ctx, source_id="eia-seds", key="SEDS", path=path, digest=digest, url=fetched.url,
                                  tables=[("kfm_eia_seds_series", len(SEDS_SERIES), series), ("kfm_eia_seds_values", 3, values),
                                          ("kfm_eia_seds_categories", 4, categories), ("kfm_eia_seds_category_series", 2, members)])
                state = {**state, "last_updated": updated, "checked": str(ctx.now().date()), "last_modified": fetched.last_modified}
                core.set_state(db, ctx, "eia-seds", state)
        finally:
            archive.unlink(missing_ok=True)
            kept_path.unlink(missing_ok=True)
        return {**result, "series": len(series), "values": len(values), "last_updated": updated}
    finally:
        db.close()
