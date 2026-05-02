package tile_runtime.release

test_allow_valid if {
  allow with input as {"receipt": {"failed_tile_count":0,"budget_decision":"allow","public_safe":true,"evidence_bundle_refs":["e1"],"release_manifest_ref":"r","policy_label":"kfm.tile_runtime.v1","runtime_profile":"mobile_emulated_mid"},"trace_manifest":{"contains_raw_urls":false,"contains_internal_paths":false,"contains_sensitive_geometry":false}}
}

test_deny_bad_budget if {
  count(deny with input as {"receipt": {"failed_tile_count":0,"budget_decision":"deny","public_safe":true,"evidence_bundle_refs":["e1"],"release_manifest_ref":"r","policy_label":"kfm.tile_runtime.v1","runtime_profile":"mobile_emulated_mid"},"trace_manifest":{"contains_raw_urls":false,"contains_internal_paths":false,"contains_sensitive_geometry":false}}) > 0
}
