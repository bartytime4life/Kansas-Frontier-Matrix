"""Focused no-network tests for the MapLibre source-metadata projection."""

from __future__ import annotations

import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.maplibre.validate_source_metadata import (  # noqa: E402
    FIXTURE_ROOT,
    OUTCOME_EXIT_CODES,
    ValidationOptions,
    run_fixtures,
    validate_source_metadata,
)

VALID_STYLE = FIXTURE_ROOT / "valid" / "style.single-source.valid.json"
MATCHING_MANIFEST = FIXTURE_ROOT / "valid" / "manifest.single-source.match.json"
MISMATCH_STYLE = FIXTURE_ROOT / "invalid" / "style.digest-mismatch.json"
UNMAPPED_STYLE = (
    FIXTURE_ROOT / "edge" / "style.manifest-supplied-source-unmapped.json"
)
UNMAPPED_MANIFEST = FIXTURE_ROOT / "edge" / "manifest.source-unmapped.json"


class SourceMetadataProjectionTests(unittest.TestCase):
    def test_repository_fixture_manifest_has_exact_polarity(self) -> None:
        self.assertEqual(run_fixtures(FIXTURE_ROOT), 0)

    def test_matching_projection_allows_without_claiming_authority(self) -> None:
        report = validate_source_metadata(
            VALID_STYLE,
            manifest_path=MATCHING_MANIFEST,
            options=ValidationOptions(
                require_proof=True,
                require_manifest_ref=True,
                strict_epoch=True,
            ),
        )
        self.assertEqual(report.outcome, "ALLOW")
        self.assertEqual(report.reason_codes, ())
        payload = report.to_dict()
        self.assertIn("renderer projection", payload["boundary"][0])
        self.assertNotIn("release approval", json.dumps(payload).lower())

    def test_digest_mismatch_denies(self) -> None:
        report = validate_source_metadata(
            MISMATCH_STYLE,
            manifest_path=MATCHING_MANIFEST,
            options=ValidationOptions(strict_epoch=True),
        )
        self.assertEqual(report.outcome, "DENY")
        self.assertEqual(report.reason_codes, ("SOURCE_DIGEST_MISMATCH",))
        self.assertEqual(OUTCOME_EXIT_CODES[report.outcome], 3)

    def test_manifest_without_selected_source_abstains(self) -> None:
        report = validate_source_metadata(
            UNMAPPED_STYLE,
            manifest_path=UNMAPPED_MANIFEST,
            options=ValidationOptions(strict_epoch=True),
        )
        self.assertEqual(report.outcome, "ABSTAIN")
        self.assertEqual(report.reason_codes, ("MANIFEST_SOURCE_UNMAPPED",))
        self.assertEqual(OUTCOME_EXIT_CODES[report.outcome], 2)

    def test_malformed_json_is_error_not_deny(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            style = Path(temp_dir) / "style.json"
            style.write_text('{"version": 8,', encoding="utf-8")
            report = validate_source_metadata(style)
        self.assertEqual(report.outcome, "ERROR")
        self.assertEqual(report.reason_codes, ("JSON_INVALID",))
        self.assertEqual(OUTCOME_EXIT_CODES[report.outcome], 4)

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            style = Path(temp_dir) / "style.json"
            style.write_text(
                '{"version":8,"version":8,"sources":{}}', encoding="utf-8"
            )
            report = validate_source_metadata(style)
        self.assertEqual(report.outcome, "ERROR")
        self.assertEqual(report.reason_codes, ("JSON_DUPLICATE_KEY",))

    def test_report_is_deterministic_and_redacts_projection_values(self) -> None:
        first = validate_source_metadata(
            VALID_STYLE,
            manifest_path=MATCHING_MANIFEST,
            options=ValidationOptions(strict_epoch=True),
        ).to_dict()
        second = validate_source_metadata(
            VALID_STYLE,
            manifest_path=MATCHING_MANIFEST,
            options=ValidationOptions(strict_epoch=True),
        ).to_dict()
        self.assertEqual(first, second)
        encoded = json.dumps(first, sort_keys=True)
        self.assertNotIn("CC-BY-4.0", encoded)
        self.assertNotIn("tiles.example.invalid", encoded)
        self.assertNotIn("a" * 64, encoded)

    def test_validation_attempts_no_network_access(self) -> None:
        with patch.object(
            socket.socket,
            "connect",
            side_effect=AssertionError("network access attempted"),
        ):
            report = validate_source_metadata(
                VALID_STYLE,
                manifest_path=MATCHING_MANIFEST,
                options=ValidationOptions(strict_epoch=True),
            )
        self.assertEqual(report.outcome, "ALLOW")

    def test_cli_uses_finite_exit_codes_and_json_output(self) -> None:
        validator = REPO_ROOT / "tools" / "validators" / "maplibre" / "validate_source_metadata.py"
        result = subprocess.run(
            [
                sys.executable,
                str(validator),
                str(UNMAPPED_STYLE),
                "--manifest",
                str(UNMAPPED_MANIFEST),
                "--strict-epoch",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["outcome"], "ABSTAIN")
        self.assertEqual(payload["reason_codes"], ["MANIFEST_SOURCE_UNMAPPED"])


if __name__ == "__main__":
    unittest.main()
