"""SQL feed for species records in Kansas: GBIF occurrences, through the occurrence search API.

``gbif``: the Global Biodiversity Information Facility (https://api.gbif.org/v1/occurrence/search, no key; docs
https://techdocs.gbif.org/en/openapi/v1/occurrence). A ``BULK_FEEDS`` feed: rows go in ``kfm_gbif_occurrences`` in
``--bulk-db``. On 2026-11-03 Kansas held about 10.46 million records, 8.4 million of them eBird, in about 1,180 datasets.
The live plan was 11,705 segments and 42,394 pages: about 44,000 requests with planning and dataset records, 55 GB of
answers, about 12 GB in the database (1.2 KB a row with indexes) and 1 GB of kept copies (70-160 B a row gzipped).

Licence and citation: every record carries its dataset's licence (CC0, CC BY or CC BY-NC), kept per row in ``license``
with ``dataset_key`` and ``publishing_org_key``. ``kfm_gbif_datasets`` keeps each dataset's title, DOI, licence and
GBIF's citation text, for citing what is used (https://www.gbif.org/citation-guidelines; terms
https://www.gbif.org/terms). The search API has no single download DOI; a published work should register a derived
dataset at GBIF from ``dataset_key`` counts. GBIF's API documentation (https://techdocs.gbif.org/en/openapi/) says a
search script taking more than 15 minutes is usually better replaced by its download API, which needs a registered
account; that account is the owner's decision, so this feed uses search, slowly.

Which records: GBIF's search cannot OR two fields or negate one, so the scope is built from queries that do not
overlap, the roots of the segment tree:

- ``gadm``: ``gadmGid=USA.17_1``, coordinates inside GADM's Kansas, whatever the record's stateProvince says.
- ``no-coordinates``: ``country=US``, ``hasCoordinate=false``, stateProvince one of ``GBIF_STATE_NAMES``. stateProvince
  matches exactly, so each spelling seen is listed; those naming several states are included and kept as published.
- ``south-of-box``, ``north-of-box``, ``west-of-box``, ``east-of-box``: the same stateProvince test with coordinates
  outside the Kansas box.
- ``box-other-gadm``: the same test inside the box, each GADM state other than Kansas (a record on the Missouri side of
  the line). Records inside the box with no GADM state at all cannot be selected: they are counted in ``gap_rows``
  (8,697 on 2026-11-03) and not loaded.

Segments: search pages at 300 records. The documented limit is an offset of 100,000, but on 2026-11-03 any offset of
10,000 or more stalled for minutes without finishing, on broad and narrow queries alike, while 9,700 answered in 3 s.
So a segment holds at most ``GBIF_WINDOW`` (10,000) records. ``kfm_gbif_segments`` holds the tree. A node over the
window is split on the first of ``GBIF_DIMENSIONS`` that divides it completely, using one facet request (a record with
no year is in no year's facet, so such a node is split another way, usually by county); where no dimension is complete
the one leaving out the fewest records is used and the rest go in ``gap_rows``. A node that cannot be split at all
keeps its first 10,000 records, marked ``truncated``. Together these left 49,550 records out of reach on 2026-11-03
(0.47%), listed by node in the table: ``SELECT key, gap_rows FROM kfm_gbif_segments WHERE gap_rows > 0``. A leaf is one
``load_version`` key (``segment/<tree path>``)
kept as ``segments/<tree path>-<sha12>.jsonl.gz``, so a stop, an outage or the window loses at most one unfinished
leaf of 34 pages and the next run carries on from the tree.

Each run, within ``max_requests`` (400) and ``max_seconds`` (1,800), 1 s apart: splits unsplit nodes, fetches dataset
records (at most a fifth of the budget), loads unloaded leaves smallest first (a run reaches many datasets long before
the eBird days), then refreshes. A 429 or 403 stops with ``GBIF_RATE_LIMITED``, and a 5xx, an HTML answer or a
connection failure with ``GBIF_UNAVAILABLE``; GBIF's rate depends on its load, so neither is pushed against, and
everything finished stays. ``lastInterpreted`` and the like change whenever GBIF reprocesses a dataset, so the kept
record leaves them out, and a re-fetched leaf with the same records is recognized as unchanged. A leaf that moved while
being paged (rows not matching the count) is tried again next run, and loaded as it stands, noted ``shifted``, at the
third try.

Refresh, once the backfill is done: a leaf or split node covering a recent year (this or the previous one, or no year
filter) is due every 28 days, older ones every 365. A due split node repeats its facet: a new value becomes a node, a
vanished one is retired with its rows, and a leaf grown past the window is retired and split (its rows return as its
children load). A due leaf with the planned row count first asks how many of its records were reinterpreted since it
was loaded (``lastInterpreted=<date>,*``, one request); none means no re-fetch. Dataset records are fetched again every
182 days. Feed state: ``requests_total``, ``runs``, ``backfill_done``, ``last_stop``; the plan is in the table, so
``status`` stays small.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
import gzip
import hashlib
import json
from math import ceil
from pathlib import Path
import re
import time
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_bulk import open_bulk_db
from tools.local_data.sql_feed_hazards import ddl, keep_version, loaded_keys, retire, save_state, snake
from tools.local_data.sql_feeds import FeedError

GBIF_FEED = "gbif"
GBIF_SEARCH = "https://api.gbif.org/v1/occurrence/search"
GBIF_DATASET = "https://api.gbif.org/v1/dataset/{key}"
GBIF_TERMS = "https://www.gbif.org/terms"
GBIF_CITATION_GUIDE = "https://www.gbif.org/citation-guidelines"
GBIF_LICENSE = "per record: see license and dataset_key (CC0 1.0, CC BY 4.0 or CC BY-NC 4.0)"
GBIF_SOURCE, GBIF_DATASET_SOURCE = "gbif-occurrence-search", "gbif-dataset-registry"
GBIF_PAGE = 300            # the API's largest page
GBIF_WINDOW = 10_000       # offsets at and beyond this stalled on 2026-11-03 (module docstring)
GBIF_PAUSE = 1.0
GBIF_TIMEOUT = 120
GBIF_RESPONSE_LIMIT = 64_000_000
GBIF_FACET_LIMIT = 3000
GBIF_RECENT_DAYS, GBIF_OLD_DAYS, GBIF_DATASET_DAYS = 28, 365, 182
GBIF_SHIFT_TRIES = 3
GBIF_GADM_KANSAS = "USA.17_1"
GBIF_BOX = (-102.06, 36.99, -94.58, 40.01)   # west, south, east, north
GBIF_DIMENSIONS = ("datasetKey", "year", "month", "day", "gadmLevel2Gid", "basisOfRecord", "institutionCode", "collectionCode",
                   "familyKey", "orderKey", "classKey", "kingdomKey", "genusKey", "speciesKey", "recordedBy")
# The spellings GBIF's stateProvince facets showed on 2026-11-03 (facet values with one record are not listed by GBIF).
GBIF_STATE_NAMES = ("Kansas", "kansas", "Ks", "Kansas?", "Kansas (?)", "Kansas (KS)", "Kansas (State)", "Kansas (堪薩斯州)", "KAN[sas]", "Kan.",
                    "Kanas", "Kansa", "Colorado, Kansas", "Kansas - Nebraska", "Nebraska or Kansas", "Kansas - Oklahoma", "Oklahoma or Kansas",
                    "Kansas or South Dakota", "Kansas/Missouri", "Kansas/Nebraska", "CO & KS", "KS & CO", "Colorado - Kansas - Nebraska - Wyoming",
                    "Colorado - Kansas - New Mexico - Oklahoma", "Douglas Cy, Kansas", "Midland, Kansas", "Osage Co. Kansas")


def _named() -> list:
    return [("country", "US"), *(("stateProvince", name) for name in GBIF_STATE_NAMES)]


def _ranges(lat: tuple, lon: tuple | None = None) -> list:
    return [("hasCoordinate", "true"), ("decimalLatitude", f"{lat[0]},{lat[1]}"), *([("decimalLongitude", f"{lon[0]},{lon[1]}")] if lon else [])]


_W, _S, _E, _N = GBIF_BOX
GBIF_ROOTS = {
    "gadm": [("gadmGid", GBIF_GADM_KANSAS)],
    "no-coordinates": [*_named(), ("hasCoordinate", "false")],
    "south-of-box": [*_named(), *_ranges((-90, _S))],
    "north-of-box": [*_named(), *_ranges((_N, 90))],
    "west-of-box": [*_named(), *_ranges((_S, _N), (-180, _W))],
    "east-of-box": [*_named(), *_ranges((_S, _N), (_E, 180))],
    "box-other-gadm": [*_named(), *_ranges((_S, _N), (_W, _E))],
}
GBIF_ROOT_DIMENSIONS = {"box-other-gadm": ("gadmLevel1Gid",)}   # always split, and on this alone
GBIF_ROOT_EXCLUDE = {"box-other-gadm": {GBIF_GADM_KANSAS}}      # those are the gadm root's

# --- The kept record and its row -------------------------------------------------------------------

_NAMES = {"gbifID": "gbif_id", "occurrenceID": "occurrence_id", "class": "class_name", "order": "order_name", "eventID": "event_id", "references": "reference_url",
          "coordinateUncertaintyInMeters": "coordinate_uncertainty_m", "elevation": "elevation_m", "gadmLevel1Gid": "gadm_level1_gid",
          "gadmLevel2Gid": "gadm_level2_gid", "gadmLevel2Name": "gadm_level2_name"}
GBIF_FIELDS = ["gbifID", "occurrenceID", "datasetKey", "datasetName", "publishingOrgKey", "license", "rightsHolder", "accessRights", "informationWithheld",
               "dataGeneralizations", "basisOfRecord", "occurrenceStatus", "individualCount", "taxonKey", "acceptedTaxonKey", "scientificName",
               "acceptedScientificName", "taxonRank", "taxonomicStatus", "kingdom", "phylum", "class", "order", "family", "genus", "species", "kingdomKey",
               "phylumKey", "classKey", "orderKey", "familyKey", "genusKey", "speciesKey", "vernacularName", "iucnRedListCategory", "eventDate", "year",
               "month", "day", "verbatimEventDate", "decimalLatitude", "decimalLongitude", "coordinateUncertaintyInMeters", "coordinatePrecision", "elevation",
               "stateProvince", "county", "municipality", "locality", "verbatimLocality", "gadmLevel1Gid", "gadmLevel2Gid", "gadmLevel2Name", "recordedBy",
               "identifiedBy", "dateIdentified", "institutionCode", "collectionCode", "catalogNumber", "recordNumber", "typeStatus", "sex", "lifeStage",
               "establishmentMeans", "habitat", "occurrenceRemarks", "eventID", "references", "modified"]
GBIF_COLUMNS = [_NAMES.get(f, snake(f)) for f in GBIF_FIELDS] + ["media_count", "issues_json", "extra_json"]
GBIF_TYPES = {"gbif_id": "INTEGER NOT NULL", "dataset_key": "TEXT NOT NULL", "individual_count": "INTEGER", "year": "INTEGER", "month": "INTEGER", "day": "INTEGER",
              "decimal_latitude": "REAL", "decimal_longitude": "REAL", "coordinate_uncertainty_m": "REAL", "coordinate_precision": "REAL", "elevation_m": "REAL",
              "media_count": "INTEGER", **{snake(k): "INTEGER" for k in ("taxonKey", "acceptedTaxonKey", "kingdomKey", "phylumKey", "classKey", "orderKey",
                                                                         "familyKey", "genusKey", "speciesKey")}}
GBIF_TABLE, GBIF_DATASET_TABLE, GBIF_SEGMENT_TABLE, GBIF_DATASET_QUEUE = "kfm_gbif_occurrences", "kfm_gbif_datasets", "kfm_gbif_segments", "kfm_gbif_dataset_queue"
GBIF_DATASET_COLUMNS = ["dataset_key", "title", "doi", "license", "citation", "publishing_org_key", "type", "homepage", "pub_date", "modified"]
GBIF_DDL = (ddl(GBIF_TABLE, GBIF_COLUMNS, GBIF_TYPES, [("gbif_id",), ("dataset_key",), ("species_key", "year"), ("year", "month"), ("gadm_level2_gid",)])
            + ddl(GBIF_DATASET_TABLE, GBIF_DATASET_COLUMNS, {"dataset_key": "TEXT NOT NULL"}, [("dataset_key",)])
            + f"""CREATE TABLE IF NOT EXISTS {GBIF_SEGMENT_TABLE} (key TEXT PRIMARY KEY, query_json TEXT NOT NULL, kind TEXT NOT NULL,
 split_dimension TEXT, planned_rows INTEGER, gap_rows INTEGER NOT NULL DEFAULT 0, loaded_rows INTEGER, loaded_on TEXT, checked_on TEXT,
 tries INTEGER NOT NULL DEFAULT 0, note TEXT) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS {GBIF_SEGMENT_TABLE}_kind ON {GBIF_SEGMENT_TABLE}(kind, loaded_on, planned_rows);
