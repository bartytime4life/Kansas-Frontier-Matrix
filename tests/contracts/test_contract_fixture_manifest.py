"""Deterministic no-network tests for the contract fixture manifest validator."""

from __future__ import annotations

import contextlib
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from tools.validators.validate_contract_fixture_manifest import (
    main,
    serialize_json,
    validate_manifest,
)

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tests/contracts/manifests/contract_fixture_families.v1.json"
INVALID_MANIFESTS = ROOT / "tests/contracts/manifests/invalid"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("contract fixture manifest validation attempted network access")


class ContractFixtureManifestTests(unittest.TestCase):
    def _write_json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def _synthetic_repo(
        self,
        *,
        invalid_case_is_valid: bool = False,
        include_invalid_lane: bool = True,
    ) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        repo_root = Path(temporary.name)
        schema_path = (
            repo_root
            / "schemas/contracts/v1/runtime/example.schema.json"
        )
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://schemas.kfm.local/contracts/v1/runtime/example.schema.json",
            "title": "example",
            "type": "object",
            "additionalProperties": False,
            "required": ["value"],
            "properties": {"value": {"type": "integer"}},
        }
        self._write_json(schema_path, schema)

        fixture_root = repo_root / "fixtures/contracts/v1/runtime/example"
        self._write_json(
            fixture_root / "valid/valid_1.json",
            {"value": 1},
        )
        if include_invalid_lane:
            self._write_json(
                fixture_root / "invalid/invalid_1.json",
                {"value": 1 if invalid_case_is_valid else "not-an-integer"},
            )

        manifest_path = (
            repo_root
            / "tests/contracts/manifests/contract_fixture_families.v1.json"
        )
        self._write_json(
            manifest_path,
            {
                "kind": "ContractFixtureManifest",
                "manifest_version": "1.0.0",
                "wave": "wave-01-core",
                "description": "Synthetic manifest used only by the focused validator tests.",
                "families": [
                    {
                        "family": "example-family",
                        "schema_path": (
                            "schemas/contracts/v1/runtime/example.schema.json"
                        ),
                        "fixture_root": (
                            "fixtures/contracts/v1/runtime/example"
                        ),
                    }
                ],
            },
        )
        return temporary, repo_root, manifest_path

    def test_repository_manifest_passes_with_three_declared_families(self) -> None:
        report = validate_manifest(MANIFEST, repo_root=ROOT)
        self.assertEqual(report.outcome, "PASS", report.findings)
        self.assertEqual(
            [item.family for item in report.families],
            [
                "decision-envelope",
                "evidence-bundle",
                "runtime-response-envelope",
            ],
        )
        self.assertEqual(report.case_count, report.passed_case_count)
        self.assertGreaterEqual(report.case_count, 6)

    def test_repository_report_is_deterministic(self) -> None:
        first = serialize_json(validate_manifest(MANIFEST, repo_root=ROOT))
        second = serialize_json(validate_manifest(MANIFEST, repo_root=ROOT))
        self.assertEqual(first, second)

    def test_exact_manifest_negative_examples_fail_closed(self) -> None:
        expected = {
            "duplicate_family.invalid.json": "FAMILY_DUPLICATE",
            "empty_families.invalid.json": "MANIFEST_FAMILIES_EMPTY",
            "path_escape.invalid.json": "SCHEMA_PATH_INVALID",
        }
        for filename, code in expected.items():
            with self.subTest(filename=filename):
                report = validate_manifest(
                    INVALID_MANIFESTS / filename,
                    repo_root=ROOT,
                )
                self.assertEqual(report.outcome, "ERROR")
                self.assertIn(code, {item.code for item in report.findings})

    def test_schema_polarity_regression_returns_fail(self) -> None:
        temporary, repo_root, manifest_path = self._synthetic_repo(
            invalid_case_is_valid=True
        )
        self.addCleanup(temporary.cleanup)
        report = validate_manifest(manifest_path, repo_root=repo_root)
        self.assertEqual(report.outcome, "FAIL")
        self.assertEqual(report.exit_code, 1)
        self.assertIn(
            "INVALID_CASE_ACCEPTED",
            {item.code for item in report.findings},
        )

    def test_missing_invalid_lane_returns_error(self) -> None:
        temporary, repo_root, manifest_path = self._synthetic_repo(
            include_invalid_lane=False
        )
        self.addCleanup(temporary.cleanup)
        report = validate_manifest(manifest_path, repo_root=repo_root)
        self.assertEqual(report.outcome, "ERROR")
        self.assertEqual(report.exit_code, 2)
        self.assertIn("INVALID_LANE_EMPTY", {item.code for item in report.findings})

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            report = validate_manifest(MANIFEST, repo_root=ROOT)
        self.assertEqual(report.outcome, "PASS", report.findings)

    def test_cli_uses_stable_exit_codes_and_json_report(self) -> None:
        temporary, repo_root, manifest_path = self._synthetic_repo()
        self.addCleanup(temporary.cleanup)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = main(
                [
                    str(manifest_path),
                    "--repo-root",
                    str(repo_root),
                    "--format",
                    "json",
                ]
            )
        self.assertEqual(exit_code, 0)
        parsed = json.loads(output.getvalue())
        self.assertEqual(parsed["outcome"], "PASS")
        self.assertEqual(parsed["tool"], "validate-contract-fixture-manifest")
        self.assertEqual(
            parsed["authority"],
            "contract-fixture-inventory-and-schema-polarity-only",
        )

    def test_cli_does_not_echo_fixture_values(self) -> None:
        temporary, repo_root, manifest_path = self._synthetic_repo(
            invalid_case_is_valid=True
        )
        self.addCleanup(temporary.cleanup)
        marker = "synthetic-sensitive-value-that-must-not-be-echoed"
        manifest_value = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_value["description"] = marker
        self._write_json(manifest_path, manifest_value)

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = main(
                [
                    str(manifest_path),
                    "--repo-root",
                    str(repo_root),
                    "--format",
                    "json",
                ]
            )
        self.assertEqual(exit_code, 1)
        self.assertNotIn(marker, output.getvalue())


if __name__ == "__main__":
    unittest.main()
