package kfm.policy.rights

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["rights_policy_not_configured"],
  "obligations": []
}
