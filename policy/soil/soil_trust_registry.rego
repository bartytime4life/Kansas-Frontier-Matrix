package kfm.soil.trust_registry

deny[msg] { input.registry_receipt.decision != "pass"; msg := "receipt decision not pass" }
deny[msg] { input.registry_receipt.from_state != "TRUST_CERTIFIED"; msg := "bad from_state" }
deny[msg] { input.registry_receipt.to_state != "TRUST_REGISTRY_READY"; msg := "bad to_state" }
deny[msg] { input.certificate_status.certificate_status != "active"; msg := "certificate not active" }
