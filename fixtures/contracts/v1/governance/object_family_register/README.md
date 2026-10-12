<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/governance/object-family-register/v1
title: Object Family Register Fixture Pack
type: fixture-readme
version: 1.1.0
status: PROPOSED
owners:
  - UNKNOWN
created: 2026-08-06
updated: 2026-08-22
policy_label: synthetic; public-safe; no-network
owning_root: fixtures/
responsibility: exercise the object-family catalog schema and fail-closed semantic validator with bounded synthetic positive and negative cases
truth_posture: CONFIRMED local synthetic fixture bytes and exact reviewed finding-code manifest / PROPOSED fixture coverage sufficiency / UNKNOWN external consumers / NEEDS VERIFICATION human review and hosted exact-head results
related:
  - ../../../../../docs/registers/OBJECT_FAMILY.md
  - ../../../../../control_plane/object_family_register.yaml
  - ../../../../../schemas/contracts/v1/governance/object_family_register.schema.json
  - ../../../../../tools/validators/control_plane/README.md
notes:
  - "Fixture validation skips repository path existence; the canonical register check does not."
  - "UNKNOWN is explicit and grants no authority."
[/KFM_META_BLOCK_V2] -->

# Object family register fixtures

Synthetic JSON-compatible YAML fixtures for schema, ordering, path-role, maturity, self-authority, and fail-closed validation. `expected_findings_manifest.json` binds each negative file to its reviewed finding-code set. Fixture success does not select a canonical contract or schema candidate, create object-family authority, prove runtime maturity, or approve release or publication.
