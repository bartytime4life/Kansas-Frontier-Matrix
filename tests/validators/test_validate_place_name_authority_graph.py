from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_place_name_authority_graph.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph.schema.json"
FIXTURE_PROFILE_PATH = REPO_ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/place_name_authority_graph/fixture_profile.json"

SPEC = importlib.util.spec_from_file_location("validator_under_test", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _profile() -> dict[str, object]:
    return json.loads(FIXTURE_PROFILE_PATH.read_text(encoding="utf-8"))


class PlaceNameAuthorityGraphValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED")
        self.assertFalse(schema["additionalProperties"])

    def test_all_valid_fixture_vectors_pass(self) -> None:
        profile = _profile()
        cases = profile["valid"]
        self.assertEqual(len(cases), 4)
        for name, case in sorted(cases.items()):
            with self.subTest(name=name):
                candidate = MODULE.materialize_fixture(case, profile)
                self.assertTrue(MODULE.validate_candidate(candidate).ok)

    def test_invalid_fixture_vectors_match_exact_reviewed_codes(self) -> None:
        profile = _profile()
        cases = profile["invalid"]
        self.assertEqual(len(cases), 10)
        for name, case in sorted(cases.items()):
            with self.subTest(name=name):
                candidate = MODULE.materialize_fixture(case, profile)
                result = MODULE.validate_candidate(candidate)
                actual = sorted({finding.code for finding in result.findings})
                self.assertFalse(result.ok)
                self.assertEqual(actual, sorted(case["expected_findings"]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertEqual(completed.stdout.count('"outcome":"PASS"'), 4)
        self.assertEqual(completed.stdout.count('"outcome":"FAIL"'), 10)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"PlaceNameAuthorityGraphPacket","object_type":"PlaceNameAuthorityGraphPacket"}',
                encoding="utf-8",
            )
            result = MODULE.validate_record(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertTrue(result.error)
        self.assertEqual({finding.code for finding in result.findings}, {"FILE_NOT_FOUND"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        profile = _profile()
        candidate = MODULE.materialize_fixture(
            profile["valid"]["valid_translation_alias.json"], profile
        )
        untrusted_value = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        candidate["untrusted_negative_canary"] = untrusted_value
        candidate["spec_hash"] = MODULE._hash(candidate)
        result = MODULE.validate_candidate(candidate)
        report = MODULE._report(Path("candidate.json"), result)
        self.assertNotIn(untrusted_value, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_patch_profile_replay_is_deterministic(self) -> None:
        profile = _profile()
        case = profile["invalid"]["semantic_invalid_alias_cycle.json"]
        first = MODULE.materialize_fixture(case, profile)
        second = MODULE.materialize_fixture(case, profile)
        self.assertEqual(first, second)
        self.assertEqual(MODULE.validate_candidate(first), MODULE.validate_candidate(second))


if __name__ == "__main__":
    unittest.main()
