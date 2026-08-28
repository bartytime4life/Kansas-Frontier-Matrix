<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-headless-render-review-packet-source-map
title: Pass 32 headless render review packet - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; partially-implemented; fixture-only; non-authoritative
owners: OWNER_TBD - map runtime steward; CI steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-PROG-0016 with existing PMTiles fixture verification and a bounded CI review-packet continuation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED synthetic review-packet implementation / NEEDS VERIFICATION published-carrier and style-health continuation / UNKNOWN hosted exact-head proof
related: [../../../apps/explorer-web/src/features/map_runtime/HEADLESS_RENDER_REVIEW_PACKET.md, ../../../apps/explorer-web/src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md, ../../../fixtures/pmtiles/mobile_verification/README.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 headless render review packet - governed implementation source map

## Source statement

`KFM-P32-PROG-0016` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes CI that loads published PMTiles through a headless renderer, verifies style health, and uploads screenshots, metrics, and sidecars for review. The card is sourced to `SRC-P32-001`, the connected Drive document *New Ideas*. Both sources record a candidate, not repository implementation or release authority.

## Current repository reconciliation

At inspected `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`, the repository already has deterministic PMTiles header, index, sidecar, signature-subject, receipt, and mobile-emulated browser verification. The `pmtiles-mobile-verification` workflow runs a headless synthetic decode/canvas probe but uploads no screenshot, metrics, or review sidecar. It explicitly retains MapLibre runtime, cryptographic verification, release, and publication holds. Repository and open-pull-request searches found no exact Pass 32 review-packet implementation.

## Implemented boundary

This slice adds a pure review-metrics builder, a digest-binding sidecar builder, one headless Chromium emission scenario, a bounded no-network packet validator, focused tests, and a read-only GitHub Actions upload. The emitted directory contains exactly one screenshot, metrics JSON, and sidecar JSON. Metrics bind the existing synthetic archive/tile sizes, mobile viewport, decoded pixel, bounded timing, and zero external requests. The sidecar binds screenshot and metrics bytes with SHA-256.

This is a **partial** implementation of the source card. It reuses the synthetic in-memory fixture and injected canvas adapter. It does not load a published PMTiles carrier, boot MapLibre, verify style health, perform cryptographic verification, authorize release, deploy, or publish. The packet therefore states `SYNTHETIC_FIXTURE_ONLY`, `PUBLISHED_PMTILES_NOT_LOADED`, `MAPLIBRE_RUNTIME_UNADMITTED`, `STYLE_HEALTH_NOT_EVALUATED`, `RELEASE_AUTHORIZATION_NOT_EVALUATED`, and `authority: NONE`. A green workflow and uploaded QA artifact do not close those holds.

## Directory Rules basis

Pure app-local builders and browser observation remain under `apps/explorer-web/`; packet validation remains in the existing `tools/validators/pmtiles/` family; executable validator tests remain under `tests/validators/`; orchestration and temporary upload remain under `.github/workflows/`; this reconciliation remains under `docs/intake/exploratory/`; and authoring accountability remains under `data/receipts/generated/`. No release, proof, publication, policy, source, schema, or registry home is created.

## Continuation boundary

Loading a published carrier and evaluating real MapLibre style health require a separately reviewed runtime-admission slice with a released-carrier selector, network and credential posture, pinned MapLibre/PMTiles dependencies, style contract, screenshot-diff budgets, failure semantics, exact artifact identity, and rollback evidence. Those unresolved dependencies are not inferred here.

## Validation and rollback

Validation is the focused TypeScript builder suite, existing mobile verifier suite, full Explorer unit suite and production build, Python packet-validator suite, existing PMTiles fixture suite, strict browser typechecking and discovery, hosted headless packet emission, emitted-packet replay, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; uploaded QA artifacts expire and are not canonical state. No live source, published carrier, style, evidence, policy, release, deployment, publication, or public-use state exists to unwind.
