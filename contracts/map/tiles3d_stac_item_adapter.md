<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/tiles3d-stac-item-adapter
title: 3D Tiles STAC Item Adapter Contract
type: semantic-contract; map-carrier; catalog-adapter; fixture-first
version: v0.1.0
status: proposed; unreleased-candidate-only; no-network; non-publisher
owners: OWNER_TBD — Map steward · Catalog steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; map; stac; tiles3d; integrity; non-authoritative
related:
  - ./tiles3d_tree_hash_manifest.md
  - ../../docs/standards/STAC_KFM_PROFILE.md
  - ../../tools/validators/catalog/README.md
  - ../../schemas/contracts/v1/map/tiles3d_stac_item_adapter_request.schema.json
tags: [kfm, map, 3d-tiles, stac, file-metadata, checksum, adapter]
[/KFM_META_BLOCK_V2] -->

# 3D Tiles STAC Item Adapter Contract

> Convert a validated `Tiles3DTreeHashManifest` plus explicit synthetic/governed metadata into an **unreleased STAC Item candidate** with per-file checksums and 3D Tiles asset roles.

## Source-derived requirement

Pass 31 card `KFM-P31-PROG-0007` calls for a STAC Item adapter for `tileset.json` assets with File-extension checksum metadata and 3D Tiles roles. The prerequisite deterministic tree-hash manifest is already a separate object family. This adapter preserves that separation.

## Inputs

1. A closed `Tiles3DTreeHashManifest`.
2. A `Tiles3DStacItemAdapterRequest` containing item identity, collection, temporal and spatial scope, license, providers, evidence references, run/representation receipt references, and the source commit.
3. A local asset root whose regular-file bytes must match the manifest.

## Output

The output is a STAC 1.0 Item candidate with:

- one asset per manifest entry;
- `file:checksum` and `file:size` copied from the verified manifest;
- roles distinguishing root tileset metadata, subtree data, and content data;
- required KFM evidence, rights, sensitivity, review, release, tree-hash, and manifest-hash properties;
- deterministic provenance links for the manifest, checksum, commit, and derived-from relationship;
- `kfm:review_state=draft` and `kfm:release_state=unreleased`.

## Fail-closed rules

- Manifest `spec_hash`, tree hash, counts, canonical path order, and local bytes must agree.
- Absolute paths, traversal, duplicate paths, symlinks, missing bytes, digest drift, size drift, or authority flags fail.
- Request shape is closed and cannot ask the adapter to release or publish.
- Evidence references and receipts are required inputs; the adapter does not create them.

## Trust boundary

A `PASS` proves deterministic local adaptation and byte binding only. It is not full 3D Tiles conformance, STAC profile adoption, evidence resolution, policy approval, review approval, promotion, release, publication, CDN upload, or public-scene authority. The map artifact remains a downstream carrier.

## Directory Rules basis

Semantic meaning belongs under `contracts/map/`; machine request shape under `schemas/contracts/v1/map/`; executable validation under `tools/validators/map/`; synthetic examples under `fixtures/map/`; tests under `tests/validators/map/`; and hosted orchestration under `.github/workflows/`.

## Rollback

Revert the additive adapter packet. The existing tree-hash manifest family remains unchanged, and no catalog record, release object, tile host, or public scene requires rollback.
