"""Deterministic no-network tests for the Fauna public-safe range carrier."""

from __future__ import annotations

import copy
import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.fauna.range.validate_public_safe_range_fixture import (
    FIXTURE_ROOT,
    Finding,
    main,
    validate_candidate,
    validate_file,
    validate_fixture_manifest,
)


VALID_FIXTURE = FIXTURE_ROOT / "valid" / "public_safe_synthetic_range.json"
EXACT_INVALID = FIXTURE_ROOT / "invalid" / "exact_occurrence_claim.json"
OPEN_RING_INVALID = FIXTURE_ROOT / "invalid" / "open_ring.json"


def _network_denied(*_args, **_kwargs):
    raise AssertionError("range fixture validation attempted network access")


class PublicSafeRangeFixtureTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _network_denied),
            patch.object(socket, "create_connection", _network_denied),
            patch.object(urllib.request, "urlopen", _network_denied),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_public_safe_synthetic_range_passes(self):
        self.assertTrue(validate_file(VALID_FIXTURE).ok)

    def test_manifest_replays_exact_inventory(self):
        self.assertTrue(validate_fixture_manifest().ok)
        actual = sorted(
            str(path.relative_to(FIXTURE_ROOT))
            for folder in (FIXTURE_ROOT / "valid", FIXTURE_ROOT / "invalid")
            for path in folder.glob("*.json")
        )
        self.assertEqual(
            actual,
            [
                "invalid/exact_occurrence_claim.json",
                "invalid/open_ring.json",
                "valid/public_safe_synthetic_range.json",
            ],
        )

    def test_exact_geometry_and_occurrence_truth_fail_closed(self):
        self.assertEqual(
            validate_file(EXACT_INVALID).findings,
            (
                Finding("claim.occurrence_truth_forbidden", "/occurrence_truth"),
                Finding("geom.derivation_method_required", "/geometry/derivation_method"),
                Finding(
                    "geom.public_safe_precision_required",
                    "/geometry/precision_class",
                ),
                Finding("sens.public_safe_required", "/sensitivity_state"),
            ),
        )

    def test_open_and_out_of_bounds_rings_fail_closed(self):
        self.assertEqual(
            validate_file(OPEN_RING_INVALID).findings,
            (Finding("geom.ring_not_closed", "/geometry/coordinates/0"),),
        )

        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["geometry"]["coordinates"][0][1] = [181.0, 0.0]
        findings = validate_candidate(candidate).findings
        self.assertIn(
            Finding("geom.position_out_of_bounds", "/geometry/coordinates/0/1"),
            findings,
        )

    def test_boolean_and_unbounded_geometry_values_fail_closed(self):
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["geometry"]["coordinates"][0][1] = [True, 0.0]
        findings = validate_candidate(candidate).findings
        self.assertIn(
            Finding("geom.position_invalid", "/geometry/coordinates/0/1"),
            findings,
        )

        too_many_rings = copy.deepcopy(candidate)
        ring = [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]]
        too_many_rings["geometry"]["coordinates"] = [ring] * 17
        self.assertIn(
            Finding("geom.ring_limit_exceeded", "/geometry/coordinates"),
            validate_candidate(too_many_rings).findings,
        )

    def test_cli_output_is_stable_and_does_not_echo_geometry(self):
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(EXACT_INVALID)])
        self.assertEqual(return_code, 1)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["outcome"], "ERROR")
        self.assertEqual(payload["scope"], "fauna-public-safe-range-fixture-v1")
        self.assertNotIn("coordinates", output.getvalue())


if __name__ == "__main__":
    unittest.main()
