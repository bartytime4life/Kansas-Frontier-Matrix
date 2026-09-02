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
    CONFIDENCE_CONTENT_PATTERN,
    CONFIDENCE_STATEMENT_MAX_LENGTH,
    FORBIDDEN_INLINE_LOCATION_FIELDS,
    FORBIDDEN_SITE_CLAIM_FIELDS,
    SPEC_HASH_PATTERN,
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

    def test_non_string_vocabularies_fail_closed_without_exception(self) -> None:
        fixture = _load(FIXTURE_ROOT / "non_string_vocabulary_deny.json")
        self.assertIn(
            "candidate_type is not in the bounded vocabulary",
            validate_candidate_feature(fixture),
        )
        cases = {
            "origin_method": "origin_method is not in the bounded vocabulary",
            "review_state": "review_state cannot imply confirmation or publication",
            "sensitivity_class": "sensitivity_class is not in the bounded vocabulary",
            "spatial_precision_class": "spatial_precision_class is not in the bounded vocabulary",
            "lifecycle_state": "lifecycle_state cannot be PUBLISHED for CandidateFeature",
        }
        for field, expected_error in cases.items():
            with self.subTest(field=field):
                payload = copy.deepcopy(self.valid)
                payload[field] = ["malformed", "synthetic"]
                self.assertIn(expected_error, validate_candidate_feature(payload))

    def test_malformed_spec_hash_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "malformed_spec_hash_deny.json")
        expected_error = "spec_hash must match ^sha256:[a-f0-9]{64}$"
        self.assertIn(expected_error, validate_candidate_feature(payload))
        payload["spec_hash"] = {"synthetic": "not-a-digest"}
        self.assertIn(expected_error, validate_candidate_feature(payload))

    def test_null_optional_scalars_fail_closed_while_omission_remains_valid(self) -> None:
        cases = {
            "candidate_type": "candidate_type is not in the bounded vocabulary",
            "spatial_precision_class": "spatial_precision_class is not in the bounded vocabulary",
            "spec_hash": "spec_hash must match ^sha256:[a-f0-9]{64}$",
        }
        for field, expected_error in cases.items():
            with self.subTest(field=field):
                payload = copy.deepcopy(self.valid)
                payload[field] = None
                self.assertIn(expected_error, validate_candidate_feature(payload))
                payload.pop(field)
                self.assertEqual(validate_candidate_feature(payload), [])

    def test_malformed_confidence_statement_fails_closed(self) -> None:
        payload = _load(
            FIXTURE_ROOT / "malformed_confidence_statement_deny.json"
        )
        expected_error = "confidence_statement must contain 1 to 1000 characters"
        self.assertIn(expected_error, validate_candidate_feature(payload))
        for malformed in (
            {"synthetic": "not-a-statement"},
            " \t\n",
            "\u0085",
            "\u00ad",
            "\u034f",
            "\u061c",
            "\u115f",
            "\ufe0f",
            "\ufeff",
            "\U000e0001",
            "x" * (CONFIDENCE_STATEMENT_MAX_LENGTH + 1),
        ):
            with self.subTest(value_type=type(malformed).__name__):
                payload["confidence_statement"] = malformed
                self.assertIn(expected_error, validate_candidate_feature(payload))

    def test_null_confidence_statement_fails_closed(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["confidence_statement"] = None
        self.assertIn(
            "confidence_statement must contain 1 to 1000 characters",
            validate_candidate_feature(payload),
        )

    def test_unicode_invisible_confidence_fixture_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "unicode_invisible_confidence_deny.json")
        self.assertEqual(payload["confidence_statement"], "\u061c\ufe0f")
        self.assertIn(
            "confidence_statement must contain 1 to 1000 characters",
            validate_candidate_feature(payload),
        )

    def test_unicode_content_with_supplementary_context_remains_valid(self) -> None:
        for statement in ("uncertain \U0001f600", "不確実"):
            with self.subTest(statement=statement):
                payload = copy.deepcopy(self.valid)
                payload["confidence_statement"] = statement
                self.assertEqual(validate_candidate_feature(payload), [])

    def test_omitted_confidence_statement_remains_optional(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload.pop("confidence_statement", None)
        self.assertEqual(validate_candidate_feature(payload), [])

    def test_unsupported_spatial_precision_fails_closed(self) -> None:
        payload = _load(FIXTURE_ROOT / "unsupported_spatial_precision_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "spatial_precision_class is not in the bounded vocabulary",
            errors,
        )

    def test_geometry_reference_requires_spatial_precision(self) -> None:
        payload = _load(FIXTURE_ROOT / "unclassified_geometry_reference_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "spatial_precision_class is required with candidate_geometry_ref",
            errors,
        )

    def test_explicit_null_geometry_reference_fails_closed(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["candidate_geometry_ref"] = None
        errors = validate_candidate_feature(payload)
        self.assertIn(
            "candidate_geometry_ref must be an opaque governed kfm:// reference "
            "without query, fragment, or encoded locator material",
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

    def test_non_string_reference_fails_closed_without_exception(self) -> None:
        payload = _load(FIXTURE_ROOT / "non_string_reference_deny.json")
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

    def test_present_evidence_binding_cannot_be_empty(self) -> None:
        payload = _load(FIXTURE_ROOT / "empty_evidence_refs_deny.json")
        errors = validate_candidate_feature(payload)
        self.assertIn("evidence_refs must contain at least one reference", errors)

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
        self.assertEqual(properties["spec_hash"]["pattern"], SPEC_HASH_PATTERN.pattern)
        self.assertEqual(properties["confidence_statement"]["minLength"], 1)
        self.assertEqual(
            properties["confidence_statement"]["pattern"],
            CONFIDENCE_CONTENT_PATTERN.pattern,
        )
        self.assertEqual(
            properties["confidence_statement"]["maxLength"],
            CONFIDENCE_STATEMENT_MAX_LENGTH,
        )
        self.assertFalse(schema["additionalProperties"])
        self.assertTrue(FORBIDDEN_INLINE_LOCATION_FIELDS.isdisjoint(properties))
        self.assertTrue(FORBIDDEN_SITE_CLAIM_FIELDS.isdisjoint(properties))
        expected_ref_pattern = "^kfm://[A-Za-z0-9][A-Za-z0-9._~/-]*$"
        self.assertEqual(properties["source_refs"]["items"]["type"], "string")
        self.assertEqual(properties["source_refs"]["items"]["pattern"], expected_ref_pattern)
        self.assertEqual(properties["candidate_geometry_ref"]["pattern"], expected_ref_pattern)
        self.assertEqual(properties["evidence_refs"]["minItems"], 1)
        self.assertEqual(properties["correction_refs"]["minItems"], 1)
        evidence_conditional = schema["allOf"][0]
        self.assertEqual(evidence_conditional["then"]["required"], ["evidence_refs"])
        correction_conditional = schema["allOf"][1]
        self.assertEqual(
            correction_conditional["then"]["required"],
            ["correction_refs"],
        )
        geometry_precision_conditional = schema["allOf"][2]
        self.assertEqual(
            geometry_precision_conditional["if"]["required"],
            ["candidate_geometry_ref"],
        )
        self.assertEqual(
            geometry_precision_conditional["then"]["required"],
            ["spatial_precision_class"],
        )

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
