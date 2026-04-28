package kfm.runtime

import data.kfm.runtime.denials
import data.kfm.runtime.proof

# Finite runtime outcomes supported by RuntimeResponseEnvelope.
allowed_outcomes := {"ANSWER", "ABSTAIN", "DENY", "ERROR"}

# Denials are fail-closed and win over other branches.
outcome := "DENY" if {
  denials.deny
}

# Engine or dependency failures are surfaced as runtime errors.
outcome := "ERROR" if {
  not denials.deny
  proof.engine_error
}

# Positive answer path requires a complete proof quartet.
outcome := "ANSWER" if {
  not denials.deny
  not proof.engine_error
  proof.proof_quartet_ok
}

# Default to ABSTAIN when policy cannot safely produce an answer.
default outcome := "ABSTAIN"

# Canonical runtime decision envelope for callers that need reasons/obligations.
decision := {
  "outcome": outcome,
  "reasons": reasons,
  "obligations": obligations,
}

reasons := ["policy_denied"] if outcome == "DENY"
reasons := ["policy_engine_error"] if outcome == "ERROR"
reasons := ["proof_quartet_satisfied"] if outcome == "ANSWER"
reasons := ["insufficient_evidence_or_policy_signal"] if outcome == "ABSTAIN"

obligations := ["surface_runtime_denial_reason"] if outcome == "DENY"
obligations := ["emit_runtime_error_receipt"] if outcome == "ERROR"
obligations := ["attach_citation_and_receipts"] if outcome == "ANSWER"
obligations := ["present_abstain_with_next_action"] if outcome == "ABSTAIN"

valid_outcome {
  allowed_outcomes[outcome]
}
