package soil.discovery_federation

default deny := []

deny contains "decision_not_pass" if { input.discovery_receipt.decision != "pass" }
deny contains "invalid_transition" if { input.discovery_receipt.from_state != "PUBLISHED"; input.discovery_receipt.to_state != "DISCOVERABLE" }
deny contains "release_not_published" if { input.release.state != "PUBLISHED" }
deny contains "retracted" if { input.retracted == true }
deny contains "public_access_blocked" if { input.operational_status.public_access_allowed != true }
