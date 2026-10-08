"""Behavioral contracts for bounded public map metadata discovery."""
import json
import hashlib
from urllib.parse import parse_qs, urlsplit

import pytest

from tools.local_data import public_map_catalog as catalog


def encoded(value):
    return json.dumps(value).encode()


def point(oid, document=42, scenes=1):
    return {"attributes": {"objectid": oid, "documentnumber": document,
            "names": "Historic mine", "mapyear": 1924, "mapscale": 200,
            "numberscenes": scenes, "processstatus": "LEGACY",
            "pointdescription": "POPULATED PLACE", "locationassurance": "LOW"},
            "geometry": {"x": -97, "y": 38}}


def page(first, last, total, entries, next_start=None):
    return encoded({"ngmdb_catalog_search": {"filter": {"start": str(first), "end": str(last),
        "total_count": str(total), "State": "KS", "publisher_list": "usgs"},
        "results": [{"id": pid, "title": title, "published_by": publisher,
                     "year": 1947, "scale": "1:50,000", "formats": "PDF", "online": "True"}
                    for pid, title, publisher in entries]}})


def test_nmmr_id_pages_keep_mine_instances_and_shared_scene_relation(monkeypatch):
    monkeypatch.setattr(catalog, "PAGE_SIZE", 1)
    calls = []
    def transport(url):
        query = parse_qs(urlsplit(url).query)
        calls.append(query)
        if "returnCountOnly" in query:
            return encoded({"count": 2})
        if "returnIdsOnly" in query:
            return encoded({"objectIds": [2, 1]})
        return encoded({"features": [point(int(query["objectIds"][0]))]})
    records, expected, failure = catalog.discover_nmmr(catalog.Budget(transport))
    assert failure is None and expected == 2
    assert [r["id"] for r in records] == ["nmmr-point-1", "nmmr-point-2"]
    assert records[0]["assets"][0]["id"] != records[1]["assets"][0]["id"]
    assert records[0]["assets"][0]["url"] == records[1]["assets"][0]["url"]
    assert records[0]["assets"][0]["url"].endswith("00004200_web.jpg")
    assert records[0]["scaleUnit"] == "feet-per-inch"
    assert records[0]["rawMetadata"]["attributes"]["processstatus"] == "LEGACY"
    assert "outSR" in calls[2] and calls[2]["outSR"] == ["4326"]


def test_nmmr_multi_scene_and_missing_coordinates_do_not_invent_geometry():
    feature = point(4, scenes=3)
    feature["geometry"] = {"x": -11000000, "y": 4600000}
    record = catalog.normalize_nmmr(feature)
    assert record["point"] is None
    assert [a["id"] for a in record["assets"]] == [
        "nmmr-point-4-document-42-scene-01", "nmmr-point-4-document-42-scene-02", "nmmr-point-4-document-42-scene-03"]
    assert all(a["availability"] == "unverified" for a in record["assets"])


def test_nmmr_duplicate_page_id_is_partial_not_complete(monkeypatch):
    monkeypatch.setattr(catalog, "PAGE_SIZE", 1)
    def transport(url):
        query = parse_qs(urlsplit(url).query)
        if "returnCountOnly" in query:
            return encoded({"count": 2})
        if "returnIdsOnly" in query:
            return encoded({"objectIds": [1, 2]})
        return encoded({"features": [point(1)]})
    records, count, failure = catalog.discover_nmmr(catalog.Budget(transport))
    assert len(records) == 1 and count == 2
    assert "NMMR_PAGE_ID_MISMATCH" in failure


def test_ngmdb_paginates_any_publisher_and_filters_by_explicit_publisher():
    def transport(url):
        query = parse_qs(urlsplit(url).query)
        if "start" not in query:
            return page(1, 2, 3, [(1, "Bourbon County geology", "Kansas Geological Survey"),
                                  (2, "Mining maps", "Office of Surface Mining")], 3)
        return page(3, 3, 3, [(3, "Regional geology", "U.S. Geological Survey")])
    records, expected, failure = catalog.discover_ngmdb(catalog.Budget(transport), catalog.load_seed())
    assert failure is None and expected == 3
    assert [r["publisher"] for r in records] == ["KGS", "USGS"]
    assert records[0]["counties"] == ["Bourbon"]
    assert records[0]["rights"]["status"] == "held"
    assert records[0]["mapYear"] == 1947 and records[0]["digitalYear"] is None
    assert records[0]["scale"] == "1:50,000"
    assert records[0]["assets"] == []  # A download icon is not a verified asset URL.


