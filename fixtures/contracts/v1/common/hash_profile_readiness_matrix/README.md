# HashProfileReadinessMatrix fixture suite

`cases.json` applies deterministic JSON-pointer replacements to the repository matrix. Each case declares whether the validator should recompute `spec_hash` after mutation, allowing semantic failures to be isolated from integrity failures.

The suite is no-network and contains no keys, signatures, source data, release artifacts, or policy decisions. A PASS is readiness evidence only.
