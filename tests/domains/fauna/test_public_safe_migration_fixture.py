"""Deterministic no-network tests for synthetic Fauna migration carriers."""

from __future__ import annotations

import copy
import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from unittest.mock import patch

from tools.validators.domains.fauna.movement.validate_public_safe_migration_fixture import (
    FIXTURE_ROOT,
    Finding,
    main,
    validate_candidate,
    validate_file,
    validate_fixture_manifest,
)


VALID = FIXTURE_ROOT / "valid" / "public_safe_synthetic_route.json"
DEGENERATE = FIXTURE_ROOT / "invalid" / "degenerate_route.json"
EXACT = FIXTURE_ROOT / "invalid" / "exact_track_claim.json"
INSUFFICIENT = FIXTURE_ROOT / "invalid" / "insufficient_positions.json"


def _network_denied(*_args, **_kwargs):
    raise AssertionError("migration fixture validation attempted network access")


class PublicSafeMigrationFixtureTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _network_denied),
            patch.object(socket, "create_connection", _network_denied),
            patch.object(urllib.request, "urlopen", _network_denied),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_public_safe_synthetic_route_passes(self):
        self.assertTrue(validate_file(VALID).ok)

    def test_manifest_replays_exact_inventory(self):
        self.assertTrue(validate_fixture_manifest().ok)

    def test_degenerate_route_fails_closed(self):
        self.assertEqual(
            validate_file(DEGENERATE).findings,
            (
                Finding("geom.route_degenerate", "/geometry/coordinates"),
            ),
        )

    def test_exact_track_and_truth_claims_fail_closed(self):
        self.assertEqual(
            validate_file(EXACT).findings,
            (
                Finding(
                    "claim.individual_tracking_truth_forbidden",
                    "/individual_tracking_truth",
                ),
                Finding("claim.telemetry_truth_forbidden", "/telemetry_truth"),
                Finding(
                    "geom.derivation_method_required",
                    "/geometry/derivation_method",
                ),
                Finding(
                    "geom.public_safe_precision_required",
                    "/geometry/precision_class",
                ),
                Finding("sens.public_safe_required", "/sensitivity_state"),
            ),
        )

    def test_insufficient_route_and_reversed_window_fail_closed(self):
        self.assertEqual(
            validate_file(INSUFFICIENT).findings,
            (
                Finding(
                    "geom.positions_insufficient",
                    "/geometry/coordinates",
                ),
                Finding("time.window_reversed", "/time_scope"),
            ),
        )

    def test_boolean_unbounded_and_oversized_positions_fail_closed(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["geometry"]["coordinates"][1] = [True, 0.0]
        self.assertIn(
            Finding("geom.position_invalid", "/geometry/coordinates/1"),
            validate_candidate(candidate).findings,
        )
        candidate["geometry"]["coordinates"][1] = [181.0, 0.0]
        self.assertIn(
            Finding("geom.position_out_of_bounds", "/geometry/coordinates/1"),
            validate_candidate(candidate).findings,
        )
        oversized = copy.deepcopy(candidate)
        oversized["geometry"]["coordinates"] = [[0.0, 0.0]] * 4097
        self.assertIn(
            Finding("geom.position_limit_exceeded", "/geometry/coordinates"),
            validate_candidate(oversized).findings,
        )

    def test_numeric_boolean_stand_ins_fail_closed(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["fixture_only"] = 1
        candidate["telemetry_truth"] = 0
        candidate["individual_tracking_truth"] = 0
        self.assertEqual(
            validate_candidate(candidate).findings,
            (
                Finding(
                    "claim.individual_tracking_truth_forbidden",
                    "/individual_tracking_truth",
                ),
                Finding("claim.telemetry_truth_forbidden", "/telemetry_truth"),
                Finding("schema.fixture_only_required", "/fixture_only"),
            ),
        )

    def test_oversized_integer_position_fails_closed(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["geometry"]["coordinates"][1] = [10**1000, 0]
        self.assertIn(
            Finding("geom.position_invalid", "/geometry/coordinates/1"),
            validate_candidate(candidate).findings,
        )

    def test_cli_output_is_stable_and_does_not_echo_geometry(self):
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(EXACT)])
        self.assertEqual(return_code, 1)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["scope"], "fauna-public-safe-migration-fixture-v1")
        self.assertNotIn("coordinates", output.getvalue())


if __name__ == "__main__":
    unittest.main()
