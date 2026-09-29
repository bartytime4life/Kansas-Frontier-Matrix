# Hydrology proof-slice fixtures

Synthetic inputs for [`pipelines/domains/hydrology/proof_slice.py`](../../../../pipelines/domains/hydrology/proof_slice.py).
The semantics are in [`contracts/domains/hydrology/proof_slice.md`](../../../../contracts/domains/hydrology/proof_slice.md).

| File | Role |
|---|---|
| `base_request.json` | The complete synthetic request every case starts from: governed API surface, a `data/published/` artifact, the `current` packet scenario, the valid EvidenceBundle, generalized HUC12 geometry, and a rollback target. |
| `evidence_bundle.json` | EvidenceBundle over the [Living Waters packet](../../../contracts/v1/domains/hydrology/living_waters_fixture_packet/valid/first_proof.json): it binds the packet's SHA-256 in `checksums` and carries a JCS `spec_hash` computed with `packages/hashing`. |
| `evidence_bundle_unknown_rights.json` | The same bundle with license `UNKNOWN`. |
| `evidence_bundle_tampered.json` | The valid bundle edited after hashing, so its `spec_hash` no longer matches. |
| `cases/NN-*.json` | One case per file: overrides on the base request and the thin-slice assertion it exercises. |

Every file here is pinned by SHA-256 in
[`control_plane/readiness/hydrology-proof-slice-profile.json`](../../../../control_plane/readiness/hydrology-proof-slice-profile.json).
Editing one changes its digest; update the profile in the same change.

Nothing here is a real observation, gauge, source record, or license grant.
