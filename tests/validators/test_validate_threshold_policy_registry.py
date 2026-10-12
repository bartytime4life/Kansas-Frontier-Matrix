from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    ROOT / "tools/validators/policy/validate_threshold_policy_registry.py"
)
SCHEMA_PATH = (
    ROOT / "schemas/contracts/v1/policy/threshold_policy_registry.schema.json"
)
REGISTRY_PATH = ROOT / "policy/thresholds/registry.v1.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/threshold_policy_registry"

SPEC = importlib.util.spec_from_file_location(
    "validate_threshold_policy_registry", VALIDATOR_PATH
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ThresholdPolicyRegistryTests(unittest.TestCase):
    def _registry(self) -> dict[str, object]:
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    def _rebind(self, value: dict[str, object]) -> dict[str, object]:
        value["spec_hash"] = MODULE.canonical_spec_hash(value)
        return value

    def test_schema_is_closed_inactive_and_value_free(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
        slot = schema["$defs"]["threshold_slot"]["properties"]
        for field in ("operator", "value", "unit", "effective_from", "supersedes"):
            self.assertEqual(slot[field]["type"], "null")

    def test_repository_registry_passes_and_identity_replays(self) -> None:
        registry = self._registry()
        self.assertTrue(MODULE.validate_record(REGISTRY_PATH).ok)
        self.assertEqual(registry["spec_hash"], MODULE.canonical_spec_hash(registry))

    def test_registry_contains_only_named_unresolved_slots(self) -> None:
        registry = self._registry()
        thresholds = registry["thresholds"]
        ids = [item["threshold_id"] for item in thresholds]
        self.assertEqual(ids, sorted(set(ids)))
        self.assertEqual(len(ids), 6)
        self.assertEqual(
            ids,
            [
                "kfm.threshold.agriculture.cdl-drift-materiality.v1",
                "kfm.threshold.atmosphere.aod-materiality.v1",
                "kfm.threshold.atmosphere.frp-materiality.v1",
                "kfm.threshold.atmosphere.ozone-materiality.v1",
                "kfm.threshold.hydrology.persistence-review.v1",
                "kfm.threshold.soil.moisture-materiality.v1",
            ],
        )
        for item in thresholds:
            with self.subTest(threshold=item["threshold_id"]):
                self.assertEqual(item["value_state"], "UNRESOLVED")
                self.assertEqual(item["binding_state"], "UNBOUND")
                self.assertEqual(item["review_state"], "HOLD")
                for field in ("operator", "value", "unit", "effective_from", "supersedes"):
                    self.assertIsNone(item[field])
                self.assertEqual(item["reason_codes"], MODULE.EXPECTED_REASONS)
        self.assertTrue(all(value is False for value in registry["governance"].values()))

    def test_semantic_negative_polarity(self) -> None:
        registry = self._registry()

        unsorted = copy.deepcopy(registry)
        unsorted["thresholds"][0], unsorted["thresholds"][1] = (
            unsorted["thresholds"][1],
            unsorted["thresholds"][0],
        )
        self._rebind(unsorted)
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unsorted).findings},
            {"THRESHOLD_IDS_NOT_CANONICAL"},
        )

        reason_drift = copy.deepcopy(registry)
        reason_drift["thresholds"][0]["reason_codes"] = [
            "EVIDENCE_UNRESOLVED",
            "NO_VALUE_ADOPTED",
            "STEWARD_REVIEW_REQUIRED",
        ]
        self._rebind(reason_drift)
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(reason_drift).findings},
            {"UNRESOLVED_REASONS_REQUIRED"},
        )

        missing_pressure = copy.deepcopy(registry)
        missing_pressure["thresholds"][0]["pressure_refs"] = [
            "docs/does-not-exist-threshold-pressure.md"
        ]
        self._rebind(missing_pressure)
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(missing_pressure).findings},
            {"PRESSURE_REF_INVALID"},
        )

    def test_schema_denies_value_and_authority_overclaims(self) -> None:
        value = self._registry()
        value["thresholds"][0]["value"] = 2
        self.assertIn(
            "SCHEMA_INVALID",
            {item.code for item in MODULE.validate_payload(value).findings},
        )

        authority = self._registry()
        authority["governance"]["watcher_binding_authorized"] = True
        self.assertIn(
            "SCHEMA_INVALID",
            {item.code for item in MODULE.validate_payload(authority).findings},
        )

    def test_fixture_profile_has_exact_polarity(self) -> None:
        valid = sorted((FIXTURES / "valid").glob("valid_*.json"))
        invalid = sorted((FIXTURES / "invalid").glob("invalid_*.json"))
        self.assertEqual(len(valid), 1)
        self.assertEqual(len(invalid), 2)
        self.assertTrue(MODULE.validate_record(valid[0]).ok)
        for path in invalid:
            self.assertFalse(MODULE.validate_record(path).ok, path.name)
        code, report = MODULE.run_fixture_profile()
        self.assertEqual(code, 0, report)
        self.assertEqual(json.loads(report)["outcome"], "PASS")

    def test_duplicate_nonfinite_and_symlink_inputs_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"object_type":"a","object_type":"b"}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            symlink = root / "candidate-link.json"
            symlink.symlink_to(REGISTRY_PATH)

            self.assertEqual(
                {item.code for item in MODULE.validate_record(duplicate).findings},
                {"JSON_DUPLICATE_KEY"},
            )
            self.assertEqual(
                {item.code for item in MODULE.validate_record(nonfinite).findings},
                {"JSON_NONFINITE_NUMBER"},
            )
            self.assertEqual(
                {item.code for item in MODULE.validate_record(symlink).findings},
                {"INPUT_SYMLINK_DENIED"},
            )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.serialize(
                REGISTRY_PATH, MODULE.validate_record(REGISTRY_PATH)
            )
            second = MODULE.serialize(
                REGISTRY_PATH, MODULE.validate_record(REGISTRY_PATH)
            )
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--registry"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["outcome"], "PASS")


if __name__ == "__main__":
    unittest.main()
