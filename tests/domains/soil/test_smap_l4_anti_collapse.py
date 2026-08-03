#!/usr/bin/env python3
"""Conformance tests for the frozen synthetic SMAP L4 fixture profile."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES  # noqa: E402
from tools.validators.domains.soil.moisture import validate_smap_l4_fixture as validator  # noqa: E402

FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "soil" / "soil_moisture" / "smap_l4"
VALID_ROOT = FIXTURE_ROOT / "valid"
INVALID_ROOT = FIXTURE_ROOT / "invalid"
VALID_NAMES = {"surface_nrt.json", "root_zone_standard_quality.json"}
INVALID_NAMES = {
    "station_support.json",
    "raw_observation.json",
    "surface_root_zone_collapse.json",
    "missing_grid_resolution.json",
    "missing_uncertainty.json",
    "nrt_cadence_collapse.json",
    "in_situ_merge.json",
    "released_candidate.json",
}


def load_surface() -> dict[str, object]:
    return json.loads((VALID_ROOT / "surface_nrt.json").read_text(encoding="utf-8"))


def finding_pairs(candidate: object) -> list[tuple[str, str]]:
    return [(finding.code, finding.path) for finding in validator.validate_candidate(candidate)]


def reverse_objects(value: object) -> object:
    if isinstance(value, dict):
        return {key: reverse_objects(child) for key, child in reversed(list(value.items()))}
    if isinstance(value, list):
        return [reverse_objects(child) for child in value]
    return value


class SmapL4AntiCollapseTests(unittest.TestCase):
    maxDiff = None

    def test_fixture_inventory_is_closed(self) -> None:
        valid = {path.name for path in VALID_ROOT.glob("*.json")}
        invalid = {path.name for path in INVALID_ROOT.glob("*.json")}
        sidecars = {path.name for path in INVALID_ROOT.glob("*.expected_error.txt")}
        self.assertEqual(VALID_NAMES, valid)
        self.assertEqual(INVALID_NAMES, invalid)
        self.assertEqual({name.removesuffix(".json") + ".expected_error.txt" for name in INVALID_NAMES}, sidecars)

    def test_valid_surface_and_root_zone_profiles_pass(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertEqual([], validator.validate_file(path))

    def test_invalid_fixtures_match_exact_sorted_sidecars(self) -> None:
        for path in sorted(INVALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                sidecar = path.with_suffix(".expected_error.txt")
                expected = [
                    tuple(line.split("\t", 1))
                    for line in sidecar.read_text(encoding="utf-8").splitlines()
                    if line
                ]
                self.assertEqual(expected, finding_pairs(json.loads(path.read_text(encoding="utf-8"))))

    def test_profile_preserves_layer_and_cadence_distinctions(self) -> None:
        surface = json.loads((VALID_ROOT / "surface_nrt.json").read_text(encoding="utf-8"))
        root_zone = json.loads((VALID_ROOT / "root_zone_standard_quality.json").read_text(encoding="utf-8"))
        self.assertEqual("surface", surface["observation"]["moisture_layer"])
        self.assertTrue(surface["observation"]["preliminary"])
        self.assertEqual("root_zone", root_zone["observation"]["moisture_layer"])
        self.assertFalse(root_zone["observation"]["preliminary"])

    def test_source_model_grid_and_truth_collapse_are_denied(self) -> None:
        cases = [
            (
                ("source_descriptor_ref",),
                "fixture://source/not-smap",
                ("SOURCE_DESCRIPTOR_REF_INVALID", "$.source_descriptor_ref"),
            ),
            (("source_role",), "raw_observation", ("SOURCE_ROLE_COLLAPSE", "$.source_role")),
            (("assimilation", "kind"), "observation", ("MODEL_ASSIMILATION_MISSING", "$.assimilation.kind")),
            (("spatial_support", "kind"), "station", ("GRID_STATION_COLLAPSE", "$.spatial_support.kind")),
            (
                ("anti_collapse", "station_observation"),
                True,
                ("GRID_STATION_COLLAPSE", "$.anti_collapse.station_observation"),
            ),
            (("anti_collapse", "field_truth"), True, ("GROUND_TRUTH_FORBIDDEN", "$.anti_collapse.field_truth")),
        ]
        for path, value, expected in cases:
            candidate = load_surface()
            target: dict[str, object] = candidate
            for key in path[:-1]:
                target = target[key]  # type: ignore[assignment,index]
            target[path[-1]] = value
            with self.subTest(path=path):
                self.assertIn(expected, finding_pairs(candidate))

    def test_station_and_precise_location_aliases_are_undeclared(self) -> None:
        for field in ("station_id", "latitude", "longitude", "field_id", "mesonet_station"):
            candidate = load_surface()
            candidate[field] = "SENTINEL"
            self.assertIn(("UNDECLARED_FIELD", f"$.{field}"), finding_pairs(candidate))

    def test_numeric_bounds_reject_booleans_and_out_of_range_values(self) -> None:
        cases = [
            (("observation", "value"), True, ("VALUE_OUT_OF_RANGE", "$.observation.value")),
            (("observation", "uncertainty"), -0.01, ("UNCERTAINTY_REQUIRED", "$.observation.uncertainty")),
            (
                ("spatial_support", "source_resolution_m"),
                False,
                ("GRID_RESOLUTION_REQUIRED", "$.spatial_support.source_resolution_m"),
            ),
        ]
        for path, value, expected in cases:
            candidate = load_surface()
            candidate[path[0]][path[1]] = value  # type: ignore[index]
            with self.subTest(path=path, value=value):
                self.assertIn(expected, finding_pairs(candidate))

    def test_canonical_utc_and_temporal_order_are_required(self) -> None:
        for value in ("2026-04-20T10:00:00+00:00", "2026-4-20T1:00:00Z"):
            candidate = load_surface()
            candidate["observation"]["observed_time"] = value  # type: ignore[index]
            with self.subTest(value=value):
                self.assertIn(
                    ("OBSERVED_TIME_INVALID", "$.observation.observed_time"),
                    finding_pairs(candidate),
                )

        candidate = load_surface()
        candidate["time"]["retrieved_at"] = "2026-04-20T09:00:00Z"  # type: ignore[index]
        self.assertIn(("TEMPORAL_ORDER_INVALID", "$.time.retrieved_at"), finding_pairs(candidate))

    def test_hash_references_and_nonrelease_governance_fail_closed(self) -> None:
        surface = load_surface()
        root_zone = json.loads((VALID_ROOT / "root_zone_standard_quality.json").read_text(encoding="utf-8"))
        self.assertEqual(validator.SPEC_HASH, surface["spec_hash"])
        self.assertEqual(surface["spec_hash"], root_zone["spec_hash"])

        candidate = load_surface()
        candidate["spec_hash"] = "sha256:" + ("1" * 64)
        candidate["run_receipt_ref"] = "https://example.invalid/receipt"
        candidate["governance"]["promotion_eligible"] = True  # type: ignore[index]
        actual = set(finding_pairs(candidate))
        self.assertIn(("SPEC_HASH_INVALID", "$.spec_hash"), actual)
        self.assertIn(("RUN_RECEIPT_REF_REQUIRED", "$.run_receipt_ref"), actual)
        self.assertIn(("GOVERNANCE_PROMOTION_STATE_INVALID", "$.governance.promotion_eligible"), actual)

    def test_fixture_references_require_identifiers_after_namespaces(self) -> None:
        candidate = load_surface()
        candidate["fixture_id"] = "fixture://soil/smap_l4/"
        candidate["source_descriptor_ref"] = "fixture://source/"
        candidate["spatial_support"]["grid_cell_id"] = "fixture://grid/cell/"  # type: ignore[index]
        candidate["evidence_refs"] = ["fixture://evidence/"]
        candidate["run_receipt_ref"] = "fixture://receipt/"
        actual = set(finding_pairs(candidate))
        self.assertTrue(
            {
                ("FIXTURE_ID_INVALID", "$.fixture_id"),
                ("SOURCE_DESCRIPTOR_REF_INVALID", "$.source_descriptor_ref"),
                ("GRID_CELL_ID_REQUIRED", "$.spatial_support.grid_cell_id"),
                ("EVIDENCE_REFS_REQUIRED", "$.evidence_refs"),
                ("RUN_RECEIPT_REF_REQUIRED", "$.run_receipt_ref"),
            }.issubset(actual)
        )

    def test_findings_are_deterministic_across_object_insertion_order(self) -> None:
        candidate = load_surface()
        candidate["station_id"] = "do-not-echo-this"
        self.assertEqual(finding_pairs(candidate), finding_pairs(reverse_objects(candidate)))

    def test_parser_rejects_duplicate_keys_nonfinite_numbers_and_oversize_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"fixture_only":true,"fixture_only":true}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + (b" " * MAX_FIXTURE_BYTES) + b"}")
            self.assertEqual(
                [("FIXTURE_JSON_INVALID", "$")],
                [(f.code, f.path) for f in validator.validate_file(duplicate)],
            )
            self.assertEqual(
                [("FIXTURE_JSON_INVALID", "$")],
                [(f.code, f.path) for f in validator.validate_file(nonfinite)],
            )
            self.assertEqual(
                [("FIXTURE_TOO_LARGE", "$")],
                [(f.code, f.path) for f in validator.validate_file(oversized)],
            )

    def test_validation_is_no_network(self) -> None:
        with (
            mock.patch.object(socket, "socket") as socket_mock,
            mock.patch.object(urllib.request, "urlopen") as urlopen_mock,
        ):
            self.assertEqual([], validator.validate_file(VALID_ROOT / "surface_nrt.json"))
            socket_mock.assert_not_called()
            urlopen_mock.assert_not_called()

    def test_cli_exit_codes_and_non_echoing_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            secret = "SENTINEL_DO_NOT_ECHO"
            candidate = load_surface()
            candidate["private_note"] = secret
            invalid_path = Path(tmp) / "invalid.json"
            invalid_path.write_text(json.dumps(candidate), encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                self.assertEqual(0, validator.main([str(VALID_ROOT / "surface_nrt.json")]))
                self.assertEqual(1, validator.main([str(invalid_path)]))
                self.assertEqual(2, validator.main([]))
            output = stdout.getvalue() + stderr.getvalue()
            self.assertNotIn(secret, output)
            self.assertIn('"status":"PASS"', output)
            self.assertIn('"status":"FAIL"', output)


if __name__ == "__main__":
    unittest.main()
