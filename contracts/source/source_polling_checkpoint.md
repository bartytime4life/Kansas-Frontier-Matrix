<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-polling-checkpoint
title: SourcePollingCheckpoint Contract
type: semantic-contract; conditional-request state
version: v0.1.0
status: proposed; fixture-only; no-network; non-fetching
owners: OWNER_TBD — Source steward · Connector steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; source; polling; candidate-only
related:
  - ./source_health_assessment.md
  - ./source_availability_watchlist.md
  - ./stac_asset_head_prefilter.md
  - ../../schemas/contracts/v1/source/source_polling_checkpoint.schema.json
[/KFM_META_BLOCK_V2] -->

# SourcePollingCheckpoint

`SourcePollingCheckpoint` records conditional-request validator state—ETag, Last-Modified, content length, and optional representation digest—without making a network request. It turns `NOT_MODIFIED`, `MODIFIED`, unavailable, unknown, and error paths into explicit deterministic review outcomes.

## Source basis

Pass 32 carries `KFM-P18-PROG-0009`, which proposes persisting ETag, Last-Modified, source URL, and validator state per SourceRef so changed and unchanged paths are explicit. This packet adapts the concept to opaque endpoint references and reuses existing source-health, watchlist, and STAC HEAD-prefilter boundaries without replacing them.

## Invariants

- the source descriptor reference is derived exactly from `source_id`;
- `NOT_MODIFIED` requires at least one usable validator and equal prior/current state;
- `MODIFIED` requires a proven state change and a candidate-fetch reference;
- no-change, unavailable, unknown, and error states forbid a candidate-fetch reference;
- decision and reason codes are recomputed;
- no network, source activation, fetch, RAW write, promotion, release, or publication authority is present.

A `FETCH_CANDIDATE` is review metadata only. It does not download bytes or admit RAW data.

## Directory Rules basis

Meaning belongs in `contracts/source/`; shape in `schemas/contracts/v1/source/`; fixtures in `fixtures/contracts/v1/source/`; validation in `tools/validators/source/`; tests in `tests/validators/`; orchestration in `.github/workflows/`; and authoring accountability in `data/receipts/generated/`.

## Validation

```bash
python -m unittest tests.validators.test_validate_source_polling_checkpoint -v
python tools/validators/source/validate_source_polling_checkpoint.py --fixtures
```

## Rollback

Revert the additive packet. No source, endpoint, capture, lifecycle object, release, or public artifact is changed.
