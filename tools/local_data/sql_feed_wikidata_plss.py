"""SQL feeds for Wikidata's Kansas items and the BLM Public Land Survey System grid for Kansas.

Both feeds keep every provider answer cut to Kansas and gzipped under ``data/raw/sql-feeds/<feed>/``, named by
the first 12 hex of its SHA-256, and load it with ``keep_version`` under a stable key, so a changed segment
replaces the one loaded before in one transaction and an unchanged one is not loaded again. Network work runs
outside the pipeline lock; database writes inside it. This module is a rebuild of the lost original from its
receipts, raw files, feed state and table DDL; where the original's choice could not be recovered the docstring
says so, and the kept bytes are reproduced canonically so an unchanged segment is recognized as unchanged.

``wikidata-kansas``: the Wikidata Query Service (https://query.wikidata.org/sparql; data CC0 1.0,
https://www.wikidata.org/wiki/Wikidata:Licensing). Four groups: ``places`` (items ``wdt:P131*`` Kansas, Q1558,
or Kansas Territory, Q1723905; 15,648 on 2026-11-03), ``places-box`` (items with coordinates in the Kansas box
that the first group does not have, kept only when a coordinate falls in a 2025 TIGER Kansas county; 344 of
1,706), ``people`` (humans born, died, resident, working or educated at a Kansas place; 13,242) and ``events``
(dated items located in Kansas; 1,599). A cycle starts with one index query per group; each group's item ids
are then cut into ranges of the id space [0, 2^28), halved until a range holds at most 1,000 items, and each
range with items is one ``load_version`` key ``<group>/Q<lo>-Q<hi>`` (source ``wikidata-<group>``). A range is
filled by detail queries of at most 375 items each (``VALUES ?item``: labels, description, enwiki title, the
group's direct properties with labels, dated statements with precision and rank, population with its date),
turned into one canonical JSON record per item (sorted keys, lists sorted by their canonical text, deprecated
ranks dropped, labels in English or ``mul``) and kept as JSON Lines in ascending id order. The receipt carries
the index and detail query texts (the item list elided as ``wd:Q…``), ``cycle``, ``group``, ``requested``,
``items``, ``missing``, ``outside_kansas`` and ``queries``. The feed state keeps ``cycle`` (``started``,
``complete``, ``done`` keys), ``items`` per group and ``ranges`` per group, so a run that stops on WDQS's
per-IP throttling (HTTP 429, ``WIKIDATA_RATE_LIMITED``) or on its query budget resumes from the next pending
range; queries are two seconds apart. When every range is done the cycle is complete and keys the cycle did
not produce are retired; a new cycle starts seven days after the last began. Needs ``ctx.tiger`` for county
GEOIDs. The index queries of ``people`` and ``events`` and the 375-item batch size are reconstructions (the
receipts only fix the places queries and the batch count per range).

``plss-grid``: the BLM Public Land Survey System grid for Kansas, the survey frame land patents are described
against. Townships, sections (first divisions) and intersected (second divisions) come from the national
CadNSDI map service in NAD83 (``BLM_Natl_PLSS_CadNSDI_NAD83``, layers 1-3, requested with ``outSR=4326``);
survey points, special survey areas and meandered water from the BLM New Mexico State Office's hosted Kansas
layers on ArcGIS Online (public, no key). Public domain (U.S. Government work); BLM's disclaimer that the data
are not a legal survey goes in every receipt. Each feature is kept as a canonical GeoJSON Feature line in
OBJECTID order under ``kfm_blm_plss_<layer>`` with every provider field in snake_case, ``geometry_geojson``
and, except for the points, a bounding box. Kansas test: ``STATEABBR='KS'`` (townships, intersected) or
``PLSSID LIKE 'KS%'`` (sections) in the query and on each feature, and every feature's envelope must meet the
Kansas box, else ``BLM_NOT_KANSAS``. Segments: townships, special surveys and meandered water are one key each
(``<layer>/KS``); sections, intersected and survey points are blocks of 2,000 OBJECTIDs (``<layer>/oid-<first>``),
one page each, paged on by OBJECTID when the server returns a shorter page. Every 28 days each layer is
described (its fields must still match, else ``BLM_FIELDS_CHANGED``) and asked for its Kansas count and
OBJECTID range (``BLM_KANSAS_EMPTIED`` if a loaded layer answers none); the national sections and intersected
layers also give, in three grouped statistics answers, a fingerprint per township (count, OBJECTID range,
summed area and length), and a block is fetched again only when the fingerprint of a township whose features
reach into it changed; the hosted layers are fetched again when their ``dataLastEditDate`` changed; the
townships are fetched at every check; everything is fetched again after 182 days. Blocks that answer no
features are retired. At most 250 requests a run, one second apart; HTTP 429 or 503, or an ArcGIS error of
those codes, stops the run with ``BLM_RATE_LIMITED`` and keeps what loaded. The feed state keeps per layer
``checked``, ``since`` and ``segments`` {key: [fingerprint, date]}; the hosted fingerprint is
``edit:<dataLastEditDate>`` as in the recovered state, the township-hash fingerprint is a reconstruction, so the
first check under this rebuild fetches the national blocks once more (unchanged bytes are not loaded again).
"""
from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
import gzip
import hashlib
import json
from pathlib import Path
import re
import time
from typing import Callable
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, county_at, ddl, kansas_counties, keep_version, loaded_keys, retire, save_state, snake
from tools.local_data.sql_feeds import FeedError

KANSAS_BOX = (-102.06, 36.99, -94.58, 40.01)   # west, south, east, north
_sleep = time.sleep                               # replaced in tests


def _json(value):
    return core.canonical(value) if value is not None else None


# --- Wikidata --------------------------------------------------------------------------------------

SPARQL = "https://query.wikidata.org/sparql"
WIKIDATA_FEED = "wikidata-kansas"
WIKIDATA_TOP = 1 << 28
WIKIDATA_RANGE_ITEMS = 1000
WIKIDATA_BATCH = 375
WIKIDATA_CYCLE_DAYS = 7
WIKIDATA_QUERIES_PER_RUN = 400
WIKIDATA_PAUSE = 2.0
WIKIDATA_LIMIT = 64_000_000
WIKIDATA_EXTRA = {"citation": "Wikidata (https://www.wikidata.org), CC0 1.0, via the Wikidata Query Service", "license": "CC0-1.0",
                  "terms": "https://www.wikidata.org/wiki/Wikidata:Licensing"}
