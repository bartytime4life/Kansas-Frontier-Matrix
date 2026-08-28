from __future__ import annotations

import hashlib
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/generators/build_output_lane_split.py"
SPEC = importlib.util.spec_from_file_location("build_output_lane_split", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

FIXTURES = ROOT / "fixtures/contracts/v1/data/output_lane_split_manifest/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/data/output_lane_split_manifest.schema.json"


class OutputLaneSplitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture_manifest = MODULE.load_fixture_manifest()
        valid_case = next(
            case
            for case in self.fixture_manifest["cases"]
            if case["case_id"] == "valid_complete_split"
        )
        self.valid = MODULE.materialize_case(self.fixture_manifest, valid_case)

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        cases = self.fixture_manifest["cases"]
        self.assertEqual(9, len(cases))
        self.assertEqual(1, sum(case["expected_outcome"] == "PASS" for case in cases))
        self.assertEqual(8, sum(case["expected_outcome"] == "DENY" for case in cases))
        for case in cases:
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_payload(
                    MODULE.materialize_case(self.fixture_manifest, case)
                )
                actual = [{"code": item.code, "field": item.field} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_spec_hash_is_stable(self) -> None:
        candidate = {key: value for key, value in self.valid.items() if key != "spec_hash"}
        self.assertEqual(self.valid["spec_hash"], MODULE.canonical_hash(candidate))
        self.assertEqual(self.valid["spec_hash"], MODULE.canonical_hash(candidate))

    def test_spec_hash_uses_repository_rfc8785_profile(self) -> None:
        from hashing import compute_spec_hash

        candidate = {"value": 1e-7, "label": "rfc8785"}
        legacy = "sha256:" + hashlib.sha256(
            json.dumps(
                candidate,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(compute_spec_hash(candidate), MODULE.canonical_hash(candidate))
        self.assertNotEqual(legacy, MODULE.canonical_hash(candidate))

    def test_split_result_preserves_all_lanes_and_no_authority(self) -> None:
        result = MODULE.split_payload(self.valid)
        self.assertEqual(list(MODULE.LANES), result["lane_order"])
        self.assertEqual({lane: 1 for lane in MODULE.LANES}, result["counts"])
        self.assertFalse(result["writes_performed"])
        self.assertFalse(result["payloads_moved_or_copied"])
        self.assertFalse(result["promotion_authorized"])
        self.assertFalse(result["release_authorized"])
        self.assertFalse(result["publication_authorized"])

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory) / "out"
            code = MODULE.main([str(self._write_input(directory))])
            self.assertEqual(0, code)
            self.assertFalse(output_dir.exists())

    def test_explicit_write_creates_indexes_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            input_path = self._write_input(directory)
            output_dir = Path(directory) / "out"
            code = MODULE.main(
                [str(input_path), "--write", "--output-dir", str(output_dir)]
            )
            self.assertEqual(0, code)
            expected = {f"{lane.lower()}.json" for lane in MODULE.LANES}
            expected.add("split-summary.json")
            self.assertEqual(expected, {path.name for path in output_dir.iterdir()})
            for path in output_dir.iterdir():
                value = json.loads(path.read_text(encoding="utf-8"))
                self.assertNotIn("payload_bytes", value)

    def test_write_refuses_nonempty_output_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory) / "out"
            output_dir.mkdir()
            (output_dir / "existing.txt").write_text("preserve\n", encoding="utf-8")
            result = MODULE.split_payload(self.valid)
            with self.assertRaises(ValueError):
                MODULE.write_indexes(result, output_dir)
            self.assertEqual("preserve\n", (output_dir / "existing.txt").read_text())

    def test_generator_does_not_open_network(self) -> None:
        def denied(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access denied")
        with mock.patch.object(socket, "socket", denied), mock.patch.object(
            socket, "create_connection", denied
        ), mock.patch.object(socket, "getaddrinfo", denied):
            self.assertEqual("PASS", MODULE.validate_payload(self.valid).outcome)
            result = MODULE.split_payload(self.valid)
            self.assertEqual("REVIEW_REQUIRED", result["status"])

    def test_fixture_runner_is_deterministic(self) -> None:
        self.assertEqual(0, MODULE.run_fixtures())
        self.assertEqual(0, MODULE.run_fixtures())

    def _write_input(self, directory: str) -> Path:
        path = Path(directory) / "manifest.json"
        path.write_text(json.dumps(self.valid, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path


if __name__ == "__main__":
    unittest.main()
