package kfm.air.public_ops

default allow := false
allow if { count(deny) == 0 }

deny["fixture_only_cannot_be_green"] if { input.all_fixture_backed; input.health_status == "green" }
deny["missing_lineage_audit"] if { not input.lineage_audit }
deny["lineage_audit_denied"] if { input.lineage_audit.result == "deny" }
deny["missing_public_read_model"] if { not input.public_read_model_present }
deny["missing_publication_manifest"] if { not input.publication_manifest_present }
deny["promotion_not_approved_for_catalog"] if { input.promotion_decision.decision != "approved_for_catalog" }
deny["release_not_public_ready"] if { input.release_manifest.public_readiness.status != "catalog_candidate"; input.release_manifest.public_readiness.status != "published" }
deny["hash_missing_or_mismatch"] if { input.hashes_verified != true }
deny["unsafe_internal_reference"] if { input.path_safety_ok != true }
deny["fixture_marked_real_public_truth"] if { input.fixture_real_public_truth }
deny["nowcast_labelled_validated_truth"] if { input.nowcast_validated_truth }
deny["active_tombstoned_publication"] if { input.retracted_active }
deny["unresolved_high_critical_incident"] if { input.unresolved_high_or_critical_incident }
deny["slo_pass_with_hard_failure"] if { input.slo.status == "pass"; count(input.slo.hard_failures) > 0 }
deny["retraction_approval_missing_steward_review"] if { input.retraction_request.status == "approved"; not input.retraction_request.steward_review_metadata }