CREATE TABLE IF NOT EXISTS {GBIF_DATASET_QUEUE} (dataset_key TEXT PRIMARY KEY, fetched_on TEXT, note TEXT) WITHOUT ROWID;
""")
_REST_LEFT_OUT = frozenset({
    # GBIF's processing, which changes without the record changing, and bookkeeping
    "key", "crawlId", "lastCrawled", "lastParsed", "lastInterpreted", "installationKey", "hostingOrganizationKey", "protocol", "datasetCategory", "networkKeys",
    "publishedByGbifRegion", "gbifRegion", "publishingCountry", "isInCluster", "isSequenced", "dnaSequenceID", "nucleotideSequence", "identifiers", "identifier",
    "facts", "relations", "startDayOfYear", "endDayOfYear", "genericName", "specificEpithet", "infraspecificEpithet", "scientificNameAuthorship", "continent",
    "country", "countryCode", "geodeticDatum", "publisher",
    # large and derivable: other checklists' classifications, multimedia details and the GADM tree (levels 1 and 2 are columns)
    "classifications", "extensions", "gadm", "media", "issues"})


def kept_record(record: dict) -> dict:
    """What is kept of one API record: the Darwin Core fields (GBIF_FIELDS), issues, a media count, and in ``extra`` the
    rest, except what changes by itself or is large and derivable (5-7 KB a record comes down to about 1.5 KB)."""
    gadm = record.get("gadm") if isinstance(record.get("gadm"), dict) else {}
    kept = {f: record[f] for f in GBIF_FIELDS if record.get(f) not in (None, "", [])}
    identifier = record.get("gbifID", record.get("key"))
    if identifier is None:
        raise FeedError("GBIF_RECORD_WITHOUT_ID")
    kept["gbifID"] = int(identifier)
    for field, level, part in (("gadmLevel1Gid", "level1", "gid"), ("gadmLevel2Gid", "level2", "gid"), ("gadmLevel2Name", "level2", "name")):
        value = (gadm.get(level) or {}).get(part)
        if value:
            kept[field] = value
    if record.get("issues"):
        kept["issues"] = sorted(record["issues"])
    if record.get("media"):
        kept["mediaCount"] = len(record["media"])
    extra = {k: v for k, v in record.items() if k not in _REST_LEFT_OUT and k not in kept and not k.startswith("http://unknown.org/") and v not in (None, "", [], {})}
    if extra:
        kept["extra"] = extra
    return kept


def _cell(value):
    """A value as SQLite takes it: GBIF gives some Darwin Core fields as lists (typeStatus) or objects (sex, lifeStage)."""
    return core.canonical(value) if isinstance(value, (list, dict)) else int(value) if isinstance(value, bool) else value


def _row(kept: dict) -> tuple:
    return (*(_cell(kept.get(f)) for f in GBIF_FIELDS), kept.get("mediaCount"),
            core.canonical(kept["issues"]) if kept.get("issues") else None, core.canonical(kept["extra"]) if kept.get("extra") else None)


def _segment_rows(path: Path):
    """Table rows from a kept segment, after its first line, which names the segment."""
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        next(handle)
        for line in handle:
            yield _row(json.loads(line))


# --- The API ----------------------------------------------------------------------------------------

class _Client:
    """GBIF requests within the run's budget, spaced apart. Fixed reasons for a provider that says stop."""

    def __init__(self, ctx, max_requests: int, max_seconds: int):
        self.ctx, self.max_requests, self.deadline = ctx, max_requests, time.monotonic() + max_seconds
        self.requests, self.bytes = 0, 0

    def left(self) -> int:
        return 0 if time.monotonic() >= self.deadline else self.max_requests - self.requests

    def get(self, url: str, *, missing_ok: bool = False) -> tuple[dict | None, object]:
        if self.requests:
            time.sleep(getattr(self.ctx, "pause", GBIF_PAUSE))
        self.requests += 1
        try:
            fetched = self.ctx.fetch(url, limit=GBIF_RESPONSE_LIMIT, timeout=GBIF_TIMEOUT, missing_ok=missing_ok, attempts=2)
        except FeedError as error:
            reason = str(error)
            if reason.startswith(("HTTP_429", "HTTP_403")):
                self.ctx.note("gbif_stopped", url=url, reason=reason[:40])
                raise FeedError("GBIF_RATE_LIMITED") from None
            if reason.startswith(("HTTP_5", "FETCH_FAILED")):
                self.ctx.note("gbif_stopped", url=url, reason=reason[:40])
                raise FeedError("GBIF_UNAVAILABLE") from None
            raise
        if fetched is None:
            return None, None
        self.bytes += len(fetched.body)
        if fetched.body.lstrip()[:1] != b"{":
            self.ctx.note("gbif_stopped", url=url, reason="not JSON")
            raise FeedError("GBIF_UNAVAILABLE")
        try:
            return json.loads(fetched.body), fetched
        except ValueError:
            raise FeedError("GBIF_UNAVAILABLE") from None

    def count(self, query: list, **more) -> int:
        answer, _ = self.get(search_url(query, limit=0, **more))
        return _count(answer)

    def facet(self, query: list, dimension: str) -> tuple[int, dict]:
        answer, _ = self.get(search_url(query, limit=0, facet=dimension, facetLimit=GBIF_FACET_LIMIT))
        counts = {}
        for facet in answer.get("facets") or []:
            for entry in facet.get("counts") or []:
                counts[str(entry["name"])] = int(entry["count"])
        return _count(answer), counts


