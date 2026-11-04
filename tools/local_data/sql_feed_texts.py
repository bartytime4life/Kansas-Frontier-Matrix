"""SQL feeds for Kansas texts and registers: Internet Archive full text, the LOC newspaper directory and FCC towers.

Rebuilds three feeds whose code was lost before they had loaded anything (``archive-texts``, ``newspaper-directory``,
``towers``), so no earlier kept file or receipt constrains them; the ``kfm_asr_*`` tables already existed empty in
``observations.sqlite`` and their DDL is reproduced exactly. Each provider answer is cut to Kansas and kept gzipped
under ``data/raw/sql-feeds/<feed>/`` as ``<name>-<sha12><ext>``, then loaded with ``load_version`` under a stable
key, so a changed version replaces the one before it in one transaction and an unchanged one is not loaded again.
Network work runs outside the pipeline lock; database writes inside it. The owner removed the size ceiling on
2026-11-02 ("ignore all data caps and floors"), so nothing here limits a feed's total size. The per-run budgets
are for politeness and for the shared timers; what is left waits for the next run.

``archive-texts`` (bulk database, ``--bulk-db``): Internet Archive items with ``mediatype:texts AND (subject:kansas
OR title:kansas)``, from the Scrape API (https://archive.org/services/search/v1/scrape, cursor paging, 30,409 items
on 2026-11-03). Terms: https://archive.org/about/terms.php. robots.txt allows these paths and IA publishes no fixed
rate, so requests go at least 1 s apart. A 429 or 503 stops the run at once with ``IA_RATE_LIMITED``, and repeated
403s with ``IA_BLOCKED``, keeping what loaded.

The listing is re-read every 28 days, or when the public-domain cut moves, and kept as canonical JSON Lines sorted by
identifier, with a first line naming the cut (key ``items``, table ``kfm_ia_items``, about 42 MB of JSON and 5 MB
gzipped). Fields that move daily (downloads, reviews) are not requested. A listing that returns under 90% of the
items loaded before is refused (``IA_LISTING_SHRANK``); one whose items do not add up to its total is refused
(``IA_RESULTS_SHIFTED``).

Full text is loaded only for items that are not access-restricted, have a ``DjVuTXT`` file, and are public domain
by one of these tests, recorded in ``kfm_ia_items.pd_basis``:

- ``date``: published no later than ``now.year - 96`` (1930 in 2026; works of 1930 entered the U.S. public domain on
  2026-01-01);
- ``license``: a Creative Commons public-domain URL or usa.gov/government-works in ``licenseurl``;
- ``rights``: ``rights`` or ``possible-copyright-status`` says public domain, not in copyright or no known copyright
  restriction (including the Library of Congress's "unaware of any copyright restrictions").

A rights field that claims copyright ("In copyright", "Copyright is held by", "all rights reserved", "modern
edition") removes an item even from the date test: an item's ``date`` may not be its first publication. On
2026-11-03 this admits about 9,330 items (7,002 by date, 608 by license, 1,717 by rights); a stricter cut changes
only ``pd_basis``. The ``date`` is IA's metadata and is not checked further.

Each eligible item costs one request to ``https://archive.org/metadata/<id>/files``, which gives every ``DjVuTXT``
file's name, size and MD5, and one per file to ``https://archive.org/download/<id>/<file>``. The MD5 is verified. Each
file is kept gzipped (``texts/<id[:2]>/<id>/<stem>-<sha12>.txt.gz``, key ``text/<id>/<file>``, receipt with MD5, size,
basis, license) and loaded in its own transaction as parts of about 100,000 characters in ``kfm_ia_texts``, with
the FTS5 index ``kfm_ia_texts_fts`` (external content, kept in step by triggers, as ``kfm_newspaper_pages_fts``).
``kfm_ia_text_status`` records each item's outcome, so a run resumes where the last stopped, a half-done item skips
the files it has, and a run is safe to stop at any point.

Items go in this order: new items with a Kansas subject, then Kansas only in the title, then Kansas City material
(mostly Missouri, such as the Kansas City Star), oldest first in each group; then items whose last try failed (after
7 days); then items whose ``oai_updatedate`` changed; then rechecks of items without text (after 182 days). A file
is downloaded again only when its MD5 changes. An item that stops qualifying or leaves the listing is retired.
A file with the same bytes as one already loaded is not loaded twice (status ``duplicate``). Each run stops
starting items at ``max_items``, ``max_bytes``, ``max_requests`` or ``max_seconds`` (400, 1 GB, 1,000, 50 minutes;
at about 10 s an item measured on 2026-11-03, the time binds, so about 300 items a run).

``newspaper-directory``: Library of Congress, Directory of U.S. Newspapers in American Libraries
(https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/), the Kansas facet: 6,983 titles
in 70 pages of 100 on 2026-11-03. Kept as canonical JSON Lines sorted by LCCN, without the result position (key
``directory``, table ``kfm_loc_newspaper_directory``); key columns beside ``record_json``, which holds every provider
field. ``dates`` is '[1897 TO 1899]', where LOC widens a year known only in part ("18??" to 1800 and 1899) and writes an
open end as 9999. ``start_year`` and ``end_year`` keep those ranges except the placeholders (1000 from "1???", 2099 from
"20??", 9999), which load as NULL; everything stays as given in ``record_json``. Re-pulled every 28 days. LOC's terms (https://www.loc.gov/legal/) ask for at most 10 requests a minute, so
requests are at least 6 s apart. A 429, a 403 or an HTML page stops the run (``LOC_RATE_LIMITED``), since LOC blocks
for an hour past its limit.

The lost feed failed on 2026-11-03 with HTTP 404 on page 2. That did not reproduce: the same URL answered 200 hours
later, as did all 70 pages in a whole pull, and only page 71, past the end, answers 404 ("exception": "not found").
So the cause was not page size, ``sp`` or the facet. LOC does fail intermittently: that pull of 70 pages met three
answers of broken JSON and one Cloudflare HTTP 520, each cured by asking again, and pages not in LOC's cache take up to
35 s. That the old 404 was the same kind of failure is likely but not proved. A 404, 5xx, dropped connection or broken
JSON inside the known range is therefore treated as temporary: the page is retried after 60 s, then read in pages of
25 from the same offset, and failing that the run stops with ``LOC_PAGE_FAILED``. Pages already read stay in a spool file outside
``data/`` (``tmp-sql-feeds/newspaper-directory-spool.jsonl``, recorded in the feed state), and the next run continues
from there for up to 7 days. Every page must start at the expected offset with the same total, and the whole must add
up to that many distinct titles, or the spool is dropped and the run stops with ``LOC_RESULTS_SHIFTED``.

``towers``: FCC Antenna Structure Registration, the weekly full file ``r_tower.zip`` (37.9 MB, built Sundays; public
record), described at https://www.fcc.gov/uls/transactions/daily-weekly. On 2026-11-03 FCC's web servers, behind
Akamai, answer 403 "Access Denied" to this pipeline's honest User-Agent on www.fcc.gov, data.fcc.gov,
wireless.fcc.gov and wireless2.fcc.gov. FCC's own anonymous FTP server, ftp://wirelessftp.fcc.gov/pub/uls/complete/,
holds the same files and is tried first; FTP sends no User-Agent and the client is not disguised. opendata.fcc.gov
has no ASR dataset. When every route in ``ASR_ROUTES`` refuses or answers something other than a zip, the feed records
``"blocked": "FCC_BLOCKED"`` and each route's reason in its state and stops with that reason (``FCC_UNAVAILABLE`` if
none refused and all simply failed); it does not try to get around a block, and tries again after ``recheck_days``.
To stop using FTP, remove its entry from ``ASR_ROUTES``.

Kansas is an RA record with structure state KS. The CO, EN, HS, RE and SC records are matched to those by unique
system identifier, the key that joins the file's records. Each member's line count must match the zip's
``counts`` file (``ASR_COUNTS_MISMATCH``) and every record its table's width (``ASR_COLUMNS_CHANGED``). Each
member's Kansas lines are kept as FCC's text (``<member>-KS-<sha12>.dat.gz``, key the member name) and load into
``kfm_asr_registrations``, ``_locations`` (with decimal degrees and a point), ``_entities``, ``_history``, ``_remarks``
and ``_special_conditions``: 3,692 registrations and 20,782 rows on 2026-11-03. Empty fields load as NULL. Re-pulled
every 7 days; a member whose Kansas lines did not change is not loaded or kept again.
"""
from __future__ import annotations

