<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-cog-byte-range-integrity-manifest-source-map
title: Pass 18 COG Byte-Range Integrity Manifest Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Raster-artifact steward · Integrity steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; cog; byte-range; integrity
responsibility: Reconcile the supplied COG internal-chunk integrity idea with current repository doctrine while preserving format, evidence, interpretation, policy, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN cryptographic-profile graduation and consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/cog_byte_range_integrity_manifest.md
  - ../../../contracts/release/tile_artifact_manifest.md
  - ../../standards/COG.md
  - ../../architecture/publication/GEO_MANIFEST.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 COG Byte-Range Integrity Manifest Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card KFM-P18-INV-183 | COG internal tile and overview hash manifests can support partial-read integrity when justified; missing, mismatched, or stale sidecars must remain visible; byte verification must not imply interpretation authority. | CONFIRMED source statement |
| Connected Drive KFM Full Atlas seed cards, KFM-CAND-0093 | The map-artifact integrity surface calls for PMTiles/COG sidecar schemas, byte-range proofs, artifact validators, signatures, and no-in-place-overwrite checks. | CONFIRMED thematic corroboration |
| Current COG standard and KFMGeoManifest architecture | COG is a downstream carrier; whole-file identity and internal-chunk recomputation are named, but format, evidence, policy, and release remain separate. | CONFIRMED doctrine |
| Current TileArtifactManifest | The release object may reference COG digest and range metadata, but its machine schema is a permissive placeholder and it has no COG range verifier. | CONFIRMED adjacent responsibility |
| Current PMTiles verifier | PMTiles has a format-specific partial-read proof implementation. Reusing its semantics as COG proof would collapse distinct formats and the open cryptographic-profile decision. | CONFIRMED non-substitute |
| Current main and PR search | No exact COG byte-range integrity schema, fixture family, local validator, focused workflow, source map, or matching pull request was found before authoring. | CONFIRMED bounded gap |

## Adaptation

The implementation is a closed synthetic candidate under the existing evidence family. It binds a local fixture to one whole SHA-256 digest and a canonical, contiguous, full-coverage list of explicit SHA-256 ranges. It records payload availability, immutability, sidecar freshness, declared range roles, format-validation posture, evidence refs, and fixed-false authority claims.

The fixture is deliberately not a TIFF or COG. The validator does not parse IFDs, tiles, overviews, HTTP behavior, signatures, or pixels. It proves local byte coherence only. BAO/BLAKE3 selection, public sidecar shape, real COG conformance, signing, policy, release, and client activation remain outside this packet.

## Directory Rules basis

The accepted responsibility-root model places semantic meaning in contracts/evidence/, machine shape in schemas/contracts/v1/evidence/, synthetic replay in fixtures/contracts/v1/evidence/, executable validation in tools/validators/evidence/, conformance proof in tests/validators/evidence/, orchestration in .github/workflows/, reconciliation in docs/intake/exploratory/, and generated authoring provenance in data/receipts/generated/.

Evidence owns the packet because it preserves a reproducible claim about referenced bytes. TileArtifactManifest and release transitions remain under release responsibility; COG conformance guidance remains under standards responsibility.

## Non-effects and rollback

A local PASS is not TIFF or COG validation, evidence closure, interpretation fitness, signing, policy approval, review completion, promotion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