def search_url(query: list, **more) -> str:
    """The occurrence search URL for query's (param, value) pairs and more parameters; commas stay literal in ranges."""
    return GBIF_SEARCH + "?" + urllib.parse.urlencode([*query, *more.items()], safe=",*")


def _count(answer: dict) -> int:
    if not isinstance(answer.get("count"), int):
        raise FeedError("GBIF_RESPONSE_SHAPE")
    return answer["count"]


# --- The segment tree -------------------------------------------------------------------------------

def _child_key(key: str, dimension: str, value: str) -> str:
    safe = re.sub(r"[^\w.-]", "_", value, flags=re.ASCII)[:60]
    if safe != value:
        safe += "-" + hashlib.sha256(value.encode()).hexdigest()[:8]
    return f"{key}/{dimension}-{safe}"


def _seed(ctx, db) -> None:
    with core.pipeline_lock(ctx):
        for root, query in GBIF_ROOTS.items():
            db.execute(f"INSERT OR IGNORE INTO {GBIF_SEGMENT_TABLE}(key, query_json, kind) VALUES (?,?,'open')", (root, json.dumps(query, ensure_ascii=False)))


def _subtree(db, key: str) -> list:
    return db.execute(f"SELECT key, kind, loaded_on FROM {GBIF_SEGMENT_TABLE} WHERE key=? OR key LIKE ? ESCAPE '\\'",
                      (key, _like(key) + "/%")).fetchall()


