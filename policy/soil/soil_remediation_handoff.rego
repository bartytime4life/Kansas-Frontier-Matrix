package soil.remediation_handoff

deny[msg] { input.remediation_handoff_receipt.decision == "fail"; msg := "bad decision" }
