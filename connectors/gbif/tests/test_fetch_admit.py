"""Deterministic synthetic tests for GBIF page retrieval recording and routing.

No provider access, rights review, sensitivity evaluation, or admission claim. Imports
connectors_core from packages/connectors-core/src (standard library only).
"""
from collections import deque
from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for path in (HERE, ROOT / "connectors/gbif/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from gbif import admit, fetch  # noqa: E402
from gbif import occurrence_api as occ  # noqa: E402
import test_occurrence_api as fixtures  # noqa: E402

RESOLVED = {"name": "gbif", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "restricted"}
URL = fixtures.url()
NC = "http://creativecommons.org/licenses/by-nc/4.0/legalcode"


def stub_hash(value):
    return "sha256:" + sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


class Clock:
    def __init__(self):
        self.wall, self.elapsed = datetime(2026, 9, 27, 12, tzinfo=timezone.utc), 0.0

    def now(self):
        return self.wall + timedelta(seconds=self.elapsed)

    def monotonic(self):
        return self.elapsed


class Sleeper:
    def __init__(self, clock):
        self.clock = clock

    def sleep(self, seconds):
        self.clock.elapsed += seconds


class Transport:
    def __init__(self, clock, *outcomes):
        self.clock, self.outcomes, self.calls = clock, deque(outcomes), []

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        self.calls.append((request, timeout_seconds, max_response_bytes, allow_redirects))
        self.clock.elapsed += 0.5
        outcome = self.outcomes.popleft()
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome


def page(records=None, **kwargs):
    return fixtures.page_body([fixtures.record()] if records is None else records, **kwargs)


def response(status=200, payload=None, headers=None):
    payload = page() if payload is None else payload
    values = {"Content-Type": "application/json", "Content-Length": str(len(payload))}
    values.update(headers or {})
    return ct.TransportResponse(status_code=status, headers=values,
                                body_chunks=(payload,) if payload else ())


def retrieve(*outcomes, url=URL, **kwargs):
    clock = Clock()
    kwargs.setdefault("retry_policy", cc.RetryPolicy(max_attempts=1))
    transport = Transport(clock, *outcomes)
    return fetch.retrieve(url, transport=transport, clock=clock, sleeper=Sleeper(clock),
                          spec_hash=stub_hash, **kwargs), transport


def decide(payload=None, descriptor=RESOLVED):
    return admit.admit(retrieve(response(payload=payload))[0], descriptor=descriptor)


class RetrievalTests(unittest.TestCase):
    def test_success_records_episode_without_query(self):
        data = page()
        retrieval, transport = retrieve(response(payload=data))
        episode = retrieval.episode
        self.assertEqual((retrieval.captured, retrieval.body), (True, data))
        self.assertEqual(episode["source_id"], fetch.SOURCE_ID)
        self.assertEqual(episode["redacted_locator"], "https://api.gbif.org/v1/occurrence/search")
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, timeout, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, timeout, budget, redirects),
                         (URL, 60.0, fetch.MAX_BYTES, False))

    def test_profile_admits_only_gbif_json(self):
        profile = fetch.profile()
        self.assertEqual(profile.allowed_hosts, frozenset({"api.gbif.org"}))
        self.assertEqual(profile.allowed_media_types, frozenset({"application/json"}))
        self.assertEqual(profile.allowed_ports, frozenset({443}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)

    def test_only_planner_urls_are_retrieved(self):
        base = "https://api.gbif.org/v1/occurrence/search?"
        cases = {
            "SOURCE_URL": ("https://api.gbif.org/v1/occurrence/search",
                           URL.replace("api.gbif.org", "example.org"), URL + "&download=true"),
            "SOURCE_URL_SCOPE": (
                base + "limit=2&offset=0",
                base + "country=US&limit=2&offset=0",
                base + "stateProvince=Kansas&limit=2&offset=0",
                base + "country=us&stateProvince=Kansas&limit=2&offset=0",
                base + "limit=2&offset=0&country=US&stateProvince=Kansas",
                fixtures.url(taxon_key=7).replace("taxonKey=7", "taxonKey=007"),
                fixtures.url().replace("stateProvince=Kansas",
                                       "stateProvince=Kansas&basisOfRecord=ALIEN"),
                fixtures.url().replace("stateProvince=Kansas",
                                       "stateProvince=Kansas&hasCoordinate=yes"),
            ),
        }
        for code, urls in cases.items():
            for url in urls:
                with self.subTest(url=url), self.assertRaises(occ.OccurrenceInputError) as ctx:
                    retrieve(response(), url=url)
                self.assertEqual(ctx.exception.args[0], code)
        # Windows plan_pages can never emit (review finding on #4750).
        for offset, limit in ((1, 300), (301, 300), (150, 200), (7, 299), (299, 300)):
            window = base + f"country=US&stateProvince=Kansas&limit={limit}&offset={offset}"
            with self.subTest(window=window), self.assertRaises(occ.OccurrenceInputError) as ctx:
                retrieve(response(), url=window)
            self.assertEqual(ctx.exception.args[0], "SOURCE_URL_SCOPE")
        planned = [plan.url for plan in occ.plan_pages(occ.OccurrenceQuery(), max_records=650)]
        planned += [plan.url for plan in occ.plan_pages(occ.OccurrenceQuery(), max_records=7,
                                                        page_size=3)]
        for url in planned:
            with self.subTest(planned=url):
                fetch._require_planned(url)
        for url in (fixtures.url(taxon_key=7, year="1990,2000", basis_of_record="PRESERVED_SPECIMEN",
                                 has_coordinate=True),
                    fixtures.url(offset=4)):
            with self.subTest(url=url):
                self.assertEqual(retrieve(response(payload=page(offset=4) if "offset=4" in url
                                                   else page()), url=url)[0].source_url, url)

    def test_failures_drop_body(self):
        for status, category in ((403, "ACCESS_DENIED"), (404, "NOT_FOUND"),
                                 (429, "RETRY_EXHAUSTED"), (503, "RETRY_EXHAUSTED")):
            with self.subTest(status=status):
                retrieval, _ = retrieve(response(status, b"no"))
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertIsNone(retrieval.body)


class AdmissionTests(unittest.TestCase):
    def test_parsed_page_is_flagged_raw_candidate(self):
        decision = decide(page([fixtures.record(1), fixtures.record(2)]))
        self.assertEqual((decision.route, decision.reasons),
                         (admit.RAW, ("SENSITIVITY_NOT_EVALUATED",)))
        self.assertEqual(len(decision.page.records), 2)
        self.assertEqual((decision.admission, decision.coverage, decision.sensitivity,
                          decision.write_performed),
                         ("NOT_ADMITTED", "NOT_ESTABLISHED", "NOT_EVALUATED", False))
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_record_level_flags_surface_on_the_page(self):
        records = [fixtures.record(1, license=NC, occurrenceStatus="ABSENT"),
                   fixtures.record(2, datasetKey=None)]
        decision = decide(page(records))
        self.assertEqual(decision.route, admit.RAW)
        self.assertEqual(decision.reasons, ("SENSITIVITY_NOT_EVALUATED",
                                            "RECORD_QUARANTINE_CANDIDATES",
                                            "NONCOMMERCIAL_TERMS_PRESENT",
                                            "ABSENCE_ASSERTIONS_PRESENT"))

    def test_empty_terminal_page_carries_no_sensitivity_flag(self):
        self.assertEqual(decide(page([])).reasons, ())

    def test_paging_ceiling_is_flagged(self):
        decision = decide(page([fixtures.record(1), fixtures.record(2)],
                               count=occ.PAGING_CEILING + 1, end=False))
        self.assertIn("PAGING_CEILING_USE_ASYNC_DOWNLOAD", decision.reasons)

    def test_page_rejection_is_quarantine_candidate(self):
        decision = decide(page([fixtures.record(1), fixtures.record(1)]))
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_DUPLICATE_OCCURRENCE_KEY",)))
        self.assertIsNone(decision.page)

    def test_uncaptured_page_is_held_with_contract_reason(self):
        decision = admit.admit(retrieve(response(403, b"no"))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.HOLD, ("ACCESS_DENIED",)))

    def test_public_or_unresolved_sensitivity_floor_holds(self):
        for floor in ("public", "PUBLIC", "TBD", "needs verification", "", "publc",
                      "internal", "synthetic-restricted", "unknown"):
            with self.subTest(floor=floor):
                decision = decide(descriptor={**RESOLVED, "sensitivity_floor": floor})
                self.assertEqual((decision.route, decision.provisional_route),
                                 (admit.HOLD, admit.RAW))
                self.assertEqual(decision.reasons[-1], "DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED")
        self.assertEqual(admit.descriptor_blockers({**RESOLVED, "name": "fema"}),
                         ("DESCRIPTOR_INVALID",))
        self.assertEqual(admit.descriptor_blockers({"name": "fema", "sensitivity_floor": "public"}),
                         ("DESCRIPTOR_INVALID",))

    def test_recognized_non_public_floors_open_the_route(self):
        for floor in ("generalized", "Restricted", "QUARANTINE"):
            with self.subTest(floor=floor):
                decision = decide(descriptor={**RESOLVED, "sensitivity_floor": floor})
                self.assertEqual(decision.route, admit.RAW)

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "gbif")
        decision = admit.admit(retrieve(response())[0])
        self.assertEqual((decision.route, decision.provisional_route), (admit.HOLD, admit.RAW))
        self.assertEqual(decision.reasons[-3:], ("DESCRIPTOR_ROLE_UNRESOLVED",
                                                 "DESCRIPTOR_RIGHTS_UNRESOLVED",
                                                 "DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED"))

    def test_tampered_retrieval_cannot_be_constructed(self):
        good = retrieve(response())[0]
        with self.assertRaises(fetch.FetchInputError):
            fetch.Retrieval(good.source_url, good.episode_json, page([fixtures.record(9)]))
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_episode_from_another_source_is_refused(self):
        good = retrieve(response())[0]
        base = good.episode
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": "kfm:source-profile:other-profile-v1"}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url, json.dumps({**base, **override}),
                                         good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(retrieve(response())[0], descriptor=RESOLVED)
            admit.admit(retrieve(response(403, b"no"))[0])


if __name__ == "__main__":
    unittest.main()
