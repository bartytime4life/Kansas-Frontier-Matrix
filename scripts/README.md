# Kansas-Frontier-Matrix — Scripts

Helper scripts that automate data ingestion, validation, terrain derivatives, and site-building for the **Kansas-Frontier-Matrix** stack.
They are **CLI-first**, modular, and reproducible, designed to slot into Makefile and CI.

---

## At-a-glance

```text
scripts/
├── fetch_arcgis.py          # ArcGIS ImageServer/FeatureServer export (+ETag, tiling, optional COG)
├── mosaic_lidar_county.py   # County LiDAR mosaic → VRT → DEM COG (parallel/resumable fetch)
├── make_hillshade.py        # Hillshade COGs (single or batch)
├── make_slope_aspect.py     # Slope/Aspect COGs (single or batch)
├── make_terrain_pack.py     # One-shot: hillshade + slope + aspect
├── derive_terrain.py        # Parallel terrain derivation (GDAL API fallback to CLI)
├── validate_cogs.py         # Parallel COG validation (rio-cogeo → gdalinfo fallback; JSON report)
├── write_meta.py            # Sidecar .sha256 and rich .meta.json (git context, inputs roll-up)
├── regionate_kml.py         # Quadtree KML Region/LOD network-links (optional KMZ)
├── sync-roadmap.js          # Sync .github/roadmap/roadmap.yaml → GitHub labels/milestones/issues
└── (optional helpers wired via Makefile targets)
```

---

## Quick start

```bash
# 1) Fetch ArcGIS sources (writes data/raw + manifest)
python scripts/fetch_arcgis.py --sources data/sources --out data/raw --etag-cache --post

# 2) Build a county LiDAR DEM COG (mosaics tiles listed in CSV)
python scripts/mosaic_lidar_county.py --county pawnee --jobs 8 --src-nodata -9999 --dst-nodata -9999

# 3) Derive terrain (COGs) from any DEM(s)
python scripts/make_terrain_pack.py data/sources/dem/processed/lidar/pawnee/pawnee_1m_dem_cog.tif \
  --multidir --compute-edges --validate

# 4) Validate COGs and emit a report
python scripts/validate_cogs.py data/cogs --jobs 8 --timeout 120 --report data/validation/cog_validate.report.json

# 5) Regionate a large GeoJSON to a KML pyramid (network-linked)
python scripts/regionate_kml.py --geojson data/processed/vectors/points.geojson \
  --out data/kml/points --name "Kansas Points" --kmz data/kml/points.kmz
```

> Prefer running through the **Makefile** whenever possible (`make terrain`, `make validate-cogs`, `make mosaic-county COUNTY=pawnee`, etc.). Targets are already wired to these scripts and include robust fallbacks.

---

## Script details (concise)

### `fetch_arcgis.py`

* **What:** Robust ImageServer/FeatureServer export with retries, optional `--post`, `--etag-cache`, and optional single-tile GeoTIFF → **COG** (`--cog`).
* **Outputs:** data files + `.sha256` sidecars and a manifest (`--manifest`).
* **Example:**

  ```bash
  python scripts/fetch_arcgis.py --sources data/sources --out data/raw \
    --only ks_hillshade --etag-cache --cog --gdal-threads ALL_CPUS
  ```

### `mosaic_lidar_county.py`

* **What:** Parallel/resumable download of county LiDAR tiles, `gdalbuildvrt` VRT, COG translate with DEM-friendly profile.
* **Paths:** infers from `--county` (`data/sources/dem/tile_indexes/<county>_1m_tiles.csv`).
* **Example:** `python scripts/mosaic_lidar_county.py --county pawnee --jobs 8`

### `make_hillshade.py`, `make_slope_aspect.py`, `make_terrain_pack.py`

* **What:** GDAL-backed terrain derivatives producing **COGs** (single file or batches).
  Options for azimuth/altitude, z-factor, scale, multi-directional, percent slope, etc.
* **One-shot pack:** `python scripts/make_terrain_pack.py <DEM or DIR> --multidir --compute-edges --validate`

### `derive_terrain.py`

* **What:** Parallel derivation pipeline using the **GDAL Python API** when present, with CLI fallbacks (`gdaldem`/`gdal_translate`).
* **Nice bits:** auto-detects **scale** (1 for meters; ~111120 for degrees), **NODATA** controls, per-product selection, SHA sidecars, and a machine-readable manifest.
* **Example:**
  `python scripts/derive_terrain.py data/cogs/dem/*.tif --cog --products hillshade,slope,aspect --multidir`

