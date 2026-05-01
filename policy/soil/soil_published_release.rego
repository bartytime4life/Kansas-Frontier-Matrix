package kfm.soil.published_release

deny[msg] { input.decision != "pass"; msg := "decision_not_pass" }
deny[msg] { input.from_state != "CATALOG/TRIPLET"; msg := "invalid_from_state" }
deny[msg] { input.to_state != "PUBLISHED"; msg := "invalid_to_state" }
deny[msg] { not input.evidence_bundle_ref; msg := "missing_evidence_bundle_ref" }
deny[msg] { not input.promotion_receipt_ref; msg := "missing_promotion_receipt" }
deny[msg] { not input.publication_receipt_ref; msg := "missing_publication_receipt" }
deny[msg] { not input.stac_ref; msg := "missing_stac" }
deny[msg] { not input.dcat_ref; msg := "missing_dcat" }
deny[msg] { not input.prov_ref; msg := "missing_prov" }
deny[msg] { not input.triplet_ref; msg := "missing_triplet" }
deny[msg] { input.hash_integrity_checked != true; msg := "hash_check_failed" }
deny[msg] { input.rights_status == "unknown"; msg := "unknown_rights" }
deny[msg] { not input.policy_label; msg := "missing_policy_label" }
deny[msg] { input.sensitivity == "private"; msg := "private_sensitivity" }
deny[msg] { input.sensitivity == "restricted"; msg := "restricted_sensitivity" }
deny[msg] { input.publication_status != "PUBLISHED"; msg := "invalid_publication_status" }
deny[msg] { input.focus_mode_provisional == true; msg := "focus_mode_provisional" }
