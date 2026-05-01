<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/air-qa-promotion-slice-v1
title: Atmosphere Air QA Promotion Slice (No-Network)
type: standard
version: v1
status: draft
owners: atmosphere-air domain steward, policy steward, data steward
created: 2026-05-01
updated: 2026-05-01
policy_label: internal-governance
related: [schemas/contracts/v1/air/qa_summary.schema.json, policy/air/air_qa.rego, tools/validators/air/validate_air_qa.py]
tags: [kfm, atmosphere, air, qa, promotion, nowcast, aqs, mesonet, no-network]
notes: [No-network governance slice; live connector claims are prohibited in this document.]
[/KFM_META_BLOCK_V2] -->

# Air QA + Promotion Slice (No-Network)

This slice provides **fixture-backed, no-network governance** for AirNow NowCast / EPA AQS / Kansas Mesonet evidence handling.

## Lifecycle placement

`RAW/WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`

- Public clients must not read RAW/WORK/QUARANTINE directly.
- NowCast is operational evidence and must not be treated as validated AQS truth.
- Promotion must fail closed when policy denies.

## Gates A-C

- **Gate A:** deny when `nowcast_max > 35 ug_m3`.
- **Gate B:** deny when `nowcast_vs_baseline_sigma > 2`.
- **Gate C:** deny when `station_coverage_pct < 75`.

Additional denial rules:

- deny when AQS hard-denial rows are included in baseline.
- deny public publication unless both `run_receipt_ref` and `evidence_bundle_ref` are present.

## Override path

- Gate C can proceed only through steward review.
- Gate D requires signed attestation.
- AQS reconciliation must complete within 72 hours.

## Scope and boundaries

- This slice keeps receipts, proofs, release manifests, and evidence bundles as separate artifacts.
- This implementation is deterministic and fixture-backed.
- Live AirNow/AQS/Mesonet connectors are **PROPOSED / NEEDS_VERIFICATION**.