def _retire_tree(ctx, db, key: str) -> int:
    """Retire a node that left the provider: its loaded leaves' rows go and the nodes are forgotten."""
    gone = 0
    with core.pipeline_lock(ctx):
        for node, kind, loaded_on in _subtree(db, key):
            if kind == "leaf" and loaded_on:
                gone += retire(db, GBIF_SOURCE, f"segment/{node}", GBIF_TABLE)
            db.execute(f"DELETE FROM {GBIF_SEGMENT_TABLE} WHERE key=?", (node,))
    return gone


def _install(ctx, db, key: str, query: list, dimension: str, total: int, counts: dict, today: date, summary: dict) -> None:
    """Record a split: children for each facet value (new ones added; ones grown past the window reopened; ones gone
    retired), and what the facet could not reach as the gap."""
    root = key.split("/", 1)[0]
    exclude = GBIF_ROOT_EXCLUDE.get(root, set()) if "/" not in key else set()
    gap = max(0, total - sum(counts.values()))
    wanted = {_child_key(key, dimension, value): (value, n) for value, n in counts.items() if n > 0 and value not in exclude}
    known = {k: (kind, loaded, note) for k, kind, loaded, note in db.execute(
        f"SELECT key, kind, loaded_on, note FROM {GBIF_SEGMENT_TABLE} WHERE key LIKE ? ESCAPE '\\' AND key NOT LIKE ? ESCAPE '\\'",
        (_like(key) + "/%", _like(key) + "/%/%"))}
    for child in known.keys() - wanted.keys():
        summary["retired"] += _retire_tree(ctx, db, child)
    with core.pipeline_lock(ctx):
        for child, (value, n) in wanted.items():
            if child not in known:
                db.execute(f"INSERT INTO {GBIF_SEGMENT_TABLE}(key, query_json, kind, planned_rows) VALUES (?,?,?,?)",
                           (child, json.dumps([*query, [dimension, value]], ensure_ascii=False), "leaf" if n <= GBIF_WINDOW else "open", n))
                continue
            kind, loaded, note = known[child]
            if kind == "leaf" and n > GBIF_WINDOW and note != "truncated":
                if loaded:
                    retire(db, GBIF_SOURCE, f"segment/{child}", GBIF_TABLE)
                db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET kind='open', planned_rows=?, loaded_on=NULL, loaded_rows=NULL, note=NULL WHERE key=?", (n, child))
            else:
                db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET planned_rows=? WHERE key=?", (n, child))
        db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET kind='split', split_dimension=?, planned_rows=?, gap_rows=?, checked_on=? WHERE key=?",
                   (dimension, total, gap, str(today), key))
        if dimension == "datasetKey":
            db.executemany(f"INSERT OR IGNORE INTO {GBIF_DATASET_QUEUE}(dataset_key) VALUES (?)", [(v,) for v in counts])


