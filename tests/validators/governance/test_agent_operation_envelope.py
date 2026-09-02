from __future__ import annotations

import ast
import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/governance/validate_agent_operation_envelope.py"
)
BUILDER_PATH = (
    REPO_ROOT
    / "tools/generators/agent_operation_envelope/build_agent_operation_envelope.py"
)
VALIDATOR = load_module("test_agent_operation_envelope_validator", VALIDATOR_PATH)
BUILDER = load_module("test_agent_operation_envelope_builder", BUILDER_PATH)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/agent_operation_envelope/cases.json"
)


class AgentOperationEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.case_by_id = {case["case_id"]: case for case in cls.suite["cases"]}
        cls.by_id = {
            case_id: BUILDER.build_case(case)
            for case_id, case in cls.case_by_id.items()
        }

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/governance/agent_operation_envelope.schema.json"
            ).read_text(encoding="utf-8")
        )
        Draft202012Validator.check_schema(schema)

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 13)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_pinned_valid_operation_ids_match_generated_documents(self) -> None:
        for case in self.suite["cases"]:
            expected = case.get("expected_operation_id")
            if expected is not None:
                self.assertEqual(BUILDER.build_case(case)["operation_id"], expected)

    def test_each_role_accepts_only_its_declared_boundary(self) -> None:
        watcher = self.by_id["valid-watcher-ready"]
        planner = self.by_id["valid-planner-ready"]
        executor = self.by_id["valid-executor-ready"]

        self.assertEqual(VALIDATOR.validate_document(watcher).outcome, "PASS")
        self.assertEqual(watcher["credential_ceiling"], "READ_ONLY")
        self.assertFalse(watcher["capability_ceiling"]["draft_pr_write"])

        self.assertEqual(VALIDATOR.validate_document(planner).outcome, "PASS")
        self.assertTrue(planner["capability_ceiling"]["emit_plan"])
        self.assertFalse(planner["capability_ceiling"]["feature_branch_write"])

        self.assertEqual(VALIDATOR.validate_document(executor).outcome, "PASS")
        self.assertTrue(executor["capability_ceiling"]["draft_pr_write"])
        self.assertFalse(executor["capability_ceiling"]["merge"])
        self.assertFalse(executor["target"]["head_is_protected"])
        self.assertTrue(executor["target"]["draft"])

    def test_kill_switch_holds_planner_without_invalidating_record(self) -> None:
        document = self.by_id["valid-planner-kill-switch-hold"]
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(document["disposition"]["outcome"], "HOLD")
        self.assertEqual(document["disposition"]["reason_codes"], ["KILL_SWITCH_ENGAGED"])

    def test_gate_denial_and_error_remain_finite_valid_outcomes(self) -> None:
        denied = self.by_id["valid-executor-policy-deny"]
        errored = self.by_id["valid-executor-gate-error"]
        self.assertEqual(VALIDATOR.validate_document(denied).outcome, "PASS")
        self.assertEqual(denied["disposition"]["outcome"], "DENY")
        self.assertEqual(VALIDATOR.validate_document(errored).outcome, "PASS")
        self.assertEqual(errored["disposition"]["outcome"], "ERROR")

    def test_executor_protected_branch_or_merge_scope_is_denied(self) -> None:
        document = copy.deepcopy(self.by_id["valid-executor-ready"])
        document["target"]["head_is_protected"] = True
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual({finding.code for finding in result.findings}, {"SCHEMA_INVALID"})

        document = copy.deepcopy(self.by_id["valid-executor-ready"])
        document["capability_ceiling"]["merge"] = True
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual({finding.code for finding in result.findings}, {"SCHEMA_INVALID"})

    def test_identity_and_idempotency_are_deterministic(self) -> None:
        document = self.by_id["valid-planner-ready"]
        first = VALIDATOR.expected_identity(document)
        second = VALIDATOR.expected_identity(copy.deepcopy(document))
        self.assertEqual(first, second)
        self.assertEqual(document["spec_hash"], first[0])
        self.assertEqual(document["operation_id"], first[1])
        self.assertEqual(
            document["operation"]["idempotency_key"],
            VALIDATOR.expected_idempotency_key(document),
        )

    def test_semantic_overreach_is_denied_even_with_recomputed_identity(self) -> None:
        document = self.by_id["invalid-planner-pr-output"]
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"OUTPUT_KIND_NOT_ALLOWED"},
        )

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
        self.assertTrue(
            {"socket", "requests", "urllib", "httpx", "subprocess"}.isdisjoint(imports)
        )
        self.assertTrue(
            {"write_text", "write_bytes", "unlink", "rename", "replace"}.isdisjoint(attributes)
        )

    def test_symlink_candidate_is_rejected(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symlink support unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            link = Path(temporary) / "candidate.json"
            try:
                link.symlink_to(FIXTURE_PATH)
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = VALIDATOR.validate_file(link)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual([finding.code for finding in result.findings], ["INPUT_JSON_INVALID"])

    def test_builder_and_fixture_clis_are_deterministic(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        commands = [
            [sys.executable, str(BUILDER_PATH), "--case", "valid-executor-ready"],
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
        ]
        for command in commands:
            first = subprocess.run(
                command,
                cwd=REPO_ROOT,
                env=environment,
                check=False,
                capture_output=True,
                text=True,
            )
            second = subprocess.run(
                command,
                cwd=REPO_ROOT,
                env=environment,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first.stdout, second.stdout)
            json.loads(first.stdout)


if __name__ == "__main__":
    unittest.main()
