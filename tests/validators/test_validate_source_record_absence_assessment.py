from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_source_record_absence_assessment.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_record_absence_assessment"
VALID_ROOT = FIXTURE_ROOT / "valid"
INVALID_ROOT = FIXTURE_ROOT / "invalid"
MANIFEST_PATH = INVALID_ROOT / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location(
    "validate_source_record_absence_assessment",
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


class SourceRecordAbsenceAssessmentTests(unittest.TestCase):
    def test_fixture_inventory_is_exact(self) -> None:
        self.assertEqual(
            [
                "valid_complete_snapshot_removal_candidate.json",
                "valid_incremental_feed_retain_prior.json",
                "valid_mixed_surface_abstain.json",
                "valid_publication_page_abstain.json",
                "valid_source_error.json",
            ],
            sorted(path.name for path in VALID_ROOT.glob("*.json")),
        )
        self.assertEqual(
            [
                "expected_findings_manifest.json",
                "invalid_missing_record_key_hash.json",
                "semantic_invalid_assessment_id.json",
                "semantic_invalid_governance_overreach.json",
                "semantic_invalid_history_deletion.json",
                "semantic_invalid_incremental_false_clear.json",
                "semantic_invalid_publication_page_removal.json",
                "semantic_invalid_removal_without_completeness.json",
                "semantic_invalid_spec_hash.json",
                "semantic_invalid_temporal_order.json",
                "semantic_invalid_unsorted_refs.json",
            ],
            sorted(path.name for path in INVALID_ROOT.glob("*.json")),
        )

    def test_valid_fixtures_pass(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertTrue(validator.validate_assessment(path).ok)

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
                result = validator.validate_assessment(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertEqual(expected[path.name], actual)

    def test_semantic_negative_vectors_remain_schema_valid(self) -> None:
        for path in sorted(INVALID_ROOT.glob("semantic_invalid_*.json")):
            with self.subTest(path=path.name):
                self.assertEqual([], validator._schema_findings(load_json(path)))

    def test_fixture_entrypoint_passes(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(0, validator.validate_fixtures())
        self.assertIn(
            "CONFIRMED: 5 valid and 10 invalid source record absence fixtures passed exact polarity.",
            stdout.getvalue(),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"SourceRecordAbsenceAssessment","object_type":"other"}',
                encoding="utf-8",
            )
            result = validator.validate_assessment(path)
            self.assertIn(
                "JSON_DUPLICATE_KEY",
                {finding.code for finding in result.findings},
            )
            self.assertTrue(result.error)

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"parse_confidence":NaN}', encoding="utf-8")
            result = validator.validate_assessment(path)
            self.assertIn(
                "JSON_NONFINITE_NUMBER",
                {finding.code for finding in result.findings},
            )
            self.assertTrue(result.error)

    def test_cli_does_not_echo_candidate_values(self) -> None:
        marker = "SENSITIVE_RECORD_IDENTIFIER_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"raw_record_id": marker}), encoding="utf-8")
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

    def test_spec_hash_is_deterministic(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                candidate = load_json(path)
                expected = validator.canonical_spec_hash(candidate)
                self.assertEqual(candidate["spec_hash"], expected)
                self.assertEqual(expected, validator.canonical_spec_hash(candidate))

    def test_assessment_id_is_deterministic(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                candidate = load_json(path)
                expected = validator.canonical_assessment_id(candidate)
                self.assertEqual(candidate["assessment_id"], expected)
                self.assertEqual(expected, validator.canonical_assessment_id(candidate))

    def test_valid_outcomes_cover_all_finite_states(self) -> None:
        outcomes = {
            load_json(path)["decision"]["outcome"]
            for path in VALID_ROOT.glob("*.json")
        }
        self.assertEqual(
            {"REMOVAL_CANDIDATE", "RETAIN_PRIOR_STATE", "ABSTAIN", "ERROR"},
            outcomes,
        )

    def test_incremental_absence_retains_prior_state(self) -> None:
        candidate = load_json(VALID_ROOT / "valid_incremental_feed_retain_prior.json")
        self.assertEqual("RETAIN_PRIOR_STATE", candidate["decision"]["outcome"])
        self.assertTrue(candidate["decision"]["retain_prior_state"])
        self.assertIsNone(candidate["decision"]["transition_candidate_ref"])

    def test_validator_performs_no_network_access(self) -> None:
        path = VALID_ROOT / "valid_complete_snapshot_removal_candidate.json"
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            self.assertTrue(validator.validate_assessment(path).ok)


if __name__ == "__main__":
    unittest.main()
