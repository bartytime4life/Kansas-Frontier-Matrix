package fauna.gbif_publication_ops

deny[msg] { not input["kfm:spec_hash"]; msg := "missing_spec_hash" }
deny[msg] { input.release_posture=="published"; input.rights_posture!="public_allowed"; msg := "published_rights_invalid" }
deny[msg] { input.release_posture=="published"; input.sensitivity_posture=="restricted"; msg := "published_sensitivity_invalid" }
