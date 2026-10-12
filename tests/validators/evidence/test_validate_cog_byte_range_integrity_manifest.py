from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    ROOT
    / "tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py"
)
SPEC = importlib.util.spec_from_file_location(
    "cog_byte_range_integrity_manifest_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class COGByteRangeIntegrityManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_draft_2020_12(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertFalse(schema["x-kfm"]["payload_fixture_is_cog"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 30)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_synthetic_payload_is_explicitly_not_a_cog_claim(self) -> None:
        payload_path = (
            ROOT
            / "fixtures/contracts/v1/evidence/cog_byte_range_integrity_manifest"
            / "synthetic-range-payload.bin"
        )
        self.assertEqual(payload_path.stat().st_size, 65)
        candidate = self._candidate(
            "pass_complete_range_integrity_without_format_claim"
        )
        self.assertEqual(candidate["artifact"]["media_type"], "application/octet-stream")
        self.assertEqual(
            set(candidate["format_validation"].values()),
            {"NOT_EVALUATED", None},
        )
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")

    def test_unavailable_or_unknown_states_abstain(self) -> None:
        for name in (
            "abstain_payload_missing",
            "abstain_payload_unknown",
            "abstain_payload_unavailable",
            "abstain_sidecar_freshness_unknown",
            "abstain_immutability_unknown",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_byte_identity_failures_deny(self) -> None:
        expected = {
            "deny_byte_length_mismatch": ["BYTE_LENGTH_MISMATCH"],
            "deny_whole_digest_mismatch": ["WHOLE_DIGEST_MISMATCH"],
            "deny_range_digest_mismatch": ["RANGE_DIGEST_MISMATCH"],
            "deny_manifest_spec_hash_tamper": ["MANIFEST_SPEC_HASH_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_range_topology_and_role_failures_deny(self) -> None:
        expected = {
            "deny_range_gap": ["RANGE_GAP"],
            "deny_range_overlap": ["RANGE_OVERLAP"],
            "deny_range_out_of_bounds": ["RANGE_OUT_OF_BOUNDS"],
            "deny_range_coverage_incomplete": ["RANGE_COVERAGE_INCOMPLETE"],
            "deny_ranges_not_canonical": ["RANGES_NOT_CANONICAL"],
            "deny_duplicate_range_id": ["DUPLICATE_RANGE_ID"],
            "deny_required_role_missing": ["REQUIRED_RANGE_ROLE_MISSING"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_format_and_governance_overclaims_deny(self) -> None:
        for name in (
            "deny_sidecar_stale",
            "deny_mutable_artifact",
            "deny_format_validation_reference_required",
            "deny_format_validation_failed",
            "deny_interpretation_authority",
            "deny_format_conformance_authority",
            "deny_review_overclaim",
            "deny_release_overclaim",
            "deny_policy_overclaim",
            "deny_release_manifest_reference_unexpected",
            "deny_evidence_refs_not_canonical",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_manifest_hash_replays_and_binds_range_semantics(self) -> None:
        candidate = self._candidate(
            "pass_complete_range_integrity_without_format_claim"
        )
        self.assertEqual(
            candidate["manifest_spec_hash"],
            MODULE.compute_manifest_spec_hash(candidate),
        )
        changed = copy.deepcopy(candidate)
        changed["range_profile"]["entries"][2]["length"] = 15
        self.assertNotEqual(
            candidate["manifest_spec_hash"],
            MODULE.compute_manifest_spec_hash(changed),
        )

    def test_non_fixture_artifact_reference_is_denied(self) -> None:
        candidate = self._candidate(
            "pass_complete_range_integrity_without_format_claim"
        )
        candidate["artifact"]["artifact_ref"] = "https://example.invalid/raster.tif"
        candidate["manifest_spec_hash"] = MODULE.compute_manifest_spec_hash(candidate)
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(result.codes, ["ARTIFACT_REF_SCHEME_DENIED"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network denied"),
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
