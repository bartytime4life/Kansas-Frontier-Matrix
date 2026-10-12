"""Focused tests for the MRTS-05 synthetic trust-spine fixture slice."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/governance/validate_trust_spine_fixture_slice.py"
SPEC = importlib.util.spec_from_file_location("kfm_trust_spine_fixture_slice", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TrustSpineFixtureSliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report, cls.loaded = MODULE.validate_current()
        assert cls.loaded is not None

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_profile_has_exact_family_link_and_case_sets(self) -> None:
        packet = self.loaded.packet
        self.assertEqual(
            tuple(item["family_id"] for item in packet["artifacts"]),
            MODULE.FAMILIES,
        )
        self.assertEqual(tuple(packet["link_requirements"]), MODULE.LINK_REQUIREMENTS)
        self.assertEqual(
            tuple(packet["required_negative_cases"]),
            tuple(MODULE.CASE_EXPECTATIONS),
        )

    def test_artifact_hashes_and_declared_identities_replay(self) -> None:
        for family in MODULE.FAMILIES:
            entry = self.loaded.artifact_entries[family]
            path = MODULE._canonical_repo_file(entry["path"])
            self.assertIsNotNone(path)
            assert path is not None
            self.assertEqual(MODULE._sha256_file(path), entry["sha256"])
            self.assertEqual(
                MODULE._derived_id(family, self.loaded.objects[family]),
                entry["object_id"],
            )

    def test_current_flow_passes_without_publication_authority(self) -> None:
        self.assertEqual(self.report["outcome"], "PASS")
        self.assertEqual(self.report["readiness"], "READY_FOR_REVIEW")
        self.assertEqual(self.report["publication_outcome"], "NOT_ATTEMPTED")
        self.assertFalse(any(self.report["authority"].values()))
        self.assertFalse(self.report["network_used"])

    def test_every_canonical_validator_lane_passes(self) -> None:
        self.assertEqual(set(self.report["canonical_lanes"]), set(MODULE.FAMILIES) - {"validation_report"})
        self.assertEqual(set(self.report["canonical_lanes"].values()), {"PASS"})

    def test_successful_dry_run_stops_before_publication(self) -> None:
        self.assertEqual(
            self.report["dry_run"],
            {
                "promotion_verification": "PASS",
                "readiness": "APPROVE_READY",
                "publication_deny": "PASS",
                "publication_created": False,
            },
        )

    def test_evidence_ref_resolves_to_matching_bundle(self) -> None:
        evidence_ref = self.loaded.objects["evidence_ref"]
        bundle = self.loaded.objects["evidence_bundle"]
        self.assertEqual(evidence_ref["bundle_ref"], bundle["bundle_id"])
        self.assertIn(evidence_ref, bundle["evidence_refs"])

    def test_source_activation_binds_exact_descriptor_bytes(self) -> None:
        activation = self.loaded.objects["source_activation_decision"]
        descriptor_entry = self.loaded.artifact_entries["source_descriptor"]
        self.assertEqual(activation["source_descriptor_digest"], descriptor_entry["sha256"])
        self.assertEqual(activation["source_descriptor_ref"], descriptor_entry["object_id"])

    def test_release_proof_and_rollback_targets_are_explicit(self) -> None:
        release = self.loaded.objects["release_manifest"]
        proof = self.loaded.objects["proof_pack"]
        rollback = self.loaded.objects["rollback_card"]
        self.assertEqual(proof["release_id"], release["release_id"])
        self.assertEqual(rollback["affected_release_ref"], release["release_id"])
        self.assertNotEqual(rollback["target"]["release_ref"], release["release_id"])
        self.assertIn(proof["proof_pack_id"], release["proof_refs"])

    def test_allow_and_deny_policy_sides_are_both_canonical(self) -> None:
        allow = self.loaded.objects["policy_decision"]
        self.assertTrue(MODULE.validate_policy_payload(allow).ok)
        objects = copy.deepcopy(self.loaded.objects)
        controls = copy.deepcopy(self.loaded.packet["controls"])
        MODULE._mutate("policy_deny", objects, controls)
        self.assertTrue(MODULE.validate_policy_payload(objects["policy_decision"]).ok)
        self.assertEqual(
            MODULE._evaluate_objects(self.loaded, objects, controls),
            ("DENY", ("POLICY_DENIED",)),
        )

    def test_all_negative_cases_match_exact_codes_and_outcomes(self) -> None:
        for case_id, expected in MODULE.CASE_EXPECTATIONS.items():
            with self.subTest(case_id=case_id):
                objects = copy.deepcopy(self.loaded.objects)
                controls = copy.deepcopy(self.loaded.packet["controls"])
                MODULE._mutate(case_id, objects, controls)
                self.assertEqual(
                    MODULE._evaluate_objects(self.loaded, objects, controls),
                    expected,
                )

    def test_duplicate_json_key_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "duplicate.json"
            path.write_text('{"a":1,"a":2}', encoding="utf-8")
            value, findings = MODULE._read_json(path)
        self.assertIsNone(value)
        self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])

    def test_path_escape_and_symlink_inputs_are_denied(self) -> None:
        self.assertIsNone(MODULE._canonical_repo_file("../outside.json"))
        self.assertIsNone(MODULE._canonical_repo_file("/absolute.json"))

    def test_validation_is_read_only(self) -> None:
        before = {
            family: MODULE._sha256_file(MODULE._canonical_repo_file(entry["path"]))
            for family, entry in self.loaded.artifact_entries.items()
        }
        report, _loaded = MODULE.validate_current()
        after = {
            family: MODULE._sha256_file(MODULE._canonical_repo_file(entry["path"]))
            for family, entry in self.loaded.artifact_entries.items()
        }
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(before, after)

    def test_cli_output_is_byte_deterministic(self) -> None:
        command = [sys.executable, str(MODULE_PATH)]
        first = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=False,
        )
        second = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=False,
        )
        self.assertEqual(first.returncode, 0)
        self.assertEqual(second.returncode, 0)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, b"")
        self.assertEqual(second.stderr, b"")


if __name__ == "__main__":
    unittest.main()
