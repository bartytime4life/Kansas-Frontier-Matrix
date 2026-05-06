package kfm.policy.review

# Fail-closed starter bundle. Returns DENY unless downstream conditions are added.
default decision := {
  "outcome": "DENY",
  "reasons": ["review_policy_not_configured"],
  "obligations": []
}
