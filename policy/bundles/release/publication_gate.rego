package kfm.policy.release

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["release_policy_not_configured"],
  "obligations": []
}
