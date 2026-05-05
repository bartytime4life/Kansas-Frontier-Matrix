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
  not input.gate == "C"
  msg := sprintf("Gate C invoked with wrong gate input: expected C, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate C missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate C artifact parse error in %s: %s", [path, err])
}

# Gate C: Rights, license, and sensitivity classification.

valid_sensitivity(level) if { level == "public" }
valid_sensitivity(level) if { level == "internal" }
valid_sensitivity(level) if { level == "confidential" }
valid_sensitivity(level) if { level == "restricted" }

restricted_or_confidential(level) if { level == "restricted" }
restricted_or_confidential(level) if { level == "confidential" }

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_object(eb.rights)
  msg := "EvidenceBundle.rights must be a non-empty object"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_string(eb.rights.license_id)
  msg := "EvidenceBundle.rights.license_id must be a non-empty string"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not nonempty_array(eb.rights.allowed_uses)
  msg := "EvidenceBundle.rights.allowed_uses must be a non-empty array"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not has_key(eb.rights, "prohibited_uses")
  msg := "EvidenceBundle.rights.prohibited_uses must be present, even when empty"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  not valid_sensitivity(eb.rights.sensitivity_level)
  msg := "EvidenceBundle.rights.sensitivity_level must be one of public, internal, confidential, restricted"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  restricted_or_confidential(eb.rights.sensitivity_level)
  not nonempty_object(eb.steward)
  msg := "confidential or restricted EvidenceBundle must include steward metadata"
}

deny contains msg if {
  eb := file_json("artifacts/EvidenceBundle.json")
  restricted_or_confidential(eb.rights.sensitivity_level)
  not nonempty_string(eb.steward.owner)
  msg := "confidential or restricted EvidenceBundle must include steward.owner"
}

deny contains msg if {
  f := file("LICENSE")
  f.exists == true
  f.kind == "file"
  f.size_bytes == 0
  msg := "LICENSE exists but is empty"
}
