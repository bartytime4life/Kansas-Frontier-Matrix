package soil.active_release_pointer

default deny = []

deny[msg] { input.active_release_pointer_receipt.decision != "pass"; input.active_release_pointer_receipt.decision != "degraded"; input.active_release_pointer_receipt.decision != "governance_only"; msg := "bad_decision" }
deny[msg] { input.active_release_pointer_receipt.from_state != "RELEASE_LINEAGE_RECONCILED"; msg := "bad_from_state" }
deny[msg] { input.active_release_pointer_receipt.to_state != "ACTIVE_RELEASE_POINTER_RECONCILED"; msg := "bad_to_state" }
deny[msg] { input.active_release_pointer_receipt.published_current_pointer_mutated == true; msg := "published_pointer_mutated" }
deny[msg] { input.active_release_pointer_receipt.immutable_artifacts_mutated == true; msg := "immutable_mutated" }
