# RAC geometry and county-crosswalk registry contract

Status: **PROPOSED, source-grounded, not released**

This contract defines the first concrete Kansas Regional Advisory Committee
(RAC) geometry dataset record and the derived RAC-to-county crosswalk record.
The records live in the existing canonical subtype-first registry lanes:

- `data/registry/datasets/water_planning/`
- `data/registry/crosswalks/water_planning/`

Geometry bytes live separately under
`data/processed/water_planning/rac_regions/`. Registry placement does not
release or publish the geometry.

## Authorities

The region geometry authority is the Kansas Water Office ArcGIS Feature
Service item `cd87ef7a0bb34cc4a7f57e662d73ec0f`, layer `0`, modified
`2026-06-24T15:17:37Z`. The source exposes exactly the 14 official planning
area names already pinned by the RAC identity inventory.

The county geometry authority is the U.S. Census Bureau TIGERweb
`State_County/MapServer/1` Counties layer, January 1, 2025 vintage, filtered
to Kansas (`STATE='20'`).

Both source responses are digest-pinned in the registry records. The source
URLs remain mutable; a later source edit requires a new observation, digest,
validation run, and either a new version or an explicit correction.

The paired SourceDescriptor candidates live under
`data/registry/sources/water_planning/`. They remain `needs_review`,
`proposed`, and `not_released`, with connector activation `disabled`.

## Geometry record

The dataset registry record identifies one normalized GeoJSON
`FeatureCollection`. It must:

- contain exactly 14 `Polygon` or `MultiPolygon` features;
- use `OGC:CRS84` longitude/latitude coordinates;
- preserve the source coordinates without simplification;
- order features by `kwo-rac-01` through `kwo-rac-14`;
- project only the stable KFM identity and source feature ID, name, and
  abbreviation into feature properties;
- pin path, byte count, SHA-256 digest, source observation, source version,
  rights-review posture, sensitivity posture, and correction state.

`record_status: current` means this is the current internal registry pointer
for this observed source version. `release_status: not-released` remains an
independent, fail-closed publication gate.

## County crosswalk

The crosswalk is a deterministic geometry derivative, not an official KWO
county-membership list. Each row represents positive-area intersection
between one 2025 Census county polygon and one KWO planning-area polygon.
Line and point touches are excluded.

Areas are calculated after projecting both inputs to `EPSG:5070`. A row is
retained only when its intersection is at least 10,000 square metres and at
least one millionth of the county area. Retained rows are classified by
county-area share:

| Class | Rule | Meaning |
|---|---:|---|
| `dominant` | share ≥ `0.999` | One region covers at least 99.9% of the county geometry |
| `material-partial` | `0.001` ≤ share < `0.999` | Material partial-county overlap |
| `boundary-sliver` | share < `0.001` | Small measured edge overlap retained for audit |

These classes describe geometry only. They do not assert political,
administrative, advisory, funding, or governance membership. Consumers that
need a binary county list must define and review their own materiality rule;
they must not silently coerce `boundary-sliver` into membership.

Each mapping carries county and region references, both area shares, the
intersection area, and the overlap class. The record pins the complete ordered
mapping array with `mapping_digest`.

## Validation and correction

The no-network validator at
`tools/validators/domains/water_planning/validate_rac_registry.py` verifies:

- dataset, geometry, and crosswalk reference agreement;
- exact 14-region identity and 105-county coverage;
- payload and mapping digests;
- deterministic ordering and duplicate denial;
- coordinate, area-share, overlap-class, source, version, release, and
  correction constraints.

The validator does not refetch either source and does not independently
recompute intersections. Source refresh and spatial derivation are separate,
receipted operations.

A correction or source refresh must preserve the prior digest and version,
create or identify the successor, update forward/backward lineage, rerun the
same deterministic checks, and separately review any downstream release.
