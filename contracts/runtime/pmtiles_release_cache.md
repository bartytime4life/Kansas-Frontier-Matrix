<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/pmtiles-release-cache
title: Release-Scoped PMTiles Cache Policy Projection
type: runtime-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-service-worker-side-effects
updated: 2026-08-08
owning_root: contracts/
related:
  - ../../apps/explorer-web/src/features/map_runtime/pmtiles_release_cache.ts
  - ../../fixtures/runtime/pmtiles_release_cache/cases.json
  - ../../apps/explorer-web/tests/pmtiles-release-cache.test.ts
[/KFM_META_BLOCK_V2] -->

# Release-Scoped PMTiles Cache Policy Projection

This no-network slice implements the first enforceable portion of MapLibre atlas idea `ML-Y-114`: release-scoped cache keys and fixtures for first run, offline miss, partial download, stale release, policy mismatch, artifact mismatch, missing glyphs/sprites, withdrawal, and denied internal-source paths.

The cache key binds release identity, PMTiles artifact digest, and policy digest. An old archive cannot be reused merely because its URL or layer ID matches.

## Boundary

The evaluator plans a future Service Worker decision. It does not call `fetch`, `CacheStorage`, MapLibre, source systems, canonical stores, or publication services. A `PASS` with `PMTILES_CACHE_FETCH_REQUIRED` authorizes no network request; it only identifies what a later governed worker would need to do.

## Directory Rules basis

Runtime meaning stays under `contracts/runtime/`; app behavior under `apps/explorer-web/`; synthetic cases under `fixtures/runtime/`; tests under the app lane; CI under `.github/workflows/`; authoring accountability under `data/receipts/generated/`.

## Rollback

Revert the additive packet. No browser cache, release alias, artifact, or public state is mutated.