from datetime import date
import gzip
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.parse
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_bulk import PUBLIC_DOMAIN, _jsonl, _jsonl_rows, _pause, _point, open_bulk_db
from tools.local_data.sql_feed_hazards import age_days, keep_version, number, retire, save_state
from tools.local_data.sql_feeds import FeedError


def _json(value):
    """A provider's list or object as canonical JSON, a missing or empty one as None."""
    return core.canonical(value) if value not in (None, [], {}, "") else None


def _as_list(value) -> list:
    return value if isinstance(value, list) else [] if value is None else [value]


def _first(value):
    values = _as_list(value)
    return values[0] if values else None


def _text(value):
    """IA gives a field as a string or a list of strings: a string stays one, a list becomes canonical JSON."""
    if isinstance(value, list):
        return _json(value)
    return None if value is None else str(value)


# --- Archive texts: the Internet Archive listing, then one source per DjVu text file ----------------

IA_SCRAPE = "https://archive.org/services/search/v1/scrape"
IA_QUERY = "mediatype:texts AND (subject:kansas OR title:kansas)"
IA_FILES = "https://archive.org/metadata/{identifier}/files"
IA_DOWNLOAD = "https://archive.org/download/{identifier}/{name}"
IA_FIELDS = ("identifier", "title", "creator", "date", "year", "publisher", "language", "subject", "collection", "licenseurl", "rights",
             "possible-copyright-status", "access-restricted-item", "imagecount", "publicdate", "addeddate", "updatedate", "oai_updatedate",
             "call_number", "volume", "sponsor", "contributor", "scanningcenter", "item_size", "format", "description")
IA_ITEMS_SOURCE, IA_TEXT_SOURCE = "ia-kansas-items", "ia-kansas-texts"
IA_CITATION = "Internet Archive (archive.org), full text derived from the item's scan (DjVuTXT)"
IA_TERMS = "https://archive.org/about/terms.php"
IA_PAUSE = 1.0
IA_PAGE = 10000                  # the Scrape API's largest count
IA_LISTING_LIMIT = 256_000_000   # one listing page; 16 MB on 2026-11-03
IA_FILES_LIMIT = 64_000_000      # one item's file list
IA_LISTING_DAYS = 28
IA_FAILED_DAYS, IA_RECHECK_DAYS = 7, 182
IA_MAX_ITEMS, IA_MAX_BYTES, IA_MAX_REQUESTS, IA_MAX_SECONDS = 400, 1_000_000_000, 1000, 3000
IA_STOP_FAILURES, IA_STOP_FORBIDDEN = 3, 5
IA_PART_CHARS = 100_000
IA_IDENTIFIER = re.compile(r"[A-Za-z0-9][\w.-]*\Z")
IA_RESTRICTED_COLLECTIONS = {"inlibrary", "printdisabled", "lendinglibrary"}
IA_LICENSE_PD = re.compile(r"creativecommons\.org/(?:publicdomain/|licenses/publicdomain)|usa\.gov/government-works", re.I)
IA_RIGHTS_PD = re.compile(r"public.?domain|not_in_copyright|not in copyright|no known copyright|no copyright|unaware of any copyright", re.I)
IA_RIGHTS_CLAIMED = re.compile(r"(?<!not )\bin copyright\b|copyright (?:is )?held|modern edition|all rights reserved", re.I)
IA_ITEM_COLUMNS = ["identifier", "title", "creator", "date", "year", "publisher", "language", "subject", "collection", "licenseurl", "rights",
                   "possible_copyright_status", "access_restricted_item", "imagecount", "publicdate", "addeddate", "updatedate", "oai_updatedate",
                   "call_number", "volume", "sponsor", "contributor", "scanningcenter", "item_size", "format", "description",
                   "has_text", "pd_basis", "queue_rank"]
IA_TEXT_COLUMNS = ["text_rowid", "identifier", "file_name", "part", "text", "char_count"]
IA_DDL = """
CREATE TABLE IF NOT EXISTS kfm_ia_items (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, identifier TEXT NOT NULL, title TEXT, creator TEXT, date TEXT, year INTEGER, publisher TEXT, language TEXT, subject TEXT, collection TEXT, licenseurl TEXT, rights TEXT, possible_copyright_status TEXT, access_restricted_item TEXT, imagecount INTEGER, publicdate TEXT, addeddate TEXT, updatedate TEXT, oai_updatedate TEXT, call_number TEXT, volume TEXT, sponsor TEXT, contributor TEXT, scanningcenter TEXT, item_size INTEGER, format TEXT, description TEXT, has_text INTEGER NOT NULL, pd_basis TEXT, queue_rank INTEGER NOT NULL, PRIMARY KEY(file_id, row_number));
CREATE INDEX IF NOT EXISTS kfm_ia_items_identifier ON kfm_ia_items(identifier);
CREATE INDEX IF NOT EXISTS kfm_ia_items_year ON kfm_ia_items(year);
CREATE INDEX IF NOT EXISTS kfm_ia_items_pd_basis ON kfm_ia_items(pd_basis, queue_rank, year);
CREATE TABLE IF NOT EXISTS kfm_ia_text_status (identifier TEXT PRIMARY KEY, status TEXT NOT NULL, oai_updatedate TEXT, files_json TEXT, checked TEXT NOT NULL, detail TEXT) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS kfm_ia_texts (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, text_rowid INTEGER PRIMARY KEY,
  identifier TEXT NOT NULL, file_name TEXT NOT NULL, part INTEGER NOT NULL, text TEXT NOT NULL, char_count INTEGER NOT NULL);
CREATE UNIQUE INDEX IF NOT EXISTS kfm_ia_texts_file_id_row_number ON kfm_ia_texts(file_id, row_number);
CREATE INDEX IF NOT EXISTS kfm_ia_texts_identifier ON kfm_ia_texts(identifier, file_name, part);
CREATE VIRTUAL TABLE IF NOT EXISTS kfm_ia_texts_fts USING fts5(text, content='kfm_ia_texts', content_rowid='text_rowid');
CREATE TRIGGER IF NOT EXISTS kfm_ia_texts_fts_insert AFTER INSERT ON kfm_ia_texts BEGIN
  INSERT INTO kfm_ia_texts_fts(rowid, text) VALUES (new.text_rowid, new.text); END;
CREATE TRIGGER IF NOT EXISTS kfm_ia_texts_fts_delete AFTER DELETE ON kfm_ia_texts BEGIN
  INSERT INTO kfm_ia_texts_fts(kfm_ia_texts_fts, rowid, text) VALUES ('delete', old.text_rowid, old.text); END;
CREATE TRIGGER IF NOT EXISTS kfm_ia_texts_fts_update AFTER UPDATE OF text_rowid, text ON kfm_ia_texts BEGIN
  INSERT INTO kfm_ia_texts_fts(kfm_ia_texts_fts, rowid, text) VALUES ('delete', old.text_rowid, old.text);
  INSERT INTO kfm_ia_texts_fts(rowid, text) VALUES (new.text_rowid, new.text); END;
"""


