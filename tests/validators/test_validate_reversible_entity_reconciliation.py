from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_reversible_entity_reconciliation.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/common/reversible_entity_reconciliation"
VALID_ROOT = FIXTURE_ROOT / "valid"
INVALID_ROOT = FIXTURE_ROOT / "invalid"
MANIFEST_PATH = INVALID_ROOT / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location(
    "validate_reversible_entity_reconciliation",
    MODULE_PATH,
)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must contain a JSON object")
    return value


class ReversibleEntityReconciliationTests(unittest.TestCase):
    def test_fixture_inventory_is_exact(self) -> None:
        self.assertEqual(
            ["valid_reconciliation_packet.json"],
            sorted(path.name for path in VALID_ROOT.glob("*.json")),
        )
        self.assertEqual(
            [
                "expected_findings_manifest.json",
                "invalid_automatic_merge.json",
                "invalid_cluster_without_match.json",
                "invalid_spec_hash.json",
                "invalid_split_partition.json",
            ],
            sorted(path.name for path in INVALID_ROOT.glob("*.json")),
        )

    def test_valid_fixtures_pass(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertTrue(validator.validate_packet(path).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        expected = load_json(MANIFEST_PATH)
        invalid_paths = sorted(
            path
            for path in INVALID_ROOT.glob("*.json")
            if path.name != MANIFEST_PATH.name
        )
        self.assertEqual(sorted(expected), [path.name for path in invalid_paths])
        for path in invalid_paths:
            with self.subTest(path=path.name):
                result = validator.validate_packet(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertEqual(expected[path.name], actual)

    def test_fixture_entrypoint_passes(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(0, validator.validate_fixtures())
        self.assertIn(
            "CONFIRMED: 1 valid and 4 invalid reconciliation fixtures passed exact polarity.",
            stdout.getvalue(),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"x","object_type":"y"}',
                encoding="utf-8",
            )
            result = validator.validate_packet(path)
            self.assertIn(
                "JSON_DUPLICATE_KEY",
                {finding.code for finding in result.findings},
            )
            self.assertTrue(result.error)

    def test_cli_does_not_echo_candidate_values(self) -> None:
        marker = "UNIQUE_ENTITY_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"marker": marker}), encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(MODULE_PATH), str(path)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(0, run.returncode)
            self.assertNotIn(marker, run.stdout)
            self.assertNotIn(marker, run.stderr)

    def test_hash_is_deterministic(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                candidate = load_json(path)
                expected = validator.canonical_spec_hash(candidate)
                self.assertEqual(candidate["spec_hash"], expected)
                self.assertEqual(expected, validator.canonical_spec_hash(candidate))

    def test_valid_fixtures_are_schema_valid(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertEqual([], validator._schema_findings(load_json(path)))


if __name__ == "__main__":
    unittest.main()