ROOTS = "VALUES ?root { wd:Q1558 wd:Q1723905 }"
BOX = ('SERVICE wikibase:box { ?item wdt:P625 ?where . bd:serviceParam wikibase:cornerSouthWest "Point(-102.06 36.99)"^^geo:wktLiteral . '
       'bd:serviceParam wikibase:cornerNorthEast "Point(-94.58 40.01)"^^geo:wktLiteral . }')
ENTITY = "http://www.wikidata.org/entity/"
POINT = re.compile(r"Point\((-?[\d.]+) (-?[\d.]+)\)")


@dataclass(frozen=True)
class Group:
    name: str
    source_id: str
    table: str
    index: str                 # the index query: SELECT DISTINCT ?item ?why
    direct: tuple              # direct properties fetched with labels
    dates: tuple               # statement properties fetched as time, precision and rank
    population: bool
    links: tuple               # properties whose values in the places index are the item's Kansas links
    box: bool                  # coordinates in a Kansas county are Kansas links too
    columns: tuple
    row: Callable


def detail_query(group: Group) -> str:
    """The receipts' detail query text, the item list elided (``wd:Q…``)."""
    text = ('SELECT ?item ?prop ?value ?valueLabel ?extra ?extra2 ?rank WHERE { VALUES ?item { wd:Q… } '
            f'{{ VALUES ?p {{ {" ".join("wdt:" + p for p in group.direct)} }} ?item ?p ?value . BIND(STRAFTER(STR(?p), "direct/") AS ?prop) '
            'OPTIONAL { ?value rdfs:label ?valueLabel FILTER(LANG(?valueLabel) IN ("en", "mul")) } } '
            'UNION { ?item rdfs:label ?value FILTER(LANG(?value) IN ("en", "mul")) BIND("label" AS ?prop) } '
            'UNION { ?item schema:description ?value FILTER(LANG(?value) = "en") BIND("description" AS ?prop) } '
            'UNION { ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?value . BIND("enwiki" AS ?prop) } '
            f'UNION {{ VALUES (?p ?psv) {{ {" ".join(f"(p:{p} psv:{p})" for p in group.dates)} }} ?item ?p ?st . ?st ?psv ?node ; wikibase:rank ?rank . '
            '?node wikibase:timeValue ?value ; wikibase:timePrecision ?extra . BIND(STRAFTER(STR(?p), "prop/") AS ?prop) }')
    if group.population:
        text += ' UNION { ?item p:P1082 ?st . ?st ps:P1082 ?value ; wikibase:rank ?rank . OPTIONAL { ?st pq:P585 ?extra } BIND("P1082" AS ?prop) }'
    return text + " }"


def _first_date(record: dict, prop: str):
    found = (record.get("dates") or {}).get(prop) or []
    if not found:
        return None, None
    value, precision = found[0]["time"].split("T", 1)[0], found[0]["precision"]
    parts = re.fullmatch(r"([+-]?\d+)-(\d{2})-(\d{2})", value)
    if parts and precision <= 10:
        value = parts[1] if precision <= 9 else f"{parts[1]}-{parts[2]}"
    return value, precision


def _population(record: dict):
    entries = record.get("population") or []
    best = [e for e in entries if e.get("rank") == "preferred"] or entries
    if not best:
        return None, None
    chosen = max(best, key=lambda e: e.get("date") or "")
    try:
        value = int(chosen["amount"])
    except ValueError:
        value = float(chosen["amount"])
    return value, chosen.get("date")


def _point(record: dict, counties):
    """Preserve the first provider coordinate and full geometry; classify any Kansas point by county."""
    coords = (record.get("claims") or {}).get("P625") or []
    if not coords:
        return None, None, None, None
    located = [(c, county_at(counties, c[0], c[1])) for c in coords]
    lon, lat = coords[0]
    geoid = next((g for c, g in located if g), None)
    geometry = {"type": "Point", "coordinates": coords[0]} if len(coords) == 1 else {"type": "MultiPoint", "coordinates": coords}
    return lon, lat, core.canonical(geometry), geoid


def _place_row(record: dict, line: str, counties) -> tuple:
    claims = record.get("claims") or {}
    lon, lat, geometry, geoid = _point(record, counties)
    inception, inception_precision = _first_date(record, "P571")
    dissolved, dissolved_precision = _first_date(record, "P576")
    population, population_date = _population(record)
    return (record["qid"], record.get("label"), record.get("description"), _json(claims.get("P31")), _json(claims.get("P131")), lon, lat, geometry,
            geoid, inception, inception_precision, dissolved, dissolved_precision, _json(claims.get("P590")), _json(claims.get("P649")), population,
            population_date, _json(claims.get("P856")), record.get("enwiki"), record.get("kansas_link"), _json(record.get("kansas") or None), line)


def _person_row(record: dict, line: str, counties) -> tuple:
    claims = record.get("claims") or {}
    birth, birth_precision = _first_date(record, "P569")
    death, death_precision = _first_date(record, "P570")
    return (record["qid"], record.get("label"), record.get("description"), birth, birth_precision, _json(claims.get("P19")), death, death_precision,
            _json(claims.get("P20")), _json(claims.get("P106")), _json(claims.get("P39")), _json(claims.get("P69")), record.get("enwiki"),
            _json(record.get("kansas") or None), line)


def _event_row(record: dict, line: str, counties) -> tuple:
    claims = record.get("claims") or {}
    lon, lat, geometry, geoid = _point(record, counties)
    when, when_precision = _first_date(record, "P585")
    start, start_precision = _first_date(record, "P580")
    end, end_precision = _first_date(record, "P582")
    return (record["qid"], record.get("label"), record.get("description"), _json(claims.get("P31")), when, when_precision, start, start_precision,
            end, end_precision, _json(claims.get("P276")), _json(claims.get("P131")), lon, lat, geometry, geoid, record.get("enwiki"),
            _json(record.get("kansas") or None), line)


PLACE_COLUMNS = ("qid", "label", "description", "classes_json", "located_in_json", "longitude", "latitude", "geometry_geojson", "county_geoid",
                 "inception", "inception_precision", "dissolved", "dissolved_precision", "gnis_ids_json", "nrhp_refs_json", "population",
                 "population_date", "official_websites_json", "enwiki_title", "kansas_link", "kansas_links_json", "record_json")
