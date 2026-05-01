package kfm.air.reentry_publication_boundary

default allow = false

unsafe_ref(r) { contains(lower(r), "data/raw/") }
unsafe_ref(r) { contains(lower(r), "data/work/") }
unsafe_ref(r) { contains(lower(r), "data/quarantine/") }
unsafe_ref(r) { contains(lower(r), "data/processed/air/") }
unsafe_ref(r) { contains(lower(r), "data/published/air/") }

deny[msg] { not input.reentry_release_candidate_postcheck_report; msg := "missing postcheck" }
deny[msg] { input.reentry_release_candidate_postcheck_report.result == "deny"; msg := "postcheck denied" }
deny[msg] { input.reentry_release_candidate_audit_report.result == "deny"; msg := "audit denied" }
deny[msg] { input.reentry_gate_d_attestation.signature_type == "fixture_signature"; input.reentry_publication_eligibility_decision.decision == "approved_for_publication_candidate"; msg := "fixture signature cannot authorize production" }
deny[msg] { some r in input.public_safe_refs; unsafe_ref(r); msg := "unsafe reference" }
allow { count(deny) == 0 }
