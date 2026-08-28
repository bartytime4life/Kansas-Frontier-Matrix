<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/backfill-window-plan/v1
title: Backfill Window Plan Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - ../../schemas/contracts/v1/runtime/backfill_window_request.schema.json
  - ../../schemas/contracts/v1/runtime/backfill_window_plan.schema.json
  - ../../packages/pipelines-core/src/pipelines_core/backfill_window.py
  - ../../scripts/plan_backfill_window.py
  - ../../fixtures/contracts/v1/runtime/backfill_window_plan/
  - ../../tests/packages/pipelines_core/test_backfill_window.py
tags: [kfm, runtime, pipeline, backfill, deterministic-identity, idempotency]
notes:
  - "Defines a planning-only no-network object; it does not execute a backfill, write lifecycle data, promote, release, or publish."
  - "The generated artifact URI is a proposed immutable destination. A separate governed runner must still satisfy policy, signature, review, promotion, and release gates."
[/KFM_META_BLOCK_V2] -->

# Backfill Window Plan

A `BackfillWindowPlan` turns one bounded dataset/time-window request into a deterministic identity and immutable proposed artifact path.

It exists to make replay and deduplication inspectable before a runner touches data. The planner is intentionally narrower than a backfill job: it performs no network fetch, source activation, artifact write, policy evaluation, signature operation, promotion, release, deployment, or publication.

## Semantic inputs

- `dataset_id`: responsibility-safe dataset identifier.
- `source_uri`: immutable or reviewable source reference using `https://` or `kfm://`.
- `window.start` / `window.end`: UTC, half-open interval `[start, end)` with `start < end` and a maximum duration of 366 days.
- `manifest`: non-empty JSON object whose canonical bytes define `spec_hash`.
- `current_published_spec_hash`: optional currently released digest used only for `NOOP` versus `REBUILD` planning.

## Deterministic outputs

- `spec_hash = sha256(canonical_json(manifest))` using sorted UTF-8 JSON with insignificant whitespace removed and non-finite numbers denied.
- `dedupe_key = sha256(dataset_id + source_uri + canonical window + spec_hash)`.
- `plan_id` and `artifact_uri` are pure functions of those normalized values.
- `decision = NOOP` only when the supplied current published hash exactly equals `spec_hash`; otherwise `REBUILD`.

A plan is byte-stable across manifest key order and repeated executions. It carries no wall-clock generation time.

## Required downstream gates

Every plan declares that policy checking, signature verification, and promotion review remain required. `write_authority` is always `false`. A valid plan is not a RunReceipt, EvidenceBundle, ProofPack, PromotionDecision, ReleaseManifest, or publication event.

## Lifecycle boundary

The artifact URI points to a possible `data/processed/` destination because a backfill runner would produce a validated processed artifact before catalog/proof/release closure. The planner does not create that path or bypass `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.

## Rollback

Remove this additive contract/schema/module/script/fixture/test packet. No data migration or published-state reversal is required because the planner writes no lifecycle state.
