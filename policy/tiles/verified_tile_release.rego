package tiles.verified_tile_release

deny contains "missing proof bundle" if { not input.proof_bundle }
deny contains "failed validator" if { input.validation_result != "ALLOW" }
deny contains "failed verifier trace" if { not input.trace_pass }
deny contains "public forbidden path" if { some p in input.public_artifacts; regex.match("(^|/)(RAW|WORK|QUARANTINE)(/|$)", p) }
deny contains "unverified runtime render mode" if { input.runtime_contract.render_mode != "verified_only" }
deny contains "missing evidence bundle" if { not input.required_refs.EvidenceBundle }
deny contains "missing release manifest" if { not input.required_refs.ReleaseManifest }
deny contains "unresolved correction/rollback posture" if { input.rollback_ref == "" or input.correction_ref == "" }
deny contains "unsupported sensitivity or rights posture" if { input.sensitivity != "public_safe" or input.rights != "public" }
