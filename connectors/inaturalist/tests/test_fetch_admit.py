"""Deterministic synthetic tests for iNaturalist page retrieval recording and routing.

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
for path in (HERE, ROOT / "connectors/inaturalist/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from inaturalist import admit, fetch  # noqa: E402
from inaturalist import observations_api as obs  # noqa: E402
import test_observations_api as fixtures  # noqa: E402

RESOLVED = {"name": "inaturalist", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "restricted"}
URL = obs.page_url(fixtures.QUERY, per_page=2)


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
    return fixtures.body([fixtures.record()] if records is None else records, **kwargs)


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


def decide(payload=None, descriptor=RESOLVED, url=URL):
    return admit.admit(retrieve(response(payload=payload), url=url)[0], descriptor=descriptor)


class RetrievalTests(unittest.TestCase):
    def test_success_records_episode_without_query(self):
        data = page()
        retrieval, transport = retrieve(response(payload=data))
        episode = retrieval.episode
        self.assertEqual((retrieval.captured, retrieval.body), (True, data))
        self.assertEqual(episode["source_id"], fetch.SOURCE_ID)
        self.assertEqual(episode["redacted_locator"], "https://api.inaturalist.org/v1/observations")
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, timeout, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, timeout, budget, redirects),
                         (URL, 60.0, fetch.MAX_BYTES, False))

    def test_profile_admits_only_inaturalist_json(self):
        profile = fetch.profile()
        self.assertEqual(profile.allowed_hosts, frozenset({"api.inaturalist.org"}))
        self.assertEqual(profile.allowed_media_types, frozenset({"application/json"}))
        self.assertEqual(profile.allowed_ports, frozenset({443}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)

    def test_only_planner_canonical_urls_are_retrieved(self):
        base = "https://api.inaturalist.org/v1/observations?"
        tail = "per_page=2&order=asc&order_by=id&id_above=0"
        cases = {
            "SOURCE_URL": ("https://api.inaturalist.org/v1/observations",
                           URL.replace("api.inaturalist.org", "example.org"),
                           URL + "&user_id=7"),
            "SOURCE_URL_SCOPE": (
                base + tail,
                base + "swlat=36.9&swlng=-102.1&" + tail,
                base + "place_id=38&swlat=36.9&swlng=-102.1&nelat=40.1&nelng=-94.5&" + tail,
                base + "place_id=038&" + tail,
                base + "swlat=36.90&swlng=-102.1&nelat=40.1&nelng=-94.5&" + tail,
                URL.replace("per_page=2", "per_page=2&quality_grade=best"),
                URL.replace("per_page=2", "per_page=2&d1=2020-1-01"),
            ),
        }
        for code, urls in cases.items():
            for url in urls:
                with self.subTest(url=url), self.assertRaises(obs.ObservationInputError) as ctx:
                    retrieve(response(), url=url)
                self.assertEqual(ctx.exception.args[0], code)
        place = obs.ObservationQuery(bounds=None, place_id=38, taxon_id=5,
                                     quality_grade="research", observed_from="2020-01-01",
                                     observed_to="2020-12-31")
        second = obs.next_page_url(obs.parse_page(
            page([fixtures.record(1), fixtures.record(2)]), status=200, source_url=URL,
            retrieved_at=fixtures.NOW))
        for url in (obs.page_url(place, per_page=2),
                    obs.page_url(fixtures.QUERY, id_above=41, per_page=2),
                    second,
                    base + "nelat=40.1&nelng=-94.5&swlat=36.9&swlng=-102.1&" + tail):
            with self.subTest(url=url):
                self.assertEqual(retrieve(response(payload=page([fixtures.record(50)])),
                                          url=url)[0].source_url, url)
        # The module's own cursor continuation must be accepted by fetch.
        self.assertNotEqual(second, obs.page_url(fixtures.QUERY, id_above=2, per_page=2))

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
        next_url = obs.next_page_url(decision.page)
        self.assertEqual(retrieve(response(payload=page([fixtures.record(3)])),
                                  url=next_url)[0].source_url, next_url)
        self.assertEqual((decision.admission, decision.coverage, decision.sensitivity,
                          decision.write_performed),
                         ("NOT_ADMITTED", "NOT_ESTABLISHED", "NOT_EVALUATED", False))
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_record_level_reasons_surface_as_page_flags(self):
        records = [fixtures.record(1, geoprivacy="obscured", obscured=True, license_code="cc-by-nc"),
                   fixtures.record(2, quality_grade="needs_id", captive=True)]
        decision = decide(page(records))
        self.assertEqual(decision.route, admit.RAW)
        self.assertEqual(decision.reasons, ("SENSITIVITY_NOT_EVALUATED",
                                            "RECORD_QUARANTINE_CANDIDATES",
                                            "GEOPRIVACY_RESTRICTED_PRESENT",
                                            "LICENSE_OBLIGATIONS_PRESENT",
                                            "NOT_RESEARCH_GRADE_PRESENT",
                                            "CAPTIVE_OR_CULTIVATED_PRESENT"))

    def test_empty_terminal_page_carries_no_flags(self):
        self.assertEqual(decide(page([], total=0)).reasons, ())

    def test_page_rejection_is_quarantine_candidate(self):
        decision = decide(page([fixtures.record(2), fixtures.record(1)]))
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_CURSOR_ORDER",)))
        self.assertIsNone(decision.page)

    def test_uncaptured_page_is_held_with_contract_reason(self):
        decision = admit.admit(retrieve(response(403, b"no"))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.HOLD, ("ACCESS_DENIED",)))

    def test_sensitivity_floor_must_be_reviewed_non_public(self):
        for floor in ("public", "TBD", "", "publc", "internal", "unknown"):
            with self.subTest(floor=floor):
                decision = decide(descriptor={**RESOLVED, "sensitivity_floor": floor})
                self.assertEqual((decision.route, decision.provisional_route),
                                 (admit.HOLD, admit.RAW))
                self.assertEqual(decision.reasons[-1], "DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED")
        for floor in ("generalized", "Restricted", "QUARANTINE"):
            with self.subTest(floor=floor):
                self.assertEqual(decide(descriptor={**RESOLVED, "sensitivity_floor": floor}).route,
                                 admit.RAW)
        self.assertEqual(admit.descriptor_blockers({"name": "gbif", "sensitivity_floor": "public"}),
                         ("DESCRIPTOR_INVALID",))

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "inaturalist")
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

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        from connectors_core.core import redact_url
        good = retrieve(response())[0]
        for url in ("https://api.inaturalist.org/v1/observations?per_page=2&order=asc&order_by=id&id_above=0",):
            episode = {**good.episode, "redacted_locator": redact_url(url)}
            forged = fetch.Retrieval(url, json.dumps(episode), good.body)
            with self.subTest(url=url), self.assertRaises(obs.ObservationInputError) as ctx:
                admit.admit(forged, descriptor=RESOLVED)
            self.assertEqual(ctx.exception.args[0], "SOURCE_URL_SCOPE")


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(retrieve(response())[0], descriptor=RESOLVED)
            admit.admit(retrieve(response(403, b"no"))[0])


if __name__ == "__main__":
    unittest.main()
