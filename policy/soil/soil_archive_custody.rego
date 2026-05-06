package kfm.soil.archive_custody

deny[msg] { input.archive_receipt.decision != "pass"; msg := "archive_receipt_not_pass" }
deny[msg] { input.archive_receipt.from_state != "PRESERVATION_READY"; msg := "bad_from_state" }
deny[msg] { input.archive_receipt.to_state != "ARCHIVAL_CUSTODY_READY"; msg := "bad_to_state" }
deny[msg] { not input.archive_receipt.signatures; msg := "missing_signatures" }
deny[msg] { input.archive_receipt.live_archive_upload_performed == true; msg := "live_upload_true" }
