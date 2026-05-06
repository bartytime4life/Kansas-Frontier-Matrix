package soil.delivery_recommissioning

deny[msg] {
  input.delivery_recommissioning_receipt.from_state != "PUBLIC_DELIVERY_RESILIENCE_READY"
  msg := "bad_from_state"
}

deny[msg] {
  not input.delivery_recommissioning_receipt.signatures
  msg := "missing_signatures"
}
