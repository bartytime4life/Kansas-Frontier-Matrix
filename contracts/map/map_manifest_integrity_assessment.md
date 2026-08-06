# MapManifestIntegrityAssessment Contract

**Status:** PROPOSED fixture profile  
**Object family:** `MapManifestIntegrityAssessment`  
**Source basis:** *New Ideas 4-10-26.pdf* — MapLibre `KfmIntegrityControl`, manifest hashing, publisher/signature verdicts, EvidenceBundle/proof references, deep asset verification, and finite outcomes  
**Directory Rules basis:** map-manifest meaning belongs under `contracts/map/`; machine shape belongs under `schemas/contracts/v1/map/`; enforcement belongs under `tools/validators/map/`.

## Purpose

Define a deterministic, no-network assessment that a future MapLibre trust control can render without doing ad hoc trust reasoning in the browser. The assessment binds one map release manifest to:

- a canonical manifest `spec_hash`;
- an expected manifest hash supplied by the consuming release/view context;
- a carried signature-verification verdict and signer identity;
- EvidenceBundle and proof-resolution states;
- an optional selected-asset byte/hash verification result; and
- a finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` decision.

The profile does **not** sign a manifest, fetch an asset, perform cryptography, approve a release, publish a map, or make a rendered layer authoritative. It is a fixture-first contract for the trust result that a governed API, CI verifier, or later MapLibre control may consume.

## Canonicalization

`manifest.spec_hash` is SHA-256 over canonical JSON for the `manifest` object with the `spec_hash` member omitted. `spec_hash` on the assessment is SHA-256 over the full assessment with only its top-level `spec_hash` omitted.

Asset entries must be sorted by `asset_id` and have unique identities. Hashes use the `sha256:<hex>` form.

## Outcome precedence

1. `ERROR` for verifier/runtime errors represented by `SIGNATURE_VERIFY_ERROR` or `ASSET_VERIFY_ERROR`.
2. `DENY` for manifest, expected-hash, signer-identity, selected-asset, asset-hash/size, or denied-evidence failures.
3. `ABSTAIN` for unresolved/missing evidence or proof, unverified signature, or required deep verification that was skipped.
4. `ANSWER` when all required checks are resolved and no reason remains.

## Finite reason families

- Manifest: `MANIFEST_SPEC_HASH_MISMATCH`, `EXPECTED_SPEC_HASH_MISMATCH`
- Publisher: `SIGNATURE_FAILED`, `SIGNATURE_UNVERIFIED`, `SIGNATURE_VERIFY_ERROR`, `SIGNER_IDENTITY_MISMATCH`
- Evidence: `EVIDENCE_BUNDLE_MISSING`, `EVIDENCE_BUNDLE_UNRESOLVED`, `EVIDENCE_BUNDLE_DENIED`, `PROOF_REF_MISSING`, `PROOF_UNRESOLVED`, `PROOF_DENIED`
- Asset: `SELECTED_ASSET_MISSING`, `ASSET_DEEP_VERIFY_SKIPPED`, `ASSET_HASH_MISMATCH`, `ASSET_SIZE_MISMATCH`, `ASSET_VERIFY_ERROR`

## Governance boundary

The fixture profile is no-network and carries precomputed verdicts only. It cannot be used as a release, promotion, signature, EvidenceBundle, proof pack, or publication record.

## Validation and rollback

```bash
python -m pytest tests/validators/map/map_manifest_integrity_assessment/test_validate_map_manifest_integrity_assessment.py -q
python tools/validators/map/map_manifest_integrity_assessment/validate_map_manifest_integrity_assessment.py \
  fixtures/map/map_manifest_integrity_assessment/valid/verified_answer.json
```

Rollback is ordinary Git reversion. No runtime route, browser control, release artifact, deployment, or public state is introduced.
