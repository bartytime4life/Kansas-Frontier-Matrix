"""Deterministic synthetic tests for NRCS SCAN (AWDB) retrieval recording and routing.

No NRCS access, station review, rights review, or admission claim. Imports connectors_core
from packages/connectors-core/src (standard library only).
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
for path in (HERE, ROOT / "connectors/nrcs/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from connectors_core.core import redact_url  # noqa: E402
from nrcs import admit, fetch, scan_awdb  # noqa: E402
import test_scan_awdb as fixtures  # noqa: E402

RESOLVED = {"name": "nrcs", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
UNRESOLVED = {"name": "nrcs", "role": "TBD", "rights": "TBD", "sensitivity_floor": "public"}
URL = fixtures.URL
BODY = fixtures.body()


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


def response(status=200, payload=b"", media="application/json"):
    headers = {"Content-Type": media, "Content-Length": str(len(payload))}
    return ct.TransportResponse(status_code=status, headers=headers,
                                body_chunks=(payload,) if payload else ())


def run(payload=BODY, url=URL, status=200, media="application/json"):
    clock = Clock()
    transport = Transport(clock, response(status, payload, media))
    retrieval = fetch.retrieve(url, transport=transport, clock=clock, sleeper=Sleeper(clock),
                               spec_hash=stub_hash, retry_policy=cc.RetryPolicy(max_attempts=1))
    return retrieval, transport


def scan(payload=BODY, **kwargs):
    return run(payload, **kwargs)[0]


class RetrievalTests(unittest.TestCase):
    def test_episode_identity_and_request(self):
        retrieval, transport = run()
        episode = retrieval.episode
        self.assertTrue(retrieval.captured)
        self.assertEqual((episode["source_id"], episode["retrieval_profile_ref"]),
                         (fetch.SOURCE_ID, fetch.RETRIEVAL_PROFILE))
        self.assertEqual(episode["redacted_locator"],
                         "https://wcc.sc.egov.usda.gov/awdbRestApi/services/v1/data")
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, _, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, budget, redirects), (URL, fetch.MAX_BYTES, False))
        self.assertEqual(dict(request.headers), {"accept": "application/json"})

    def test_only_planner_canonical_urls(self):
        for url, code in ((URL.replace("KS%3ASCAN", "KS%3ATSCAN"), "STATION_SCOPE"),
                          (URL.replace("%3A", ":"), "SOURCE_URL_SCOPE"),
                          (URL + "&extra=1", "SOURCE_URL")):
            with self.subTest(url=url), self.assertRaises(scan_awdb.ScanInputError) as ctx:
                scan(url=url)
            self.assertEqual(ctx.exception.args[0], code)

    def test_profile(self):
        self.assertEqual(fetch.profile().allowed_hosts, frozenset({"wcc.sc.egov.usda.gov"}))
        self.assertEqual(fetch.profile().allowed_media_types, frozenset({"application/json"}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)
        blocked = scan(media="text/html")
        self.assertEqual(blocked.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")


class AdmissionTests(unittest.TestCase):
    def test_parsed_response_routes_raw_with_flags(self):
        decision = admit.admit(scan(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.RAW, ("MISSING_VALUES_PRESENT",)))
        self.assertEqual(decision.data.series[0].element_code, "SMS")
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.HOLD
        flagged = fixtures.body([fixtures.element(values=[{"date": "2023-06-01", "value": "x"}]),
                                 fixtures.element("STO", depth=None, values=[])])
        self.assertEqual(admit.admit(scan(flagged, url=fixtures.LOOSE_URL),
                                     descriptor=RESOLVED).reasons,
                         ("RECORD_QUARANTINE_CANDIDATES", "EMPTY_SERIES_PRESENT",
                          "DEPTH_NOT_STATED"))
        partial = fixtures.body([fixtures.element(values=[{"date": "2023-06-01", "value": 1}])])
        self.assertEqual(admit.admit(scan(partial), descriptor=RESOLVED).reasons,
                         ("REQUESTED_SERIES_NOT_RETURNED",))
        clean = fixtures.body([
            fixtures.element(values=[{"date": "2023-06-01", "value": 1}]),
            fixtures.element("STO", values=[{"date": "2023-06-01", "value": 20.5}])])
        self.assertEqual(admit.admit(scan(clean), descriptor=RESOLVED).reasons, ())

    def test_parser_rejection_is_quarantine_candidate(self):
        decision = admit.admit(scan(fixtures.body(triplet="99902:KS:SCAN")), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_STATION_NOT_REQUESTED",)))
        self.assertIsNone(decision.data)

    def test_uncaptured_retrievals_are_held(self):
        for status in (403, 404, 500):
            retrieval = scan(b"no", status=status)
            with self.subTest(status=status):
                decision = admit.admit(retrieval, descriptor=RESOLVED)
                self.assertEqual(decision.route, admit.HOLD)
                self.assertEqual(decision.reasons,
                                 tuple(retrieval.episode["result"]["reason_codes"]))

    def test_checked_in_descriptor_releases_candidate_routes(self):
        descriptor = admit.load_descriptor()
        self.assertEqual((descriptor.get("name"), descriptor.get("role"), descriptor.get("rights")),
                         ("nrcs", "observed", "public-domain-us-government-work"))
        self.assertEqual(admit.descriptor_blockers(descriptor), ())
        decision = admit.admit(scan())
        self.assertEqual((decision.route, decision.provisional_route), (admit.RAW, admit.RAW))
        self.assertEqual((decision.admission, decision.write_performed), ("NOT_ADMITTED", False))
        self.assertEqual(admit.admit(scan(), descriptor=UNRESOLVED).reasons[-2:],
                         ("DESCRIPTOR_ROLE_UNRESOLVED", "DESCRIPTOR_RIGHTS_UNRESOLVED"))

    def test_episode_from_another_source_is_refused(self):
        good = scan()
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": "kfm:source-profile:other-v1"},
                         {"source_id": ["nrcs.scan-awdb"]}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url,
                                         json.dumps({**good.episode, **override}), good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        for good in (scan(), scan(b"no", status=404)):
            for url, code in ((URL.replace("KS%3ASCAN", "KS%3ATSCAN"), "STATION_SCOPE"),
                              (URL.replace("wcc.sc.egov.usda.gov", "evil.example"),
                               "SOURCE_URL")):
                episode = {**good.episode, "redacted_locator": redact_url(url)}
                forged = fetch.Retrieval(url, json.dumps(episode), good.body)
                with self.subTest(url=url, captured=good.captured), \
                        self.assertRaises(scan_awdb.ScanInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], code)


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(scan(), descriptor=RESOLVED)


if __name__ == "__main__":
    unittest.main()
