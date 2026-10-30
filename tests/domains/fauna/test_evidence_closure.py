"""Offline metadata binding, abstention, and the remaining evidence-closure gate."""
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

from fauna import EvidenceCatalog, TaxonomyCatalog, normalize_occurrence
from fauna.evidence import MAX_BUNDLES, MAX_BUNDLE_REFS, MAX_SCHEMA_RESOURCES


def read(relative):
    return json.loads((ROOT / relative).read_text())


SCHEMA = read("schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json")
BUNDLE_SCHEMA = read("schemas/contracts/v1/evidence/evidence_bundle.schema.json")
RESOURCES = [read("schemas/contracts/v1/" + relative) for relative in (
    "evidence/evidence_ref.schema.json", "policy/sensitivity_label.schema.json",
    "common/spec_hash.schema.json",
)]
BUNDLES = read("fixtures/domains/fauna/evidence_bindings/bundles.json")
SOURCE = read("fixtures/domains/fauna/occurrence_evidence/valid/valid_observed_open.json")


class EvidenceBindingTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden"))
        patcher.start()
        self.addCleanup(patcher.stop)
        taxonomy = TaxonomyCatalog.from_candidate(
            read("fixtures/domains/fauna/normalization/taxonomy_snapshot.json"),
            schema=read("schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json"),
        )
        self.record = normalize_occurrence(
            SOURCE, taxonomy=taxonomy, schema=SCHEMA, validated_at="2026-10-29T00:00:00Z",
        ).occurrence
        self.assertIsNotNone(self.record)

    def catalog(self, bundles=None, **kwargs):
        return EvidenceCatalog.from_candidates(
            copy.deepcopy(BUNDLES if bundles is None else bundles),
            schema=kwargs.get("schema", BUNDLE_SCHEMA), resources=kwargs.get("resources", RESOURCES),
        )

    def test_links_all_occurrence_and_taxonomy_references_without_closing_or_mutating(self):
        before = copy.deepcopy(self.record)
        result = self.catalog().assess(self.record, schema=SCHEMA)
        self.assertEqual(result.outcome, "linked")
        self.assertEqual((result.required_refs, result.linked_refs), (3, 3))
        self.assertFalse(result.public_ready)
        self.assertFalse(result.integrity_verified)
        self.assertEqual(self.record, before)
        self.assertEqual(self.record["validation"]["validator_result"], "quarantine")
        self.assertIn("prov.evidence_closure_unverified", self.record["validation"]["reason_codes"])
        self.assertEqual(self.record["geometry"]["public_safe_geometry"]["geometry_type"], "withheld")

    def test_empty_or_partial_inventory_abstains_instead_of_using_taxonomy_as_occurrence_evidence(self):
        for bundles, linked in (([], 0), ([BUNDLES[1]], 2), ([BUNDLES[0]], 1)):
            with self.subTest(linked=linked):
                result = self.catalog(bundles).assess(self.record, schema=SCHEMA)
                self.assertEqual(result.outcome, "abstain")
                self.assertEqual(result.linked_refs, linked)
                self.assertTrue(all(f.code == "prov.evidence_ref_unresolved" for f in result.findings))

    def test_references_match_exactly_without_case_or_uri_normalization(self):
        bundles = copy.deepcopy(BUNDLES)
        bundles[0]["evidence_refs"][0]["ref"] = bundles[0]["evidence_refs"][0]["ref"].upper()
        self.assertEqual(self.catalog(bundles).assess(self.record, schema=SCHEMA).outcome, "abstain")

    def test_cross_bundle_collision_abstains_independently_of_input_order(self):
        other = copy.deepcopy(BUNDLES[0])
        other["bundle_id"] = "fixture:bundle:other"
        other["evidence_refs"][0]["bundle_ref"] = other["bundle_id"]
        for bundles in ([*BUNDLES, other], [other, *reversed(BUNDLES)]):
            result = self.catalog(bundles).assess(self.record, schema=SCHEMA)
            self.assertEqual(result.outcome, "abstain")
            self.assertEqual(result.linked_refs, 2)
            self.assertEqual(result.findings[0].code, "prov.evidence_ref_ambiguous")

    def test_source_record_must_be_declared_by_a_linked_bundle(self):
        bundles = copy.deepcopy(BUNDLES)
        bundles[0]["source_records"] = ["fixture:unrelated"]
        result = self.catalog(bundles).assess(self.record, schema=SCHEMA)
        self.assertEqual(result.linked_refs, 3)
        self.assertEqual(result.findings[0].code, "prov.source_record_binding_missing")

    def test_raw_artifact_checksum_declaration_must_share_source_record_support(self):
        bundles = copy.deepcopy(BUNDLES)
        raw = self.record["provenance"]["raw_artifact_ref"]
        bundles[0]["checksums"] = {"fixture:unrelated": "sha256:" + "3" * 64}
        bundles[1]["checksums"][raw] = "sha256:" + "1" * 64
        result = self.catalog(bundles).assess(self.record, schema=SCHEMA)
        self.assertEqual(result.outcome, "abstain")
        self.assertEqual(result.findings[0].code, "prov.raw_artifact_binding_missing")

    def test_declared_hashes_are_never_reported_as_verified_bytes(self):
        bundles = copy.deepcopy(BUNDLES)
        bundles[0]["checksums"] = {key: "sha256:" + "f" * 64 for key in bundles[0]["checksums"]}
        result = self.catalog(bundles).assess(self.record, schema=SCHEMA)
        self.assertEqual(result.outcome, "linked")
        self.assertFalse(result.integrity_verified)

    def test_preserves_upstream_deny_and_error(self):
        for disposition in ("deny", "error"):
            record = copy.deepcopy(self.record)
            record["validation"]["validator_result"] = disposition
            result = self.catalog().assess(record, schema=SCHEMA)
            self.assertEqual(result.outcome, disposition)
            self.assertEqual(result.linked_refs, 0)

    def test_invalid_occurrence_never_becomes_linked_or_raises(self):
        bad = copy.deepcopy(self.record)
        bad["validation"]["validator_result"] = []
        for record in (None, [], {}, bad):
            with self.subTest(record_type=type(record).__name__):
                self.assertEqual(self.catalog().assess(record, schema=SCHEMA).outcome, "error")

    def test_mutating_candidate_inventory_cannot_change_the_built_index(self):
        bundles = copy.deepcopy(BUNDLES)
        before = copy.deepcopy(bundles)
        catalog = EvidenceCatalog.from_candidates(bundles, schema=BUNDLE_SCHEMA, resources=RESOURCES)
        self.assertEqual(bundles, before)
        bundles[0]["source_records"].clear()
        bundles[0]["checksums"].clear()
        bundles[0]["evidence_refs"].clear()
        self.assertEqual(catalog.assess(self.record, schema=SCHEMA).outcome, "linked")

    def test_duplicate_bundle_ids_and_duplicate_constituents_are_rejected(self):
        repeated_ref = copy.deepcopy(BUNDLES[0])
        repeated_ref["evidence_refs"].append(copy.deepcopy(repeated_ref["evidence_refs"][0]))
        for bundles in ([*BUNDLES, BUNDLES[0]], [repeated_ref]):
            with self.assertRaisesRegex(ValueError, "prov.evidence_inventory_invalid"):
                self.catalog(bundles)

    def test_bundle_reference_cannot_silently_point_elsewhere(self):
        bundles = copy.deepcopy(BUNDLES)
        bundles[0]["evidence_refs"][0]["bundle_ref"] = "fixture:bundle:elsewhere"
        with self.assertRaisesRegex(ValueError, "prov.bundle_reference_mismatch"):
            self.catalog(bundles)

    def test_shared_schema_enforces_fields_types_and_formats(self):
        mutations = (("citations", []), ("rights", {}), ("extra", "private-location-clue"),
                     ("sensitivity", {"level": "quarantine", "reason": "fixture", "applied_at": "yesterday"}))
        for key, value in mutations:
            bundles = copy.deepcopy(BUNDLES)
            bundles[0][key] = value
            with self.assertRaisesRegex(ValueError, "schema.evidence_bundle_invalid"):
                self.catalog(bundles)

    def test_schema_permitted_blank_semantic_metadata_is_rejected_for_binding(self):
        for key, value in (("claim_scope", " "), ("source_records", [""]), ("citations", [" "])):
            bundles = copy.deepcopy(BUNDLES)
            bundles[0][key] = value
            with self.assertRaisesRegex(ValueError, "prov.evidence_metadata_empty"):
                self.catalog(bundles)

    def test_inventory_shape_and_operational_bounds(self):
        for bundles in ({}, None, [BUNDLES[0]] * (MAX_BUNDLES + 1)):
            with self.assertRaisesRegex(ValueError, "prov.evidence_inventory_invalid"):
                EvidenceCatalog.from_candidates(bundles, schema=BUNDLE_SCHEMA, resources=RESOURCES)
        bundles = copy.deepcopy(BUNDLES)
        bundles[0]["evidence_refs"] = [{"ref": "fixture:" + str(i), "kind": "record"} for i in range(MAX_BUNDLE_REFS + 1)]
        with self.assertRaisesRegex(ValueError, "prov.evidence_inventory_invalid"):
            self.catalog(bundles)

    def test_missing_remote_and_invalid_schema_resources_fail_without_network(self):
        remote = copy.deepcopy(BUNDLE_SCHEMA)
        remote["properties"]["evidence_refs"]["items"] = {"$ref": "https://example.invalid/private-schema"}
        invalid = copy.deepcopy(BUNDLE_SCHEMA)
        invalid["type"] = "impossible"
        for schema, resources in ((BUNDLE_SCHEMA, []), (remote, RESOURCES), (invalid, RESOURCES),
                                  (BUNDLE_SCHEMA, RESOURCES * (MAX_SCHEMA_RESOURCES + 1))):
            with self.assertRaisesRegex(ValueError, "schema.evidence_bundle_unavailable"):
                self.catalog(schema=schema, resources=resources)

    def test_result_diagnostics_and_repr_do_not_expose_source_metadata(self):
        catalog = self.catalog([])
        rendered = repr(catalog) + repr(catalog.assess(self.record, schema=SCHEMA))
        for private in (self.record["source_record_id"], "fixture:evidence", "Specimen", "latitude", "longitude"):
            self.assertNotIn(private, rendered)


if __name__ == "__main__":
    unittest.main()
