<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-partial-read-readme
title: PMTiles Partial-Read Compatibility Fixtures
type: README
version: v0.1.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns deterministic descriptors for the bounded PMTiles partial-read compatibility verifier without storing PMTiles, response, leaf, signature, key, source, or production-derived bytes
truth_posture: test-or-abstain
related:
  - ../../../../tools/validators/pmtiles/verify_partial_read.py
  - ../../../../tests/validators/test_pmtiles_attestation_bundle.py
  - ../../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
notes:
  - "The focused test generates every byte-bearing object in a temporary directory."
  - "STRUCTURAL_HOLD preserves crypto, range-metadata-authentication, Bao-adoption, whole-archive, policy, and release holds."
[/KFM_META_BLOCK_V2] -->

# PMTiles partial-read compatibility fixtures

These descriptors drive the fixture-only
`kfm.pmtiles.partial-read.compat.v1` reference verifier. The focused test
generates a minimal PMTiles v3 archive, PMIDX, PMSIG-shaped object, captured
range bytes, and containing-leaf bytes in a temporary directory, then applies
exactly one named mutation.

No PMTiles archive, response payload, Merkle leaf payload, signature, key,
credential, production receipt, release record, or source-derived data is
committed here.

The positive case returns `STRUCTURAL_HOLD`, not `STRUCTURAL_PASS`: captured
bytes bind to the existing SHA-256 compatibility commitments, but PMSIG remains
shape-only, PMIDX range metadata is not authenticated by its Merkle root, the
whole archive is not reread, Bao/BLAKE3 is not adopted, and policy plus release
authority are not evaluated.
