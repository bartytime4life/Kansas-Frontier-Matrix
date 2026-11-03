"""Deep-time SQL feeds: PBDB fossils, Macrostrat columns, p3k14c radiocarbon dates, Neotoma paleoecology and iDigBio fossils.

A rewrite (2026-11-03) of the lost ``sql_feed_prehistory`` module against the data its feeds left on the data volume:
the same tables (DDL copied column for column), the same receipt keys and ``extra`` fields, the same kept-file names
and the same feed-state fields, so the existing loads are recognized as loaded and nothing is downloaded twice.
Every kept copy is a canonical cut of the provider's answer (sorted canonical JSON lines, or a CSV re-serialized
with minimal quoting), named ``<name>-<sha12><ext>``, so an unchanged answer is the same kept file and
``load_version`` does not load it again; a changed one replaces the loaded version in one transaction (several
tables at once where a source file feeds more than one, with ``load_tables``). Network work runs outside the
pipeline lock, database writes inside it. Checked against the kept files: the PBDB CSVs, the Macrostrat column
and unit files, the p3k14c cut, every Neotoma list and download and the iDigBio segments re-parse to the row
counts recorded in ``kfm_sql_sources``.

``pbdb``: the Paleobiology Database data service (https://paleobiodb.org/data1.2/; data CC0 1.0 per the service's
datainfo, https://creativecommons.org/publicdomain/zero/1.0/), four CSV downloads of everything in Kansas
(``state=Kansas&cc=US``, ``vocab=pbdb``, ``limit=all``, ``rowcount``): collections (``colls/list``, 1,923 on
2026-11-03), occurrences (``occs/list``, 12,826), the taxa of those occurrences (``occs/taxa``, 3,565) and their
references (``occs/refs``, 2,060). PBDB answers with a four-line count block before the header; the feed checks
that "Records Found" equals "Records Returned" and the rows parsed, keeps the rows re-serialized (header included,
duplicate ``cc``/``formation`` columns and all) and loads them under one key per file (``collections``,
``occurrences``, ``taxa``, ``references``). Ma ages and coordinates are REAL; everything else is PBDB's text. The
header must still start with the table's columns (``PBDB_COLUMNS_CHANGED``). Checked every 6 days; PBDB revises
continuously, so a weekly timer refreshes all four files (about 13 MB).

``macrostrat``: Macrostrat (https://macrostrat.org/api/v2/; CC-BY 4.0; Peters, Husson and Czaplewski 2018,
doi:10.1029/2018GC007467). Each check reads every column's outline (``columns?all&format=geojson``, 1.3 MB) and
takes the columns whose polygon's bounding box overlaps Kansas (36.993-40.003 N, 102.051-94.588 W): 18 on
2026-11-03, project 1 "North America", three of them Oklahoma and Texas Panhandle columns that reach over the
line. Then ``columns?col_id=...&format=geojson&response=long`` (kept as one canonical feature per line, by col_id;
key ``columns``) and ``units?col_id=...&response=long`` (kept as ``{"refs": ..., "units": [...]}`` canonical; key
``units``, loading ``kfm_macrostrat_units`` and ``kfm_macrostrat_refs`` from the one file). Nested lists (lith,
environ, econ, refs, measure, units above and below) are stored as canonical JSON text. Checked every 6 days.

``radiocarbon``: p3k14c (Bird et al. 2022, Scientific Data 9:27, doi:10.1038/s41597-022-01118-7; data CC0 1.0
with attribution requested per the README, code MIT), the ``inst/p3k14c_scrubbed_fuzzed.csv`` file of
https://github.com/people3k/p3k14c. The GitHub commits API names the newest commit touching the file; the file is
fetched at that commit (raw.githubusercontent.com, 25.9 MB, streamed to a temp file) only when the commit changed.
Kansas rows: ``Province`` is Kansas (``kansas_basis`` "province"), or the fuzzed coordinates fall inside a 2025
TIGER Kansas county (``ctx.tiger``; "coordinates"; 6 rows with no province on 2026-11-03). ``county_geoid`` is the
county holding the point. The coordinates are deliberately fuzzed for site protection and are kept as published,
``LocAccuracy`` with them. Key ``p3k14c-scrubbed-fuzzed``; checked every 6 days (the last commit was 2022-06-10).

``neotoma``: the Neotoma Paleoecology Database API (https://api.neotomadb.org/v2.0/; CC BY 4.0,
https://www.neotomadb.org/data/data-use-and-embargo-policy; Williams et al. 2018, Quaternary Research 89:156-177).
Kansas is geopolitical unit 7034. Two lists are kept as canonical JSON lines: the sites
(``geopoliticalunits/7034/sites``, 142 sites with their collection units; key ``sites``, loading
``kfm_neotoma_sites`` and ``kfm_neotoma_collection_units``, the units merged by id with their datasets) and the
datasets (``datasets?gpid=7034``, 226 datasets on 172 collection units; key ``datasets``). Then each dataset's
download (``downloads/<id>``, kept canonical; key ``dataset/<id>``) loads one ``kfm_neotoma_dataset_summaries``
row, a ``kfm_neotoma_samples`` row per datum, a ``kfm_neotoma_sample_ages`` row per sample age and, for each
chronology, a ``kfm_neotoma_chron_controls`` row per control (one row with empty control columns when the
chronology has none); Neotoma's all-null placeholders are not rows. The lists are re-read every 6 days; a dataset
new to the list is downloaded on the next run (``NEOTOMA_DOWNLOADS_PER_RUN`` a run, so the first load took one
run), one loaded before is downloaded again after ``NEOTOMA_REFRESH_DAYS`` (180), and a dataset that left the list
is retired. Feed state: ``datasets`` (the listed ids), ``fetched`` (id: date) and ``lists_checked``.

``idigbio-fossils``: iDigBio's search API (https://search.idigbio.org/v2/; https://www.idigbio.org/terms; rights
vary by recordset and record, so each recordset's ``data_rights`` and each record's license, rights and access
rights are kept). Kansas fossil specimens (``basisofrecord`` fossilspecimen) are the records whose indexed
``stateprovince`` is one of the 21 Kansas spellings iDigBio's index held on 2026-11-03 (``KANSAS_STATEPROVINCE``;
"arkansas" is not among them): 279,643 records in 51 recordsets. They are loaded in segments so each pages
reliably: one per indexed ``county`` value (``summary/top/records``, key ``county/<value>``; a value over
``IDIGBIO_SEGMENT_MAX`` records is split by recordset, key ``county/<value>/recordset/<uuid>``) and one for the
records with no county (``county-missing``). A segment is paged by uuid order and a uuid range (keyset, 5,000 a
page), kept as canonical JSON lines (uuid, etag, data, indexTerms) under
``segments/<slug>-<sha256(key)[:8]>/idigbio-fossils-<sha12>.jsonl.gz``, and loaded whole. Each run continues the
sweep in ``pending`` ([key, query, count] in key order) until about ``IDIGBIO_RECORDS_PER_RUN`` (50,000) records or
``IDIGBIO_REQUESTS_PER_RUN`` requests, saving state after every segment, so an interrupted backfill resumes: the
2026-11-03 state (232,476 of 279,643 records loaded, 103 segments pending) is consumed as it is. When the sweep is
done a new one starts after ``IDIGBIO_RESWEEP_DAYS`` (28): the recordsets list (the ``attribution`` block of a
one-record search; key ``recordsets``) is kept again and every segment whose count changed, or whose copy is older
than ``IDIGBIO_REFRESH_DAYS``, is queued; segments the summary no longer lists are retired. iDigBio has said it
is winding down and its site already redirects to GBIF: an answer that is not the API's JSON stops the run with
``IDIGBIO_API_GONE`` rather than looping. The recordsets list kept on 2026-11-03 came from the same attribution
block; should iDigBio's ordering of its fields have changed, the first rebuilt run supersedes it once.
"""
from __future__ import annotations

import csv
from datetime import date
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import time
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import (age_days, county_at, csv_bytes, kansas_counties, keep_version, loaded_keys, number,
                                               retire, save_state, snake)
from tools.local_data.sql_feeds import FeedError

# --- Shared ----------------------------------------------------------------------------------------

KANSAS_BOX = (-102.051, 36.993, -94.588, 40.003)   # west, south, east, north
PAUSE = 0.5                                        # seconds between requests to one provider (ctx.pause overrides)