def test_ngmdb_failed_next_page_never_claims_complete():
    def transport(url):
        if "start=" in url:
            raise OSError("HTTP 503")
        return page(1, 1, 2, [(1, "Kansas geology", "U.S. Geological Survey")])
    records, expected, failure = catalog.discover_ngmdb(catalog.Budget(transport), catalog.load_seed())
    assert len(records) == 1 and expected == 2
    assert "HTTP 503" in failure


def test_ngmdb_last_page_end_can_describe_unfilled_requested_window():
    raw = page(1, 100, 2, [(1, "Map one", "U.S. Geological Survey"),
                          (2, "Map two", "Kansas Geological Survey")])
    records, expected, failure = catalog.discover_ngmdb(catalog.Budget(lambda _: raw), catalog.load_seed())
    assert failure is None and expected == len(records) == 2


def test_source_failure_preserves_existing_records_and_has_unavailable_coverage():
    def fail(_):
        raise OSError("certificate verify failed")
    seed = catalog.load_seed()
    result = catalog.discover_catalog(seed, transport=fail)
    assert seed == catalog.load_seed()
    assert {r["id"] for r in result["records"]} == {r["id"] for r in seed["records"]}
    assert all(c["state"] == "unavailable" for c in result["coverage"])
    assert all(c["expectedCount"] is None for c in result["coverage"])
    assert all(c["recordCount"] == c["discoveredCount"] + c["seedReferenceCount"]
               for c in result["coverage"])
    assert result["discovery"]["mapBytesDownloaded"] == 0


def test_failed_refresh_preserves_previous_discovery_but_marks_partial():
    existing = catalog.load_seed()
    existing["records"].append(catalog.normalize_nmmr(point(1)))
    def fail(_):
        raise OSError("offline")
    result = catalog.discover_catalog(existing, transport=fail)
    assert result["coverage"][0]["state"] == "partial"
    assert any(r["id"] == "nmmr-point-1" for r in result["records"])


def test_complete_coverage_counts_discovered_rows_separately_from_seed_references():
    def transport(url):
        query = parse_qs(urlsplit(url).query)
        if url.startswith(catalog.NMMR):
            return encoded({"objectIds": []} if "returnIdsOnly" in query else {"count": 0})
        return page(1, 100, 2, [(12, "Regional geology", "U.S. Geological Survey"),
                               (13, "County geology", "Kansas Geological Survey")])
    result = catalog.discover_catalog(transport=transport)
    for coverage in result["coverage"]:
        assert coverage["state"] == "complete"
        assert coverage["discoveredCount"] == coverage["expectedCount"]
        assert coverage["recordCount"] == sum(r["sourceId"] == coverage["sourceId"] for r in result["records"])
    assert result["discovery"]["ngmdbTotalCount"] == 2
    assert result["discovery"]["ngmdbExcludedPublisherCount"] == 0
    assert len(result["discovery"]["receipts"]) == 4


def test_review_bundle_preserves_raw_metadata_and_binds_exact_bytes():
    def transport(url):
        query = parse_qs(urlsplit(url).query)
        if url.startswith(catalog.NMMR):
            return encoded({"objectIds": []} if "returnIdsOnly" in query else {"count": 0})
        return page(1, 100, 1, [(12, "County geology", "Kansas Geological Survey")])
    snapshot = encoded(catalog.discover_catalog(transport=transport))
    bundle = catalog.build_review_bundle(snapshot)
    assert bundle == catalog.build_review_bundle(snapshot)
    index_name = next(name for name in bundle if name.endswith(".jsonl"))
    receipt = json.loads(bundle[next(name for name in bundle if name.endswith(".json"))])
    row = json.loads(bundle[index_name])
    assert row["rawMetadata"]["published_by"] == "Kansas Geological Survey"
    assert row["rightsStatus"] == "held"
    assert receipt["index"]["sha256"] == hashlib.sha256(bundle[index_name]).hexdigest()
    assert receipt["snapshot"]["sha256"] == hashlib.sha256(snapshot).hexdigest()
    assert receipt["sourceUrls"] == catalog.load_seed()["sourceUrls"]
    invalid = json.loads(snapshot)
    invalid["coverage"][0]["recordCount"] += 1
    with pytest.raises(ValueError, match="CATALOG_COVERAGE_MISMATCH"):
        catalog.build_review_bundle(encoded(invalid))


