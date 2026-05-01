package kfm.fauna.gbif

import data.kfm.fauna.gbif

test_deny_missing_spec_hash if {
  count(gbif.deny with input as {"evidence_bundle_id":"x"}) > 0
}

test_deny_small_public_aggregate if {
  count(gbif.deny with input as {
    "evidence_bundle_id":"x","kfm:spec_hash":"sha256:abc","source_uri":"u","download_key":"d","query_predicate":{},
    "records_count": 9,
    "license_summary": ["CC0"],
    "outputs": {"publication_target":"public","normalized_records":[]}
  }) > 0
}