def ia_year(item: dict):
    """An item's publication year: IA's ``year``, else the leading year of ``date``."""
    year = _first(item.get("year"))
    if isinstance(year, int) and 1000 <= year <= 2100:
        return year
    if isinstance(year, str) and re.fullmatch(r"\d{4}", year):
        return int(year)
    for value in _as_list(item.get("date")):
        found = re.match(r"\d{4}", str(value))
        if found:
            return int(found.group())
    return None


def _ia_has_text(item: dict) -> bool:
    return "DjVuTXT" in _as_list(item.get("format"))


def pd_basis(item: dict, cutoff: int):
    """Why an item's full text may be loaded (``date``, ``license``, ``rights``), or None; see the module docstring."""
    collections = set(_as_list(item.get("collection")))
    if str(_first(item.get("access-restricted-item"))).lower() == "true" or collections & IA_RESTRICTED_COLLECTIONS or not _ia_has_text(item):
        return None
    rights = " ".join(str(v) for field in ("rights", "possible-copyright-status") for v in _as_list(item.get(field)))
    if IA_RIGHTS_CLAIMED.search(rights):
        return None
    year = ia_year(item)
    if year is not None and year <= cutoff:
        return "date"
    if any(IA_LICENSE_PD.search(str(v)) for v in _as_list(item.get("licenseurl"))):
        return "license"
    return "rights" if IA_RIGHTS_PD.search(rights) else None


def queue_rank(item: dict) -> int:
    """0: a Kansas subject; 1: Kansas only in the title; 2: Kansas City material, mostly Missouri, queued last."""
    subjects = " ".join(str(v) for v in _as_list(item.get("subject"))).lower()
    title = " ".join(str(v) for v in _as_list(item.get("title"))).lower()
    if "kansas city" in title or any("kansas-city" in str(c) for c in _as_list(item.get("collection"))):
        return 2
    return 0 if "kansas" in subjects.replace("kansas city", "") else 1


def item_row(item: dict, cutoff: int) -> tuple:
    """A kfm_ia_items row from one listing entry."""
    named = {"possible_copyright_status": "possible-copyright-status", "access_restricted_item": "access-restricted-item"}
    fields = {c: _text(item.get(named.get(c, c))) for c in IA_ITEM_COLUMNS[:-3]}
    fields["year"] = ia_year(item)
    fields["imagecount"], fields["item_size"] = (int(item[k]) if str(item.get(k, "")).isdigit() else None for k in ("imagecount", "item_size"))
    return (*fields.values(), 1 if _ia_has_text(item) else 0, pd_basis(item, cutoff), queue_rank(item))


def _ia_item_rows(path: Path):
    entries = _jsonl_rows(path)
    cutoff = next(entries)["pd_cutoff_year"]
    return (item_row(item, cutoff) for item in entries)


