package ecology.publication

# Fail-closed publication policy for ecology bundles.
#
# Input is expected to be an object with governance fields used by the
# ecology schemas and source registry, including:
# - object_type
# - source_role
# - sensitivity
# - sensitivity_class
# - rights_status
# - policy_id
# - policy_label
# - public_visibility
# - public_geometry_policy
# - exact_geometry_present
# - evidence_refs
# - evidence_bundle_resolved
# - catalog_closure
# - claim_status
#
# This policy decides whether an ecology object may be published to a
# public surface. It does not promote data by itself.

default allow := false

default decision := "deny"

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
  input.source_role == "DERIVED_MODEL_LAYER"
  object.get(input, "claim_status", "") == "CONFIRMED"
  r := "derived_layer_as_confirmed_truth"
}

deny_reasons contains r if {
  input.source_role == "DERIVED_MODEL_LAYER"
  object.get(input, "catalog_closure", false) == false
  r := "derived_layer_missing_catalog_closure"
}

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
  input.sensitivity == "review_required"
  r := "requires_steward_review"
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
  input.policy_label == "internal"
  r := "internal_policy_label_not_publishable"
}

generalize_reasons contains r if {
  input.sensitivity == "generalize"
  input.rights_status != "unknown"
  r := "generalization_required"
}

generalize_reasons contains r if {
  object.get(input, "public_visibility", "") == "generalized"
  object.get(input, "exact_geometry_present", false)
  r := "public_visibility_requires_generalization"
}

allow if {
  count(deny_reasons) == 0
  input.sensitivity == "public"
  input.rights_status in {"public", "open"}
  object.get(input, "evidence_bundle_resolved", false) == true
}

allow if {
  count(deny_reasons) == 0
  input.source_role == "DERIVED_MODEL_LAYER"
  input.policy_label == "public_after_catalog_closure"
  object.get(input, "catalog_closure", false) == true
  object.get(input, "evidence_bundle_resolved", false) == true
}

decision := "allow" if {
  allow
}

decision := "generalize" if {
  not allow
  count(deny_reasons) == 0
  count(generalize_reasons) > 0
}

decision := "hold" if {
  not allow
  input.sensitivity == "review_required"
}

decision := "deny" if {
  not allow
  count(deny_reasons) > 0
}
