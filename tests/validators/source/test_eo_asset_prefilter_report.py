from __future__ import annotations

import hashlib
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.source.validate_eo_asset_prefilter_report import (
    FIXTURE_ROOT,
    PROFILE_PATH,
    PROFILE_SCHEMA_PATH,
    REPORT_SCHEMA_PATH,
    REPO_ROOT,
    canonical_spec_hash,
    validate_report,
)


class EOAssetPrefilterReportTests(unittest.TestCase):
    def test_schemas_and_profile_hash_are_valid(self) -> None:
        for path in (PROFILE_SCHEMA_PATH, REPORT_SCHEMA_PATH):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(profile["spec_hash"], canonical_spec_hash(profile))
        self.assertEqual("PROPOSED_INACTIVE", profile["status"])
        self.assertFalse(profile["governance"]["source_activated"])

    def test_valid_fixtures_match_expected_decisions(self) -> None:
        lane = FIXTURE_ROOT / "valid"
        manifest = json.loads(
            (lane / "expected_decisions_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(manifest), 5)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_report(lane / name)
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(expected["decision"], result.decision)
                candidate = json.loads((lane / name).read_text(encoding="utf-8"))
                self.assertEqual(
                    expected["reason_codes"],
                    candidate["summary"]["reason_codes"],
                )
                self.assertFalse(candidate["governance"]["public_use_allowed"])

    def test_invalid_fixtures_match_exact_code_sets(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(manifest), 8)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_report(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(expected)),
                    sorted({item.code for item in result.findings}),
                )

    def test_validation_is_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_pass.json"
        self.assertEqual(validate_report(path), validate_report(path))

    def test_threshold_boundaries_are_inclusive(self) -> None:
        source = json.loads(
            (FIXTURE_ROOT / "valid/valid_pass.json").read_text(
                encoding="utf-8"
            )
        )
        for item in source["items"]:
            item["valid_pixel_fraction"] = 0.6
            item["cloud_cover_percent"] = 30.0
        source["summary"]["items_meeting_valid_pixel_fraction"] = 6
        source["summary"]["items_meeting_cloud_cover"] = 6
        source["summary"]["items_usable"] = 6
        source["spec_hash"] = canonical_spec_hash(source)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "boundary.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            result = validate_report(path)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.decision)

    def test_last_modified_is_an_accepted_replay_fallback(self) -> None:
        source = json.loads(
            (FIXTURE_ROOT / "valid/valid_pass.json").read_text(
                encoding="utf-8"
            )
        )
        asset = source["items"][0]["assets"][0]
        asset["etag"] = None
        asset["etag_strength"] = "missing"
        source["spec_hash"] = canonical_spec_hash(source)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fallback.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            result = validate_report(path)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.decision)

    def test_profile_tampering_fails_closed(self) -> None:
        profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        profile["requirements"]["minimum_items_found"] = 1
        with tempfile.TemporaryDirectory() as directory:
            profile_path = Path(directory) / "profile.json"
            profile_path.write_text(json.dumps(profile), encoding="utf-8")
            result = validate_report(
                FIXTURE_ROOT / "valid/valid_pass.json", profile_path
            )
        self.assertFalse(result.ok)
        self.assertEqual(
            ["PROFILE_HASH_MISMATCH"],
            sorted({item.code for item in result.findings}),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"EOAssetPrefilterReport",'
                '"object_type":"EOAssetPrefilterReport"}',
                encoding="utf-8",
            )
            result = validate_report(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_report(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )

    def test_fixture_cli_passes_without_echoing_locators_or_etags(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/source/validate_eo_asset_prefilter_report.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("EO_PREFILTER_FIXTURES_VALID", result.stdout)
        self.assertNotIn("kfm://evidence/fixture/eo-asset", result.stdout)
        sample = json.loads(
            (FIXTURE_ROOT / "valid/valid_pass.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertNotIn(sample["items"][0]["assets"][0]["etag"], result.stdout)

    def test_validation_performs_no_network_calls(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ):
            result = validate_report(FIXTURE_ROOT / "valid/valid_pass.json")
        self.assertTrue(result.ok, result.findings)


if __name__ == "__main__":
    unittest.main()
