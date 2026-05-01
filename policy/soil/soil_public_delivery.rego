package soil.public_delivery

deny[msg] {
  input.public_delivery_receipt.decision != "pass"
  input.public_delivery_receipt.decision != "degraded"
  input.public_delivery_receipt.decision != "governance_only"
  msg := "invalid receipt decision"
}

deny[msg] {
  input.public_delivery_receipt.from_state != "PUBLIC_ROUTING_RECONCILED"
  msg := "invalid from_state"
}

deny[msg] {
  input.public_delivery_receipt.to_state != "PUBLIC_DELIVERY_VERIFIED"
  msg := "invalid to_state"
}
