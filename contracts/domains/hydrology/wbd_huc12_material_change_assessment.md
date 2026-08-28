# WBD HUC12 Material Change Assessment

**Status:** PROPOSED fixture profile  
**Domain:** Hydrology  
**Source basis:** *New Ideas 4-10-26.pdf* — Kansas WBD HUC12 access, geometry normalization, geometry/area fingerprints, metadata-churn suppression, and ADD/REMOVE/REAL CHANGE classifications  
**Directory Rules basis:** hydrology meaning belongs under `contracts/domains/hydrology/`; shape under `schemas/contracts/v1/domains/hydrology/`; validator under `tools/validators/domains/hydrology/`.

## Purpose

Define a deterministic, no-network assessment that distinguishes a meaningful WBD HUC12 feature change from upstream metadata churn. The validator normalizes Polygon/MultiPolygon geometry, rounds coordinates, canonicalizes ring rotation and direction, sorts holes and polygons, rounds `areasqkm`, and computes a SHA-256 feature fingerprint.

The assessment is downstream of the existing WBD HUC12 source descriptor. It does not fetch the USGS service, activate a connector, write RAW/WORK/PROCESSED state, promote a candidate, or publish a boundary.

## Fingerprint basis

The feature fingerprint includes only:

```json
{
  "geometry": "canonical GeoJSON geometry",
  "areasqkm": "rounded to six decimals"
}
```

`load_date`, `last_edit_date`, request headers, retrieval time, and other source metadata are retained for traceability but excluded from feature identity. A metadata-only update therefore remains `NO_CHANGE`.

## Geometry normalization

- input CRS is fixed to `EPSG:4326`;
- coordinate precision is six or seven decimal places;
- each ring is closed and contains at least three distinct vertices;
- ring starting point and direction are normalized by lexicographic minimum;
- interior rings and MultiPolygon members are sorted deterministically;
- longitude and latitude ranges are validated.

## Finite outcomes

| Outcome | Exact change types |
|---|---|
| `NO_CHANGE` | `[]` |
| `MATERIAL_CHANGE` | one or both of `area_change`, `geometry_change` |
| `ADD` | `added` |
| `REMOVE` | `removed` |

The validator recomputes every snapshot fingerprint and the exact decision. `spec_hash` covers the full assessment with only the top-level `spec_hash` omitted.

## Validation and rollback

```bash
python -m pytest tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py -q
python tools/validators/domains/hydrology/wbd_huc12_material_change/validate_wbd_huc12_material_change.py \
  fixtures/domains/hydrology/wbd_huc12_material_change/valid/metadata_churn_no_change.json
```

Rollback is ordinary Git reversion. The slice is fixture-only and does not alter the existing source descriptor, pipeline spec, connector, catalog, or published layer.
