"""Deterministic synthetic tests; no provider access, rights, or sensitivity claim."""
from dataclasses import FrozenInstanceError, replace
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/gbif/occurrence_api.py"
SPEC = importlib.util.spec_from_file_location("kfm_gbif_occurrence_tested", PATH)
occ = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = occ
SPEC.loader.exec_module(occ)
NOW = "2026-09-26T12:00:00Z"
DATASET = "00000000-0000-4000-8000-000000000001"
CC_BY = "http://creativecommons.org/licenses/by/4.0/legalcode"


def record(key=1, **overrides):
    # Synthetic values only: no real occurrence, taxon, or location.
    base = {"key": key, "datasetKey": DATASET, "license": CC_BY,
            "basisOfRecord": "HUMAN_OBSERVATION", "occurrenceStatus": "PRESENT",
            "taxonKey": 1, "scientificName": "Synthetica exempla",
            "eventDate": "2020-05-01", "decimalLatitude": 38.5,
            "decimalLongitude": -98.5, "coordinateUncertaintyInMeters": 30,
            "unknown_field": {"retained": True}}
    base.update(overrides)
    return {k: v for k, v in base.items() if v is not ...}


def page_body(results, *, offset=0, limit=2, count=None, end=True):
    return json.dumps({"offset": offset, "limit": limit, "endOfRecords": end,
                       "count": len(results) if count is None else count,
                       "results": results}).encode()


def url(offset=0, limit=2, **params):
    query = occ.OccurrenceQuery(**params)
    return occ.plan_pages(query, max_records=offset + limit, page_size=limit)[-1].url


def parse(results=None, *, offset=0, limit=2, **kwargs):
    body = page_body([record()] if results is None else results,
                     offset=offset, limit=limit, **kwargs)
    return occ.parse_page(body, status=200, source_url=url(offset, limit), retrieved_at=NOW)


class PlanTests(unittest.TestCase):
    def test_plan_is_bounded_and_kansas_scoped(self):
        plans = occ.plan_pages(occ.OccurrenceQuery(taxon_key=7, year="1900,2020"),
                               max_records=650)
        self.assertEqual([(p.offset, p.limit) for p in plans], [(0, 300), (300, 300), (600, 50)])
        params = parse_qs(urlsplit(plans[1].url).query)
        self.assertEqual(params["stateProvince"], ["Kansas"])
        self.assertEqual(params["country"], ["US"])
        self.assertEqual(params["offset"], ["300"])
        self.assertTrue(all(p.url.startswith("https://api.gbif.org/v1/occurrence/search?")
                            for p in plans))

    def test_plan_rejects_unbounded_or_invalid_filters(self):
        for kwargs, plan_kwargs in (
                ({}, {"max_records": 100_001}), ({}, {"page_size": 301}),
                ({"year": "2020,1900"}, {}), ({"basis_of_record": "RUMOR"}, {}),
                ({"country": "usa"}, {}), ({"taxon_key": -1}, {}),
                ({"has_coordinate": 1}, {})):
            with self.subTest(kwargs=kwargs, plan=plan_kwargs), \
                    self.assertRaises(occ.OccurrenceInputError):
                occ.plan_pages(occ.OccurrenceQuery(**kwargs), **plan_kwargs)

    def test_source_url_allowlist(self):
        good = url()
        for bad in (good.replace("https://", "http://"), good.replace("api.gbif.org", "example.org"),
                    good + "&datasetKey=x", good.replace("limit=2", "limit=301"), good + "#f",
                    "https://api.gbif.org/v1/occurrence/download/request?limit=1&offset=0"):
            with self.subTest(bad=bad), self.assertRaises(occ.OccurrenceInputError):
                occ.parse_page(page_body([]), status=200, source_url=bad, retrieved_at=NOW)


