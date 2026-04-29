package ecology.publication

# Fail-closed publication policy for ecology bundles.
#
# This policy evaluates whether an ecology object may be exposed on a public surface.
# It enforces KFM governance invariants:
# - Evidence must resolve to an EvidenceBundle
# - Sensitive geometry must not leak
# - Derived layers must remain labeled as derived
# - Rights must be known and acceptable
# - Publication state must be safe for release
#
# NOTE:
# This policy does NOT promote objects — it only allows, generalizes, holds, or denies.

default allow := false
default decision := "deny"

# -------------------------------------------------------------------
# DENY CONDITIONS (fail-closed)
# -------------------------------------------------------------------

deny_reasons contains r if {
  not input.object_type
  r := "missing_object_type"
}

deny_reasons contains r if {
  not input.sensitivity
  r := "missing_sensitivity"
}

deny_reasons contains r if {
  not input.rights_status
  r := "missing_rights_status"
}

deny_reasons contains r if {
  not input.policy_id
  r := "missing_policy_id"
}

deny_reasons contains r if {
  not input.policy_label
  r := "missing_policy_label"
}

deny_reasons contains r if {
  not input.spec_hash
  r := "missing_spec_hash"
}

deny_reasons contains r if {
  input.spec_hash != ""
  not regex.match("^sha256:[a-fA-F0-9]{64}$", input.spec_hash)
  r := "invalid_spec_hash"
}

deny_reasons contains r if {
  count(object.get(input, "evidence_refs", [])) == 0
  r := "missing_evidence_refs"
}

deny_reasons contains r if {
  object.get(input, "evidence_bundle_resolved", false) == false
  r := "unresolved_evidence_bundle"
}

deny_reasons contains r if {
  input.rights_status == "unknown"
  r := "unknown_rights"
}

deny_reasons contains r if {
  input.policy_label == "internal"
  r := "internal_policy_label_not_publishable"
}

# -------------------------------------------------------------------
# PUBLIC SURFACE SAFETY
# -------------------------------------------------------------------

deny_reasons contains r if {
  object.get(input, "surface", "public") == "public"
  input.publication_state == "candidate"
  r := "candidate_not_publishable"
}

deny_reasons contains r if {
  object.get(input, "surface", "public") == "public"
  input.publication_state == "held"
  r := "held_not_publishable"
}

deny_reasons contains r if {
  object.get(input, "surface", "public") == "public"
  input.publication_state == "quarantined"
  r := "quarantined_not_publishable"
}

# -------------------------------------------------------------------
# DERIVED LAYER RULES
# -------------------------------------------------------------------

deny_reasons contains r if {
  input.source_role == "DERIVED_MODEL_LAYER"
  object.get(input, "claim_status", "") == "CONFIRMED"
  r := "derived_layer_as_confirmed_truth"
}

deny_reasons contains r if {
  input.source_role == "DERIVED_MODEL_LAYER"
  object.get(input, "catalog_closure", false) == false
  r := "derived_layer_missing_catalog_closure"
}

# -------------------------------------------------------------------
# SENSITIVE OCCURRENCE RULES
# -------------------------------------------------------------------

deny_reasons contains r if {
  input.source_role == "SENSITIVE_OCCURRENCE"
  object.get(input, "exact_geometry_present", false)
  r := "sensitive_exact_geometry_not_publishable"
}

deny_reasons contains r if {
  input.sensitivity == "restricted"
  object.get(input, "exact_geometry_present", false)
  r := "restricted_exact_geometry_not_publishable"
}

deny_reasons contains r if {
  object.get(input, "public_geometry_policy", "") == "deny_exact_generalize_required"
  object.get(input, "exact_geometry_present", false)
  r := "exact_geometry_requires_generalization"
}

deny_reasons contains r if {
  object.get(input, "public_visibility", "") == "internal_only"
  r := "internal_only_not_publishable"
}

deny_reasons contains r if {
  object.get(input, "public_visibility", "") == "generalized"
  not input.redaction_receipt_ref
  r := "missing_redaction_receipt"
}

# -------------------------------------------------------------------
# HOLD CONDITIONS
# -------------------------------------------------------------------

hold_reasons contains r if {
  input.sensitivity == "review_required"
  r := "requires_steward_review"
}

# -------------------------------------------------------------------
# GENERALIZATION PATH
# -------------------------------------------------------------------

generalize_reasons contains r if {
  input.sensitivity == "generalize"
  input.rights_status != "unknown"
  object.get(input, "exact_geometry_present", false) == false
  r := "generalization_required"
}

generalize_reasons contains r if {
  object.get(input, "public_visibility", "") == "generalized"
  object.get(input, "exact_geometry_present", false) == false
  input.redaction_receipt_ref
  r := "public_visibility_generalized_with_receipt"
}

# -------------------------------------------------------------------
# ALLOW CONDITIONS
# -------------------------------------------------------------------

allow if {
  count(deny_reasons) == 0
  count(hold_reasons) == 0
  count(generalize_reasons) == 0
  input.sensitivity == "public"
  input.rights_status in {"public", "open"}
  object.get(input, "evidence_bundle_resolved", false) == true
}

allow if {
  count(deny_reasons) == 0
  count(hold_reasons) == 0
  input.source_role == "DERIVED_MODEL_LAYER"
  input.policy_label == "public_after_catalog_closure"
  object.get(input, "catalog_closure", false) == true
  object.get(input, "evidence_bundle_resolved", false) == true
}

# -------------------------------------------------------------------
# DECISION OUTPUT
#
# Precedence:
# 1. deny
# 2. hold
# 3. generalize
# 4. allow
# -------------------------------------------------------------------

decision := "deny" if {
  count(deny_reasons) > 0
}

decision := "hold" if {
  count(deny_reasons) == 0
  count(hold_reasons) > 0
}

decision := "generalize" if {
  count(deny_reasons) == 0
  count(hold_reasons) == 0
  count(generalize_reasons) > 0
}

decision := "allow" if {
  allow
}
