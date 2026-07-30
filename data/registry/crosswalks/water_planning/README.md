# Water-planning crosswalk registry

This canonical registry child contains compact water-planning mapping-state
records. It is not a geometry payload lane or a public-serving surface.

## Concrete inventory

| Record | Mapping | Status |
|---|---|---|
| `kwo_rac_counties_2026-06-24__tiger2025.json` | KWO 2026-06-24 RAC geometry × Census 2025 Kansas counties | Current derived registry record; not released |

The crosswalk is computed from polygon intersections. It is not an official
KWO county-membership list. `dominant`, `material-partial`, and
`boundary-sliver` describe measured county-area share only.

The record is governed by
`contracts/domains/water_planning/rac_geometry_registry.md` and
`schemas/contracts/v1/domains/water_planning/rac_county_crosswalk_registry.schema.json`.
The no-network validator pins its source descriptor references and complete
ordered mapping array by digest.
