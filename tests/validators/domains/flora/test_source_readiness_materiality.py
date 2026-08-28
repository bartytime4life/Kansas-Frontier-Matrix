from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.domains.flora.validate_source_readiness_materiality import (
    CANDIDATE_SCHEMA_PATH,
    FIXTURE_ROOT,
    PROFILE_PATH,
    PROFILE_SCHEMA_PATH,
    REPO_ROOT,
    evaluate_candidate,
)


class FloraSourceReadinessMaterialityTests(unittest.TestCase):
    def test_profile_schema_and_hash(self) -> None:
        schema = json.loads(PROFILE_SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        candidate_schema = json.loads(
            CANDIDATE_SCHEMA_PATH.read_text(encoding="utf-8")
        )
        Draft202012Validator.check_schema(candidate_schema)
        profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        declared = profile.pop("spec_hash")
        computed = "sha256:" + hashlib.sha256(
            json.dumps(
                profile,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(declared, computed)

    def test_valid_fixtures_match_expected_shared_outcomes(self) -> None:
        lane = FIXTURE_ROOT / "valid"
        manifest = json.loads(
            (lane / "expected_outputs_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(manifest), 9)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = evaluate_candidate(lane / name)
                self.assertTrue(result.ok, result.findings)
                assessment = result.assessment
                self.assertIsNotNone(assessment)
                self.assertEqual(
                    expected["change_class"],
                    assessment["classification"]["change_class"],
                )
                self.assertEqual(
                    expected["outcome"],
                    assessment["classification"]["outcome"],
                )
                self.assertFalse(
                    assessment["governance"]["authority_created"]
                )
                self.assertFalse(
                    assessment["governance"]["promotion_authorized"]
                )

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(manifest), 8)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = evaluate_candidate(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(expected)),
                    sorted({item.code for item in result.findings}),
                )

    def test_evaluation_is_deterministic(self) -> None:
        path = (
            FIXTURE_ROOT
            / "valid/valid_material_license_regression.json"
        )
        first = evaluate_candidate(path)
        second = evaluate_candidate(path)
        self.assertEqual(first, second)

    def test_numeric_thresholds_are_strictly_greater_than(self) -> None:
        source = json.loads(
            (
                FIXTURE_ROOT
                / "valid/valid_semantic_non_material.json"
            ).read_text(encoding="utf-8")
        )
        source["metrics"]["candidate"]["georeferenced_fraction"] = 0.85
        source["metrics"]["candidate"]["specimen_backed_fraction"] = 0.60
        source["metrics"]["candidate"][
            "coordinate_uncertainty_p95_km"
        ] = 13.0
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "boundary.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            result = evaluate_candidate(path)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(
            "SEMANTIC_NON_MATERIAL",
            result.assessment["classification"]["change_class"],
        )

    def test_freshness_threshold_changes_only_when_state_crosses(self) -> None:
        source = json.loads(
            (
                FIXTURE_ROOT
                / "valid/valid_semantic_non_material.json"
            ).read_text(encoding="utf-8")
        )
        source["metrics"]["baseline"]["freshness_age_days"] = 91
        source["metrics"]["candidate"]["freshness_age_days"] = 120
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stale-to-stale.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            result = evaluate_candidate(path)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(
            "SEMANTIC_NON_MATERIAL",
            result.assessment["classification"]["change_class"],
        )

    def test_profile_tampering_fails_closed(self) -> None:
        profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        profile["triggers"]["georeferenced_fraction_delta"][
            "threshold"
        ] = 0.5
        with tempfile.TemporaryDirectory() as directory:
            profile_path = Path(directory) / "profile.json"
            profile_path.write_text(json.dumps(profile), encoding="utf-8")
            result = evaluate_candidate(
                FIXTURE_ROOT / "valid/valid_unchanged.json",
                profile_path,
            )
        self.assertFalse(result.ok)
        self.assertEqual(
            ["PROFILE_HASH_MISMATCH"],
            sorted({item.code for item in result.findings}),
        )

    def test_fixture_cli_profile_passes_without_echoing_source_ref(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                (
                    "tools/validators/domains/flora/"
                    "validate_source_readiness_materiality.py"
                ),
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            0,
            result.returncode,
            result.stdout + result.stderr,
        )
        self.assertIn(
            '"assessment_outcome":"PROMOTION_CANDIDATE"',
            result.stdout,
        )
        self.assertNotIn(
            "kfm://source/flora/example-occurrence-dataset",
            result.stdout,
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"assessment_id":"a","assessment_id":"b"}',
                encoding="utf-8",
            )
            result = evaluate_candidate(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = evaluate_candidate(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )


if __name__ == "__main__":
    unittest.main()
