<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/hash-binding-assessment
title: Hash Binding Assessment semantic contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; assessment-only; no-policy-adoption
owners: OWNER_TBD — Integrity steward · Contracts steward · Schema steward · Security reviewer · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: repository-facing; hashing; integrity; fail-closed; non-authoritative
owning_root: contracts/
responsibility: Define the bounded semantics and non-authority boundary for synthetic purpose-specific hash-subject assessments.
truth_posture: proposed; cite-or-abstain
related:
  - ./hash_profile_readiness_matrix.md
  - ../../control_plane/hash_profile_readiness_matrix.json
  - ../../schemas/contracts/v1/common/hash_binding_assessment.schema.json
  - ../../fixtures/contracts/v1/common/hash_binding_assessment/
  - ../../tools/validators/validate_hash_binding_assessment.py
  - ../../docs/intake/exploratory/full-atlas-hash-binding-assessment-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, hashing, canonicalization, hash-binding, integrity, test-vectors, readiness]
notes:
  - "Source idea: KFM-TRIAD-042 and KFM-CAND-0124 through KFM-CAND-0126."
  - "This assessment is not an ADR and cannot activate, equate, or migrate a hash profile."
[/KFM_META_BLOCK_V2] -->

# Hash Binding Assessment

`HashBindingAssessment` is a **synthetic, inactive conformance carrier** for inspecting how a purpose-specific digest would bind to a subject. It complements the existing `HashProfileReadinessMatrix`: the matrix records which profile tuples are known, while this assessment proves that a proposed subject declaration is non-recursive, purpose-bound, and no more authoritative than its referenced readiness entry.

The assessment never computes a candidate `content_hash`, `descriptor_hash`, `root_hash`, `range_hash`, or `signature_digest`. The only executable digest is the repository's existing `spec_hash`, used to make the synthetic assessment itself tamper-evident.

## Binding fields

| Field | Meaning |
|---|---|
| `profile_id`, `hash_role` | Exact identity and role from the readiness matrix. |
| `purpose`, `subject_kind` | The single identity question and the kind of subject being bound. |
| `algorithm`, `digest_prefix`, `canonicalization_profile` | Exact inactive or baseline tuple inherited from the readiness matrix. |
| `included_fields`, `excluded_fields` | Explicit subject selection. A field cannot appear in both. |
| `volatile_fields` | Unstable values that must be excluded from semantic subjects. |
| `digest_fields` | Digest outputs that must be excluded from their own subjects. |
| `signature_fields` | Signature material that must be excluded from signed subjects. |
| `unordered_collections` | Every selected set-like collection and its deterministic ordering rule. |
| `finite_numbers_required` | Whether non-finite JSON numbers must be rejected before canonicalization. |
| `crs_profile` | Geometry coordinate-reference profile, when a geometry binding eventually exists. |
| `equality_scope`, `comparison_profile_id` | Equality is meaningful only within the same declared profile. |

## Invariants

1. The assessment status is `PROPOSED_INACTIVE`, and `decision_ref` remains `null`.
2. Every binding references exactly one entry in `control_plane/hash_profile_readiness_matrix.json` and repeats its role, algorithm, prefix, canonicalization, implementation, and activation state without modification.
3. Profile identifiers and purpose gaps are complete, unique, and canonically ordered.
4. Digest fields, signature fields, and volatile fields are excluded from their subjects.
5. Included and excluded fields are disjoint.
6. Every selected unordered collection has a declared deterministic ordering rule.
7. RFC 8785 JCS subjects require finite JSON numbers.
8. Cross-profile comparison is rejected even when algorithms or output bytes happen to match.
9. Normalized-geometry identity remains `HOLD_NO_PROFILE` until a profile declares at least CRS and finite-coordinate controls.
10. Receipt-payload identity remains `HOLD_NO_PROFILE`; it cannot silently reuse specification or signature identity.
11. All truth, authority, source-admission, evidence-closure, policy, release, and publication effects are fixed to `false`.

## Outcome meaning

- `PASS` means only that the synthetic declaration is closed, matrix-consistent, non-recursive, and purpose-bound.
- `ERROR` means its shape, reference closure, canonicalization controls, subject exclusions, comparison scope, or self-hash is invalid.

Neither outcome proves that candidate algorithms are implemented, that input content is true, that evidence is sufficient, or that a digest is authorized for storage, signature, release, or public use.

## Authority split

- Semantic meaning: this file.
- Readiness authority: `contracts/common/hash_profile_readiness_matrix.md` and its machine instance.
- Machine shape: `schemas/contracts/v1/common/hash_binding_assessment.schema.json`.
- Synthetic vectors: `fixtures/contracts/v1/common/hash_binding_assessment/`.
- Deterministic validation: `tools/validators/validate_hash_binding_assessment.py` and focused tests.
- Activation, equivalence, migration, and deprecation: a later accepted ADR and implementation change.

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. The slice creates no stored digest, signature, migration, release, publication, or external cleanup obligation.
