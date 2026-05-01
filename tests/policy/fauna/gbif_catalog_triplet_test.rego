package kfm.fauna.gbif_catalog_triplet
import data.kfm.fauna.gbif_catalog_triplet

base := {"catalog_entry":{},"evidence":{},"source_evidence_bundle_id":"eb1","download_key":"d1","geoprivacy_receipt_ref":"r1","kfm:spec_hash":"sha256:x","rights_posture":"public_allowed","sensitivity_posture":"public_generalized","presence_posture":"reported_occurrence_not_confirmed_presence","claim_text":"GBIF-reported public occurrence aggregate","answer_posture":"abstain","query":{"exact_coordinates_requested":true},"claims":[]}

test_allow if { count(gbif_catalog_triplet.deny with input as base) == 0 }
test_deny_presence if { count(gbif_catalog_triplet.deny with input as object.union(base,{"presence_posture":"confirmed_present"})) > 0 }
