from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/governance/validate_model_card_envelope.py"
SPEC = importlib.util.spec_from_file_location("model_card_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ModelCardEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base, cases, paths = MODULE.load_fixture_suite()
        cls.suite = {"base": base, "cases": cases}
        cls.paths = paths
        cls.by_id = {item["case_id"]: item for item in cases}

    def build(self, case_id: str):
        return MODULE.build_fixture_case(self.by_id[case_id], self.suite["base"])

    def test_fixture_suite_exact(self) -> None:
        ok, report = MODULE.run_fixture_suite()
        self.assertTrue(ok)
        self.assertEqual(report["counts"], {"PASS": 1, "FAIL": 10, "ERROR": 0, "HOLD": 1, "DENY": 1})
        self.assertTrue(all(item["ok"] for item in report["cases"]))

    def test_fixture_files_match_case_ids(self) -> None:
        self.assertEqual(
            [path.stem for path in self.paths],
            [case["case_id"] for case in self.suite["cases"]],
        )

    def test_valid_finite_states(self) -> None:
        for case_id, outcome in (
            ("pass-climate-reconstruction", "PASS"),
            ("hold-focus-mode-narrative", "HOLD"),
            ("deny-sensitive-alignment", "DENY"),
        ):
            with self.subTest(case_id=case_id):
                result = MODULE.validate_document(self.build(case_id))
                self.assertEqual(result.outcome, outcome)
                self.assertEqual(result.findings, ())

    def test_negative_cases_are_exact(self) -> None:
        for case in self.suite["cases"]:
            if not case["case_id"].startswith("invalid-"):
                continue
            with self.subTest(case_id=case["case_id"]):
                result = MODULE.validate_document(MODULE.build_fixture_case(case, self.suite["base"]))
                self.assertEqual(result.outcome, "FAIL")
                self.assertEqual(sorted({f.code for f in result.findings}), case["expected"]["finding_codes"])

    def test_hash_is_deterministic(self) -> None:
        candidate = self.build("pass-climate-reconstruction")
        self.assertEqual(MODULE.expected_spec_hash(candidate), candidate["spec_hash"])
        self.assertEqual(MODULE.expected_spec_hash(candidate), MODULE.expected_spec_hash(copy.deepcopy(candidate)))

    def test_model_output_never_claims_observation_or_authority(self) -> None:
        candidate = self.build("pass-climate-reconstruction")
        self.assertFalse(candidate["reality_boundary"]["observation_claim_allowed"])
        self.assertFalse(candidate["reality_boundary"]["operational_authority"])
        self.assertFalse(candidate["reality_boundary"]["publication_authority"])
        self.assertFalse(any(candidate["authority_limits"].values()))

    def test_unknown_property_fails_schema(self) -> None:
        candidate = self.build("pass-climate-reconstruction")
        candidate["invented_authority"] = True
        candidate["spec_hash"] = MODULE.expected_spec_hash(candidate)
        result = MODULE.validate_document(candidate)
        self.assertEqual(result.outcome, "FAIL")
        self.assertIn("SCHEMA_INVALID", {f.code for f in result.findings})

    def test_duplicate_json_key_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
            result = MODULE.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings[0].code, "INPUT_JSON_INVALID")

    def test_candidate_cli_exit_codes(self) -> None:
        expected = {"pass-climate-reconstruction": 0, "hold-focus-mode-narrative": 3, "deny-sensitive-alignment": 4}
        with tempfile.TemporaryDirectory() as directory:
            for case_id, exit_code in expected.items():
                path = Path(directory) / f"{case_id}.json"
                path.write_text(json.dumps(self.build(case_id), sort_keys=True), encoding="utf-8")
                run = subprocess.run([sys.executable, str(MODULE_PATH), "--candidate", str(path)], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
                self.assertEqual(run.returncode, exit_code, run.stderr)
                self.assertEqual(json.loads(run.stdout)["outcome"], MODULE.validate_document(self.build(case_id)).outcome)

    def test_fixture_cli_succeeds(self) -> None:
        run = subprocess.run([sys.executable, str(MODULE_PATH), "--fixtures"], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertTrue(json.loads(run.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
