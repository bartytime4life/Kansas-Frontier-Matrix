# Geospatial Carrier Readiness Check

Status: `PROPOSED_INACTIVE`

`GeospatialCarrierReadinessCheck` is a fixture-first preflight for downstream geospatial carriers. It turns three standards documents that currently describe KFM expectations into one finite, no-network review surface:

- Cloud Optimized GeoTIFF (COG) raster carriers;
- Mapbox Vector Tile (MVT) public vector-tile carriers; and
- GeoParquet 1.1.0 canonical vector artifacts.

The check evaluates declared metadata only. It does **not** open TIFF/Parquet/Protobuf bytes, execute GDAL, Tippecanoe, PMTiles, MapLibre, or a Parquet reader, fetch STAC, resolve a `SourceDescriptor`, authenticate a `RunReceipt`, verify evidence, evaluate policy, sign an artifact, promote lifecycle state, release, deploy, or publish.

## Finite result

The validator returns exactly one outcome:

- `READY` — the declared metadata satisfies this inactive KFM profile;
- `HOLD` — the declaration is well formed but misses one or more KFM readiness requirements; or
- `ERROR` — the declaration is malformed, internally unsafe, or violates a fail-closed integrity boundary.

Advisories may accompany `READY` or `HOLD`. An advisory never grants authority.

## Common boundary

Every candidate binds an immutable artifact identity, `SourceDescriptor`, `RunReceipt`, and STAC item reference. All governance effects are fixed false and `release_ref` is fixed null. Artifact hashes are shape-checked only; this profile does not resolve artifact bytes.

## COG profile

The COG lane checks declared TIFF media/extension, internal tiling, power-of-two block layout, overview presence for rasters whose largest dimension exceeds 512 pixels, explicit CRS/nodata policy, range-read support, and Raster + Projection STAC extension declarations.

These checks implement KFM's standards posture as a metadata preflight only. Binary COG conformance remains a later `rio-cogeo`/GDAL-class validation responsibility.

## MVT profile

The MVT lane checks MVT v2.x, extent 4096, XYZ scheme, contract-bearing source-layer agreement, stable feature IDs, `source_ref` retention, attribute-whitelist closure, sensitive-attribute exclusion, the 64 KiB interactive tile budget, zero silent geometry drops, bounded area drift, pinned tiler parameters, and the PMTiles + range-read public-delivery default.

A style is never allowed to conceal attributes that were already encoded into public tile bytes.

## GeoParquet profile

The GeoParquet lane pins KFM to GeoParquet 1.1.0, `.parquet`, `application/vnd.apache.parquet`, one root primary geometry declaration, WKB, explicit PROJJSON CRS, stable deterministic row grouping/order, null-only missing-value behavior, forward-compatible unknown-metadata preservation, and numeric-unit coverage.

GeoParquet 2.x declarations are held rather than silently accepted. Missing 1.1 bbox covering is an advisory because KFM recommends it for pruning but does not treat it as a universal hard requirement.

## Non-effects

A green check is not a `ValidationReport`, `EvidenceBundle`, `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, signature, or proof. It creates no source or publication authority and cannot move an artifact into `PUBLISHED`.
