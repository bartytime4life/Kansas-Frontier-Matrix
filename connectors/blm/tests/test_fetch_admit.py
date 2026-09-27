"""Deterministic synthetic tests for BLM PLSS (CadNSDI) retrieval recording and routing.

No BLM access, survey review, title claim, or admission claim. Imports connectors_core
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
for path in (HERE, ROOT / "connectors/blm/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from connectors_core.core import redact_url  # noqa: E402
from blm import admit, fetch, plss_cadnsdi  # noqa: E402
import test_plss_cadnsdi as fixtures  # noqa: E402

RESOLVED = {"name": "blm", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
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


def run(payload=BODY, url=URL, status=200, media="application/geo+json"):
    clock = Clock()
    transport = Transport(clock, response(status, payload, media))
    retrieval = fetch.retrieve(url, transport=transport, clock=clock, sleeper=Sleeper(clock),
                               spec_hash=stub_hash, retry_policy=cc.RetryPolicy(max_attempts=1))
    return retrieval, transport


def plss(payload=BODY, **kwargs):
    return run(payload, **kwargs)[0]


class RetrievalTests(unittest.TestCase):
    def test_episode_identity_and_request(self):
        retrieval, transport = run()
        episode = retrieval.episode
        self.assertTrue(retrieval.captured)
        self.assertEqual((episode["source_id"], episode["retrieval_profile_ref"]),
                         (fetch.SOURCE_ID, fetch.RETRIEVAL_PROFILE))
        self.assertEqual(episode["redacted_locator"], URL.split("?")[0])
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, _, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, budget, redirects), (URL, fetch.MAX_BYTES, False))
        self.assertTrue(plss(media="application/json").captured)

    def test_only_planner_canonical_urls(self):
        for url, code in ((URL.replace("%27KS%27", "%27NE%27"), "SOURCE_URL_SCOPE"),
                          (URL.replace("/MapServer/1/", "/MapServer/7/"), "LAYER"),
                          (URL + "#x", "SOURCE_URL")):
            with self.subTest(url=url), self.assertRaises(plss_cadnsdi.PlssInputError) as ctx:
                plss(url=url)
            self.assertEqual(ctx.exception.args[0], code)

    def test_profile(self):
        self.assertEqual(fetch.profile().allowed_hosts, frozenset({"gis.blm.gov"}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)
        blocked = plss(media="text/html")
        self.assertEqual(blocked.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")


class AdmissionTests(unittest.TestCase):
    def test_parsed_page_routes_raw_with_flags(self):
        decision = admit.admit(plss(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(decision.page.features[0].title_authority, False)
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.HOLD
        flagged = fixtures.body([fixtures.feature(1, ring=fixtures.SQUARE[:-1])],
                                exceededTransferLimit=True)
        self.assertEqual(admit.admit(plss(flagged), descriptor=RESOLVED).reasons,
                         ("RECORD_QUARANTINE_CANDIDATES", "MORE_PAGES"))

    def test_parser_rejection_is_quarantine_candidate(self):
        decision = admit.admit(plss(fixtures.body([fixtures.feature(STATEABBR="NE")])),
                               descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_STATE_SCOPE",)))
        self.assertIsNone(decision.page)

    def test_uncaptured_retrievals_are_held(self):
        for status in (403, 404, 500):
            retrieval = plss(b"no", status=status)
            with self.subTest(status=status):
                decision = admit.admit(retrieval, descriptor=RESOLVED)
                self.assertEqual(decision.route, admit.HOLD)
                self.assertEqual(decision.reasons,
                                 tuple(retrieval.episode["result"]["reason_codes"]))

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "blm")
        decision = admit.admit(plss())
        self.assertEqual((decision.route, decision.provisional_route), (admit.HOLD, admit.RAW))
        self.assertEqual(decision.reasons[-2:], ("DESCRIPTOR_ROLE_UNRESOLVED",
                                                 "DESCRIPTOR_RIGHTS_UNRESOLVED"))

    def test_episode_from_another_source_is_refused(self):
        good = plss()
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": "kfm:source-profile:other-v1"},
                         {"source_id": ["blm.plss-cadnsdi"]}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url,
                                         json.dumps({**good.episode, **override}), good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        for good in (plss(), plss(b"no", status=404)):
            for url, code in ((URL.replace("%27KS%27", "%27NE%27"), "SOURCE_URL_SCOPE"),
                              (URL.replace("gis.blm.gov", "evil.example"), "SOURCE_URL")):
                episode = {**good.episode, "redacted_locator": redact_url(url)}
                forged = fetch.Retrieval(url, json.dumps(episode), good.body)
                with self.subTest(url=url, captured=good.captured), \
                        self.assertRaises(plss_cadnsdi.PlssInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], code)


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(plss(), descriptor=RESOLVED)


if __name__ == "__main__":
    unittest.main()
