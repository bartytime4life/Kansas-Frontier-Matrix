<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/layer-manifest-admission
title: LayerManifest Runtime Admission Projection
type: runtime-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-registry-mutation
updated: 2026-08-08
owning_root: contracts/
related:
  - ../data/layer_manifest.md
  - ../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts
  - ../../fixtures/runtime/layer_manifest_admission/cases.json
  - ../../apps/explorer-web/tests/layer-manifest-admission.test.ts
[/KFM_META_BLOCK_V2] -->

# LayerManifest Runtime Admission Projection

The existing LayerManifest contract explicitly records that live registry integration and a runtime loader are absent. This slice adds a no-network admission projection that proves the denial boundary before any MapLibre or registry integration.

A `PASS` means only that a synthetic, released runtime projection is **eligible** for a later governed loader. The evaluator never mutates a registry and never creates a MapLibre source.

## Fail-closed rules

Legacy and inactive profiles, candidate lifecycle state, stale trust state, withdrawn or superseded releases, unresolved evidence, policy denial, mismatched release subjects, direct canonical/internal source classes, and authority overclaims return finite `HOLD`, `DENY`, or `ERROR` results.

## Directory Rules basis

Runtime semantics belong in `contracts/runtime/`; Explorer behavior under `apps/explorer-web/`; synthetic cases under `fixtures/runtime/`; tests under the app test lane; read-only orchestration under `.github/workflows/`; authoring accountability under `data/receipts/generated/`.

## Non-effects

This fixture does not resolve real references, authenticate reviewers, execute policy, verify actual artifacts or signatures, register a layer, read lifecycle stores, authorize release, deploy, publish, or permit public use.

## Rollback

Revert the additive packet. No registry, public artifact, cache, release, or lifecycle state is modified.