def columns(spec: str) -> list[tuple[str, str]]:
    """[(name, type)] from "name[:TYPE[!]] ...": TEXT by default, ! for NOT NULL."""
    out = []
    for token in spec.split():
        name, _, kind = token.partition(":")
        out.append((name, (kind.rstrip("!") or "TEXT") + (" NOT NULL" if kind.endswith("!") else "")))
    return out


def table_ddl(table: str, cols: list[tuple[str, str]], indexes=()) -> str:
    """The existing tables' DDL, character for character: quoted column names, PRIMARY KEY(file_id, row_number)."""
    body = ", ".join(f'"{name}" {kind}' for name, kind in cols)
    return (f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, "
            f"PRIMARY KEY(file_id, row_number));\n"
            + "".join(f"CREATE INDEX IF NOT EXISTS {table}_{'_'.join(i)} ON {table}({', '.join(chr(34) + c + chr(34) for c in i)});\n"
                      for i in indexes))


def jtext(value):
    """A nested value as canonical JSON text; None stays NULL."""
    return None if value is None else core.canonical(value)


def flag(value):
    """A provider's boolean as "1"/"0" text; None stays NULL."""
    return None if value is None else ("1" if value is True else "0" if value is False else str(value))


def nonnull(value) -> bool:
    """Whether a provider's placeholder record holds any value at all."""
    if isinstance(value, dict):
        return any(nonnull(v) for v in value.values())
    if isinstance(value, list):
        return any(nonnull(v) for v in value)
    return value is not None


def rings(geometry) -> list:
    if geometry["type"] == "Polygon":
        return geometry["coordinates"]
    if geometry["type"] == "MultiPolygon":
        return [ring for polygon in geometry["coordinates"] for ring in polygon]
    if geometry["type"] == "Point":
        return [[geometry["coordinates"]]]
    raise FeedError(f"GEOMETRY_TYPE_UNSUPPORTED {geometry['type']}")


def bbox(geometry) -> tuple:
    xs = [x for ring in rings(geometry) for x, _ in ring]
    ys = [y for ring in rings(geometry) for _, y in ring]
    return (min(xs), min(ys), max(xs), max(ys))


def in_kansas_box(lon: float, lat: float) -> bool:
    west, south, east, north = KANSAS_BOX
    return west <= lon <= east and south <= lat <= north


def json_body(ctx, url: str, code: str, *, limit: int = 64_000_000, timeout: int = 300):
    """GET url and parse it as JSON; anything else is <code>_RESPONSE_SHAPE. Returns (payload, fetched)."""
    fetched = ctx.fetch(url, limit=limit, timeout=timeout)
    try:
        return json.loads(fetched.body), fetched
    except ValueError:
        raise FeedError(f"{code}_RESPONSE_SHAPE {url[:120]}") from None


def pause(ctx) -> None:
    time.sleep(getattr(ctx, "pause", PAUSE))


def load_tables(db, ctx, *, source_id: str, key: str, path: Path, digest: str, url: str, tables) -> dict:
    """``load_version`` for a source file that feeds several tables: tables is [(table, rows, width)]; each
    table numbers its rows from 1 and ``imported_rows`` is their total. The version loaded before is replaced in
    every table in the one transaction; a return to a version loaded before (A, B, then A) is reinstated from its
    kept copy under its old file_id. Lock held."""
    receipt = core.receipt_for(ctx, path)
    if receipt.get("key") != key:
        raise FeedError(f"RECEIPT_KEY_MISMATCH {key}")
    previous = db.execute("SELECT file_id, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                          "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()
    if digest in {sha for _, sha in previous}:
        return {"state": "unchanged", "rows": 0, "superseded": 0}
    old = db.execute("SELECT file_id FROM kfm_sql_sources WHERE sha256=? AND source_id=? AND state='superseded' "
                     "AND json_extract(receipt_json,'$.key')=?", (digest, source_id, key)).fetchone()
    if old is None:
        if core.loaded(db, digest):
            raise FeedError(f"SOURCE_CONTENT_SHARED {key}")
        file_id = core.begin_source(db, ctx, source_id, path, digest, url, receipt)
    else:
        core.guard(ctx)
        db.execute("BEGIN IMMEDIATE")
        file_id = old[0]
    try:
        for previous_id, _ in previous:
            for table, _, _ in tables:
                db.execute(f"DELETE FROM {table} WHERE file_id=?", (previous_id,))
            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (previous_id,))
        total = 0
        for table, rows, width in tables:
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
        db.execute("UPDATE kfm_sql_sources SET imported_rows=?, state='complete' WHERE file_id=?", (total, file_id))
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"state": "loaded" if old is None else "reinstated", "rows": total, "superseded": len(previous)}


def keep_tables(ctx, db, *, feed: str, source_id: str, key: str, name: str, ext: str, body, url: str, tables, fetched=None,
                original=None, extra: dict | None = None) -> dict:
    """``keep_version`` for several tables: tables(path) gives [(table, rows, width)] from the kept copy."""
    digest = core.file_sha256(body) if isinstance(body, Path) else core.sha256(body)
    path, digest = core.store_raw(ctx, feed, f"{name}-{digest[:12]}{ext}", body, url=url, fetched=fetched, original=original,
                                  extra={"key": key, **(extra or {})})
    with core.pipeline_lock(ctx):
        return load_tables(db, ctx, source_id=source_id, key=key, path=path, digest=digest, url=url, tables=tables(path))


def retire_all(db, source_id: str, key: str, tables) -> int:
    """``retire`` across the tables a source file feeds. Lock held."""
    db.execute("BEGIN IMMEDIATE")
    try:
        previous = db.execute("SELECT file_id FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                              "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()
        for (file_id,) in previous:
            for table in tables:
                db.execute(f"DELETE FROM {table} WHERE file_id=?", (file_id,))
            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (file_id,))
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return len(previous)


