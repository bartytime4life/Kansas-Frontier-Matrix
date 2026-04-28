package kfm.policy.admission

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["admission_policy_not_configured"],
  "obligations": []
}
