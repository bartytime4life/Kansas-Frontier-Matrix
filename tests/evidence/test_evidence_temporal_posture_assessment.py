from __future__ import annotations

import hashlib
import importlib.util
import json
import socket
import sys
import unittest
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

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


def correction_replay_cases() -> dict[str, dict[str, object]]:
    """Test-local variants; no migration, storage, or lineage resolver is implied."""
    original = load(LEGACY_ROOT / "valid/current_observation.json")
    corrected = deepcopy(original)
    corrected["times"] = {
        "observed_at": "2026-08-08T00:00:00Z",
        "valid_from": "2026-08-07T23:00:00Z",
        "valid_to": "2026-08-08T01:00:00Z",
        "source_updated_at": "2026-08-08T00:05:00Z",
        "retrieved_at": "2026-08-08T00:06:00Z",
        "released_at": "2026-08-08T00:07:00Z",
        "corrected_at": "2026-08-08T00:08:00Z",
    }
    corrected["lineage_refs"] = ["fixture:synthetic", "correction:synthetic:1"]
    superseded = deepcopy(corrected)
    superseded["temporal_posture"] = "SUPERSEDED"
    superseded["supersedes_ref"] = "kfm:temporal-authority:synthetic-predecessor"
    withdrawn = deepcopy(corrected)
    withdrawn["temporal_posture"] = "WITHDRAWN"
    withdrawn["withdrawal_ref"] = "withdrawal:synthetic:1"
    return {
        "original": original,
        "corrected": corrected,
        "superseded": superseded,
        "withdrawn": withdrawn,
    }


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

    def test_correction_replay_and_legacy_fallback_preserve_every_clock(self) -> None:
        cases = correction_replay_cases()
        baseline = deepcopy(cases)
        fixture_path = LEGACY_ROOT / "valid/current_observation.json"
        persisted_bytes = fixture_path.read_bytes()
        expected_id = "kfm:temporal-authority:mesonet.demo.1"
        # Legacy -> successor -> legacy is validator fallback, not a data rollback.
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            for engine in (LEGACY, CANONICAL, LEGACY):
                for name, record in cases.items():
                    with self.subTest(engine=engine.__name__, case=name):
                        self.assertEqual([], engine.validate_doc(record, now=NOW))
                        self.assertEqual(expected_id, record["envelope_id"])
                        self.assertEqual(baseline[name], record)
        self.assertEqual(persisted_bytes, fixture_path.read_bytes())
        self.assertEqual(load(fixture_path), cases["original"])

    def test_replayed_negative_cases_keep_exact_diagnostics(self) -> None:
        base = correction_replay_cases()["corrected"]
        mutations = (
            ("times", "source_updated_at", "2026-08-08T00:09:00Z",
             "source_updated_at must not exceed retrieved_at"),
            ("times", "valid_from", "2026-08-08T02:00:00Z",
             "valid_from must not exceed valid_to"),
            ("times", "released_at", "2026-08-08T00:05:30Z",
             "released_at must not precede retrieved_at"),
            ("times", "corrected_at", "2026-08-08T00:06:30Z",
             "corrected_at requires and must not precede released_at"),
            (None, "temporal_posture", "SUPERSEDED", "SUPERSEDED requires supersedes_ref"),
            (None, "temporal_posture", "WITHDRAWN", "WITHDRAWN requires withdrawal_ref"),
            (None, "freshness_deadline", "2026-08-16T23:59:59Z",
             "CURRENT envelope freshness_deadline is elapsed"),
        )
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            for section, field, value, expected in mutations:
                candidate = deepcopy(base)
                target = candidate[section] if section else candidate
                target[field] = value
                before = deepcopy(candidate)
                for engine in (LEGACY, CANONICAL, LEGACY):
                    with self.subTest(engine=engine.__name__, field=field, value=value):
                        self.assertEqual([expected], engine.validate_doc(candidate, now=NOW))
                        self.assertEqual(before, candidate)

    def test_replay_uses_the_supplied_validation_instant(self) -> None:
        candidate = correction_replay_cases()["corrected"]
        candidate["freshness_deadline"] = "2026-08-17T00:00:00Z"
        elapsed = datetime(2026, 8, 17, 0, 0, 1, tzinfo=timezone.utc)
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            for engine in (LEGACY, CANONICAL, LEGACY):
                self.assertEqual([], engine.validate_doc(candidate, now=NOW))
                self.assertEqual(
                    ["CURRENT envelope freshness_deadline is elapsed"],
                    engine.validate_doc(candidate, now=elapsed),
                )
                self.assertEqual([], engine.validate_doc(candidate, now=NOW))

    def test_replay_preserves_legacy_namespace_and_receipt_lineage(self) -> None:
        receipt_root = ROOT / "data/receipts/generated"
        predecessor = receipt_root / "genrec-evidence-temporal-posture-split-phase1-20260817.json"
        successor = receipt_root / "genrec-evidence-temporal-posture-split-reconciliation-20260827.json"
        receipt = load(successor)
        predecessor_digest = "sha256:" + hashlib.sha256(predecessor.read_bytes()).hexdigest()
        self.assertIn(predecessor_digest, receipt["inputs"]["evidence_hashes"])
        self.assertIn(
            "repository://" + predecessor.relative_to(ROOT).as_posix(),
            receipt["inputs"]["evidence_refs"],
        )
        # Only these unchanged replay inputs are bound; historical check results
        # and changed test/workflow bytes are not claimed as current evidence.
        for path in (CANONICAL_ROOT / "valid/current_observation.json", CANONICAL.CANONICAL_SCHEMA):
            self.assertEqual(
                receipt["artifact_hashes"][path.relative_to(ROOT).as_posix()],
                "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest(),
            )
        candidate = correction_replay_cases()["corrected"]
        candidate["envelope_id"] = "kfm:evidence-temporal-posture:mesonet.demo.1"
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            legacy = LEGACY.validate_doc(candidate, now=NOW)
            self.assertEqual(legacy, CANONICAL.validate_doc(candidate, now=NOW))
        self.assertEqual(1, len(legacy))
        self.assertIn("does not match", legacy[0])

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

    def test_unreadable_inputs_are_finite_errors(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            truncated = Path(tmp) / "truncated.json"
            truncated.write_text('{"time": ', encoding="utf-8")
            missing = Path(tmp) / "missing.json"
            for module in (CANONICAL, LEGACY):
                for path in (truncated, missing):
                    with self.subTest(module=module.__name__, path=path.name):
                        self.assertEqual(["input is not readable JSON"], module.validate_file(path))

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
