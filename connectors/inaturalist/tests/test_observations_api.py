"""Deterministic synthetic tests; no provider access, rights, or sensitivity claim."""
from dataclasses import FrozenInstanceError
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/inaturalist/observations_api.py"
SPEC = importlib.util.spec_from_file_location("kfm_inat_observations_tested", PATH)
obs = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = obs
SPEC.loader.exec_module(obs)
NOW = "2026-09-26T12:00:00Z"
QUERY = obs.ObservationQuery()


def record(identifier=1, **overrides):
    # Synthetic values only: no real observation, observer, taxon, or location.
    base = {"id": identifier, "quality_grade": "research", "license_code": "cc-by",
            "geoprivacy": None, "taxon_geoprivacy": "open", "obscured": False,
            "geojson": {"type": "Point", "coordinates": [-98.5, 38.5]},
            "positional_accuracy": 10, "observed_on": "2020-05-01",
            "updated_at": "2020-05-02T00:00:00Z", "captive": False,
            "taxon": {"id": 1, "name": "Synthetica exempla", "rank": "species"},
            "user": {"id": 7, "login": "synthetic_observer", "name": "Private Name",
                     "icon_url": "https://example.invalid/icon.png"},
            "unknown_field": {"retained": True}}
    base.update(overrides)
    return {k: v for k, v in base.items() if v is not ...}


def body(results, *, per_page=2, total=None):
    return json.dumps({"total_results": len(results) if total is None else total,
                       "page": 1, "per_page": per_page, "results": results}).encode()


def parse(results=None, *, id_above=0, per_page=2, total=None, query=QUERY):
    url = obs.page_url(query, id_above=id_above, per_page=per_page)
    return obs.parse_page(body([record()] if results is None else results,
                               per_page=per_page, total=total),
                          status=200, source_url=url, retrieved_at=NOW)


class QueryTests(unittest.TestCase):
    def test_cursor_url_is_bounded_and_ordered(self):
        params = parse_qs(urlsplit(obs.page_url(QUERY, id_above=41)).query)
        self.assertEqual(params["order_by"], ["id"])
        self.assertEqual(params["order"], ["asc"])
        self.assertEqual(params["id_above"], ["41"])
        self.assertEqual(params["per_page"], ["200"])
        self.assertEqual(params["swlng"], ["-102.1"])

    def test_invalid_scopes_rejected(self):
        for kwargs, url_kwargs in (
                ({"bounds": None}, {}), ({"place_id": 5}, {}),
                ({"bounds": (1, 1, 0, 2)}, {}), ({"quality_grade": "gold"}, {}),
                ({"observed_from": "2020-5-1"}, {}),
                ({"observed_from": "2021-01-01", "observed_to": "2020-01-01"}, {}),
                ({}, {"per_page": 201}), ({}, {"id_above": -1})):
            with self.subTest(kwargs=kwargs, url=url_kwargs), \
                    self.assertRaises(obs.ObservationInputError):
                obs.page_url(obs.ObservationQuery(**kwargs), **url_kwargs)
        place = obs.ObservationQuery(bounds=None, place_id=5)
        self.assertIn("place_id=5", obs.page_url(place))

    def test_source_url_allowlist(self):
        good = obs.page_url(QUERY, per_page=2)
        for bad in (good.replace("https://", "http://"),
                    good.replace("api.inaturalist.org", "example.org"),
                    good.replace("order=asc", "order=desc"), good + "&user_id=1",
                    good.replace("per_page=2", "per_page=500"), good + "#x"):
            with self.subTest(bad=bad), self.assertRaises(obs.ObservationInputError):
                obs.parse_page(body([]), status=200, source_url=bad, retrieved_at=NOW)


