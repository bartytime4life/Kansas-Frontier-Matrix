package soil.delivery_restoration

deny["invalid_decision"] if { not input.delivery_restoration_receipt.decision in {"pass","degraded","governance_only","requires_reprobe","requires_routing_rebuild","blocked"} }
deny["bad_from_state"] if { input.delivery_restoration_receipt.from_state != "PUBLIC_DELIVERY_RECOMMISSIONING_READY" }
deny["bad_to_state"] if { input.delivery_restoration_receipt.to_state != "PUBLIC_DELIVERY_RESTORATION_READY" }
deny["missing_signatures"] if { not input.delivery_restoration_receipt.signatures }
