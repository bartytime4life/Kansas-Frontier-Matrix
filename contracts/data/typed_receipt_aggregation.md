<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/typed-receipt-aggregation
title: TypedReceiptAggregationCandidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · Receipt steward · Evidence steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; data; receipts; aggregation; no-network; non-release
source_card: KFM-P31-PROG-0013
source_spec_hash: sha256:fa365992bb1c2f8569fd070249dea29aa05442be2a032b33922aed4318317a4a
related:
  - ../../data/receipts/README.md
  - ../../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../schemas/contracts/v1/data/typed_receipt_aggregation.schema.json
  - ../../fixtures/contracts/v1/data/typed_receipt_aggregation/cases.json
  - ../../tools/validators/receipts/validate_typed_receipt_aggregation.py
  - ../../tests/validators/receipts/test_typed_receipt_aggregation.py
tags: [kfm, data, receipt, aggregation, materiality, artifact, fixture]
[/KFM_META_BLOCK_V2] -->

# TypedReceiptAggregationCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile aggregates bounded declarations about existing typed receipt families. It does not become a receipt, resolve receipt bytes, query Rekor, verify a signature, read artifact bytes, evaluate policy, approve review, promote, release, or publish.

## Source-derived gap

Pass 31 card `KFM-P31-PROG-0013` calls for a typed aggregation shape carrying dataset, run, specification, input digest, Rekor identifier, produced artifacts, materiality delta, and publish-candidate declarations. KFM already has distinct `RunReceipt`, `PromotionReceipt`, generated-receipt, and other receipt families. This profile references those families without replacing, widening, or collapsing their authority.

## Directory Rules basis

Aggregation meaning belongs under `contracts/data/`; machine shape under `schemas/contracts/v1/data/`; synthetic cases under `fixtures/contracts/v1/data/`; reusable enforcement under `tools/validators/receipts/`; and proof under `tests/validators/receipts/`. Canonical receipt instances remain under `data/receipts/`. The packet creates no second receipt store, schema root, policy decision, release object, or publication lane.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `dataset_ref` and `run_id` | Scope one synthetic aggregation to one dataset/run context. | They are identifiers only and do not establish source or run validity. |
| `entries` | Canonically ordered typed receipt references, declared schema references, digests, optional Rekor identifiers, produced artifacts, materiality deltas, and publish-candidate flags. | Duplicate receipt references, duplicate artifact paths, incoherent materiality flags, or unordered lists fail. |
| `summary` | Exact reproduced counts and closure lists. | Stale or hand-edited summaries fail. |
| `review_posture` | Fixed `HOLD_FOR_SEPARATE_REVIEW`. | Aggregation never upgrades a receipt or candidate to approved, promoted, released, or published. |
| `controls` | Fixed no-resolution and non-authority posture. | Receipt resolution, Rekor access, signature verification, artifact reads, policy, review, promotion, release, and publication remain false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the complete record after removing `aggregation_id` and `spec_hash`. `aggregation_id` is `kfm:typed-receipt-aggregation:` followed by the first 24 hexadecimal digest characters.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/receipts \
  --pattern 'test_typed_receipt_aggregation.py' \
  --verbose

python tools/validators/receipts/validate_typed_receipt_aggregation.py --fixtures
```

A pass proves only the bounded synthetic declaration, exact summary closure, canonical ordering, fixed non-effects, and deterministic identity encoded here.

## Rollback

Revert this additive packet. Existing receipt contracts, receipt instances, verification state, lifecycle state, release state, and publication state are unaffected.
