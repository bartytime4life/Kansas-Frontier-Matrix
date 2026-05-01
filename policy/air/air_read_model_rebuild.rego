package kfm.air.read_model_rebuild

default allow = false
allow if { count(deny)==0 }

deny contains "missing_source_index" if { not input.source_index_ref }
deny contains "missing_tombstone" if { count(input.applied_tombstone_refs)==0 }
deny contains "missing_invalidation" if { count(input.applied_invalidation_notice_refs)==0 }
deny contains "missing_steward_decision" if { count(input.steward_decision_refs)==0 }
deny contains "unapproved_steward_decision" if { some d in input.steward_decisions; not d.decision=="approve_retraction"; not d.decision=="approve_remediation_package" }
deny contains "source_index_mutated_in_place" if { input.source_index_ref==input.new_index_ref }
deny contains "fixture_public_delta" if { input.fixture_backed==true; input.delta_status=="public_delta" }
deny contains "fixture_public_readable" if { input.fixture_backed==true; input.index_visibility=="public_readable" }
deny contains "production_status_forbidden" if { input.status=="production_proposed" }
deny contains "unsafe_path_ref" if { some r in input.public_safe_refs; contains(lower(r),"data/raw/") or contains(lower(r),"data/work/") or contains(lower(r),"data/quarantine/") or contains(lower(r),"data/processed/air/") }
deny contains "nowcast_validated_truth_forbidden" if { input.nowcast_label=="validated_aqs_truth" }
