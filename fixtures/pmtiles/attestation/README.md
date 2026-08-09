<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-readme
title: PMTiles Attestation Compatibility Fixtures
type: README
version: v0.3.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward
created: 2026-08-02
updated: 2026-08-09
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns deterministic mutation descriptors for bounded PMTiles split-bundle, captured partial-read, and opt-in declared-manifest compatibility validation while excluding production bytes, credentials, canonical schema authority, truth, proof, release, and publication authority
truth_posture: test-or-abstain
related:
  - ../../../tools/validators/pmtiles/validate_attestation_bundle.py
  - ../../../tools/validators/pmtiles/verify_partial_read.py
  - ../../../tests/validators/test_pmtiles_attestation_bundle.py
  - ../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
notes:
  - "PMTiles bytes and companion objects are generated only in temporary test directories."
  - "This lane has one fixture-steward authority-owner role; assignment NEEDS VERIFICATION. PMTiles and validation stewards are review roles. CODEOWNERS routes review to @bartytime4life."
  - "A positive fixture proves bounded structural behavior only and retains cryptographic, range-metadata-authentication, policy, and release holds."
[/KFM_META_BLOCK_V2] -->

# PMTiles attestation compatibility fixtures

This lane contains small mutation descriptors for the split PMTiles + PMIDX +
PMSIG + RunReceipt compatibility profile and its opt-in
`kfm.pmtiles.tile-artifact-manifest.compat.v1` declared-metadata check, plus the
`partial-read/` descriptor matrix for
`kfm.pmtiles.partial-read.compat.v1`, exercised by
`tests/validators/test_pmtiles_attestation_bundle.py`.

The tests generate a minimal PMTiles v3 archive and all companion JSON inside a
temporary directory, then apply exactly the named mutation. No PMTiles binary,
source dataset, signature, private key, production receipt, release record, or
publication artifact is stored here.

`manifest_*.json` descriptors test PMTiles v3 + MVT declarations against the
generated archive header, embedded vector-layer metadata, SHA-256 bundle
binding, `spec_hash`, digest-bound artifact-ref syntax, versioned source-ref
syntax, generation-tool identifier syntax, and order-independent vector-layer
id/field maps. Source refs, generator declarations, and the artifact locator
are not resolved or attested. These fixtures do not instantiate or select a
canonical `TileArtifactManifest` schema.

`STRUCTURAL_PASS` proves only the bounded offline checks named by the validator.
Every positive manifest case retains schema-authority, declared-provenance,
artifact-registry, cryptographic, range-metadata-authentication, policy, and
release holds.

`partial-read/` descriptors generate captured response and containing-leaf
bytes only in a temporary test directory. Their positive outcome is
`STRUCTURAL_HOLD`, because the compatibility check does not authenticate range
metadata, cryptographically verify PMSIG, recompute the whole archive, adopt
Bao/BLAKE3, execute policy, or authorize release.

Supported envelope: PMIDX JSON up to 16 MiB, companion JSON up to 1 MiB,
`chunk_bytes` from 1 byte through 64 MiB, and at most 100,000 leaves or ranges.
Ranges use half-open byte intervals `[offset, offset + length)` and the existing
single `leaf` field; therefore a range must remain within one declared chunk.
