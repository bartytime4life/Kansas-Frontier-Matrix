# SourceActivationDecision fixtures

Synthetic, no-network fixtures for the proposed source-admission decision profile.

- `valid/` contains six finite-route examples: fixture-only admit, reviewed live RAW capture, quarantine, hold, deny, and evaluator error.
- `invalid/` contains four schema-invalid candidates with repository-compatible structured schema sidecars and one exact validator-code manifest.
- `semantic_invalid/` contains eight schema-valid candidates rejected by descriptor binding, digest, routing, timing, or lineage semantics, plus one exact finding manifest.

No fixture activates a source, represents a real license or policy decision, writes lifecycle state, or grants public-use or release authority.