def _like(key: str) -> str:
    return key.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def _split_open(ctx, db, client: _Client, today: date, summary: dict) -> None:
    """Split or settle the nodes not yet decided, as far as the budget goes."""
    while True:
        nodes = db.execute(f"SELECT key, query_json FROM {GBIF_SEGMENT_TABLE} WHERE kind='open' ORDER BY key").fetchall()
        if not nodes:
            return
        for key, query_json in nodes:
            query = [tuple(pair) for pair in json.loads(query_json)]
            if not _split_one(ctx, db, client, key, query, today, summary):
                return


def _split_one(ctx, db, client: _Client, key: str, query: list, today: date, summary: dict) -> bool:
    used = {param for param, _ in query}
    forced = key in GBIF_ROOT_DIMENSIONS
    best, total = None, None
    for dimension in GBIF_ROOT_DIMENSIONS.get(key, GBIF_DIMENSIONS):
        if dimension in used:
            continue
        if client.left() <= 0:
            return False
        total, counts = client.facet(query, dimension)
        if total <= GBIF_WINDOW and not forced:
            with core.pipeline_lock(ctx):
                db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET kind='leaf', planned_rows=?, loaded_on=NULL WHERE key=?", (total, key))
            return True
        gap = max(0, total - sum(counts.values()))
        narrows = counts and (len(counts) > 1 or gap > 0) and max(counts.values()) < total
        if not narrows and not forced:
            continue
        if best is None or gap < best[2]:
            best = (dimension, counts, gap)
        if gap == 0:
            break
    if best is None:
        # Nothing divides it: its first window of records is all the API gives.
        gap = max(0, (total or 0) - GBIF_WINDOW)
        with core.pipeline_lock(ctx):
            db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET kind='leaf', planned_rows=?, gap_rows=?, note='truncated' WHERE key=?", (total, gap, key))
        return True
    _install(ctx, db, key, query, best[0], total, best[1], today, summary)
    return True


