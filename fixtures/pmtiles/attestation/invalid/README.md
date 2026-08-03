<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-pmtiles-attestation-invalid-readme
title: Invalid PMTiles Attestation Fixture Descriptors
type: README
version: v0.1.0
status: draft; PROPOSED; synthetic-only
owner: TODO-fixture-steward-plus-validation-steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; synthetic-fixtures; no-public-path
owning_root: fixtures/
responsibility: owns negative generated-bundle mutation descriptors and pinned finite reason codes without storing production bytes or granting authority
truth_posture: test-or-abstain
related:
  - ../README.md
  - ../../../../tests/validators/test_pmtiles_attestation_bundle.py
notes:
  - "Each descriptor is expected to fail closed for the pinned reason set."
[/KFM_META_BLOCK_V2] -->

# Invalid PMTiles attestation fixture descriptors

Each descriptor introduces one named mutation. The adjacent
`.expected_error.txt` pins its primary finite reason code; the JSON descriptor
pins the complete sorted issue set when reconciliation produces more than one
finding.