def jsonl_lines(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


def jsonl_bytes(records) -> bytes:
    return core.gz("".join(core.canonical(r) + "\n" for r in records).encode())


# --- PBDB: four Kansas downloads, one version each ---------------------------------------------------

PBDB = "https://paleobiodb.org/data1.2/"
PBDB_QUERY = "state=Kansas&cc=US&vocab=pbdb&limit=all&rowcount"
PBDB_CITATION = "The Paleobiology Database (https://paleobiodb.org/), with the primary references of the records used"
PBDB_LICENSE = "CC0 1.0 (PBDB data service datainfo; https://creativecommons.org/publicdomain/zero/1.0/)"
PBDB_RECHECK_DAYS = 6
PBDB_COLUMNS = {
    "collections": columns(
        "collection_no record_type authorization release_on formation lng:REAL lat:REAL collection_name container_no collection_aka "
        "n_occs early_interval late_interval max_ma:REAL min_ma:REAL reference_no cc state county latlng_basis latlng_precision "
        "altitude_value altitude_unit geogscale geogcomments latdeg latmin latsec latdec latdir lngdeg lngmin lngsec lngdec lngdir "
        "gps_datum paleomodel geoplate paleoage paleolng:REAL paleolat:REAL protected cx_int_no time_bins geological_group member "
        "stratscale zone zone_type localsection localbed localbedunit localorder regionalsection regionalbed regionalbedunit "
        "regionalorder stratcomments lithdescript lithology1 lithadj1 lithification1 minor_lithology1 fossilsfrom1 lithology2 "
        "lithadj2 lithification2 minor_lithology2 fossilsfrom2 environment tectonic_setting geology_comments pres_mode "
        "preservation_quality spatial_resolution temporal_resolution lagerstatten concentration orientation abund_in_sediment "
        "sorting fragmentation bioerosion encrustation preservation_comments size_classes articulated_parts associated_parts "
        "common_body_parts rare_body_parts feed_pred_traces artifacts component_comments collection_type collection_methods museum "
        "collection_coverage collection_size rock_censused collectors collection_dates collection_comments taxonomy_comments "
        "research_group primary_reference authorizer_no enterer_no modifier_no updater_no authorizer enterer modifier updater "
        "created modified updated"),
    "occurrences": columns(
        "occurrence_no record_type reid_no flags collection_no identified_name identified_rank identified_no difference "
        "accepted_name accepted_rank accepted_no early_interval late_interval max_ma:REAL min_ma:REAL reference_no phylum phylum_no "
        "class class_no order order_no family family_no genus genus_no subgenus_no primary_name primary_reso subgenus_name "
        "subgenus_reso species_name species_reso occurrence_comments abund_value abund_unit plant_organ taxon_environment "
        "environment_basis motility motility_basis life_habit life_habit_basis vision vision_basis diet diet_basis reproduction "
        "reproduction_basis ontogeny ontogeny_basis ecospace_comments composition architecture thickness reinforcement "
        "taphonomy_basis primary_reference authorizer_no enterer_no modifier_no updater_no authorizer enterer modifier updater "
        "created modified updated"),
    "taxa": columns(
        "orig_no taxon_no record_type flags taxon_rank taxon_name taxon_attr common_name difference accepted_no accepted_rank "
        "accepted_name parent_no parent_name container_no reference_no is_extant n_occs firstapp_max_ma:REAL firstapp_min_ma:REAL "
        "lastapp_max_ma:REAL lastapp_min_ma:REAL early_interval late_interval taxon_size extant_size phylum phylum_no class class_no "
        "order order_no family family_no genus genus_no subgenus_no type_taxon type_taxon_no n_orders n_families n_genera n_species "
        "taxon_environment environment_basis motility motility_basis life_habit life_habit_basis vision vision_basis diet diet_basis "
        "reproduction reproduction_basis ontogeny ontogeny_basis ecospace_comments composition architecture thickness reinforcement "
        "taphonomy_basis primary_reference created modified updated"),
    "references": columns(
        "reference_no record_type publication_type reftitle pubyr author1init author1last author2init author2last otherauthors "
        "editors refabbr pubtitle pubabbr r_journal r_booktitle r_school publisher pubcity pubvol pubno firstpage lastpage language "
        "doi isbn ref_type formatted relevance project_name comments created modified updated"),
}
PBDB_FILES = {   # key: (service path, query additions, table, indexes)
    "collections": ("colls/list.csv", "&show=locext,paleoloc,prot,time,timebins,stratext,lithext,env,geo,ctaph,comps,methods,rem,resgroup,ref,ent,entname,crmod",
                    "kfm_pbdb_collections", (("collection_no",), ("county",), ("formation",))),
    "occurrences": ("occs/list.csv", "&show=classext,ident,rem,abund,plant,ecospace,taphonomy,etbasis,pres,ref,ent,entname,crmod",
                    "kfm_pbdb_occurrences", (("accepted_name",), ("accepted_no",), ("collection_no",))),
    "taxa": ("occs/taxa.csv", "&show=attr,app,common,parent,size,classext,subcounts,ecospace,taphonomy,etbasis,pres,ref,crmod",
             "kfm_pbdb_taxa", (("orig_no",), ("taxon_name",))),
    "references": ("occs/refs.csv", "&ref_type=occs,colls,specs,auth,class&show=both,comments,crmod",
                   "kfm_pbdb_references", (("reference_no",),)),
}
PBDB_DDL = "".join(table_ddl(table, PBDB_COLUMNS[key], indexes) for key, (_, _, table, indexes) in PBDB_FILES.items())


def pbdb_url(key: str) -> str:
    path, show, _, _ = PBDB_FILES[key]
    return f"{PBDB}{path}?{PBDB_QUERY}{show}"


def pbdb_parse(body: bytes, key: str) -> tuple[list, list]:
    """(header, rows) of a PBDB CSV answer with its rowcount block, checked against the counts it reports."""
    rows = list(csv.reader(io.StringIO(body.decode("utf-8"), newline="")))
    try:
        start = rows.index(["Records:"])
    except ValueError:
        raise FeedError(f"PBDB_RESPONSE_SHAPE {key}") from None
    counts = {r[0]: r[1] for r in rows[:start] if len(r) == 2}
    header, data = rows[start + 1], rows[start + 2:]
    if not counts.get("Records Found", "").isdigit() or counts["Records Found"] != counts.get("Records Returned") \
            or int(counts["Records Found"]) != len(data):
        raise FeedError(f"PBDB_ROWCOUNT_MISMATCH {key} {counts.get('Records Found')} found, {counts.get('Records Returned')} returned, "
                        f"{len(data)} rows")
    if any(len(r) != len(header) for r in data):
        raise FeedError(f"PBDB_ROW_SHAPE {key}")
    return header, data


def pbdb_positions(header: list, key: str) -> list[int]:
    """The header position of each table column (the first of a repeated name)."""
    wanted = [name for name, _ in PBDB_COLUMNS[key]]
    seen = {}
    for i, name in enumerate(header):
        seen.setdefault(name, i)
    if [name for name in dict.fromkeys(header)] != wanted:
        raise FeedError(f"PBDB_COLUMNS_CHANGED {key}")
    return [seen[name] for name in wanted]


def pbdb_rows(path: Path, key: str):
    reals = {name for name, kind in PBDB_COLUMNS[key] if kind == "REAL"}
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None) or []
        positions = pbdb_positions(header, key)
        for row in reader:
            if len(row) != len(header):
                raise FeedError(f"PBDB_ROW_SHAPE {key} kept")
            yield tuple(number(row[i]) if name in reals else row[i] for (name, _), i in zip(PBDB_COLUMNS[key], positions))


