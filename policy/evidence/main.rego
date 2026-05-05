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
  not input.gate == "A"
  msg := sprintf("Gate A invoked with wrong gate input: expected A, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate A missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate A artifact parse error in %s: %s", [path, err])
}

# Gate A: Evidence integrity.

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.bundle_id)
  msg := "EvidenceBundle.bundle_id must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.version)
  msg := "EvidenceBundle.version must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.created_at)
  msg := "EvidenceBundle.created_at must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.producer)
  msg := "EvidenceBundle.producer must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_object(eb.subject)
  msg := "EvidenceBundle.subject must be a non-empty object"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.subject.id)
  msg := "EvidenceBundle.subject.id must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_array(eb.artifacts)
  msg := "EvidenceBundle.artifacts must be a non-empty array"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not valid_sha256(eb.spec_hash)
  msg := "EvidenceBundle.spec_hash must be a 64-character sha256 hex digest"
}

deny contains msg if {
  spec_hash := file_text_stripped("artifacts/spec_hash.txt")
  not valid_sha256(spec_hash)
  msg := "artifacts/spec_hash.txt must contain a 64-character sha256 hex digest"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  spec_hash := file_text_stripped("artifacts/spec_hash.txt")
  eb.spec_hash != spec_hash
  msg := "EvidenceBundle.spec_hash must exactly match artifacts/spec_hash.txt"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  some i
  artifact := eb.artifacts[i]
  not nonempty_string(artifact.path)
  msg := sprintf("EvidenceBundle.artifacts[%v].path must be a non-empty string", [i])
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  some i
  artifact := eb.artifacts[i]
  not valid_sha256(artifact.sha256)
  msg := sprintf("EvidenceBundle.artifacts[%v].sha256 must be a 64-character sha256 hex digest", [i])
}
