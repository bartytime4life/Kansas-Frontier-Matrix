package soil.delivery_recommissioning

default allow = false

valid_decisions := {"pass","degraded","governance_only","requires_reprobe","requires_routing_rebuild","blocked"}

deny[msg] { input.delivery_recommissioning_receipt.decision == d; not valid_decisions[d]; msg := "invalid decision" }
deny[msg] { input.delivery_recommissioning_receipt.from_state != "PUBLIC_DELIVERY_RESILIENCE_READY"; msg := "bad from_state" }
deny[msg] { input.delivery_recommissioning_receipt.to_state != "PUBLIC_DELIVERY_RECOMMISSIONING_READY"; msg := "bad to_state" }
deny[msg] { count(input.delivery_recommissioning_receipt.signatures) == 0; msg := "missing signatures" }
allow { count(deny)==0 }
