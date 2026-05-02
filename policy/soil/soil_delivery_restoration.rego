package kfm.soil.delivery_restoration

default deny := []

deny contains "bad_state_transition" if {
  input.receipt.from_state != "PUBLIC_DELIVERY_RECOMMISSIONING_READY"
}