def pbdb(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(PBDB_DDL)
        state, today = core.get_state(db, "pbdb"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < PBDB_RECHECK_DAYS and loaded_keys(db, "pbdb-collections") >= {"collections"}:
            return {"state": "not_due", "checked": state["checked"]}
        summary, records = {"rows": 0}, dict(state.get("records", {}))
        for key, (_, _, table, _) in PBDB_FILES.items():
            fetched = ctx.fetch(pbdb_url(key), limit=256_000_000, timeout=900)
            header, data = pbdb_parse(fetched.body, key)
            pbdb_positions(header, key)
            if not data:
                raise FeedError(f"PBDB_NO_KANSAS_ROWS {key}")
            result = keep_version(ctx, db, feed="pbdb", source_id=f"pbdb-{key}", key=key, name=f"{key}/pbdb-{key}-kansas", ext=".csv.gz",
                                  body=core.gz(csv_bytes([header, *data])), url=fetched.url, fetched=fetched,
                                  extra={"citation": PBDB_CITATION, "license": PBDB_LICENSE, "records": len(data)}, table=table,
                                  width=len(PBDB_COLUMNS[key]), rows=lambda path, key=key: pbdb_rows(path, key))
            records[key] = len(data)
            summary[key] = f"{result['state']} {len(data)}"
            summary["rows"] += result["rows"]
            state = save_state(ctx, db, "pbdb", {**state, "records": records})
            pause(ctx)
        save_state(ctx, db, "pbdb", {**state, "checked": str(today)})
        return summary
    finally:
        db.close()


# --- Macrostrat: the columns over Kansas and their units ---------------------------------------------

MACROSTRAT = "https://macrostrat.org/api/v2/"
MACROSTRAT_ALL = MACROSTRAT + "columns?all&format=geojson"
MACROSTRAT_CITATION = ("Peters, S.E., Husson, J.M., Czaplewski, J. 2018. Macrostrat: a platform for geological data integration and "
                       "deep-time Earth crust research. G-cubed 19:1393-1409, doi:10.1029/2018GC007467; with the column references")
MACROSTRAT_LICENSE = "CC-BY 4.0"
MACROSTRAT_RECHECK_DAYS = 6
MACROSTRAT_JSON = {"refs", "refs_expanded", "lith", "environ", "econ", "measure", "units_above", "units_below"}
COLUMN_COLUMNS = columns(
    "col_id:INTEGER col_name col_group col_group_id:INTEGER group_col_id lat:REAL lng:REAL col_area:REAL project_id:INTEGER col_type "
    "status_code refs project_name refs_expanded t_units:INTEGER t_sections:INTEGER max_thick:REAL max_min_thick:REAL min_min_thick:REAL "
    "b_age:REAL t_age:REAL b_int_name t_int_name pbdb_collections:INTEGER lith environ econ geometry_geojson min_lon:REAL min_lat:REAL "
    "max_lon:REAL max_lat:REAL")
UNIT_COLUMNS = columns(
    "unit_id:INTEGER section_id:INTEGER col_id:INTEGER project_id:INTEGER col_area:REAL unit_name strat_name_id:INTEGER mbr fm gp sgp "
    "t_age:REAL b_age:REAL max_thick:REAL min_thick:REAL outcrop pbdb_collections:INTEGER pbdb_occurrences:INTEGER lith environ econ "
    "measure notes color text_color t_int_id:INTEGER t_int_name t_int_age:REAL t_prop:REAL units_above b_int_id:INTEGER b_int_name "
    "b_int_age:REAL b_prop:REAL units_below strat_name_long refs clat:REAL clng:REAL t_plat:REAL t_plng:REAL b_plat:REAL b_plng:REAL")
UNIT_KEYS = {"mbr": "Mbr", "fm": "Fm", "gp": "Gp", "sgp": "SGp"}
MACROSTRAT_DDL = (table_ddl("kfm_macrostrat_columns", COLUMN_COLUMNS, (("col_id",),))
                  + table_ddl("kfm_macrostrat_refs", columns("ref_id:INTEGER citation"), (("ref_id",),))
                  + table_ddl("kfm_macrostrat_units", UNIT_COLUMNS, (("col_id",), ("fm",), ("unit_id",))))
MACROSTRAT_TABLES = ("kfm_macrostrat_units", "kfm_macrostrat_refs")


def _macrostrat_data(payload, code: str):
    data = payload.get("success", {}).get("data") if isinstance(payload, dict) else None
    if data is None:
        raise FeedError(f"MACROSTRAT_RESPONSE_SHAPE {code}")
    return data


def _value(record: dict, name: str, kind: str, json_keys=MACROSTRAT_JSON):
    value = record.get(name)
    if name in json_keys:
        return jtext(value)
    if kind in ("REAL", "INTEGER") and isinstance(value, str):
        return number(value)
    return value


def macrostrat_column_rows(path: Path):
    for feature in jsonl_lines(path):
        p, geometry = feature["properties"], feature["geometry"]
        west, south, east, north = bbox(geometry)
        yield (*(_value(p, name, kind) for name, kind in COLUMN_COLUMNS[:-5]), core.canonical(geometry), west, south, east, north)


def macrostrat_unit_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        kept = json.load(handle)
    for unit in kept["units"]:
        yield tuple(_value(unit, UNIT_KEYS.get(name, name), kind) for name, kind in UNIT_COLUMNS)


def macrostrat_ref_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        kept = json.load(handle)
    for ref_id, citation in sorted(kept["refs"].items(), key=lambda item: int(item[0])):
        yield (int(ref_id), citation)


def macrostrat(ctx) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(MACROSTRAT_DDL)
        state, today = core.get_state(db, "macrostrat"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < MACROSTRAT_RECHECK_DAYS and loaded_keys(db, "macrostrat-units") >= {"units"}:
            return {"state": "not_due", "checked": state["checked"]}
        payload, everything = json_body(ctx, MACROSTRAT_ALL, "MACROSTRAT")
        features = _macrostrat_data(payload, "all").get("features")
        if not isinstance(features, list):
            raise FeedError("MACROSTRAT_RESPONSE_SHAPE all")
        west, south, east, north = KANSAS_BOX
        col_ids = sorted(int(f["properties"]["col_id"]) for f in features if f.get("geometry") and (
            lambda b: b[0] <= east and b[2] >= west and b[1] <= north and b[3] >= south)(bbox(f["geometry"])))
        if not col_ids:
            raise FeedError("MACROSTRAT_NO_KANSAS_COLUMNS")
        ids = ",".join(str(i) for i in col_ids)
        pause(ctx)
        payload, fetched = json_body(ctx, f"{MACROSTRAT}columns?col_id={ids}&format=geojson&response=long", "MACROSTRAT")
        kansas = _macrostrat_data(payload, "columns").get("features")
        if not isinstance(kansas, list) or sorted(int(f["properties"]["col_id"]) for f in kansas) != col_ids:
            raise FeedError("MACROSTRAT_COLUMNS_MISMATCH")
        kansas.sort(key=lambda f: int(f["properties"]["col_id"]))
        extra = {"citation": MACROSTRAT_CITATION, "license": MACROSTRAT_LICENSE, "col_ids": col_ids}
        result = keep_version(ctx, db, feed="macrostrat", source_id="macrostrat-columns", key="columns", name="columns/macrostrat-columns-kansas",
                              ext=".jsonl.gz", body=jsonl_bytes(kansas), url=fetched.url, fetched=fetched, original=everything.body,
                              extra=extra, table="kfm_macrostrat_columns", width=len(COLUMN_COLUMNS), rows=macrostrat_column_rows)
        summary = {"columns": f"{result['state']} {len(col_ids)}", "rows": result["rows"]}
        pause(ctx)
        payload, fetched = json_body(ctx, f"{MACROSTRAT}units?col_id={ids}&response=long", "MACROSTRAT")
        units = _macrostrat_data(payload, "units")
        refs = payload["success"].get("refs")
        if not isinstance(units, list) or not isinstance(refs, dict):
            raise FeedError("MACROSTRAT_RESPONSE_SHAPE units")
        if not units:
            raise FeedError("MACROSTRAT_NO_UNITS")
        kept = (core.canonical({"refs": refs, "units": units}) + "\n").encode()
        result = keep_tables(ctx, db, feed="macrostrat", source_id="macrostrat-units", key="units", name="units/macrostrat-units-kansas",
                             ext=".json.gz", body=core.gz(kept), url=fetched.url, fetched=fetched, extra={**extra, "units": len(units)},
                             tables=lambda path: [("kfm_macrostrat_units", macrostrat_unit_rows(path), len(UNIT_COLUMNS)),
                                                  ("kfm_macrostrat_refs", macrostrat_ref_rows(path), 2)])
        summary["units"] = f"{result['state']} {len(units)}"
        summary["rows"] += result["rows"]
        save_state(ctx, db, "macrostrat", {"checked": str(today), "col_ids": col_ids, "units": len(units)})
        return summary
    finally:
        db.close()


# --- Radiocarbon: the p3k14c file at its newest commit, cut to Kansas --------------------------------

P3K14C_REPO = "people3k/p3k14c"
P3K14C_PATH = "inst/p3k14c_scrubbed_fuzzed.csv"
P3K14C_COMMITS = f"https://api.github.com/repos/{P3K14C_REPO}/commits?path={P3K14C_PATH}&per_page=1"
P3K14C_RAW = f"https://raw.githubusercontent.com/{P3K14C_REPO}/{{commit}}/{P3K14C_PATH}"
P3K14C_CITATION = ("Bird, D., Miranda, L., Vander Linden, M., et al. 2022. p3k14c, a synthetic global database of archaeological "
                   "radiocarbon dates. Scientific Data 9:27, doi:10.1038/s41597-022-01118-7; Bocinsky, R.K., Bird, D., Miranda, L., "
                   "Freeman, J. Compendium of R code and data for p3k14c, doi:10.5281/zenodo.6633635")
P3K14C_LICENSE = "CC0 1.0 for the data, attribution requested (p3k14c README; code MIT, text CC BY 4.0)"
P3K14C_HEADER = ["LabID", "Age", "Error", "Material", "Taxa", "d13C", "Method", "Long", "Lat", "LocAccuracy", "Period", "SiteID", "SiteName",
                 "Country", "Province", "Continent", "Source", "Reference"]
P3K14C_COLUMNS = columns("lab_id:TEXT! age:NUMERIC error:NUMERIC material taxa d13c:REAL method long:REAL lat:REAL loc_accuracy period "
                         "site_id site_name country province continent source reference county_geoid kansas_basis")
P3K14C_NUMBERS = {"Age", "Error", "d13C", "Long", "Lat"}
P3K14C_TABLE = "kfm_p3k14c_dates"
P3K14C_DDL = table_ddl(P3K14C_TABLE, P3K14C_COLUMNS, (("county_geoid",), ("lab_id",), ("site_id",)))
P3K14C_KEY = "p3k14c-scrubbed-fuzzed"
P3K14C_RECHECK_DAYS = 6


def p3k14c_place(row: list, counties) -> tuple:
    """(county_geoid, kansas_basis) of a p3k14c row, or (None, None) outside Kansas."""
    lon, lat = number(row[7]), number(row[8])
    geoid = county_at(counties, lon, lat) if lon is not None and lat is not None and in_kansas_box(lon, lat) else None
    if row[14] == "Kansas":
        return geoid, "province"
    return (geoid, "coordinates") if geoid else (None, None)


def p3k14c_rows(path: Path, counties):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        if next(reader, None) != P3K14C_HEADER:
            raise FeedError("P3K14C_COLUMNS_CHANGED kept")
        for row in reader:
            if len(row) != len(P3K14C_HEADER):
                raise FeedError("P3K14C_ROW_SHAPE kept")
            geoid, basis = p3k14c_place(row, counties)
            yield (*(number(v) if name in P3K14C_NUMBERS else v for name, v in zip(P3K14C_HEADER, row)), geoid, basis)


def radiocarbon(ctx) -> dict:
    if not ctx.tiger:
        raise FeedError("TIGER_GEOPACKAGE_REQUIRED")
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(P3K14C_DDL)
        state, today = core.get_state(db, "radiocarbon"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < P3K14C_RECHECK_DAYS and P3K14C_KEY in loaded_keys(db, "p3k14c"):
            return {"state": "not_due", "checked": state["checked"]}
        commits, _ = json_body(ctx, P3K14C_COMMITS, "GITHUB", limit=4_000_000)
        if not isinstance(commits, list) or not commits or not isinstance(commits[0].get("sha"), str):
            raise FeedError("GITHUB_COMMITS_SHAPE")
        commit, committed = commits[0]["sha"], ((commits[0].get("commit") or {}).get("committer") or {}).get("date")
        if commit == state.get("commit") and P3K14C_KEY in loaded_keys(db, "p3k14c"):
            save_state(ctx, db, "radiocarbon", {**state, "checked": str(today)})
            return {"state": "unchanged", "commit": commit, "kansas_rows": state.get("kansas_rows")}
        counties, temp = kansas_counties(ctx.tiger), core.temp_path(ctx, "p3k14c.csv")
        try:
            fetched = core.download(ctx, P3K14C_RAW.format(commit=commit), temp, limit=512_000_000, timeout=900)
            with open(temp, "r", encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle)
                if next(reader, None) != P3K14C_HEADER:
                    raise FeedError("P3K14C_COLUMNS_CHANGED")
                keep, by_coordinates = [], 0
                for row in reader:
                    if len(row) != len(P3K14C_HEADER):
                        raise FeedError("P3K14C_ROW_SHAPE")
                    geoid, basis = p3k14c_place(row, counties)
                    if basis:
                        keep.append(row)
                        by_coordinates += basis == "coordinates"
            if not keep:
                raise FeedError("P3K14C_NO_KANSAS_ROWS")
            result = keep_version(ctx, db, feed="radiocarbon", source_id="p3k14c", key=P3K14C_KEY, name="p3k14c-scrubbed-fuzzed-kansas",
                                  ext=".csv.gz", body=core.gz(csv_bytes([P3K14C_HEADER, *keep])), url=fetched.url, fetched=fetched, original=temp,
                                  extra={"citation": P3K14C_CITATION, "license": P3K14C_LICENSE, "commit": commit, "committed": committed,
                                         "kansas_rows": len(keep), "by_coordinates": by_coordinates},
                                  table=P3K14C_TABLE, width=len(P3K14C_COLUMNS), rows=lambda path: p3k14c_rows(path, counties))
        finally:
            temp.unlink(missing_ok=True)
        save_state(ctx, db, "radiocarbon", {"checked": str(today), "commit": commit, "committed": committed, "kansas_rows": len(keep)})
        return {**result, "commit": commit, "kansas_rows": len(keep), "by_coordinates": by_coordinates}
    finally:
        db.close()


# --- Neotoma: the Kansas lists and every dataset's download ---------------------------------------------

NEOTOMA = "https://api.neotomadb.org/v2.0/data/"
NEOTOMA_GPID = 7034
NEOTOMA_SITES = f"{NEOTOMA}geopoliticalunits/{NEOTOMA_GPID}/sites?limit=10000"
NEOTOMA_DATASETS = f"{NEOTOMA}datasets?gpid={NEOTOMA_GPID}&limit=10000"
NEOTOMA_DOWNLOAD = NEOTOMA + "downloads/{id}"
NEOTOMA_LIMIT = 10000
NEOTOMA_CITATION = ("Williams, J.W., et al. 2018. The Neotoma Paleoecology Database. Quaternary Research 89:156-177, "
                    "doi:10.1017/qua.2017.105; with the constituent database and each dataset's DOI")
NEOTOMA_LICENSE = "CC BY 4.0 (https://www.neotomadb.org/data/data-use-and-embargo-policy)"
NEOTOMA_LISTS_DAYS = 6
NEOTOMA_REFRESH_DAYS = 180
NEOTOMA_DOWNLOADS_PER_RUN = 300
SITE_COLUMNS = columns("siteid:INTEGER sitename sitedescription altitude:REAL recdatecreated geometry_geojson min_lon:REAL min_lat:REAL "
                       "max_lon:REAL max_lat:REAL")
UNIT_LIST_COLUMNS = columns("siteid:INTEGER collectionunitid:INTEGER handle collectionunit collectionunittype datasets")
DATASET_COLUMNS = columns("datasetid:INTEGER siteid:INTEGER sitename collectionunitid:INTEGER collectionunit handle unittype datasettype "
                          "database doi agerange_units ageold:REAL ageyoung:REAL agerange datasetpi datasetnotes recdatecreated")
SUMMARY_COLUMNS = columns(
    "datasetid:INTEGER siteid:INTEGER sitename geopolitical collectionunitid:INTEGER handle collectionunit collunittype "
    "depositionalenvironment collectiondevice colldate waterdepth:REAL location gpslocation collectors collectionunit_notes datasettype "
    "database datasetname defaultchronology:INTEGER samples:INTEGER data_values:INTEGER taxa:INTEGER min_depth:REAL max_depth:REAL "
    "age_type min_age:REAL max_age:REAL chronologies:INTEGER chron_controls:INTEGER")
SAMPLE_COLUMNS = columns(
    "datasetid:INTEGER sampleid:INTEGER samplename analysisunitid:INTEGER analysisunitname depth:REAL thickness:REAL igsn analysisdate "
    "samplenotes analysisunitnotes sampleanalyst taxonid:INTEGER variablename taxongroup ecologicalgroup element elementtype symmetry "
    "context units value:REAL")
AGE_COLUMNS = columns("datasetid:INTEGER sampleid:INTEGER chronologyid:INTEGER chronologyname agetype age:REAL ageolder:REAL ageyounger:REAL")
CHRON_COLUMNS = columns(
    "datasetid:INTEGER collectionunitid:INTEGER chronologyid:INTEGER chronologyname isdefault agemodel modelagetype ageboundolder:REAL "
    "ageboundyounger:REAL dateprepared chronology_notes chronology_contact chroncontrolid:INTEGER chroncontroltype depth:REAL "
    "thickness:REAL chroncontrolage:REAL agelimitolder:REAL agelimityounger:REAL geochronid:INTEGER geochrontype labnumber "
    "geochron_agetype geochronage:REAL geochronerrorolder:REAL geochronerroryounger:REAL geochronmaterialdated delta13c:REAL "
    "delta15n:REAL infinite reservoir radiocarbonmethod percentc:REAL percentn:REAL percentcollagen:REAL geochronnotes")
NEOTOMA_DDL = (table_ddl("kfm_neotoma_chron_controls", CHRON_COLUMNS, (("datasetid",), ("labnumber",)))
               + table_ddl("kfm_neotoma_collection_units", UNIT_LIST_COLUMNS, (("collectionunitid",), ("siteid",)))
               + table_ddl("kfm_neotoma_dataset_summaries", SUMMARY_COLUMNS, (("datasetid",),))
               + table_ddl("kfm_neotoma_datasets", DATASET_COLUMNS, (("datasetid",), ("datasettype",), ("siteid",)))
               + table_ddl("kfm_neotoma_sample_ages", AGE_COLUMNS, (("datasetid", "sampleid"),))
               + table_ddl("kfm_neotoma_samples", SAMPLE_COLUMNS, (("datasetid", "sampleid"), ("taxonid",), ("variablename",)))
               + table_ddl("kfm_neotoma_sites", SITE_COLUMNS, (("siteid",),)))
NEOTOMA_DOWNLOAD_TABLES = ("kfm_neotoma_dataset_summaries", "kfm_neotoma_samples", "kfm_neotoma_sample_ages", "kfm_neotoma_chron_controls")


def _neotoma_list(ctx, url: str, code: str) -> tuple[list, core.Fetched]:
    payload, fetched = json_body(ctx, url, "NEOTOMA")
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, list):
        raise FeedError(f"NEOTOMA_RESPONSE_SHAPE {code}")
    if len(data) >= NEOTOMA_LIMIT:
        raise FeedError(f"NEOTOMA_LIST_TRUNCATED {code}")
    return data, fetched


def _geometry(geography):
    """A Neotoma geography (GeoJSON text with a crs member) as (canonical text, bbox)."""
    if not geography:
        return None, (None, None, None, None)
    geometry = json.loads(geography) if isinstance(geography, str) else geography
    geometry.pop("crs", None)
    return core.canonical(geometry), bbox(geometry)


def neotoma_site_rows(path: Path):
    for site in jsonl_lines(path):
        geometry, (west, south, east, north) = _geometry(site.get("geography"))
        yield (site["siteid"], site.get("sitename"), site.get("sitedescription"), site.get("altitude"), site.get("recdatecreated"),
               geometry, west, south, east, north)


def neotoma_unit_rows(path: Path):
    """One row per collection unit, its datasets merged from the per-dataset entries Neotoma lists."""
    for site in jsonl_lines(path):
        units = {}
        for entry in site.get("collectionunits") or []:
            unit = units.setdefault(entry["collectionunitid"], {**entry, "datasets": []})
            unit["datasets"].extend(entry.get("datasets") or [])
        for unit in units.values():
            yield (site["siteid"], unit["collectionunitid"], unit.get("handle"), unit.get("collectionunit"), unit.get("collectionunittype"),
                   jtext(unit["datasets"]))


def neotoma_dataset_rows(path: Path):
    for item in jsonl_lines(path):
        site = item["site"]
        for ds in site.get("datasets") or []:
            first = (ds.get("agerange") or [None])[0] or {}
            yield (ds["datasetid"], site["siteid"], site.get("sitename"), site.get("collectionunitid"), site.get("collectionunit"),
                   site.get("handle"), site.get("unittype"), ds.get("datasettype"), ds.get("database"), jtext(ds.get("doi")),
                   first.get("units"), first.get("ageold"), first.get("ageyoung"), jtext(ds.get("agerange")), jtext(ds.get("datasetpi")),
                   ds.get("datasetnotes"), ds.get("recdatecreated"))


def _download_parts(kept: dict) -> dict:
    site = kept["site"]
    unit = site["collectionunit"]
    ds = unit["dataset"]
    samples = [s for s in ds.get("samples") or [] if nonnull(s)]
    chronologies = [c["chronology"] for c in unit.get("chronologies") or [] if (c.get("chronology") or {}).get("chronologyid") is not None]
    return {"site": site, "unit": unit, "dataset": ds, "samples": samples, "chronologies": chronologies}


def neotoma_download_tables(path: Path) -> list:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        parts = _download_parts(json.load(handle))
    site, unit, ds, samples, chronologies = (parts[k] for k in ("site", "unit", "dataset", "samples", "chronologies"))
    did = ds["datasetid"]
    data = [(s, d) for s in samples for d in s.get("datum") or [] if nonnull(d)]
    ages = [(s, a) for s in samples for a in s.get("ages") or [] if nonnull(a)]
    controls = [(c, cc) for c in chronologies for cc in ([x for x in c.get("chroncontrols") or [] if nonnull(x)] or [None])]
    depths = [s["depth"] for s in samples if s.get("depth") is not None]
    first = (ds.get("agerange") or [None])[0] or {}
    gps = unit.get("gpslocation")
    summary = (did, site.get("siteid"), site.get("sitename"), jtext(site.get("geopolitical")), unit.get("collectionunitid"), unit.get("handle"),
               unit.get("collectionunit"), unit.get("collunittype"), unit.get("depositionalenvironment"), unit.get("collectiondevice"),
               unit.get("colldate"), unit.get("waterdepth"), unit.get("location"), jtext(gps), jtext(unit.get("collectors")), unit.get("notes"),
               ds.get("datasettype"), ds.get("database"), ds.get("datasetname"), unit.get("defaultchronology"), len(samples), len(data),
               len({d.get("taxonid") for _, d in data}), min(depths) if depths else None, max(depths) if depths else None,
               first.get("units"), first.get("ageyoung"), first.get("ageold"), len(chronologies), sum(1 for _, cc in controls if cc))

    def sample_rows():
        for s, d in data:
            yield (did, s.get("sampleid"), s.get("samplename"), s.get("analysisunitid"), s.get("analysisunitname"), s.get("depth"),
                   s.get("thickness"), s.get("igsn"), s.get("analysisdate"), s.get("samplenotes"), s.get("analysisunitnotes"),
                   jtext(s.get("sampleanalyst")) if nonnull(s.get("sampleanalyst")) else None,
                   d.get("taxonid"), d.get("variablename"), d.get("taxongroup"), d.get("ecologicalgroup"),
                   d.get("element"), d.get("elementtype"), d.get("symmetry"), d.get("context"), d.get("units"), d.get("value"))

    def age_rows():
        for s, a in ages:
            yield (did, s.get("sampleid"), a.get("chronologyid"), a.get("chronologyname"), a.get("agetype"), a.get("age"), a.get("ageolder"),
                   a.get("ageyounger"))

    def chron_rows():
        for c, cc in controls:
            meta, cc = c.get("chronology") or {}, cc or {}
            geo = cc.get("geochron") or {}
            yield (did, unit.get("collectionunitid"), c.get("chronologyid"), meta.get("chronologyname"), flag(meta.get("isdefault")),
                   meta.get("agemodel"), meta.get("modelagetype"), (meta.get("agerange") or {}).get("ageboundolder"),
                   (meta.get("agerange") or {}).get("ageboundyounger"), meta.get("dateprepared"), meta.get("notes"), jtext(meta.get("contact")),
                   cc.get("chroncontrolid"), cc.get("chroncontroltype"), cc.get("depth"), cc.get("thickness"), cc.get("chroncontrolage"),
                   cc.get("agelimitolder"), cc.get("agelimityounger"), geo.get("geochronid"), geo.get("geochrontype"), geo.get("labnumber"),
                   geo.get("agetype"), geo.get("geochronage"), geo.get("geochronerrorolder"), geo.get("geochronerroryounger"),
                   geo.get("geochronmaterialdated"), geo.get("delta13c"), geo.get("delta15n"), flag(geo.get("infinite")), geo.get("reservoir"),
                   geo.get("radiocarbonmethod"), geo.get("percentc"), geo.get("percentn"), geo.get("percentcollagen"), geo.get("geochronnotes"))
    return [("kfm_neotoma_dataset_summaries", [summary], len(SUMMARY_COLUMNS)), ("kfm_neotoma_samples", sample_rows(), len(SAMPLE_COLUMNS)),
            ("kfm_neotoma_sample_ages", age_rows(), len(AGE_COLUMNS)), ("kfm_neotoma_chron_controls", chron_rows(), len(CHRON_COLUMNS))]


def _neotoma_download(ctx, db, dataset_id: int) -> dict:
    payload, fetched = json_body(ctx, NEOTOMA_DOWNLOAD.format(id=dataset_id), "NEOTOMA")
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, list) or len(data) != 1 or not isinstance(data[0], dict) or "site" not in data[0]:
        raise FeedError(f"NEOTOMA_RESPONSE_SHAPE download {dataset_id}")
    try:
        ds = _download_parts(data[0])["dataset"]
    except (KeyError, TypeError):
        raise FeedError(f"NEOTOMA_RESPONSE_SHAPE download {dataset_id}") from None
    if ds.get("datasetid") != dataset_id:
        raise FeedError(f"NEOTOMA_DATASET_MISMATCH {dataset_id}")
    return keep_tables(ctx, db, feed="neotoma", source_id="neotoma-download", key=f"dataset/{dataset_id}",
                       name=f"downloads/{dataset_id}/neotoma-dataset-{dataset_id}", ext=".json.gz",
                       body=core.gz((core.canonical(data[0]) + "\n").encode()), url=fetched.url, fetched=fetched,
                       extra={"citation": NEOTOMA_CITATION, "license": NEOTOMA_LICENSE, "datasettype": ds.get("datasettype"),
                              "doi": ds.get("doi") or None},
                       tables=neotoma_download_tables)


def neotoma(ctx, max_downloads: int = NEOTOMA_DOWNLOADS_PER_RUN) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(NEOTOMA_DDL)
        state, today = core.get_state(db, "neotoma"), ctx.now().date()
        summary, fetched_on = {"rows": 0}, dict(state.get("fetched", {}))
        age = age_days(state, "lists_checked", today)
        extra = {"citation": NEOTOMA_CITATION, "license": NEOTOMA_LICENSE}
        if age is None or age >= NEOTOMA_LISTS_DAYS or not loaded_keys(db, "neotoma-datasets"):
            sites, fetched = _neotoma_list(ctx, NEOTOMA_SITES, "sites")
            if not sites:
                raise FeedError("NEOTOMA_NO_KANSAS_SITES")
            sites.sort(key=lambda s: s["siteid"])
            result = keep_tables(ctx, db, feed="neotoma", source_id="neotoma-sites", key="sites", name="lists/neotoma-sites-gpid7034",
                                 ext=".jsonl.gz", body=jsonl_bytes(sites), url=fetched.url, fetched=fetched, extra={**extra, "sites": len(sites)},
                                 tables=lambda path: [("kfm_neotoma_sites", neotoma_site_rows(path), len(SITE_COLUMNS)),
                                                      ("kfm_neotoma_collection_units", neotoma_unit_rows(path), len(UNIT_LIST_COLUMNS))])
            summary["sites"], summary["rows"] = f"{result['state']} {len(sites)}", summary["rows"] + result["rows"]
            pause(ctx)
            items, fetched = _neotoma_list(ctx, NEOTOMA_DATASETS, "datasets")
            items.sort(key=lambda i: (i["site"]["siteid"], i["site"]["collectionunitid"]))
            listed = sorted({ds["datasetid"] for i in items for ds in i["site"].get("datasets") or []})
            if not listed:
                raise FeedError("NEOTOMA_NO_KANSAS_DATASETS")
            result = keep_tables(ctx, db, feed="neotoma", source_id="neotoma-datasets", key="datasets", name="lists/neotoma-datasets-gpid7034",
                                 ext=".jsonl.gz", body=jsonl_bytes(items), url=fetched.url, fetched=fetched, extra={**extra, "datasets": len(listed)},
                                 tables=lambda path: [("kfm_neotoma_datasets", neotoma_dataset_rows(path), len(DATASET_COLUMNS))])
            summary["datasets"], summary["rows"] = f"{result['state']} {len(listed)}", summary["rows"] + result["rows"]
            gone = sorted(int(k) for k in fetched_on if int(k) not in listed)
            with core.pipeline_lock(ctx):
                for dataset_id in gone:
                    retire_all(db, "neotoma-download", f"dataset/{dataset_id}", NEOTOMA_DOWNLOAD_TABLES)
                    fetched_on.pop(str(dataset_id), None)
            summary["retired"] = len(gone)
            state = save_state(ctx, db, "neotoma", {"datasets": listed, "fetched": fetched_on, "lists_checked": str(today)})
        listed = [int(i) for i in state.get("datasets", [])]
        loaded = loaded_keys(db, "neotoma-download")
        due = [i for i in listed if str(i) not in fetched_on or f"dataset/{i}" not in loaded]
        stale = sorted((i for i in listed if i not in due and age_days(fetched_on, str(i), today) >= NEOTOMA_REFRESH_DAYS),
                       key=lambda i: fetched_on[str(i)])
        summary.update({"downloaded": 0, "unchanged": 0, "download_rows": 0})
        for dataset_id in (due + stale)[:max_downloads]:
            if summary["downloaded"] or summary["unchanged"]:
                pause(ctx)
            result = _neotoma_download(ctx, db, dataset_id)
            summary["unchanged" if result["state"] == "unchanged" else "downloaded"] += 1
            summary["download_rows"] += result["rows"]
            summary["rows"] += result["rows"]
            fetched_on[str(dataset_id)] = str(today)
            state = save_state(ctx, db, "neotoma", {**state, "fetched": fetched_on})
        summary["pending"] = max(0, len(due + stale) - max_downloads)
        return summary
    finally:
        db.close()


# --- iDigBio: Kansas fossil specimens, in county segments ------------------------------------------------

IDIGBIO = "https://search.idigbio.org/v2/"
IDIGBIO_CITATION = "iDigBio (https://search.idigbio.org/), with the recordsets and institutions of the records used"
IDIGBIO_LICENSE = "Per recordset (kfm_idigbio_recordsets.data_rights) and per record (license, rights, access_rights)"
# The spellings of Kansas in iDigBio's indexed stateprovince on 2026-11-03, most records first.
KANSAS_STATEPROVINCE = ["kansas", "ks", "united states of america; kansas", "kansas; united states of america", "kansas; kansas",
                        "clark; kansas", "cloud; kansas", "ellis; kansas", "ellsworth; kansas", "gove; kansas", "graham; kansas",
                        "lane; kansas", "logan; kansas", "mitchell; kansas", "ness; kansas", "phillips; kansas", "rooks; kansas",
                        "russell; kansas", "trego; kansas", "douglas cy, kansas", "osage co. kansas"]
IDIGBIO_FIELDS = ["uuid", "etag", "recordset", "datemodified", "county", "stateprovince", "basisofrecord", "geopoint"] + [
    "data." + f for f in (
        "dwc:occurrenceID dwc:basisOfRecord dwc:institutionCode dwc:institutionID dwc:collectionCode dwc:collectionID "
        "dwc:ownerInstitutionCode dwc:datasetName dwc:catalogNumber dwc:otherCatalogNumbers dwc:scientificName "
        "dwc:scientificNameAuthorship dwc:taxonRank dwc:kingdom dwc:phylum dwc:class dwc:order dwc:family dwc:genus dwc:subgenus "
        "dwc:specificEpithet dwc:infraspecificEpithet dwc:higherClassification dwc:vernacularName dwc:identifiedBy dwc:dateIdentified "
        "dwc:identificationQualifier dwc:typeStatus dwc:earliestEonOrLowestEonothem dwc:latestEonOrHighestEonothem "
        "dwc:earliestEraOrLowestErathem dwc:latestEraOrHighestErathem dwc:earliestPeriodOrLowestSystem dwc:latestPeriodOrHighestSystem "
        "dwc:earliestEpochOrLowestSeries dwc:latestEpochOrHighestSeries dwc:earliestAgeOrLowestStage dwc:latestAgeOrHighestStage "
        "dwc:lowestBiostratigraphicZone dwc:highestBiostratigraphicZone dwc:group dwc:formation dwc:member dwc:bed "
        "dwc:lithostratigraphicTerms dwc:country dwc:stateProvince dwc:county dwc:municipality dwc:locality dwc:verbatimLocality "
        "dwc:locationRemarks dwc:decimalLatitude dwc:decimalLongitude dwc:geodeticDatum dwc:coordinateUncertaintyInMeters "
        "dwc:coordinatePrecision dwc:georeferenceRemarks dwc:informationWithheld dwc:dataGeneralizations dwc:recordedBy dwc:recordNumber "
        "dwc:fieldNumber dwc:eventDate dwc:verbatimEventDate dwc:year dwc:month dwc:day dwc:individualCount dwc:preparations "
        "dwc:disposition dwc:occurrenceRemarks dwc:associatedMedia dwc:associatedReferences dcterms:license dcterms:rights dc:rights "
        "dcterms:rightsHolder dcterms:accessRights dcterms:bibliographicCitation dcterms:references dcterms:modified").split()]
IDIGBIO_DATA = [f[5:] for f in IDIGBIO_FIELDS if f.startswith("data.")]
FOSSIL_COLUMNS = columns("uuid:TEXT! etag recordset datemodified idigbio_county idigbio_stateprovince geopoint_lon:REAL geopoint_lat:REAL") + [
    ("dc_rights" if term == "dc:rights" else snake(term.split(":")[1]), "TEXT") for term in IDIGBIO_DATA]
RECORDSET_COLUMNS = columns("uuid name data_rights publisher url emllink archivelink logo description item_count:INTEGER total_count:INTEGER contacts")
FOSSIL_TABLE, RECORDSET_TABLE = "kfm_idigbio_fossils", "kfm_idigbio_recordsets"
IDIGBIO_DDL = (table_ddl(FOSSIL_TABLE, FOSSIL_COLUMNS, (("formation",), ("idigbio_county",), ("scientific_name",), ("uuid",)))
               + table_ddl(RECORDSET_TABLE, RECORDSET_COLUMNS, (("uuid",),)))
IDIGBIO_PAGE = 5000               # the search API's largest limit
IDIGBIO_SUMMARY_COUNT = 1000
IDIGBIO_SEGMENT_MAX = 20_000      # a county with more records is split by recordset
IDIGBIO_RECORDS_PER_RUN = 50_000
IDIGBIO_REQUESTS_PER_RUN = 200
IDIGBIO_RESWEEP_DAYS = 28
IDIGBIO_REFRESH_DAYS = 180
IDIGBIO_MISSING = "county-missing"


def idigbio_query(**extra) -> dict:
    return {"stateprovince": KANSAS_STATEPROVINCE, "basisofrecord": "fossilspecimen", **extra}


def _compact(value) -> str:
    return json.dumps(value, separators=(",", ":"))


def idigbio_search_url(rq: dict, fields: list, limit: int) -> str:
    return IDIGBIO + "search/records?" + urllib.parse.urlencode({"rq": _compact(rq), "fields": _compact(fields), "sort": '["uuid"]', "limit": limit})


def idigbio_summary_url(rq: dict, field: str) -> str:
    return IDIGBIO + "summary/top/records?" + urllib.parse.urlencode({"rq": _compact(rq), "top_fields": _compact([field]), "count": IDIGBIO_SUMMARY_COUNT})


def idigbio_json(ctx, url: str):
    """iDigBio's JSON, or IDIGBIO_API_GONE when the answer is something else (the site now redirects to GBIF)."""
    fetched = ctx.fetch(url, limit=256_000_000, timeout=600)
    try:
        payload = json.loads(fetched.body)
    except ValueError:
        raise FeedError(f"IDIGBIO_API_GONE {url[:100]}") from None
    if not isinstance(payload, dict):
        raise FeedError(f"IDIGBIO_API_GONE {url[:100]}")
    return payload, fetched


def idigbio_segment_name(key: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
    return f"segments/{slug}-{hashlib.sha256(key.encode()).hexdigest()[:8]}/idigbio-fossils"


def idigbio_top(ctx, rq: dict, field: str) -> tuple[dict, int]:
    """({value: count} of the field over the records rq matches, the records matched)."""
    payload, _ = idigbio_json(ctx, idigbio_summary_url(rq, field))
    values = payload.get(field)
    if not isinstance(values, dict) or not isinstance(payload.get("itemCount"), int):
        raise FeedError(f"IDIGBIO_RESPONSE_SHAPE summary {field}")
    if len(values) >= IDIGBIO_SUMMARY_COUNT:
        raise FeedError(f"IDIGBIO_SUMMARY_TRUNCATED {field}")
    return {k: int(v["itemCount"]) for k, v in values.items()}, payload["itemCount"]


def idigbio_plan(ctx, state: dict, today: date) -> tuple[list, int]:
    """The segments of a new sweep: ([key, query, count] in key order, every one; and the request count), skipping
    none here (the caller drops the ones whose loaded copy is current)."""
    counts, total = idigbio_top(ctx, idigbio_query(), "county")
    requests, plan = 1, []
    for value, count in counts.items():
        if count > IDIGBIO_SEGMENT_MAX:
            pause(ctx)
            by_recordset, _ = idigbio_top(ctx, idigbio_query(county=value), "recordset")
            requests += 1
            plan.extend([f"county/{value}/recordset/{rs}", {"county": value, "recordset": rs}, n] for rs, n in by_recordset.items())
        else:
            plan.append([f"county/{value}", {"county": value}, count])
    missing = total - sum(counts.values())
    if missing > 0:
        plan.append([IDIGBIO_MISSING, {"county": {"type": "missing"}}, missing])
    plan.sort(key=lambda entry: entry[0])
    return plan, requests


def idigbio_fetch_segment(ctx, extra: dict) -> tuple[list, str, int]:
    """Every record of one segment, in uuid order, paged by a uuid range: (records, first page URL, requests)."""
    records, last, first, requests = [], None, None, 0
    while True:
        rq = idigbio_query(**extra) if last is None else idigbio_query(**extra, uuid={"type": "range", "gt": last})
        url = idigbio_search_url(rq, IDIGBIO_FIELDS, IDIGBIO_PAGE)
        first = first or url
        if requests:
            pause(ctx)
        payload, _ = idigbio_json(ctx, url)
        requests += 1
        items = payload.get("items")
        if not isinstance(items, list):
            raise FeedError("IDIGBIO_RESPONSE_SHAPE search")
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("uuid"), str) or (last and item["uuid"] <= last):
                raise FeedError("IDIGBIO_RESPONSE_SHAPE record")
            records.append({"uuid": item["uuid"], "etag": item.get("etag"), "data": item.get("data") or {}, "indexTerms": item.get("indexTerms") or {}})
            last = item["uuid"]
        if len(items) < IDIGBIO_PAGE:
            break
    records.sort(key=lambda r: r["uuid"])
    return records, first, requests


def _text(value):
    return value if value is None or isinstance(value, str) else core.canonical(value)


def idigbio_fossil_rows(path: Path):
    for record in jsonl_lines(path):
        terms, data = record.get("indexTerms") or {}, record.get("data") or {}
        point = terms.get("geopoint") or {}
        yield (record["uuid"], record.get("etag"), terms.get("recordset"), terms.get("datemodified"), _text(terms.get("county")),
               _text(terms.get("stateprovince")), point.get("lon"), point.get("lat"), *(_text(data.get(term)) for term in IDIGBIO_DATA))


def idigbio_recordset_rows(path: Path):
    for rs in jsonl_lines(path):
        yield (rs.get("uuid"), rs.get("name"), rs.get("data_rights"), rs.get("publisher"), rs.get("url"), rs.get("emllink"), rs.get("archivelink"),
               rs.get("logo"), rs.get("description"), rs.get("itemCount"), rs.get("totalCount"), jtext(rs.get("contacts")))


def idigbio_fossils(ctx, max_records: int = IDIGBIO_RECORDS_PER_RUN, max_requests: int = IDIGBIO_REQUESTS_PER_RUN) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(IDIGBIO_DDL)
        state, today = core.get_state(db, "idigbio-fossils"), ctx.now().date()
        pending, segments = list(state.get("pending", [])), dict(state.get("segments", {}))
        summary, extra = {"loaded": 0, "unchanged": 0, "records": 0, "requests": 0, "rows": 0}, {"citation": IDIGBIO_CITATION, "license": IDIGBIO_LICENSE}
        if not pending:
            age = age_days(state, "started", today)
            if age is not None and age < IDIGBIO_RESWEEP_DAYS:
                return {"state": "not_due", "started": state["started"], "segments": len(segments)}
            payload, fetched = idigbio_json(ctx, idigbio_search_url(idigbio_query(), ["uuid"], 1))
            recordsets, total = payload.get("attribution"), payload.get("itemCount")
            if not isinstance(recordsets, list) or not isinstance(total, int):
                raise FeedError("IDIGBIO_RESPONSE_SHAPE attribution")
            recordsets.sort(key=lambda rs: str(rs.get("uuid")))
            result = keep_version(ctx, db, feed="idigbio-fossils", source_id="idigbio-recordsets", key="recordsets", name="recordsets/idigbio-recordsets-kansas",
                                  ext=".jsonl.gz", body=jsonl_bytes(recordsets), url=fetched.url, fetched=fetched,
                                  extra={**extra, "records": total, "recordsets": len(recordsets)}, table=RECORDSET_TABLE,
                                  width=len(RECORDSET_COLUMNS), rows=idigbio_recordset_rows)
            summary["recordsets"], summary["rows"] = f"{result['state']} {len(recordsets)}", result["rows"]
            pause(ctx)
            plan, requests = idigbio_plan(ctx, state, today)
            summary["requests"] += requests + 1
            planned = {key for key, _, _ in plan}
            with core.pipeline_lock(ctx):
                for key in sorted(set(segments) - planned):
                    retire(db, "idigbio-fossils", key, FOSSIL_TABLE)
                    segments.pop(key)
            summary["retired"] = len(state.get("segments", {})) - len(segments)
            pending = [entry for entry in plan if not (segments.get(entry[0], {}).get("records") == entry[2]
                                                       and age_days(segments[entry[0]], "fetched", today) < IDIGBIO_REFRESH_DAYS)]
            summary["planned"] = len(plan)
            state = save_state(ctx, db, "idigbio-fossils", {"pending": pending, "segments": segments, "started": str(today)})
        while pending and summary["records"] < max_records and summary["requests"] < max_requests:
            key, query, count = pending[0]
            if summary["requests"]:
                pause(ctx)
            records, url, requests = idigbio_fetch_segment(ctx, query)
            summary["requests"] += requests
            if records:
                result = keep_version(ctx, db, feed="idigbio-fossils", source_id="idigbio-fossils", key=key, name=idigbio_segment_name(key),
                                      ext=".jsonl.gz", body=jsonl_bytes(records), url=url, extra={**extra, "query": idigbio_query(**query), "records": len(records)},
                                      table=FOSSIL_TABLE, width=len(FOSSIL_COLUMNS), rows=idigbio_fossil_rows)
            else:
                with core.pipeline_lock(ctx):
                    retire(db, "idigbio-fossils", key, FOSSIL_TABLE)
                result = {"state": "empty", "rows": 0}
            summary["unchanged" if result["state"] == "unchanged" else "loaded"] += 1
            summary["records"] += len(records)
            summary["rows"] += result["rows"]
            pending.pop(0)
            segments[key] = {"fetched": str(today), "records": len(records)}
            state = save_state(ctx, db, "idigbio-fossils", {**state, "pending": pending, "segments": segments})
        return {**summary, "pending": len(pending), "segments": len(segments)}
    finally:
        db.close()
