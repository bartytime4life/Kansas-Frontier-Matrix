<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/stac-zarr-asset-metadata-profile
title: STAC Zarr Asset Metadata Profile Candidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · Catalog steward · STAC steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; data; stac; zarr; metadata-projection; no-network; non-release
source_card: KFM-P30-PROG-0005
source_spec_hash: sha256:582bcdbcde5aeab78adef39af4ddc0c4c47a235f0609b0f303962c367987d25c
related:
  - ./stac_attestation_hook.md
  - ../../docs/standards/STAC_KFM_PROFILE.md
  - ../../schemas/contracts/v1/data/stac_zarr_asset_metadata_profile.schema.json
  - ../../fixtures/contracts/v1/data/stac_zarr_asset_metadata_profile/cases.json
  - ../../tools/validators/stac/validate_stac_zarr_asset_metadata_profile.py
  - ../../tests/validators/stac/test_stac_zarr_asset_metadata_profile.py
tags: [kfm, stac, zarr, chunk-shape, dtype, codecs, dimensions, fixture]
[/KFM_META_BLOCK_V2] -->

# STAC Zarr Asset Metadata Profile Candidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile projects declared Zarr array metadata beside one synthetic STAC asset identity. It does not validate a complete STAC Item, access a Zarr store, resolve an asset, verify bytes, mutate catalog state, evaluate policy, promote, release, or publish.

## Source-derived gap

Pass 30 card `KFM-P30-PROG-0005` calls for a STAC asset metadata shim carrying `chunk_shape`, `shape`, `dtype`, `order`, `codecs`, `dimension_names`, `fill_value`, and `store_version`. Current repository STAC surfaces define discovery, trust, and attestation boundaries but do not expose this exact closed Zarr metadata projection.

## Directory Rules basis

The profile defines metadata for a governed data asset, so semantic meaning belongs under `contracts/data/`. Its machine shape belongs under `schemas/contracts/v1/data/`; fixture records under `fixtures/contracts/v1/data/`; STAC-oriented validation under `tools/validators/stac/`; and tests under `tests/validators/stac/`. Actual arrays remain in lifecycle data stores, and catalog records remain under catalog responsibility roots.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `stac` | Declared STAC version, collection, item, asset key, fixture-only asset reference, media type, and roles. | The profile requires the `data` role and denies live asset references. |
| `zarr.shape` | Declared logical array extent per dimension. | Rank must match chunks and dimension names. |
| `zarr.chunk_shape` | Declared chunk extent per dimension. | Every chunk dimension must be positive and no larger than the matching array dimension. |
| `zarr.dimension_names` | Ordered semantic dimension names. | Names are unique and rank-preserving; order is semantic. |
| `zarr.dtype` / `order` | Declared data type and memory-order metadata. | Shape validation does not assert that store bytes match the declaration. |
| `zarr.codecs` | Ordered codec pipeline with fixture configuration references. | Codec names cannot repeat; the profile does not execute codecs. |
| `zarr.fill_value` / `nodata_semantics` | Declared fill and missing-data posture. | No scientific or rendering interpretation is inferred. |
| `provenance` | Source descriptor, evidence references, method, declaration time, and `DECLARED_NOT_VERIFIED` status. | Evidence is referenced but not resolved or authenticated. |
| `controls` | Fixed non-effect flags. | Store access, asset resolution, byte verification, catalog mutation, policy, review, promotion, release, and publication remain false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the entire record after removing `profile_id` and `spec_hash`. `profile_id` is `kfm:stac-zarr-asset-metadata:` plus the first 24 hexadecimal digest characters. Asset roles and evidence references are sorted and duplicate-free; dimension and codec order remain semantic.

## Compatibility boundary

This object is an additive projection, not a STAC extension registration or a replacement for the current KFM STAC profile. It accepts declared STAC `1.0.0` or `1.1.0` version posture without claiming that the surrounding Item has been validated. A future integration must bind this declaration to verified asset bytes, an accepted extension vocabulary, evidence resolution, policy, review, and release state before any public use.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/stac \
  --pattern 'test_stac_zarr_asset_metadata_profile.py' \
  --verbose

python tools/validators/stac/validate_stac_zarr_asset_metadata_profile.py --fixtures
```

A passing result proves only declared fixture shape, rank and chunk consistency, reference ordering, fixed non-authority flags, and deterministic identity.

## Rollback

Revert this additive packet. It creates no Zarr store access, catalog mutation, lifecycle transition, release, or published artifact.
