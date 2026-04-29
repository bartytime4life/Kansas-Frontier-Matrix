package kfm.catalog.correction

default correction_ready := false

deny[msg] {
  input["status"] == "superseded"
  not input["replacement_ref"]
  msg := "superseded catalog record must include replacement_ref"
}

deny[msg] {
  input["status"] == "withdrawn"
  not input["withdrawal_reason"]
  msg := "withdrawn catalog record must include withdrawal_reason"
}

deny[msg] {
  input["status"] == "rollback"
  not input["rollback_target_ref"]
  msg := "rollback catalog record must include rollback_target_ref"
}

correction_ready {
  count(deny) == 0
}
