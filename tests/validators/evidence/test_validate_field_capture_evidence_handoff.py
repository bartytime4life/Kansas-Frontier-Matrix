from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.evidence import validate_field_capture_evidence_handoff as validator

ROOT = Path(__file__).resolve().parents[3]


class FieldCaptureEvidenceHandoffTests(unittest.TestCase):
    def test_schema_is_valid_closed_and_coordinate_free(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["capture"]["additionalProperties"])
        self.assertFalse(schema["$defs"]["governance"]["additionalProperties"])
        capture_fields = set(schema["$defs"]["capture"]["properties"])
        self.assertTrue(capture_fields.isdisjoint({"latitude", "longitude", "coordinates", "geometry"}))

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_finite_outcomes_are_complete(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "ABSTAIN", "DENY"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 20)

    def test_manual_and_gnss_point_semantics_do_not_collapse(self) -> None:
        manifest = validator.load_fixtures()
        passing = {
            validator.materialize_case(manifest, case)["capture"]["capture_kind"]:
            validator.materialize_case(manifest, case)["capture"]["acquisition_method"]
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        }
        self.assertEqual("GNSS_RECEIVER", passing["GNSS_POINT"])
        self.assertEqual("MANUAL_MAP_PLACEMENT", passing["MANUAL_POINT"])

    def test_identity_binds_handoff_metadata(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual((document["spec_hash"], document["assessment_id"]), validator.canonical_identity(document))
        changed = json.loads(json.dumps(document))
        changed["capture"]["revision_ref"] = "kfm://revision/fixture/gnss-point-001-v2"
        self.assertNotEqual(validator.canonical_identity(document), validator.canonical_identity(changed))

    def test_validation_has_no_network_or_capture_runtime(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            self.assertEqual("PASS", validator.validate_payload(document).outcome)
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "subprocess", "rasterio", "geopandas"):
            self.assertNotIn(token, source)

    def test_serialization_does_not_echo_candidate_metadata(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        sentinel = "do-not-echo-capture-ref"
        document["capture"]["capture_ref"] = f"kfm://capture/fixture/{sentinel}"
        result = validator.validate_payload(document)
        rendered = validator.serialize(Path("candidate.json"), result)
        self.assertNotIn(sentinel, rendered)
        self.assertNotIn("gnss-point-001", rendered)

    def test_cli_fixture_replay_and_parser_error(self) -> None:
        command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"case_count":26', first.stdout)
        self.assertIn('"suite_match":true', first.stdout)

        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "invalid.json"
            invalid.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(invalid)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
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
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_BYTES + 1))
            for path, code in (
                (duplicate, "FIELD_CAPTURE_JSON_DUPLICATE_KEY"),
                (nonfinite, "FIELD_CAPTURE_JSON_NONFINITE_NUMBER"),
                (link, "FIELD_CAPTURE_INPUT_SYMLINK_DENIED"),
                (oversized, "FIELD_CAPTURE_INPUT_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
