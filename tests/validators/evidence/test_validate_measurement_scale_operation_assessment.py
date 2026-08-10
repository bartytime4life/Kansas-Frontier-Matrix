from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_measurement_scale_operation_assessment.py"
SPEC = importlib.util.spec_from_file_location("measurement_scale_operation_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class MeasurementScaleOperationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        self.assertEqual(len(MODULE.validate_fixture_manifest()), 13)

    def test_nominal_ordinal_and_ratio_profiles(self) -> None:
        for name in ("pass_ratio_summary", "pass_nominal_categorical", "pass_ordinal_public_with_blocked_mean"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_and_custom_profiles_abstain(self) -> None:
        for name in ("abstain_incomplete_assessment", "abstain_custom_scale", "abstain_unresolved_definition"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_operation_partition_and_metadata_fail_closed(self) -> None:
        expected = {
            "deny_nominal_mean_permitted": ["OPERATION_PARTITION_MISMATCH"],
            "deny_scale_metadata_mismatch": ["MEASUREMENT_METADATA_INCOHERENT", "OPERATION_PARTITION_MISMATCH"],
            "deny_ratio_true_zero_absent": ["MEASUREMENT_METADATA_INCOHERENT"],
            "deny_numeric_unit_missing": ["NUMERIC_UNIT_REQUIRED"],
            "deny_public_review_missing": ["PUBLIC_REVIEW_REFERENCE_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_binds_semantics(self) -> None:
        candidate = self._candidate("pass_ratio_summary")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["requested_operations"] = ["MEAN"]
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
