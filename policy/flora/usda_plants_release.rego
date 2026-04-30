package kfm.flora.usda_plants_release

import rego.v1

deny contains "USDA_PLANTS_RELEASE_MISSING_DATASETS" if { input.dataset_count == 0 }
deny contains "USDA_PLANTS_RELEASE_MISSING_EVIDENCE_LINKS" if { count(input.evidence_link_refs) == 0 }
deny contains "USDA_PLANTS_RELEASE_MISSING_CATALOG" if { count(input.catalog_refs) == 0 }
deny contains "USDA_PLANTS_RELEASE_MISSING_PROOF" if { count(input.proof_refs) == 0 }
deny contains "USDA_PLANTS_RELEASE_MISSING_RECEIPTS" if { count(input.receipt_refs) == 0 }
deny contains "USDA_PLANTS_RELEASE_BAD_PROMOTION_STATE" if { input.promotion_state != "not_promoted" }
deny contains "USDA_PLANTS_RELEASE_BAD_PUBLICATION_STATE" if { input.publication_state != "not_published" }
deny contains "USDA_PLANTS_RELEASE_PUBLICATION_NOT_BLOCKED" if { input.gates.publication != "blocked" }
deny contains "USDA_PLANTS_RELEASE_MISSING_HASH" if { not input.release_candidate_hash }
deny contains "USDA_PLANTS_RELEASE_MAP_CONTRACT_PUBLISHED" if { some r in input.map_layer_contract_refs; contains(lower(r), "published") }

deny contains "USDA_PLANTS_RELEASE_RAW_REF_LEAK" if { leaked_ref("raw/") }
deny contains "USDA_PLANTS_RELEASE_WORK_REF_LEAK" if { leaked_ref("work/") }
deny contains "USDA_PLANTS_RELEASE_QUARANTINE_REF_LEAK" if { leaked_ref("quarantine/") }

deny contains "USDA_PLANTS_RELEASE_HASH_MISMATCH" if { not startswith(input.release_candidate_hash, "sha256:") }

leaked_ref(x) if { some r in input.dataset_refs; contains(lower(r), x) }
leaked_ref(x) if { some r in input.evidence_link_refs; contains(lower(r), x) }
leaked_ref(x) if { some r in input.catalog_refs; contains(lower(r), x) }
leaked_ref(x) if { some r in input.receipt_refs; contains(lower(r), x) }
leaked_ref(x) if { some r in input.proof_refs; contains(lower(r), x) }
