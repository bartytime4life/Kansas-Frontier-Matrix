<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-30-stac-zarr-asset-metadata-source-map
title: Pass 30 STAC Zarr Asset Metadata Source Adaptation
type: source-adaptation-map
version: v1.0.0
status: proposed; exploratory; review-pending
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; intake; stac; zarr; source-map
[/KFM_META_BLOCK_V2] -->

# Pass 30 STAC Zarr Asset Metadata Source Adaptation

## Source card

- Stable ID: `KFM-P30-PROG-0005`
- Title: `STAC Zarr chunk shim`
- Status in consolidated atlas: active, unchanged
- Source ID: `SRC-P30-001`
- Spec hash: `sha256:582bcdbcde5aeab78adef39af4ddc0c4c47a235f0609b0f303962c367987d25c`
- Drive carrier: `gdrive://1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0005`
- Supplied carrier: `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`

The source proposes a STAC asset metadata shim for chunk shape, array shape, dtype, order, codecs, dimension names, fill value, and store version. It explicitly marks repository implementation status unknown.

## Repository assay

At assayed base `6947a2cbae6e02ce0bacedc74353f8dc3b430774`:

- KFM STAC standards preserve discovery, evidence, policy, review, release, and byte-integrity boundaries.
- `contracts/data/stac_attestation_hook.md` provides an accepted placement precedent for a bounded STAC-related data projection.
- repository search found Zarr documentation and modeled-data references but no indexed `chunk_shape`, `dimension_names`, or `store_version` implementation, matching pull request, or Zarr-named branch.

## Adaptation decision

The smallest dependency-closed slice is a fixture-only declared metadata profile. It checks shape/chunk/dimension consistency and preserves evidence references while explicitly declining store access, asset resolution, byte verification, catalog mutation, policy, promotion, release, and publication.

## Placement

Directory Rules assigns data-object semantic meaning to `contracts/data/`, machine shape to `schemas/contracts/v1/data/`, synthetic examples to `fixtures/`, STAC-oriented validators to `tools/validators/stac/`, tests to `tests/validators/stac/`, and emitted authoring accountability to `data/receipts/generated/`.

## Truth posture

- **CONFIRMED:** source-card identity, statement, status, spec hash, and current repository overlap were inspected.
- **PROPOSED:** the projection vocabulary and accepted STAC/Zarr integration remain pending human steward review.
- **NEEDS VERIFICATION:** live store binding, byte equivalence, media-type/extension registration, schema registry admission, policy integration, and runtime use.
