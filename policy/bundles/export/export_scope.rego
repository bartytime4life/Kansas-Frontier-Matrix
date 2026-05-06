package kfm.policy.export

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["export_policy_not_configured"],
  "obligations": []
}
