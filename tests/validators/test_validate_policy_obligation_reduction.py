from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/policy/validate_policy_obligation_reduction.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/policy/policy_obligation_reduction.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/policy/policy_obligation_reduction"
)

SPEC = importlib.util.spec_from_file_location(
    "validate_policy_obligation_reduction",
    VALIDATOR_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyObligationReductionValidatorTests(unittest.TestCase):
    def _load(self, relative: str) -> dict[str, object]:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(
            schema["x-kfm"]["algorithm"],
            "kfm-policy-obligation-max-severity-v1",
        )

    def test_all_valid_fixtures_pass(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 5)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)

    def test_manifest_has_exact_reviewed_polarity(self) -> None:
        manifest = self._load("expected_findings_manifest.json")
        cases = manifest["cases"]
        self.assertEqual(len(cases), 18)
        self.assertEqual(
            len({case["case_id"] for case in cases}),
            len(cases),
        )
        for case in cases:
            path = FIXTURE_ROOT / case["record"]
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_record(path)
                actual_outcome = (
                    "PASS"
                    if result.ok
                    else ("ERROR" if result.error else "FAIL")
                )
                actual_codes = sorted(
                    {finding.code for finding in result.findings}
                )
                self.assertEqual(actual_outcome, case["expected_outcome"])
                self.assertEqual(actual_codes, case["expected_findings"])

    def test_schema_and_semantic_negative_names_do_not_collide(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
        schema_invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        semantic_invalid = sorted(
            (FIXTURE_ROOT / "invalid").glob("semantic_invalid_*.json")
        )
        self.assertEqual(len(schema_invalid), 4)
        self.assertEqual(len(semantic_invalid), 9)
        for path in schema_invalid:
            self.assertTrue(
                list(
                    validator.iter_errors(
                        json.loads(path.read_text(encoding="utf-8"))
                    )
                ),
                path.name,
            )
        for path in semantic_invalid:
            self.assertFalse(
                list(
                    validator.iter_errors(
                        json.loads(path.read_text(encoding="utf-8"))
                    )
                ),
                path.name,
            )

    def test_reducer_uses_maximum_severity_for_every_dimension(self) -> None:
        candidate = self._load("valid/valid_full_suppress.json")
        reduced = MODULE.reduce_obligations(candidate["inputs"])
        self.assertEqual(reduced["transform"], "SUPPRESS")
        self.assertEqual(reduced["generalize_distance_m"], 5000)
        self.assertEqual(reduced["date_fuzz_days"], 7300)
        self.assertTrue(reduced["suppress_geometry"])
        self.assertEqual(reduced["embargo_until"], "2035-12-31")
        self.assertEqual(reduced, candidate["result"])

    def test_reducer_is_order_independent_and_does_not_mutate(self) -> None:
        candidate = self._load("valid/valid_mixed_maxima.json")
        original = copy.deepcopy(candidate["inputs"])
        forward = MODULE.reduce_obligations(candidate["inputs"])
        reverse = MODULE.reduce_obligations(
            list(reversed(candidate["inputs"]))
        )
        self.assertEqual(forward, reverse)
        self.assertEqual(candidate["inputs"], original)

    def test_replay_is_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_geometry_suppression.json"
        first = MODULE._serialize(path, MODULE.validate_record(path))
        second = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertEqual(first, second)
        candidate = self._load("valid/valid_geometry_suppression.json")
        self.assertEqual(
            MODULE.reduce_obligations(candidate["inputs"]),
            MODULE.reduce_obligations(candidate["inputs"]),
        )

    def test_empty_reduction_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.reduce_obligations([])

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"PolicyObligationReduction",'
                '"object_type":"PolicyObligationReduction"}',
                encoding="utf-8",
            )
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_DUPLICATE_KEY"},
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_NONFINITE_NUMBER"},
        )

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertTrue(result.error)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"FILE_NOT_FOUND"},
        )

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._load("valid/valid_none_embargo.json")
        untrusted = "UNTRUSTED_SUBJECT_VALUE_DO_NOT_ECHO"
        candidate["subject_ref"] = untrusted
        candidate["schema_negative_canary"] = True
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        candidate["reduction_id"] = MODULE.compute_reduction_id(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_shared_hash_and_reduction_id_reproduce_fixture(self) -> None:
        candidate = self._load("valid/valid_mixed_maxima.json")
        self.assertEqual(
            MODULE.compute_record_spec_hash(candidate),
            candidate["spec_hash"],
        )
        self.assertEqual(
            MODULE.compute_reduction_id(candidate),
            candidate["reduction_id"],
        )
        self.assertRegex(candidate["spec_hash"], r"^sha256:[0-9a-f]{64}$")

    def test_fixture_suite_is_no_network_and_cli_is_deterministic(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network access denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access denied"),
        ):
            ok, first_lines = MODULE.validate_fixture_suite()
            second_ok, second_lines = MODULE.validate_fixture_suite()
        self.assertTrue(ok)
        self.assertTrue(second_ok)
        self.assertEqual(first_lines, second_lines)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            completed.returncode,
            0,
            completed.stdout + completed.stderr,
        )
        self.assertEqual(len(completed.stdout.splitlines()), 18)
        self.assertNotIn("suite_match\":false", completed.stdout)


if __name__ == "__main__":
    unittest.main()
