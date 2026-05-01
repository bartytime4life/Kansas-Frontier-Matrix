package kfm.soil.correction_resolution

deny[msg] { input.resolution_receipt.decision != "pass"; input.resolution_receipt.decision != "degraded"; msg := "bad resolution decision" }
deny[msg] { input.resolution_receipt.from_state != "PUBLIC_ACCOUNTABILITY_READY"; msg := "bad from_state" }
deny[msg] { input.resolution_receipt.to_state != "CORRECTION_RESOLUTION_READY"; msg := "bad to_state" }
deny[msg] { not input.resolution_receipt.signatures; msg := "missing signatures" }
deny[msg] { input.resolution_receipt.live_helpdesk_submission_performed == true; msg := "live helpdesk forbidden" }
deny[msg] { input.resolution_receipt.live_notification_performed == true; msg := "live notification forbidden" }
