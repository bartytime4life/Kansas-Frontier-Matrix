package kfm.air.publication

default allow := false
allow if { count(deny) == 0 }

deny[msg] if { input.promotion_decision.decision != "approved_for_catalog"; msg := "promotion_decision_not_approved_for_catalog" }
deny[msg] if { not input.evidence_bundle; msg := "missing_evidence_bundle" }
deny[msg] if { input.evidence_bundle.measurements.nowcast_truth_status != "operational_evidence_not_validated_aqs_truth"; msg := "nowcast_mislabelled_as_validated_truth" }
deny[msg] if { input.release_manifest.public_readiness.status != "catalog_candidate"; input.release_manifest.public_readiness.status != "published"; msg := "release_not_catalog_candidate_or_better" }
deny[msg] if { input.requested_status == "published"; not input.attestation; msg := "missing_attestation" }
deny[msg] if { input.requested_status == "published"; input.attestation.signature_type == "fixture_signature"; msg := "fixture_attestation_forbidden_for_real_publish" }
deny[msg] if { input.requested_status == "published"; not input.aqs_reconciliation; msg := "missing_aqs_reconciliation" }
deny[msg] if { input.requested_status == "published"; input.aqs_reconciliation.status == "pending"; msg := "aqs_reconciliation_pending" }
deny[msg] if { input.requested_status == "published"; input.aqs_reconciliation.status == "conflict_detected"; msg := "aqs_reconciliation_conflict" }
