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
  not input.gate == "D"
  msg := sprintf("Gate D invoked with wrong gate input: expected D, got %v", [input.gate])
}

deny contains msg if {
  some path in input.required
  not file_exists(path)
  msg := sprintf("Gate D missing required artifact: %s", [path])
}

deny contains msg if {
  some path in input.required
  err := parse_error(path)
  msg := sprintf("Gate D artifact parse error in %s: %s", [path, err])
}

# Gate D: Obligations and redaction receipts.

bool_value(x) if { is_boolean(x) }

redaction_required_from_evidence if {
  eb := file_json("artifacts/EvidenceBundle.json")
  eb.obligations.redaction_required == true
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  not bool_value(receipt.redaction_required)
  msg := "redaction_receipt.redaction_required must be a boolean"
}

deny contains msg if {
  redaction_required_from_evidence
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required != true
  msg := "EvidenceBundle requires redaction but redaction_receipt.redaction_required is not true"
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required == true
  receipt.completed != true
  msg := "redaction_receipt.completed must be true when redaction_required is true"
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required == true
  not nonempty_array(receipt.actions)
  msg := "redaction_receipt.actions must be non-empty when redaction_required is true"
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required == true
  not valid_sha256(receipt.post_process_spec_hash)
  msg := "redaction_receipt.post_process_spec_hash must be a sha256 hex digest when redaction_required is true"
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required == true
  eb := file_json("artifacts/EvidenceBundle.json")
  receipt.post_process_spec_hash != eb.spec_hash
  msg := "redaction_receipt.post_process_spec_hash must match final EvidenceBundle.spec_hash"
}

deny contains msg if {
  receipt := file_json("artifacts/redaction_receipt.json")
  receipt.redaction_required == false
  not nonempty_string(receipt.reason)
  msg := "redaction_receipt.reason must explain why redaction is not required"
}