PEOPLE_COLUMNS = ("qid", "label", "description", "birth_date", "birth_precision", "birth_places_json", "death_date", "death_precision",
                  "death_places_json", "occupations_json", "positions_json", "educated_at_json", "enwiki_title", "kansas_links_json", "record_json")
EVENT_COLUMNS = ("qid", "label", "description", "classes_json", "point_in_time", "point_in_time_precision", "start_time", "start_precision",
                 "end_time", "end_precision", "locations_json", "located_in_json", "longitude", "latitude", "geometry_geojson", "county_geoid",
                 "enwiki_title", "kansas_links_json", "record_json")
PLACE_PROPS = (("P31", "P131", "P625", "P590", "P649", "P856"), ("P571", "P576"), True)
GROUPS = (
    Group("places", "wikidata-places", "kfm_wikidata_places",
          f'SELECT DISTINCT ?item ?why WHERE {{ {ROOTS} ?item wdt:P131* ?root . BIND("P131" AS ?why) }}',
          *PLACE_PROPS, ("P131",), False, PLACE_COLUMNS, _place_row),
    Group("places-box", "wikidata-places-box", "kfm_wikidata_places",
          f'SELECT DISTINCT ?item ?why WHERE {{ {BOX} BIND("P625" AS ?why) }}',
          *PLACE_PROPS, ("P131",), True, PLACE_COLUMNS, _place_row),
    Group("people", "wikidata-people", "kfm_wikidata_people",
          f'SELECT DISTINCT ?item ?why WHERE {{ {ROOTS} VALUES ?p {{ wdt:P19 wdt:P20 wdt:P551 wdt:P937 wdt:P69 }} ?place wdt:P131* ?root . '
          '?item ?p ?place . ?item wdt:P31 wd:Q5 . BIND(STRAFTER(STR(?p), "direct/") AS ?why) }',
          ("P19", "P20", "P551", "P937", "P69", "P106", "P39"), ("P569", "P570"), False, ("P19", "P20", "P551", "P937", "P69"), False,
          PEOPLE_COLUMNS, _person_row),
    Group("events", "wikidata-events", "kfm_wikidata_events",
          f'SELECT DISTINCT ?item ?why WHERE {{ {{ {ROOTS} ?place wdt:P131* ?root . ?item wdt:P276 ?place . BIND("P276" AS ?why) }} '
          f'UNION {{ {BOX} BIND("P625" AS ?why) }} ?item wdt:P585|wdt:P580 ?when . }}',
          ("P31", "P276", "P131", "P625"), ("P585", "P580", "P582"), False, ("P276", "P131"), True, EVENT_COLUMNS, _event_row),
)
WIKIDATA_TYPES = {"qid": "TEXT NOT NULL", "record_json": "TEXT NOT NULL", "longitude": "REAL", "latitude": "REAL", "population": "NUMERIC",
                  **{c: "INTEGER" for c in ("inception_precision", "dissolved_precision", "birth_precision", "death_precision",
                                            "point_in_time_precision", "start_precision", "end_precision")}}
WIKIDATA_DDL = (ddl("kfm_wikidata_places", PLACE_COLUMNS, WIKIDATA_TYPES, [("county_geoid",), ("label",), ("qid",)])
                + ddl("kfm_wikidata_people", PEOPLE_COLUMNS, WIKIDATA_TYPES, [("birth_date",), ("label",), ("qid",)])
                + ddl("kfm_wikidata_events", EVENT_COLUMNS, WIKIDATA_TYPES, [("point_in_time",), ("qid",), ("start_time",)]))


