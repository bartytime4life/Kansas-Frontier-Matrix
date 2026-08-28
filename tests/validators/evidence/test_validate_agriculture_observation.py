from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.evidence import validate_agriculture_observation as validator

ROOT = Path(__file__).resolve().parents[3]
GUARD_ROOT = ROOT / "tools/ci/kfm_no_network"
DENIAL_MESSAGE = "KFM no-network guard denied Python network egress"


def _shared_no_network_env() -> dict[str, str]:
    env = os.environ.copy()
    python_path = [str(GUARD_ROOT), str(ROOT)]
    if env.get("PYTHONPATH"):
        python_path.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(python_path)
    env["KFM_NO_NETWORK"] = "1"
    return env


class AgricultureObservationTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_positive_cases_cover_families_states_zero_classification_and_correction(self) -> None:
        manifest = validator.load_fixtures()
        passing = [
            validator.materialize_case(manifest, case)
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        ]
        self.assertEqual(set(validator.FAMILY_UNITS), {item["measure"]["measure_family"] for item in passing})
        self.assertEqual(
            {"OBSERVED", "SUPPRESSED", "MISSING"},
            {item["measure"]["result_state"] for item in passing},
        )
        self.assertIn(0, {item["measure"]["value"] for item in passing})
        self.assertIn("SOURCE_CLASSIFIED", {item["measure"]["classification_scope"] for item in passing})
        self.assertIn("CORRECTED", {item["lineage"]["correction_state"] for item in passing})
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "DENY"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 25)

    def test_observed_zero_is_not_missing_or_suppressed(self) -> None:
        manifest = validator.load_fixtures()
        case = next(case for case in manifest["cases"] if case["case_id"] == "valid-observed-zero")
        document = validator.materialize_case(manifest, case)
        self.assertEqual(0, document["measure"]["value"])
        self.assertEqual("OBSERVED", document["measure"]["result_state"])
        self.assertEqual("NOT_APPLICABLE", document["suppression"]["status"])
        self.assertEqual("PASS", validator.validate_payload(document).outcome)

    def test_fixture_has_no_farm_producer_geometry_or_frontier_payload(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        keys: set[str] = set()

        def collect(value: object) -> None:
            if isinstance(value, dict):
                keys.update(value)
                for item in value.values():
                    collect(item)
            elif isinstance(value, list):
                for item in value:
                    collect(item)

        collect(document)
        forbidden = {
            "farm_id",
            "producer_id",
            "producer_name",
            "address",
            "coordinates",
            "geometry",
            "classification_result",
            "frontier_status",
        }
        self.assertTrue(forbidden.isdisjoint(keys))
        governance = dict(document["governance"])
        self.assertEqual("FIXTURE_ONLY", governance.pop("execution_mode"))
        self.assertTrue(all(value is False for value in governance.values()))

    def test_source_role_rejects_role_collapse(self) -> None:
        manifest = validator.load_fixtures()
        case = next(case for case in manifest["cases"] if case["case_id"] == "valid-farm-count")
        for source_role in ("SATELLITE_GRID", "STATION_OBSERVATION", "OPERATOR_RECORD"):
            with self.subTest(source_role=source_role):
                document = validator.materialize_case(manifest, case)
                document["source"]["source_role"] = source_role
                result = validator.validate_payload(document)
                self.assertEqual("DENY", result.outcome)
                self.assertEqual(
                    (validator.Finding("AGRICULTURE_SCHEMA_INVALID", "/source/source_role"),),
                    result.findings,
                )

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["measure"]["value"] += 1
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_validation_does_not_open_network(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(document)
        self.assertEqual("PASS", result.outcome)
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "socket.create_connection"):
            self.assertNotIn(token, source)

    def test_cli_fixture_mode_runs_under_shared_no_network_guard(self) -> None:
        env = _shared_no_network_env()
        probe = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import socket, sitecustomize; "
                    "assert sitecustomize.GUARD_ACTIVE; "
                    "socket.create_connection(('192.0.2.1', 443), timeout=0.01)"
                ),
            ],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, probe.returncode)
        self.assertIn(DENIAL_MESSAGE, probe.stderr)
        self.assertIn("socket.create_connection", probe.stderr)

        completed = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["suite_match"])
        self.assertEqual(len(validator.load_fixtures()["cases"]), payload["cases"])

    def test_bounded_reader_rejects_duplicate_keys_and_non_object_roots(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            value, findings = validator._read(duplicate)
            self.assertIsNone(value)
            self.assertEqual("AGRICULTURE_JSON_DUPLICATE_KEY", findings[0].code)

            root = Path(directory) / "root.json"
            root.write_text("[]", encoding="utf-8")
            value, findings = validator._read(root)
            self.assertIsNone(value)
            self.assertEqual("AGRICULTURE_JSON_ROOT_INVALID", findings[0].code)

    def test_bounded_reader_rejects_symlinks_and_oversized_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            symlink = root / "symlink.json"
            symlink.symlink_to(target)
            value, findings = validator._read(symlink)
            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_INPUT_SYMLINK_DENIED", "/"),),
                findings,
            )

            oversized = root / "oversized.json"
            with oversized.open("wb") as handle:
                handle.truncate(validator.MAX_BYTES + 1)
            value, findings = validator._read(oversized)
            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_INPUT_TOO_LARGE", "/"),),
                findings,
            )

    def test_bounded_reader_rejects_non_files_nonfinite_and_malformed_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            non_file = root / "directory"
            non_file.mkdir()
            value, findings = validator._read(non_file)
            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_INPUT_NOT_FILE", "/"),),
                findings,
            )

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            value, findings = validator._read(nonfinite)
            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_JSON_NONFINITE_NUMBER", "/"),),
                findings,
            )

            malformed = root / "malformed.json"
            malformed.write_text('{"value":', encoding="utf-8")
            value, findings = validator._read(malformed)
            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_JSON_INVALID", "/"),),
                findings,
            )

    def test_serialized_result_disclaims_authority(self) -> None:
        payload = json.loads(validator.serialize(None, validator.Result("PASS", ())))
        self.assertEqual("NONE", payload["authority"])
        self.assertEqual("FIXTURE_ONLY", payload["execution_mode"])
        self.assertIn("no_publication", payload["non_effects"])
        self.assertIn("no_farm_or_producer_identification", payload["non_effects"])


if __name__ == "__main__":
    unittest.main()
