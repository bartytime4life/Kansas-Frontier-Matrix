from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_temporal_authority_envelope.py"
SPEC = importlib.util.spec_from_file_location("legacy_evidence_tae", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
NOW = datetime(2026, 8, 17, tzinfo=timezone.utc)


def load(relative: str) -> dict[str, object]:
    value = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


class LegacyEvidenceTemporalAuthorityEnvelopeTests(unittest.TestCase):
    def test_valid_fixture_replays(self) -> None:
        self.assertEqual([], MODULE.validate_doc(load(
            "fixtures/contracts/v1/evidence/temporal_authority_envelope/valid/current_observation.json"
        ), now=NOW))

    def test_inverted_validity_rejected(self) -> None:
        errors = MODULE.validate_doc(load(
            "fixtures/contracts/v1/evidence/temporal_authority_envelope/invalid/inverted_validity.json"
        ), now=NOW)
        self.assertTrue(any("valid_from" in error for error in errors))

    def test_source_after_retrieval_rejected(self) -> None:
        errors = MODULE.validate_doc(load(
            "fixtures/contracts/v1/evidence/temporal_authority_envelope/invalid/source_after_retrieval.json"
        ), now=NOW)
        self.assertTrue(any("source_updated_at" in error for error in errors))

    def test_entry_point_is_explicit_compatibility_wrapper(self) -> None:
        text = MODULE_PATH.read_text(encoding="utf-8")
        self.assertIn("EvidenceTemporalPostureAssessment", text)
        self.assertIn("LEGACY_SCHEMA", text)
        self.assertNotIn("schemas/contracts/v1/common/temporal_authority_envelope", text)


if __name__ == "__main__":
    unittest.main()
