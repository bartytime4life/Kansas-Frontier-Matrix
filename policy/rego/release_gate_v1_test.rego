package kfm.pass12.release_gate_v1_test

import data.kfm.pass12.release_gate_v1

valid_input := {
	"release_scope": "public",
	"spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
	"evidence_refs": ["evidence:hydrology:huc12:102600010101"],
	"sensitivity": {"reviewed": true, "class": "PUBLIC"},
	"attestation": {"required": true, "verified": true, "ref": "attestation:sha256:bbbb"},
	"review": {"state": "REVIEWED", "review_ref": "review:pass12:001"},
	"release_manifest_ref": "release:manifest:pass12:001",
	"correction_ref": "correction:path:pass12:001",
	"rollback_ref": "rollback:path:pass12:001",
}

test_valid_candidate_allows if {
	release_gate_v1.allow with input as valid_input
	count(release_gate_v1.deny) == 0 with input as valid_input
}

test_missing_evidence_denies if {
	candidate := object.union(valid_input, {"evidence_refs": []})
	not release_gate_v1.allow with input as candidate
	"MISSING_EVIDENCE" in release_gate_v1.deny with input as candidate
}

test_missing_sensitivity_denies if {
	candidate := object.union(valid_input, {"sensitivity": {"reviewed": false, "class": "PUBLIC"}})
	not release_gate_v1.allow with input as candidate
	"MISSING_SENSITIVITY_REVIEW" in release_gate_v1.deny with input as candidate
}

test_restricted_public_candidate_denies if {
	candidate := object.union(valid_input, {"sensitivity": {"reviewed": true, "class": "RESTRICTED"}})
	not release_gate_v1.allow with input as candidate
	"PUBLIC_SENSITIVITY_UNSAFE" in release_gate_v1.deny with input as candidate
}

test_missing_required_attestation_denies if {
	candidate := object.union(valid_input, {"attestation": {"required": true, "verified": false, "ref": ""}})
	not release_gate_v1.allow with input as candidate
	"MISSING_REQUIRED_ATTESTATION" in release_gate_v1.deny with input as candidate
}

test_unreviewed_candidate_denies if {
	candidate := object.union(valid_input, {"review": {"state": "PENDING", "review_ref": ""}})
	not release_gate_v1.allow with input as candidate
	"MISSING_HUMAN_REVIEW" in release_gate_v1.deny with input as candidate
}
