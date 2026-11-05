"""SQL feed for the Library of Congress's Kansas holdings: photos, maps, HABS/HAER/HALS and newspaper indexes.

``loc-kansas``: the loc.gov JSON API (https://www.loc.gov/apis/json-and-yaml/, no key). Terms:
https://www.loc.gov/legal/, which asks for no more than 10 requests a minute whatever the number of machines, so
requests are spaced 6 s apart (``ctx.pause`` in tests). The API blocks a client that goes too fast. Each item's own
rights statement is kept (``rights``); newspaper issues carry none of their own, and the collection's statement is
https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/. No images and no OCR
text are fetched: newspaper text is the separate bulk feed ``newspaper-text``.

Segments, each one ``load_version`` key, kept as ``<name>-<sha12>.jsonl.gz`` and loaded in one transaction, so a
stopped run keeps every segment finished before it:

- ``photo``, ``map``: https://www.loc.gov/photos/ and https://www.loc.gov/maps/ with ``fa=location_state:kansas``.
- ``habs``: the HABS/HAER/HALS collection with ``fa=location:kansas``, because those records have no
  ``location_state``.
- ``newspaper-titles``: Chronicling America with ``fa=location_state:kansas&dl=title`` (84 titles on 2026-11-03).
- ``newspaper/<lccn>``: one title's issues, ``fa=location_state:kansas|number_lccn:<lccn>&dl=issue``. The titles' listed
  issue counts sum to 47,566 while the index holds about 47,380, so each segment is checked against its own query's
  count, not against the title's listed count.

Paging: ``c=1000`` is the largest page, a larger ``c`` silently falls back to 25, so any other page size stops the run
(``LOC_PAGE_SIZE_CHANGED``). ``at=results,pagination`` keeps the answer to results and paging. loc.gov cuts large
answers off mid-transfer, and /photos/ and /maps/ answer 503 after about 45 s on a page it has not served lately, then
the same page in a second or two (seen on 2026-11-03). So a failed page is asked for again after 30 s, then at 500,
then 100 a page, continuing at the same offset. A segment that still fails is left for the next run; the others go on,
and the run ends with ``LOC_UNAVAILABLE`` (at once when a second segment fails). A 429, a 403 or an HTML page (a block
or challenge) stops the run with ``LOC_RATE_LIMITED``; it is never retried or worked around. A segment must return
exactly its count with no id twice, or the run stops with ``LOC_RESULTS_SHIFTED``.

Each run stops starting segments at ``max_pages`` (50), estimating 1,000 records a page. Buckets are pulled again
every 28 days and the title list every 7. A title's issues are pulled when never pulled, when its listed issue count,
first or last issue changes, and every 182 days; ``number_source_modified`` is ignored because LOC touched every title
on 2026-04-13. A loaded title gone from the list keeps its rows and stops the run, after the others, with
``LOC_TITLE_UNLISTED``.

The kept copy is canonical JSON Lines sorted by id, the whole result without what differs from one request to the
next: the result position ``index``, the order of top-level string lists (``subject``, ``partof``, ``location``,
``contributor``) and the ``c=`` inside ``segments`` links. So an unchanged segment is recognized as unchanged. Feed
state: ``buckets`` {name: {pulled, records}}, ``titles_pulled``, ``titles`` {lccn: {issue_count, first_issue,
last_issue, pulled, records}}. Tables: ``kfm_loc_items`` (an item in two buckets has a row in each),
``kfm_loc_newspaper_titles``. Expected on 2026-11-03: about 50,700 rows, 100 MB in the database (2 KB a newspaper issue
with indexes) and 8 MB of kept copies, from about 115 pages (225 MB of answers): three or four runs of about 12 minutes.
"""
from __future__ import annotations

from datetime import date
import gzip
import json
from pathlib import Path
import re
import time
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_bulk import TITLE_COLUMNS, title_row
from tools.local_data.sql_feed_hazards import age_days, ddl, keep_version, loaded_keys, retire, save_state
from tools.local_data.sql_feeds import FeedError

