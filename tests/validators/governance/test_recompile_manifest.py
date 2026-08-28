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

from hashing import canonicalize_json  # noqa: E402


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


COMPILER_PATH = (
    REPO_ROOT / "tools/generators/recompile_manifest/compile_recompile_manifest.py"
)
VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/governance/validate_recompile_manifest.py"
)
QUERY_VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/governance/validate_query_run_record.py"
)
COMPILER = load_module("test_recompile_compiler", COMPILER_PATH)
VALIDATOR = load_module("test_recompile_validator", VALIDATOR_PATH)
QUERY_VALIDATOR = load_module("test_recompile_query_validator", QUERY_VALIDATOR_PATH)
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/recompile_manifest"
PROPOSAL_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/ai_change_proposal"


class RecompileManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.query = json.loads((FIXTURE_ROOT / "query_ready.json").read_text())
        cls.unbound_query = json.loads((FIXTURE_ROOT / "query_unbound.json").read_text())
        cls.subject = json.loads((PROPOSAL_ROOT / "subjects/base.json").read_text())
        cls.ready_proposal = json.loads(
            (PROPOSAL_ROOT / "valid/valid_ready.json").read_text()
        )
        cls.pending_proposal = json.loads(
            (PROPOSAL_ROOT / "valid/valid_hold_pending_review.json").read_text()
        )
        cls.denied_proposal = json.loads(
            (PROPOSAL_ROOT / "valid/valid_deny_policy.json").read_text()
        )
        cls.expected_candidate = json.loads(
            (FIXTURE_ROOT / "expected_candidate.json").read_text()
        )
        cls.expected_manifest = json.loads(
            (FIXTURE_ROOT / "expected_manifest.json").read_text()
        )

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/governance/recompile_manifest.schema.json"
            ).read_text()
        )
        Draft202012Validator.check_schema(schema)

    def test_ready_compile_matches_exact_candidate_and_manifest(self) -> None:
        result = COMPILER.compile_documents(
            self.query,
            self.ready_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
        )
        self.assertEqual(result.outcome, "COMPILED_CANDIDATE")
        self.assertEqual(result.findings, ())
        self.assertEqual(result.candidate, self.expected_candidate)
        self.assertEqual(result.manifest, self.expected_manifest)
        self.assertEqual(result.candidate_bytes, canonicalize_json(self.expected_candidate))

    def test_replay_validator_accepts_exact_fixture(self) -> None:
        result = VALIDATOR.validate_documents(
            self.expected_manifest,
            self.expected_candidate,
            self.query,
            self.ready_proposal,
            self.subject,
        )
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(result.findings, ())

    def test_query_with_partial_evidence_holds(self) -> None:
        query = copy.deepcopy(self.query)
        query["candidate_proposal_refs"] = []
        query["evidence_resolution"] = {
            "summary": "PARTIAL",
            "items": [
                {
                    "evidence_bundle_ref": None,
                    "evidence_ref": "kfm:evidence-ref:"
                    + "3" * 64,
                    "status": "UNRESOLVED",
                }
            ],
        }
        query["outcome"] = "ABSTAIN"
        query["reason_codes"] = [
            "EVIDENCE_UNRESOLVED",
            "FIXTURE_ONLY",
            "NO_CANDIDATE_DELTA",
            "QUERY_VALIDATED",
        ]
        hashes = QUERY_VALIDATOR._expected_hashes(query)
        query["hashes"] = {
            "algorithm": "SHA-256",
            "canonicalization": "RFC8785-JCS",
            **hashes,
        }
        query["query_run_id"] = (
            "kfm:query-run:" + hashes["run_hash"].removeprefix("sha256:")
        )
        self.assertEqual(QUERY_VALIDATOR.validate_document(query).outcome, "PASS")
        result = COMPILER.compile_documents(
            query,
            self.ready_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
        )
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual([finding.code for finding in result.findings], ["QUERY_NOT_READY"])

    def _query_for_proposal(self, proposal_id: str) -> dict[str, object]:
        query = copy.deepcopy(self.query)
        query["candidate_proposal_refs"] = [proposal_id]
        hashes = QUERY_VALIDATOR._expected_hashes(query)
        query["hashes"] = {
            "algorithm": "SHA-256",
            "canonicalization": "RFC8785-JCS",
            **hashes,
        }
        query["query_run_id"] = (
            "kfm:query-run:" + hashes["run_hash"].removeprefix("sha256:")
        )
        self.assertEqual(QUERY_VALIDATOR.validate_document(query).outcome, "PASS")
        return query

    def test_pending_review_holds(self) -> None:
        result = COMPILER.compile_documents(
            self._query_for_proposal(self.pending_proposal["proposal_id"]),
            self.pending_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
        )
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["PROPOSAL_NOT_READY"],
        )

    def test_policy_denied_proposal_is_denied(self) -> None:
        result = COMPILER.compile_documents(
            self._query_for_proposal(self.denied_proposal["proposal_id"]),
            self.denied_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual([finding.code for finding in result.findings], ["PROPOSAL_DENIED"])

    def test_unbound_proposal_is_denied(self) -> None:
        result = COMPILER.compile_documents(
            self.unbound_query,
            self.ready_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["PROPOSAL_NOT_BOUND_TO_QUERY"],
        )

    def test_published_target_is_denied_before_compilation(self) -> None:
        result = COMPILER.compile_documents(
            self.query,
            self.ready_proposal,
            self.subject,
            compiled_at="2026-08-06T23:05:00Z",
            target_stage="PUBLISHED",
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["TARGET_STAGE_NOT_ALLOWED"],
        )

    def test_symlink_subject_is_rejected(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symlink support unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            link = Path(temporary) / "subject.json"
            try:
                link.symlink_to(PROPOSAL_ROOT / "subjects/base.json")
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = COMPILER.compile_files(
                FIXTURE_ROOT / "query_ready.json",
                PROPOSAL_ROOT / "valid/valid_ready.json",
                link,
                compiled_at="2026-08-06T23:05:00Z",
            )
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["SUBJECT_JSON_INVALID"],
        )

    def test_manifest_drift_fails_closed(self) -> None:
        manifest = copy.deepcopy(self.expected_manifest)
        manifest["rollback"]["content_spec_hash"] = "sha256:" + "f" * 64
        result = VALIDATOR.validate_documents(
            manifest,
            self.expected_candidate,
            self.query,
            self.ready_proposal,
            self.subject,
        )
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            codes,
            {
                "MANIFEST_ID_MISMATCH",
                "MANIFEST_SPEC_HASH_MISMATCH",
                "ROLLBACK_BINDING_MISMATCH",
            },
        )

    def test_compiler_has_no_network_or_file_write_surface(self) -> None:
        tree = ast.parse(COMPILER_PATH.read_text(encoding="utf-8"))
        imports: set[str] = set()
        attributes: set[str] = set()
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
            {"write_text", "write_bytes", "unlink", "rename"}.isdisjoint(attributes)
        )

    def test_fixture_clis_are_deterministic_and_pass(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        commands = [
            [sys.executable, str(COMPILER_PATH), "--fixtures"],
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
            self.assertTrue(json.loads(first.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
