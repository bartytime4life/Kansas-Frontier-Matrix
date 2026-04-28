package kfm.runtime.proof

# Proof quartet requires these four runtime trust artifacts.
default proof_quartet_ok := false

default engine_error := false

proof_quartet_ok if {
  input.runtime.proof.ai_receipt
  input.runtime.proof.run_receipt
  input.runtime.proof.attestation
  input.runtime.proof.citation
}

engine_error if {
  input.runtime.engine_unavailable == true
}

engine_error if {
  input.runtime.policy_evaluation_failed == true
}
