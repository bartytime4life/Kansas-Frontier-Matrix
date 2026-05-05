package main

import rego.v1

file(path) := f if {
  f := input.files[path]
}

file_exists(path) if {
  f := file(path)
  f.exists == true
}

directory_nonempty(path) if {
  f := file(path)
  f.exists == true
  f.kind == "directory"
  f.child_count > 0
}

has_parse_error(path) if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  nonempty_string(f.parse_error)
}

parse_error(path) := msg if {
  f := file(path)
  msg := f.parse_error
  nonempty_string(msg)
}

file_json(path) := doc if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  not has_parse_error(path)
  doc := f.json
}

file_text_stripped(path) := txt if {
  f := file(path)
  f.exists == true
  f.kind == "file"
  txt := f.text_stripped
}

nonempty_string(x) if {
  is_string(x)
  count(x) > 0
}

nonempty_array(xs) if {
  is_array(xs)
  count(xs) > 0
}

nonempty_object(obj) if {
  is_object(obj)
  count(obj) > 0
}

valid_sha256(x) if {
  is_string(x)
  regex.match("^[a-fA-F0-9]{64}$", x)
}

has_key(obj, key) if {
  _ := obj[key]
}

deny contains msg if {
  not input.gate == "G"
  msg := sprintf("Gate G invoked with wrong gate input: expected G, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate G missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate G artifact parse error in %s: %s", [path, err])
}

# Gate G: Final release publication and archival.

valid_target_env(env) if { env == "staging" }
valid_target_env(env) if { env == "prod" }

release_approved(manifest) if {
  manifest.publish_approved == true
}

release_approved(manifest) if {
  manifest.approvals.release_approved == true
}

deny contains msg if {
  not directory_nonempty("artifacts/attestations/")
  msg := "artifacts/attestations/ must exist and contain at least one attestation file"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not nonempty_string(manifest.release_id)
  msg := "release_manifest.release_id must be a non-empty string"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not nonempty_string(manifest.version)
  msg := "release_manifest.version must be a non-empty string"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not valid_target_env(manifest.target_env)
  msg := "release_manifest.target_env must be staging or prod"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not valid_sha256(manifest.spec_hash)
  msg := "release_manifest.spec_hash must be a sha256 hex digest"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  spec_hash := file_text_stripped("artifacts/spec_hash.txt")
  manifest.spec_hash != spec_hash
  msg := "release_manifest.spec_hash must match artifacts/spec_hash.txt"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  eb := file_json("artifacts/EvidenceBundle.json")
  manifest.spec_hash != eb.spec_hash
  msg := "release_manifest.spec_hash must match EvidenceBundle.spec_hash"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not nonempty_array(manifest.artifacts)
  msg := "release_manifest.artifacts must be a non-empty array"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  some i
  artifact := manifest.artifacts[i]
  not nonempty_string(artifact.path)
  msg := sprintf("release_manifest.artifacts[%v].path must be a non-empty string", [i])
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  some i
  artifact := manifest.artifacts[i]
  not valid_sha256(artifact.sha256)
  msg := sprintf("release_manifest.artifacts[%v].sha256 must be a sha256 hex digest", [i])
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not nonempty_string(manifest.evidence_bundle_ref)
  msg := "release_manifest.evidence_bundle_ref must be a non-empty string"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not nonempty_string(manifest.decision_log_ref)
  msg := "release_manifest.decision_log_ref must be a non-empty string"
}

deny contains msg if {
  manifest := file_json("artifacts/release_manifest.json")
  not release_approved(manifest)
  msg := "release_manifest must include publish_approved=true or approvals.release_approved=true"
}

deny contains msg if {
  bundle := file_json("artifacts/signatures/release_manifest.sigstore.json")
  not nonempty_string(bundle.mediaType)
  msg := "release_manifest.sigstore.json must include mediaType"
}

deny contains msg if {
  bundle := file_json("artifacts/signatures/release_manifest.sigstore.json")
  not has_key(bundle, "verificationMaterial")
  msg := "release_manifest.sigstore.json must include verificationMaterial"
}
