<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-valid-readme
title: Valid PMTiles Attestation Fixture Descriptors
type: README
version: v0.2.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward
created: 2026-08-02
updated: 2026-08-03
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns positive generated-bundle and declared-manifest compatibility descriptors without establishing schema, cryptographic, policy, release, or publication authority
truth_posture: test-or-abstain
related:
  - ../README.md
  - ../../../../tests/validators/test_pmtiles_attestation_bundle.py
notes:
  - "Descriptors contain no PMTiles binary or production-derived payload."
  - "This lane has one fixture-steward authority-owner role; assignment NEEDS VERIFICATION. Validation and PMTiles stewards are review roles. CODEOWNERS routes review to @bartytime4life."
[/KFM_META_BLOCK_V2] -->

# Valid PMTiles attestation fixture descriptors

Each JSON descriptor must produce `STRUCTURAL_PASS`. That status is not
canonical schema conformance, cryptographic verification, policy approval,
release authorization, or publication eligibility. The `manifest_` case also
must retain `TILE_ARTIFACT_MANIFEST_SCHEMA_AUTHORITY_UNRESOLVED`,
`TILE_MANIFEST_DECLARED_PROVENANCE_UNATTESTED`, and
`TILE_MANIFEST_ARTIFACT_REF_REGISTRY_UNRESOLVED`.