class ClassifyTests(unittest.TestCase):
    def test_open_research_record_is_raw_candidate(self):
        (candidate,) = parse().records
        self.assertEqual(candidate.route, "RAW_CANDIDATE")
        self.assertEqual((candidate.geoprivacy_status, candidate.precision_class),
                         ("open", "source_point"))
        self.assertEqual((candidate.latitude, candidate.longitude), (38.5, -98.5))
        self.assertEqual(candidate.rights_holder, "synthetic_observer")
        self.assertEqual((candidate.sensitivity, candidate.admission),
                         ("NOT_EVALUATED", "NOT_ADMITTED"))
        with self.assertRaises(FrozenInstanceError):
            candidate.route = "PUBLISHED"

    def test_user_profile_minimized(self):
        (candidate,) = parse().records
        self.assertNotIn("Private Name", candidate.raw_record_json)
        self.assertNotIn("icon_url", candidate.raw_record_json)
        self.assertIn('"user":{"id":7,"login":"synthetic_observer"}', candidate.raw_record_json)
        self.assertIn('"unknown_field":{"retained":true}', candidate.raw_record_json)

    def test_nested_user_profiles_minimized(self):
        profile = {"id": 9, "login": "synthetic_identifier", "name": "Nested Private Name",
                   "orcid": "0000-0000-0000-0000"}
        (candidate,) = parse([record(
            identifications=[{"id": 1, "user": profile, "taxon": {"id": 1}}],
            comments=[{"id": 2, "body": "synthetic", "user": dict(profile, id=10)}],
            project_observations=[{"project": {"user": dict(profile, id=11)}}])]).records
        self.assertNotIn("Nested Private Name", candidate.raw_record_json)
        self.assertNotIn("orcid", candidate.raw_record_json)
        self.assertEqual(candidate.raw_record_json.count('"login":"synthetic_identifier"'), 3)
        self.assertIn('"body":"synthetic"', candidate.raw_record_json)

    def test_deep_nesting_is_a_bounded_error(self):
        nested = {}
        for _ in range(900):
            nested = {"child": nested}
        with self.assertRaises(obs.ObservationInputError) as caught:
            parse([record(extra=nested)])
        self.assertEqual(str(caught.exception), "RECORD_DEPTH")

    def test_most_restrictive_geoprivacy_governs(self):
        cases = [({"geoprivacy": "obscured"}, "obscured", "obscured_randomized"),
                 ({"taxon_geoprivacy": "obscured"}, "obscured", "obscured_randomized"),
                 ({"obscured": True}, "obscured", "obscured_randomized"),
                 ({"geoprivacy": "private", "geojson": None}, "private", "withheld"),
                 ({"geoprivacy": "open", "taxon_geoprivacy": "private"}, "private",
                  "private_supplied")]
        for overrides, status, precision in cases:
            with self.subTest(overrides=overrides):
                (candidate,) = parse([record(**overrides)]).records
                self.assertEqual((candidate.geoprivacy_status, candidate.precision_class),
                                 (status, precision))
                self.assertEqual(candidate.route, "QUARANTINE_CANDIDATE")

    def test_obscured_coordinates_carried_unmodified(self):
        (candidate,) = parse([record(geoprivacy="obscured", geojson={
            "type": "Point", "coordinates": [-98.123456, 38.654321]})]).records
        self.assertEqual((candidate.latitude, candidate.longitude), (38.654321, -98.123456))

    def test_rights_routing(self):
        for code in (None, "all-rights-reserved", "custom"):
            with self.subTest(code=code):
                (candidate,) = parse([record(license_code=code)]).records
                self.assertEqual(candidate.route, "QUARANTINE_CANDIDATE")
                self.assertIn("LICENSE_UNRESOLVED", candidate.reasons)
        (nc_sa,) = parse([record(license_code="CC-BY-NC-SA")]).records
        self.assertEqual(nc_sa.route, "RAW_CANDIDATE")
        self.assertEqual(nc_sa.reasons, ("NONCOMMERCIAL_TERMS", "SHAREALIKE_TERMS"))
        (no_user,) = parse([record(user=...)]).records
        self.assertIn("ATTRIBUTION_MISSING", no_user.reasons)
        self.assertEqual(no_user.route, "QUARANTINE_CANDIDATE")

    def test_flags_and_taxon(self):
        (casual,) = parse([record(quality_grade="casual", captive=True)]).records
        self.assertEqual(casual.route, "RAW_CANDIDATE")
        self.assertEqual(casual.reasons, ("NOT_RESEARCH_GRADE", "CAPTIVE_OR_CULTIVATED"))
        (no_taxon,) = parse([record(taxon=...)]).records
        self.assertIn("TAXON_ABSENT", no_taxon.reasons)
        (no_point,) = parse([record(geojson=...)]).records
        self.assertIn("COORDINATES_ABSENT", no_point.reasons)

    def test_malformed_pages_rejected_whole(self):
        cases = {
            "descending ids": [record(2), record(1)],
            "duplicate ids": [record(1), record(1)],
            "bad geoprivacy": [record(geoprivacy="hidden")],
            "bad geometry": [record(geojson={"type": "Polygon", "coordinates": []})],
            "bad latitude": [record(geojson={"type": "Point", "coordinates": [0, 91]})],
            "negative accuracy": [record(positional_accuracy=-1)],
            "bad id": [record(identifier=0)],
            "too many": [record(1), record(2), record(3)],
        }
        url = obs.page_url(QUERY, per_page=2)
        for name, results in cases.items():
            with self.subTest(name=name), self.assertRaises(obs.ObservationInputError):
                obs.parse_page(body(results), status=200, source_url=url, retrieved_at=NOW)
        for raw in (b"<html>", b'{"total_results":0,"total_results":0}',
                    b'{"total_results":NaN,"per_page":2,"results":[]}'):
            with self.subTest(raw=raw), self.assertRaises(obs.ObservationInputError):
                obs.parse_page(raw, status=200, source_url=url, retrieved_at=NOW)
        with self.assertRaises(obs.ObservationInputError) as caught:
            obs.parse_page(b"", status=429, source_url=url, retrieved_at=NOW)
        self.assertEqual(str(caught.exception), "RATE_LIMITED")
        with self.assertRaises(obs.ObservationInputError):
            parse([record(1)], id_above=1)

    def test_errors_do_not_echo_payload(self):
        secret = "PRECISE-NEST-LOCATION"
        with self.assertRaises(obs.ObservationInputError) as caught:
            parse([record(geoprivacy=secret)])
        self.assertNotIn(secret, str(caught.exception))


