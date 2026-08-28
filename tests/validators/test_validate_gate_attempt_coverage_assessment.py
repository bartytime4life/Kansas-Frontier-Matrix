from __future__ import annotations

import ast
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_gate_attempt_coverage_assessment.py"
BUILDER_PATH = REPO_ROOT / "tools/generators/gate_attempt_coverage_assessment/build_gate_attempt_coverage_assessment.py"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/validation/gate_attempt_coverage_assessment/cases.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/validation/gate_attempt_coverage_assessment.schema.json"
VALIDATOR = load_module("test_gate_attempt_coverage_validator", VALIDATOR_PATH)
BUILDER = load_module("test_gate_attempt_coverage_builder", BUILDER_PATH)


class GateAttemptCoverageAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.documents = {case["case_id"]: BUILDER.build_case(case) for case in cls.suite["cases"]}

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_fixture_polarity(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 13)

    def test_attempt_population_reconciles_without_dropping_refusals(self) -> None:
        document = self.documents["valid-accounted-with-refusal-and-unobserved"]
        counts = document["counts"]
        self.assertEqual(counts["attempted"], counts["admitted"] + counts["refused"] + counts["error"] + counts["unobserved"])
        self.assertEqual(counts, {"attempted": 5, "admitted": 2, "refused": 1, "error": 1, "unobserved": 1})
        self.assertEqual(document["terminal_coverage_state"], "INCOMPLETE")
        self.assertEqual(VALIDATOR.validate_document(document).outcome, "PASS")

    def test_refusal_is_not_action_evidence_or_same_gate_feedback(self) -> None:
        refusal = self.documents["valid-accounted-with-refusal-and-unobserved"]["class_semantics"]["REFUSED"]
        self.assertEqual(refusal["guarded_action_occurrence"], "DID_NOT_OCCUR")
        self.assertFalse(refusal["same_gate_feedback_allowed"])

    def test_signature_domains_are_distinct_by_attempt_class(self) -> None:
        classes = self.documents["valid-accounted-with-refusal-and-unobserved"]["attempt_classes"]
        domains = {
            class_name: {row["signature_domain"] for row in rows}
            for class_name, rows in classes.items()
        }
        self.assertEqual(domains, {
            "admitted": {"kfm.gate.attempt.admitted.v1"},
            "refused": {"kfm.gate.attempt.refused.v1"},
            "error": {"kfm.gate.attempt.error.v1"},
            "unobserved": {"kfm.gate.attempt.unobserved.v1"},
        })

    def test_denominator_policies_partition_all_classes(self) -> None:
        document = self.documents["valid-accounted-with-refusal-and-unobserved"]
        all_classes = {"ADMITTED", "ERROR", "REFUSED", "UNOBSERVED"}
        for policy in document["denominator_policies"]:
            included = set(policy["included_classes"])
            excluded = set(policy["excluded_classes"])
            self.assertFalse(included.intersection(excluded))
            self.assertEqual(included.union(excluded), all_classes)
        admission_policy = document["denominator_policies"][0]
        self.assertIn("REFUSED", admission_policy["included_classes"])
        self.assertEqual(admission_policy["denominator_count"], 5)

    def test_builder_and_validator_have_no_network_or_write_surface(self) -> None:
        imports: set[str] = set()
        attributes: set[str] = set()
        for path in (BUILDER_PATH, VALIDATOR_PATH):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
                elif isinstance(node, ast.Attribute):
                    attributes.add(node.attr)
        self.assertTrue({"socket", "requests", "urllib", "httpx", "subprocess"}.isdisjoint(imports))
        self.assertTrue({"write_text", "write_bytes", "unlink", "rename", "replace"}.isdisjoint(attributes))

    def test_symlink_candidate_is_rejected(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symlink support unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary) / "candidate.json"
            try:
                candidate.symlink_to(FIXTURE_PATH)
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = VALIDATOR.validate_file(candidate)
        self.assertEqual(result.outcome, "ERROR")

    def test_clis_are_deterministic(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        commands = [
            [sys.executable, str(BUILDER_PATH), "--case", "valid-accounted-with-refusal-and-unobserved"],
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
        ]
        for command in commands:
            first = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
            second = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)
            json.loads(first.stdout)


if __name__ == "__main__":
    unittest.main()
