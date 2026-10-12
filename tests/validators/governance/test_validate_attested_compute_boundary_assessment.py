from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.governance import validate_attested_compute_boundary_assessment as validator


class AttestedComputeBoundaryAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validator.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(item for item in self.manifest["cases"] if item["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return validator.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_draft_2020_12(self) -> None:
        schema = validator._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["compute"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(18, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_four_postures_have_exact_fixture_coverage(self) -> None:
        names = (
            "pass_no_tre_existing_controls_sufficient",
            "pass_simulated_assessment",
            "abstain_real_tee_deferred",
            "deny_unverified_external_attestation",
        )
        postures = {self._candidate(name)["decision"]["posture"] for name in names}
        self.assertEqual(
            {
                "NO_TRE",
                "SIMULATED_ASSESSMENT",
                "DEFER_REAL_TEE",
                "DENY_UNVERIFIED_ATTESTATION",
            },
            postures,
        )

    def test_positive_postures_never_authorize_effects(self) -> None:
        for name in (
            "pass_no_tre_existing_controls_sufficient",
            "pass_simulated_assessment",
        ):
            candidate = self._candidate(name)
            self.assertEqual("PASS", validator.validate_candidate(candidate).outcome)
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertFalse(candidate["decision"]["real_tee_authorized"])
            self.assertEqual("NO_DATA_SYNTHETIC_ONLY", candidate["safeguards"]["data_mode"])

    def test_incomplete_inputs_abstain_and_preserve_real_tee_boundary(self) -> None:
        for name in (
            "abstain_real_tee_deferred",
            "abstain_control_review_incomplete",
            "abstain_residual_problem_unresolved",
            "abstain_boundary_component_unresolved",
            "abstain_synthetic_attestation_boundary_incomplete",
            "abstain_simulation_plan_incomplete",
        ):
            result = validator.validate_candidate(self._candidate(name))
            self.assertEqual("ABSTAIN", result.outcome)
            self.assertFalse(self._candidate(name)["decision"]["real_tee_authorized"])

    def test_simulated_profile_preserves_adr_entry_evidence_seams(self) -> None:
        candidate = self._candidate("pass_simulated_assessment")
        self.assertTrue(candidate["problem"]["affected_owner_refs"])
        self.assertTrue(candidate["safeguards"]["simulation_plan_ref"])
        self.assertEqual(
            validator.UNSUPPORTED_AUTHORITIES,
            candidate["attestation_claim"]["unsupported_authorities"],
        )
        self.assertIn("execution_receipt", candidate["boundary_declarations"])
        self.assertIn(
            "evidence_and_reviewer_decision", candidate["boundary_declarations"]
        )

    def test_unverified_attestation_is_denied(self) -> None:
        result = validator.validate_candidate(
            self._candidate("deny_unverified_external_attestation")
        )
        self.assertEqual("DENY", result.outcome)
        self.assertEqual(["UNVERIFIED_ATTESTATION_DENIED"], result.codes)

    def test_decision_and_identity_are_deterministic(self) -> None:
        candidate = self._candidate("pass_simulated_assessment")
        self.assertEqual(candidate["decision"], validator.derive_decision(candidate))
        self.assertEqual(
            candidate["profile_spec_hash"], validator.compute_profile_hash(candidate)
        )
        changed = copy.deepcopy(candidate)
        changed["problem"]["statement"] = (
            "A different synthetic residual problem declaration changes identity."
        )
        self.assertNotEqual(
            candidate["profile_spec_hash"], validator.compute_profile_hash(changed)
        )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = validator.validate_fixture_manifest()
            second = validator.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_FILE_BYTES + 1))
            for path, code in (
                (duplicate, "JSON_DUPLICATE_KEY"),
                (nonfinite, "JSON_NONFINITE_NUMBER"),
                (link, "INPUT_SYMLINK_DENIED"),
                (oversized, "FILE_TOO_LARGE"),
            ):
                with self.subTest(path=path.name):
                    value, findings = validator.load_json_object(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