def _is_recent(query: list, today: date) -> bool:
    years = [int(value) for param, value in query if param == "year"]
    return not years or max(years) >= today.year - 1


def _due(query_json: str, checked_on: str | None, today: date) -> bool:
    if not checked_on:
        return True
    query = [tuple(pair) for pair in json.loads(query_json)]
    return (today - date.fromisoformat(checked_on)).days >= (GBIF_RECENT_DAYS if _is_recent(query, today) else GBIF_OLD_DAYS)


def _refresh_splits(ctx, db, client: _Client, today: date, summary: dict) -> None:
    """Repeat the facet of each due split node, parents first (a retired parent takes its children with it)."""
    rows = db.execute(f"SELECT key, query_json, split_dimension, checked_on FROM {GBIF_SEGMENT_TABLE} WHERE kind='split' ORDER BY key").fetchall()
    for key, query_json, dimension, checked_on in rows:
        if not _due(query_json, checked_on, today) or not db.execute(f"SELECT 1 FROM {GBIF_SEGMENT_TABLE} WHERE key=?", (key,)).fetchone():
            continue
        if client.left() <= 0:
            return
        query = [tuple(pair) for pair in json.loads(query_json)]
        total, counts = client.facet(query, dimension)
        _install(ctx, db, key, query, dimension, total, counts, today, summary)
        summary["splits_checked"] += 1


# --- Datasets ---------------------------------------------------------------------------------------

_ACCESSED = re.compile(r"\s*accessed via GBIF\.org on \d{4}-\d{2}-\d{2}\.?\s*$")


def _dataset_kept(record: dict) -> dict:
    citation = record.get("citation") if isinstance(record.get("citation"), dict) else {}
    return {"datasetKey": record.get("key"), "title": record.get("title"), "doi": record.get("doi"), "license": record.get("license"),
            "citation": _ACCESSED.sub("", citation.get("text") or "") or None, "publishingOrganizationKey": record.get("publishingOrganizationKey"),
            "type": record.get("type"), "homepage": record.get("homepage"), "pubDate": record.get("pubDate"), "modified": record.get("modified")}


def _dataset_rows(path: Path):
    kept = json.loads(gzip.decompress(path.read_bytes()))
    yield (kept["datasetKey"], kept["title"], kept["doi"], kept["license"], kept["citation"], kept["publishingOrganizationKey"],
           kept["type"], kept["homepage"], kept["pubDate"], kept["modified"])


def _fetch_datasets(ctx, db, client: _Client, today: date, allowance: int, summary: dict) -> None:
    """Dataset records (licence, DOI, citation text), up to allowance requests."""
    due = []
    for key, fetched_on in db.execute(f"SELECT dataset_key, fetched_on FROM {GBIF_DATASET_QUEUE} ORDER BY dataset_key").fetchall():
        if not fetched_on or (today - date.fromisoformat(fetched_on)).days >= GBIF_DATASET_DAYS:
            due.append(key)
    for key in due[:allowance]:
        if client.left() <= 0:
            break
        url = GBIF_DATASET.format(key=key)
        record, fetched = client.get(url, missing_ok=True)
        if record is None:
            with core.pipeline_lock(ctx):
                db.execute(f"UPDATE {GBIF_DATASET_QUEUE} SET fetched_on=?, note='missing' WHERE dataset_key=?", (str(today), key))
            continue
        kept = _dataset_kept({**record, "key": record.get("key", key)})
        body = core.gz(core.canonical(kept).encode())
        result = keep_version(ctx, db, feed=GBIF_FEED, source_id=GBIF_DATASET_SOURCE, key=f"dataset/{key}", name=f"datasets/{key}", ext=".json.gz", body=body,
                              url=url, fetched=fetched, table=GBIF_DATASET_TABLE, width=len(GBIF_DATASET_COLUMNS), rows=_dataset_rows,
                              extra={"license": record.get("license"), "citation": kept["citation"], "doi": record.get("doi"), "terms": GBIF_TERMS,
                                     "accessed": str(today), "citation_guidelines": GBIF_CITATION_GUIDE})
        summary["datasets"] += 1 if result["state"] != "unchanged" else 0
        with core.pipeline_lock(ctx):
            db.execute(f"UPDATE {GBIF_DATASET_QUEUE} SET fetched_on=?, note=NULL WHERE dataset_key=?", (str(today), key))
    summary["datasets_pending"] = max(0, len(due) - allowance)


# --- Leaves -----------------------------------------------------------------------------------------