class ParseTests(unittest.TestCase):
    def test_clean_record_is_raw_candidate_but_never_admitted(self):
        (candidate,) = parse().records
        self.assertEqual(candidate.route, "RAW_CANDIDATE")
        self.assertEqual(candidate.license_id, "CC_BY_4_0")
        self.assertEqual(candidate.sensitivity, "NOT_EVALUATED")
        self.assertEqual(candidate.admission, "NOT_ADMITTED")
        self.assertIn('"unknown_field":{"retained":true}', candidate.raw_record_json)
        self.assertTrue(candidate.record_sha256.startswith("sha256:"))
        with self.assertRaises(FrozenInstanceError):
            candidate.route = "PUBLISHED"

    def test_coordinates_carried_exactly(self):
        (candidate,) = parse([record(decimalLatitude=38.123456789,
                                     decimalLongitude=-98.987654321)]).records
        self.assertEqual((candidate.latitude, candidate.longitude), (38.123456789, -98.987654321))

    def test_unresolved_rights_or_precision_quarantine(self):
        cases = {
            "LICENSE_UNRESOLVED": record(license="custom"),
            "DATASET_IDENTITY_MISSING": record(datasetKey=...),
            "INFORMATION_WITHHELD": record(informationWithheld="coordinates withheld"),
            "DATA_GENERALIZED": record(dataGeneralizations="rounded to 0.1 deg"),
            "COORDINATES_ABSENT": record(decimalLatitude=..., decimalLongitude=...),
            "BASIS_OF_RECORD_UNKNOWN": record(basisOfRecord="HEARSAY"),
            "OCCURRENCE_STATUS_UNKNOWN": record(occurrenceStatus="MAYBE"),
        }
        for reason, item in cases.items():
            with self.subTest(reason=reason):
                (candidate,) = parse([item]).records
                self.assertEqual(candidate.route, "QUARANTINE_CANDIDATE")
                self.assertIn(reason, candidate.reasons)

    def test_flags_that_do_not_quarantine(self):
        (nc,) = parse([record(license=CC_BY.replace("by/", "by-nc/"))]).records
        self.assertEqual((nc.route, nc.reasons), ("RAW_CANDIDATE", ("NONCOMMERCIAL_TERMS",)))
        (absent,) = parse([record(occurrenceStatus="ABSENT")]).records
        self.assertEqual(absent.reasons, ("ABSENCE_ASSERTION",))
        (https,) = parse([record(license=CC_BY.replace("http://", "https://"))]).records
        self.assertEqual(https.license_id, "CC_BY_4_0")

    def test_malformed_pages_rejected_whole(self):
        cases = {
            "duplicate key": page_body([record(1), record(1)]),
            "window mismatch": page_body([record()], offset=2),
            "too many rows": page_body([record(1), record(2), record(3)]),
            "short non-terminal page": page_body([record()], end=False, count=5),
            "half coordinate": page_body([record(decimalLatitude=...)]),
            "bad latitude": page_body([record(decimalLatitude=91)]),
            "negative uncertainty": page_body([record(coordinateUncertaintyInMeters=-1)]),
            "nan": b'{"offset":0,"limit":2,"endOfRecords":true,"count":0,"results":[NaN]}',
            "duplicate json key": b'{"offset":0,"offset":0,"limit":2,"results":[]}',
            "not json": b"<html>",
        }
        for name, body in cases.items():
            with self.subTest(name=name), self.assertRaises(occ.OccurrenceInputError):
                occ.parse_page(body, status=200, source_url=url(), retrieved_at=NOW)
        with self.assertRaises(occ.OccurrenceInputError):
            occ.parse_page(page_body([]), status=500, source_url=url(), retrieved_at=NOW)
        with self.assertRaises(occ.OccurrenceInputError):
            occ.parse_page(page_body([]), status=200, source_url=url(), retrieved_at="2026-09-26")

    def test_errors_do_not_echo_payload(self):
        secret = "SENSITIVE-LOCATION-TEXT"
        with self.assertRaises(occ.OccurrenceInputError) as caught:
            occ.parse_page(page_body([record(key=secret)]), status=200,
                           source_url=url(), retrieved_at=NOW)
        self.assertNotIn(secret, str(caught.exception))


class ReconcileTests(unittest.TestCase):
    def pages(self, total=5, limit=2, count=None):
        pages, offset = [], 0
        while offset < total:
            rows = [record(k) for k in range(offset, min(offset + limit, total))]
            end = offset + limit >= total
            body = page_body(rows, offset=offset, limit=limit, end=end,
                             count=total if count is None else count)
            pages.append(occ.parse_page(body, status=200, source_url=url(offset, limit),
                                        retrieved_at=NOW))
            offset += limit
        return pages

    def test_complete_capture(self):
        capture = occ.reconcile(list(reversed(self.pages())))
        self.assertEqual(capture.outcome, "CAPTURE_CANDIDATE")
        self.assertEqual([r.gbif_key for r in capture.records], [0, 1, 2, 3, 4])
        self.assertEqual(capture.coverage, "NOT_ESTABLISHED")

    def test_gap_and_truncation_are_incomplete(self):
        pages = self.pages()
        gap = occ.reconcile([pages[0], pages[2]])
        self.assertEqual(gap.outcome, "INCOMPLETE_CAPTURE")
        self.assertIn("PAGE_GAP_OR_OVERLAP", gap.reasons)
        truncated = occ.reconcile(pages[:2])
        self.assertIn("END_OF_RECORDS_NOT_REACHED", truncated.reasons)
        drift = occ.reconcile([pages[0], pages[1], replace(pages[2], count=6)])
        self.assertIn("COUNT_DRIFT", drift.reasons)

    def test_paging_ceiling_holds(self):
        (page,) = self.pages(total=1, count=100_001)[:1]
        page = replace(page, end_of_records=True)
        capture = occ.reconcile([page])
        self.assertEqual(capture.outcome, "HOLD")
        self.assertEqual(capture.reasons[0], "PAGING_CEILING_USE_ASYNC_DOWNLOAD")

    def test_mixed_queries_rejected(self):
        other = occ.parse_page(page_body([record(9)]), status=200,
                               source_url=url(taxon_key=5), retrieved_at=NOW)
        with self.assertRaises(occ.OccurrenceInputError):
            occ.reconcile([self.pages(total=1)[0], other])
        with self.assertRaises(occ.OccurrenceInputError):
            occ.reconcile([])


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            occ.plan_pages(occ.OccurrenceQuery())
            occ.reconcile([parse()])


if __name__ == "__main__":
    unittest.main()
