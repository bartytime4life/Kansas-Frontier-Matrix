package soil.continuous_assurance

deny[msg] { input.assurance_receipt.decision != "pass"; input.assurance_receipt.decision != "degraded"; msg := "decision_invalid" }
deny[msg] { input.assurance_receipt.from_state != "TRUST_REGISTRY_READY"; msg := "from_state_invalid" }
deny[msg] { input.assurance_receipt.to_state != "CONTINUOUS_ASSURANCE_READY"; msg := "to_state_invalid" }
