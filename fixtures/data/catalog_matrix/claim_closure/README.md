# CatalogMatrix ClaimEnvelope closure fixtures

These synthetic, no-network fixtures exercise the proposed `CLAIM_ENVELOPE_CATALOG_MATRIX_CLOSURE_V1` integration profile.

- `valid/` contains conservative aligned projections: READY/PUBLISHED, HOLD/CANDIDATE, and DENY/terminal-negative posture.
- `invalid/` contains closed-schema failures.
- `semantic_invalid/` contains schema-valid overstatement or reference-drift cases.
- `expected_findings_manifest.json` is the exact polarity and reason-code contract replayed by the validator and focused tests.

A valid fixture proves only local deterministic consistency. It does not resolve an EvidenceRef, validate a real source, decide policy, authenticate a reviewer, create a release, publish a claim, or authorize public use.
