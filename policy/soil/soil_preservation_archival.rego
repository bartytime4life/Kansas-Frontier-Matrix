package kfm.soil_preservation_archival

deny[msg] { input.preservation_receipt.decision != "pass"; msg := "receipt_not_pass" }
deny[msg] { input.preservation_receipt.from_state != "FEDERATION_RECONCILED"; msg := "bad_from_state" }
deny[msg] { input.preservation_receipt.to_state != "PRESERVATION_READY"; msg := "bad_to_state" }
