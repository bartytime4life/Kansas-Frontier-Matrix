from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_PATH = ROOT / "tools/validators/evidence/validate_evidence_temporal_posture_assessment.py"
LEGACY_PATH = ROOT / "tools/validators/evidence/validate_temporal_authority_envelope.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CANONICAL = load_module("canonical_evidence_temporal_posture", CANONICAL_PATH)
LEGACY = load_module("legacy_evidence_temporal_posture", LEGACY_PATH)
NOW = datetime(2026, 8, 17, tzinfo=timezone.utc)
CANONICAL_ROOT = ROOT / "fixtures/contracts/v1/evidence/evidence_temporal_posture_assessment"
LEGACY_ROOT = ROOT / "fixtures/contracts/v1/evidence/temporal_authority_envelope"


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


class EvidenceTemporalPostureAssessmentTests(unittest.TestCase):
    def test_schema_is_distinct_and_meta_valid(self) -> None:
        schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        Draft202012Validator.check_schema(schema)
        self.assertEqual("EvidenceTemporalPostureAssessment", schema["title"])
        self.assertNotEqual(
            "https://schemas.kfm.local/contracts/v1/common/temporal_authority_envelope.schema.json",
            schema["$id"],
        )

    def test_canonical_fixture_polarity(self) -> None:
        valid = CANONICAL.validate_doc(load(CANONICAL_ROOT / "valid/current_observation.json"), now=NOW)
        self.assertEqual([], valid)
        inverted = CANONICAL.validate_doc(load(CANONICAL_ROOT / "invalid/inverted_validity.json"), now=NOW)
        self.assertTrue(any("valid_from" in error for error in inverted))
        source_after = CANONICAL.validate_doc(load(CANONICAL_ROOT / "invalid/source_after_retrieval.json"), now=NOW)
        self.assertTrue(any("source_updated_at" in error for error in source_after))

    def test_legacy_and_canonical_fixture_bytes_are_identical(self) -> None:
        canonical = sorted(path.relative_to(CANONICAL_ROOT) for path in CANONICAL_ROOT.rglob("*.json"))
        legacy = sorted(path.relative_to(LEGACY_ROOT) for path in LEGACY_ROOT.rglob("*.json"))
        self.assertEqual(legacy, canonical)
        for relative in canonical:
            self.assertEqual((LEGACY_ROOT / relative).read_bytes(), (CANONICAL_ROOT / relative).read_bytes())

    def test_legacy_and_canonical_diagnostics_are_identical(self) -> None:
        for relative in sorted(path.relative_to(CANONICAL_ROOT) for path in CANONICAL_ROOT.rglob("*.json")):
            canonical = CANONICAL.validate_doc(load(CANONICAL_ROOT / relative), now=NOW)
            legacy = LEGACY.validate_doc(load(LEGACY_ROOT / relative), now=NOW)
            self.assertEqual(legacy, canonical, relative)

    def test_legacy_identifiers_remain_resolvable(self) -> None:
        candidate = load(CANONICAL_ROOT / "valid/current_observation.json")
        self.assertTrue(str(candidate["envelope_id"]).startswith("kfm:temporal-authority:"))
        self.assertEqual([], CANONICAL.validate_doc(candidate, now=NOW))
        self.assertEqual([], LEGACY.validate_doc(candidate, now=NOW))

    def test_common_and_evidence_shapes_reject_each_other(self) -> None:
        common_schema = load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json")
        assessment_schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        evidence_fixture = load(CANONICAL_ROOT / "valid/current_observation.json")
        common_fixture = load(ROOT / "fixtures/contracts/v1/common/temporal_authority_envelope/valid/valid_3_corrected_revision.json")
        common_errors = list(Draft202012Validator(common_schema, format_checker=FormatChecker()).iter_errors(evidence_fixture))
        evidence_errors = list(Draft202012Validator(assessment_schema, format_checker=FormatChecker()).iter_errors(common_fixture))
        self.assertTrue(common_errors)
        self.assertTrue(evidence_errors)

    def test_incompatible_correction_chronology_remains_explicit(self) -> None:
        candidate = load(CANONICAL_ROOT / "valid/current_observation.json")
        candidate["temporal_posture"] = "UNKNOWN"
        candidate["freshness_deadline"] = None
        times = candidate["times"]
        assert isinstance(times, dict)
        times["released_at"] = "2026-08-08T00:07:00Z"
        times["corrected_at"] = "2026-08-08T00:08:00Z"
        self.assertEqual([], CANONICAL.validate_doc(candidate, now=NOW))
        times["corrected_at"] = "2026-08-08T00:06:30Z"
        self.assertIn(
            "corrected_at requires and must not precede released_at",
            CANONICAL.validate_doc(candidate, now=NOW),
        )
        common_fixture = load(ROOT / "fixtures/contracts/v1/common/temporal_authority_envelope/valid/valid_3_corrected_revision.json")
        common_times = common_fixture["time"]
        assert isinstance(common_times, dict)
        self.assertLessEqual(common_times["corrected_at"], common_times["retrieved_at"])

    def test_source_role_is_not_source_descriptor_binding(self) -> None:
        assessment_schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        common_schema = load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json")
        self.assertIn("source_role", assessment_schema["properties"])
        self.assertNotIn("source_descriptor_ref", assessment_schema["properties"])
        self.assertIn("source", common_schema["properties"])

    def test_advisory_reference_remains_bound_to_common_schema(self) -> None:
        advisory = load(ROOT / "schemas/contracts/v1/common/advisory_event_envelope.schema.json")
        self.assertEqual(
            "https://schemas.kfm.local/contracts/v1/common/temporal_authority_envelope.schema.json",
            advisory["properties"]["temporal_authority"]["$ref"],
        )

    def test_no_third_same_named_semantic_family(self) -> None:
        schemas = [
            load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json"),
            load(ROOT / "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"),
            load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json"),
        ]
        self.assertEqual(2, sum(schema.get("title") in {"TemporalAuthorityEnvelope", "temporal_authority_envelope"} for schema in schemas))
        self.assertEqual("EvidenceTemporalPostureAssessment", schemas[2]["title"])


if __name__ == "__main__":
    unittest.main()
