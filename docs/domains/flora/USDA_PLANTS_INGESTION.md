---
doc_id: kfm://doc/flora/usda-plants-ingestion
title: USDA PLANTS Ingestion Slice
status: draft
owners: [@bartytime4life]
created: 2026-04-30
updated: 2026-04-30
domain: flora
layer: ingestion
kfm_meta_block: v2
---

# USDA PLANTS Ingestion (No-Network Governance Slice)

## Purpose
Define a deterministic, fixture-backed USDA PLANTS ingestion slice for Flora so CI can validate source posture and core data integrity without live downloads.

## Lifecycle placement
This slice currently covers **PROCESSED contract validation** fed by no-network fixtures. RAW/WORK/QUARANTINE intake and promotion to CATALOG/TRIPLET/PUBLISHED remain governed separately and are not bypassed.

## Source posture
- Source: USDA PLANTS Database (USDA/NRCS).
- Role: official public source.
- CI posture: fixtures only, no network access.

## Validation rules
`tools/validators/flora/usda_plants_dataset_validator.py` enforces:
- Schema validation against `schemas/flora/usda_plants_dataset.schema.json` (fail closed if schema missing).
- `properties["plants:symbol"]` is uppercase alphanumeric.
- `scientificName` includes apparent authorship after genus/species.
- `family` is non-empty.
- `license == "USDA / U.S. Public Domain"`.
- `rightsHolder == "United States Department of Agriculture"`.
- Every county `fips` is exactly five digits.
- Top-level `spec_hash` equals `properties["kfm:spec_hash"]`.
- Finite result vocabulary: `pass` or `fail`, with explicit reason codes.

## Fixture strategy
Fixtures live under `tests/fixtures/flora/usda_plants/`:
- `valid_minimal.json` (expected pass)
- `invalid_missing_author.json` (expected fail: missing author token)
- `invalid_bad_fips.json` (expected fail: county fips shape)

Fixtures remain small, no-network, and avoid sensitive coordinate detail.

## Promotion gates
Promotion-facing usage must still satisfy KFM governance:
- cite-or-abstain
- public outputs cannot depend on RAW/WORK/QUARANTINE paths
- separation of receipts/proofs/manifests/published objects
- deterministic `spec_hash` handling across lanes

## Not implemented yet (intentional)
- Live USDA download/fetch connectors.
- Scheduled intake jobs.
- Promotion automation from fixtures to released public artifacts.
- Expanded flora EvidenceBundle integration beyond this validator slice.

These are future work items and are explicitly out of scope for this no-network implementation.
