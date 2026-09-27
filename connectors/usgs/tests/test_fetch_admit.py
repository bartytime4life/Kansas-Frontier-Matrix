"""Deterministic synthetic tests for USGS retrieval classification and routing; no network."""
from dataclasses import FrozenInstanceError
from hashlib import sha256
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

SRC = Path(__file__).resolve().parents[1] / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from usgs import admit, earthquake, fetch  # noqa: E402

START, END = "2026-09-22T18:00:00Z", "2026-09-22T18:00:02Z"
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


def classify(status=200, payload=None, headers=None, url=None, **kwargs):
    payload = body() if payload is None and status == 200 else (payload or b"")
    if headers is None:
        headers = (("Content-Type", "application/json"),)
    return fetch.classify_response(source_url=url or earthquake.live_url(), attempted_at=START,
                                   completed_at=END, spec_hash=stub_hash, status=status,
                                   headers=headers, body=payload, **kwargs)


class ClassificationTests(unittest.TestCase):
    def test_success_keeps_body_and_records_identity(self):
        data = body()
        retrieval = classify(payload=data, headers=(
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(data))), ("ETag", '"v1"'),
            ("Last-Modified", "Tue, 22 Sep 2026 17:59:00 GMT")))
        transport = retrieval.episode["transport"]
        self.assertTrue(retrieval.captured)
        self.assertEqual(retrieval.body, data)
        self.assertEqual(transport["category"], "SUCCESS")
        self.assertEqual(transport["body_digest"], "sha256:" + sha256(data).hexdigest())
        self.assertEqual(transport["body_bytes"], len(data))
        self.assertEqual(transport["content_type"], "application/json;charset=utf-8")
        self.assertEqual(transport["last_modified"], "2026-09-22T17:59:00Z")
        self.assertEqual(transport["elapsed_ms"], 2000)
        self.assertEqual(retrieval.episode["result"],
                         {"status": "CAPTURED", "reason_codes": ["RETRIEVAL_BODY_CAPTURED"]})

    def test_status_mapping_drops_body(self):
        cases = {206: "PARTIAL", 401: "AUTH_REQUIRED", 403: "ACCESS_DENIED",
                 451: "ACCESS_DENIED", 404: "NOT_FOUND", 429: "RATE_LIMITED",
                 500: "TRANSPORT_ERROR", 503: "TRANSPORT_ERROR",
                 304: "INVALID_RESPONSE_METADATA", 302: "INVALID_RESPONSE_METADATA"}
        for status, category in cases.items():
            with self.subTest(status=status):
                retrieval = classify(status, b"provider error text")
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertIsNone(retrieval.body)
                self.assertIsNone(retrieval.episode["transport"]["body_digest"])

    def test_success_metadata_failures(self):
        data = body()
        cases = {
            "RESPONSE_TOO_LARGE": dict(payload=data, max_bytes=len(data) - 1),
            "INTEGRITY_MISMATCH": dict(headers=(("Content-Type", "application/json"),
                                                ("Content-Length", "1"))),
            "UNSAFE_METADATA": dict(headers=(("Content-Type", "application/json"),
                                             ("Content-Encoding", "gzip"))),
            "INVALID_RESPONSE_METADATA": dict(headers=(("Content-Type", "text/html"),)),
        }
        for category, kwargs in cases.items():
            with self.subTest(category=category):
                retrieval = classify(**kwargs)
                self.assertEqual(retrieval.episode["transport"]["category"], category)
                self.assertIsNone(retrieval.body)
        for headers in ((), (("Content-Type", "application/json"), ("ETag", "unquoted")),
                        (("Content-Type", "application/json"),
                         ("Last-Modified", "Tue, 22 Sep 2026 19:00:00 GMT")),
                        (("Content-Type", "application/json"), ("Last-Modified", "soon"))):
            with self.subTest(headers=headers):
                self.assertEqual(classify(headers=headers).episode["transport"]["category"],
                                 "INVALID_RESPONSE_METADATA")
        self.assertEqual(classify(payload=b"").episode["transport"]["category"],
                         "INVALID_RESPONSE_METADATA")

    def test_failures_without_response(self):
        for failure, status in (("TIMEOUT", "RETRY_REQUIRED"), ("CANCELLED", "RETRY_REQUIRED"),
                                ("RETRY_EXHAUSTED", "RETRY_REQUIRED"),
                                ("TRANSPORT_ERROR", "ERROR")):
            with self.subTest(failure=failure):
                retrieval = fetch.classify_response(
                    source_url=earthquake.live_url(), attempted_at=START, completed_at=END,
                    spec_hash=stub_hash, failure=failure, retry_count=2)
                self.assertEqual(retrieval.episode["result"]["status"], status)
                self.assertIsNone(retrieval.episode["transport"]["http_status"])

    def test_locator_is_redacted_and_governance_fixed(self):
        plan = earthquake.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z")[0]
        episode = classify(url=plan.query_url).episode
        self.assertEqual(episode["redacted_locator"],
                         "https://earthquake.usgs.gov/fdsnws/event/1/query")
        self.assertEqual(episode["governance"], fetch.GOVERNANCE)
        self.assertFalse(episode["governance"]["network_attempted"])
        self.assertEqual(episode["episode_id"],
                         "kfm:source-retrieval-episode:" + episode["spec_hash"][7:31])

    def test_rejected_inputs(self):
        cases = {
            "SOURCE_URL": dict(url="https://example.org/feed.geojson"),
            "EMPTY_SUCCESS_UNREPRESENTABLE": dict(status=204, payload=b""),
            "DUPLICATE_HEADER": dict(headers=(("ETag", '"a"'), ("etag", '"b"'))),
            "HEADERS": dict(headers=(("Content-Type",),)),
            "RESPONSE_SHAPE": dict(status=99),
            "RETRY_COUNT": dict(retry_count=21),
            "RESPONSE_BOUND": dict(max_bytes=fetch.MAX_BYTES + 1),
            "FAILURE_SHAPE": dict(failure="TIMEOUT"),
        }
        for code, kwargs in cases.items():
            with self.subTest(code=code), self.assertRaises(earthquake.EarthquakeInputError
                                                            if code == "SOURCE_URL"
                                                            else fetch.FetchInputError) as ctx:
                classify(**kwargs)
            self.assertEqual(ctx.exception.args[0], code)
        for start, end in ((END, START), ("2026-09-22T18:00:00", END),
                           (START, "2026-09-22T20:00:01Z")):
            with self.subTest(start=start, end=end), self.assertRaises(fetch.FetchInputError):
                fetch.classify_response(source_url=earthquake.live_url(), attempted_at=start,
                                        completed_at=end, spec_hash=stub_hash, status=200,
                                        body=body())
        with self.assertRaises(fetch.FetchInputError) as ctx:
            fetch.classify_response(source_url=earthquake.live_url(), attempted_at=START,
                                    completed_at=END, spec_hash=lambda _: "md5:x",
                                    status=200, body=body(),
                                    headers=(("Content-Type", "application/json"),))
        self.assertEqual(ctx.exception.args[0], "SPEC_HASH")