### `validate_cogs.py`

* **What:** Parallel validation via `rio cogeo validate` (if available) or `gdalinfo --json` fallback.
  Include/exclude globs, directory pruning, per-file timeouts, and a **JSON report**.
* **Example:**
  `python scripts/validate_cogs.py data/cogs --jobs 8 --timeout 120 --report data/validation/cog_validate.report.json`

### `write_meta.py`

* **What:** Emits `<artifact>.<algo>` checksum sidecar and rich `<artifact>.meta.json` (command, CWD, git commit/branch/dirty, inputs digests, roll-up).
* **Example:**
  `python scripts/write_meta.py data/cogs/terrain/ks_slope_deg.tif --inputs data/cogs/dem/ks_1m_dem_2018_2020.tif --extra stage=slope`

### `regionate_kml.py`

* **What:** Quadtree **Region/LOD** KML with NetworkLinks for progressive loading in Google Earth; optional `.kmz`.
* **Inputs:** GeoJSON (preferred) or simple KML with Placemarks.

### `sync-roadmap.js`

* **What:** Idempotent sync of `.github/roadmap/roadmap.yaml` → GitHub **labels, milestones, issues**.
  Supports **DRY_RUN**, retries/backoff, optional pruning flags.

---

## How everything connects

* **Makefile** calls these scripts for repeatable pipelines:

  * `make terrain` → hillshade/slope/aspect COGs + mirror to `data/derivatives/`
  * `make validate-cogs` → runs `scripts/validate_cogs.py` and stores a JSON report
  * `make mosaic-county COUNTY=pawnee` → LiDAR → DEM COG
  * `make regionate SRC=... OUT=...` → KML pyramid
  * `make stac` / `make stac-validate` → STAC build/validate (auto-patches DEM checksum/size)
* **CI (GitHub Actions)**: use these scripts in jobs to fetch, build, validate, and publish artifacts.
* **Provenance**: `write_meta.py` is invoked by several scripts (best-effort) to attach machine-readable lineage.

---

## Conventions & guarantees

* **Stdlib-first** (plus GDAL/requests where needed), atomic writes, clear exit codes:

  * `0` success; `1–2` input/env problems; `>2` processing errors.
* **Sidecars**: `.sha256` are written for major outputs; JSON **manifests** capture runs for CI.
* **Idempotency**: most scripts skip existing outputs unless `--overwrite`; some support **ETag** (`fetch_arcgis.py --etag-cache`).
* **Parallelism**: controlled via `--jobs` or `NUM_THREADS=ALL_CPUS` creation options for GDAL COGs.

---

## Minimal dependencies

* **Required**: Python 3.10+, `requests` (for ArcGIS fetches)
* **GIS tools** (preferred/optional): GDAL (`gdaldem`, `gdal_translate`, `gdalbuildvrt`, `gdalinfo`), `rio cogeo` (for validation fast-path)
* **Dev**: `@actions/core`, `@actions/github`, `js-yaml` for `sync-roadmap.js`

> The Makefile checks for tool availability and gracefully falls back when possible.

---

## Common usage snippets

```bash
# Derive only hillshade with multi-directional light, auto scale
python scripts/derive_terrain.py data/cogs/dem/ks_1m_dem_2018_2020.tif \
  --products hillshade --cog --multidir --threads ALL_CPUS

# Validate just the hillshade file
python scripts/validate_cogs.py data/cogs/hillshade --pattern "ks_hillshade_*.tif" --report data/validation/hill.json

# Write meta + checksum for any artifact
python scripts/write_meta.py data/derivatives/hillshade.tif --inputs data/cogs/dem/ks_1m_dem_2018_2020.tif --extra stage=hillshade
```

---

## Roadmap (scripts in progress)

* `ingest_texts.py` — OCR/NLP pipeline for scanned diaries/newspapers.
* `ingest_vectors.py` — ETL for treaties, PLSS grids, railroads, hydrology.
* `ingest_hazards.py` — NOAA/FEMA hazards integration.
* `graph_linker.py` — Entity/event linker to the knowledge graph.

---

### Tips

* Keep raw downloads in `data/raw/`; COGs in `data/cogs/`; mirrored viewer assets in `data/derivatives/`.
* Ensure CRS units align with **scale** assumptions (meters vs degrees). The derivation tools auto-detect but allow overrides.
* For heavy jobs, prefer `--threads ALL_CPUS` and set GDAL cache vars (e.g., `GDAL_CACHEMAX=2048`).

---
