from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/historical_network_proximity.py"
SPEC = importlib.util.spec_from_file_location(
    "historical_network_proximity_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HistoricalNetworkProximityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(case for case in self.manifest["cases"] if case["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_closed_inactive_and_non_authoritative(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["authority"], "NONE")
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["geometry_execution"])
        self.assertFalse(schema["x-kfm"]["real_location_data"])
        self.assertFalse(schema["x-kfm"]["release"])

    def test_fixture_manifest_matches_twenty_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 20)
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_valid_finite_interpretations_remain_distinct(self) -> None:
        expected = {
            "pass_exact_historical_proximity_candidate": (
                "PROXIMITY_CANDIDATE",
                "CANDIDATE",
            ),
            "pass_non_overlapping_intervals_abstain": (
                "NO_TEMPORAL_OVERLAP",
                "ABSTAIN",
            ),
            "pass_ambiguous_assertion_abstain": ("AMBIGUOUS", "ABSTAIN"),
            "pass_unresolved_assertion_abstain": ("UNSUPPORTED", "ABSTAIN"),
            "pass_modern_alignment_context_only_abstain": (
                "UNSUPPORTED",
                "ABSTAIN",
            ),
        }
        for name, pair in expected.items():
            candidate = self._candidate(name)
            observed = (
                candidate["interpretation"]["relation_kind"],
                candidate["conclusion"]["declared_outcome"],
            )
            self.assertEqual(observed, pair)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")

    def test_half_open_temporal_overlap_is_calculated(self) -> None:
        candidate = self._candidate("pass_exact_historical_proximity_candidate")
        candidate["route_assertion"]["valid_time"] = {
            "start": "1870-01-01T00:00:00Z",
            "end": "1880-01-01T00:00:00Z",
            "bounds": "[)",
        }
        self.assertFalse(MODULE.calculated_temporal_overlap(candidate))

    def test_approximate_candidate_exposes_uncertainty_separately(self) -> None:
        candidate = self._candidate("pass_approximate_reconstructed_candidate")
        self.assertEqual(candidate["place_assertion"]["uncertainty_m"], 400)
        self.assertEqual(candidate["route_assertion"]["uncertainty_m"], 600)
        self.assertEqual(candidate["proximity"]["combined_uncertainty_m"], 1000)
        self.assertLess(
            candidate["proximity"]["distance_min_m"],
            candidate["proximity"]["distance_max_m"],
        )

    def test_proximity_candidate_never_claims_relationship_or_authority(self) -> None:
        candidate = self._candidate("pass_exact_historical_proximity_candidate")
        claims = candidate["interpretation"]
        self.assertTrue(
            all(value is False for key, value in claims.items() if key.endswith("_claimed"))
        )
        self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))
        self.assertIn("DISTANCE_IS_NOT_RELATIONSHIP", candidate["limitations"])

    def test_negative_cases_have_exact_codes(self) -> None:
        expected = {
            "deny_temporal_overlap_flag_mismatch": ["TEMPORAL_OVERLAP_MISMATCH"],
            "deny_combined_uncertainty_mismatch": ["COMBINED_UNCERTAINTY_MISMATCH"],
            "deny_distance_band_reversed": ["DISTANCE_BAND_INVALID"],
            "deny_approximate_place_without_uncertainty": ["PLACE_UNCERTAINTY_REQUIRED"],
            "deny_reconstructed_route_without_uncertainty": ["ROUTE_UNCERTAINTY_REQUIRED"],
            "deny_modern_role_alignment_mismatch": ["MODERN_ALIGNMENT_ROLE_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_is_deterministic_and_mutation_sensitive(self) -> None:
        candidate = self._candidate("pass_exact_historical_proximity_candidate")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["proximity"]["distance_max_m"] = 1201
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_input_loader_rejects_unsafe_json_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            self.assertEqual(MODULE.load_json_object(duplicate)[1][0].code, "JSON_DUPLICATE_KEY")
            self.assertEqual(MODULE.load_json_object(nonfinite)[1][0].code, "JSON_NONFINITE_NUMBER")
            self.assertEqual(MODULE.load_json_object(link)[1][0].code, "INPUT_SYMLINK_DENIED")

        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_helper_has_no_network_client_or_write_path(self) -> None:
        source = MODULE_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import urllib",
            "import socket",
            "httpx",
            "aiohttp",
            "boto3",
            "write_text(",
            "write_bytes(",
            "open(\"w",
            "open('w",
        )
        self.assertFalse(any(token in source for token in forbidden))


if __name__ == "__main__":
    unittest.main()
