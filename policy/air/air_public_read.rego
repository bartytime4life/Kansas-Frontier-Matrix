package kfm.air.public_read

default allow := false
allow if { count(deny) == 0 }

unsafe_path(p) if { contains(lower(p), "/raw/") }
unsafe_path(p) if { contains(lower(p), "/work/") }
unsafe_path(p) if { contains(lower(p), "/quarantine/") }
unsafe_path(p) if { contains(lower(p), "data/processed/air/") }

deny["missing_publication_manifest"] if { not input.publication_manifest }
deny["fixture_blocked_cannot_be_published_index"] if { input.publication_manifest.status == "published_fixture_blocked"; input.target_index_status == "public_index_published" }
deny["fixture_cannot_be_public_readable"] if { input.fixture_backed; input.target_record_status == "public_readable" }
deny["artifact_missing_sha256"] if { some a in input.artifacts; not a.sha256 }
deny["nowcast_mislabelled_as_validated_truth"] if { input.measurement_summary.nowcast_is_validated_aqs_truth }
deny["aqs_validated_missing_24h_window"] if { input.source_class == "epa_aqs_validated"; input.measurement_summary.averaging_window != "24h_validated" }
deny["retracted_publication_marked_active"] if { input.retraction_state == "retracted"; input.target_record_status == "public_readable" }
deny["promotion_decision_not_approved_for_catalog"] if { input.promotion_decision.decision != "approved_for_catalog" }
deny["release_manifest_not_public_ready"] if { input.release_manifest.public_readiness.status != "catalog_candidate"; input.release_manifest.public_readiness.status != "published" }
deny["non_public_dereference_required"] if { input.requires_non_public_dereference }
deny["public_api_has_unsafe_path"] if { some r in input.public_refs; unsafe_path(r) }
