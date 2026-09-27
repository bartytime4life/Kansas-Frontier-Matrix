"""Deterministic synthetic tests for NOAA retrieval recording and routing.

No NOAA access, rights review, alert relay, or admission claim. Imports connectors_core
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
for path in (HERE, ROOT / "connectors/noaa/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from connectors_core.core import redact_url  # noqa: E402
from noaa import admit, fetch, nws_alerts, storm_events, uscrn_hourly  # noqa: E402
import test_nws_alerts as nws_fixtures  # noqa: E402
import test_storm_events as storm_fixtures  # noqa: E402
import test_uscrn_hourly as uscrn_fixtures  # noqa: E402

RESOLVED = {"name": "noaa", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
STORM_URL = storm_events.details_url(2020, "20260915")
USCRN_URL = uscrn_hourly.hourly_url(2023, "KS_Synthetic_1_N")
NWS_URL = nws_alerts.alerts_url("KS")
STORM_BODY = storm_fixtures.gz([storm_fixtures.row()])
USCRN_BODY = (uscrn_fixtures.line(1) + "\n" + uscrn_fixtures.line(2) + "\n").encode()
NWS_BODY = nws_fixtures.collection([nws_fixtures.alert()])


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


def response(status=200, payload=b"", media="application/gzip", extra=None):
    headers = {"Content-Type": media, "Content-Length": str(len(payload)), **(extra or {})}
    return ct.TransportResponse(status_code=status, headers=headers,
                                body_chunks=(payload,) if payload else ())


def effects(*outcomes):
    clock = Clock()
    return dict(transport=Transport(clock, *outcomes), clock=clock, sleeper=Sleeper(clock),
                spec_hash=stub_hash, retry_policy=cc.RetryPolicy(max_attempts=1))


def storm(payload=STORM_BODY, url=STORM_URL, status=200, media="application/gzip"):
    return fetch.retrieve_storm_events(url, **effects(response(status, payload, media)))


def uscrn(payload=USCRN_BODY, url=USCRN_URL, status=200):
    return fetch.retrieve_uscrn_hourly(url, **effects(response(status, payload,
                                                               "text/plain; charset=us-ascii")))


def nws(payload=NWS_BODY, url=NWS_URL, status=200, extra=None):
    return fetch.retrieve_nws_alerts(url, **effects(response(status, payload,
                                                             "application/geo+json", extra)))


class RetrievalTests(unittest.TestCase):
    def test_each_product_records_its_own_identity(self):
        for retrieval, source_id, profile_ref in (
                (storm(), fetch.STORM_SOURCE_ID, fetch.STORM_RETRIEVAL_PROFILE),
                (uscrn(), fetch.USCRN_SOURCE_ID, fetch.USCRN_RETRIEVAL_PROFILE),
                (nws(), fetch.NWS_SOURCE_ID, fetch.NWS_RETRIEVAL_PROFILE)):
            episode = retrieval.episode
            with self.subTest(source_id=source_id):
                self.assertTrue(retrieval.captured)
                self.assertEqual((episode["source_id"], episode["retrieval_profile_ref"]),
                                 (source_id, profile_ref))
                self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)
        self.assertEqual(nws().episode["redacted_locator"], "https://api.weather.gov/alerts/active")

    def test_request_is_get_with_no_redirects_and_profile_budget(self):
        kwargs = effects(response(200, STORM_BODY))
        fetch.retrieve_storm_events(STORM_URL, **kwargs)
        request, _, budget, redirects = kwargs["transport"].calls[0]
        self.assertEqual((request.url, budget, redirects),
                         (STORM_URL, fetch.STORM_MAX_BYTES, False))
        self.assertEqual(dict(request.headers), {"accept": "application/gzip"})

    def test_x_gzip_is_admitted_and_other_media_types_are_blocked(self):
        self.assertTrue(storm(media="application/x-gzip").captured)
        blocked = storm(media="text/html")
        self.assertEqual(blocked.episode["transport"]["category"], "INVALID_RESPONSE_METADATA")
        self.assertIsNone(blocked.body)

    def test_only_planner_canonical_urls(self):
        cases = (
            (storm, storm_events.StormEventsInputError, "SOURCE_URL",
             (STORM_URL.replace("www.ncei.noaa.gov", "example.org"),
              STORM_URL + "?x=1", STORM_URL.replace("_c20260915", "_c2026091"))),
            (storm, storm_events.StormEventsInputError, "INTEGER_BOUND",
             (STORM_URL.replace("_d2020_c20260915", "_d1949_c20260915"),)),
            (uscrn, uscrn_hourly.UscrnInputError, "SOURCE_URL",
             (USCRN_URL.replace("/2023/", "/2022/"), USCRN_URL + "#frag")),
            (uscrn, uscrn_hourly.UscrnInputError, "YEAR",
             (USCRN_URL.replace("2023", "1999"),)),
            (nws, nws_alerts.NwsInputError, "SOURCE_URL",
             (NWS_URL.replace("area=KS", "area=KS&limit=5"),
              NWS_URL.replace("api.weather.gov", "example.org"))),
            (nws, nws_alerts.NwsInputError, "SOURCE_URL_SCOPE",
             (NWS_URL.replace("area=KS", "area=%4BS"),)),
        )
        for run, error, code, urls in cases:
            for url in urls:
                with self.subTest(url=url), self.assertRaises(error) as ctx:
                    run(url=url)
                self.assertEqual(ctx.exception.args[0], code)
        self.assertTrue(nws(url=nws_alerts.alerts_url("KS", active=False)).captured)

    def test_profiles_are_bounded(self):
        for build, limit in ((fetch.storm_profile, fetch.STORM_MAX_BYTES),
                             (fetch.uscrn_profile, fetch.USCRN_MAX_BYTES),
                             (fetch.nws_profile, fetch.NWS_MAX_BYTES)):
            with self.subTest(build=build.__name__), self.assertRaises(fetch.FetchInputError):
                build(limit + 1)
        self.assertEqual(fetch.nws_profile().allowed_hosts, frozenset({"api.weather.gov"}))
        self.assertEqual(fetch.uscrn_profile().allowed_media_types, frozenset({"text/plain"}))


class AdmissionTests(unittest.TestCase):
    def test_parsed_products_route_raw(self):
        decision = admit.admit(storm(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(len(decision.details_file.events), 1)
        self.assertIsNone(decision.station_year)
        decision = admit.admit(uscrn(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(len(decision.station_year.records), 2)
        decision = admit.admit(nws(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(decision.alerts.alerts[0].freshness_as_of,
                         decision.alerts.retrieved_at)
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.HOLD

    def test_product_flags(self):
        bad_damage = storm_fixtures.gz([storm_fixtures.row(DAMAGE_PROPERTY="lots")])
        self.assertEqual(admit.admit(storm(bad_damage), descriptor=RESOLVED).reasons,
                         ("RECORD_QUARANTINE_CANDIDATES",))
        gap = (uscrn_fixtures.line(1) + "\n" + uscrn_fixtures.line(3) + "\n").encode()
        self.assertEqual(admit.admit(uscrn(gap), descriptor=RESOLVED).reasons,
                         ("MISSING_HOURS_PRESENT",))
        partial = nws_fixtures.collection([nws_fixtures.alert(status="Test")],
                                          pagination={"next": NWS_URL + "&cursor=x"})
        self.assertEqual(admit.admit(nws(partial), descriptor=RESOLVED).reasons,
                         ("RECORD_QUARANTINE_CANDIDATES", "PARTIAL_COLLECTION_MORE_PAGES"))
        seven_day = nws(url=nws_alerts.alerts_url("KS", active=False))
        self.assertEqual(admit.admit(seven_day, descriptor=RESOLVED).reasons,
                         ("SEVEN_DAY_WINDOW_NOT_ARCHIVE",))

    def test_parser_rejection_is_quarantine_candidate(self):
        impossible_date = (uscrn_fixtures.line(1, date="20231301") + "\n").encode()
        enum_object = nws_fixtures.collection([nws_fixtures.alert(status={"x": 1})])
        for retrieval, code in ((storm(b"not gzip"), "PARSE_NOT_GZIP"),
                                (uscrn(b"1 2 3\n"), "PARSE_SCHEMA_DRIFT"),
                                (uscrn(impossible_date), "PARSE_TIME_FORMAT"),
                                (nws(b"{}"), "PARSE_COLLECTION_SHAPE"),
                                (nws(enum_object), "PARSE_ALERT_ENUM")):
            with self.subTest(code=code):
                decision = admit.admit(retrieval, descriptor=RESOLVED)
                self.assertEqual((decision.route, decision.reasons), (admit.QUARANTINE, (code,)))
                self.assertIsNone(decision.details_file or decision.station_year
                                  or decision.alerts)

    def test_recorded_nws_cache_headers_reach_the_parser(self):
        retrieval = nws(extra={"ETag": '"v7"', "Last-Modified": "Fri, 01 May 2026 11:59:00 GMT",
                               "Cache-Control": "public, max-age=30"})
        decision = admit.admit(retrieval, descriptor=RESOLVED)
        # Cache-Control is not a SourceRetrievalEpisode field, so it cannot survive recording.
        self.assertEqual(decision.alerts.cache_headers,
                         (("Last-Modified", "Fri, 01 May 2026 11:59:00 GMT"), ("ETag", '"v7"')))
        self.assertEqual(admit.admit(nws(), descriptor=RESOLVED).alerts.cache_headers, ())
        # A reconstructed episode with a malformed recorded Last-Modified is refused, bounded.
        for bad in ("yesterday", "2026-05-01T11:59:00", "2026-05-01T11:59:00+02:00",
                    "2026-13-01T11:59:00Z", 5):
            episode = retrieval.episode
            episode["transport"]["last_modified"] = bad
            forged = fetch.Retrieval(retrieval.source_url, json.dumps(episode), retrieval.body)
            with self.subTest(bad=bad), self.assertRaises(fetch.FetchInputError) as ctx:
                admit.admit(forged, descriptor=RESOLVED)
            self.assertEqual(ctx.exception.args[0], "EPISODE_LAST_MODIFIED")

    def test_uncaptured_retrievals_are_held(self):
        for retrieval in (storm(status=404, payload=b"no"), uscrn(status=403, payload=b"no"),
                          nws(status=500, payload=b"no")):
            with self.subTest(source=retrieval.episode["source_id"]):
                decision = admit.admit(retrieval, descriptor=RESOLVED)
                self.assertEqual(decision.route, admit.HOLD)
                self.assertEqual(decision.reasons,
                                 tuple(retrieval.episode["result"]["reason_codes"]))

    def test_checked_in_descriptor_holds_every_route(self):
        self.assertEqual(admit.load_descriptor().get("name"), "noaa")
        for retrieval in (storm(), uscrn(), nws()):
            decision = admit.admit(retrieval)
            self.assertEqual(decision.route, admit.HOLD)
            self.assertEqual(decision.provisional_route, admit.RAW)
            self.assertEqual(decision.reasons[-2:], ("DESCRIPTOR_ROLE_UNRESOLVED",
                                                     "DESCRIPTOR_RIGHTS_UNRESOLVED"))

    def test_episode_from_another_source_is_refused(self):
        good = storm()
        base = good.episode
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": fetch.NWS_RETRIEVAL_PROFILE},
                         {"source_id": fetch.USCRN_SOURCE_ID,
                          "source_descriptor_ref": f"kfm://source/{fetch.USCRN_SOURCE_ID}"},
                         {"source_id": [fetch.STORM_SOURCE_ID]}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url, json.dumps({**base, **override}),
                                         good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        for good, url, error, code in (
                (storm(), STORM_URL.replace("www.ncei.noaa.gov", "evil.example"),
                 storm_events.StormEventsInputError, "SOURCE_URL"),
                (storm(status=404, payload=b"no"), STORM_URL.replace("d2020", "d1949"),
                 storm_events.StormEventsInputError, "INTEGER_BOUND"),
                (uscrn(), USCRN_URL.replace("/2023/", "/2022/"),
                 uscrn_hourly.UscrnInputError, "SOURCE_URL"),
                (nws(), NWS_URL.replace("area=KS", "area=%4BS"),
                 nws_alerts.NwsInputError, "SOURCE_URL_SCOPE")):
            episode = {**good.episode, "redacted_locator": redact_url(url)}
            forged = fetch.Retrieval(url, json.dumps(episode), good.body)
            with self.subTest(url=url), self.assertRaises(error) as ctx:
                admit.admit(forged, descriptor=RESOLVED)
            self.assertEqual(ctx.exception.args[0], code)


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            for retrieval in (storm(), uscrn(), nws()):
                admit.admit(retrieval, descriptor=RESOLVED)


if __name__ == "__main__":
    unittest.main()
