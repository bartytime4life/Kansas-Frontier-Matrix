"""Deterministic synthetic tests for USGS retrieval recording and routing; no network.

Imports connectors_core from packages/connectors-core/src (standard library only).
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

ROOT = Path(__file__).resolve().parents[3]
for path in (ROOT / "connectors/usgs/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from usgs import admit, earthquake, fetch  # noqa: E402

RESOLVED = {"name": "usgs", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}


def stub_hash(value):
    return "sha256:" + sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def body(events=1, count=None):
    features = [{"type": "Feature", "id": f"synthetic{i}",
                 "geometry": {"type": "Point", "coordinates": [-98, 38, 5]},
                 "properties": {"time": 1000, "updated": 2000, "mag": 1.1, "magType": "ml",
                                "type": "earthquake", "status": "reviewed"}}
                for i in range(events)]
    return json.dumps({"type": "FeatureCollection", "features": features,
                       "metadata": {"status": 200, "generated": 3000,
                                    "count": events if count is None else count}}).encode()


class Clock:
    def __init__(self):
        self.wall, self.elapsed = datetime(2026, 9, 22, 18, tzinfo=timezone.utc), 0.0

    def now(self):
        return self.wall + timedelta(seconds=self.elapsed)

    def monotonic(self):
        return self.elapsed


class Sleeper:
    def __init__(self, clock):
        self.clock, self.delays = clock, []

    def sleep(self, seconds):
        self.delays.append(seconds)
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


def response(status=200, payload=None, headers=None, url=None, **kwargs):
    payload = body() if payload is None else payload
    values = {"Content-Type": "application/json; charset=utf-8",
              "Content-Length": str(len(payload))}
    values.update(headers or {})
    return ct.TransportResponse(status_code=status, headers=values,
                                body_chunks=(payload,) if payload else (),
                                final_url=url, **kwargs)


def retrieve(*outcomes, url=None, **kwargs):
    clock = Clock()
    kwargs.setdefault("retry_policy", cc.RetryPolicy(max_attempts=1))
    transport = Transport(clock, *outcomes)
    result = fetch.retrieve(url or earthquake.live_url(), transport=transport, clock=clock,
                            sleeper=Sleeper(clock), spec_hash=stub_hash, **kwargs)
    return result, transport


class RetrievalTests(unittest.TestCase):
    def test_success_keeps_body_and_records_identity(self):
        data = body()
        retrieval, transport = retrieve(response(payload=data, headers={
            "ETag": 'W/"v1"', "Last-Modified": "Tue, 22 Sep 2026 17:59:00 GMT"}))
        episode, record = retrieval.episode, retrieval.episode["transport"]
        self.assertTrue(retrieval.captured)
        self.assertEqual(retrieval.body, data)
        self.assertEqual((record["category"], record["http_status"]), ("SUCCESS", 200))
        self.assertEqual(record["body_digest"], "sha256:" + sha256(data).hexdigest())
        self.assertEqual((record["body_bytes"], record["content_length"]), (len(data), len(data)))
        self.assertEqual(record["content_type"], "application/json")
        self.assertEqual((record["etag"], record["last_modified"]),
                         ('W/"v1"', "2026-09-22T17:59:00Z"))
        self.assertEqual((record["elapsed_ms"], record["retry_count"]), (500, 0))
        self.assertEqual((episode["attempted_at"], episode["completed_at"]),
                         ("2026-09-22T18:00:00Z", "2026-09-22T18:00:00Z"))
        self.assertEqual(episode["result"],
                         {"status": "CAPTURED", "reason_codes": ["RETRIEVAL_BODY_CAPTURED"]})
        request, timeout, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, request.headers["accept"]),
                         (earthquake.live_url(), fetch.ACCEPT))
        self.assertEqual((timeout, budget, redirects), (30.0, fetch.MAX_BYTES, False))

    def test_status_mapping_drops_body(self):
        # Transient outcomes on the last permitted attempt become RETRY_EXHAUSTED.
        cases = {206: "RETRY_EXHAUSTED", 401: "AUTH_REQUIRED", 403: "ACCESS_DENIED",
                 451: "ACCESS_DENIED", 404: "NOT_FOUND", 429: "RETRY_EXHAUSTED",
                 500: "RETRY_EXHAUSTED", 503: "RETRY_EXHAUSTED", 302: "UNSAFE_METADATA",
                 304: "INVALID_RESPONSE_METADATA"}
        for status, category in cases.items():
            with self.subTest(status=status):
                payload = b"" if status == 304 else b"provider error text"
                retrieval, _ = retrieve(response(status, payload))
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertEqual(retrieval.episode["transport"]["http_status"], status)
                self.assertIsNone(retrieval.body)
                self.assertIsNone(retrieval.episode["transport"]["body_digest"])

    def test_shared_transport_checks_apply(self):
        data = body()
        cases = {
            "RESPONSE_TOO_LARGE": (dict(max_bytes=len(data) - 1), response(payload=data)),
            "INVALID_RESPONSE_METADATA": ({}, response(headers={"Content-Type": "text/html"})),
            "UNSAFE_METADATA": ({}, response(url="https://earthquake.usgs.gov/elsewhere")),
            "RETRY_EXHAUSTED": ({}, response(complete=False)),
        }
        for category, (kwargs, outcome) in cases.items():
            with self.subTest(category=category):
                retrieval, _ = retrieve(outcome, **kwargs)
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertIsNone(retrieval.body)
        mismatch, _ = retrieve(response(headers={"Content-Length": "1"}))
        self.assertEqual(mismatch.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")

    def test_retries_and_exhaustion_are_recorded(self):
        retrieval, transport = retrieve(response(503, b"busy"), response(),
                                        retry_policy=cc.RetryPolicy(max_attempts=2))
        self.assertTrue(retrieval.captured)
        self.assertEqual(retrieval.episode["transport"]["retry_count"], 1)
        self.assertEqual(len(transport.calls), 2)
        exhausted, _ = retrieve(response(503, b"busy"), response(503, b"busy"),
                                retry_policy=cc.RetryPolicy(max_attempts=2))
        self.assertEqual(exhausted.episode["transport"]["category"], "RETRY_EXHAUSTED")
        self.assertEqual(exhausted.episode["result"]["status"], "RETRY_REQUIRED")

    def test_transport_exceptions_and_cancellation(self):
        timed_out, _ = retrieve(TimeoutError())
        self.assertEqual(timed_out.episode["transport"]["category"], "RETRY_EXHAUSTED")
        self.assertIsNone(timed_out.episode["transport"]["http_status"])

        class Cancelled:
            def is_cancelled(self):
                return True
        cancelled, transport = retrieve(cancellation=Cancelled())
        self.assertEqual(cancelled.episode["transport"]["category"], "CANCELLED")
        self.assertEqual((cancelled.episode["transport"]["retry_count"], transport.calls), (0, []))

    def test_locator_is_redacted_and_governance_fixed(self):
        plan = earthquake.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z")[0]
        episode = retrieve(response(), url=plan.query_url)[0].episode
        self.assertEqual(episode["redacted_locator"],
                         "https://earthquake.usgs.gov/fdsnws/event/1/query")
        self.assertEqual(episode["governance"], fetch.GOVERNANCE)
        self.assertEqual(episode["episode_id"],
                         "kfm:source-retrieval-episode:" + episode["spec_hash"][7:31])

    def test_profile_admits_only_usgs_json(self):
        profile = fetch.profile()
        self.assertEqual(profile.allowed_hosts, frozenset({"earthquake.usgs.gov"}))
        self.assertEqual(profile.allowed_media_types, fetch.MEDIA_TYPES)
        self.assertEqual((profile.allowed_ports, profile.max_response_bytes),
                         (frozenset({443}), fetch.MAX_BYTES))

    def test_rejected_inputs(self):
        with self.assertRaises(earthquake.EarthquakeInputError):
            retrieve(response(), url="https://earthquake.usgs.gov/other")
        for code, args, kwargs in (
                ("EMPTY_SUCCESS_UNREPRESENTABLE", (response(204, b""),), {}),
                ("RESPONSE_BOUND", (response(),), dict(max_bytes=fetch.MAX_BYTES + 1)),
                ("SPEC_HASH", (response(),), {})):
            with self.subTest(code=code), self.assertRaises(fetch.FetchInputError) as ctx:
                if code == "SPEC_HASH":
                    clock = Clock()
                    fetch.retrieve(earthquake.live_url(), transport=Transport(clock, *args),
                                   clock=clock, sleeper=Sleeper(clock),
                                   spec_hash=lambda _: "md5:x",
                                   retry_policy=cc.RetryPolicy(max_attempts=1))
                else:
                    retrieve(*args, **kwargs)
            self.assertEqual(ctx.exception.args[0], code)


class AdmissionTests(unittest.TestCase):
    def test_parsed_capture_is_raw_candidate_when_descriptor_resolved(self):
        decision = admit.admit(retrieve(response())[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.provisional_route), (admit.RAW, admit.RAW))
        self.assertEqual(decision.reasons, ())
        self.assertEqual(len(decision.snapshot.events), 1)
        self.assertEqual(decision.snapshot.retrieved_at, "2026-09-22T18:00:00.000Z")
        self.assertEqual((decision.admission, decision.coverage, decision.write_performed),
                         ("NOT_ADMITTED", "NOT_ESTABLISHED", False))
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_parser_rejection_is_quarantine_candidate(self):
        decision = admit.admit(retrieve(response(payload=body(count=5)))[0], descriptor=RESOLVED)
        self.assertEqual(decision.route, admit.QUARANTINE)
        self.assertEqual(decision.reasons, ("PARSE_COUNT_MISMATCH",))
        self.assertIsNone(decision.snapshot)

    def test_uncaptured_episode_is_held_with_contract_reason(self):
        decision = admit.admit(retrieve(response(429, b"slow"))[0], descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.HOLD, ("RETRY_BUDGET_EXHAUSTED",)))
        denied = admit.admit(retrieve(response(403, b"no"))[0], descriptor=RESOLVED)
        self.assertEqual((denied.route, denied.reasons), (admit.HOLD, ("ACCESS_DENIED",)))

    def test_query_limit_flag(self):
        plan = earthquake.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z",
                                          limit=2)[0]
        retrieval = retrieve(response(payload=body(2)), url=plan.query_url)[0]
        decision = admit.admit(retrieval, descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ("QUERY_LIMIT_REACHED",)))

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "usgs")
        for outcome, provisional in ((response(), admit.RAW),
                                     (response(payload=body(count=9)), admit.QUARANTINE)):
            with self.subTest(provisional=provisional):
                decision = admit.admit(retrieve(outcome)[0])
                self.assertEqual((decision.route, decision.provisional_route),
                                 (admit.HOLD, provisional))
                self.assertIn("DESCRIPTOR_RIGHTS_UNRESOLVED", decision.reasons)
                self.assertIn("DESCRIPTOR_ROLE_UNRESOLVED", decision.reasons)

    def test_descriptor_parsing_is_strict(self):
        root = Path(self._testMethodName)
        cases = {"name: usgs\nrole: a\nrights: b\n": ("name", "role", "rights"),
                 "name: usgs\nrole: a\nrole: b\n": (),
                 "name: usgs\nnested:\n  key: v\n": (),
                 "name: usgs\n  role: a\n": (),
                 "name: other\nrole: a\nrights: b\n": ("name", "role", "rights")}
        for text, keys in cases.items():
            with self.subTest(text=text), patch.object(Path, "read_bytes",
                                                       return_value=text.encode()):
                self.assertEqual(tuple(admit.load_descriptor(root)), keys)
        self.assertEqual(admit.descriptor_blockers({"name": "other", "role": "a", "rights": "b"}),
                         ("DESCRIPTOR_INVALID",))
        self.assertEqual(admit.descriptor_blockers({"name": "usgs", "role": "a", "rights": "tbd"}),
                         ("DESCRIPTOR_RIGHTS_UNRESOLVED",))
        oversized = b"name: usgs\n" + b"# pad\n" * admit.MAX_DESCRIPTOR_BYTES
        with patch.object(Path, "read_bytes", return_value=oversized):
            self.assertEqual(admit.load_descriptor(root), {})
        with patch.object(Path, "read_bytes", return_value=b"name: \xff\n"):
            self.assertEqual(admit.load_descriptor(root), {})
        with patch.object(Path, "read_bytes", side_effect=OSError):
            self.assertEqual(admit.load_descriptor(root), {})
        self.assertEqual(admit.descriptor_blockers({}), ("DESCRIPTOR_INVALID",))

    def test_requires_recorded_retrieval(self):
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(retrieve(response())[0], descriptor=RESOLVED)
            admit.admit(retrieve(response(429, b"slow"))[0])


if __name__ == "__main__":
    unittest.main()
