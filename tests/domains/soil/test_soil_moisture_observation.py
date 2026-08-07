from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/domains/soil/validate_soil_moisture_observation.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/soil/soil_moisture_observation.schema.json"
CONTRACT_PATH = REPO_ROOT / "contracts/domains/soil/soil_moisture_observation.md"
FIXTURES = REPO_ROOT / "fixtures/domains/soil/soil_moisture_observation"

spec = importlib.util.spec_from_file_location("validate_soil_moisture_observation", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class SoilMoistureObservationTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_six_valid_fixtures_cover_finite_outcomes_and_support_types(self) -> None:
        expected = {
            "abstain_stale.json": "ABSTAIN",
            "answer_reference_station.json": "ANSWER",
            "answer_satellite_surface.json": "ANSWER",
            "answer_station.json": "ANSWER",
            "deny_private_sensor.json": "DENY",
            "error_operational.json": "ERROR",
        }
        files = {path.name: path for path in (FIXTURES / "valid").glob("*.json")}
        self.assertEqual(set(expected), set(files))
        support_types: set[str] = set()
        outcomes: set[str] = set()
        for name, packet_outcome in expected.items():
            with self.subTest(name=name):
                result = validator.validate_file(files[name])
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(packet_outcome, result.packet_outcome)
                payload = json.loads(files[name].read_text(encoding="utf-8"))
                support_types.add(payload["support_type"])
                outcomes.add(packet_outcome)
        self.assertEqual(
            {
                "station_soil_moisture",
                "reference_station_soil_climate",
                "satellite_soil_moisture_grid",
            },
            support_types,
        )
        self.assertEqual({"ANSWER", "ABSTAIN", "DENY", "ERROR"}, outcomes)

    def test_reviewed_invalid_fixtures_have_exact_findings(self) -> None:
        expected = json.loads(
            (FIXTURES / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        files = {path.name: path for path in (FIXTURES / "invalid").glob("*.json")}
        self.assertEqual(set(expected), set(files))
        for name, expected_codes in expected.items():
            with self.subTest(name=name):
                result = validator.validate_file(files[name])
                self.assertFalse(result.ok)
                self.assertEqual(expected_codes, sorted({item.code for item in result.findings}))

    def test_identity_is_stable_across_mapping_key_order(self) -> None:
        payload = json.loads((FIXTURES / "valid/answer_station.json").read_text(encoding="utf-8"))
        reordered = {key: payload[key] for key in reversed(list(payload))}
        self.assertEqual(payload["spec_hash"], validator.canonical_spec_hash(reordered))
        self.assertEqual(payload["observation_id"], validator.expected_observation_id(reordered))

    def test_answer_and_negative_value_polarity(self) -> None:
        for path in sorted((FIXTURES / "valid").glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            outcome = payload["assessment"]["outcome"]
            value = payload["measurement"]["normalized_value"]
            with self.subTest(path=path.name, outcome=outcome):
                if outcome == "ANSWER":
                    self.assertIsInstance(value, (int, float))
                else:
                    self.assertIsNone(value)

    def test_station_and_satellite_depth_postures_remain_distinct(self) -> None:
        station = json.loads((FIXTURES / "valid/answer_station.json").read_text(encoding="utf-8"))
        satellite = json.loads(
            (FIXTURES / "valid/answer_satellite_surface.json").read_text(encoding="utf-8")
        )
        self.assertEqual("SENSOR_DEPTH", station["measurement"]["depth_support"]["kind"])
        self.assertIsInstance(station["measurement"]["depth_support"]["depth_cm"], (int, float))
        self.assertIsNone(station["subject"]["resolution_m"])
        self.assertEqual("SURFACE_LAYER", satellite["measurement"]["depth_support"]["kind"])
        self.assertIsNone(satellite["measurement"]["depth_support"]["depth_cm"])
        self.assertGreater(satellite["subject"]["resolution_m"], 0)

    def test_unknown_member_is_denied_by_schema(self) -> None:
        payload = json.loads((FIXTURES / "valid/answer_station.json").read_text(encoding="utf-8"))
        payload["unexpected"] = True
        result = validator.validate_payload(payload)
        self.assertFalse(result.ok)
        self.assertIn("SCHEMA_INVALID", {item.code for item in result.findings})

    def test_duplicate_key_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"domain":"soil","domain":"other"}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("JSON_DUPLICATE_KEY", "/"),), result.findings)

    def test_nonfinite_number_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("JSON_NONFINITE_NUMBER", "/"),), result.findings)

    def test_symlink_input_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            result = validator.validate_file(link)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("INPUT_SYMLINK_DENIED", "/"),), result.findings)

    def test_validator_imports_no_network_client(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import aiohttp",
            "import socket",
            "from urllib",
        )
        self.assertFalse(any(token in source for token in forbidden))

    def test_contract_records_implemented_fixture_profile_without_authority_claim(self) -> None:
        text = CONTRACT_PATH.read_text(encoding="utf-8")
        self.assertIn("PROPOSED_INACTIVE", text)
        self.assertIn("paired schema and validator", text)
        self.assertNotIn("Schema: missing", text)
        self.assertIn("do not activate", text.lower())

    def test_cli_passes_valid_packet(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                str(FIXTURES / "valid/answer_station.json"),
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("PASS", payload["outcome"])
        self.assertEqual("ANSWER", payload["packet_outcome"])
        self.assertEqual([], payload["findings"])
        self.assertEqual({False}, set(payload["authority"].values()))

    def test_cli_fails_contradictory_packet(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                str(FIXTURES / "invalid/support_type_role_collapse.json"),
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertEqual("FAIL", payload["outcome"])
        self.assertTrue(
            any(item["code"] == "SOURCE_ROLE_SUPPORT_MISMATCH" for item in payload["findings"])
        )

    def test_fixture_profile_cli_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertEqual(14, len([line for line in completed.stdout.splitlines() if line.strip()]))


if __name__ == "__main__":
    unittest.main()
