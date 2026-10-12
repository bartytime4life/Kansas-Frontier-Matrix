# EvidenceTemporalPostureAssessment fixtures

These synthetic, rights-safe fixtures are byte-for-byte copies of the legacy evidence `TemporalAuthorityEnvelope` JSON fixtures. They prove exact replay compatibility while the semantic object receives a distinct evidence responsibility and name.

- `valid/current_observation.json` must pass both canonical and legacy evidence entry points at the same validation instant.
- `invalid/inverted_validity.json` must be rejected for inverted validity.
- `invalid/source_after_retrieval.json` must be rejected because the source update follows retrieval.

The fixtures do not conform to the common `TemporalAuthorityEnvelope`, authenticate a source role, resolve evidence, or authorize release/publication. Do not change one fixture tree without changing the compatibility proof and explicitly documenting the migration.