class AdmissionTests(unittest.TestCase):
    def test_parsed_capture_is_raw_candidate_when_descriptor_resolved(self):
        decision = admit.admit(classify(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.provisional_route), (admit.RAW, admit.RAW))
        self.assertEqual(decision.reasons, ())
        self.assertEqual(len(decision.snapshot.events), 1)
        self.assertEqual(decision.snapshot.retrieved_at, "2026-09-22T18:00:02.000Z")
        self.assertEqual((decision.admission, decision.coverage, decision.write_performed),
                         ("NOT_ADMITTED", "NOT_ESTABLISHED", False))
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_parser_rejection_is_quarantine_candidate(self):
        decision = admit.admit(classify(payload=body(count=5)), descriptor=RESOLVED)
        self.assertEqual(decision.route, admit.QUARANTINE)
        self.assertEqual(decision.reasons, ("PARSE_COUNT_MISMATCH",))
        self.assertIsNone(decision.snapshot)

    def test_uncaptured_episode_is_held_with_contract_reason(self):
        decision = admit.admit(classify(429, b""), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.HOLD, ("SOURCE_RATE_LIMITED",)))

    def test_query_limit_flag(self):
        plan = earthquake.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z",
                                          limit=2)[0]
        decision = admit.admit(classify(url=plan.query_url, payload=body(2)), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ("QUERY_LIMIT_REACHED",)))

    def test_checked_in_descriptor_holds_every_route(self):
        descriptor = admit.load_descriptor()
        self.assertEqual(descriptor.get("name"), "usgs")
        for retrieval, provisional in ((classify(), admit.RAW),
                                       (classify(payload=body(count=9)), admit.QUARANTINE)):
            with self.subTest(provisional=provisional):
                decision = admit.admit(retrieval)
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

    def test_requires_classified_retrieval(self):
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})


class NoNetworkTests(unittest.TestCase):
    def test_classification_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(classify(), descriptor=RESOLVED)
            admit.admit(classify(429, b""))


if __name__ == "__main__":
    unittest.main()
