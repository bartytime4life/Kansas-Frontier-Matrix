package kfm.runtime.proof_quartet

import rego.v1

default allow := false

requires_proof_quartet if {
  input.kind == "ReleaseManifest"
}

requires_proof_quartet if {
  input.kind == "RuntimeResponseEnvelope"
}

has_model_mediation if {
  input.model_mediated == true
}

deny contains "missing spec_hash" if {
  requires_proof_quartet
  not input.spec_hash
}

deny contains "missing run_receipt reference" if {
  requires_proof_quartet
  not input.run_receipt_ref
}

deny contains "missing ai_receipt reference for model-mediated flow" if {
  has_model_mediation
  not input.ai_receipt_ref
}

deny contains "missing attestation_refs" if {
  requires_proof_quartet
  count(input.attestation_refs) == 0
}

deny contains "missing attestation_refs" if {
  requires_proof_quartet
  not input.attestation_refs
}

allow if {
  count(deny) == 0
}
