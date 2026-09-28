"""Deterministic synthetic tests for OpenFEMA page retrieval recording and routing.

No FEMA access, rights review, or admission claim. Imports connectors_core from
packages/connectors-core/src (standard library only).
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
for path in (HERE, ROOT / "connectors/fema/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from fema import admit, fetch  # noqa: E402
from fema import openfema_declarations as of  # noqa: E402
import test_openfema_declarations as fixtures  # noqa: E402

RESOLVED = {"name": "fema", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
UNRESOLVED = {"name": "fema", "role": "TBD", "rights": "TBD", "sensitivity_floor": "public"}
URL = of.page_url(of.declaration_filter(), top=2)


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


def page(rows=None, **kwargs):
    return fixtures.body([fixtures.record()] if rows is None else rows, top=2, **kwargs)


def response(status=200, payload=None, headers=None, url=None):
    payload = page() if payload is None else payload
    values = {"Content-Type": "application/json", "Content-Length": str(len(payload))}
    values.update(headers or {})
    return ct.TransportResponse(status_code=status, headers=values,
                                body_chunks=(payload,) if payload else (), final_url=url)


def retrieve(*outcomes, url=URL, **kwargs):
    clock = Clock()
    kwargs.setdefault("retry_policy", cc.RetryPolicy(max_attempts=1))
    transport = Transport(clock, *outcomes)
    return fetch.retrieve(url, transport=transport, clock=clock, sleeper=Sleeper(clock),
                          spec_hash=stub_hash, **kwargs), transport


class RetrievalTests(unittest.TestCase):
    def test_success_records_episode_without_query(self):
        data = page()
        retrieval, transport = retrieve(response(payload=data))
        episode = retrieval.episode
        self.assertTrue(retrieval.captured)
        self.assertEqual(retrieval.body, data)
        self.assertEqual(episode["source_id"], fetch.SOURCE_ID)
        self.assertEqual(episode["redacted_locator"],
                         "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries")
        self.assertEqual(episode["transport"]["body_digest"], "sha256:" + sha256(data).hexdigest())
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        request, timeout, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, timeout, budget, redirects),
                         (URL, 60.0, fetch.MAX_BYTES, False))

    def test_profile_admits_only_fema_json(self):
        profile = fetch.profile()
        self.assertEqual(profile.allowed_hosts, frozenset({"www.fema.gov"}))
        self.assertEqual(profile.allowed_media_types, frozenset({"application/json"}))
        self.assertEqual(profile.allowed_ports, frozenset({443}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.profile(fetch.MAX_BYTES + 1)

    def test_only_planner_urls_are_retrieved(self):
        for url in ("https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries",
                    URL.replace("state+eq+%27KS%27", "state+eq+%27MO%27"),
                    URL.replace("www.fema.gov", "example.org")):
            with self.subTest(url=url), self.assertRaises(of.OpenFemaInputError):
                retrieve(response(), url=url)

    def test_failures_drop_body(self):
        for status, category in ((403, "ACCESS_DENIED"), (404, "NOT_FOUND"),
                                 (429, "RETRY_EXHAUSTED"), (503, "RETRY_EXHAUSTED")):
            with self.subTest(status=status):
                retrieval, _ = retrieve(response(status, b"no"))
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertIsNone(retrieval.body)
        wrong_type, _ = retrieve(response(headers={"Content-Type": "text/html"}))
        self.assertEqual(wrong_type.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")


class AdmissionTests(unittest.TestCase):
    def test_parsed_page_is_raw_candidate_with_next_cursor(self):
        rows = [fixtures.record(1), fixtures.record(2)]
        decision = admit.admit(retrieve(response(payload=page(rows)))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(len(decision.page.records), 2)
        self.assertEqual(of.next_page_url(decision.page),
                         of.page_url(of.declaration_filter(), after_id=fixtures.rid(2), top=2))
        self.assertEqual((decision.admission, decision.coverage, decision.write_performed),
                         ("NOT_ADMITTED", "NOT_ESTABLISHED", False))
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_record_level_quarantine_is_flagged(self):
        rows = [fixtures.record(1, incidentEndDate="2020-03-01T00:00:00.000Z")]
        decision = admit.admit(retrieve(response(payload=page(rows)))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.RAW, ("RECORD_QUARANTINE_CANDIDATES",)))

    def test_page_rejection_is_quarantine_candidate(self):
        decision = admit.admit(retrieve(response(payload=page(count=-1)))[0], descriptor=RESOLVED)
        self.assertEqual(decision.route, admit.QUARANTINE)
        self.assertTrue(decision.reasons[0].startswith("PARSE_"))
        self.assertIsNone(decision.page)

    def test_uncaptured_page_is_held_with_contract_reason(self):
        decision = admit.admit(retrieve(response(403, b"no"))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.HOLD, ("ACCESS_DENIED",)))

    def test_checked_in_descriptor_releases_candidate_routes(self):
        descriptor = admit.load_descriptor()
        self.assertEqual((descriptor.get("name"), descriptor.get("role"), descriptor.get("rights")),
                         ("fema", "administrative", "public-domain-us-government-work"))
        self.assertEqual(admit.descriptor_blockers(descriptor), ())
        for payload, provisional in ((page(), admit.RAW), (page(count=-1), admit.QUARANTINE)):
            with self.subTest(provisional=provisional):
                decision = admit.admit(retrieve(response(payload=payload))[0])
                self.assertEqual((decision.route, decision.provisional_route),
                                 (provisional, provisional))
                self.assertFalse([r for r in decision.reasons if r.startswith("DESCRIPTOR_")])
        held = admit.admit(retrieve(response(payload=page()))[0], descriptor=UNRESOLVED)
        self.assertEqual(held.route, admit.HOLD)

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
        for url in (URL.replace("www.fema.gov", "evil.example"),):
            episode = {**good.episode, "redacted_locator": redact_url(url)}
            forged = fetch.Retrieval(url, json.dumps(episode), good.body)
            with self.subTest(url=url), self.assertRaises(of.OpenFemaInputError) as ctx:
                admit.admit(forged, descriptor=RESOLVED)
            self.assertEqual(ctx.exception.args[0], "SOURCE_URL")


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(retrieve(response())[0], descriptor=RESOLVED)
            admit.admit(retrieve(response(403, b"no"))[0])


if __name__ == "__main__":
    unittest.main()
