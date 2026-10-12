#!/usr/bin/env python3
"""Bounded, TLS-verified public map metadata discovery; no map downloads.

NGMDB's publisher_list URL parameter is not a reliable server-side filter.
Reconcile the complete Kansas result list before declaring the explicitly
selected USGS/KGS publisher subsets complete. NMMR scope is a bounding rectangle
of map-index points, not a complete census of Kansas mines or mine-map documents.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[2]
SEED_PATH = ROOT / "apps/site/source/app/public-map-catalog.json"
NMMR = "https://geodata.osmre.gov/arcgis/rest/services/NMMR/MineMap_Points/MapServer/0"
NGMDB = "https://ngmdb.usgs.gov/ngm-bin/ngm_search_dbi.pl"
NGMDB_JSON = "https://ngmdb.usgs.gov/ngm-bin/ngm_search_json.pl"
# NCEI reissues Storm Events files under new creation dates (the _c suffix), so
# the current names are read from the publisher's own listing, never guessed.
STORM_EVENTS = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
STORM_EVENTS_FILE = re.compile(
    r"StormEvents_(details|fatalities|locations)-ftp_v1\.0_d(\d{4})_c(\d{8})\.csv\.gz\Z")
STORM_EVENTS_KINDS = ("details", "fatalities", "locations")
BBOX = "-102.052,36.993,-94.588,40.003"
PAGE_BYTES = 4 * 1024**2
TOTAL_BYTES = 64 * 1024**2
MAX_RECORDS = 10000
MAX_PAGES = 40
PAGE_SIZE = 200


def now():
    return datetime.now(timezone.utc).isoformat()


def load_seed():
    """Return a fresh, mutable copy of the shared researched reference catalog."""
    return json.loads(SEED_PATH.read_text(encoding="utf-8"))


def reconcile_seed(existing):
    """Overlay current curated references without replacing discovered metadata.

    Discovery time, coverage checks, and response receipts retain their original
    meaning. A separate seedAugmentation records additions made without network
    discovery, including newly verified selectable assets.
    """
    seed = load_seed()
    result = copy.deepcopy(existing)
    if result.get("schema") != seed["schema"]:
        raise ValueError("CATALOG_SCHEMA_INVALID")
    by_id = {record["id"]: record for record in result["records"]}
    if len(by_id) != len(result["records"]):
        raise ValueError("CATALOG_DUPLICATE_RECORD")
    changed = []
    for curated in seed["records"]:
        previous = by_id.get(curated["id"])
        if previous is None or not previous.get("discovered"):
            replacement = copy.deepcopy(curated)
        else:
            replacement = copy.deepcopy(previous)
            assets = {asset["id"]: asset for asset in replacement["assets"]}
            assets.update({asset["id"]: copy.deepcopy(asset) for asset in curated["assets"]})
            replacement["assets"] = list(assets.values())
            if curated["rights"]["status"] == "held":
                replacement["rights"] = copy.deepcopy(curated["rights"])
        replacement.setdefault("crs", None)
        replacement.setdefault("spatialAccuracy", None)
        if replacement != previous:
            changed.append(curated["id"])
            by_id[curated["id"]] = replacement
    result["records"] = list(by_id.values())
    defaults_applied = 0
    for record in result["records"]:
        missing = any(field not in record for field in ("crs", "spatialAccuracy"))
        record.setdefault("crs", None)
        record.setdefault("spatialAccuracy", None)
        defaults_applied += int(missing)
    urls = list(result.get("sourceUrls", []))
    for url in seed["sourceUrls"]:
        if url not in urls:
            urls.append(url)
    result["sourceUrls"] = urls
    coverage = {item["sourceId"]: item for item in result["coverage"]}
    for seed_coverage in seed["coverage"]:
        source = seed_coverage["sourceId"]
        item = coverage.setdefault(source, copy.deepcopy(seed_coverage))
        records = [record for record in result["records"] if record["sourceId"] == source]
        found = sum(bool(record.get("discovered")) for record in records)
        item.update(recordCount=len(records), discoveredCount=found,
                    seedReferenceCount=len(records) - found)
    result["coverage"] = list(coverage.values())
    if changed or defaults_applied:
        canonical_seed = json.dumps(seed, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        result["seedAugmentation"] = {"appliedAt": now(), "seedGeneratedAt": seed["generatedAt"],
            "seedSha256": hashlib.sha256(canonical_seed).hexdigest(), "updatedRecordIds": sorted(changed),
            "normalizationDefaultsApplied": defaults_applied, "discoveryRefreshed": False}
    return result


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def validate_metadata_url(url):
    parts = urlsplit(url)
    if (parts.scheme != "https" or parts.fragment or parts.username or parts.password
            or (parts.netloc, parts.path) not in {
                ("www.ncei.noaa.gov", urlsplit(STORM_EVENTS).path),
                ("geodata.osmre.gov", urlsplit(NMMR).path + "/query"),
                ("ngmdb.usgs.gov", urlsplit(NGMDB).path),
                ("ngmdb.usgs.gov", urlsplit(NGMDB_JSON).path)}):
        raise ValueError("METADATA_URL_DENIED")
    if parts.netloc == "www.ncei.noaa.gov":
        if parts.query:
            raise ValueError("STORM_EVENTS_QUERY_DENIED")
        return url
    query = parse_qs(parts.query, keep_blank_values=True, strict_parsing=True)
    if any(len(values) != 1 for values in query.values()):
        raise ValueError("DUPLICATE_QUERY_PARAMETER")
    if parts.netloc == "ngmdb.usgs.gov":
        if query.get("State") != ["KS"]:
            raise ValueError("KANSAS_QUERY_REQUIRED")
        allowed = {"Title", "Author", "map_number", "State", "bc_ule", "bc_lre",
                   "g_center", "g_zoom", "useextents", "bc_ul", "bc_lr", "publisher_list",
                   "scale", "scale2", "datebgn", "dateend", "format", "start", "sort"}
        if set(query) - allowed:
            raise ValueError("NGMDB_QUERY_PARAMETER_DENIED")
    return url


def fetch(url):
    """Read only fixed public metadata endpoints, without redirects or TLS bypass."""
    validate_metadata_url(url)
    opener = build_opener(ProxyHandler({}), NoRedirect())
    with opener.open(Request(url, headers={"User-Agent": "KFM-public-map-catalog/1",
                                          "Accept-Encoding": "identity"}), timeout=20) as response:
        if response.status != 200 or response.headers.get("Content-Encoding", "identity") != "identity":
            raise ValueError("METADATA_RESPONSE_INVALID")
        raw = response.read(PAGE_BYTES + 1)
        if len(raw) > PAGE_BYTES:
            raise ValueError("METADATA_PAGE_LIMIT")
        return raw


class Budget:
    def __init__(self, transport):
        self.transport, self.total, self.requests = transport, 0, 0
        self.receipts = []

    def read(self, url):
        validate_metadata_url(url)
        self.requests += 1
        if self.requests > MAX_PAGES + MAX_RECORDS // PAGE_SIZE + 4:
            raise ValueError("METADATA_REQUEST_LIMIT")
        raw = self.transport(url)
        if not isinstance(raw, bytes):
            raise ValueError("METADATA_BYTES_REQUIRED")
        self.total += len(raw)
        if len(raw) > PAGE_BYTES or self.total > TOTAL_BYTES:
            raise ValueError("METADATA_BYTE_LIMIT")
        self.receipts.append({"url": url, "sha256": hashlib.sha256(raw).hexdigest(),
                              "bytes": len(raw), "checkedAt": now()})
        return raw

    def json(self, url):
        def reject_constant(value):
            raise ValueError("NONFINITE_METADATA")
        value = json.loads(self.read(url), parse_constant=reject_constant)
        if not isinstance(value, dict) or value.get("error"):
            raise ValueError("PROVIDER_QUERY_ERROR")
        return value


def _integer(value):
    try:
        result = int(value)
        return result if str(result) == str(value).strip() and result >= 0 else None
    except (ValueError, TypeError):
        return None


def _record(identity, source, publisher, title, url, raw):
    return {"id": identity, "sourceId": source, "publisher": publisher,
            "title": title, "counties": [], "mapYear": None, "digitalYear": None,
            "scale": None, "scaleUnit": None, "metadataUrl": url,
            "rights": {"status": "held" if publisher == "KGS" else "source-terms",
                       "text": "Existing KGS rights hold remains in force." if publisher == "KGS" else
                       "Retain source attribution, accuracy limits and source-specific rights; discovery is not admission.",
                       "url": url},
            "description": "", "geometryRole": "index-point" if publisher == "OSMRE" else "map-extent",
            "bbox": None, "point": None, "crs": None, "spatialAccuracy": None,
            "assets": [], "rawMetadata": raw,
            "discovered": True}


def normalize_nmmr(feature):
    attrs = feature.get("attributes")
    if not isinstance(attrs, dict):
        raise ValueError("NMMR_ATTRIBUTES_REQUIRED")
    lower = {key.lower(): value for key, value in attrs.items()}
    oid, doc = _integer(lower.get("objectid")), _integer(lower.get("documentnumber"))
    if oid is None or doc is None:
        raise ValueError("NMMR_IDENTIFIERS_REQUIRED")
    record = _record(f"nmmr-point-{oid}", "osmre-nmmr", "OSMRE",
                     f"{lower.get('names') or 'Mine map'} — document {doc}",
                     "https://experience.arcgis.com/experience/d84e5b88af674f588645f153e2127910",
                     copy.deepcopy(feature))
    record["mapYear"] = _integer(lower.get("mapyear")) or None
    scale = lower.get("mapscale")
    record["scale"] = str(scale) if scale not in (None, "", 0) else None
    record["scaleUnit"] = "feet-per-inch" if record["scale"] else None
    record["description"] = ("Historical map index point; not a mine footprint. "
        f"Point type: {lower.get('pointdescription') or 'unknown'}; "
        f"location assurance: {lower.get('locationassurance') or 'unknown'}; "
        f"archive status: {lower.get('processstatus') or 'unknown'}.")
    geometry = feature.get("geometry") or {}
    xy = [geometry.get("x"), geometry.get("y")]
    if (all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in xy)
            and -180 <= xy[0] <= 180 and -90 <= xy[1] <= 90):
        record["point"] = xy
        record["pointCoordinateCrs"] = "EPSG:4326"
    scenes = _integer(lower.get("numberscenes")) or 0
    # The provider's scene rule distinguishes one-scene 00 from multi-scene 01..N.
    for scene in ([0] if scenes == 1 else range(1, min(scenes, 100) + 1)):
        prefix = str(doc).zfill(7 if doc >= 1000000 else 6)
        record["assets"].append({"id": f"nmmr-point-{oid}-document-{doc}-scene-{scene:02d}",
            "title": f"Document {doc}, scene {scene if scene else 1}", "format": "JPEG",
            "url": f"https://mmr.osmre.gov/images/{prefix}{scene:02d}_web.jpg",
            "expectedBytes": None, "kind": "download", "availability": "unverified", "checkedAt": None})
    return record


def _query(options):
    return NMMR + "/query?" + urlencode({"f": "json", **options})


def discover_nmmr(budget):
    records, expected, failure = [], None, None
    scope = {"where": "1=1", "geometry": BBOX, "geometryType": "esriGeometryEnvelope",
             "inSR": "4326", "spatialRel": "esriSpatialRelIntersects"}
    try:
        expected = _integer(budget.json(_query({**scope, "returnCountOnly": "true"})).get("count"))
        if expected is None or expected > MAX_RECORDS:
            raise ValueError("NMMR_COUNT_LIMIT_OR_INVALID")
        ids_value = budget.json(_query({**scope, "returnIdsOnly": "true"}))
        ids = ids_value.get("objectIds")
        if (not isinstance(ids, list) or any(type(i) is not int for i in ids)
                or len(ids) != len(set(ids)) or len(ids) != expected
                or ids_value.get("exceededTransferLimit")):
            raise ValueError("NMMR_ID_COUNT_MISMATCH")
        ids = sorted(ids)
        for start in range(0, len(ids), PAGE_SIZE):
            page_ids = ids[start:start + PAGE_SIZE]
            data = budget.json(_query({"objectIds": ",".join(map(str, page_ids)),
                "outFields": "*", "outSR": "4326", "returnGeometry": "true"}))
            features = data.get("features")
            if not isinstance(features, list) or data.get("exceededTransferLimit"):
                raise ValueError("NMMR_PAGE_INCOMPLETE")
            normalized = [normalize_nmmr(feature) for feature in features]
            returned = [int(record["id"].rsplit("-", 1)[1]) for record in normalized]
            if len(returned) != len(set(returned)) or set(returned) != set(page_ids):
                raise ValueError("NMMR_PAGE_ID_MISMATCH")
            records.extend(normalized)
        final_count = _integer(budget.json(_query({**scope, "returnCountOnly": "true"})).get("count"))
        if final_count != expected:
            raise ValueError("NMMR_COUNT_CHANGED")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        failure = f"{type(exc).__name__}: {str(exc)[:220]}"
    return records, expected, failure


def normalize_ngmdb(entry):
    publisher = {"Kansas Geological Survey": "KGS", "U.S. Geological Survey": "USGS",
                 "United States Geological Survey": "USGS"}.get(entry.get("published_by"))
    if publisher is None:
        return None
    identity = _integer(entry.get("id"))
    title = entry.get("title")
    if identity is None or not isinstance(title, str) or not title.strip():
        raise ValueError("NGMDB_PRODUCT_ID_OR_TITLE_INVALID")
    url = f"https://ngmdb.usgs.gov/Prodesc/proddesc_{identity}.htm"
    record = _record("ngmdb-" + str(identity), "ngmdb-" + publisher.lower(), publisher,
                     title, url, copy.deepcopy(entry))
    record["mapYear"] = _integer(entry.get("year")) or None
    scale = entry.get("scale")
    record["scale"] = scale if isinstance(scale, str) and scale else None
    record["scaleUnit"] = "denominator" if record["scale"] and record["scale"].startswith("1:") else None
    record["counties"] = re.findall(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?) County\b", title)
    record["description"] = ", ".join(str(entry[k]) for k in
        ("authors", "year", "title", "published_by", "series", "scale") if entry.get(k))
    return record


def discover_ngmdb(budget, seed):
    """Read the JSON endpoint used by the public search UI, serially, 100 rows/page."""
    records, expected, seen_ids = [], None, set()
    original = next(u for u in seed["sourceUrls"] if u.startswith(NGMDB))
    base = NGMDB_JSON + "?" + urlsplit(original).query
    start = 1
    try:
        for _ in range(MAX_PAGES):
            url = base + (f"&start={start}" if start > 1 else "")
            data = budget.json(url).get("ngmdb_catalog_search")
            if not isinstance(data, dict):
                raise ValueError("NGMDB_RESULT_SHAPE_INVALID")
            criteria, entries = data.get("filter"), data.get("results")
            if not isinstance(criteria, dict) or not isinstance(entries, list):
                raise ValueError("NGMDB_RESULT_SHAPE_INVALID")
            first, last, total = (_integer(criteria.get(key)) for key in ("start", "end", "total_count"))
            if (total is None or first is None or last is None or total > MAX_RECORDS
                    or expected not in (None, total) or criteria.get("State") != "KS"):
                raise ValueError("NGMDB_COUNT_OR_STATE_INVALID")
            expected = total
            if total == 0 and not entries and start == 1:
                return [], 0, None
            # The service reports the requested window end (e.g. 2300), even
            # when its final page ends at total_count (e.g. 2270).
            last = min(last, total)
            if first != start or last < first or len(entries) != last - first + 1:
                raise ValueError("NGMDB_PAGE_COUNT_MISMATCH")
            page_ids = [_integer(entry.get("id")) for entry in entries]
            if (None in page_ids or len(page_ids) != len(set(page_ids))
                    or seen_ids.intersection(page_ids)):
                raise ValueError("NGMDB_DUPLICATE_OR_MISSING_ID")
            # Validate the complete page before accepting any of its records.
            normalized = [normalize_ngmdb(entry) for entry in entries]
            seen_ids.update(page_ids)
            records.extend(record for record in normalized if record is not None)
            if len(seen_ids) == expected:
                return records, expected, None
            start = last + 1
        raise ValueError("NGMDB_PAGE_LIMIT")
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return records, expected, f"{type(exc).__name__}: {str(exc)[:220]}"


def storm_events_record(year, files, checked_at):
    """One Storm Events year: its listed details, fatalities and locations files."""
    record_id = f"publisher-noaa-storm-events-{year}"
    return {"id": record_id, "sourceId": "publisher-noaa-storm-events", "publisher": "NOAA NCEI",
        "title": f"Storm Events {year} · national CSV files including Kansas", "counties": [],
        "mapYear": year, "digitalYear": None, "scale": None, "scaleUnit": None,
        "metadataUrl": STORM_EVENTS,
        "rights": {"status": "public-domain",
                   "text": "U.S. Government work; cite the NOAA NCEI Storm Events Database. Reports are compiled "
                           "by the National Weather Service; magnitudes, damage estimates and locations are "
                           "approximate, and reporting practices changed over time.",
                   "url": STORM_EVENTS},
        "description": f"NOAA NCEI Storm Events Database bulk CSV files for {year}, gzip-compressed. Each file "
                       "covers the whole United States and is not clipped to Kansas: Kansas rows have STATE "
                       "KANSAS in the details file, and the fatalities and locations files join to it by "
                       "EVENT_ID. File names are read from the NCEI directory listing; the newest creation "
                       "date (_c suffix) for each file is offered.",
        "geometryRole": "National files including Kansas; not a Kansas clip",
        "bbox": None, "point": None, "crs": None, "spatialAccuracy": None,
        "assets": [{"id": f"{record_id}-{kind}", "title": name, "format": "GZIP", "url": STORM_EVENTS + name,
                    "expectedBytes": None, "kind": "download", "availability": "verified",
                    "checkedAt": checked_at} for kind, name in sorted(files.items(), key=lambda item: STORM_EVENTS_KINDS.index(item[0]))],
        "rawMetadata": {"listing": STORM_EVENTS, "files": dict(sorted(files.items()))},
        "discovered": True}


def discover_storm_events(budget):
    """Read the NCEI listing once; keep the newest file per kind and year."""
    records, failure = [], None
    try:
        listing = budget.read(STORM_EVENTS).decode("utf-8")
        latest = {}
        for name in sorted(set(re.findall(r'href="([^"]+)"', listing))):
            match = STORM_EVENTS_FILE.fullmatch(name)
            if not match:
                continue
            kind, year, created = match.group(1), int(match.group(2)), match.group(3)
            datetime.strptime(created, "%Y%m%d")
            if not 1950 <= year <= datetime.now(timezone.utc).year or int(created[:4]) < year:
                raise ValueError("STORM_EVENTS_FILE_DATE_INVALID")
            key = (kind, year)
            if key not in latest or created > latest[key][0]:
                latest[key] = (created, name)
        if not latest:
            raise ValueError("STORM_EVENTS_LISTING_EMPTY")
        checked_at = now()[:10]
        for year in sorted({year for _, year in latest}, reverse=True):
            files = {kind: latest[(kind, year)][1] for kind in STORM_EVENTS_KINDS if (kind, year) in latest}
            records.append(storm_events_record(year, files, checked_at))
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        records, failure = [], f"{type(exc).__name__}: {str(exc)[:220]}"
    return records, len(records) if failure is None else None, failure


def discover_catalog(existing=None, *, transport=fetch):
    """Discover serially; source failures retain prior records with honest coverage."""
    seed = load_seed()
    catalog = reconcile_seed(existing) if existing is not None else copy.deepcopy(seed)
    if catalog.get("schema") != "kfm-public-map-catalog/v1":
        raise ValueError("CATALOG_SCHEMA_INVALID")
    catalog.setdefault("sourceUrls", seed["sourceUrls"])
    budget = Budget(transport)
    curated_by_id = {record["id"]: record for record in seed["records"]}
    nmmr_records, nmmr_count, nmmr_error = discover_nmmr(budget)
    ngmdb_records, ngmdb_count, ngmdb_error = discover_ngmdb(budget, seed)
    storm_records, storm_count, storm_error = discover_storm_events(budget)
    catalog["generatedAt"] = now()
    sources = [("osmre-nmmr", nmmr_records, nmmr_count, nmmr_error),
               ("ngmdb-usgs", [r for r in ngmdb_records if r["publisher"] == "USGS"], ngmdb_count, ngmdb_error),
               ("ngmdb-kgs", [r for r in ngmdb_records if r["publisher"] == "KGS"], ngmdb_count, ngmdb_error),
               ("publisher-noaa-storm-events", storm_records, storm_count, storm_error)]
    discovered_sources = {row[0] for row in sources}
    coverage = []
    for source, records, count, error in sources:
        prior = [r for r in catalog["records"] if r["sourceId"] == source]
        retained = [r for r in prior if error or not r.get("discovered")]
        by_id = {r["id"]: r for r in retained}
        for record in records:
            previous = by_id.get(record["id"])
            if previous and not record["assets"]:
                record["assets"] = previous["assets"]
            curated = curated_by_id.get(record["id"])
            if curated:
                assets = {asset["id"]: asset for asset in record["assets"]}
                assets.update({asset["id"]: copy.deepcopy(asset) for asset in curated["assets"]})
                record["assets"] = list(assets.values())
                if curated["rights"]["status"] == "held":
                    record["rights"] = copy.deepcopy(curated["rights"])
            by_id[record["id"]] = record
        catalog["records"] = [r for r in catalog["records"] if r["sourceId"] != source] + list(by_id.values())
        discovered = sum(bool(r.get("discovered")) for r in by_id.values())
        state = ("partial" if discovered else "unavailable") if error else "complete"
        if source == "publisher-noaa-storm-events":
            reason = ("Years listed in the NCEI Storm Events CSV directory; national files including Kansas, not "
                      "clipped to the state. File sizes are not captured by this catalog; choose a download maximum. ")
            reason += error or f"Listed {len(records)} years."
        else:
            reason = ("Kansas bounding rectangle of index points; not exact state membership, "
                      "mine footprints or exhaustive archival coverage. " if source == "osmre-nmmr" else
                      "Explicit publisher subset of the full Kansas search; URL publisher filter is not trusted. ")
            reason += error or (f"Reconciled {len(records)} point IDs." if source == "osmre-nmmr" else
                               f"Reconciled {count} total search IDs; retained {len(records)} matching publications.")
        coverage.append({"sourceId": source, "title": next(c["title"] for c in seed["coverage"] if c["sourceId"] == source),
            "state": state, "recordCount": len(by_id), "discoveredCount": discovered,
            "seedReferenceCount": len(by_id) - discovered,
            "expectedCount": count if source in {"osmre-nmmr", "publisher-noaa-storm-events"} else len(records) if not error else None,
            "reason": reason, "checkedAt": catalog["generatedAt"]})
    coverage.extend(copy.deepcopy(row) for row in catalog["coverage"] if row["sourceId"] not in discovered_sources)
    catalog["coverage"] = coverage
    catalog["discovery"] = {"metadataBytes": budget.total, "requests": budget.requests,
                            "mapBytesDownloaded": 0, "kansasBounds": BBOX,
                            "ngmdbTotalCount": ngmdb_count,
                            "ngmdbExcludedPublisherCount": ngmdb_count - len(ngmdb_records)
                            if ngmdb_error is None and ngmdb_count is not None else None,
                            "receipts": budget.receipts}
    return catalog


def build_review_bundle(snapshot_bytes):
    """Build deterministic metadata-only JSONL and receipt bytes from a snapshot.

    This is an inspection index, not a governed catalog projection or admission.
    It retains each discovered provider record without repeating UI defaults.
    """
    catalog = json.loads(snapshot_bytes)
    if catalog.get("schema") != "kfm-public-map-catalog/v1":
        raise ValueError("CATALOG_SCHEMA_INVALID")
    date = catalog["generatedAt"][:10].replace("-", "")
    if not re.fullmatch(r"\d{8}", date):
        raise ValueError("CATALOG_DATE_INVALID")
    records = catalog["records"]
    discovered = [record for record in records if record.get("discovered")]
    if len({record["id"] for record in records}) != len(records):
        raise ValueError("CATALOG_DUPLICATE_RECORD")
    for coverage in catalog["coverage"]:
        source = [record for record in records if record["sourceId"] == coverage["sourceId"]]
        found = sum(bool(record.get("discovered")) for record in source)
        if (coverage["recordCount"] != len(source) or coverage.get("discoveredCount") != found
                or coverage.get("seedReferenceCount") != len(source) - found
                or (coverage["state"] == "complete" and coverage["expectedCount"] != found)):
            raise ValueError("CATALOG_COVERAGE_MISMATCH")
    index_name = f"public-map-metadata-{date}.jsonl"
    rows = [{"id": record["id"], "sourceId": record["sourceId"],
             "metadataUrl": record["metadataUrl"], "rightsStatus": record["rights"]["status"],
             "rawMetadata": record["rawMetadata"]}
            for record in sorted(discovered, key=lambda record: (record["sourceId"], record["id"]))]
    index = b"".join((json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                                allow_nan=False) + "\n").encode("utf-8") for row in rows)
    receipt = {"schema": "kfm-public-map-discovery-review/v1", "generatedAt": catalog["generatedAt"],
        "lifecycle": "candidate-metadata-only", "sourceUrls": catalog["sourceUrls"],
        "coverage": catalog["coverage"], "discovery": catalog["discovery"],
        "index": {"file": index_name, "recordCount": len(rows), "bytes": len(index),
                  "sha256": hashlib.sha256(index).hexdigest()},
        "snapshot": {"schema": catalog["schema"], "recordCount": len(records),
                     "bytes": len(snapshot_bytes), "sha256": hashlib.sha256(snapshot_bytes).hexdigest()},
        "seedReferenceIds": sorted(record["id"] for record in records if not record.get("discovered")),
        "rights": {"kgsReview": "held", "admission": "not-granted", "mapOriginalsDownloaded": 0},
        "scope": "Kansas search results explicitly filtered to USGS and KGS publishers. NMMR coverage and failures are separate. "
                 "Online/GIS metadata flags do not verify files, download rights, georeferencing, or local availability."}
    if "seedAugmentation" in catalog:
        receipt["seedAugmentation"] = catalog["seedAugmentation"]
    receipt_bytes = (json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    return {index_name: index, f"discovery-{date}.json": receipt_bytes}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Snapshot path outside the repository")
    args = parser.parse_args(argv)
    path = args.output.resolve()
    if path == ROOT or ROOT in path.parents:
        parser.error("Live metadata snapshots must be stored outside the Git tree")
    if path.exists():
        parser.error("Output already exists; preserve prior snapshots")
    result = discover_catalog()
    with path.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"output": str(path), "coverage": result["coverage"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
