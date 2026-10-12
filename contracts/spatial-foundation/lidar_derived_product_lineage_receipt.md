<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/spatial-foundation/lidar-derived-product-lineage-receipt
title: LiDAR Derived Product Lineage Receipt Contract
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED_INACTIVE; fixture-only; non-authoritative
owners: OWNER_TBD — Spatial foundation steward · Source steward · Contracts steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; contracts; spatial-foundation; lidar; lineage; non-authoritative
owning_root: contracts/
responsibility: Define fixture-only LiDAR source-capture, access-carrier, and modeled-derivative lineage semantics without creating source, lifecycle, policy, or release authority.
truth_posture: "CONFIRMED repository dependencies; PROPOSED inactive contract; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ./README.md
  - ../../schemas/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt.schema.json
  - ../../fixtures/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt/cases.json
  - ../../tools/validators/validate_lidar_derived_product_lineage_receipt.py
  - ../../tests/validators/test_validate_lidar_derived_product_lineage_receipt.py
  - ../../docs/sources/catalog/usgs/3dep-elevation.md
  - ../../docs/intake/exploratory/pass-30-lidar-derived-product-lineage-source-map.md
notes:
  - "Adapts the proposal in KFM-P30-PROG-0028 after current-repository reconciliation."
  - "Fixtures contain opaque references and hashes only; they contain no real point cloud, raster, geometry, coordinate, or live source URL."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `LidarDerivedProductLineageReceipt`

> A fixture-only, source-role-aware receipt that binds a LiDAR source capture to analytic access carriers and modeled elevation or terrain derivatives without changing source, policy, lifecycle, or release state.

## Purpose

The current 3DEP source documentation describes a heterogeneous chain:

- LAZ is the observed source capture;
- EPT and COPC are observation-preserving analytic access carriers derived from LAZ;
- DEM is a modeled elevation derivative; and
- terrain products are modeled derivatives of DEM or another declared modeled step.

This contract makes that chain reviewable as one deterministic directed acyclic graph. It records artifact identity, parent links, transform receipts, acquisition context, horizontal and vertical reference context, and the exact anti-collapse limitations carried by every node.

## Directory Rules basis

Cross-domain spatial representation, geometry lineage, reference systems, and fitness-for-use already belong to `contracts/spatial-foundation/`. The companion schema, synthetic fixtures, validator, tests, hosted check, source map, and generated authoring receipt use their existing responsibility roots. This packet creates no new root, source registry, catalog, proof store, lifecycle state, or release lane.

## Two-axis role model

`source_role` and `product_role` answer different questions and must not be collapsed.

| Product kind | `source_role` | `product_role` | Required meaning |
|---|---|---|---|
| `LAZ` | `OBSERVED` | `SOURCE_CAPTURE` | Immutable captured returns for this lineage graph. |
| `COPC` / `EPT` | `OBSERVED` | `ANALYTIC_ACCESS_CARRIER` | A derived carrier of the captured returns, not a new observation and not a replacement source capture. |
| `DEM` | `MODELED` | `ELEVATION_MODEL` | An interpolated or gridded surface with modeled semantics. |
| `TERRAIN` | `MODELED` | `TERRAIN_DERIVATIVE` | A modeled downstream terrain product. |

The receipt never promotes a carrier or model to stronger source authority. A DEM cannot claim point-cloud substitution, and a terrain derivative cannot claim to be observed elevation.

## Lineage closure

A conforming receipt has exactly one LAZ root and at least one derived node. Products are in canonical topological order. Every non-root node:

- names one or more earlier parents;
- names at least one transform receipt;
- resolves transitively to the LAZ root; and
- preserves the LAZ acquisition window, quality level, horizontal CRS reference, vertical datum, geoid-model reference, and vertical units in this initial profile.

Cross-datum, cross-unit, or cross-CRS products are intentionally deferred. A future profile may admit them only with explicit transform semantics and independent fixtures; this profile fails them closed.

## Deterministic identity

The receipt uses the repository RFC 8785 JCS plus SHA-256 implementation. `lineage_id` and `spec_hash` are recomputed from the complete document projection after removing those two identity fields. Array order is semantic and canonical:

- products are ordered by stable `node_id` and must also be topological;
- parent, transform, evidence, and leaf-reference arrays are sorted and unique.

Artifact hashes identify declared artifacts. They do not prove the bytes were fetched, admitted, validated, released, or published.

## Validation boundary

The offline validator checks closed schema shape, deterministic identity, role mapping, one-root topology, parent closure, LAZ ancestry, transform references, acquisition and spatial-reference preservation, leaf/edge summary projection, canonical ordering, and no-authority claims.

A passing fixture does not:

- fetch or inspect LAZ, EPT, COPC, DEM, or terrain bytes;
- verify an external source, source descriptor, transform, datum, CRS, quality level, or artifact hash;
- admit data to RAW or any later lifecycle state;
- establish engineering, surveying, legal-boundary, policy, promotion, release, deployment, publication, or public-use authority; or
- write repository, catalog, lifecycle, or public state.

## Correction and rollback

The slice is additive and fixture-only. Before merge, close the draft pull request and delete its feature branch. After merge, revert the bounded commit or merge commit. No data migration, source shutdown, cache purge, deployment rollback, or public correction is required because the packet creates no live or published state.

<p align="right"><a href="#top">Back to top</a></p>
