package soil.external_federation

deny[msg] { input.federation_receipt.decision != "pass"; msg := "federation decision not pass" }
deny[msg] { input.federation_receipt.from_state != "DISCOVERABLE"; msg := "from_state invalid" }
deny[msg] { input.federation_receipt.to_state != "FEDERATION_READY"; msg := "to_state invalid" }
deny[msg] { input.discovery_receipt.decision != "pass"; msg := "discovery decision not pass" }
deny[msg] { input.discovery_status != "DISCOVERABLE"; msg := "discovery status invalid" }
deny[msg] { input.release_status != "PUBLISHED"; msg := "release not published" }
deny[msg] { input.release_retracted == true; msg := "release retracted" }
deny[msg] { input.operational_status.public_access_allowed != true; msg := "public access blocked" }
deny[msg] { input.operational_status.latest_probe_decision != "pass"; msg := "probe failed" }
