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
  not input.gate == "B"
  msg := sprintf("Gate B invoked with wrong gate input: expected B, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate B missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate B artifact parse error in %s: %s", [path, err])
}

# Gate B: Run provenance and evidence signature bundle.

has_bundle_signature(bundle) if {
  has_key(bundle, "messageSignature")
}

has_bundle_signature(bundle) if {
  has_key(bundle, "dsseEnvelope")
}

has_bundle_signature(bundle) if {
  has_key(bundle, "signature")
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  rr.status != "success"
  msg := "run_receipt.status must be success"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.run_id)
  msg := "run_receipt.run_id must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.source_repo)
  msg := "run_receipt.source_repo must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.source_sha)
  msg := "run_receipt.source_sha must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.workflow)
  msg := "run_receipt.workflow must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.actor)
  msg := "run_receipt.actor must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.started_at)
  msg := "run_receipt.started_at must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not nonempty_string(rr.completed_at)
  msg := "run_receipt.completed_at must be a non-empty string"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  not valid_sha256(rr.spec_hash)
  msg := "run_receipt.spec_hash must be a 64-character sha256 hex digest"
}

deny contains msg if {
  rr := file_json("artifacts/run_receipt.json")
  spec_hash := file_text_stripped("artifacts/spec_hash.txt")
  rr.spec_hash != spec_hash
  msg := "run_receipt.spec_hash must match artifacts/spec_hash.txt"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  rr := file_json("artifacts/run_receipt.json")
  eb.spec_hash != rr.spec_hash
  msg := "run_receipt.spec_hash must match EvidenceBundle.spec_hash"
}

deny contains msg if {
  bundle := file_json("artifacts/signatures/evidence.sigstore.json")
  not nonempty_string(bundle.mediaType)
  msg := "evidence.sigstore.json must include mediaType"
}

deny contains msg if {
  bundle := file_json("artifacts/signatures/evidence.sigstore.json")
  not has_bundle_signature(bundle)
  msg := "evidence.sigstore.json must include messageSignature, dsseEnvelope, or signature"
}

deny contains msg if {
  bundle := file_json("artifacts/signatures/evidence.sigstore.json")
  not has_key(bundle, "verificationMaterial")
  msg := "evidence.sigstore.json must include verificationMaterial"
}
