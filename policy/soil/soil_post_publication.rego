package soil.post_publication

deny[msg] { input.audit_passed == false; msg := "audit_failed" }
deny[msg] { input.release.state != "PUBLISHED"; msg := "release_not_published" }
deny[msg] { input.publication_receipt.decision != "pass"; msg := "publication_decision_not_pass" }
deny[msg] { input.artifact_hash_check_passed == false; msg := "artifact_hash_failed" }
deny[msg] { some i; not input.records[i].evidence_bundle_ref; msg := "missing_evidence_ref" }
deny[msg] { not input.publication_receipt; msg := "missing_publication_receipt" }
deny[msg] { not input.publication_receipt.signatures; msg := "missing_signatures" }
deny[msg] { some i; input.records[i].rights_status == "unknown"; msg := "rights_unknown" }
deny[msg] { some i; not input.records[i].policy_label; msg := "policy_label_missing" }
deny[msg] { some i; v := input.records[i].sensitivity; v == "private" or v == "restricted"; msg := "sensitivity_blocked" }
deny[msg] { some i; input.focus_cards[i].provisional == true; msg := "provisional_focus_card" }
deny[msg] { contains(lower(json.marshal(input.public_index)), "raw") or contains(lower(json.marshal(input.public_index)), "work") or contains(lower(json.marshal(input.public_index)), "quarantine") or contains(lower(json.marshal(input.public_index)), "processed"); msg := "lifecycle_path_exposed" }
deny[msg] { input.current_release_id == input.retracted_release_id; msg := "retracted_release_active" }
deny[msg] { input.retraction.steward_review.decision != "approved"; msg := "retraction_not_approved" }
deny[msg] { input.retraction.immutable_release_preserved != true; msg := "immutable_release_modified" }
