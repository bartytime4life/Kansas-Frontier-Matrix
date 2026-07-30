# Water-planning dataset registry

This canonical registry child contains machine-readable identity and state
records for water-planning datasets. It does not contain dataset payloads and
is not a public-serving surface.

## Concrete inventory

| Record | Payload | Status |
|---|---|---|
| `kwo_rac_regions_2026-06-24.json` | `data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson` | Current internal registry record; not released |

The record is governed by
`contracts/domains/water_planning/rac_geometry_registry.md` and
`schemas/contracts/v1/domains/water_planning/rac_geometry_dataset_registry.schema.json`.
Its payload digest, source-response digest, and source descriptor reference are
mandatory.

Adding a record here does not admit another source, prove a claim, clear
rights, or authorize release.
