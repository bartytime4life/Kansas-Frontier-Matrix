package ecology.publication

# Fail-closed publication policy for ecology bundles.
# Input is expected to be an object with at least:
# - sensitivity
# - rights_status
# - policy_id
# - exact_geometry_present (boolean, optional)
# - evidence_refs (array)

default allow = false

default decision = "deny"

deny_reasons[r] {
  not input.sensitivity
  r := "missing_sensitivity"
}

deny_reasons[r] {
  not input.rights_status
  r := "missing_rights_status"
}

deny_reasons[r] {
  not input.policy_id
  r := "missing_policy_id"
}

deny_reasons[r] {
  count(object.get(input, "evidence_refs", [])) == 0
  r := "missing_evidence_refs"
}

deny_reasons[r] {
  input.sensitivity == "restricted"
  object.get(input, "exact_geometry_present", false)
  r := "restricted_exact_geometry_not_publishable"
}

deny_reasons[r] {
  input.sensitivity == "review_required"
  r := "requires_steward_review"
}

allow {
  count(deny_reasons) == 0
  input.sensitivity == "public"
  input.rights_status == "public" or input.rights_status == "open"
}

allow {
  count(deny_reasons) == 0
  input.sensitivity == "generalize"
  input.rights_status != "unknown"
}

decision := "allow" {
  allow
}

decision := "generalize" {
  not allow
  count(deny_reasons) == 0
  input.sensitivity == "generalize"
}

decision := "hold" {
  not allow
  input.sensitivity == "review_required"
}