LOC_PAUSE = 6.0   # https://www.loc.gov/legal/: at most 10 requests a minute
LOC_PAGE_SIZES = (1000, 500, 100)
LOC_PAGE_TRIES = 2         # at each page size
LOC_RETRY_WAIT = 30.0
LOC_UNAVAILABLE_SEGMENTS = 2
LOC_PAGE_LIMIT = 64_000_000
LOC_TIMEOUT = 300
LOC_BUCKET_DAYS, LOC_TITLES_DAYS, LOC_ISSUES_DAYS = 28, 7, 182
LOC_TERMS = "https://www.loc.gov/legal/"
LOC_LICENSE = "per item: see each record's rights statement (rights); https://www.loc.gov/legal/"
CHRONAM_RIGHTS = "https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/"
CHRONAM = "https://www.loc.gov/collections/chronicling-america/"
LOC_BUCKETS = {   # name: (endpoint, facet, Library of Congress collection named in the citation, pages expected)
    "photo": ("https://www.loc.gov/photos/", "location_state:kansas", "Photos, Prints, Drawings", 2),
    "map": ("https://www.loc.gov/maps/", "location_state:kansas", "Maps", 2),
    "habs": ("https://www.loc.gov/collections/historic-american-buildings-landscapes-and-engineering-records/",
             "location:kansas", "Historic American Buildings Survey/Engineering Record/Landscapes Survey", 1),
}
LOC_SOURCE = "loc-gov-kansas-items"
LOC_TITLES_SOURCE = "loc-gov-chronam-kansas-titles"
LOC_ITEM_TABLE = "kfm_loc_items"
LOC_TITLE_TABLE = "kfm_loc_newspaper_titles"
LOC_ITEM_COLUMNS = ["bucket", "id", "title", "date", "dates_json", "location_json", "subject_json", "contributor_json",
                    "description_json", "rights", "online_format_json", "image_url_json", "url", "partof_json",
                    "original_format_json", "segments", "medium", "lccn", "shelf_id", "timestamp"]
LOC_DDL = (ddl(LOC_ITEM_TABLE, LOC_ITEM_COLUMNS, {"bucket": "TEXT NOT NULL", "id": "TEXT NOT NULL", "segments": "INTEGER"},
               [("bucket", "date"), ("id",), ("lccn", "date")])
           + ddl(LOC_TITLE_TABLE, TITLE_COLUMNS, {"lccn": "TEXT NOT NULL", "issue_count": "INTEGER"}, [("lccn",)]))
_SEGMENT_PAGE_SIZE = re.compile(r"([?&])c=\d+&?")


def _pause(ctx) -> None:
    time.sleep(getattr(ctx, "pause", LOC_PAUSE))


def _page(ctx, url: str):
    """One loc.gov JSON answer: (Fetched, dict), or None when the provider failed and a smaller page may do. A 429, a
    403 or an HTML page stops the run."""
    try:
        fetched = ctx.fetch(url, limit=LOC_PAGE_LIMIT, timeout=LOC_TIMEOUT, attempts=1)
    except FeedError as error:
        reason = str(error)
        if reason.startswith(("HTTP_429", "HTTP_403")):
            raise FeedError(f"LOC_RATE_LIMITED {url}") from None
        if reason.startswith(("HTTP_5", "FETCH_FAILED")):
            ctx.note("loc_page_failed", url=url, reason=reason.split(" ", 1)[0])
            return None
        raise
    body = fetched.body.lstrip()
    if body[:1] == b"<":
        raise FeedError(f"LOC_RATE_LIMITED {url}")
    try:
        answer = json.loads(body)
        if not isinstance(answer["results"], list) or not isinstance(answer["pagination"], dict):
            raise ValueError
    except (ValueError, KeyError, TypeError):
        ctx.note("loc_page_failed", url=url, reason="not the JSON expected")
        return None
    return fetched, answer