def test_reconcile_seed_adds_new_assets_without_replacing_discovered_records(monkeypatch):
    seed = catalog.load_seed()
    existing = json.loads(json.dumps(seed))
    discovered = catalog.normalize_ngmdb({"id": 959, "title": "Provider title",
        "published_by": "U.S. Geological Survey", "year": 1954, "scale": "1:62,500"})
    existing["records"] = [r for r in existing["records"] if r["id"] != "ngmdb-959"] + [discovered]
    existing["discovery"] = {"receipts": [{"sha256": "prior-response"}]}
    checked = "2026-01-01T00:00:00Z"
    existing["coverage"][1].update(state="complete", checkedAt=checked, expectedCount=1)
    publication = next(r for r in seed["records"] if r["id"] == "ngmdb-959")
    publication["assets"] = [{"id": "new-verified-asset", "url": "https://pubs.usgs.gov/gq/map.zip"}]
    limon = next(r for r in seed["records"] if r["id"] == "usgs-limon-p9djg0o3")
    limon["description"] = "Updated verified archive reference"
    monkeypatch.setattr(catalog, "load_seed", lambda: json.loads(json.dumps(seed)))
    merged = catalog.reconcile_seed(existing)
    current = next(r for r in merged["records"] if r["id"] == "ngmdb-959")
    assert current["title"] == "Provider title" and current["discovered"]
    assert current["rawMetadata"] == discovered["rawMetadata"]
    assert current["assets"] == publication["assets"]
    assert merged["generatedAt"] == existing["generatedAt"]
    assert merged["discovery"] == existing["discovery"]
    assert merged["coverage"][1]["checkedAt"] == checked
    assert merged["coverage"][1]["discoveredCount"] == merged["coverage"][1]["expectedCount"] == 1
    assert merged["seedAugmentation"]["discoveryRefreshed"] is False
    assert existing["records"][-1]["assets"] == []
    assert catalog.reconcile_seed(merged) == merged  # No new timestamp when nothing changes.


def test_successful_refresh_keeps_curated_assets_on_discovered_record(monkeypatch):
    seed = catalog.load_seed()
    curated = next(record for record in seed["records"] if record["id"] == "ngmdb-959")
    curated["assets"] = [{"id": "curated-archive", "url": "https://pubs.usgs.gov/example.zip"}]
    existing = json.loads(json.dumps(seed))
    old = catalog.normalize_ngmdb({"id": 959, "title": "Old provider title",
        "published_by": "U.S. Geological Survey", "year": 1954})
    existing["records"] = [record for record in existing["records"] if record["id"] != old["id"]] + [old]
    monkeypatch.setattr(catalog, "load_seed", lambda: json.loads(json.dumps(seed)))
    def transport(url):
        if url.startswith(catalog.NMMR):
            return encoded({"objectIds": []} if "returnIdsOnly" in url else {"count": 0})
        return page(1, 100, 1, [(959, "New provider title", "U.S. Geological Survey")])
    refreshed = catalog.discover_catalog(existing, transport=transport)
    record = next(record for record in refreshed["records"] if record["id"] == old["id"])
    assert record["discovered"] and record["title"] == "New provider title"
    assert record["rawMetadata"]["title"] == "New provider title"
    assert record["assets"] == curated["assets"]
    assert refreshed["coverage"][1]["expectedCount"] == 1


@pytest.mark.parametrize("url", [
    "http://ngmdb.usgs.gov/ngm-bin/ngm_search_dbi.pl?State=KS",
    "https://attacker.example/ngm-bin/ngm_search_dbi.pl?State=KS",
    "https://ngmdb.usgs.gov/other?State=KS",
    catalog.NGMDB + "?State=KS&State=CO",
    catalog.NGMDB + "?State=CO",
])
def test_untrusted_pagination_urls_are_rejected(url):
    with pytest.raises(ValueError):
        catalog.validate_metadata_url(url)


def test_seed_keeps_known_sizes_and_service_request_boundaries():
    seed = catalog.load_seed()
    assets = {a["id"]: a for r in seed["records"] for a in r["assets"]}
    assert assets["kgs-m118-pdf"]["expectedBytes"] == 37386469
    assert assets["kgs-m97-jpeg"]["expectedBytes"] == 66506223
    assert assets["kgs-m118-gems"]["kind"] == "service"
    assert assets["osmre-nmmr-request"]["availability"] == "request-only"
