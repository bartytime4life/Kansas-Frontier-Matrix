#!/usr/bin/env python3
"""Focused proof for the internal manifest-backed Hydrology fixture adapter."""

from __future__ import annotations

import ast
import copy
import hashlib
import json
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver import hydrology_fixture_adapter as adapter  # noqa: E402
from evidence_resolver.core import PROFILE, result_json  # noqa: E402
from evidence_resolver.runtime_projection import posture_json  # noqa: E402
from evidence_resolver.verification_history import (  # noqa: E402
    canonical_spec_hash,
)


MANIFEST_RELATIVE = Path(
    "fixtures/packages/evidence_resolver/v1alpha1/repository/"
    "hydrology_bundle_manifest.json"
)
BUNDLE_RELATIVE = Path(
    "fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json"
)
EXPECTED_DIGEST = (
    "sha256:e280b85328f9978e1ff909f3324a95f1a9273d118a077d53b0ff78ed55654537"
)
EVIDENCE_REF = "kfm://synthetic/hydrology/observation-001"


def _digest(value: object) -> str:
    canonical = json.dumps(
        value,
        ensure_ascii=True,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _request(bundle_id: str = "hb1", *, policy: str = "ANSWER") -> dict[str, object]:
    history: dict[str, object] = {
        "schema_version": "1.0.0",
        "history_id": "kfm:verification-history:synthetic:hydrology-adapter-001",
        "subject_ref": EVIDENCE_REF,
        "profile_id": "kfm://profile/verification-state-replay/v1",
        "events": [
            {
                "event_id": "evt:001",
                "event_type": "VERIFIED",
                "state": "ACTIVE",
                "effective_at": "2026-01-01T00:00:00Z",
                "recorded_at": "2026-01-01T00:00:00Z",
                "reason_code": "INITIAL_VERIFICATION",
                "basis_refs": [
                    "kfm://synthetic/receipt/hydrology-adapter-001"
                ],
            }
        ],
    }
    history["spec_hash"] = canonical_spec_hash(history)
    return {
        "profile": PROFILE,
        "evidence_ref": {
            "ref": EVIDENCE_REF,
            "kind": "measurement",
            "bundle_ref": bundle_id,
        },
        "bundle_candidate": None,
        "lookup_context": {
            "bundle_id": None,
            "current_head": True,
            "policy_outcome": policy,
            "policy_decision_ref": f"policy:synthetic:{policy.lower()}-hydrology",
            "correction_state": "ACTIVE",
            "correction_ref": None,
        },
        "verification_history": history,
        "verification_as_of": {
            "effective_as_of": "2026-01-02T00:00:00Z",
            "recorded_as_of": "2026-01-02T00:00:00Z",
        },
    }


class HydrologyFixtureAdapterTests(unittest.TestCase):
    def _isolated_repository(self) -> Path:
        directory = self.enterContext(tempfile.TemporaryDirectory())
        root = Path(directory)
        for relative in (MANIFEST_RELATIVE, BUNDLE_RELATIVE):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        self.enterContext(mock.patch.object(adapter, "_REPOSITORY_ROOT", root))
        return root

    def _manifest(self, root: Path) -> dict[str, object]:
        return json.loads((root / MANIFEST_RELATIVE).read_text(encoding="utf-8"))

    def _write_manifest(self, root: Path, value: object) -> None:
        (root / MANIFEST_RELATIVE).write_text(
            json.dumps(value, indent=2) + "\n", encoding="utf-8"
        )

    def _write_bundle(self, root: Path, value: object) -> None:
        (root / BUNDLE_RELATIVE).write_text(
            json.dumps(value, indent=2) + "\n", encoding="utf-8"
        )

    def assertFailsClosed(self, result: adapter.HydrologyFixtureResolution) -> None:
        self.assertNotEqual("RESOLVED", result.candidate.status)
        self.assertIsNone(result.candidate.bundle_id)
        self.assertNotEqual("CONTINUE_GOVERNED_CHECKS", result.runtime.disposition)
        self.assertFalse(result.runtime.as_dict()["authoritative"])
        self.assertFalse(result.runtime.as_dict()["renderable"])

    def test_manifest_binds_the_complete_selected_fixture_digest(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / MANIFEST_RELATIVE).read_text(encoding="utf-8")
        )
        bundle = json.loads(
            (REPO_ROOT / BUNDLE_RELATIVE).read_text(encoding="utf-8")
        )
        self.assertEqual(["entries"], list(manifest))
        self.assertEqual(1, len(manifest["entries"]))
        entry = manifest["entries"][0]
        self.assertEqual(adapter.ADAPTER_PROFILE, entry["adapter_profile"])
        self.assertEqual(adapter.DIGEST_PROFILE, entry["digest_profile"])
        self.assertEqual("hb1", entry["bundle_id"])
        self.assertEqual(BUNDLE_RELATIVE.as_posix(), entry["fixture_path"])
        self.assertEqual(EXPECTED_DIGEST, entry["expected_digest"])
        self.assertEqual(EXPECTED_DIGEST, _digest(bundle))

    def test_verified_fixture_uses_existing_evaluator_and_runtime_projection(
        self,
    ) -> None:
        resolved = adapter.resolve_hydrology_fixture("hb1", _request())
        candidate = resolved.candidate.as_dict()
        runtime = resolved.runtime.as_dict()

        self.assertEqual("RESOLVED", candidate["status"])
        self.assertEqual("hb1", candidate["bundle_id"])
        self.assertIn(
            "fixture_bundle_digest_binding", candidate["checks_performed"]
        )
        self.assertIn(
            "shared_hydrology_evidence_bundle_shape",
            candidate["checks_performed"],
        )
        self.assertEqual("CONTINUE_GOVERNED_CHECKS", runtime["disposition"])
        self.assertFalse(runtime["authoritative"])
        self.assertFalse(runtime["renderable"])
        self.assertNotEqual("ANSWER", runtime["disposition"])

    def test_manifest_miss_abstains_without_exposing_identity_or_path(self) -> None:
        unresolved = adapter.resolve_hydrology_fixture("hb2", _request("hb2"))
        self.assertEqual("UNRESOLVED", unresolved.candidate.status)
        self.assertEqual("ABSTAIN", unresolved.runtime.disposition)
        self.assertIsNone(unresolved.candidate.bundle_id)
        encoded = result_json(unresolved.candidate)
        self.assertNotIn(BUNDLE_RELATIVE.as_posix(), encoded)
        self.assertNotIn("hydrology feature", encoded)
        self.assertFailsClosed(unresolved)

    def test_existing_policy_deny_projects_only_deny(self) -> None:
        denied = adapter.resolve_hydrology_fixture(
            "hb1", _request(policy="DENY")
        )
        self.assertEqual("DENIED", denied.candidate.status)
        self.assertEqual("DENY", denied.runtime.disposition)
        self.assertFailsClosed(denied)

    def test_existing_correction_state_preserves_evaluator_abstain(self) -> None:
        request = _request()
        lookup = request["lookup_context"]
        self.assertIsInstance(lookup, dict)
        assert isinstance(lookup, dict)
        lookup["correction_state"] = "WITHDRAWN"
        lookup["correction_ref"] = "kfm://synthetic/correction/hydrology-001"
        withdrawn = adapter.resolve_hydrology_fixture("hb1", request)

        self.assertEqual("UNRESOLVED", withdrawn.candidate.status)
        self.assertEqual("ABSTAIN", withdrawn.runtime.disposition)
        self.assertIn(
            "correction/withdrawn",
            {issue.code for issue in withdrawn.candidate.issues},
        )
        self.assertFailsClosed(withdrawn)

    def test_result_is_deterministic(self) -> None:
        first = adapter.resolve_hydrology_fixture("hb1", _request())
        second = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual(result_json(first.candidate), result_json(second.candidate))
        self.assertEqual(posture_json(first.runtime), posture_json(second.runtime))

    def test_digest_tamper_is_error_without_raw_payload_echo(self) -> None:
        root = self._isolated_repository()
        bundle = json.loads((root / BUNDLE_RELATIVE).read_text(encoding="utf-8"))
        bundle["claim_scope"] = "protected-tamper-sentinel"
        self._write_bundle(root, bundle)

        failed = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual("ERROR", failed.candidate.status)
        self.assertEqual(
            ["fixture-adapter/digest-mismatch"],
            [issue.code for issue in failed.candidate.issues],
        )
        self.assertNotIn("protected-tamper-sentinel", result_json(failed.candidate))
        self.assertFailsClosed(failed)

    def test_schema_failure_after_matching_digest_is_error(self) -> None:
        root = self._isolated_repository()
        bundle = json.loads((root / BUNDLE_RELATIVE).read_text(encoding="utf-8"))
        del bundle["citations"]
        self._write_bundle(root, bundle)
        manifest = self._manifest(root)
        manifest["entries"][0]["expected_digest"] = _digest(bundle)
        self._write_manifest(root, manifest)

        failed = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual("ERROR", failed.candidate.status)
        self.assertEqual(
            ["input/missing-field"],
            [issue.code for issue in failed.candidate.issues],
        )
        self.assertFailsClosed(failed)

    def test_duplicate_manifest_identity_is_error(self) -> None:
        root = self._isolated_repository()
        manifest = self._manifest(root)
        manifest["entries"].append(copy.deepcopy(manifest["entries"][0]))
        self._write_manifest(root, manifest)

        failed = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual(
            ["fixture-adapter/duplicate-id"],
            [issue.code for issue in failed.candidate.issues],
        )
        self.assertFailsClosed(failed)

    def test_malformed_manifest_and_bundle_fail_closed(self) -> None:
        root = self._isolated_repository()
        (root / MANIFEST_RELATIVE).write_text(
            '{"entries":[],"entries":[]}', encoding="utf-8"
        )
        manifest_failure = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual(
            ["fixture-adapter/manifest-duplicate-key"],
            [issue.code for issue in manifest_failure.candidate.issues],
        )
        self.assertFailsClosed(manifest_failure)

        root = self._isolated_repository()
        (root / BUNDLE_RELATIVE).write_text("{", encoding="utf-8")
        bundle_failure = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual(
            ["fixture-adapter/bundle-malformed-json"],
            [issue.code for issue in bundle_failure.candidate.issues],
        )
        self.assertFailsClosed(bundle_failure)

    def test_unsupported_adapter_and_digest_profiles_are_errors(self) -> None:
        for field, expected in (
            ("adapter_profile", "fixture-adapter/adapter-profile-unsupported"),
            ("digest_profile", "fixture-adapter/digest-profile-unsupported"),
        ):
            with self.subTest(field=field):
                root = self._isolated_repository()
                manifest = self._manifest(root)
                manifest["entries"][0][field] = "unsupported/profile"
                self._write_manifest(root, manifest)
                failed = adapter.resolve_hydrology_fixture("hb1", _request())
                self.assertEqual([expected], [i.code for i in failed.candidate.issues])
                self.assertFailsClosed(failed)

    def test_path_inputs_fail_before_any_outside_read(self) -> None:
        path_cases = (
            ("/tmp/fixture.json", "fixture-adapter/path-absolute"),
            ("../data/fixture.json", "fixture-adapter/path-traversal"),
            ("data/fixture.json", "fixture-adapter/path-outside-root"),
            (
                "fixtures/domains/hydrology/evidence_bundle/valid/other.json",
                "fixture-adapter/path-not-allowlisted",
            ),
        )
        for fixture_path, expected in path_cases:
            with self.subTest(fixture_path=fixture_path):
                root = self._isolated_repository()
                manifest = self._manifest(root)
                manifest["entries"][0]["fixture_path"] = fixture_path
                self._write_manifest(root, manifest)
                original_reader = adapter._read_repository_file
                with mock.patch.object(
                    adapter,
                    "_read_repository_file",
                    wraps=original_reader,
                ) as reader:
                    failed = adapter.resolve_hydrology_fixture("hb1", _request())
                self.assertEqual(1, reader.call_count, "only manifest may be read")
                self.assertEqual([expected], [i.code for i in failed.candidate.issues])
                self.assertFailsClosed(failed)

    def test_symlinked_bundle_is_rejected(self) -> None:
        root = self._isolated_repository()
        fixture = root / BUNDLE_RELATIVE
        outside = root / "outside.json"
        shutil.copy2(fixture, outside)
        fixture.unlink()
        fixture.symlink_to(outside)

        failed = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual(
            ["fixture-adapter/path-symlink"],
            [issue.code for issue in failed.candidate.issues],
        )
        self.assertFailsClosed(failed)

    def test_caller_candidate_and_path_like_id_are_rejected(self) -> None:
        request = _request()
        request["bundle_candidate"] = {"caller": "injected"}
        injected = adapter.resolve_hydrology_fixture("hb1", request)
        self.assertEqual(
            ["fixture-adapter/caller-bundle-forbidden"],
            [issue.code for issue in injected.candidate.issues],
        )
        self.assertFailsClosed(injected)

        path_input = adapter.resolve_hydrology_fixture("../../data/raw", _request())
        self.assertEqual(
            ["fixture-adapter/bundle-id-invalid"],
            [issue.code for issue in path_input.candidate.issues],
        )
        self.assertFailsClosed(path_input)

    def test_execution_has_no_network_process_or_model_dependency(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "getaddrinfo", side_effect=AssertionError("dns denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("socket denied")
        ), mock.patch.object(
            urllib.request, "urlopen", side_effect=AssertionError("url denied")
        ), mock.patch.object(
            subprocess, "run", side_effect=AssertionError("process denied")
        ):
            resolved = adapter.resolve_hydrology_fixture("hb1", _request())
        self.assertEqual("RESOLVED", resolved.candidate.status)

        source_path = PACKAGE_SRC / "evidence_resolver/hydrology_fixture_adapter.py"
        source = source_path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(source_path))
        roots: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                roots.add(node.module.split(".", 1)[0])
        self.assertLessEqual(
            roots,
            {
                "__future__",
                "core",
                "dataclasses",
                "hashlib",
                "json",
                "pathlib",
                "re",
                "runtime_projection",
                "stat",
                "typing",
            },
        )
        self.assertNotIn("openai", source.lower())
        self.assertNotIn("ollama", source.lower())

    def test_hydrology_alias_remains_the_closed_shared_schema_alias(self) -> None:
        shared = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/evidence/evidence_bundle.schema.json"
            ).read_text(encoding="utf-8")
        )
        hydrology = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/domains/hydrology/"
                "evidence_bundle.schema.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual([{"$ref": shared["$id"]}], hydrology["allOf"])
        self.assertIs(hydrology["unevaluatedProperties"], False)
        self.assertIs(shared["additionalProperties"], False)


if __name__ == "__main__":
    unittest.main()
