package soil.public_service

deny[msg] { not input.audit_passed; msg := "audit_failed" }
deny[msg] { input.retracted; msg := "retracted" }
deny[msg] { not input.current_release_id; msg := "no_active_release" }
deny[msg] { input.publication_receipt_missing; msg := "missing_publication_receipt" }
deny[msg] { input.publication_receipt_decision != "pass"; msg := "receipt_not_pass" }
deny[msg] { not input.signatures_present; msg := "missing_signatures" }
deny[msg] { not input.evidence_bundle_ref; msg := "missing_evidence_ref" }
deny[msg] { input.rights_status == "unknown"; msg := "unknown_rights" }
deny[msg] { not input.policy_label; msg := "missing_policy_label" }
deny[msg] { input.sensitivity == "private" or input.sensitivity == "restricted"; msg := "sensitivity_block" }
deny[msg] { input.focus_card_provisional; msg := "provisional_focus_card" }
deny[msg] { lower(input.response_text) contains "raw" or lower(input.response_text) contains "work" or lower(input.response_text) contains "quarantine" or lower(input.response_text) contains "processed"; msg := "forbidden_lifecycle_path" }
deny[msg] { lower(input.response_text) contains "token" or lower(input.response_text) contains "secret" or lower(input.response_text) contains "password"; msg := "secret_exposed" }
deny[msg] { input.state != "PUBLISHED"; msg := "wrong_state" }
deny[msg] { input.arbitrary_path_read; msg := "arbitrary_path_read" }
