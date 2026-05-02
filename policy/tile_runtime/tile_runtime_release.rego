package tile_runtime.release

default allow := false

allowed_policy_labels := {"kfm.tile_runtime.v1"}
allowed_runtime_profiles := {"mobile_emulated_mid", "mobile_emulated_low", "mobile_emulated_high"}

deny[msg] if input.receipt.failed_tile_count > 0 { msg := "failed tiles present" }
deny[msg] if input.receipt.budget_decision != "allow" { msg := "budget denied" }
deny[msg] if input.receipt.public_safe != true { msg := "receipt not public safe" }
deny[msg] if not input.trace_manifest { msg := "missing trace manifest" }
deny[msg] if input.trace_manifest.contains_raw_urls { msg := "trace contains raw urls" }
deny[msg] if input.trace_manifest.contains_internal_paths { msg := "trace contains internal paths" }
deny[msg] if input.trace_manifest.contains_sensitive_geometry { msg := "trace contains sensitive geometry" }
deny[msg] if count(input.receipt.evidence_bundle_refs) == 0 { msg := "missing evidence refs" }
deny[msg] if input.receipt.release_manifest_ref == "" { msg := "missing release manifest ref" }
deny[msg] if not input.receipt.policy_label in allowed_policy_labels { msg := "unknown policy_label" }
deny[msg] if not input.receipt.runtime_profile in allowed_runtime_profiles { msg := "unknown runtime_profile" }

allow if count(deny) == 0
