package soil.public_stability

deny[msg] {
  input.public_delivery_stability_receipt.from_state != "PUBLIC_DELIVERY_CONTINUITY_READY"
  msg := "bad_from_state"
}
