<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/tiles3d-tree-hash-manifest
title: 3D Tiles Tree Hash Manifest Contract
type: semantic-contract; map-integrity; fixture-first; no-network
version: v0.1.0
status: proposed; candidate-integrity-only; non-release
owners: OWNER_TBD — Map artifact steward · Validation steward · Release steward · Security reviewer
created: 2026-08-08
updated: 2026-08-08
policy_label: public; map; tiles3d; integrity; derived-stays-derived; non-release
related:
  - ../release/tile_artifact_manifest.md
  - ../../schemas/contracts/v1/map/tiles3d_tree_hash_manifest.schema.json
  - ../../tools/validators/map/tiles3d_tree_hash_manifest/build_tiles3d_tree_hash_manifest.py
  - ../../fixtures/map/tiles3d_tree_hash_manifest/
  - ../../docs/architecture/planetary-3d.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, map, 3d-tiles, tree-hash, checksum, integrity, deterministic, fixture-first]
[/KFM_META_BLOCK_V2] -->

# 3D Tiles Tree Hash Manifest Contract

> `Tiles3DTreeHashManifest` is a deterministic inventory and byte-integrity report for one local 3D Tiles directory. It is a candidate validation artifact that may later be referenced by `TileArtifactManifest`; it is not a `TileArtifactManifest`, proof pack, attestation, promotion decision, release manifest, or publication record.

## Source-derived requirement

Pass 31 proposes digest-immutable 3D Tiles publication and a sorted-path SHA-256 tree-hash builder with per-file checksums. This slice implements the deterministic, no-network integrity primitive only. It deliberately stops before STAC registration, signing, source admission, policy, promotion, release, serving, or UI dashboards.

## Responsibility split

| Responsibility | Home |
|---|---|
| Manifest semantics | `contracts/map/tiles3d_tree_hash_manifest.md` |
| Machine shape | `schemas/contracts/v1/map/tiles3d_tree_hash_manifest.schema.json` |
| Builder/verifier | `tools/validators/map/tiles3d_tree_hash_manifest/` |
| Synthetic trees and expected reports | `fixtures/map/tiles3d_tree_hash_manifest/` |
| Focused tests | `tests/validators/map/tiles3d_tree_hash_manifest/` |
| Release-facing tile artifact meaning | `contracts/release/tile_artifact_manifest.md` |

This follows the repository's existing map assessment pattern. The new object is a validation report and does not resolve the open canonical schema-home question for `TileArtifactManifest`.

## Canonical algorithm

1. Require a regular, non-symlink root directory containing `tileset.json`.
2. Walk regular non-symlink files only, bounded by file-count and byte budgets.
3. Convert paths to canonical POSIX paths relative to the tree root.
4. Sort entries by path.
5. Record `path`, `byte_size`, `sha256`, `media_type`, and a coarse `role` (`tileset`, `subtree`, or `content`).
6. Compute `tree_hash` as SHA-256 over RFC 8785 canonical JSON of the sorted `files` array.
7. Compute top-level `spec_hash` over the manifest with only `spec_hash` omitted.

The algorithm is deterministic and timestamp-free. It hashes exact bytes; it does not claim semantic equality, 3D Tiles conformance, feature-semantic correctness, public safety, or release readiness.

## Required boundaries

- Symlinked roots, files, or directories are denied.
- File and aggregate byte limits fail closed.
- `tileset.json` must be valid UTF-8 JSON with an `asset.version` string.
- Every listed file is bound to an exact SHA-256 digest and size.
- Verification recomputes the tree and requires exact manifest equality.
- `governance` fields remain false/null; the report grants no release or public authority.

## Relationship to release objects

A future candidate `TileArtifactManifest` may cite this report through an integrity or attestation reference. That future binding requires its own accepted contract/schema/policy/release work. A passing tree hash cannot authorize publication, prove source rights, resolve EvidenceBundle support, or make 3D content authoritative.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive contract/schema/tool/fixture/test/workflow packet. No released artifact, cache, public route, renderer, or lifecycle object is modified.
