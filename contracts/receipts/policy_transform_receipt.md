<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/receipts/policy-transform-receipt
title: PolicyTransformReceiptCandidate Semantic Contract
type: semantic-contract; receipt; fixture-first; no-network
version: v0.1.0
status: proposed; inactive; fixture-only; no-runtime-transform-proof; no-release-authority
owners: OWNER_TBD — Receipt steward · Policy steward · Release steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; receipts; policy; transform; rollback; no-release-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/receipts/policy_transform_receipt.schema.json
  - ../../fixtures/contracts/v1/receipts/policy_transform_receipt/
  - ../../tools/validators/validate_policy_transform_receipt.py
  - ../../tests/validators/test_validate_policy_transform_receipt.py
  - ../policy/policy_transform_plan_simulation.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, receipt, policy-transform, fixture-only, deterministic, rollback]
[/KFM_META_BLOCK_V2] -->

# `PolicyTransformReceiptCandidate`

> A fixture-only process-memory candidate that binds a **satisfying**
> `PolicyTransformPlanSimulation` to declared input/output snapshots, an exact ordered
> operation declaration, obligation references, and a rollback target. A valid candidate
> is not evidence that any transform ran and grants no policy, review, promotion, release,
> publication, or public-use authority.

## Purpose and boundary

The policy-obligation reducer and transform-plan simulator establish what a future
publication path would have to do. This profile adds the next narrow object: a deterministic
receipt-shaped declaration that can be reviewed and replayed before any runtime executor is
admitted.

It intentionally does **not** resolve artifact bytes, execute geometry or temporal transforms,
verify cryptographic attestations, re-evaluate current policy, complete accountable review,
or make a release decision. Those are separate future gates.

## Responsibility-root placement

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/receipts/` |
| Machine shape | `schemas/contracts/v1/receipts/` |
| Synthetic records | `fixtures/contracts/v1/receipts/` |
| Deterministic validator | `tools/validators/` |
| Tests | `tests/validators/` |
| Read-only CI | `.github/workflows/` |
| Generated authoring provenance | `data/receipts/generated/` |

This uses existing roots accepted by ADR-0029 and creates no parallel policy, receipt,
release, proof, registry, or publication authority.

## Required semantics

1. `source_simulation` resolves to an existing fixture under the landed transform-plan
   simulation profile.
2. The source fixture must validate as `SATISFIES`; an `INSUFFICIENT` simulation cannot
   support a receipt candidate.
3. The source simulation ID, full record hash, plan hash, lifecycle phase, and source
   reduction ID/hash are reproduced exactly.
4. The input and output artifact references match the source plan.
5. Operations are derived mechanically and kept in this order:
   `GENERALIZE_GEOMETRY`, `FUZZ_DATE`, `SUPPRESS_GEOMETRY`,
   `SUPPRESS_RECORD`, `APPLY_EMBARGO`.
6. Every operation carries a deterministic `operation_spec_hash` over its position,
   operation, admitted fixture algorithm ID, and parameters.
7. Obligation IDs, source policy references, and reason codes exactly match the plan.
8. `rollback_target` exactly equals the declared input snapshot.
9. Input and output snapshot hashes differ; the profile records no no-op receipt.
10. `spec_hash` is the RFC 8785 JCS + SHA-256 identity of the record with
    `receipt_id` and `spec_hash` omitted. `receipt_id` uses the first 24 digest hex.

## Verification and governance flags

The profile may truthfully mark only deterministic fixture checks as `true`: source-simulation
recomputation, operation derivation, operation-hash recomputation, obligation binding,
receipt identity, and rollback equality. Runtime execution, artifact-byte inspection,
cryptographic verification, policy recheck, accountable review, and release checks remain
`false`; a runtime transform receipt remains required.

All governance effects are fixed false. A green validator result proves fixture conformance
only. It does not mutate repository or canonical state and cannot authorize promotion,
release, publication, or public use.

## Future enforcement boundary

A separately reviewed executor must resolve the exact input bytes, apply admitted algorithms,
calculate output hashes from produced bytes, validate geometry/time/suppression behavior,
recheck current policy and review state, emit a signed runtime `TransformReceipt`, and preserve
correction and rollback targets.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge,
revert the additive commit. No runtime transforms, sources, releases, public artifacts, caches,
or indexes are created by this profile.
