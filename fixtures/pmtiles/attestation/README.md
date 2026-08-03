<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-readme
title: PMTiles Attestation Compatibility Fixtures
type: README
version: v0.1.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward-plus-pmtiles-steward-plus-validation-steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns deterministic mutation descriptors for bounded PMTiles split-bundle validation while excluding production bytes, credentials, truth, proof, release, and publication authority
truth_posture: test-or-abstain
related:
  - ../../../tools/validators/pmtiles/validate_attestation_bundle.py
  - ../../../tests/validators/test_pmtiles_attestation_bundle.py
  - ../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
notes:
  - "PMTiles bytes and companion objects are generated only in temporary test directories."
  - "A positive fixture proves bounded structural behavior only and retains cryptographic, range-metadata-authentication, policy, and release holds."
[/KFM_META_BLOCK_V2] -->

# PMTiles attestation compatibility fixtures

This lane contains small mutation descriptors for the split PMTiles + PMIDX +
PMSIG + RunReceipt compatibility profile exercised by
`tests/validators/test_pmtiles_attestation_bundle.py`.

The tests generate a minimal PMTiles v3 archive and all companion JSON inside a
temporary directory, then apply exactly the named mutation. No PMTiles binary,
source dataset, signature, private key, production receipt, release record, or
publication artifact is stored here.

`STRUCTURAL_PASS` proves only the bounded offline checks named by the validator.
Every positive case retains cryptographic, range-metadata-authentication,
policy, and release holds.

Supported envelope: PMIDX JSON up to 16 MiB, companion JSON up to 1 MiB,
`chunk_bytes` from 1 byte through 64 MiB, and at most 100,000 leaves or ranges.
Ranges use half-open byte intervals `[offset, offset + length)` and the existing
single `leaf` field; therefore a range must remain within one declared chunk.
