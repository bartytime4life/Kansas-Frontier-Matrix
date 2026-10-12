<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/spatial-foundation/readme
title: Spatial Foundation - Reference Geometry and Versioning Guide
type: domain-readme
version: v0.1
status: draft; repository-grounded; documentation-only; review-required
owners: NEEDS VERIFICATION - domain and documentation stewardship
created: 2026-10-08
created_note: Date of this substantive documentation edition; the tracked path existed earlier.
updated: 2026-10-08
policy_label: repository-facing; cite-or-abstain; no-operational-approval
owning_root: docs/
responsibility: Navigate existing geometry, geography-version, crosswalk, and transformation contracts without creating a parallel schema, policy, or geometry authority.
truth_posture: CONFIRMED pinned repository inventory and source inspection; PROPOSED review-required documentation guide; NEEDS VERIFICATION accountable stewardship and operational acceptance
evidence_snapshot: main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
related:
  - contracts/common/spatial_geometry.md
  - contracts/common/geography_version.md
  - contracts/crosswalks/geography_crosswalk.md
  - contracts/evidence/spatial_transform_receipt.md
  - docs/domains/habitat/sublanes/ecoregions.md
  - docs/domains/fauna/EXPANSION_PLAN.md
[/KFM_META_BLOCK_V2] -->

# Spatial Foundation

Spatial Foundation is the shared documentation entry point for geometry carriers, coordinate references, geography versions, crosswalk declarations and spatial-transformation provenance. It helps domain authors use the existing owning contracts without creating another schema, policy or geometry store under `docs/`.

Start here when a source has coordinates, two datasets use different boundary vintages, a map derivative changes geometry, or an analysis combines place and time. A spatially valid carrier does not prove survey accuracy, legal authority, source admission or public-safe exposure.

## Start with the right object

| Question | Owning source | Bounded meaning |
|---|---|---|
| What geometry, CRS and precision bucket are carried? | [SpatialGeometry](../../../contracts/common/spatial_geometry.md) | Geometry carrier; not a geocoder or CRS transformation engine. |
| Which geography vocabulary and boundary artifact does a result use? | [GeographyVersion](../../../contracts/common/geography_version.md) | Immutable version declaration with version-local identity; no boundary payload. |
| How is one version proposed to map to another? | [GeographyCrosswalk](../../../contracts/crosswalks/geography_crosswalk.md) | Direction-specific mapping declaration; does not execute or prove a join. |
| What transformation was performed? | [SpatialTransformReceipt](../../../contracts/evidence/spatial_transform_receipt.md) | Owning receipt semantics and limits; a reference alone does not verify a transform. |
| Which display uses that geometry? | [Map architecture](../../architecture/map-shell.md) | Renderer and evidence interaction; display is not domain truth. |

The schemas remain in [common](../../../schemas/contracts/v1/common/) and [crosswalk](../../../schemas/contracts/v1/crosswalks/) homes. Domain meaning and source rights remain with their respective owners.

## What the current source establishes

At `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`, SpatialGeometry has a bounded no-network validator for Point, MultiPoint, LineString, MultiLineString, Polygon and MultiPolygon carriers, explicit EPSG identifiers, consistent position dimensionality, simple rings and EPSG:4326 coordinate bounds. That scope does not repair geometry, resolve registry authority, transform a CRS or certify survey accuracy.

GeographyVersion and GeographyCrosswalk are proposed, inactive, fixture-only profiles. Their deterministic identities and closed declarations are useful implementation building blocks; fixture success does not approve a real geography source or cross-version analysis.

A crosswalk is forward and version-specific. `EXACT`, `SPLIT`, `MERGE`, `PARTIAL_OVERLAP` and `UNMAPPED` describe declared relationships. Do not infer a reverse mapping or manufacture matches for unsupported rows.

## Work a spatial question

1. Record the source edition, feature identity, geometry type, CRS, units, source scale and any vertical/depth datum.
2. Separate observation time, valid interval, source publication, retrieval and transformation time.
3. Identify whether the geometry is original, generalized, derived, modeled or synthetic.
4. Validate the supported carrier profile with its actual schema and validator. Record unsupported geometry or CRS conditions explicitly.
5. For a cross-version join, pin both geography versions and the reviewed method/crosswalk. Shared names or codes alone do not establish stable identity.
6. Preserve unmatched and partially supported rows. Check that an aggregate still describes its declared area and time.
7. Carry provenance and sensitivity through maps, exports, API responses and reports; route public eligibility through the owning policy/evidence/release process.

Example: county statistics from different boundary vintages should first bind each result to its own GeographyVersion. A proposed allocation needs an explicitly reviewed crosswalk and method. This is an analytical planning example, not an approved dataset or computed result.

## Domain relationships

[Habitat ecoregions](../habitat/sublanes/ecoregions.md) use reference geometry and scale support without redefining them. [Fauna planning](../fauna/EXPANSION_PLAN.md) depends on qualified reference geometry and sensitivity-preserving transformations. The underground viewer must preserve each borehole's depth reference rather than invent a shared elevation datum; see [Underground Explorer](../../../apps/site/source/docs/underground-explorer.md).

A basemap is display context. Tile retrieval time, zoom and screen resolution do not establish acquisition date, additional measurements or a new authority over domain records.

## Validation and maintenance

Read the [spatial validator](../../../tools/validators/validate_spatial_geometry.py), [geography-version validator](../../../tools/validators/validate_geography_version.py) and [crosswalk validator](../../../tools/validators/validate_geography_crosswalk.py) alongside their contract fixtures before selecting a check. This documentation edition records source inspection, not a fresh test run or provider exercise.

Re-review when supported geometry/CRS behavior, version identity, crosswalk semantics, transformation receipts or consumer boundaries change. Unresolved stewardship, real-data review, runtime integration and public-use acceptance stay explicit. Reverting this page restores explanation only; it does not undo a transformation or join.
