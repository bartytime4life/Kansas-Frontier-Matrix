"""Deterministic no-network tests for synthetic Fauna migration carriers."""

from __future__ import annotations

import copy
import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools.validators.domains.fauna.movement import (
    validate_public_safe_migration_fixture as migration_validator,
)
from tools.validators.domains.fauna.movement.validate_public_safe_migration_fixture import (
    FIXTURE_ROOT,
    MAX_INPUT_BYTES,
    Finding,
    main,
    validate_candidate,
    validate_file,
    validate_fixture_manifest,
)


VALID = FIXTURE_ROOT / "valid" / "public_safe_synthetic_route.json"
CONSECUTIVE_DUPLICATE = (
    FIXTURE_ROOT / "invalid" / "consecutive_duplicate_position.json"
)
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

    def test_duplicate_json_members_fail_closed(self):
        payloads = {
            "top-level": '{"route_id":"safe","route_id":"forbidden"}',
            "nested": '{"geometry":{"type":"Point","type":"LineString"}}',
        }
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "candidate.json"
            for name, payload in payloads.items():
                with self.subTest(name=name):
                    path.write_text(payload, encoding="utf-8")
                    self.assertEqual(
                        validate_file(path).findings,
                        (Finding("schema.input_invalid", "/"),),
                    )

    def test_symlinked_and_oversized_inputs_fail_before_read(self):
        with TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            target = temp_root / "target.json"
            target.write_text(VALID.read_text(encoding="utf-8"), encoding="utf-8")
            symlink = temp_root / "symlink.json"
            symlink.symlink_to(target)
            self.assertEqual(
                validate_file(symlink).findings,
                (Finding("schema.input_invalid", "/"),),
            )

            oversized = temp_root / "oversized.json"
            oversized.write_bytes(b" " * (MAX_INPUT_BYTES + 1))
            with patch.object(
                Path,
                "read_text",
                side_effect=AssertionError("oversized candidate was read"),
            ) as candidate_reader:
                self.assertEqual(
                    validate_file(oversized).findings,
                    (Finding("schema.input_invalid", "/"),),
                )
            candidate_reader.assert_not_called()

    def test_manifest_path_escape_fails_before_candidate_read(self):
        with TemporaryDirectory() as temp_dir:
            manifest_path = Path(temp_dir) / "manifest.json"
            path_cases = {
                "traversal": "../outside.json",
                "absolute": str(Path(temp_dir) / "outside.json"),
                "nested": "valid/nested/outside.json",
            }
            for name, candidate_path in path_cases.items():
                with self.subTest(name=name):
                    manifest_path.write_text(
                        json.dumps(
                            {
                                "cases": [
                                    {
                                        "path": candidate_path,
                                        "expected_findings": [],
                                    }
                                ]
                            }
                        ),
                        encoding="utf-8",
                    )
                    with (
                        patch.object(
                            migration_validator,
                            "MANIFEST_PATH",
                            manifest_path,
                        ),
                        patch.object(
                            migration_validator,
                            "validate_file",
                        ) as candidate_reader,
                    ):
                        result = migration_validator.validate_fixture_manifest()
                    self.assertIn(
                        Finding("fixture.path_invalid", "/cases/0/path"),
                        result.findings,
                    )
                    candidate_reader.assert_not_called()

    def test_degenerate_route_fails_closed(self):
        self.assertEqual(
            validate_file(DEGENERATE).findings,
            (
                Finding("geom.route_degenerate", "/geometry/coordinates"),
            ),
        )

    def test_consecutive_duplicate_position_fails_closed(self):
        self.assertEqual(
            validate_file(CONSECUTIVE_DUPLICATE).findings,
            (
                Finding(
                    "geom.consecutive_position_duplicate",
                    "/geometry/coordinates/2",
                ),
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

    def test_semantically_empty_fixture_references_fail_closed(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["route_id"] = "fixture:fauna:migration::"
        candidate["taxon_ref"] = "fixture:taxon:fauna:-:"
        candidate["source_descriptor_ref"] = "fixture:source:fauna:--"
        candidate["evidence_refs"] = ["fixture:evidence:fauna:-:"]
        self.assertEqual(
            validate_candidate(candidate).findings,
            (
                Finding(
                    "evidence.fixture_ref_required",
                    "/evidence_refs/0",
                ),
                Finding("schema.fixture_ref_required", "/route_id"),
                Finding(
                    "schema.fixture_ref_required",
                    "/source_descriptor_ref",
                ),
                Finding("schema.fixture_ref_required", "/taxon_ref"),
            ),
        )

    def test_unicode_fixture_reference_homoglyphs_fail_closed(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["route_id"] = "fixture:fauna:migration:synthetic-α"
        candidate["taxon_ref"] = "fixture:taxon:fauna:synthetic-١"
        candidate["source_descriptor_ref"] = "fixture:source:fauna:synthetic-é"
        candidate["evidence_refs"] = ["fixture:evidence:fauna:synthetic-０"]
        self.assertEqual(
            validate_candidate(candidate).findings,
            (
                Finding(
                    "evidence.fixture_ref_required",
                    "/evidence_refs/0",
                ),
                Finding("schema.fixture_ref_required", "/route_id"),
                Finding(
                    "schema.fixture_ref_required",
                    "/source_descriptor_ref",
                ),
                Finding("schema.fixture_ref_required", "/taxon_ref"),
            ),
        )

    def test_evidence_references_are_bounded_and_duplicate_safe(self):
        candidate = json.loads(VALID.read_text(encoding="utf-8"))
        candidate["evidence_refs"] = [
            "fixture:evidence:fauna:synthetic-duplicate",
            "fixture:evidence:fauna:synthetic-duplicate",
        ]
        self.assertEqual(
            validate_candidate(candidate).findings,
            (
                Finding(
                    "evidence.reference_duplicate",
                    "/evidence_refs/1",
                ),
            ),
        )

        candidate["evidence_refs"] = [
            "fixture:evidence:fauna:over-limit-duplicate"
        ] * 65
        self.assertEqual(
            validate_candidate(candidate).findings,
            (
                Finding(
                    "evidence.reference_limit_exceeded",
                    "/evidence_refs",
                ),
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
