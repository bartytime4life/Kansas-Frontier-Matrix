package kfm.flora.usda_plants_release_test
import rego.v1
import data.kfm.flora.usda_plants_release

base := {"dataset_count": 1,"dataset_refs": ["processed/flora/usda_plants/ACMI2.json"],"evidence_link_refs": ["evidence/flora/usda_plants/ACMI2.evidence_link.json"],"catalog_refs": ["catalog/flora/usda_plants/catalog.json"],"receipt_refs": ["receipts/flora/usda_plants/ingest_receipt.json"],"proof_refs": ["proofs/flora/usda_plants/spec_hash_manifest.json"],"promotion_state": "not_promoted","publication_state": "not_published","gates": {"publication": "blocked"},"release_candidate_hash": "sha256:abc","map_layer_contract_refs": [],"blockers":["x"]}

test_valid if { count(usda_plants_release.deny with input as base) == 0 }
test_published_denied if { "USDA_PLANTS_RELEASE_BAD_PUBLICATION_STATE" in usda_plants_release.deny with input as object.union(base,{"publication_state":"published"}) }
test_promoted_denied if { "USDA_PLANTS_RELEASE_BAD_PROMOTION_STATE" in usda_plants_release.deny with input as object.union(base,{"promotion_state":"promoted"}) }
test_missing_proof if { "USDA_PLANTS_RELEASE_MISSING_PROOF" in usda_plants_release.deny with input as object.union(base,{"proof_refs":[]}) }
test_missing_catalog if { "USDA_PLANTS_RELEASE_MISSING_CATALOG" in usda_plants_release.deny with input as object.union(base,{"catalog_refs":[]}) }
test_raw_leak if { "USDA_PLANTS_RELEASE_RAW_REF_LEAK" in usda_plants_release.deny with input as object.union(base,{"dataset_refs":["raw/x"]}) }
test_work_leak if { "USDA_PLANTS_RELEASE_WORK_REF_LEAK" in usda_plants_release.deny with input as object.union(base,{"dataset_refs":["work/x"]}) }
test_quarantine_leak if { "USDA_PLANTS_RELEASE_QUARANTINE_REF_LEAK" in usda_plants_release.deny with input as object.union(base,{"dataset_refs":["quarantine/x"]}) }
test_missing_hash if { "USDA_PLANTS_RELEASE_MISSING_HASH" in usda_plants_release.deny with input as object.union(base,{"release_candidate_hash":""}) }
test_map_contract_published if { "USDA_PLANTS_RELEASE_MAP_CONTRACT_PUBLISHED" in usda_plants_release.deny with input as object.union(base,{"map_layer_contract_refs":["published/flora/x"]}) }
