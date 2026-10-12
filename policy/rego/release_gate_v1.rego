package kfm.pass12.release_gate_v1

# PROPOSED_INACTIVE policy profile. It evaluates a declared release candidate only;
# it does not resolve evidence, verify signatures, authenticate review, promote,
# release, deploy, or publish.

default allow := false

valid_release_scope if {
	input.release_scope in {"public", "semi_public"}
}

valid_spec_hash if {
	regex.match("^sha256:[0-9a-f]{64}$", input.spec_hash)
}

has_evidence if {
	count(input.evidence_refs) > 0
	every ref in input.evidence_refs {
		is_string(ref)
		ref != ""
	}
}

sensitivity_complete if {
	input.sensitivity.reviewed == true
	input.sensitivity.class in {"PUBLIC", "GENERALIZED", "RESTRICTED"}
}

public_sensitivity_safe if {
	input.release_scope != "public"
}

public_sensitivity_safe if {
	input.release_scope == "public"
	input.sensitivity.class in {"PUBLIC", "GENERALIZED"}
}

attestation_complete if {
	input.attestation.required == false
}

attestation_complete if {
	input.attestation.required == true
	input.attestation.verified == true
	is_string(input.attestation.ref)
	input.attestation.ref != ""
}

review_complete if {
	input.review.state == "REVIEWED"
	is_string(input.review.review_ref)
	input.review.review_ref != ""
}

release_manifest_bound if {
	is_string(input.release_manifest_ref)
	input.release_manifest_ref != ""
}

correction_path_bound if {
	is_string(input.correction_ref)
	input.correction_ref != ""
}

rollback_path_bound if {
	is_string(input.rollback_ref)
	input.rollback_ref != ""
}

deny contains "INVALID_RELEASE_SCOPE" if {
	not valid_release_scope
}

deny contains "INVALID_SPEC_HASH" if {
	not valid_spec_hash
}

deny contains "MISSING_EVIDENCE" if {
	not has_evidence
}

deny contains "MISSING_SENSITIVITY_REVIEW" if {
	not sensitivity_complete
}

deny contains "PUBLIC_SENSITIVITY_UNSAFE" if {
	not public_sensitivity_safe
}

deny contains "MISSING_REQUIRED_ATTESTATION" if {
	not attestation_complete
}

deny contains "MISSING_HUMAN_REVIEW" if {
	not review_complete
}

deny contains "MISSING_RELEASE_MANIFEST" if {
	not release_manifest_bound
}

deny contains "MISSING_CORRECTION_PATH" if {
	not correction_path_bound
}

deny contains "MISSING_ROLLBACK_PATH" if {
	not rollback_path_bound
}

allow if {
	count(deny) == 0
}

decision := {
	"allow": allow,
	"deny_reasons": sort([reason | reason := deny[_]]),
	"profile": "kfm.pass12.release-gate.v1",
}
