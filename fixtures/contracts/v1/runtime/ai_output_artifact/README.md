# AIOutputArtifact and AIOutputBatchManifest fixtures

Synthetic, no-network cases for Pass 7 `KFM-P7-IDEA-0001`.

The `cases/` directory contains eight reviewable case documents and 26 total cases:

- six valid per-input artifacts covering all four finite outcomes plus revocation and supersession;
- ten schema-invalid or semantic-invalid per-input artifact cases;
- two valid batch manifests covering active and partially revoked batches; and
- eight schema-invalid or semantic-invalid batch cases covering identity, canonicalization, counts, status, references, and authority boundaries.

Each case declares an exact expected finite outcome and finding-code set. The grouped case documents reduce repetitive fixture metadata while keeping positive, schema-negative, and semantic-negative families explicit.

No fixture contains real prompts, model output, evidence payloads, personal data, sensitive geometry, credentials, or chain-of-thought. A fixture or validator `PASS` creates no evidence, policy, review, promotion, release, publication, or public-use authority.
