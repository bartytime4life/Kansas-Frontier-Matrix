# `data/earth/` — Earth Observation & Global Context Layers

This folder holds **Earth observation datasets** and **global reference layers** that complement the
Kansas-focused datasets under `data/`. These layers provide basemaps, climate context, and environmental
indices for comparative analysis.

---

## Scope

- 🌍 **Global context**: datasets that extend beyond Kansas, e.g., NASA/NOAA satellite products, DEMs,
  land cover, vegetation indices.
- 🛰️ **Remote sensing**: MODIS, Sentinel, Landsat, Daymet, NLCD, GEDI, HydroSHEDS, etc.
- 🌱 **Environmental indices**: NDVI, EVI, drought indices, fire perimeters, global soils.
- 🗺️ **Basemaps**: natural earth, coastlines, political boundaries, rivers, or topographic backgrounds.

> Kansas is the core of this project — these global layers exist **only for context and comparison**.

---

## Structure

```text
data/earth/
├── sources/       # JSON descriptors (STAC-style or source metadata)
├── raw/           # downloaded archives / unprocessed rasters/vectors
├── processed/     # reprojected/cleaned GeoJSON, COGs, vector tiles
├── stac/          # STAC Items & Collections referencing processed assets
└── README.md      # this file
````

* **sources/** → `*.json` descriptors compatible with `scripts/fetch.py` and `make fetch`
* **raw/** → untouched downloads (tar/zip, HDF, NetCDF, GeoTIFF, etc.)
* **processed/** → converted outputs (Cloud-Optimized GeoTIFF, GeoJSON, MBTiles)
* **stac/** → metadata to connect to the hub

---

## Conventions

* **Coordinate reference**: Standardize to **EPSG:4326** (WGS84) unless otherwise justified.
* **Raster format**: Cloud-Optimized GeoTIFF (`.tif`) with internal overviews.
* **Vector format**: GeoJSON for small/medium, or vector tiles (MBTiles/PMTiles) for large.
* **Metadata**: Every dataset has a STAC Item (`stac/items/*.json`) pointing to processed assets.
* **Checksums**: `.sha256` files accompany raw/processed artifacts for reproducibility.

---

## Connections

* `stac-badges.yml` → validates `data/earth/stac/**` and generates Shields badges for repo/site.
* `stac.yml` → renders `web/app.config.json` including earth layers if referenced.
* `site.yml` → deploys processed layers into MapLibre viewer for time slider or background context.

---

## Common tasks

* **Add a new dataset**:

  1. Create `data/earth/sources/<dataset>.json` (endpoint, license, bbox, temporal coverage).
  2. Run `make fetch` to download to `data/earth/raw/`.
  3. Convert with `make cogs` (for rasters) or `make vectors` (for shapefiles → GeoJSON).
  4. Write STAC Item under `data/earth/stac/items/`.
  5. Validate via `make stac-validate`.

* **Update an existing dataset**:

  * Refresh sources JSON.
  * Re-run `make fetch` + conversion steps.
  * Re-validate STAC.

* **Link to viewer**:

  * Reference STAC Item in `scripts/badges/source_map.json`.
  * Regenerate `web/app.config.json` via `make stac`.

---

## Notes

* Global datasets can be large. Prefer **per-tile** or **per-year** subsets (MODIS, Sentinel, etc.).
* Always record **license** in source JSONs (e.g., NASA EarthData, Copernicus, CC-BY-4.0).
* Use `scripts/gen_sha256.sh` to hash large files after fetch.

---

✅ With this structure, **Kansas remains the focus**, while Earth layers add the environmental and global
dimensions needed for robust historical + geospatial analysis.

```

---
