"""Deterministic synthetic tests for Census ACS/TIGER retrieval recording and routing.

No Census access, rights review, or admission claim. Imports connectors_core from
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
for path in (HERE, ROOT / "connectors/census/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from connectors_core import core as cc  # noqa: E402
from connectors_core import retrieval_episode  # noqa: E402
from connectors_core import transport as ct  # noqa: E402
from census import acs_api, admit, fetch, tiger_package  # noqa: E402
import test_acs_api as acs_fixtures  # noqa: E402
import test_tiger_package as tiger_fixtures  # noqa: E402

RESOLVED = {"name": "census", "role": "synthetic-role", "rights": "synthetic-rights",
            "sensitivity_floor": "public"}
UNRESOLVED = {"name": "census", "role": "TBD", "rights": "TBD", "sensitivity_floor": "public"}
ACS_URL = acs_fixtures.URL
TIGER_NAME = "tl_2025_20_tract.zip"
TIGER_BODY = tiger_fixtures.package(TIGER_NAME[:-4])
TIGER_URL = f"https://www2.census.gov/geo/tiger/TIGER2025/TRACT/{TIGER_NAME}"
MANIFEST = {"inventory": {"packages": [
    {**tiger_fixtures.entry_for(TIGER_NAME, TIGER_BODY, "TRACT"), "source_url": TIGER_URL}]}}


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


def acs_rows(*rows):
    return acs_fixtures.body(list(rows) or [["Synthetic County, Kansas", "100", "5", "20", "001"]])


def response(status=200, payload=b"", media="application/json"):
    headers = {"Content-Type": media, "Content-Length": str(len(payload))}
    return ct.TransportResponse(status_code=status, headers=headers,
                                body_chunks=(payload,) if payload else ())


def effects(*outcomes):
    clock = Clock()
    return dict(transport=Transport(clock, *outcomes), clock=clock, sleeper=Sleeper(clock),
                spec_hash=stub_hash, retry_policy=cc.RetryPolicy(max_attempts=1))


def acs(payload=None, url=ACS_URL, status=200):
    return fetch.retrieve_acs(url, **effects(response(status, acs_rows() if payload is None
                                                      else payload)))


def tiger(payload=TIGER_BODY, manifest=MANIFEST, status=200):
    kwargs = effects(response(status, payload, "application/zip"))
    return fetch.retrieve_tiger(TIGER_NAME, manifest=manifest, **kwargs), kwargs["transport"]


class AcsRetrievalTests(unittest.TestCase):
    def test_acs_episode(self):
        retrieval = acs()
        episode = retrieval.episode
        self.assertTrue(retrieval.captured)
        self.assertEqual((episode["source_id"], episode["retrieval_profile_ref"]),
                         (fetch.ACS_SOURCE_ID, fetch.ACS_RETRIEVAL_PROFILE))
        self.assertEqual(episode["redacted_locator"], "https://api.census.gov/data/2023/acs/acs5")
        self.assertEqual(episode["governance"], retrieval_episode.GOVERNANCE)

    def test_only_planner_canonical_acs_urls(self):
        base = ACS_URL.split("?")[0] + "?"
        cases = {
            "API_KEY_IN_URL": (ACS_URL + "&key=secret",),
            "SOURCE_URL": (ACS_URL.replace("api.census.gov", "example.org"),
                           ACS_URL.replace("/acs/acs5?", "/dec/pl?")),
            "SOURCE_URL_SCOPE": (
                # Reordered parameters and an unencoded equivalent of the planner URL.
                base + "for=county%3A%2A&get=NAME%2CB01001_001E%2CB01001_001M&in=state%3A20",
                ACS_URL.replace("%3A", ":").replace("%2C", ","),
            ),
        }
        for code, urls in cases.items():
            for url in urls:
                with self.subTest(url=url), self.assertRaises(acs_api.AcsInputError) as ctx:
                    acs(url=url)
                self.assertEqual(ctx.exception.args[0], code)
        unpaired = acs_api.acs_url(2023, "acs/acs5", ("NAME", "B01001_001E"), "county",
                                   pair_moe=False)
        self.assertEqual(acs(url=unpaired, payload=acs_fixtures.body(
            [["Synthetic County, Kansas", "100", "20", "001"]],
            header=["NAME", "B01001_001E", "state", "county"])).source_url, unpaired)

    def test_acs_profile(self):
        profile = fetch.acs_profile()
        self.assertEqual(profile.allowed_hosts, frozenset({"api.census.gov"}))
        self.assertEqual(profile.allowed_media_types, frozenset({"application/json"}))
        with self.assertRaises(fetch.FetchInputError):
            fetch.acs_profile(fetch.ACS_MAX_BYTES + 1)


class TigerRetrievalTests(unittest.TestCase):
    def test_manifest_pins_url_budget_and_digest(self):
        retrieval, transport = tiger()
        request, timeout, budget, redirects = transport.calls[0]
        self.assertEqual((request.url, budget, redirects), (TIGER_URL, len(TIGER_BODY), False))
        self.assertEqual(request.expected_digest, "sha256:" + sha256(TIGER_BODY).hexdigest())
        self.assertEqual(retrieval.episode["source_id"], fetch.TIGER_SOURCE_ID)
        self.assertEqual(retrieval.body, TIGER_BODY)

    def test_digest_mismatch_is_integrity_episode(self):
        tampered = bytearray(TIGER_BODY)
        tampered[-1] ^= 1
        retrieval, _ = tiger(payload=bytes(tampered))
        self.assertEqual(retrieval.episode["transport"]["category"], "INTEGRITY_MISMATCH")
        self.assertIsNone(retrieval.body)

    def test_packages_outside_manifest_or_archive_are_refused(self):
        with self.assertRaises(tiger_package.TigerPackageError) as ctx:
            fetch.tiger_entry("tl_2025_20_county.zip", MANIFEST)
        self.assertEqual(ctx.exception.args[0], "NOT_IN_MANIFEST")
        for override in ({"source_url": "https://example.org/" + TIGER_NAME},
                         {"source_url": TIGER_URL.replace("TRACT/", "COUNTY/")},
                         {"sha256": "not-a-digest"}, {"sha256": "a" * 63}):
            with self.subTest(override=override), self.assertRaises(
                    tiger_package.TigerPackageError):
                entry = {**MANIFEST["inventory"]["packages"][0], **override}
                fetch.tiger_entry(TIGER_NAME, {"inventory": {"packages": [entry]}})

    def test_committed_manifest_entries_are_accepted(self):
        manifest = tiger_package.load_manifest()
        for entry in manifest["inventory"]["packages"]:
            with self.subTest(file_name=entry["file_name"]):
                self.assertIs(fetch.tiger_entry(entry["file_name"], manifest), entry)


# Source role is product-level; a product without a role in admit.PRODUCT_ROLES holds.
PRODUCT_HOLD = ("PRODUCT_ROLE_UNRESOLVED",)


def product_hold(retrieval):
    return () if retrieval.episode["source_id"] in admit.PRODUCT_ROLES else PRODUCT_HOLD


class AdmissionTests(unittest.TestCase):
    def test_acs_table_routes_raw_with_flags(self):
        decision = admit.admit(acs(), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons), (admit.RAW, ()))
        self.assertEqual(len(decision.table.rows), 1)
        self.assertIsNone(decision.package)
        flagged = admit.admit(acs(acs_rows(["Synthetic County, Kansas", "-5", "1",
                                            "20", "001"])), descriptor=RESOLVED)
        self.assertIn("RECORD_QUARANTINE_CANDIDATES", flagged.reasons)
        with self.assertRaises(FrozenInstanceError):
            decision.route = admit.RAW

    def test_acs_rejection_is_quarantine_candidate(self):
        decision = admit.admit(acs(acs_rows(["Synthetic County, Missouri", "100", "5", "29",
                                             "001"])), descriptor=RESOLVED)
        self.assertEqual((decision.route, decision.reasons),
                         (admit.QUARANTINE, ("PARSE_STATE_SCOPE_MISMATCH",)))

    def test_tiger_package_keeps_inspector_route(self):
        decision = admit.admit(tiger()[0], descriptor=RESOLVED, manifest=MANIFEST)
        self.assertEqual(decision.source_id, fetch.TIGER_SOURCE_ID)
        self.assertEqual(decision.route, decision.package.route)
        self.assertEqual(decision.reasons, decision.package.reasons)
        self.assertEqual(decision.source_role, "administrative")

    def test_tiger_quarantine_route_and_reasons_pass_through(self):
        body = tiger_fixtures.package(TIGER_NAME[:-4], flag=b"*")
        manifest = {"inventory": {"packages": [
            {**tiger_fixtures.entry_for(TIGER_NAME, body, "TRACT"), "source_url": TIGER_URL}]}}
        decision = admit.admit(tiger(payload=body, manifest=manifest)[0], descriptor=RESOLVED,
                               manifest=manifest)
        self.assertEqual(decision.route, admit.QUARANTINE)
        self.assertIn("DELETED_RECORDS_PRESENT", decision.reasons)

    def test_uncaptured_retrievals_are_held(self):
        for retrieval in (acs(status=403, payload=b"no"), tiger(status=404, payload=b"no")[0],
                          tiger(payload=TIGER_BODY[:-1] + b"x")[0]):
            with self.subTest(source=retrieval.episode["source_id"],
                              category=retrieval.episode["transport"]["category"]):
                decision = admit.admit(retrieval, descriptor=RESOLVED, manifest=MANIFEST)
                self.assertEqual(decision.route, admit.HOLD)
                self.assertEqual(decision.reasons, tuple(
                    retrieval.episode["result"]["reason_codes"]) + product_hold(retrieval))

    def test_checked_in_descriptor_releases_candidate_routes(self):
        descriptor = admit.load_descriptor()
        self.assertEqual((descriptor.get("name"), descriptor.get("role"), descriptor.get("rights")),
                         ("census", "aggregate", "public-domain-us-government-work"))
        self.assertEqual(admit.descriptor_blockers(descriptor), ())
        self.assertEqual(admit.PRODUCT_ROLES, {fetch.ACS_SOURCE_ID: "aggregate",
                                               fetch.TIGER_SOURCE_ID: "administrative"})
        for retrieval in (acs(), tiger()[0]):
            decision = admit.admit(retrieval, manifest=MANIFEST)
            self.assertEqual(decision.route, decision.provisional_route)
            self.assertNotEqual(decision.route, admit.HOLD)
            self.assertFalse([r for r in decision.reasons if r.startswith("DESCRIPTOR_")
                              or r == "PRODUCT_ROLE_UNRESOLVED"])
            self.assertEqual(decision.source_role,
                             admit.PRODUCT_ROLES[retrieval.episode["source_id"]])
            held = admit.admit(retrieval, manifest=MANIFEST, descriptor=UNRESOLVED)
            self.assertEqual(held.reasons[-2:], ("DESCRIPTOR_ROLE_UNRESOLVED",
                                                 "DESCRIPTOR_RIGHTS_UNRESOLVED"))

    def test_product_without_a_role_holds(self):
        for retrieval in (acs(), tiger()[0]):
            source = retrieval.episode["source_id"]
            roles = {key: value for key, value in admit.PRODUCT_ROLES.items() if key != source}
            with self.subTest(source=source), patch.object(admit, "PRODUCT_ROLES", roles):
                decision = admit.admit(retrieval, descriptor=RESOLVED, manifest=MANIFEST)
                self.assertEqual((decision.route, decision.reasons[-1], decision.source_role),
                                 (admit.HOLD, "PRODUCT_ROLE_UNRESOLVED", None))

    def test_episode_from_another_source_is_refused(self):
        good = acs()
        base = good.episode
        for override in ({"source_id": "other.source",
                          "source_descriptor_ref": "kfm://source/other.source"},
                         {"retrieval_profile_ref": fetch.TIGER_RETRIEVAL_PROFILE},
                         {"source_id": fetch.TIGER_SOURCE_ID,
                          "source_descriptor_ref": f"kfm://source/{fetch.TIGER_SOURCE_ID}"},
                         {"source_id": [fetch.ACS_SOURCE_ID]}):
            with self.subTest(override=override):
                forged = fetch.Retrieval(good.source_url, json.dumps({**base, **override}),
                                         good.body)
                with self.assertRaises(fetch.FetchInputError) as ctx:
                    admit.admit(forged, descriptor=RESOLVED)
                self.assertEqual(ctx.exception.args[0], "EPISODE_SOURCE_MISMATCH")
        with self.assertRaises(TypeError):
            admit.admit({"episode": {}})

    def test_reconstructed_episode_with_non_planner_url_is_refused(self):
        from connectors_core.core import redact_url
        reordered = (ACS_URL.split("?")[0] + "?for=county%3A%2A&get=NAME%2CB01001_001E"
                     "%2CB01001_001M&in=state%3A20")
        evil_tiger = TIGER_URL.replace("www2.census.gov", "evil.example")
        for good, url, error, code in (
                (acs(), reordered, acs_api.AcsInputError, "SOURCE_URL_SCOPE"),
                (tiger()[0], evil_tiger, tiger_package.TigerPackageError, "SOURCE_URL_SCOPE"),
                (tiger(status=404, payload=b"no")[0], evil_tiger,
                 tiger_package.TigerPackageError, "SOURCE_URL_SCOPE"),
                (tiger()[0], TIGER_URL.replace("tl_2025_20_tract", "tl_2025_20_county"),
                 tiger_package.TigerPackageError, "NOT_IN_MANIFEST")):
            episode = {**good.episode, "redacted_locator": redact_url(url)}
            forged = fetch.Retrieval(url, json.dumps(episode), good.body)
            with self.subTest(url=url), self.assertRaises(error) as ctx:
                admit.admit(forged, descriptor=RESOLVED, manifest=MANIFEST)
            self.assertEqual(ctx.exception.args[0], code)


class NoNetworkTests(unittest.TestCase):
    def test_recording_and_routing_open_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            admit.admit(acs(), descriptor=RESOLVED)
            admit.admit(tiger()[0], descriptor=RESOLVED, manifest=MANIFEST)


if __name__ == "__main__":
    unittest.main()
