"""Repository-parity and fail-closed decision tests for path aliases."""

from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.validators.directory_governance.path_alias_model import REGISTER_PATH, ROOT_REGISTRY_PATH
from tools.validators.directory_governance.validate_path_alias_register import validate_register


class PathAliasRepositoryCases(unittest.TestCase):
    def test_repository_parity_checks_blob_and_target_digest(self) -> None:
        payload = copy.deepcopy(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        alias = payload["aliases"][0]
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            old = repo / alias["old_path"]
            target = repo / alias["canonical_target"]
            adr = repo / "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
            old.parent.mkdir(parents=True, exist_ok=True)
            target.parent.mkdir(parents=True, exist_ok=True)
            adr.parent.mkdir(parents=True, exist_ok=True)
            old_bytes = b"legacy read-only body\n"
            target_bytes = b"canonical doctrine body\n"
            old.write_bytes(old_bytes)
            target.write_bytes(target_bytes)
            adr.write_text("status: accepted\n# ADR-0029\n", encoding="utf-8")
            header = f"blob {len(old_bytes)}\0".encode("ascii")
            alias["legacy_git_blob"] = hashlib.sha1(header + old_bytes).hexdigest()
            alias["canonical_sha256"] = f"sha256:{hashlib.sha256(target_bytes).hexdigest()}"
            register_path = repo / "candidate.yaml"
            register_path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            result = validate_register(
                register_path,
                repo_root=repo,
                root_registry_path=ROOT_REGISTRY_PATH,
                check_repository=True,
                enforce_projection_binding=False,
            )
        self.assertTrue(result.ok, result.findings)

    def test_missing_alias_path_is_new_drift(self) -> None:
        payload = copy.deepcopy(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        alias = payload["aliases"][0]
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / alias["canonical_target"]
            adr = repo / "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            adr.parent.mkdir(parents=True, exist_ok=True)
            target_bytes = b"canonical doctrine body\n"
            target.write_bytes(target_bytes)
            adr.write_text("status: accepted\n# ADR-0029\n", encoding="utf-8")
            alias["canonical_sha256"] = f"sha256:{hashlib.sha256(target_bytes).hexdigest()}"
            register_path = repo / "candidate.yaml"
            register_path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            result = validate_register(
                register_path,
                repo_root=repo,
                root_registry_path=ROOT_REGISTRY_PATH,
                check_repository=True,
                enforce_projection_binding=False,
            )
        self.assertEqual("FAIL_NEW_DRIFT", result.outcome)
        self.assertIn("ALIAS_PATH_MISSING", {item.code for item in result.findings})

    def test_missing_accepted_adr_holds_fail_closed(self) -> None:
        payload = copy.deepcopy(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        alias = payload["aliases"][0]
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            old = repo / alias["old_path"]
            target = repo / alias["canonical_target"]
            old.parent.mkdir(parents=True, exist_ok=True)
            target.parent.mkdir(parents=True, exist_ok=True)
            old_bytes = b"legacy read-only body\n"
            target_bytes = b"canonical doctrine body\n"
            old.write_bytes(old_bytes)
            target.write_bytes(target_bytes)
            header = f"blob {len(old_bytes)}\0".encode("ascii")
            alias["legacy_git_blob"] = hashlib.sha1(header + old_bytes).hexdigest()
            alias["canonical_sha256"] = f"sha256:{hashlib.sha256(target_bytes).hexdigest()}"
            register_path = repo / "candidate.yaml"
            register_path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            result = validate_register(
                register_path,
                repo_root=repo,
                root_registry_path=ROOT_REGISTRY_PATH,
                check_repository=True,
                enforce_projection_binding=False,
            )
        self.assertEqual("HOLD_UNRESOLVED", result.outcome)
        self.assertIn("DECISION_EVIDENCE_MISSING", {item.code for item in result.findings})