def ia_parts(handle, size: int = IA_PART_CHARS):
    """Split a text stream into parts of about size characters, at a line end where one is near."""
    buffer = ""
    while chunk := handle.read(1 << 20):
        buffer += chunk.replace("\x00", "")
        while len(buffer) >= 2 * size:
            cut = buffer.rfind("\n", size // 2, size)
            cut = size if cut < 0 else cut + 1
            yield buffer[:cut]
            buffer = buffer[cut:]
    while buffer:
        cut = buffer.rfind("\n", size // 2, size) if len(buffer) > size else len(buffer) - 1
        cut = size if cut < 0 else cut + 1
        yield buffer[:cut]
        buffer = buffer[cut:]


def _ia_text_rows(path: Path, identifier: str, name: str):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as handle:
        for part, text in enumerate(ia_parts(handle), 1):
            yield (None, identifier, name, part, text, len(text))


class _IAStop(Exception):
    """A per-run budget ran out inside an item; the item is left to the next run."""


class _IARun:
    """Pacing and budgets of one archive-texts run. Every request counts."""

    def __init__(self, ctx, max_items: int, max_bytes: int, max_requests: int, max_seconds: int):
        self.ctx, self.max_items, self.max_bytes, self.max_requests, self.max_seconds = ctx, max_items, max_bytes, max_requests, max_seconds
        self.started, self.requests, self.bytes, self.items = time.monotonic(), 0, 0, 0

    def spent(self) -> bool:
        return (self.items >= self.max_items or self.bytes >= self.max_bytes or self.requests + 2 > self.max_requests
                or time.monotonic() - self.started > self.max_seconds)

    def json(self, url: str, limit: int):
        _pause(self.ctx, IA_PAUSE)
        self.requests += 1
        fetched = self.ctx.fetch(url, limit=limit, timeout=600, attempts=1)
        try:
            return json.loads(fetched.body)
        except ValueError:
            raise FeedError(f"IA_ANSWER_INVALID {url}") from None

    def download(self, url: str, dest: Path, size: int):
        """One attempt: a 503 must stop the run, not be retried as core's other downloads are."""
        _pause(self.ctx, IA_PAUSE)
        self.requests += 1
        limit = size + (1 << 20)
        if self.ctx.download is None and self.ctx.fetch is core.http_fetch:
            return core.http_download(url, dest, limit=limit, timeout=3600, attempts=1)
        return core.download(self.ctx, url, dest, limit=limit, timeout=3600)


def _ia_refusal(error: FeedError):
    """How an IA request failed: ``rate``, ``forbidden``, ``missing``, ``failed``; None for a reason not about the request."""
    code = str(error).split(" ", 1)[0]
    if code in ("HTTP_429", "HTTP_503"):
        return "rate"
    if code in ("HTTP_401", "HTTP_403", "HTTP_451"):
        return "forbidden"
    if code in ("HTTP_404", "HTTP_410"):
        return "missing"
    return "failed" if code.startswith("HTTP_") or code in ("FETCH_FAILED", "IA_ANSWER_INVALID") else None


def _ia_listing(ctx, db, run: _IARun, cutoff: int, loaded_items: int) -> dict:
    """Fetch, keep and load the whole Kansas listing; returns its load result."""
    items, cursor, total = {}, None, None
    while True:
        query = {"q": IA_QUERY, "fields": ",".join(IA_FIELDS), "count": IA_PAGE, **({"cursor": cursor} if cursor else {})}
        url = IA_SCRAPE + "?" + urllib.parse.urlencode(query)
        try:
            payload = run.json(url, IA_LISTING_LIMIT)
        except FeedError as error:
            kind = _ia_refusal(error)
            if kind == "rate":
                raise FeedError(f"IA_RATE_LIMITED {str(error)[:200]}") from None
            if kind == "forbidden":
                raise FeedError(f"IA_BLOCKED {str(error)[:200]}") from None
            raise
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list) or "total" not in payload:
            raise FeedError(f"IA_LISTING_SHAPE {str(payload)[:200]}")
        total = payload["total"] if total is None else total
        for item in payload["items"]:
            if not isinstance(item, dict) or not item.get("identifier"):
                raise FeedError("IA_LISTING_SHAPE entry")
            items[item["identifier"]] = {k: v for k, v in item.items() if k in IA_FIELDS}
        cursor = payload.get("cursor")
        if not cursor or not payload["items"]:
            break
    if len(items) != total:
        raise FeedError(f"IA_RESULTS_SHIFTED {len(items)} of {total}")
    if not items:
        raise FeedError("IA_KANSAS_EMPTY")
    if len(items) < 0.9 * loaded_items:
        raise FeedError(f"IA_LISTING_SHRANK {loaded_items} to {len(items)}")
    body = _jsonl([{"pd_cutoff_year": cutoff}, *(items[k] for k in sorted(items))])
    result = keep_version(ctx, db, feed="archive-texts", source_id=IA_ITEMS_SOURCE, key="items", name="items/ia-kansas-items", ext=".jsonl.gz", body=body,
                          url=IA_SCRAPE, table="kfm_ia_items", width=len(IA_ITEM_COLUMNS), rows=_ia_item_rows,
                          extra={"query": IA_QUERY, "items": len(items), "pd_cutoff_year": cutoff, "citation": IA_CITATION, "terms": IA_TERMS})
    return {**result, "items": len(items)}


def _ia_loaded_files(db) -> dict:
    """{identifier: {file name: md5}} of the text files loaded now."""
    found = {}
    for key, md5 in db.execute("SELECT json_extract(receipt_json,'$.key'), json_extract(receipt_json,'$.md5') FROM kfm_sql_sources "
                               "WHERE source_id=? AND state='complete'", (IA_TEXT_SOURCE,)):
        _, identifier, name = key.split("/", 2)
        found.setdefault(identifier, {})[name] = md5
    return found


def _ia_set_status(ctx, db, identifier: str, status: str, oai, files, today: date, detail=None) -> None:
    with core.pipeline_lock(ctx):
        db.execute("INSERT OR REPLACE INTO kfm_ia_text_status VALUES (?,?,?,?,?,?)",
                   (identifier, status, oai, _json(files), str(today), str(detail)[:300] if detail else None))


def _ia_keep_text(ctx, db, run: _IARun, row: dict, name: str, entry: dict, size: int) -> dict:
    """Download one DjVu text file, check its MD5, keep it gzipped and load it. Lock taken for the load only."""
    identifier, url = row["identifier"], IA_DOWNLOAD.format(identifier=row["identifier"], name=urllib.parse.quote(name))
    download, packed = core.temp_path(ctx, "ia-text.txt"), core.temp_path(ctx, "ia-text.txt.gz")
    try:
        fetched = run.download(url, download, size)
        got, md5 = download.stat().st_size, hashlib.md5(usedforsecurity=False)
        with open(download, "rb") as source, open(packed, "wb") as out, gzip.GzipFile(filename="", fileobj=out, mode="wb", mtime=0) as zipped:
            while chunk := source.read(1 << 20):
                md5.update(chunk)
                zipped.write(chunk)
        if entry.get("md5") and md5.hexdigest() != entry["md5"]:
            raise FeedError(f"IA_FILE_CHANGED {identifier}/{name} {got} bytes")
        stem = re.sub(r"[^\w.-]+", "_", re.sub(r"\.txt$", "", name))
        result = keep_version(ctx, db, feed="archive-texts", source_id=IA_TEXT_SOURCE, key=f"text/{identifier}/{name}",
                              name=f"texts/{identifier[:2]}/{identifier}/{stem}", ext=".txt.gz", body=packed, url=url, fetched=fetched,
                              original=download, table="kfm_ia_texts", width=len(IA_TEXT_COLUMNS),
                              rows=lambda path: _ia_text_rows(path, identifier, name),
                              extra={"identifier": identifier, "file_name": name, "md5": entry.get("md5"), "size": got, "title": row["title"],
                                     "year": row["year"], "pd_basis": row["pd_basis"], "license": f"public domain ({row['pd_basis']}; see module docstring)",
                                     "citation": IA_CITATION, "terms": IA_TERMS})
        run.bytes += got
        return result
    finally:
        download.unlink(missing_ok=True)
        packed.unlink(missing_ok=True)


def _ia_item(ctx, db, run: _IARun, row: dict, have: dict, today: date) -> dict:
    """Bring one item's text up to date. Returns {"status", "rows"}; raises FeedError when a request failed."""
    identifier, oai = row["identifier"], row["oai_updatedate"]
    if not IA_IDENTIFIER.match(identifier):
        _ia_set_status(ctx, db, identifier, "bad_identifier", oai, None, today)
        return {"status": "bad_identifier", "rows": 0}
    payload = run.json(IA_FILES.format(identifier=identifier), IA_FILES_LIMIT)
    listed = payload.get("result") if isinstance(payload, dict) else None
    if not isinstance(listed, list):
        _ia_set_status(ctx, db, identifier, "missing", oai, None, today, "no such item")
        return {"status": "missing", "rows": 0}
    wanted = {f["name"]: f for f in listed if isinstance(f, dict) and f.get("format") == "DjVuTXT" and f.get("name")}
    public = {name: f for name, f in wanted.items() if str(f.get("private", "")).lower() != "true"}
    current, rows, shared = have.get(identifier, {}), 0, False
    for name in sorted(public):
        if current.get(name) == public[name].get("md5") and public[name].get("md5"):
            continue
        size = int(public[name].get("size") or 0)
        if size == 0:
            continue
        if run.requests + 1 > run.max_requests or (run.bytes and run.bytes + size > run.max_bytes):
            raise _IAStop
        try:
            result = _ia_keep_text(ctx, db, run, row, name, public[name], size)
        except FeedError as error:
            if not str(error).startswith("SOURCE_CONTENT_SHARED"):
                raise
            shared = True
            continue
        rows += result["rows"]
        current = {**current, name: public[name].get("md5")}
    with core.pipeline_lock(ctx):
        for name in sorted(set(current) - set(public)):
            retire(db, IA_TEXT_SOURCE, f"text/{identifier}/{name}", "kfm_ia_texts")
            current = {k: v for k, v in current.items() if k != name}
    have[identifier] = current
    status = "loaded" if current else "duplicate" if shared else "empty" if public else "restricted" if wanted else "no_text"
    _ia_set_status(ctx, db, identifier, status, oai, {n: public[n].get("md5") for n in sorted(public)}, today)
    return {"status": status, "rows": rows}


def _ia_queue(db, today: date) -> list:
    """Eligible items that need work, in order; see the module docstring."""
    new, failed, changed, recheck = [], [], [], []
    for identifier, title, year, basis, oai, status, seen, checked in db.execute(
            "SELECT i.identifier, i.title, i.year, i.pd_basis, i.oai_updatedate, s.status, s.oai_updatedate, s.checked FROM kfm_ia_items i "
            "LEFT JOIN kfm_ia_text_status s ON s.identifier=i.identifier WHERE i.pd_basis IS NOT NULL "
            "ORDER BY i.queue_rank, i.year IS NULL, i.year, i.identifier").fetchall():
        row = {"identifier": identifier, "title": title, "year": year, "pd_basis": basis, "oai_updatedate": oai}
        age = (today - date.fromisoformat(checked)).days if checked else None
        if status is None:
            new.append(row)
        elif status == "failed":
            if age >= IA_FAILED_DAYS:
                failed.append(row)
        elif seen != oai:
            changed.append(row)
        elif status != "loaded" and age >= IA_RECHECK_DAYS:
            recheck.append(row)
    return new + failed + changed + recheck


def _ia_retire(ctx, db, have: dict) -> int:
    """Remove the text of items that left the listing or stopped qualifying. Lock taken here."""
    eligible = {i for (i,) in db.execute("SELECT identifier FROM kfm_ia_items WHERE pd_basis IS NOT NULL")}
    retired = 0
    with core.pipeline_lock(ctx):
        for identifier in sorted(set(have) - eligible):
            for name in sorted(have.pop(identifier)):
                retired += retire(db, IA_TEXT_SOURCE, f"text/{identifier}/{name}", "kfm_ia_texts")
        db.execute("DELETE FROM kfm_ia_text_status WHERE identifier NOT IN (SELECT identifier FROM kfm_ia_items WHERE pd_basis IS NOT NULL)")
    return retired


def archive_texts(ctx, max_items: int = IA_MAX_ITEMS, max_bytes: int = IA_MAX_BYTES, max_requests: int = IA_MAX_REQUESTS,
                  max_seconds: int = IA_MAX_SECONDS, listing_days: int = IA_LISTING_DAYS) -> dict:
    """Internet Archive public-domain Kansas texts: the listing every 28 days, then full text item by item until a
    budget runs out; the next run continues. A 429 or 503 stops the run with ``IA_RATE_LIMITED``, repeated 403s with
    ``IA_BLOCKED`` and repeated failures with ``IA_UNAVAILABLE``, keeping what loaded and saying so in the state.
    See the module docstring for the provider, terms, the public-domain tests and the revision rules."""
    db = open_bulk_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(IA_DDL)
        state, today = core.get_state(db, "archive-texts"), ctx.now().date()
        cutoff, run = today.year - 96, _IARun(ctx, max_items, max_bytes, max_requests, max_seconds)
        summary = {"listing": "not_due", "loaded": 0, "unchanged": 0, "without_text": 0, "failed": 0, "retired": 0, "rows": 0, "stopped": None}
        have = _ia_loaded_files(db)
        age = age_days(state, "items_checked", today)
        if age is None or age >= listing_days or state.get("pd_cutoff_year") != cutoff:
            previous = state.get("items", 0)
            try:
                result = _ia_listing(ctx, db, run, cutoff, previous)
            except FeedError as error:
                if str(error).startswith(("IA_RATE_LIMITED", "IA_BLOCKED")):
                    save_state(ctx, db, "archive-texts", {**state, "stopped": str(error)})
                raise
            summary["listing"] = result["state"]
            state = save_state(ctx, db, "archive-texts", {**state, "items_checked": str(today), "items": result["items"], "pd_cutoff_year": cutoff})
            summary["retired"] = _ia_retire(ctx, db, have)
        queue, failures, forbidden, reason, done = _ia_queue(db, today), 0, 0, None, 0
        for row in queue:
            if run.spent():
                summary["stopped"] = "budget"
                break
            try:
                outcome = _ia_item(ctx, db, run, row, have, today)
            except _IAStop:
                summary["stopped"] = "budget"
                break
            except FeedError as error:
                changed = str(error).startswith(("IA_FILE_CHANGED", "RESPONSE_TOO_LARGE"))   # this file, not the service
                kind = "failed" if changed else _ia_refusal(error)
                if kind is None:
                    raise
                if kind == "rate":
                    reason = f"IA_RATE_LIMITED {str(error)[:200]}"
                    break
                run.items += 1
                done += 1
                _ia_set_status(ctx, db, row["identifier"], kind, row["oai_updatedate"], None, today, error)
                summary["failed" if kind == "failed" else "without_text"] += 1
                failures = failures + 1 if kind == "failed" and not changed else 0
                forbidden = forbidden + 1 if kind == "forbidden" else 0
                if forbidden >= IA_STOP_FORBIDDEN:
                    reason = f"IA_BLOCKED {str(error)[:200]}"
                    break
                if failures >= IA_STOP_FAILURES:
                    reason = f"IA_UNAVAILABLE {str(error)[:200]}"
                    break
                continue
            failures, forbidden = 0, 0
            run.items += 1
            done += 1
            summary["rows"] += outcome["rows"]
            if outcome["status"] == "loaded" and outcome["rows"]:
                summary["loaded"] += 1
            elif outcome["status"] == "loaded":
                summary["unchanged"] += 1
            else:
                summary["without_text"] += 1
        pending = len(queue) - done
        statuses = dict(db.execute("SELECT status, count(*) FROM kfm_ia_text_status GROUP BY status").fetchall())
        state = save_state(ctx, db, "archive-texts", {**state, "pending": pending, "statuses": statuses, "stopped": reason})
        if reason:
            raise FeedError(reason)
        return {**summary, "pending": pending, "requests": run.requests, "bytes": run.bytes, "statuses": statuses}
    finally:
        db.close()


# --- Newspaper directory: every Kansas title, read page by page into a resumable spool --------------

LOC_DIRECTORY = ("https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/?fa=location_state%3Akansas&fo=json"
                 "&c={size}&sp={page}&at=results%2Cpagination")
LOC_SOURCE = "loc-newspaper-directory"
LOC_TABLE = "kfm_loc_newspaper_directory"
LOC_CITATION = "Library of Congress, Directory of U.S. Newspapers in American Libraries"
LOC_LICENSE = "bibliographic records published by the Library of Congress; see its terms"
LOC_TERMS = "https://www.loc.gov/legal/"
LOC_PAUSE = 6.0        # https://www.loc.gov/legal/: at most 10 requests a minute
LOC_RETRY_PAUSE = 60.0
LOC_PAGE_SIZE, LOC_SMALL_PAGE = 100, 25
LOC_PAGE_LIMIT = 64_000_000
LOC_RECHECK_DAYS, LOC_SPOOL_DAYS = 28, 7
LOC_MAX_SECONDS = 3000
LOC_COLUMNS = ["lccn", "id", "title", "url", "date", "start_year", "end_year", "city", "county", "publication_frequency", "created_published", "digitized",
               "language_json", "contributor_json", "subject_json", "description_json", "preceding_json", "succeeding_json", "other_title_json", "oclc_json",
               "issn_json", "institution_json", "source_modified", "timestamp", "record_json"]
LOC_DDL = """
CREATE TABLE IF NOT EXISTS kfm_loc_newspaper_directory (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, lccn TEXT NOT NULL, id TEXT, title TEXT, url TEXT, date TEXT, start_year INTEGER, end_year INTEGER, city TEXT, county TEXT, publication_frequency TEXT, created_published TEXT, digitized INTEGER, language_json TEXT, contributor_json TEXT, subject_json TEXT, description_json TEXT, preceding_json TEXT, succeeding_json TEXT, other_title_json TEXT, oclc_json TEXT, issn_json TEXT, institution_json TEXT, source_modified TEXT, timestamp TEXT, record_json TEXT NOT NULL, PRIMARY KEY(file_id, row_number));
CREATE INDEX IF NOT EXISTS kfm_loc_newspaper_directory_lccn ON kfm_loc_newspaper_directory(lccn);
CREATE INDEX IF NOT EXISTS kfm_loc_newspaper_directory_county ON kfm_loc_newspaper_directory(county, start_year);
CREATE INDEX IF NOT EXISTS kfm_loc_newspaper_directory_city ON kfm_loc_newspaper_directory(city, start_year);
CREATE INDEX IF NOT EXISTS kfm_loc_newspaper_directory_start_year ON kfm_loc_newspaper_directory(start_year);
"""


def _directory_years(title: dict) -> tuple:
    """Start and end year from the first ``dates`` range ('[1897 TO 1899]'); without one, from ``date`` and the title's
    '1854-1860'. LOC's placeholders (9999, 2099 from '20??', 1000 from '1???') are not years."""
    ranges = [re.findall(r"\d{4}", str(v)) for v in _as_list(title.get("dates"))]
    found = ranges[0] if ranges and ranges[0] else re.findall(r"^\d{4}$", str(title.get("date") or ""))
    start, end = (int(found[0]) if found else None), (int(found[1]) if len(found) > 1 else None)
    if not ranges:
        closing = re.search(r"\b\d[\d?]{3}-(\d{4})\b", str(title.get("title") or ""))
        end = int(closing.group(1)) if closing else None
    return (start if start and start >= 1700 else None, end if end and end < 2090 else None)


def directory_row(title: dict) -> tuple:
    """A kfm_loc_newspaper_directory row from one kept title."""
    item = title.get("item") if isinstance(title.get("item"), dict) else {}
    start, end = _directory_years(title)
    return (_first(title.get("number_lccn")) or re.sub(r".*/item/([^/]+)/?$", r"\1", str(title.get("id"))), title.get("id"), title.get("title"), title.get("url"),
            title.get("date"), start, end, _first(title.get("location_city")), _first(title.get("location_county")),
            _first(title.get("publication_frequency")), _first(item.get("created_published")), 1 if title.get("digitized") else 0,
            *(_json(title.get(k)) for k in ("language", "contributor", "subject", "description", "number_preceding_items", "number_succeeding_items",
                                            "other_title", "number_oclc", "number_issn", "number_institution")),
            _first(title.get("number_source_modified")), title.get("timestamp"), core.canonical(title))


def _directory_rows(path: Path):
    return (directory_row(title) for title in _jsonl_rows(path))


def _directory_fetch(ctx, url: str):
    """(payload, None), or (None, why) for a failure worth another try. A block stops the run."""
    try:
        fetched = ctx.fetch(url, limit=LOC_PAGE_LIMIT, timeout=600, attempts=1)
    except FeedError as error:
        code = str(error).split(" ", 1)[0]
        if code in ("HTTP_429", "HTTP_403"):
            raise FeedError(f"LOC_RATE_LIMITED {url}") from None
        if code in ("HTTP_404", "FETCH_FAILED") or code.startswith("HTTP_5"):
            return None, code
        raise
    body = fetched.body.lstrip()
    if body[:1] == b"<":
        raise FeedError(f"LOC_RATE_LIMITED {url}")
    try:
        payload = json.loads(body)
    except ValueError:
        return None, "INVALID_JSON"
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list) or not isinstance(payload.get("pagination"), dict):
        return None, "INVALID_SHAPE"
    return payload, None


