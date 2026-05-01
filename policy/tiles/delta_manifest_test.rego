package tiles.delta_manifest

valid_manifest := {
  "base_pmtiles": {"spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "url": "https://cdn.example.org/base.pmtiles"},
  "tiles": [
    {"change_type": "added", "digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "prior_digest": null, "run_receipt_url": "https://receipts.example.org/a"}
  ]
}

missing_spec_hash_manifest := {
  "base_pmtiles": {"url": "https://cdn.example.org/base.pmtiles"},
  "tiles": [
    {"change_type": "added", "digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "prior_digest": null, "run_receipt_url": "https://receipts.example.org/a"}
  ]
}

rollback_mismatch_manifest := {
  "base_pmtiles": {"spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "url": "https://cdn.example.org/base.pmtiles"},
  "tiles": [
    {"change_type": "modified", "digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "prior_digest": null, "run_receipt_url": "https://receipts.example.org/a"}
  ]
}

test_valid_manifest_has_no_deny if {
  count(deny) with input as valid_manifest == 0
}

test_missing_spec_hash_denied if {
  "missing base_pmtiles.spec_hash" in deny with input as missing_spec_hash_manifest
}

test_rollback_rules_denied if {
  "rollback-risk: modified tile missing prior_digest" in deny with input as rollback_mismatch_manifest
}
