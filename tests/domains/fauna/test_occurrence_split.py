"""Normalization, role preservation, and withheld projection boundary tests."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "packages/domains/fauna/src"))
sys.path.insert(0, str(ROOT / "packages/hashing/src"))

from fauna import TaxonomyCatalog, compute_occurrence_spec_hash, normalize_occurrence, prepare_public_candidate, validate_candidate

SCHEMA = json.loads((ROOT / "schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json").read_text())
TAXONOMY_SCHEMA = json.loads((ROOT / "schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json").read_text())
SNAPSHOT = json.loads((ROOT / "fixtures/domains/fauna/normalization/taxonomy_snapshot.json").read_text())
FIXTURE_ROOT = ROOT / "fixtures/domains/fauna/occurrence_evidence/valid"
VALIDATED_AT = "2026-10-29T00:00:00Z"


def load(name="valid_observed_open.json"):
    return json.loads((FIXTURE_ROOT / name).read_text())


class OccurrenceSplitTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden"))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.taxonomy = TaxonomyCatalog.from_candidate(SNAPSHOT, schema=TAXONOMY_SCHEMA)

    def normalize(self, candidate, **kwargs):
        return normalize_occurrence(candidate, taxonomy=self.taxonomy, schema=SCHEMA,
                                    validated_at=kwargs.get("validated_at", VALIDATED_AT))

    def test_normalized_record_stays_held_and_preserves_internal_evidence(self):
        source = load()
        original = copy.deepcopy(source)
        result = self.normalize(source)
        self.assertEqual(source, original)
        self.assertEqual(result.outcome, "quarantine")
        record = result.occurrence
        self.assertTrue(validate_candidate(record, schema=SCHEMA).ok)
        self.assertEqual(record["geometry"]["latitude"], source["geometry"]["latitude"])
        self.assertEqual(record["geometry"]["longitude"], source["geometry"]["longitude"])
        self.assertEqual(record["source_role"], source["source_role"])
        self.assertEqual(record["observation"], source["observation"])
        self.assertEqual(record["provenance"]["raw_artifact_ref"], source["provenance"]["raw_artifact_ref"])
        self.assertIn(SNAPSHOT["snapshot_ref"], record["provenance"]["evidence_refs"])
        self.assertEqual(record["validation"]["validator_result"], "quarantine")
        self.assertEqual(record["validation"]["evidence_strength"], "unreviewed")
        self.assertIsNone(record["geometry"]["public_safe_geometry"]["coordinates"])
        self.assertEqual(prepare_public_candidate(record, schema=SCHEMA).outcome, "HOLD")

    def test_taxonomy_synonym_resolution_preserves_original_assertion(self):
        source = load()
        source["taxon"]["scientific_name"] = "Specimen antiquus"
        record = self.normalize(source).occurrence
        self.assertEqual(record["taxon"]["scientific_name"], "Specimen antiquus")
        self.assertEqual(record["taxon"]["accepted_scientific_name"], "Specimen fictivus")

    def test_unresolved_and_ambiguous_taxa_have_no_normalized_payload(self):
        for name in ("Specimen ambiguus", "Specimen unknownus"):
            source = load()
            source["taxon"]["scientific_name"] = name
            result = self.normalize(source)
            self.assertEqual(result.outcome, "quarantine")
            self.assertIsNone(result.occurrence)
            self.assertTrue(result.findings)

    def test_invalid_inputs_do_not_receive_fabricated_coordinates_or_dates(self):
        for mutate in (
            lambda x: x["geometry"].pop("latitude"),
            lambda x: x["observation"].pop("event_date"),
            lambda x: x["geometry"].update({"longitude": 181}),
            lambda x: x["geometry"].update({"latitude": float("nan")}),
            lambda x: x["provenance"].update({"evidence_refs": []}),
            lambda x: x["provenance"].update({"raw_artifact_ref": None}),
            lambda x: x["rights"].update({"license": "UNKNOWN"}),
            lambda x: x.update({"extra": "not-admitted"}),
        ):
            source = load()
            mutate(source)
            result = self.normalize(source)
            self.assertEqual(result.outcome, "error", result.findings)
            self.assertIsNone(result.occurrence)

    def test_source_roles_cannot_be_changed_by_basis_or_taxonomy(self):
        source = load("valid_modeled_context.json")
        record = self.normalize(source).occurrence
        self.assertEqual(record["source_role"], "modeled")
        self.assertEqual(record["observation"]["basis_of_record"], "model_output")
        source["source_role"] = "observed"
        result = self.normalize(source)
        self.assertIsNone(result.occurrence)
        self.assertIn("obs.source_role_mismatch", {f.code for f in result.findings})

    def test_deny_and_error_cannot_be_reopened_by_normalization(self):
        for outcome in ("deny", "error"):
            source = load()
            source["validation"]["validator_result"] = outcome
            result = self.normalize(source)
            self.assertEqual(result.outcome, outcome)
            self.assertIsNone(result.occurrence)

    def test_existing_hold_reasons_survive_normalization(self):
        source = load()
        source["validation"].update({"validator_result": "quarantine", "reason_codes": ["rights.owner_review_pending"]})
        record = self.normalize(source).occurrence
        self.assertIn("rights.owner_review_pending", record["validation"]["reason_codes"])

    def test_validation_time_does_not_change_observation_or_identity(self):
        source = load()
        first = self.normalize(source).occurrence
        second = self.normalize(source, validated_at="2026-10-30T00:00:00Z").occurrence
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["observation"], second["observation"])
        self.assertNotEqual(first["validation"]["validated_at"], second["validation"]["validated_at"])
        self.assertEqual(self.normalize(source, validated_at="not-a-time").outcome, "error")

    def test_normalization_is_idempotent_for_fixed_snapshot_and_time(self):
        first = self.normalize(load()).occurrence
        second = self.normalize(first).occurrence
        self.assertEqual(first, second)
        self.assertEqual(first["spec_hash"], compute_occurrence_spec_hash(first))

    def test_internal_payload_is_absent_from_result_repr(self):
        source = load()
        source["geometry"].update({"latitude": 12.345678, "longitude": 34.56789})
        result = self.normalize(source)
        self.assertIsNotNone(result.occurrence)
        for value in ("12.345678", "34.56789", source["source_record_id"]):
            self.assertNotIn(value, repr(result))

    def test_projection_uses_positive_allowlist_and_is_unreleased(self):
        result = prepare_public_candidate(load(), schema=SCHEMA)
        self.assertEqual(result.outcome, "CANDIDATE")
        self.assertEqual(result.payload["publication_state"], "unreleased")
        self.assertEqual(result.payload["audience"], "internal")
        self.assertIsNone(result.payload["geometry"])
        rendered = json.dumps(result.payload)
        for forbidden in ("source_record_id", "latitude", "longitude", "observed_by", "source_uri", "retrieved_at", "event_date", "evidence_refs"):
            self.assertNotIn(forbidden, rendered)

    def test_projection_never_forwards_sensitive_or_held_records(self):
        result = prepare_public_candidate(load("valid_sensitive_withheld_quarantine.json"), schema=SCHEMA)
        self.assertEqual(result.outcome, "HOLD")
        self.assertIsNone(result.payload)
        source = load()
        source["sensitivity"].update({"sensitive_species_flag": True, "review_required": True})
        source["validation"]["evidence_strength"] = "steward_reviewed"
        result = prepare_public_candidate(source, schema=SCHEMA)
        self.assertEqual(result.outcome, "WITHHELD")
        self.assertIsNone(result.payload)

    def test_unknown_fields_and_forged_identity_never_reach_projection(self):
        for mutate in (
            lambda x: x.update({"private_notes": "exact-location-clue"}),
            lambda x: x.update({"spec_hash": "sha256:" + "0" * 64}),
        ):
            source = load()
            mutate(source)
            result = prepare_public_candidate(source, schema=SCHEMA)
            self.assertEqual(result.outcome, "ERROR")
            self.assertIsNone(result.payload)

    def test_redistribution_denial_withholds_review_projection(self):
        source = load()
        source["rights"]["redistribution_allowed"] = False
        self.assertTrue(validate_candidate(source, schema=SCHEMA).ok)
        result = prepare_public_candidate(source, schema=SCHEMA)
        self.assertEqual(result.outcome, "HOLD")
        self.assertIsNone(result.payload)

    def test_invalid_or_remote_schema_fails_closed_without_network(self):
        for schema in ({"type": 17}, {"$ref": "https://invalid.example/schema"}):
            result = validate_candidate(load(), schema=schema)
            self.assertFalse(result.ok)
            self.assertEqual(result.findings[0].code, "schema.unavailable")


if __name__ == "__main__":
    unittest.main()
