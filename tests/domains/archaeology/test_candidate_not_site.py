"""Synthetic no-network proof for CandidateFeature safety invariants."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.validators.archaeology.validate_candidate_feature import (
    CANDIDATE_ID_PATTERN,
    CANDIDATE_TYPES,
    FORBIDDEN_INLINE_LOCATION_FIELDS,
    FORBIDDEN_SITE_CLAIM_FIELDS,
    SPATIAL_PRECISION_CLASSES,
    validate_candidate_feature,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/archaeology/synthetic_candidate_feature"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/archaeology/candidate_feature.schema.json"
VALIDATOR_PATH = REPO_ROOT / "tools/validators/archaeology/validate_candidate_feature.py"


def _load(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


class CandidateFeatureSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = _load(FIXTURE_ROOT / "valid.json")

    def test_synthetic_candidate_remains_candidate(self) -> None:
        self.assertEqual(validate_candidate_feature(self.valid), [])
        self.assertEqual(self.valid["truth_state"], "CANDIDATE")
        self.assertNotIn("geometry", self.valid)
        self.assertNotIn("coordinates", self.valid)

    def test_malformed_candidate_identifier_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "malformed_candidate_id_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "candidate_feature_id must match ^arc-candidate-[a-z0-9][a-z0-9-]*$",
            errors,
        )

    def test_unsupported_candidate_type_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "unsupported_candidate_type_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn("candidate_type is not in the bounded vocabulary", errors)

    def test_unsupported_spatial_precision_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "unsupported_spatial_precision_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "spatial_precision_class is not in the bounded vocabulary",
            errors,
        )

    def test_inline_location_fixture_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "sensitive_geometry_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertTrue(errors)
        self.assertTrue(any("inline location fields are denied" in error for error in errors))

    def test_location_bearing_reference_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "location_bearing_reference_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertTrue(errors)
        self.assertTrue(any("opaque kfm:// references" in error for error in errors))

    def test_catalog_candidate_requires_evidence_binding(self) -> None:
        payload = _load(FIXTURE_ROOT / "unbound_catalog_candidate_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "evidence_refs are required before review or processed/catalog lifecycle",
            errors,
        )

    def test_work_candidate_can_await_evidence_binding(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload.pop("evidence_refs")
        self.assertEqual(validate_candidate_feature(payload), [])

    def test_superseded_candidate_requires_correction_binding(self) -> None:
        payload = _load(
            FIXTURE_ROOT / "superseded_without_correction_deny.json"
        )
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "correction_refs are required for superseded candidates",
            errors,
        )

    def test_rejected_candidate_does_not_claim_supersession(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["review_state"] = "REJECTED"
        payload.pop("correction_refs", None)
        self.assertEqual(validate_candidate_feature(payload), [])

    def test_candidate_cannot_claim_confirmed_truth(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["truth_state"] = "CONFIRMED"
        errors = validate_candidate_feature(payload)
        self.assertIn("truth_state must remain CANDIDATE", errors)

    def test_candidate_cannot_carry_site_identity(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["archaeological_site_id"] = "synthetic-site-claim"
        errors = validate_candidate_feature(payload)
        self.assertTrue(any("confirmed-site claim fields are denied" in error for error in errors))

    def test_schema_projects_same_fail_closed_boundary(self) -> None:
        schema = _load(SCHEMA_PATH)
        properties = schema["properties"]
        self.assertEqual(properties["object_type"], {"const": "CandidateFeature"})
        self.assertEqual(properties["truth_state"], {"const": "CANDIDATE"})
        self.assertEqual(set(properties["candidate_type"]["enum"]), CANDIDATE_TYPES)
        self.assertEqual(
            set(properties["spatial_precision_class"]["enum"]),
            SPATIAL_PRECISION_CLASSES,
        )
        self.assertEqual(
            properties["candidate_feature_id"]["pattern"],
            CANDIDATE_ID_PATTERN.pattern,
        )
        self.assertFalse(schema["additionalProperties"])
        self.assertTrue(FORBIDDEN_INLINE_LOCATION_FIELDS.isdisjoint(properties))
        self.assertTrue(FORBIDDEN_SITE_CLAIM_FIELDS.isdisjoint(properties))
        expected_ref_pattern = "^kfm://[A-Za-z0-9][A-Za-z0-9._~/-]*$"
        self.assertEqual(properties["source_refs"]["items"]["pattern"], expected_ref_pattern)
        self.assertEqual(properties["candidate_geometry_ref"]["pattern"], expected_ref_pattern)
        self.assertEqual(properties["evidence_refs"]["minItems"], 1)
        evidence_conditional = schema["allOf"][0]
        self.assertEqual(evidence_conditional["then"]["required"], ["evidence_refs"])
        correction_conditional = schema["allOf"][1]
        self.assertEqual(
            correction_conditional["then"]["required"],
            ["correction_refs"],
        )
        self.assertEqual(properties["correction_refs"]["minItems"], 1)

    def test_fixture_cli_is_deterministic_and_local(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)
        self.assertIn("EXPECTED_FAIL", result.stdout)


if __name__ == "__main__":
    unittest.main()
