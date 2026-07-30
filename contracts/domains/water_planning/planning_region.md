<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-planning-region
title: PlanningRegion Contract — Water Planning
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-scaffold; reference-authority checks implemented; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Water Planning domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
created: 2026-07-28
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json
  - ../../../fixtures/domains/water_planning/planning_region/
  - ../../../fixtures/domains/water_planning/geometry_authority/
  - ../../../tools/validators/domains/water_planning/validate_geometry_authority.py
  - ../../../tests/domains/water_planning/test_geometry_authority.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../data/registry/crosswalks/README.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# PlanningRegion Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/planning_region.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/planning_region/`
> **Authority checks:** `tools/validators/domains/water_planning/validate_geometry_authority.py`

## Meaning

A Kansas Regional Advisory Committee (RAC) planning-area identity. The Kansas Water Office source identifies exactly 14 RAC names. KFM assigns `kwo-rac-01` through `kwo-rac-14` in the frozen lexicographic order of that source-grounded name inventory. The ordinal is a KFM identity convention, not a claim that KWO publishes native RAC numbers.

The KWO page exposes no source-native version. The identity inventory therefore records that unversioned-page posture and an observation date, then pins its normalized authority metadata plus ordered ID/ordinal/name tuples with a KFM record version and digest. The digest is not represented as a digest of remote page bytes. Each `PlanningRegion.source_ref` resolves to that one identity-authority record. A later correction must create explicit correction or supersession lineage; it must not silently renumber identities.

## Authority and resolution rules

- Exactly 14 unique IDs and ordinals exist: `kwo-rac-01` through `kwo-rac-14` and 1 through 14.
- `region_id` and `rac_number` correspond exactly. Values `00`, `15`, `99`, gaps, duplicates, mismatches, and foreign namespaces fail.
- RAC, groundwater-management-district, county, municipality, venue, and project-location identities remain distinct. A GMD reference cannot satisfy a RAC reference.
- `geometry_confidence: unresolved` requires `geometry_ref: null`.
- `approximate` and `confirmed` each require a non-inline reference to a declared region-geometry authority record with version, digest, correction posture, and use boundary.
- `county_crosswalk_resolution_status: unresolved` requires `county_crosswalk_ref: null`.
- A resolved county crosswalk is reference-only and must resolve to a declared authority record. County membership is not embedded or invented here.
- Geometry, GeoJSON, coordinates, polygons, centroids, addresses, and inferred containment are not valid `PlanningRegion` payload fields.

The canonical registry now contains one source-grounded KWO RAC geometry
dataset version and one derived Census 2025 county-intersection crosswalk.
Resolved region records may reference
`kfm:dataset-version:water-planning:kwo-rac-regions:2026-06-24` and
`kfm:crosswalk:water-planning:kwo-rac-to-county:2026-06-24:tiger-2025`
through their governing authority records. The original synthetic authority
fixtures remain test-only and do not override those canonical records.

The county crosswalk records positive-area geometry overlap, not county
membership. A `boundary-sliver` must not be silently promoted to a political,
administrative, funding, or governance relationship.

## Anti-collapse boundaries

- A planning region is not a meeting, grant award, GMD, county, municipality, venue, or project.
- A region identity is not region geometry.
- A county crosswalk is not substitute geometry.
- Link presence or source-page prose is not geometry proof.
- A passing schema or validator is not source admission, proof, release, or publication.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/planning_region.schema.json` |
| Schema status | `PROPOSED` |
| Exact RAC ID pattern | `^kwo-rac-(0[1-9]\|1[0-4])$` |
| Geometry coherence | Enforced by schema shape and reference-authority validator |
| County-crosswalk coherence | Enforced by schema shape and reference-authority validator |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/planning_region.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) — Schema
- [`fixtures/domains/water_planning/geometry_authority/`](../../../fixtures/domains/water_planning/geometry_authority/) — Synthetic authority fixtures
- [`tools/validators/domains/water_planning/validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) — Deterministic checker
- [`tests/domains/water_planning/test_geometry_authority.py`](../../../tests/domains/water_planning/test_geometry_authority.py) — No-network tests