def item_ranges(ids, top: int = WIKIDATA_TOP, limit: int = WIKIDATA_RANGE_ITEMS) -> list:
    """[[lo, hi], ...] covering [0, top): halved until no range holds more than limit items."""
    ids = sorted(ids)
    while ids and ids[-1] >= top:
        top *= 2
    out = []

    def split(lo, hi):
        if bisect_right(ids, hi - 1) - bisect_left(ids, lo) > limit and hi - lo > 1:
            split(lo, (lo + hi) // 2)
            split((lo + hi) // 2, hi)
        else:
            out.append([lo, hi])
    split(0, top)
    return out


class _Budget:
    """Counts a run's queries, pauses between them and stops at the cap."""

    def __init__(self, limit: int, pause: float):
        self.limit, self.pause, self.used = limit, pause, 0

    def left(self) -> bool:
        return self.used < self.limit

    def take(self) -> None:
        if not self.left():
            raise FeedError("QUERY_BUDGET")
        if self.used:
            _sleep(self.pause)
        self.used += 1


def _sparql(ctx, budget: _Budget, query: str) -> tuple[bytes, list]:
    budget.take()
    url = SPARQL + "?format=json&query=" + urllib.parse.quote(query, safe="")
    try:
        fetched = ctx.fetch(url, limit=WIKIDATA_LIMIT, timeout=120)
    except FeedError as error:
        if str(error).startswith("HTTP_429"):
            raise FeedError("WIKIDATA_RATE_LIMITED") from None
        raise
    try:
        payload = json.loads(fetched.body)
    except ValueError:
        raise FeedError("WIKIDATA_RESPONSE_SHAPE") from None
    bindings = (payload.get("results") or {}).get("bindings") if isinstance(payload, dict) else None
    if not isinstance(bindings, list) or any(not isinstance(b, dict) for b in bindings):
        raise FeedError("WIKIDATA_RESPONSE_SHAPE")
    return fetched.body, bindings


def _entity(binding) -> str | None:
    value = (binding or {}).get("value", "")
    return value[len(ENTITY):] if (binding or {}).get("type") == "uri" and value.startswith(ENTITY) else None


def _rank(binding) -> str:
    return (binding or {}).get("value", "NormalRank").rsplit("#", 1)[-1].removesuffix("Rank").lower()


def _index(ctx, budget: _Budget, group: Group) -> dict:
    """{numeric id: {why, ...}} of the group's items."""
    _, bindings = _sparql(ctx, budget, group.index)
    items = defaultdict(set)
    for binding in bindings:
        qid = _entity(binding.get("item"))
        if qid is None or not qid[1:].isdigit():
            raise FeedError(f"WIKIDATA_RESPONSE_SHAPE {group.name} index")
        items[int(qid[1:])].add(binding.get("why", {}).get("value", group.links[0] if group.links else "P625"))
    return items


def _record(qid: str, bindings: list, group: Group, whys: set, places: set, counties) -> dict:
    claims, labels_of, dates, population, labels, entities = defaultdict(dict), defaultdict(dict), defaultdict(set), {}, {}, set()
    description = enwiki = None
    for binding in bindings:
        prop, value = binding.get("prop", {}).get("value"), binding.get("value") or {}
        text = value.get("value")
        if prop == "label":
            labels[value.get("xml:lang")] = text
        elif prop == "description":
            description = text
        elif prop == "enwiki":
            enwiki = text
        elif prop in group.dates:
            if _rank(binding.get("rank")) != "deprecated":
                dates[prop].add((int(binding.get("extra", {}).get("value")), text))
        elif prop == "P1082":
            if group.population and _rank(binding.get("rank")) != "deprecated":
                population[(text, binding.get("extra", {}).get("value"), _rank(binding.get("rank")))] = None
        elif prop in group.direct:
            if prop == "P625":
                found = POINT.fullmatch(text or "")
                if found:
                    claims[prop][(float(found.group(1)), float(found.group(2)))] = None
            elif (ident := _entity(value)) is not None:
                claims[prop].setdefault(ident, None)
                entities.add(prop)
                label = binding.get("valueLabel")
                if label:
                    labels_of[ident][label.get("xml:lang")] = label.get("value")
            else:
                claims[prop][text] = None
    out = {"qid": qid, "label": labels.get("en", labels.get("mul")), "labels": labels, "claims": {}, "dates": {}}
    for prop, values in claims.items():
        if prop == "P625":
            listed = [list(c) for c in values]
        elif prop in entities:
            listed = [{"id": v, "label": labels_of[v].get("en", labels_of[v].get("mul"))} for v in values]
        else:
            listed = list(values)
        out["claims"][prop] = sorted(listed, key=core.canonical)
    for prop, values in dates.items():
        out["dates"][prop] = sorted([{"precision": p, "time": t} for p, t in values], key=core.canonical)
    if description is not None:
        out["description"] = description
    if enwiki is not None:
        out["enwiki"] = enwiki
    if population:
        out["population"] = sorted([{"amount": a, "rank": r, **({"date": d} if d is not None else {})} for a, d, r in population], key=core.canonical)
    links = [{"id": e["id"], "label": e["label"], "property": p} for p in group.links for e in out["claims"].get(p, []) if e["id"] in places]
    if group.box:
        links += [{"county_geoid": g, "property": "P625"} for lon, lat in out["claims"].get("P625", []) if (g := county_at(counties, lon, lat))]
    out["kansas"] = sorted({core.canonical(l): l for l in links}.values(), key=core.canonical)
    out["kansas_link"] = sorted(whys)[0]
    return out


def _wikidata_rows(path: Path, group: Group, counties):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            yield group.row(json.loads(line), line, counties)


def _fill_range(ctx, db, budget: _Budget, group: Group, lo: int, hi: int, items: dict, places: set, counties, cycle: str) -> dict:
    """Fetch the range's items in batches, keep the Kansas records as the key's version and load them."""
    ids = [i for i in sorted(items) if lo <= i < hi]
    key, records, bodies, queries, seen = f"{group.name}/Q{lo}-Q{hi}", [], [], 0, set()
    template = detail_query(group)
    for start in range(0, len(ids), WIKIDATA_BATCH):
        batch = ids[start:start + WIKIDATA_BATCH]
        body, bindings = _sparql(ctx, budget, template.replace("wd:Q…", " ".join(f"wd:Q{i}" for i in batch)))
        queries += 1
        bodies.append(body)
        grouped = defaultdict(list)
        for binding in bindings:
            qid = _entity(binding.get("item"))
            if qid is None:
                raise FeedError(f"WIKIDATA_RESPONSE_SHAPE {key}")
            grouped[qid].append(binding)
        for i in batch:
            qid = f"Q{i}"
            if qid in grouped:
                seen.add(i)
                records.append(_record(qid, grouped[qid], group, items[i], places, counties))
    kept = [r for r in records if r["kansas"] or r["kansas_link"] != "P625"]
    extra = {**WIKIDATA_EXTRA, "cycle": cycle, "group": group.name, "index_query": group.index, "detail_query": template, "requested": len(ids),
             "items": len(kept), "missing": len(ids) - len(seen), "outside_kansas": len(records) - len(kept), "queries": queries}
    if not kept:
        with core.pipeline_lock(ctx):
            retire(db, group.source_id, key, group.table)
        return {"state": "empty", "rows": 0, **extra}
    kept.sort(key=lambda r: int(r["qid"][1:]))
    result = keep_version(ctx, db, feed=WIKIDATA_FEED, source_id=group.source_id, key=key, name=f"{key}/{group.name}-Q{lo}-Q{hi}", ext=".jsonl.gz",
                          body=core.gz("".join(core.canonical(r) + "\n" for r in kept).encode()), url=SPARQL, original=b"".join(bodies),
                          extra=extra, table=group.table, width=len(group.columns), rows=lambda path: _wikidata_rows(path, group, counties))
    return {**result, **extra}


def wikidata_kansas(ctx, max_queries: int = WIKIDATA_QUERIES_PER_RUN, cycle_days: int = WIKIDATA_CYCLE_DAYS) -> dict:
    if not ctx.tiger:
        raise FeedError("TIGER_GEOPACKAGE_REQUIRED")
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(WIKIDATA_DDL)
        state, today = core.get_state(db, WIKIDATA_FEED), ctx.now().date()
        cycle = state.get("cycle") or {}
        if cycle.get("complete"):
            age = age_days(cycle, "started", today)
            if age is not None and age < cycle_days:
                return {"state": "not_due", "cycle": cycle["started"]}
            cycle = {}
        fresh = not cycle
        if fresh:
            cycle = {"started": str(today), "complete": False, "done": []}
            state = {"cycle": cycle, "items": {}, "ranges": {}}
        budget, counties = _Budget(max_queries, WIKIDATA_PAUSE), kansas_counties(ctx.tiger)
        summary = {"cycle": cycle["started"], "loaded": 0, "unchanged": 0, "empty": 0, "rows": 0, "pending": 0, "queries": 0}
        done, places = set(cycle["done"]), None
        try:
            for group in GROUPS:
                pending = group.name not in state["ranges"] or any(
                    f"{group.name}/Q{lo}-Q{hi}" not in done for lo, hi in state["ranges"].get(group.name, []))
                if not pending:
                    continue
                if places is None:
                    places_index = _index(ctx, budget, GROUPS[0])
                    places = {f"Q{i}" for i in places_index}
                items = places_index if group is GROUPS[0] else _index(ctx, budget, group)
                if group.name == "places-box":
                    items = {i: w for i, w in items.items() if f"Q{i}" not in places}
                if not items and loaded_keys(db, group.source_id):
                    raise FeedError(f"WIKIDATA_INDEX_EMPTIED {group.name}")
                if group.name not in state["ranges"]:
                    state["ranges"][group.name] = item_ranges(items)
                state["items"][group.name] = len(items)
                state = save_state(ctx, db, WIKIDATA_FEED, state)
                for lo, hi in state["ranges"][group.name]:
                    key = f"{group.name}/Q{lo}-Q{hi}"
                    if key in done:
                        continue
                    result = _fill_range(ctx, db, budget, group, lo, hi, items, places, counties, cycle["started"])
                    summary[result["state"] if result["state"] in ("unchanged", "empty") else "loaded"] += 1
                    summary["rows"] += result["rows"]
                    done.add(key)
                    cycle["done"] = sorted(done, key=lambda k: (GROUP_ORDER[k.split("/")[0]], int(k.split("/Q")[1].split("-")[0])))
                    state = save_state(ctx, db, WIKIDATA_FEED, {**state, "cycle": cycle})
        except FeedError as error:
            if str(error) != "QUERY_BUDGET":
                raise
            summary["stopped"] = "QUERY_BUDGET"
        summary["queries"] = budget.used
        if summary.get("stopped"):
            # Ranges not done include the empty ones of groups whose index was not reached; the next run settles them.
            summary["pending"] = (sum(g.name not in state["ranges"] for g in GROUPS)
                                  + sum(1 for g in GROUPS for lo, hi in state["ranges"].get(g.name, [])
                                        if f"{g.name}/Q{lo}-Q{hi}" not in done))
        else:
            with core.pipeline_lock(ctx):
                summary["retired"] = 0
                for group in GROUPS:
                    for key in sorted(loaded_keys(db, group.source_id) - done):
                        summary["retired"] += retire(db, group.source_id, key, group.table)
            cycle["complete"] = True
            save_state(ctx, db, WIKIDATA_FEED, {**state, "cycle": cycle})
        return summary
    finally:
        db.close()


GROUP_ORDER = {g.name: n for n, g in enumerate(GROUPS)}


# --- BLM PLSS grid ---------------------------------------------------------------------------------

PLSS_FEED = "plss-grid"
PLSS_SOURCE = "blm-plss-cadnsdi-kansas"
BLM_NATIONAL = "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI_NAD83/MapServer"
BLM_HOSTED = "https://services1.arcgis.com/KbxwQRRfWyEYLgp4/arcgis/rest/services/BLM_NM_REGION_CadNSDI_{}_FOR_KS/FeatureServer"
BLM_BLOCK = 2000
BLM_PAGE = 2000
BLM_REQUESTS_PER_RUN = 250
BLM_RECHECK_DAYS = 28
BLM_FULL_DAYS = 182
BLM_PAUSE = 1.0
BLM_LIMIT = 256_000_000
BLM_TOWNSHIP_SPLITS = ("KS060120", "KS060240")   # three PLSSID ranges, each well under a 2,000-group statistics answer
BLM_LICENSE = "public domain (U.S. Government work, 17 U.S.C. 105); BLM: 'None, these data are considered public domain'"
BLM_DISCLAIMER = (
    "These data are provided by Bureau of Land Management (BLM) 'as is' and might contain errors or omissions. The User assumes the entire risk "
    "associated with its use of these data and bears all responsibility in determining whether these data are fit for the User's intended use. "
    "The information contained in these data is dynamic and may change over time. The data are not better than the sources from which they "
    "were derived, and both scale and accuracy may vary across the data set. These data might not have the accuracy, resolution, completeness, "
    "timeliness, or other characteristics appropriate for applications that potential users of the data may contemplate. The User is encouraged "
    "to carefully consider the content of the metadata file associated with these data. These data are neither legal documents nor land surveys, "
    "and must not be used as such. Official records may be referenced at most BLM offices. Please report any errors in the data to the BLM office "
    "from which it was obtained. The BLM should be cited as the data source in any products derived from these data. Any Users wishing to modify "
    "the data should describe the types of modifications they have performed. The User should not misrepresent the data, nor imply that changes "
    "made were approved or endorsed by BLM. This data may be updated by the BLM without notification.")
NATIONAL_CITATION = ("Bureau of Land Management, National Public Land Survey System, Cadastral National Spatial Data Infrastructure (CadNSDI), "
                     "BLM_Natl_PLSS_CadNSDI_NAD83 map service")
HOSTED_CITATION = "Bureau of Land Management, New Mexico State Office, CadNSDI for Kansas (BLM NM REGION CadNSDI ... FOR KS)"
NATIONAL_TERMS = "https://blm-egis.maps.arcgis.com/home/item.html?id=6822892a0201443f8d568b73c8baf653"
SPATIAL_REFERENCE = "EPSG:4326 (outSR=4326, transformed by the server from NAD83)"


@dataclass(frozen=True)
class Layer:
    name: str
    url: str                   # the layer's REST URL
    where: str
    fields: tuple              # provider fields as snake_case columns, in the table's order
    bbox: bool
    blocks: bool               # OBJECTID blocks, else one key "<layer>/KS"
    hosted: bool               # fingerprint by dataLastEditDate, else by township statistics
    indexes: tuple
    terms: str

    @property
    def table(self) -> str:
        return f"kfm_blm_plss_{self.name}"

    @property
    def citation(self) -> str:
        return HOSTED_CITATION if self.hosted else NATIONAL_CITATION

    def ddl(self) -> str:
        columns = ", ".join(f'"{c}" INTEGER' if c == "objectid" else f'"{c}"' for c in self.fields)
        geometry = '"geometry_geojson" TEXT' + (', "min_lon" REAL, "min_lat" REAL, "max_lon" REAL, "max_lat" REAL' if self.bbox else "")
        return (f"CREATE TABLE IF NOT EXISTS {self.table} (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, {columns}, {geometry}, "
                f"PRIMARY KEY(file_id, row_number));\n"
                + "".join(f"CREATE INDEX IF NOT EXISTS {self.table}_{'_'.join(i)} ON {self.table}({', '.join(f'{chr(34)}{c}{chr(34)}' for c in i)});\n"
                          for i in self.indexes))

    @property
    def width(self) -> int:
        return len(self.fields) + 1 + (4 if self.bbox else 0)

    def is_kansas(self, properties: dict) -> bool:
        if self.where == "STATEABBR='KS'":
            return properties.get("STATEABBR") == "KS"
        if self.where == "PLSSID LIKE 'KS%'":
            return str(properties.get("PLSSID") or "").startswith("KS")
        return True


TOWNSHIP_FIELDS = ("objectid", "stateabbr", "prinmercd", "prinmer", "twnshpno", "twnshpfrac", "twnshpdir", "rangeno", "rangefrac", "rangedir",
                   "twnshpdpcd", "plssid", "twnshplab", "srvname", "survtyp", "survtyptxt", "sourcedate", "sourceref", "steward", "secsrvname",
                   "created_user", "created_date", "last_edited_user", "last_edited_date", "origid", "part_count", "global_id", "shape_starea",
                   "shape_stlength")
SECTION_FIELDS = ("objectid", "plssid", "frstdivid", "frstdivtyp", "frstdivtxt", "frstdivno", "frstdivdup", "frstdivlab", "survtyp", "survtyptxt",
                  "sourcedate", "sourceref", "shape_starea", "shape_stlength")
INTERSECTED_FIELDS = ("objectid", "stateabbr", "prinmercd", "prinmer", "twnshpno", "twnshpfrac", "twnshpdir", "rangeno", "rangefrac", "rangedir",
                      "twnshpdpcd", "plssid", "steward", "twnshplab", "frstdivid", "frstdivtyp", "frstdivtxt", "frstdivno", "frstdivdup", "frstdivlab",
                      "secdivid", "secdivtyp", "secdivno", "secdivsuf", "secdivnote", "secdivlab", "survtyp", "survno", "survsuf", "survnote",
                      "survlab", "qsec", "qqsec", "govlot", "secdivtxt", "survid", "survtyptxt", "srvname", "survdiv", "sourceref", "sourcedate",
                      "recrdareatx", "recrdareano", "gisacre", "reviseddate", "shape_starea", "shape_stlength")
SURVEY_POINT_FIELDS = ("objectid", "plssid", "pointid", "pointlab", "xcoord", "ycoord", "zcoord", "elev", "relytxt", "relynumb", "errorx", "errory",
                       "errorz", "hdatum", "vdatum", "coordmeth", "coordsys", "steward1", "steward2", "local1", "local2", "local3", "local4",
                       "surveyyear", "reviseddate")
SPECIAL_SURVEY_FIELDS = ("objectid", "survid", "survtyp", "survtyptxt", "survno", "survsuf", "survnote", "survdiv", "survlab", "recrdareatx",
                         "recrdareano", "gisacre", "sourceref", "sourcedate", "shape_area", "shape_length")
MEANDERED_WATER_FIELDS = ("objectid", "survtyp", "survtyptxt", "shape_area", "shape_length")
LAYERS = (
    Layer("townships", BLM_NATIONAL + "/1", "STATEABBR='KS'", TOWNSHIP_FIELDS, True, False, False, (("plssid",), ("twnshplab",)), NATIONAL_TERMS),
    Layer("sections", BLM_NATIONAL + "/2", "PLSSID LIKE 'KS%'", SECTION_FIELDS, True, True, False, (("frstdivid",), ("plssid",)), NATIONAL_TERMS),
    Layer("intersected", BLM_NATIONAL + "/3", "STATEABBR='KS'", INTERSECTED_FIELDS, True, True, False, (("frstdivid",), ("plssid",), ("secdivid",)),
          NATIONAL_TERMS),
    Layer("survey_points", BLM_HOSTED.format("SURVEY_POINTS") + "/3", "1=1", SURVEY_POINT_FIELDS, False, True, True, (("plssid",), ("pointid",)),
          "https://www.arcgis.com/home/item.html?id=fcb4ea95da7d4153912b36fce0626d34"),
    Layer("special_surveys", BLM_HOSTED.format("SPECIAL_SURVEY_AREAS") + "/6", "1=1", SPECIAL_SURVEY_FIELDS, True, False, True,
          (("survtyp", "survno"),), "https://www.arcgis.com/home/item.html?id=5c975dcb578443a381572593e92bf677"),
    Layer("meandered_water", BLM_HOSTED.format("MEANDERED_WATER") + "/2", "1=1", MEANDERED_WATER_FIELDS, True, False, True, (),
          "https://www.arcgis.com/home/item.html?id=f471e9f511e8410a82f73151d9935cab"),
)
LAYER_BY_NAME = {layer.name: layer for layer in LAYERS}
PLSS_DDL = "".join(layer.ddl() for layer in LAYERS)


def column_name(field: str) -> str:
    """A provider field as a column: GlobalID -> global_id, SHAPE.STArea() -> shape_starea, Shape__Area -> shape_area."""
    return re.sub(r"[^a-z0-9]+", "_", snake(field)).strip("_")


def _coordinates(geometry) -> list:
    coords = (geometry or {}).get("coordinates")
    if not coords:
        return []
    if isinstance(coords[0], (int, float)):
        return [coords]
    return [p for part in coords for p in _coordinates({"coordinates": part})]


def _envelope(geometry):
    points = _coordinates(geometry)
    if not points:
        return None
    return (min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points))


def _meets_kansas(envelope) -> bool:
    west, south, east, north = KANSAS_BOX
    return envelope is not None and envelope[0] <= east and envelope[2] >= west and envelope[1] <= north and envelope[3] >= south


def _properties(layer: Layer, feature: dict) -> dict:
    """{column: value} of a feature, which must carry exactly the layer's fields."""
    properties = feature.get("properties") if isinstance(feature, dict) else None
    if not isinstance(properties, dict):
        raise FeedError(f"BLM_RESPONSE_SHAPE {layer.name}")
    columns = {column_name(k): v for k, v in properties.items()}
    if set(columns) != set(layer.fields):
        raise FeedError(f"BLM_FIELDS_CHANGED {layer.name} {sorted(set(columns) ^ set(layer.fields))[:5]}")
    return columns


def _plss_rows(path: Path, layer: Layer):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            feature = json.loads(line)
            columns = _properties(layer, feature)
            bounds = (_envelope(feature.get("geometry")) or (None,) * 4) if layer.bbox else ()
            yield (*(columns[c] for c in layer.fields), core.canonical(feature.get("geometry")), *bounds)


class _Blm:
    """ArcGIS REST requests under the run's cap, one second apart, with the provider's throttling as BLM_RATE_LIMITED."""

    def __init__(self, ctx, limit: int):
        self.ctx, self.limit, self.used = ctx, limit, 0

    def get(self, url: str) -> dict:
        if self.used >= self.limit:
            raise FeedError("REQUEST_BUDGET")
        if self.used:
            _sleep(BLM_PAUSE)
        self.used += 1
        try:
            body = self.ctx.fetch(url, limit=BLM_LIMIT, timeout=600).body
        except FeedError as error:
            if str(error).startswith(("HTTP_429", "HTTP_503")):
                raise FeedError("BLM_RATE_LIMITED") from None
            raise
        try:
            payload = json.loads(body)
        except ValueError:
            raise FeedError(f"BLM_RESPONSE_SHAPE {url[:100]}") from None
        if not isinstance(payload, dict):
            raise FeedError(f"BLM_RESPONSE_SHAPE {url[:100]}")
        if isinstance(payload.get("error"), dict):
            code = payload["error"].get("code")
            if code in (429, 503):
                raise FeedError("BLM_RATE_LIMITED")
            raise FeedError(f"BLM_QUERY_ERROR {code} {str(payload['error'].get('message'))[:80]}")
        return payload


def query_url(layer: Layer, lo: int, hi: int) -> str:
    where = f"({layer.where}) AND OBJECTID >= {lo} AND OBJECTID < {hi}"
    return layer.url + "/query?" + urllib.parse.urlencode([("where", where), ("outFields", "*"), ("outSR", 4326), ("orderByFields", "OBJECTID"),
                                                           ("resultRecordCount", BLM_PAGE), ("returnGeometry", "true"), ("f", "geojson")])


def _statistics(fields) -> list:
    out = [{"statisticType": "count", "onStatisticField": "OBJECTID", "outStatisticFieldName": "n"},
           {"statisticType": "min", "onStatisticField": "OBJECTID", "outStatisticFieldName": "lo"},
           {"statisticType": "max", "onStatisticField": "OBJECTID", "outStatisticFieldName": "hi"}]
    out += [{"statisticType": "sum", "onStatisticField": f, "outStatisticFieldName": n} for f, n in fields]
    return out


def _stats_url(layer: Layer, where: str, fields=(), group_by=None) -> str:
    params = [("where", where), ("outStatistics", json.dumps(_statistics(fields), separators=(",", ":")))]
    if group_by:
        params += [("groupByFieldsForStatistics", group_by), ("orderByFields", group_by)]
    return layer.url + "/query?" + urllib.parse.urlencode(params + [("returnGeometry", "false"), ("f", "json")])


def _attributes(payload: dict, layer: Layer) -> list:
    features = payload.get("features")
    if not isinstance(features, list) or any(not isinstance(f, dict) or not isinstance(f.get("attributes"), dict) for f in features):
        raise FeedError(f"BLM_RESPONSE_SHAPE {layer.name} statistics")
    return [f["attributes"] for f in features]


def _describe(blm: _Blm, layer: Layer) -> tuple:
    """(last edit date or None, provider names of the area and length fields) after checking the layer's fields."""
    payload = blm.get(layer.url + "?f=json")
    fields = payload.get("fields")
    if not isinstance(fields, list):
        raise FeedError(f"BLM_RESPONSE_SHAPE {layer.name} description")
    names = [str(f.get("name")) for f in fields if isinstance(f, dict) and f.get("type") != "esriFieldTypeGeometry"]
    if {column_name(n) for n in names} != set(layer.fields):
        raise FeedError(f"BLM_FIELDS_CHANGED {layer.name} {sorted({column_name(n) for n in names} ^ set(layer.fields))[:5]}")
    shape = {column_name(n): n for n in names}
    return (payload.get("editingInfo") or {}).get("dataLastEditDate"), (shape.get("shape_starea"), shape.get("shape_stlength"))


def _township_fingerprints(blm: _Blm, layer: Layer, shape_fields) -> dict:
    """{PLSSID: [count, first OBJECTID, last OBJECTID, area, length]} from three grouped statistics answers."""
    bounds = [None, *BLM_TOWNSHIP_SPLITS, None]
    fingerprints = {}
    for lo, hi in zip(bounds, bounds[1:]):
        where = " AND ".join([f"({layer.where})"] + ([f"PLSSID >= '{lo}'"] if lo else []) + ([f"PLSSID < '{hi}'"] if hi else []))
        fields = [(f, n) for f, n in zip(shape_fields, ("area", "length")) if f]
        for row in _attributes(blm.get(_stats_url(layer, where, fields, "PLSSID")), layer):
            fingerprints[str(row.get("PLSSID"))] = [row.get("n"), row.get("lo"), row.get("hi"), row.get("area"), row.get("length")]
    return fingerprints


def _block_fingerprint(fingerprints: dict, lo: int, hi: int) -> str:
    touching = {p: f for p, f in fingerprints.items() if isinstance(f[1], int) and isinstance(f[2], int) and f[1] < hi and f[2] >= lo}
    return hashlib.sha256(core.canonical(touching).encode()).hexdigest()[:16]


def _pull(blm: _Blm, layer: Layer, lo: int, hi: int) -> tuple[list, str]:
    """The layer's Kansas features with OBJECTID in [lo, hi), paged on by OBJECTID; and the first page's URL."""
    features, start, first = [], lo, None
    while start < hi:
        url = query_url(layer, start, hi)
        first = first or url
        payload = blm.get(url)
        page = payload.get("features")
        if not isinstance(page, list):
            raise FeedError(f"BLM_RESPONSE_SHAPE {layer.name}")
        for feature in page:
            columns = _properties(layer, feature)
            oid = columns["objectid"]
            if not isinstance(oid, int) or not start <= oid < hi:
                raise FeedError(f"BLM_SHIFTED {layer.name} OBJECTID {oid} outside {start}-{hi}")
            if not layer.is_kansas(feature["properties"]) or not _meets_kansas(_envelope(feature.get("geometry"))):
                raise FeedError(f"BLM_NOT_KANSAS {layer.name} OBJECTID {oid}")
            features.append({"geometry": feature.get("geometry"), "properties": feature["properties"], "type": "Feature"})
        if not page or (len(page) < BLM_PAGE and not (payload.get("properties") or {}).get("exceededTransferLimit")):
            break
        start = max(f["properties"]["OBJECTID"] for f in page) + 1
    features.sort(key=lambda f: f["properties"]["OBJECTID"])
    return features, first


def _keep_segment(ctx, db, blm: _Blm, layer: Layer, key: str, lo: int, hi: int, last_edit) -> dict:
    features, url = _pull(blm, layer, lo, hi)
    if not features:
        with core.pipeline_lock(ctx):
            return {"state": "empty", "rows": 0, "retired": retire(db, PLSS_SOURCE, key, layer.table)}
    name = key.split("/", 1)[1]
    extra = {"layer": layer.name, "where": layer.where, "service": layer.url, "objectids": [lo, hi - 1], "rows": len(features),
             "layer_last_edit": last_edit, "kansas_test": f"{layer.where} and the feature's envelope meets the Kansas box",
             "spatial_reference": SPATIAL_REFERENCE, "citation": layer.citation, "disclaimer": BLM_DISCLAIMER, "license": BLM_LICENSE,
             "terms": layer.terms}
    body = core.gz("".join(core.canonical(f) + "\n" for f in features).encode())
    return keep_version(ctx, db, feed=PLSS_FEED, source_id=PLSS_SOURCE, key=key, name=f"{layer.name}/plss-grid-{layer.name}-{name}", ext=".jsonl.gz",
                        body=body, url=url, extra=extra, table=layer.table, width=layer.width, rows=lambda path: _plss_rows(path, layer))


def _layer_run(ctx, db, blm: _Blm, layer: Layer, seen: dict, today, summary: dict) -> dict:
    """Check one layer and fetch its changed segments. Returns the layer's new state."""
    last_edit, shape_fields = _describe(blm, layer)
    stats = _attributes(blm.get(_stats_url(layer, layer.where)), layer)
    count = stats[0].get("n") if stats else 0
    segments = dict(seen.get("segments", {}))
    loaded = {k for k in loaded_keys(db, PLSS_SOURCE) if k.startswith(layer.name + "/")}
    if not count:
        if loaded:
            raise FeedError(f"BLM_KANSAS_EMPTIED {layer.name}")
        return {**seen, "checked": str(today), "segments": {}}
    lo, hi = stats[0].get("lo"), stats[0].get("hi")
    if not isinstance(lo, int) or not isinstance(hi, int) or hi < lo:
        raise FeedError(f"BLM_RESPONSE_SHAPE {layer.name} statistics")
    fingerprints = _township_fingerprints(blm, layer, shape_fields) if layer.blocks and not layer.hosted else {}
    if layer.blocks:
        wanted = [(f"{layer.name}/oid-{s}", s, s + BLM_BLOCK) for s in range(lo // BLM_BLOCK * BLM_BLOCK, hi + 1, BLM_BLOCK)]
    else:
        wanted = [(f"{layer.name}/KS", lo, hi + 1)]
    since = age_days(seen, "since", today)
    full = since is None or since >= BLM_FULL_DAYS
    layer_summary = {"loaded": 0, "unchanged": 0, "retired": 0, "rows": 0}
    with core.pipeline_lock(ctx):
        for key in sorted(loaded - {k for k, _, _ in wanted}):
            layer_summary["retired"] += retire(db, PLSS_SOURCE, key, layer.table)
            segments.pop(key, None)
    for key, start, stop in wanted:
        if layer.hosted:
            fingerprint = f"edit:{last_edit}"
        elif layer.blocks:
            fingerprint = _block_fingerprint(fingerprints, start, stop)
        else:
            fingerprint = f"stats:{count}:{lo}:{hi}"
        previous = segments.get(key)
        age = (today - date.fromisoformat(previous[1])).days if previous else None
        if previous and previous[0] == fingerprint and key in loaded and not full and not (age is not None and age >= BLM_FULL_DAYS) \
                and not (layer.name == "townships"):
            layer_summary["unchanged"] += 1
            continue
        result = _keep_segment(ctx, db, blm, layer, key, start, stop, last_edit)
        if result["state"] == "empty":
            layer_summary["retired"] += result["retired"]
            segments.pop(key, None)
        else:
            layer_summary["loaded" if result["state"] != "unchanged" else "unchanged"] += 1
            layer_summary["rows"] += result["rows"]
            segments[key] = [fingerprint, str(today)]
        save_state(ctx, db, PLSS_FEED, {**core.get_state(db, PLSS_FEED), layer.name: {**seen, "segments": segments}})
    summary[layer.name] = layer_summary
    for field in ("loaded", "unchanged", "retired", "rows"):
        summary[field] += layer_summary[field]
    return {"checked": str(today), "since": str(today) if full else seen.get("since", str(today)), "segments": segments}


def plss_grid(ctx, max_requests: int = BLM_REQUESTS_PER_RUN, recheck_days: int = BLM_RECHECK_DAYS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript(PLSS_DDL)
        state, today = core.get_state(db, PLSS_FEED), ctx.now().date()
        due = [layer for layer in LAYERS if (age := age_days(state.get(layer.name, {}), "checked", today)) is None or age >= recheck_days]
        if not due:
            return {"state": "not_due", "checked": {layer.name: state[layer.name]["checked"] for layer in LAYERS}}
        blm, summary = _Blm(ctx, max_requests), {"loaded": 0, "unchanged": 0, "retired": 0, "rows": 0, "requests": 0, "checked": []}
        try:
            for layer in due:
                state = {**core.get_state(db, PLSS_FEED), layer.name: _layer_run(ctx, db, blm, layer, state.get(layer.name, {}), today, summary)}
                save_state(ctx, db, PLSS_FEED, state)
                summary["checked"].append(layer.name)
        except FeedError as error:
            if str(error) != "REQUEST_BUDGET":
                raise
            summary["stopped"] = "REQUEST_BUDGET"
        summary["requests"] = blm.used
        return summary
    finally:
        db.close()
