package kfm.catalog.visibility

default public_visible := false

deny[msg] {
  input["policy_label"] != "public"
  msg := "catalog record is not marked public"
}

deny[msg] {
  input["sensitivity"] != "public"
  msg := "catalog record sensitivity must be public"
}

deny[msg] {
  input["review_state"] != "reviewed"
  input["review_state"] != "published"
  msg := "catalog record review_state must be reviewed or published"
}

public_visible {
  count(deny) == 0
}