def _pages(rows: int) -> int:
    return max(1, ceil(min(rows, GBIF_WINDOW) / GBIF_PAGE))


def _fetch_leaf(client: _Client, query: list, whole: bool) -> tuple[dict, int, int, str, object, int]:
    """Page one leaf: ({gbif id: kept record}, the count reported, pages, sha256 of the answers, the last Fetched, answer
    bytes). A leaf that must be whole (not marked truncated) and has outgrown the window stops at its first page."""
    records, digest, reported, offset, pages, fetched, size = {}, hashlib.sha256(), None, 0, 0, None, 0
    while True:
        answer, fetched = client.get(search_url(query, offset=offset, limit=min(GBIF_PAGE, GBIF_WINDOW - offset)))
        digest.update(fetched.body)
        size += len(fetched.body)
        pages += 1
        reported = _count(answer)
        if whole and reported > GBIF_WINDOW:
            return {}, reported, pages, digest.hexdigest(), fetched, size
        results = answer.get("results")
        if not isinstance(results, list):
            raise FeedError("GBIF_RESPONSE_SHAPE")
        for record in results:
            kept = kept_record(record)
            records[kept["gbifID"]] = kept
        offset += len(results)
        if answer.get("endOfRecords") or not results or offset >= min(reported, GBIF_WINDOW):
            return records, reported, pages, digest.hexdigest(), fetched, size


def _load_leaf(ctx, db, key: str, query: list, records: dict, reported: int, pages: int, digest: str, fetched, size: int, truncated: bool) -> dict:
    segment = f"segment/{key}"
    ordered = [records[i] for i in sorted(records)]
    lines = [core.canonical({"segment": segment})] + [core.canonical(r) for r in ordered]
    body = core.gz("".join(line + "\n" for line in lines).encode())
    licenses, datasets = Counter(r.get("license") for r in ordered), Counter(r.get("datasetKey") for r in ordered)
    extra = {"citation": f"GBIF.org occurrence search, accessed {ctx.now().date()}; cite each dataset from kfm_gbif_datasets",
             "citation_guidelines": GBIF_CITATION_GUIDE, "license": GBIF_LICENSE, "terms": GBIF_TERMS, "query": query, "records": len(ordered),
             "reported_count": reported, "pages": pages, "api_bytes": size, "api_sha256": digest, "licenses": dict(licenses),
             "datasets": dict(datasets), **({"truncated": True} if truncated else {})}
    result = keep_version(ctx, db, feed=GBIF_FEED, source_id=GBIF_SOURCE, key=segment, name=f"segments/{key}", ext=".jsonl.gz", body=body, url=fetched.url,
                          fetched=fetched, table=GBIF_TABLE, width=len(GBIF_COLUMNS), rows=_segment_rows, extra=extra)
    with core.pipeline_lock(ctx):
        db.executemany(f"INSERT OR IGNORE INTO {GBIF_DATASET_QUEUE}(dataset_key) VALUES (?)", [(k,) for k in datasets if k])
    return result


def _pull_leaf(ctx, db, client: _Client, node: tuple, today: date, summary: dict) -> None:
    """Fetch and load one leaf, or put it back in the plan when it has outgrown the window or moved while being paged."""
    key, query_json, planned, tries, note = node
    query = [tuple(pair) for pair in json.loads(query_json)]
    truncated = note == "truncated"
    records, reported, pages, digest, fetched, size = _fetch_leaf(client, query, not truncated)
    if reported > GBIF_WINDOW and not truncated:
        with core.pipeline_lock(ctx):
            if f"segment/{key}" in loaded_keys(db, GBIF_SOURCE):
                retire(db, GBIF_SOURCE, f"segment/{key}", GBIF_TABLE)
            db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET kind='open', planned_rows=?, loaded_on=NULL, loaded_rows=NULL WHERE key=?", (reported, key))
        summary["reopened"] += 1
        return
    shifted = len(records) != min(reported, GBIF_WINDOW)
    if shifted and tries + 1 < GBIF_SHIFT_TRIES:
        with core.pipeline_lock(ctx):
            db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET tries=?, note='shifted' WHERE key=?", (tries + 1, key))
        summary["shifted"] += 1
        return
    if records:
        result = _load_leaf(ctx, db, key, query, records, reported, pages, digest, fetched, size, truncated)
        summary["rows"] += result["rows"]
        summary["segments_unchanged" if result["state"] == "unchanged" else "segments_loaded"] += 1
    elif f"segment/{key}" in loaded_keys(db, GBIF_SOURCE):
        with core.pipeline_lock(ctx):
            summary["retired"] += retire(db, GBIF_SOURCE, f"segment/{key}", GBIF_TABLE)
    with core.pipeline_lock(ctx):
        db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET planned_rows=?, loaded_rows=?, loaded_on=?, checked_on=?, tries=0, note=? WHERE key=?",
                   (reported, len(records), str(today), str(today), "truncated" if truncated else "shifted" if shifted else None, key))


