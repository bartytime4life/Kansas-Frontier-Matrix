package kfm.catalog.rights

default releasable := false

deny[msg] {
  not input["rights"]
  msg := "rights block missing"
}

deny[msg] {
  input["rights"]["redistribution"] != "allowed"
  msg := "redistribution must be allowed for release-linked catalog"
}

deny[msg] {
  input["rights"]["attribution_required"]
  not input["rights"]["attribution_text"]
  msg := "attribution text required when attribution_required=true"
}

releasable {
  count(deny) == 0
}
