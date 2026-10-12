#!/usr/bin/env python3
"""Tests for the fixture-only ArtifactDeltaReceiptCandidate validator."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_artifact_delta_receipt.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/receipts/artifact_delta_receipt"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/receipts/artifact_delta_receipt.schema.json"

spec = importlib.util.spec_from_file_location("artifact_delta_receipt_validator", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("validator module could not be loaded")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ArtifactDeltaReceiptTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def codes(self, candidate: dict) -> set[str]:
        return {finding.code for finding in module.validate_candidate(candidate).findings}

    def redigest(self, candidate: dict) -> dict:
        candidate["canonicalization"]["payload_digest"] = module.expected_payload_digest(candidate)
        return candidate

    def test_schema_is_closed_draft_2020_12_receipt_profile(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["object_type"]["const"], "ArtifactDeltaReceiptCandidate")
        self.assertEqual(schema["x-kfm"]["authority"], "shape_and_local_consistency_only")

    def test_valid_fixture_polarity_and_digest(self) -> None:
        for name in ("valid_approved.json", "valid_rollback.json"):
            with self.subTest(name=name):
                candidate = self.load(f"valid/{name}")
                result = module.validate_candidate(candidate)
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(
                    candidate["canonicalization"]["payload_digest"],
                    module.expected_payload_digest(candidate),
                )

    def test_invalid_fixture_exact_findings(self) -> None:
        manifest = self.load("invalid/expected_findings_manifest.json")
        for name, expected in sorted(manifest.items()):
            with self.subTest(name=name):
                candidate = self.load(f"invalid/{name}")
                self.assertEqual(sorted(self.codes(candidate)), sorted(expected))

    def test_approval_requires_review_attestation_and_rollback(self) -> None:
        candidate = self.load("valid/valid_approved.json")
        candidate["review"]["state"] = "PENDING"
        candidate["review"]["review_record_ref"] = None
        candidate["attestation"]["verification_state"] = "UNVERIFIED"
        candidate["rollback_target_ref"] = None
        self.redigest(candidate)
        codes = self.codes(candidate)
        self.assertIn("APPROVAL_REQUIRES_APPROVED_REVIEW", codes)
        self.assertIn("APPROVAL_REQUIRES_VERIFIED_ATTESTATION", codes)
        self.assertIn("APPROVAL_REQUIRES_ROLLBACK_TARGET", codes)

    def test_change_specific_references_fail_closed(self) -> None:
        rollback = self.load("valid/valid_rollback.json")
        rollback["rollback_target_ref"] = None
        self.redigest(rollback)
        self.assertIn("ROLLBACK_TARGET_REQUIRED", self.codes(rollback))

        correction = self.load("valid/valid_approved.json")
        correction["change_kind"] = "CORRECTION"
        correction["correction_notice_ref"] = None
        self.redigest(correction)
        self.assertIn("CORRECTION_NOTICE_REQUIRED", self.codes(correction))

    def test_digest_changes_when_bound_revision_changes(self) -> None:
        candidate = self.load("valid/valid_approved.json")
        original = candidate["canonicalization"]["payload_digest"]
        candidate["after"]["artifact_digest"] = "sha256:" + ("9" * 64)
        self.assertNotEqual(original, module.expected_payload_digest(candidate))
        self.assertIn("PAYLOAD_DIGEST_MISMATCH", self.codes(candidate))

    def test_governance_authority_is_always_denied(self) -> None:
        candidate = self.load("valid/valid_approved.json")
        candidate["governance"]["release_authorized"] = True
        self.redigest(candidate)
        codes = self.codes(candidate)
        self.assertIn("SCHEMA_INVALID", codes)
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", codes)

    def test_fixture_runner(self) -> None:
        self.assertEqual(module.run_fixture_profile(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
