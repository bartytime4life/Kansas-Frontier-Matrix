# AIOutputArtifact and AIOutputBatchManifest fixtures

Synthetic, no-network examples for Pass 7 `KFM-P7-IDEA-0001`.

The eight JSON documents under `cases/` partition 26 reviewed cases into:

- per-input artifact valid, schema-invalid, and semantic-invalid families;
- batch-manifest valid, schema-invalid, and semantic-invalid families; and
- exact finite-outcome and finding-code expectations for every case.

Coverage includes all four finite outcomes, active/revoked/superseded item lineage, partial batch revocation, deterministic identity, canonical references, floating-reference denial, count/status reduction, and fixed no-authority flags.

No fixture contains real prompts, model output, evidence, personal data, sensitive geometry, credentials, or chain-of-thought. A fixture or validator `PASS` creates no evidence, policy, review, promotion, release, publication, or public-use authority.
