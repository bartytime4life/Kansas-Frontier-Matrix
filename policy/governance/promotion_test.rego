package governance.promotion

test_allow_valid if {
  allow with input as {"policy_label":"x","release_state":"PUBLISHED","decision_log":{"allow":true},"steward_attestation":{"approved":true},"signing":{"local_stub_signature":true},"gatehouse_registration":{"receipt_id":"r","registered_at":"2026-01-01T00:00:00Z"},"publish_manifest":{"published_at":"2026-01-01T00:01:00Z"},"artifact":{"public_path":"data/published/x.json"},"obligations":["rollback_ref:r1"]}
}

test_deny_forbidden_path if {
  deny[_] with input as {"artifact":{"public_path":"data/published/RAW/x"},"decision_log":{"allow":true},"obligations":["x"]}
}
