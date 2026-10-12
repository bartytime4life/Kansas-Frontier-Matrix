# Geospatial carrier readiness — mined implementation source map

Status: `PROPOSED` / implementation adaptation record.

This slice was mined from three existing KFM standards references whose KFM-specific implementation posture remained documentary:

- `docs/standards/COG.md`
- `docs/standards/MVT.md`
- `docs/standards/GEOPARQUET.md`

The common missing capability was not another file-format writer. It was a deterministic, fixture-first boundary that lets reviewers distinguish a declared carrier that is ready for deeper binary validation from a declaration that must be held or rejected before release work proceeds.

## Adapted ideas

### COG

Adapted: internal tiling, block layout, overviews, explicit raster metadata, Range-read posture, and STAC Raster/Projection bindings.

Deferred: opening TIFF bytes, `rio-cogeo`, `gdalinfo`, actual CORS/HTTP Range testing, STAC dereference, signatures, evidence closure, and release.

### MVT

Adapted: v2.x + extent, source-layer contract, attribute whitelist, stable feature IDs, `source_ref`, tile budget, zero silent geometry drops, area-drift gate, tiler-parameter pinning, and PMTiles public-container default.

Deferred: Protobuf decode, Tippecanoe/Tegola execution, actual tile-size scans, geometry comparison, PMTiles byte inspection, MapLibre rendering, policy, and release.

### GeoParquet

Adapted: GeoParquet 1.1.0 adoption, `.parquet`, WKB, explicit PROJJSON CRS, root geometry, stable row grouping/order, null-only missing values, forward-compatible metadata handling, numeric-unit coverage, and bbox-covering advisory.

Deferred: Parquet footer/metadata decode, geometry validity, CRS semantic comparison, row-group statistics, actual bbox covering, reader compatibility, GeoParquet 2.x migration, evidence, and release.

## Trust boundary

The resulting profile is deliberately metadata-only. `READY` means only “eligible for the next, stronger validation layer.” It never means source-admitted, evidence-complete, policy-allowed, signed, promoted, released, deployed, published, or public-safe.
