# `schemas/contracts/v1/map/` — Map Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-map-readme
title: Map Schema Family Index
type: schema-family-index
version: v0.2
status: draft
owners: ["@bartytime4life"]
created: 2026-07-04
updated: 2026-08-07
policy_label: public
related:
  - ./layer_manifest.schema.json
  - ./style_manifest.schema.json
  - ./tile_artifact_manifest.schema.json
  - ./map_release_manifest.schema.json
  - ../../../../contracts/release/map_release_manifest.md
  - ../../../../contracts/map/map_release_manifest/README.md
tags: [kfm, schemas, map, maplibre, release, no-parallel-authority]
notes:
  - "MapReleaseManifest is machine-backed; the remaining listed map schemas retain their separately verified maturity."
[/KFM_META_BLOCK_V2] -->

`schemas/contracts/v1/map/` owns map-facing machine shapes. It does not own semantic meaning, policy, release decisions, map artifacts, runtime code, evidence, or publication state.

## Current inventory

| Schema | Current posture |
|---|---|
| `layer_manifest.schema.json` | PROPOSED scaffold; overlaps the shared `layers/` family and remains NEEDS VERIFICATION. |
| `style_manifest.schema.json` | PROPOSED scaffold. |
| `tile_artifact_manifest.schema.json` | PROPOSED scaffold; describes artifacts but stores none. |
| `map_release_manifest.schema.json` | **PROPOSED machine-backed fixture profile** paired with `contracts/release/map_release_manifest.md`, fixtures, validator, tests, and read-only CI. |

## MapReleaseManifest authority split

- semantic contract: `contracts/release/map_release_manifest.md`;
- compatibility pointer: `contracts/map/map_release_manifest/README.md`;
- machine shape: this folder;
- validator: `tools/validators/map/validate_map_release_manifest.py`;
- fixtures: `fixtures/contracts/v1/map/map_release_manifest/`;
- tests: `tests/map/test_map_release_manifest.py`;
- release decisions and emitted records: release-governed roots;
- policy and review: separate policy/decision/review families.

The machine-backed fixture profile does not authorize release, load artifacts, evaluate policy, resolve evidence, invalidate caches, execute rollback, or publish.

## Promotion boundary

A map schema may support public clients only after semantic, evidence, policy, rights, sensitivity, review, attestation, release, correction, and rollback closure are independently verified. Schema success alone is not public-safety or release proof.

## Map-vs-layers overlap

The current map and shared layers families both contain layer-manifest surfaces. This update does not resolve that overlap. Do not duplicate, move, alias, or deprecate those schemas without a PathDecisionRecord and migration decision.

## Rollback

Revert the MapReleaseManifest profile change to restore the permissive scaffold. Other map-family schemas and runtime behavior are unaffected.
