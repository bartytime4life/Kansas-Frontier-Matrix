<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-family/receipts
title: contracts/receipts/ — Receipt Semantic Contract Family
type: README; semantic-contract-family
version: v0.1.0
status: proposed; repository-native; non-authoritative
owners: OWNER_TBD — Receipt steward · Contract steward · Evidence steward · Release steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; receipts; process-memory; no-release-authority
related:
  - ../README.md
  - ./representation_receipt.md
  - ../../schemas/contracts/v1/receipts/
  - ../../data/receipts/
tags: [kfm, contracts, receipts, process-memory, representation]
[/KFM_META_BLOCK_V2] -->

# `contracts/receipts/` — receipt semantic contract family

> This lane defines the human-readable meaning of receipt objects. It does not store
> emitted receipts, prove that an operation occurred, evaluate policy, authorize release,
> or publish an artifact.

## Responsibility

| Surface | Owner |
|---|---|
| Receipt meaning and invariants | `contracts/receipts/` |
| Machine-checkable shape | `schemas/contracts/v1/receipts/` |
| Synthetic fixtures | `fixtures/contracts/v1/receipts/` |
| Executable validation | `tools/validators/` |
| Emitted process memory | `data/receipts/` |
| Release, correction, and rollback decisions | `release/` |

## Current contracts

- [`RepresentationReceipt`](representation_receipt.md) records how evidence was
  converted into a downstream visual, tile, scene, raster overview, or export carrier.

## Boundary

A schema-valid receipt remains process memory. Public claims still require resolvable
evidence, applicable policy and review, a governed release state, correction support, and
a rollback target appropriate to consequence.

## Rollback

Before merge, close the draft pull request. After merge, revert the dependency-closed
receipt contract/schema/fixture/validator/test slice. Preserve any real emitted receipts as
audit history and use correction or supersession rather than deletion.