def _url(endpoint: str, facet: str, size: int, sp: int, dl: str | None = None) -> str:
    query = [("fa", facet), *([("dl", dl)] if dl else []), ("fo", "json"), ("c", size), ("sp", sp), ("at", "results,pagination")]
    return endpoint + "?" + urllib.parse.urlencode(query, safe=":|,")


class _Unavailable(Exception):
    """A segment's page failed at every page size."""


class _Budget:
    def __init__(self, max_pages: int):
        self.max_pages, self.pages = max_pages, 0

    def admits(self, estimate: int) -> bool:
        """Whether a segment of estimate pages starts. The first segment of a run always does, so a title larger than
        max_pages still loads."""
        return self.pages == 0 or self.pages + estimate <= self.max_pages


def _pull(ctx, budget: _Budget, endpoint: str, facet: str, dl: str | None = None) -> tuple[list, object, int]:
    """Every result of one query: (results, the last Fetched, the query's count). See the module docstring for paging."""
    results, seen, sizes, fetched, expected, tries = [], set(), list(LOC_PAGE_SIZES), None, None, 0
    while True:
        size = sizes[0]
        url = _url(endpoint, facet, size, len(results) // size + 1, dl)
        if budget.pages:
            _pause(ctx)
        budget.pages += 1
        got = _page(ctx, url)
        if got is None:
            tries += 1
            if tries >= LOC_PAGE_TRIES:
                sizes.pop(0)
                tries = 0
                if not sizes:
                    raise _Unavailable(url)
            time.sleep(getattr(ctx, "pause", LOC_RETRY_WAIT))
            continue
        fetched, answer = got
        tries = 0
        paging = answer["pagination"]
        if paging.get("perpage") != size:
            raise FeedError(f"LOC_PAGE_SIZE_CHANGED {url}")
        if not isinstance(paging.get("of"), int) or (expected is not None and paging["of"] != expected):
            raise FeedError(f"LOC_RESULTS_SHIFTED {url}")
        expected = paging["of"]
        for result in answer["results"]:
            if result.get("id") in seen:
                raise FeedError(f"LOC_RESULTS_SHIFTED {url}")
            seen.add(result.get("id"))
            results.append(result)
        if not answer["results"] or not paging.get("next") or len(results) >= expected:
            break
    if len(results) != expected:
        raise FeedError(f"LOC_RESULTS_SHIFTED {url}")
    return results, fetched, expected


def _segments_stable(segments):
    return [{**s, "link": _SEGMENT_PAGE_SIZE.sub(lambda m: m.group(1) if m.group(0).endswith("&") else "", s["link"])}
            if isinstance(s, dict) and isinstance(s.get("link"), str) else s for s in segments]


def canonical_item(result: dict) -> dict:
    """A result without what differs from one request to the next (see the module docstring)."""
    item = {}
    for name, value in result.items():
        if name == "index":
            continue
        if name == "segments" and isinstance(value, list):
            value = _segments_stable(value)
        elif isinstance(value, list) and all(isinstance(v, str) for v in value):
            value = sorted(value)
        item[name] = value
    return item


def _jsonl(results: list) -> bytes:
    lines = sorted(core.canonical(canonical_item(r)) for r in results)
    return core.gz("".join(line + "\n" for line in lines).encode())


def _read_jsonl(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


def _json_or_none(value):
    return core.canonical(value) if value not in (None, [], {}, "") else None


def _text(value):
    if isinstance(value, list):
        return "; ".join(str(v) for v in value) or None
    return value if value not in (None, "") else None


def item_row(bucket: str, record: dict) -> tuple:
    """A kfm_loc_items row from one kept record."""
    nested = record["item"] if isinstance(record.get("item"), dict) else {}
    pages = [s["count"] for s in record.get("segments") or [] if isinstance(s, dict) and isinstance(s.get("count"), int)]
    lccn = record.get("number_lccn") or nested.get("library_of_congress_control_number")
    shelf = record.get("shelf_id")
    return (bucket, record.get("id"), _text(record.get("title")), _text(record.get("date") or nested.get("date") or nested.get("created_published_date")), _json_or_none(record.get("dates")),
            _json_or_none(record.get("location")), _json_or_none(record.get("subject")), _json_or_none(record.get("contributor")),
            _json_or_none(record.get("description")), _text(nested.get("rights_information") or nested.get("rights_advisory") or record.get("rights")),
            _json_or_none(record.get("online_format")), _json_or_none(record.get("image_url")), record.get("url"), _json_or_none(record.get("partof")),
            _json_or_none(record.get("original_format")), sum(pages) if pages else None, _text(nested.get("medium")),
            lccn[0] if isinstance(lccn, list) and lccn else lccn if isinstance(lccn, str) else None, _text(shelf), record.get("timestamp"))


def _load_items(ctx, db, key: str, name: str, bucket: str, results: list, fetched, citation: str) -> dict:
    extra = {"citation": f"Library of Congress, {citation}, loc.gov JSON API", "license": LOC_LICENSE, "terms": LOC_TERMS,
             "records": len(results), **({"rights": CHRONAM_RIGHTS} if bucket == "newspaper" else {})}
    return keep_version(ctx, db, feed="loc-kansas", source_id=LOC_SOURCE, key=key, name=name, ext=".jsonl.gz", body=_jsonl(results),
                        url=fetched.url, fetched=fetched, table=LOC_ITEM_TABLE, width=len(LOC_ITEM_COLUMNS), extra=extra,
                        rows=lambda path: (item_row(bucket, record) for record in _read_jsonl(path)))


def _title_entry(row: tuple) -> dict:
    return {"issue_count": row[7], "first_issue": row[5], "last_issue": row[6]}


def _titles_due(state: dict, today: date, titles: dict) -> list:
    """The titles whose issues to pull, in order: smallest first, so one bad title does not hold back the rest."""
    loaded = state.get("titles", {})
    due = []
    for lccn, entry in titles.items():
        old = loaded.get(lccn)
        if (not old or not old.get("pulled") or any(old.get(k) != entry[k] for k in entry)
                or (age_days(old, "pulled", today) or 0) >= LOC_ISSUES_DAYS):
            due.append(lccn)
    return sorted(due, key=lambda lccn: ((titles[lccn]["issue_count"] or 0), lccn))


def _load_titles(ctx, db, budget: _Budget, state: dict, today: date, summary: dict) -> tuple[dict, dict]:
    """The title list, from the kept copy when not due. Returns (state, {lccn: entry})."""
    if (age_days(state, "titles_pulled", today) is None or age_days(state, "titles_pulled", today) >= LOC_TITLES_DAYS) and budget.admits(1):
        try:
            results, fetched, _ = _pull(ctx, budget, CHRONAM, "location_state:kansas", "title")
        except _Unavailable:
            raise FeedError("LOC_UNAVAILABLE newspaper-titles") from None
        rows = [title_row(r) for r in results]
        if not rows or any(row[0] is None for row in rows):
            raise FeedError("LOC_TITLES_SHAPE")
        result = keep_version(ctx, db, feed="loc-kansas", source_id=LOC_TITLES_SOURCE, key="newspaper-titles", name="newspaper-titles",
                              ext=".jsonl.gz", body=_jsonl(results), url=fetched.url, fetched=fetched, table=LOC_TITLE_TABLE,
                              width=len(TITLE_COLUMNS),
                              extra={"citation": "Chronicling America: Historic American Newspapers. Library of Congress", "license": LOC_LICENSE,
                                     "rights": CHRONAM_RIGHTS, "terms": LOC_TERMS, "records": len(rows)},
                              rows=lambda path: (title_row(record) for record in _read_jsonl(path)))
        summary["titles"] = result["state"]
        summary["rows"] += result["rows"]
        state = save_state(ctx, db, "loc-kansas", {**state, "titles_pulled": str(today)})
    rows = db.execute(f"SELECT {', '.join(TITLE_COLUMNS)} FROM {LOC_TITLE_TABLE}").fetchall()
    return state, {row[0]: _title_entry(row) for row in rows}


def loc_kansas(ctx, max_pages: int = 50) -> dict:
    """Kansas items and newspaper indexes from the Library of Congress: backfilled and refreshed in segments, within
    ``max_pages`` loc.gov pages a run. See the module docstring."""
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(LOC_DDL)
        state, today = core.get_state(db, "loc-kansas"), ctx.now().date()
        budget = _Budget(max_pages)
        summary = {"loaded": [], "unchanged": [], "rows": 0, "pending": []}
        unavailable = []
        state, titles = _load_titles(ctx, db, budget, state, today, summary)
        buckets = dict(state.get("buckets", {}))
        for bucket, (endpoint, facet, citation, pages) in LOC_BUCKETS.items():
            age = age_days(buckets.get(bucket, {}), "pulled", today)
            if age is not None and age < LOC_BUCKET_DAYS:
                continue
            if not budget.admits(pages) or len(unavailable) >= LOC_UNAVAILABLE_SEGMENTS:
                summary["pending"].append(bucket)
                continue
            try:
                results, fetched, _ = _pull(ctx, budget, endpoint, facet)
            except _Unavailable:
                unavailable.append(bucket)
                summary["pending"].append(bucket)
                continue
            result = _load_items(ctx, db, bucket, bucket, bucket, results, fetched, citation)
            summary["unchanged" if result["state"] == "unchanged" else "loaded"].append(bucket)
            summary["rows"] += result["rows"]
            buckets[bucket] = {"pulled": str(today), "records": len(results)}
            state = save_state(ctx, db, "loc-kansas", {**state, "buckets": buckets})
        loaded_titles = dict(state.get("titles", {}))
        for lccn in _titles_due(state, today, titles):
            pages = (titles[lccn]["issue_count"] or 0) // 1000 + 1
            key = f"newspaper/{lccn}"
            if not budget.admits(pages) or len(unavailable) >= LOC_UNAVAILABLE_SEGMENTS:
                summary["pending"].append(key)
                continue
            try:
                results, fetched, _ = _pull(ctx, budget, CHRONAM, f"location_state:kansas|number_lccn:{lccn}", "issue")
            except _Unavailable:
                unavailable.append(key)
                summary["pending"].append(key)
                continue
            if results:
                result = _load_items(ctx, db, key, key, "newspaper", results, fetched, "Chronicling America: Historic American Newspapers")
                summary["unchanged" if result["state"] == "unchanged" else "loaded"].append(key)
                summary["rows"] += result["rows"]
            elif key in loaded_keys(db, LOC_SOURCE):
                with core.pipeline_lock(ctx):
                    retire(db, LOC_SOURCE, key, LOC_ITEM_TABLE)
            loaded_titles[lccn] = {**titles[lccn], "pulled": str(today), "records": len(results)}
            state = save_state(ctx, db, "loc-kansas", {**state, "titles": loaded_titles})
        unlisted = sorted(k.split("/", 1)[1] for k in loaded_keys(db, LOC_SOURCE) if k.startswith("newspaper/") and k.split("/", 1)[1] not in titles)
        result = {**summary, "pages": budget.pages, "pending_segments": len(summary["pending"]), "pending": summary["pending"][:20],
                  "titles_listed": len(titles), "titles_pulled": len(loaded_titles)}
        if unlisted:
            ctx.note("loc_titles_unlisted", titles=unlisted)
            raise FeedError(f"LOC_TITLE_UNLISTED {','.join(unlisted[:10])}")
        if unavailable:
            raise FeedError(f"LOC_UNAVAILABLE {','.join(unavailable)}")
        return result
    finally:
        db.close()
