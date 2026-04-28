package kfm.policy.sensitivity

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["sensitivity_policy_not_configured"],
  "obligations": []
}
