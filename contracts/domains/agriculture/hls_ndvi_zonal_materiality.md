# Fixture-Only HLS NDVI Zonal Materiality Assessment Contract

**Status:** PROPOSED fixture profile  
**Owning domain:** Agriculture  
**Artifact family:** `HlsNdviZonalMaterialityAssessment`  
**Source basis:** *New Ideas 4-2-26.pdf* — clear-pixel NDVI statistics, equal-area aggregation, and emit-only-on-material-change rules  
**Directory Rules basis:** agriculture-product meaning belongs under `contracts/domains/agriculture/`; machine shape belongs under `schemas/contracts/v1/domains/agriculture/`; deterministic enforcement belongs under `tools/validators/domains/agriculture/`.

## Purpose

Define a deterministic, no-network assessment over two precomputed HLS-style county or HUC12 NDVI summaries. The profile verifies reproducible mask counts, equal-area grid identity, clear-pixel statistics, source-change evidence, signal-change thresholds, valid-pixel coverage, and a finite review outcome.

This slice validates summary and decision semantics only. It does not search STAC, download HLS assets, decode Fmask pixels, reproject rasters, compute NDVI, run zonal statistics, build a COG, issue an agricultural alert, or publish a layer.

## Frozen fixture profile

The fixture profile uses the source packet's initial rules:

- grid CRS is `EPSG:5070`;
- statistics are computed only over clear pixels with acceptable aerosol and without cloud, shadow, or adjacent-cloud contamination;
- source change exists when STAC update time, collection version, asset digest, or source-spec hash changes;
- signal change requires an absolute mean-NDVI change greater than `0.05` or a relative change greater than `10%`;
- material assessment requires current valid-pixel fraction of at least `60%`;
- threshold equality is not material because the source rule uses strict greater-than comparisons.

These values are fixture rules, not adopted production policy.

## Finite outcomes

- `MATERIAL_CHANGE_CANDIDATE` — source and signal changed, and valid coverage passes.
- `NO_MATERIAL_CHANGE` — source or signal change is insufficient under the frozen rules.
- `HOLD` — current valid-pixel coverage is below the minimum.
- validator `ERROR` — schema, count closure, temporal order, deterministic hash, computed fields, or decision semantics are inconsistent.

## Required anti-collapse rules

- HLS source metadata remains distinct from a derived polygon summary.
- `VI_ASSET` and `NIR_RED_FALLBACK` remain explicit.
- county and HUC12 identities use different formats.
- pixel counts must close exactly to the total; percentages cannot be asserted without counts.
- map or alert publication is not implied by `MATERIAL_CHANGE_CANDIDATE`.
- smoke, irrigation, post-fire regrowth, crop rotation, and other interpretation flags remain outside this bounded statistic gate unless separately evidenced.

## Trust boundary

This slice does not:

- call a STAC API or remote asset host;
- claim that an HLS asset, mask, or polygon statistic is current or authoritative;
- perform raster calculations or geometry operations;
- create an observation, EvidenceBundle, PolicyDecision, ReleaseManifest, COG, GeoJSON, PMTiles archive, alert, or public layer;
- promote, release, deploy, or publish.

## Rollback

The slice is additive. Remove the contract, schema, validator, fixtures, tests, workflow, and generated authoring receipt. No source, raster, database, cache, API, map, alert, release, or published artifact requires cleanup.
