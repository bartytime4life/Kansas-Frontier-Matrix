package kfm.fauna.gbif_distribution

deny[msg] { input.kind=="distribution_bundle"; not input.doc["kfm:spec_hash"]; msg:="distribution bundle missing kfm:spec_hash" }
deny[msg] { input.kind=="distribution_bundle"; input.doc.distribution_state=="ready"; input.doc.release_state!="published"; msg:="distribution bundle ready while release_state != published" }
deny[msg] { input.kind=="static_export"; count(input.doc.citation_refs)==0; msg:="static export missing citation_refs" }
deny[msg] { input.kind=="search"; count(input.doc.citation_refs)==0; msg:="search index record missing citations" }
deny[msg] { input.kind=="api"; count(input.doc.citations)==0; msg:="API response missing citations" }
deny[msg] { input.kind=="cache"; not input.doc.reason; msg:="cache invalidation receipt missing reason" }
deny[msg] { input.kind=="takedown"; input.doc.takedown_reason=="withdrawal_applied"; not input.doc.withdrawal_receipt_ref; msg:="takedown receipt missing withdrawal_receipt_ref" }
deny[msg] { input.kind=="takedown"; input.doc.public_use_allowed!=false; msg:="takedown receipt with public_use_allowed != false" }