def _directory_page(ctx, offset: int, page_size: int) -> tuple:
    """The page starting at offset: (payload, size asked for). See the module docstring for the retries."""
    tries = [(page_size, LOC_PAUSE), (page_size, LOC_RETRY_PAUSE), (LOC_SMALL_PAGE, LOC_RETRY_PAUSE)] if offset % page_size == 0 else \
        [(LOC_SMALL_PAGE, LOC_PAUSE), (LOC_SMALL_PAGE, LOC_RETRY_PAUSE)]
    why = url = None
    for size, wait in tries:
        if offset % size:
            continue
        _pause(ctx, wait)
        url = LOC_DIRECTORY.format(size=size, page=offset // size + 1)
        payload, why = _directory_fetch(ctx, url)
        if payload is not None:
            return payload, size
        ctx.note("loc_page_retry", url=url, reason=why)
    raise FeedError(f"LOC_PAGE_FAILED {why} {url}")


def _spool_path(ctx) -> Path:
    return core.temp_path(ctx, "spool").parent / "newspaper-directory-spool.jsonl"


def _spool_resume(ctx, state: dict, today: date) -> dict:
    """The spool's progress if it can be continued, cut back to what the state recorded; else a fresh one."""
    path, recorded = _spool_path(ctx), state.get("spool") or {}
    usable = (recorded and path.is_file() and path.stat().st_size >= recorded["bytes"]
              and (today - date.fromisoformat(recorded["started"])).days < LOC_SPOOL_DAYS)
    if not usable:
        path.unlink(missing_ok=True)
        return {"started": str(today), "offset": 0, "bytes": 0, "of": None}
    with open(path, "r+b") as handle:
        handle.truncate(recorded["bytes"])
    return dict(recorded)


def newspaper_directory(ctx, recheck_days: int = LOC_RECHECK_DAYS, page_size: int = LOC_PAGE_SIZE, max_seconds: int = LOC_MAX_SECONDS) -> dict:
    """The LOC directory's Kansas newspaper titles, every 28 days: pages of 100 at least 6 s apart, resumable across runs
    through a spool. A run out of time returns ``state: partial``; a block stops with ``LOC_RATE_LIMITED``, a page that
    keeps failing with ``LOC_PAGE_FAILED``, a list that moved with ``LOC_RESULTS_SHIFTED``. See the module docstring."""
    started = time.monotonic()
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(LOC_DDL)
        state, today = core.get_state(db, "newspaper-directory"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "titles": state.get("titles")}
        path, spool, pages = _spool_path(ctx), _spool_resume(ctx, state, today), 0
        while spool["of"] is None or spool["offset"] < spool["of"]:
            if pages and time.monotonic() - started > max_seconds:
                return {"state": "partial", "pages": pages, "offset": spool["offset"], "of": spool["of"]}
            payload, size = _directory_page(ctx, spool["offset"], page_size)
            pagination, results = payload["pagination"], payload["results"]
            if pagination.get("perpage") != size:
                raise FeedError(f"LOC_PAGE_SIZE_CHANGED {size} answered {pagination.get('perpage')}")
            if pagination.get("from") != spool["offset"] + 1 or spool["of"] not in (None, pagination.get("of")) or not results \
                    or len(results) != pagination.get("to", 0) - spool["offset"]:
                path.unlink(missing_ok=True)
                save_state(ctx, db, "newspaper-directory", {k: v for k, v in state.items() if k != "spool"})
                raise FeedError(f"LOC_RESULTS_SHIFTED from {pagination.get('from')} of {pagination.get('of')} at {spool['offset']}")
            with open(path, "ab") as out:
                out.write("".join(core.canonical({k: v for k, v in title.items() if k != "index"}) + "\n" for title in results).encode())
            spool = {**spool, "offset": spool["offset"] + len(results), "bytes": path.stat().st_size, "of": pagination.get("of")}
            state = save_state(ctx, db, "newspaper-directory", {**state, "spool": spool})
            pages += 1
        with open(path, encoding="utf-8") as handle:
            titles = {title.get("id"): title for title in map(json.loads, handle)}
        if len(titles) != spool["of"] or None in titles:
            path.unlink(missing_ok=True)
            save_state(ctx, db, "newspaper-directory", {k: v for k, v in state.items() if k != "spool"})
            raise FeedError(f"LOC_RESULTS_SHIFTED {len(titles)} distinct titles of {spool['of']}")
        if state.get("titles") and len(titles) < 0.9 * state["titles"]:
            raise FeedError(f"LOC_DIRECTORY_SHRANK {state['titles']} to {len(titles)}")
        entries = [titles[k] for k in sorted(titles)]
        result = keep_version(ctx, db, feed="newspaper-directory", source_id=LOC_SOURCE, key="directory", name="loc-newspaper-directory-kansas", ext=".jsonl.gz",
                              body=_jsonl(entries), url=LOC_DIRECTORY.format(size=page_size, page=1), table=LOC_TABLE, width=len(LOC_COLUMNS), rows=_directory_rows,
                              extra={"citation": LOC_CITATION, "license": LOC_LICENSE, "terms": LOC_TERMS, "titles": len(entries)})
        path.unlink(missing_ok=True)
        save_state(ctx, db, "newspaper-directory", {**{k: v for k, v in state.items() if k != "spool"}, "checked": str(today), "titles": len(entries)})
        return {**result, "titles": len(entries), "pages": pages}
    finally:
        db.close()


# --- Towers: the FCC ASR weekly file, one version per record type ----------------------------------

ASR_ROUTES = ("ftp://wirelessftp.fcc.gov/pub/uls/complete/r_tower.zip",     # FCC's anonymous FTP; first since FCC's web servers refuse us
              "https://data.fcc.gov/download/pub/uls/complete/r_tower.zip",
              "https://wireless.fcc.gov/uls/data/complete/r_tower.zip")
ASR_PAGE = "https://www.fcc.gov/uls/transactions/daily-weekly"
ASR_CITATION = "Federal Communications Commission, Antenna Structure Registration, weekly public access file r_tower.zip"
ASR_LIMIT = 512_000_000
ASR_RECHECK_DAYS = 7
ASR_SHARED = ["record_type", "content_indicator", "file_number", "registration_number", "unique_system_identifier"]
ASR_TABLES = {   # member: (table, provider columns, indexed columns)
    "RA": ("kfm_asr_registrations",
           [*ASR_SHARED, "application_purpose", "previous_purpose", "input_source_code", "status_code", "date_entered", "date_received", "date_issued",
            "date_constructed", "date_dismantled", "date_action", "archive_flag_code", "version", "signature_first_name", "signature_middle_initial",
            "signature_last_name", "signature_suffix", "signature_title", "invalid_signature", "structure_street_address", "structure_city",
            "structure_state_code", "county_code", "zip_code", "height_of_structure", "ground_elevation", "overall_height_above_ground",
            "overall_height_amsl", "structure_type", "date_faa_determination_issued", "faa_study_number", "faa_circular_number", "specification_option",
            "painting_and_lighting", "mark_light_code", "mark_light_other", "faa_emi_flag", "nepa_flag", "date_signed", "assignor_signature_last_name",
            "assignor_signature_first_name", "assignor_signature_middle_initial", "assignor_signature_suffix", "assignor_signature_title",
            "assignor_signature_date"],
           ["county_code", "registration_number", "structure_city"]),
    "CO": ("kfm_asr_locations",
           [*ASR_SHARED, "coordinate_type", "latitude_degrees", "latitude_minutes", "latitude_seconds", "latitude_direction", "latitude_total_seconds",
            "longitude_degrees", "longitude_minutes", "longitude_seconds", "longitude_direction", "longitude_total_seconds", "array_tower_position",
            "array_total_tower"],
           ["registration_number"]),
    "EN": ("kfm_asr_entities",
           [*ASR_SHARED, "entity_type", "entity_type_code", "entity_type_other", "licensee_id", "entity_name", "first_name", "mi", "last_name", "suffix", "phone",
            "fax_number", "internet_address", "street_address", "street_address2", "po_box", "city", "state", "zip_code", "attention", "frn"],
           ["entity_name", "registration_number"]),
    "HS": ("kfm_asr_history", [*ASR_SHARED, "date", "description"], ["registration_number"]),
    "RE": ("kfm_asr_remarks", [*ASR_SHARED, "remark_type", "date_keyed", "sequence_number", "remark_text"], ["registration_number"]),
    "SC": ("kfm_asr_special_conditions", [*ASR_SHARED, "date_keyed", "sequence_number", "special_condition_text"], ["registration_number"]),
}
ASR_NUMBERS = {"height_of_structure", "ground_elevation", "overall_height_above_ground", "overall_height_amsl"}
ASR_GEOMETRY = ["latitude", "longitude", "geometry_geojson"]
ASR_FREE_TEXT = {"RE", "SC"}   # the last field is free text, which may hold a pipe
ASR_STATE = ASR_TABLES["RA"][1].index("structure_state_code")
ASR_USI = ASR_SHARED.index("unique_system_identifier")


def _asr_ddl() -> str:
    """Byte for byte the kfm_asr_* tables and indexes already in observations.sqlite."""
    script = ""
    for table, columns, indexes in ASR_TABLES.values():
        typed = [(c, "REAL" if c in ASR_NUMBERS else "TEXT") for c in columns]
        if table == "kfm_asr_locations":
            typed += [("latitude", "REAL"), ("longitude", "REAL"), ("geometry_geojson", "TEXT")]
        body = ", ".join(f'"{c}" {kind}' for c, kind in typed)
        script += f"CREATE TABLE IF NOT EXISTS {table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {body}, PRIMARY KEY(file_id, row_number));\n"
        script += "".join(f'CREATE INDEX IF NOT EXISTS {table}_{c} ON {table}("{c}");\n' for c in indexes)
    return script


ASR_DDL = _asr_ddl()


def _asr_fields(line: bytes, member: str) -> list:
    """One record's fields, checked against its table's width."""
    columns = ASR_TABLES[member][1]
    text = line.decode("utf-8", "replace").rstrip("\r\n")
    fields = text.split("|", len(columns) - 1) if member in ASR_FREE_TEXT else text.split("|")
    if len(fields) != len(columns) or fields[0] != member:
        raise FeedError(f"ASR_COLUMNS_CHANGED {member} {len(fields)} fields")
    return fields


def _asr_records(handle, member: str):
    """The records of a member's lines: a line not starting with the member's tag continues the record before it."""
    tag, record = member.encode() + b"|", None
    for line in handle:
        if line.startswith(tag):
            if record is not None:
                yield record
            record = line
        elif record is not None:
            record += line
        elif line.strip():
            raise FeedError(f"ASR_COLUMNS_CHANGED {member} first line")
    if record is not None:
        yield record


def _count_lines(handle, counter: list):
    """Pass lines through, counting newlines in counter[0] as ``wc -l``, which wrote FCC's counts file, does."""
    for line in handle:
        counter[0] += line.endswith(b"\n")
        yield line


def _asr_cut(zip_path: Path) -> tuple[dict, dict, str | None]:
    """Each member's Kansas records, its full line count, and the file's creation date. The counts file is checked."""
    with zipfile.ZipFile(zip_path) as z:
        names = set(z.namelist())
        if "counts" not in names or any(f"{m}.dat" not in names for m in ASR_TABLES):
            raise FeedError("ASR_MEMBERS_CHANGED")
        counts = z.read("counts").decode("ascii", "replace")
        listed = {m: int(n) for n, m in re.findall(r"^\s*(\d+)\s+\S*/([A-Z]{2})\.dat\s*$", counts, re.M)}
        created = re.search(r"File Creation Date:\s*(.+?)\s*$", counts, re.M)
        kansas, usis, lines = {}, set(), {}
        for member in ASR_TABLES:     # RA first, which gives the identifiers
            kept, physical = [], [0]
            with z.open(f"{member}.dat") as handle:
                for record in _asr_records(_count_lines(handle, physical), member):
                    fields = _asr_fields(record, member)
                    if member == "RA" and fields[ASR_STATE] == "KS":
                        usis.add(fields[ASR_USI])
                    if fields[ASR_USI] in usis:
                        kept.append(record)
            if listed.get(member) != physical[0]:
                raise FeedError(f"ASR_COUNTS_MISMATCH {member} {physical[0]} lines, counts says {listed.get(member)}")
            kansas[member], lines[member] = kept, physical[0]
    return kansas, lines, created.group(1) if created else None


def _degrees(degrees: str, minutes: str, seconds: str, direction: str, total: str):
    """Decimal degrees from FCC's degrees, minutes, seconds, or its total seconds; S and W negative; blank is None."""
    try:
        value = float(degrees) + float(minutes or 0) / 60 + float(seconds or 0) / 3600 if degrees else float(total) / 3600 if total else None
    except ValueError:
        return None
    if value is None:
        return None
    return round(-value if direction.strip().upper() in ("S", "W") else value, 7)


def _asr_rows(path: Path, member: str):
    """A member's table rows from its kept Kansas lines."""
    columns = ASR_TABLES[member][1]
    numbers = [i for i, c in enumerate(columns) if c in ASR_NUMBERS]
    with gzip.open(path, "rb") as handle:
        for record in _asr_records(handle, member):
            fields = _asr_fields(record, member)
            row = [value if value != "" else None for value in fields]
            for i in numbers:
                row[i] = number(fields[i])
            if member == "CO":
                lat = _degrees(*fields[6:11])
                lon = _degrees(*fields[11:16])
                row += [lat, lon, _point(lon, lat) if lat is not None and lon is not None else None]
            yield tuple(row)


def _asr_download(ctx, dest: Path):
    """The zip from the first route that gives one: (route, fetched, None), or (None, None, {route: why it failed})."""
    reasons = {}
    for route in ASR_ROUTES:
        try:
            fetched = core.download(ctx, route, dest, limit=ASR_LIMIT, timeout=1800)
        except FeedError as error:
            if str(error).startswith("RESPONSE_TOO_LARGE"):
                raise
            code = str(error).split(" ", 1)[0]
            reasons[route] = f"{code} {str(error).rsplit(': ', 1)[-1][:80]}" if code == "FETCH_FAILED" else code
            continue
        if fetched is not None and zipfile.is_zipfile(dest):
            return route, fetched, None
        reasons[route] = "NOT_A_ZIP"   # a block page with status 200, or a truncated answer
    return None, None, reasons


def towers(ctx, recheck_days: int = ASR_RECHECK_DAYS) -> dict:
    """FCC Antenna Structure Registration, Kansas: the weekly file from the first official route that serves it, cut to
    registrations with structure state KS and the records of those registrations. Every 7 days. When no route serves it,
    records ``FCC_BLOCKED`` with each route's reason in the state and stops; it never disguises the client or tries to
    get around a block. See the module docstring for the routes tried on 2026-11-03."""
    db = core.open_db(ctx)
    archive = core.temp_path(ctx, "r_tower.zip")
    try:
        with core.pipeline_lock(ctx):
            db.executescript(ASR_DDL)
        state, today = core.get_state(db, "towers"), ctx.now().date()
        age = age_days(state, "checked", today)
        if age is not None and age < recheck_days:
            return {"state": "not_due", "blocked": state.get("blocked"), "registrations": state.get("registrations")}
        route, fetched, reasons = _asr_download(ctx, archive)
        if route is None:
            refused = any(r.startswith(("HTTP_4", "NOT_A_ZIP")) for r in reasons.values())
            code = "FCC_BLOCKED" if refused else "FCC_UNAVAILABLE"
            save_state(ctx, db, "towers", {**state, "blocked": code, "routes": reasons, "checked": str(today)})
            raise FeedError(f"{code} no official FCC route served r_tower.zip to the pipeline's honest client: "
                            + "; ".join(f"{u} {r}" for u, r in reasons.items()))
        try:
            kansas, lines, created = _asr_cut(archive)
        except zipfile.BadZipFile:
            raise FeedError("ASR_ZIP_UNREADABLE") from None
        if not kansas["RA"]:
            raise FeedError("ASR_KANSAS_EMPTY")
        results, loaded = {}, 0
        for member, (table, columns, _) in ASR_TABLES.items():
            if not kansas[member]:
                with core.pipeline_lock(ctx):
                    retire(db, f"fcc-asr-{member.lower()}", member, table)
                results[member] = "empty"
                continue
            width = len(columns) + (len(ASR_GEOMETRY) if member == "CO" else 0)
            result = keep_version(ctx, db, feed="towers", source_id=f"fcc-asr-{member.lower()}", key=member, name=f"{member}-KS", ext=".dat.gz",
                                  body=core.gz(b"".join(kansas[member])), url=route, fetched=fetched, original=archive, table=table, width=width,
                                  rows=lambda path, member=member: _asr_rows(path, member),
                                  extra={"citation": ASR_CITATION, "license": PUBLIC_DOMAIN, "terms": ASR_PAGE, "member": member, "file_creation_date": created,
                                         "kansas_records": len(kansas[member]), "national_lines": lines[member]})
            results[member], loaded = result["state"], loaded + result["rows"]
        registrations = len(kansas["RA"])
        save_state(ctx, db, "towers", {"checked": str(today), "fetched": str(today), "file_creation_date": created, "route": route, "registrations": registrations,
                                       "blocked": None})
        return {"state": "loaded" if loaded else "unchanged", "route": route, "file_creation_date": created, "registrations": registrations,
                "rows": loaded, "records": sum(len(v) for v in kansas.values()), "members": results}
    finally:
        archive.unlink(missing_ok=True)
        db.close()
