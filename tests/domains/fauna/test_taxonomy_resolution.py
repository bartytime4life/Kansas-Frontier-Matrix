"""Offline, snapshot-bound taxonomy matching and ambiguity regression tests."""
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

from fauna import TaxonomyCatalog

SCHEMA = json.loads((ROOT / "schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json").read_text())
SNAPSHOT = json.loads((ROOT / "fixtures/domains/fauna/normalization/taxonomy_snapshot.json").read_text())


class TaxonomyResolutionTests(unittest.TestCase):
    def setUp(self):
        self.network = patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden"))
        self.network.start()
        self.addCleanup(self.network.stop)
        self.catalog = TaxonomyCatalog.from_candidate(SNAPSHOT, schema=SCHEMA)

    def test_accepted_name_is_bound_to_snapshot_and_evidence(self):
        result = self.catalog.resolve("Specimen fictivus")
        self.assertEqual(result.outcome, "resolved")
        self.assertEqual(result.authority, SNAPSHOT["authority"])
        self.assertEqual(result.snapshot_ref, SNAPSHOT["snapshot_ref"])
        self.assertEqual(result.concept.concept_id, "fixture:taxon:fauna:001")
        self.assertTrue(result.concept.evidence_refs)

    def test_explicit_synonym_preserves_source_name(self):
        result = self.catalog.resolve("  SPECIMEN   antiquus ")
        self.assertEqual(result.outcome, "resolved")
        self.assertEqual(result.queried_name, "  SPECIMEN   antiquus ")
        self.assertEqual(result.concept.accepted_scientific_name, "Specimen fictivus")

    def test_unlisted_name_is_not_fuzzy_matched_or_stripped_of_authorship(self):
        for name in ("Specimen fictivu", "Specimen fictivus Author, 1900", "Unknown animal"):
            with self.subTest(name=name):
                result = self.catalog.resolve(name)
                self.assertEqual(result.outcome, "unresolved")
                self.assertIsNone(result.concept)

    def test_ambiguous_synonym_abstains_independent_of_inventory_order(self):
        for reverse in (False, True):
            snapshot = copy.deepcopy(SNAPSHOT)
            if reverse:
                snapshot["concepts"].reverse()
            result = TaxonomyCatalog.from_candidate(snapshot, schema=SCHEMA).resolve("Specimen ambiguus")
            self.assertEqual(result.outcome, "ambiguous")
            self.assertIsNone(result.concept)
            self.assertEqual(result.findings[0].code, "taxon.name_ambiguous")

    def test_invalid_names_abstain(self):
        for name in (None, [], {}, 123, "", "  ", "a" * 257):
            self.assertEqual(self.catalog.resolve(name).outcome, "unresolved")

    def test_snapshot_is_closed_and_requires_evidence(self):
        for mutate in (
            lambda x: x.update({"live_url": "https://invalid.example/"}),
            lambda x: x.update({"state": "approved"}),
            lambda x: x["concepts"][0].update({"evidence_refs": []}),
            lambda x: x["concepts"][0].update({"taxon_rank": "guessed"}),
        ):
            candidate = copy.deepcopy(SNAPSHOT)
            mutate(candidate)
            with self.assertRaisesRegex(ValueError, "taxon.snapshot_invalid"):
                TaxonomyCatalog.from_candidate(candidate, schema=SCHEMA)

    def test_duplicate_concept_identity_is_rejected(self):
        candidate = copy.deepcopy(SNAPSHOT)
        candidate["concepts"][1]["concept_id"] = candidate["concepts"][0]["concept_id"]
        with self.assertRaisesRegex(ValueError, "taxon.duplicate_concept"):
            TaxonomyCatalog.from_candidate(candidate, schema=SCHEMA)

    def test_remote_schema_reference_cannot_make_network_request(self):
        schema = {"$ref": "https://invalid.example/schema"}
        with self.assertRaisesRegex(ValueError, "taxon.schema_unavailable"):
            TaxonomyCatalog.from_candidate(SNAPSHOT, schema=schema)

    def test_catalog_does_not_change_when_original_snapshot_changes(self):
        candidate = copy.deepcopy(SNAPSHOT)
        catalog = TaxonomyCatalog.from_candidate(candidate, schema=SCHEMA)
        candidate["concepts"][0]["synonyms"].clear()
        self.assertEqual(catalog.resolve("Specimen antiquus").outcome, "resolved")


if __name__ == "__main__":
    unittest.main()