def _load_new(ctx, db, client: _Client, today: date, summary: dict) -> None:
    """Load unloaded leaves, smallest first, while the budget admits the next whole leaf."""
    nodes = db.execute(f"SELECT key, query_json, planned_rows, tries, note FROM {GBIF_SEGMENT_TABLE} WHERE kind='leaf' AND loaded_on IS NULL "
                       "ORDER BY planned_rows, key").fetchall()
    for node in nodes:
        if client.left() < _pages(node[2] or 1):
            return
        _pull_leaf(ctx, db, client, node, today, summary)


def _refresh_leaves(ctx, db, client: _Client, today: date, summary: dict) -> None:
    """Refresh due leaves: a count of records reinterpreted since the load, then a re-fetch only when any are."""
    nodes = db.execute(f"SELECT key, query_json, planned_rows, tries, note, loaded_rows, loaded_on, checked_on FROM {GBIF_SEGMENT_TABLE} "
                       "WHERE kind='leaf' AND loaded_on IS NOT NULL ORDER BY checked_on, key").fetchall()
    for key, query_json, planned, tries, note, loaded_rows, loaded_on, checked_on in nodes:
        if not _due(query_json, checked_on, today):
            continue
        if client.left() < 1 + _pages(planned or 1):
            return
        query = [tuple(pair) for pair in json.loads(query_json)]
        same_size = min(planned or 0, GBIF_WINDOW) == loaded_rows
        if same_size and not client.count(query, lastInterpreted=f"{loaded_on},*"):
            with core.pipeline_lock(ctx):
                db.execute(f"UPDATE {GBIF_SEGMENT_TABLE} SET checked_on=? WHERE key=?", (str(today), key))
            summary["segments_checked"] += 1
            continue
        _pull_leaf(ctx, db, client, (key, query_json, planned, tries, note), today, summary)


def _plan_counts(db) -> dict:
    row = db.execute(f"""SELECT SUM(kind='open'), SUM(kind='leaf'), SUM(kind='leaf' AND loaded_on IS NULL), SUM(CASE WHEN kind='leaf' THEN planned_rows END),
        SUM(CASE WHEN kind='leaf' AND loaded_on IS NULL THEN planned_rows END), SUM(CASE WHEN kind='leaf' THEN COALESCE(loaded_rows,0) END),
        SUM(gap_rows), SUM(CASE WHEN kind='leaf' AND loaded_on IS NULL THEN MAX(1, (MIN(planned_rows, ?) + ? - 1) / ?) END)
        FROM {GBIF_SEGMENT_TABLE}""", (GBIF_WINDOW, GBIF_PAGE, GBIF_PAGE)).fetchone()
    return dict(zip(("nodes_open", "segments", "segments_pending", "rows_planned", "rows_pending", "rows_loaded", "gap_rows", "pages_pending"),
                    (v or 0 for v in row)))


def gbif(ctx, max_requests: int = 400, max_seconds: int = 1800) -> dict:
    """GBIF occurrences in Kansas, keeping licence, dataset and citation per record, through resumable segments. Each
    run spends at most max_requests requests and max_seconds; see the module docstring for the plan and the stops."""
    db = open_bulk_db(ctx)
    client = _Client(ctx, max_requests, max_seconds)
    today = ctx.now().date()
    summary = {"rows": 0, "segments_loaded": 0, "segments_unchanged": 0, "segments_checked": 0, "splits_checked": 0, "retired": 0, "reopened": 0, "shifted": 0,
               "datasets": 0, "datasets_pending": 0}
    try:
        with core.pipeline_lock(ctx):
            db.executescript(GBIF_DDL)
        state = core.get_state(db, GBIF_FEED)
        _seed(ctx, db)
        stop = None
        try:
            if state.get("backfill_done"):
                _refresh_splits(ctx, db, client, today, summary)
            _split_open(ctx, db, client, today, summary)
            if not _plan_counts(db)["nodes_open"]:
                _fetch_datasets(ctx, db, client, today, max(1, max_requests // 5), summary)
            _load_new(ctx, db, client, today, summary)
            plan = _plan_counts(db)
            if not plan["nodes_open"] and not plan["segments_pending"]:
                state = {**state, "backfill_done": state.get("backfill_done") or str(today)}
                _refresh_leaves(ctx, db, client, today, summary)
        except FeedError as error:
            if not str(error).startswith(("GBIF_RATE_LIMITED", "GBIF_UNAVAILABLE")):
                raise
            stop = error
        plan = _plan_counts(db)
        state = {**state, "requests_total": state.get("requests_total", 0) + client.requests, "runs": state.get("runs", 0) + 1,
                 "last_stop": str(stop) if stop else None, "plan": plan}
        save_state(ctx, db, GBIF_FEED, state)
        if stop:
            raise stop
        return {**summary, **plan, "requests": client.requests, "api_bytes": client.bytes, "backfill_done": state.get("backfill_done")}
    finally:
        db.close()
