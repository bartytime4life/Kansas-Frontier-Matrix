# Generated runtime-proof artifact fixtures

Synthetic fixture records for the proposed `GeneratedRuntimeProofArtifact` lifecycle profile.

- `valid/` covers ephemeral, retained, reviewed, promoted-golden, stale, invalidated, and deleted states.
- `invalid/` covers illegal transitions, missing golden review, digest mismatch, unsafe golden promotion, unsupported invalidation, missing deletion receipt, authority overclaim, timing inversion, artifact-ref mismatch, and noncanonical references.
- `invalid/expected_findings_manifest.json` binds every negative case to its reviewed semantic finding code set.

The fixtures contain no real source data, credentials, personal data, or precise sensitive geometry. A passing fixture profile proves only proposed schema and local semantic consistency. It does not authenticate review, create evidence, evaluate policy, authorize release, or publish a runtime output.
