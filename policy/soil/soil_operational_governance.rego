package kfm.soil.operational

default deny = []

deny[msg] { input.probe.decision != "pass"; msg := "probe_not_pass" }
deny[msg] { not input.status_receipt; msg := "missing_status_receipt" }
deny[msg] { not input.status_receipt.signatures; msg := "missing_status_receipt_signatures" }
deny[msg] { input.status.service_state == "unavailable"; msg := "service_unavailable" }
deny[msg] { input.status.public_access_allowed == false; msg := "public_access_blocked" }
deny[msg] { input.status.retracted == true; msg := "release_retracted" }
deny[msg] { some i; inc:=input.status.active_incidents[i]; inc.severity=="critical"; inc.status!="resolved"; msg := "critical_incident_unresolved" }
