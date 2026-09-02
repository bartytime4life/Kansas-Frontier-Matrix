<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/cog-byte-range-integrity-manifest
title: COGByteRangeIntegrityManifestCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Raster-artifact steward · Integrity steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; raster; cog; integrity; byte-range
responsibility: Define fixture-only semantics for whole-artifact and explicit COG byte-range digest verification without asserting TIFF structure, COG layout, interpretation fitness, review, release, or publication authority.
truth_posture: "CONFIRMED source-card traceability, current-main gap, and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption and cryptographic-profile graduation; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../docs/standards/COG.md
  - ../release/tile_artifact_manifest.md
  - ../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../schemas/contracts/v1/evidence/cog_byte_range_integrity_manifest.schema.json
  - ../../fixtures/contracts/v1/evidence/cog_byte_range_integrity_manifest/cases.json
  - ../../tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py
  - ../../tests/validators/evidence/test_validate_cog_byte_range_integrity_manifest.py
  - ../../docs/intake/exploratory/pass-18-cog-byte-range-integrity-manifest-source-map.md
[/KFM_META_BLOCK_V2] -->

# COGByteRangeIntegrityManifestCandidate

COGByteRangeIntegrityManifestCandidate is an additive, fixture-only profile for binding one declared raster-carrier artifact to a whole-file SHA-256 digest and a canonical, contiguous set of explicit byte-range SHA-256 digests.

It implements a dependency-closed portion of supplied Pass 18 card KFM-P18-INV-183. The card proposes internal tile and overview hash manifests when partial-read integrity or high-risk public use justifies chunk-level verification. Current repository doctrine independently names recomputation of COG internal-chunk hashes as a validation check while keeping artifact integrity separate from format, evidence, policy, and release authority.

## Boundary

The profile is PROPOSED_INACTIVE, deterministic, no-network, synthetic, and non-authoritative. A validator PASS means only that the declared fixture bytes match the whole digest, the explicit ranges cover those bytes exactly once in canonical order, every range digest replays, required range-role declarations are present, and boundary states are locally coherent.

It does not parse TIFF, validate COG structure or overview layout, prove HTTP Range behavior, implement BAO or BLAKE3, resolve evidence, infer pixel meaning, determine data quality or fitness, verify a signature, decide policy, approve review, promote, release, deploy, publish, or authorize public use.

The bundled payload is deliberately not a TIFF or COG. It is a 65-byte synthetic byte string used only to exercise deterministic range verification. Range roles in fixtures are declared labels, not parser-derived structural findings.

## Core semantics

| Surface | Required posture |
|---|---|
| Artifact identity | Governed fixture ref, byte length, whole SHA-256 digest, availability, immutability, and sidecar-freshness states remain explicit. |
| Range set | Entries are unique, canonical by offset, positive length, in bounds, contiguous, non-overlapping, and collectively cover the full artifact. |
| Range roles | Header, image-file-directory, tile-data, and overview-data labels must each appear; labels do not prove those structures exist. |
| Digest replay | The validator reads only a bounded local fixture and checks the whole artifact plus each declared range. |
| Format validation | TIFF, COG-layout, and overview-layout states remain separate and cannot be upgraded without a validator-report reference. |
| Governance | Evidence refs, policy, review, release, rollback, and fixed-false authority claims remain visible and separate. |

This version deliberately uses explicit SHA-256 segments. It does not select the open BAO/BLAKE3 range-proof design, define a public sidecar format, or replace KFMGeoManifest, TileArtifactManifest, COGValidationReport, PolicyDecision, PromotionDecision, or MapReleaseManifest.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| PASS | The bounded local bytes, whole digest, exact range coverage, range digests, role declarations, profile hash, and boundary states are coherent. Human review remains pending. |
| ABSTAIN | Payload availability, immutability, or sidecar freshness cannot be established. |
| DENY | Bytes, ranges, digests, freshness, role coverage, format claims, or governance boundaries conflict. |
| ERROR | The candidate cannot be evaluated safely under the closed machine schema. |

These outcomes are integrity-candidate results only. They are not format conformance, evidence closure, interpretation fitness, policy decisions, review approval, or release decisions.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under contracts/, machine shape under schemas/, synthetic replay under fixtures/, executable validation under tools/, conformance checks under tests/, CI orchestration under .github/, source reconciliation under docs/, and authoring accountability under data/receipts/generated/.

Evidence owns this candidate because its one responsibility is preserving a reproducible integrity assertion about referenced artifact bytes. Release remains the owner of TileArtifactManifest and publication transitions; standards remain the owner of COG conformance guidance.

## Validation

    python -m unittest tests.validators.evidence.test_validate_cog_byte_range_integrity_manifest -v
    python tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py --fixtures

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no source raster, artifact store, catalog, evidence bundle, policy, review, lifecycle, release, deployment, cache, or public surface.
