from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/validate_occurrence_retrieval_query_safety.py"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/source/occurrence_retrieval_snapshot/query_safety"
)

SPEC = importlib.util.spec_from_file_location(
    "validate_occurrence_retrieval_query_safety",
    VALIDATOR_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class OccurrenceRetrievalQuerySafetyTests(unittest.TestCase):
    def test_valid_fixture_passes(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 1)
        self.assertTrue(MODULE.validate_query_safety(paths[0]).ok)

    def test_semantic_invalid_fixtures_match_manifest_exactly(self) -> None:
        invalid_root = FIXTURE_ROOT / "semantic_invalid"
        manifest = json.loads(
            (invalid_root / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        paths = sorted(invalid_root.glob("semantic_invalid_*.json"))
        self.assertEqual(len(paths), 2)
        self.assertEqual(set(manifest), {path.name for path in paths})
        for path in paths:
            with self.subTest(path=path.name):
                result = MODULE.validate_query_safety(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertFalse(result.ok)
                self.assertEqual(actual, sorted(manifest[path.name]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        self.assertEqual(MODULE.main(["--fixtures"]), 0)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"OccurrenceRetrievalSnapshotCandidate",'
                '"object_type":"OccurrenceRetrievalSnapshotCandidate"}',
                encoding="utf-8",
            )
            result = MODULE.validate_query_safety(path)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_DUPLICATE_KEY"},
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_query_safety(path)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_NONFINITE_NUMBER"},
        )

    def test_diagnostics_do_not_echo_sensitive_values(self) -> None:
        untrusted = "reviewer@example.test"
        candidate = {
            "object_type": "OccurrenceRetrievalSnapshotCandidate",
            "query_snapshot": {
                "predicates": [
                    {
                        "field": "notification_target",
                        "operator": "equals",
                        "value": untrusted,
                    }
                ]
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            result = MODULE.validate_query_safety(path)
            report = MODULE._serialize(path, result)
        self.assertIn("OCCURRENCE_RETRIEVAL_QUERY_EMAIL_VALUE_DENIED", report)
        self.assertNotIn(untrusted, report)

    def test_nested_secret_marker_is_rejected(self) -> None:
        candidate = {
            "object_type": "OccurrenceRetrievalSnapshotCandidate",
            "query_snapshot": {
                "predicates": [
                    {
                        "field": "request_note",
                        "operator": "in",
                        "value": ["reviewed", "authorization: Bearer SYNTHETIC"],
                    }
                ]
            },
        }
        findings = MODULE._semantic_findings(candidate)
        self.assertEqual(
            {finding.code for finding in findings},
            {"OCCURRENCE_RETRIEVAL_QUERY_SECRET_VALUE_DENIED"},
        )

    def test_replay_is_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_no_sensitive_query_values.json"
        first = MODULE._serialize(path, MODULE.validate_query_safety(path))
        second = MODULE._serialize(path, MODULE.validate_query_safety(path))
        self.assertEqual(first, second)

    def test_validator_imports_no_network_client(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        for token in (
            "import requests",
            "import httpx",
            "import urllib.request",
            "import socket",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
