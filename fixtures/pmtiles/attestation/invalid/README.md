<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-invalid-readme
title: Invalid PMTiles Attestation Fixture Descriptors
type: README
version: v0.2.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward
created: 2026-08-02
updated: 2026-08-03
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns negative generated-bundle and declared-manifest mutation descriptors with pinned finite reason codes without storing production bytes or granting authority
truth_posture: test-or-abstain
related:
  - ../README.md
  - ../../../../tests/validators/test_pmtiles_attestation_bundle.py
notes:
  - "Each descriptor is expected to fail closed for the pinned reason set."
  - "This lane has one fixture-steward authority-owner role; assignment NEEDS VERIFICATION. Validation and PMTiles stewards are review roles. CODEOWNERS routes review to @bartytime4life."
[/KFM_META_BLOCK_V2] -->

# Invalid PMTiles attestation fixture descriptors

Each descriptor introduces one named mutation. The adjacent
`.expected_error.txt` pins its primary finite reason code; the JSON descriptor
pins the complete sorted issue set when reconciliation produces more than one
finding.

The `manifest_` cases isolate one declaration fault each: profile identity,
archive binding, digest-bound-ref syntax, media-type literal, digest, byte size,
build spec, versioned lineage-ref syntax, generator-identifier syntax, PMTiles
version, tile format, tiling scheme, zoom, KFM Web-Mercator-envelope bounds,
vector-layer id/field maps, or embedded payload. Archive-header and metadata
contradictions are covered separately from declaration-shape failures. They are
compatibility evidence, not a canonical schema fixture family.
