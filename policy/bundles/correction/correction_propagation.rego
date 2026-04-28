package kfm.policy.correction

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["correction_policy_not_configured"],
  "obligations": []
}
