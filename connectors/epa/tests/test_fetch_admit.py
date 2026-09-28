"""Deterministic synthetic tests for EPA AQS AirData retrieval recording and routing.

No EPA access, monitor review, rights review, or admission claim. Imports connectors_core
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
for path in (HERE, ROOT / "connectors/epa/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from connectors_core.core import redact_url  # noqa: E402
from epa import admit, aqs_airdata, fetch  # noqa: E402
import test_aqs_airdata as fixtures  # noqa: E402

RESOLVED = {"name": "epa", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
URL = fixtures.URL
BODY = fixtures.archive()
MEDIA = "application/zip"


def stub_hash(value):
    return "sha256:" + sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


class Clock:
    def __init__(self):
        self.wall, self.elapsed = datetime(2026, 9, 28, 12, tzinfo=timezone.utc), 0.0

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


def response(status=200, payload=b"", media=MEDIA):
    headers = {"Content-Type": media, "Content-Length": str(len(payload))}
    return ct.TransportResponse(status_code=status, headers=headers,
                                body_chunks=(payload,) if payload else ())


def run(payload=BODY, url=URL, status=200, media=MEDIA):
    clock = Clock()
    transport = Transport(clock, response(status, payload, media))
    retrieval = fetch.retrieve(url, transport=transport, clock=clock, sleeper=Sleeper(clock),
                               spec_hash=stub_hash, retry_policy=cc.RetryPolicy(max_attempts=1))
    return retrieval, transport


def daily(payload=BODY, **kwargs):
    return run(payload, **kwargs)[0]


class RetrievalTests(unittest.TestCase):
    def test_episode_identity_and_request(self):
        retrieval, transport = run()
        episode = retrieval.episode
        self.assertTrue(retrieval.captured)
        self.assertEqual((episode["source_id"], episode["retrieval_profile_ref"]),
                         (fetch.SOURCE_ID, fetch.RETRIEVAL_PROFILE))
        self.assertEqual(episode["redacted_locator"], URL)
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, _, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, budget, redirects), (URL, fetch.MAX_BYTES, False))
        self.assertEqual(dict(request.headers), {"accept": "application/zip"})

    def test_only_planner_canonical_urls(self):
        for url, code in ((URL.replace("88101", "12345"), "PARAMETER_SCOPE"),
                          (URL + "?x=1", "SOURCE_URL"),
                          (URL.replace("aqs.epa.gov", "evil.example"), "SOURCE_URL")):
            with self.subTest(url=url), self.assertRaises(aqs_airdata.AqsInputError) as ctx:
                daily(url=url)
            self.assertEqual(ctx.exception.args[0], code)

    def test_profile(self):
        self.assertEqual(fetch.profile().allowed_hosts, frozenset({"aqs.epa.gov"}))
        self.assertEqual(fetch.profile().allowed_media_types, fetch.MEDIA_TYPES)
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)
        self.assertTrue(daily(media="application/x-zip-compressed").captured)
        blocked = daily(media="text/html")
        self.assertEqual(blocked.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")


class AdmissionTests(unittest.TestCase):
    def test_parsed_archive_routes_raw_with_flags(self):
        decision = admit.admit(daily(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(decision.daily_file.records[0].site_id, "20-999-9001")
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.HOLD
        flagged = fixtures.archive([
            fixtures.row(**{"Event Type": "Included"}),
            fixtures.row(AQI="", **{"Date Local": "2023-06-02"}),
            fixtures.row(**{"Date Local": "2023-06-03", "Arithmetic Mean": "x"})])
        self.assertEqual(admit.admit(daily(flagged), descriptor=RESOLVED).reasons,
                         ("RECORD_QUARANTINE_CANDIDATES", "EVENT_TREATED_ROWS_PRESENT",
                          "AQI_NOT_REPORTED_PRESENT"))
        elsewhere = fixtures.archive([fixtures.row(**{"State Code": "19"})])
        self.assertEqual(admit.admit(daily(elsewhere), descriptor=RESOLVED).reasons,
                         ("NO_KANSAS_ROWS",))

    def test_parser_rejection_is_quarantine_candidate(self):
        decision = admit.admit(daily(fixtures.archive(member="other.csv")), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_ZIP_MEMBER_NAME",)))
        self.assertIsNone(decision.daily_file)

    def test_uncaptured_retrievals_are_held(self):
        for status in (403, 404, 500):
            retrieval = daily(b"no", status=status)
            with self.subTest(status=status):
                decision = admit.admit(retrieval, descriptor=RESOLVED)
                self.assertEqual(decision.route, admit.HOLD)
                self.assertEqual(decision.reasons,
                                 tuple(retrieval.episode["result"]["reason_codes"]))

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "epa")
        decision = admit.admit(daily())
        self.assertEqual((decision.route, decision.provisional_route), (admit.HOLD, admit.RAW))
        self.assertEqual(decision.reasons[-2:], ("DESCRIPTOR_ROLE_UNRESOLVED",
                                                 "DESCRIPTOR_RIGHTS_UNRESOLVED"))

    def test_episode_from_another_source_is_refused(self):
        good = daily()
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": "kfm:source-profile:other-v1"},
                         {"source_id": ["epa.aqs-airdata-daily"]}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url,
                                         json.dumps({**good.episode, **override}), good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        for good in (daily(), daily(b"no", status=404)):
            for url, code in ((URL.replace("88101", "12345"), "PARAMETER_SCOPE"),
                              (URL.replace("aqs.epa.gov", "evil.example"), "SOURCE_URL")):
                episode = {**good.episode, "redacted_locator": redact_url(url)}
                forged = fetch.Retrieval(url, json.dumps(episode), good.body)
                with self.subTest(url=url, captured=good.captured), \
                        self.assertRaises(aqs_airdata.AqsInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], code)


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(daily(), descriptor=RESOLVED)


if __name__ == "__main__":
    unittest.main()