class CursorTests(unittest.TestCase):
    def walk(self, total=5, per_page=2):
        pages, cursor, ids = [], 0, list(range(10, 10 + total))
        while True:
            chunk = [record(i) for i in ids if i > cursor][:per_page]
            page = parse(chunk, id_above=cursor, per_page=per_page,
                         total=len([i for i in ids if i > cursor]))
            pages.append(page)
            nxt = obs.next_page_url(page)
            if nxt is None:
                return pages
            self.assertIn(f"id_above={page.next_id_above}", nxt)
            cursor = page.next_id_above

    def test_complete_walk(self):
        pages = self.walk()
        self.assertEqual(len(pages), 3)
        capture = obs.reconcile(list(reversed(pages)))
        self.assertEqual(capture.outcome, "CAPTURE_CANDIDATE")
        self.assertEqual([r.observation_id for r in capture.records], [10, 11, 12, 13, 14])
        self.assertEqual(capture.coverage, "NOT_ESTABLISHED")

    def test_exact_multiple_needs_empty_terminal_page(self):
        pages = self.walk(total=4)
        self.assertEqual(len(pages[-1].records), 0)
        self.assertEqual(obs.reconcile(pages).outcome, "CAPTURE_CANDIDATE")

    def test_broken_walks_are_incomplete(self):
        pages = self.walk()
        self.assertIn("CURSOR_GAP_OR_OVERLAP", obs.reconcile([pages[0], pages[2]]).reasons)
        self.assertIn("END_NOT_REACHED", obs.reconcile(pages[:2]).reasons)
        self.assertIn("CURSOR_NOT_FROM_START", obs.reconcile(pages[1:]).reasons)
        drifted = parse([record(12), record(13)], id_above=11, total=9)
        self.assertIn("COUNT_DRIFT", obs.reconcile([pages[0], drifted, pages[2]]).reasons)

    def test_mixed_or_empty_input_rejected(self):
        other = parse([record(10)], query=obs.ObservationQuery(taxon_id=3))
        with self.assertRaises(obs.ObservationInputError):
            obs.reconcile([self.walk()[0], other])
        with self.assertRaises(obs.ObservationInputError):
            obs.reconcile([])


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            obs.reconcile([parse([record(10)])])


if __name__ == "__main__":
    unittest.main()
