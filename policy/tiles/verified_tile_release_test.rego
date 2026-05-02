package policy.tiles.verified_tile_release
import data.tiles.verified_tile_release.deny

test_allow if { count(deny with input as {"proof_bundle":true,"validation_result":"ALLOW","trace_pass":true,"public_artifacts":["published/a"],"runtime_contract":{"render_mode":"verified_only"},"required_refs":{"EvidenceBundle":"x","ReleaseManifest":"y"},"rollback_ref":"r","correction_ref":"c","sensitivity":"public_safe","rights":"public"})==0 }

test_deny_missing_bundle if { "missing proof bundle" in deny with input as {} }
