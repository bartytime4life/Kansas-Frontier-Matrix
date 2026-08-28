<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-map-map-release-manifest-readme
title: MapReleaseManifest Compatibility Pointer
type: readme
version: v0.2
status: compatibility
owners: ["@bartytime4life"]
created: 2026-06-24
updated: 2026-08-07
policy_label: public
related:
  - ../../release/map_release_manifest.md
  - ../../../schemas/contracts/v1/map/map_release_manifest.schema.json
  - ../../../tools/validators/map/validate_map_release_manifest.py
  - ../../../fixtures/contracts/v1/map/map_release_manifest/
  - ../../../tests/map/test_map_release_manifest.py
tags: [kfm, map, release, compatibility, no-parallel-authority]
notes:
  - "This path is a compatibility pointer, not a second semantic or release authority."
[/KFM_META_BLOCK_V2] -->

# `contracts/map/map_release_manifest/`

This folder is a compatibility and navigation surface for `MapReleaseManifest`.

The **canonical semantic contract** is [`../../release/map_release_manifest.md`](../../release/map_release_manifest.md). The existing map schema family owns the machine shape at [`../../../schemas/contracts/v1/map/map_release_manifest.schema.json`](../../../schemas/contracts/v1/map/map_release_manifest.schema.json).

## Authority boundary

This compatibility path does not own:

- release approval, promotion, correction, withdrawal, or rollback;
- JSON Schema;
- policy or review decisions;
- evidence or proof bundles;
- map artifacts, styles, tiles, sprites, glyphs, or runtime state;
- API, UI, MapLibre, or AI behavior.

Do not add a second `map_release_manifest.md` or schema here. A future move or rename requires a PathDecisionRecord, migration note, consumer audit, and rollback.

## Current machine-backed profile

The current fixture profile includes:

- strict Draft 2020-12 shape;
- deterministic SHA-256 identity;
- valid candidate, held, published, generalized, superseded, withdrawn, and rolled-back examples;
- reviewed negative fixtures;
- a no-network validator and tests;
- read-only CI and generated authoring receipt.

The profile remains `PROPOSED_INACTIVE`. It validates synthetic closure only and creates no release or publication authority.

## Rollback

Restore the prior compatibility README if the canonical semantic contract or schema location changes through a later accepted decision. Existing map artifacts and releases are unaffected.
