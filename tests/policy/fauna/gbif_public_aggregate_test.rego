package kfm.fauna.gbif_public_aggregate

import data.kfm.fauna.gbif_public_aggregate

base := {"source_evidence_bundle_id":"eb1","download_key":"d1","kfm:spec_hash":"sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","geoprivacy_receipt_ref":"r1","observation_count":10,"rights_posture":"public_allowed","sensitivity_posture":"public_generalized","geometry_role":"generalized_public_area"}

test_allow_base if { count(gbif_public_aggregate.deny with input as base) == 0 }
test_deny_exact_coords if { count(gbif_public_aggregate.deny with input as object.union(base,{"decimalLatitude":1.1})) > 0 }
test_deny_missing_refs if { count(gbif_public_aggregate.deny with input as object.remove(base,["source_evidence_bundle_id"])) > 0 }
test_deny_observation_count if { count(gbif_public_aggregate.deny with input as object.union(base,{"observation_count":9})) > 0 }
