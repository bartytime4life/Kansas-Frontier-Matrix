from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/ui/validate_time_bucket_playback_manifest.py"
spec = importlib.util.spec_from_file_location("time_bucket_playback_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class TimeBucketPlaybackManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        self.assertGreaterEqual(len(self.manifest["cases"]), 24)
        outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(self.manifest, case)
                )
                outcomes.add(result.outcome)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_state"], result.state)
                self.assertEqual(
                    case["expected_findings"],
                    [
                        {"code": finding.code, "path": finding.path}
                        for finding in result.findings
                    ],
                )
        self.assertEqual({"PASS", "DENY"}, outcomes)

    def test_valid_manifest_is_review_required_and_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.state)
        self.assertFalse(value["transition"]["autoplay"])
        self.assertFalse(value["transition"]["outcome_requires_playback"])
        self.assertFalse(value["boundary"]["runtime_execution_performed"])
        self.assertFalse(value["boundary"]["artifact_integrity_verified"])
        self.assertFalse(value["boundary"]["release_authorized"])
        self.assertFalse(value["boundary"]["public_use_authorized"])

    def test_one_time_kind_and_field_is_preserved(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "valid_observed_time_manifest"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("OBSERVED_TIME", value["time_semantics"]["filter_time_kind"])
        self.assertEqual(
            {"observed_time"},
            {bucket["time_field"] for bucket in value["buckets"]},
        )

    def test_explicit_gap_is_preserved_without_interpolation_mode(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "valid_explicit_transition_gap"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertTrue(value["buckets"][0]["gap_after"])
        self.assertIn(value["transition"]["gap_policy"], {"SHOW_GAP", "PAUSE", "DISABLE_PLAYBACK"})
        self.assertNotIn("INTERPOLATE", json.dumps(value))

    def test_bucket_and_manifest_identity_are_deterministic(self) -> None:
        case = self.manifest["cases"][0]
        first = validator.materialize_case(self.manifest, case)
        second = validator.materialize_case(self.manifest, case)
        self.assertEqual(
            [bucket["bucket_hash"] for bucket in first["buckets"]],
            [bucket["bucket_hash"] for bucket in second["buckets"]],
        )
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["manifest_id"], second["manifest_id"])

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(
                "TIME_BUCKET_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "TIME_BUCKET_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )
            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "TIME_BUCKET_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "TIME_BUCKET_INPUT_TOO_LARGE",
                validator.validate_file(oversized).findings[0].code,
            )

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_artifact_or_evidence_values(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "evidence_refs_unsorted"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn("events-2026-01", output)
        self.assertNotIn("temporal-method-v1", output)
        self.assertIn("TIME_BUCKET_EVIDENCE_ORDER_INVALID", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
