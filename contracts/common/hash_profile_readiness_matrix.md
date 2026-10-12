<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/hash-profile-readiness-matrix
title: Hash Profile Readiness Matrix semantic contract
type: semantic-contract; hash-readiness; object-family; fixture-first
version: v0.1.0
status: proposed; inactive; readiness-evidence-only; no-policy-adoption
owners: OWNER_TBD — Integrity steward · Contracts steward · Schema steward · Security reviewer · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; hashing; integrity; readiness; fail-closed; non-authoritative
related:
  - ./spec_hash.md
  - ../../schemas/contracts/v1/common/hash_profile_readiness_matrix.schema.json
  - ../../control_plane/hash_profile_readiness_matrix.json
  - ../../packages/hashing/
  - ../../tools/validators/validate_hash_profile_readiness_matrix.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, hashing, spec-hash, content-hash, root-hash, range-hash, descriptor-hash, signature, readiness]
notes:
  - "Source idea: KFM-P4-PROG-0003."
  - "This matrix is not an ADR and cannot adopt or migrate a hash policy."
[/KFM_META_BLOCK_V2] -->

# Hash Profile Readiness Matrix

`HashProfileReadinessMatrix` is an **inactive, machine-checkable readiness index** for the hash roles named by KFM-P4-PROG-0003. It prevents terms such as `descriptor_hash`, `content_hash`, `root_hash`, `range_hash`, `spec_hash`, SHA-256, BLAKE3, Bao, and canonical JSON from being treated as interchangeable while the final cross-family policy remains unadopted.

It records candidate tuples and verifies that the one already-executable `spec_hash` tuple remains exactly bound to the current shared hashing package. It does not create a new hash authority, activate BLAKE3/Bao, authorize signatures, migrate stored digests, or change an object-family contract.

## Roles

| Role | Intended question | Readiness posture |
|---|---|---|
| `spec_hash` | Do declared semantic inputs canonicalize to the same identity? | Current executable baseline: RFC 8785 JCS + SHA-256. |
| `descriptor_hash` | Does a versioned descriptor have the same selected semantic content? | Inactive candidate; field selection remains object-family-owned. |
| `content_hash` | Are exact artifact bytes identical? | Inactive candidate. |
| `root_hash` | Does an ordered governed file set have the same root? | Inactive candidate; leaf and inclusion rules unresolved. |
| `range_hash` | Can a byte range be verified against a streaming proof tree? | Inactive and unavailable; BLAKE3/Bao is readiness-only. |
| `signature_digest` | Which bytes are supplied to a signature envelope? | Inactive candidate; signature verification is a separate control. |

## Hard boundaries

1. The matrix status is `PROPOSED_INACTIVE`.
2. `decision_ref` is `null`; an accepted ADR must precede any new activation or migration.
3. Exactly one profile may be `BASELINE`: the current executable `spec_hash` tuple.
4. An unavailable implementation cannot be active.
5. Algorithm prefix and canonicalization are role-specific and machine-checked.
6. A matching digest establishes only the declared identity property. It does not establish truth, evidence sufficiency, rights, policy, review, release, or publication.
7. Object-family contracts continue to own field selection, pre-canonicalization transforms, file inclusion, chunking, and signing obligations.

## Authority split

- Semantic readiness meaning: `contracts/common/hash_profile_readiness_matrix.md`.
- Machine shape: `schemas/contracts/v1/common/hash_profile_readiness_matrix.schema.json`.
- Inactive machine index: `control_plane/hash_profile_readiness_matrix.json`.
- Executable `spec_hash`: `packages/hashing/`.
- Final adoption, migration, compatibility, and deprecation: a separate accepted ADR and later implementation change.
- Fixtures, validator, tests, and CI: their corresponding responsibility roots.

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. The matrix is inactive and creates no digest migration, signature rotation, release withdrawal, or external cleanup requirement.
