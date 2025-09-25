# Kansas-Frontier-Matrix — Scripts

Helper scripts that automate **fetch → convert → derive → validate → package → index** for the Kansas-Frontier-Matrix / Kansas Geo Timeline stack.  
They are **CLI-first**, modular, reproducible, and designed to slot into the **Makefile** and **CI**.

- **Stdlib-first** (GDAL/`requests` where appropriate), atomic writes, clear exit codes.
- **Idempotent** by default (skip unless forced).
- Every major artifact gets a **`.sha256`** and many write a **JSON manifest**.

---

## At-a-glance

```text
scripts/
├── fetch.py                # Fetch STAC/cat URLs → data/raw (atomic, sidecars, manifest)
├── topoview_fetch.py       # USGS TopoView API (v4) → downloads + optional STAC items
├── make_cogs.py            # GeoTIFF → COG (gdal_translate → rio-cogeo; atomic; sidecars; manifest)
├── derive_terrain.py       # Parallel hillshade/slope/aspect (GDAL Python API → CLI fallback)
├── make_terrain_pack.py    # One-shot hillshade+slope+aspect wrapper
├── validate_cogs.py        # Parallel COG validation (rio → gdalinfo fallback) → JSON report
├── make_stac.py            # Build STAC (collections/items) from data/cogs & vectors → stac/
├── validate_stac.py        # Validate STAC Items/Collections/Catalogs (schema + URL/file checks)
├── validate_sources.py     # Validate data/sources + STAC (lenient for sources; URL/file checks)
├── patch_stac_asset.py     # Patch STAC asset fields (checksum, size; batch/filters)
├── pack_kmz.py             # Package KML + assets → KMZ (fix hrefs; strip/blank remotes; sidecars)
└── scripts                 # Tiny task-runner (subcommands for common flows)
````

> Prefer running through the **Makefile** or `scripts/scripts` when possible — targets are wired and include robust fallbacks.

---

## Quick start

```bash
# 0) Doctor — show environment/tooling
scripts/scripts doctor

# 1) Fetch mixed sources → data/raw
python scripts/fetch.py data/sources/*.json stac/items/**/*.json --jobs 6 --by-domain

# 2) Convert to COG (ZSTD by default)
python scripts/make_cogs.py --inp data/processed --recursive --pattern "*.tif" \
  --out data/cogs --jobs 8 --validate

# 3) Derive terrain (hillshade/slope/aspect)
python scripts/derive_terrain.py data/cogs/dem/*.tif --products hillshade,slope,aspect \
  --cog --multidir --threads ALL_CPUS

# 4) Validate COGs → JSON report
python scripts/validate_cogs.py data/cogs --jobs 8 --timeout 120 \
  --report data/validation/cog_validate.report.json

# 5) Build STAC → stac/
python scripts/make_stac.py

# 6) Validate STAC (schema + URL/local-file checks)
python scripts/validate_stac.py stac --check-urls --check-files \
  --report data/validation/validate_stac.report.json

# 7) Regionate & package KML → KMZ
python scripts/pack_kmz.py --kml out/regionated --out dist --strip-remote --name-from-kml
```

Or via the runner:

```bash
# validate STAC + sources into data/validation/
scripts/scripts validate:stac --check-urls --check-files
scripts/scripts validate:sources --check-urls --check-files

# render viewer config (requires kgt)
scripts/scripts stac:render --stac stac/items --out web/app.config.json

# USGS TopoView fetch
scripts/scripts fetch:topoview --max 25 --stac-dir stac/topoview
```

---

## Script details

### `fetch.py`

Fetch mixed inputs → `data/raw/` with atomic writes and `.sha256` sidecars.
Understands STAC Items, source catalogs (`endpoint[s]`, `urls`, `assets[].href`), or direct URLs.
Groups by JSON stem (default) or `--subdir` or `--by-domain`.
Manifest: `data/raw/manifest.fetch.json`.

### `topoview_fetch.py`

USGS TopoView API (v4.x) with bbox/year filters, paging, format/series/scale filters.
Outputs: downloads → `data/raw/topoview/`; README index + manifest; optional per-map STAC items.

### `make_cogs.py`

GeoTIFF → **COG** (prefers `gdal_translate`; falls back to `rio cogeo`).
Defaults: ZSTD, BLOCKSIZE=512, OVERVIEWS=AUTO, NUM_THREADS=ALL_CPUS.
Atomic write, `.sha256` + `.meta.json`, skip/repack logic, optional validation.

### `derive_terrain.py` / `make_terrain_pack.py`

Parallel **hillshade / slope / aspect** from DEMs (COG or GeoTIFF).
Auto scale (meters vs degrees), `--multidir`, NODATA handling, SHA sidecars, manifest.

### `validate_cogs.py`

Validate COG conformance (`rio cogeo validate` → `gdalinfo -json` fallback).
Outputs: JSON report for CI.

### `make_stac.py`

Create STAC `collections` and `items` from `data/cogs/` and `data/processed/vectors/` → **`stac/`**.
Valid by default: always writes bbox; sets temporal rules; copies `file:size` and `checksum:sha256` if sidecars exist; links provenance.

### `validate_stac.py` / `validate_sources.py`

Validate **Items / Collections / Catalogs** (schema + minimal checks).
Optionally check http(s) URLs and local/relative `file://` hrefs.
Emit CI-ready report JSON.

### `patch_stac_asset.py`

Patch STAC asset fields (`checksum:sha256`, `file:size`), batch-mode, filters (`--role`, `--type`), dotted `--item-set` for item properties.

### `pack_kmz.py`

Package KML + local assets into KMZ, fix `<href>` paths, include extras, strip or blank remote refs, name from `<Document><name>`.
Writes `.sha256` + `.meta.json`.

### `scripts/scripts` (task runner)

Subcommands: `validate:stac`, `validate:sources`, `stac:render`, `stac:validate`, `fetch:topoview`, `doctor`.

---

## How everything connects

* **Makefile** targets wrap these tools:

  * `make fetch`, `make cogs`, `make terrain`, `make validate-cogs`, `make stac`, `make stac-validate`, `make kmz`.
* **CI (GitHub Actions)** calls the same scripts; JSON reports land under `data/validation/` and upload as artifacts.
* **Provenance**: `.sha256` + `.meta.json` sidecars and run-level manifests capture lineage.

---

## Conventions & guarantees

* **Exit codes:** `0` success; `1–2` input/env problems; `>2` processing errors.
* **Atomic writes:** outputs written as `*.part`/`*.tmp` then renamed.
* **Idempotent:** skip existing outputs unless `--force`/`--repack`/`--overwrite`.
* **Parallelism:** `--jobs`, `NUM_THREADS=ALL_CPUS` for GDAL transforms.
* **Paths:**

  * Raw downloads → `data/raw/`
  * COGs & derivatives → `data/cogs/…`
  * STAC index → `stac/`
  * Validation reports → `data/validation/`

---

## Minimal deps

* Python 3.10+
* `requests` (for ArcGIS/TopoView fetchers)
* GIS tools (optional): GDAL (`gdal_translate`, `gdaldem`, `gdalinfo`, `gdalbuildvrt`), `rio cogeo`

---

## Tips

* Keep raw downloads in `data/raw/`; convert to COGs in `data/cogs/`; viewer assets in `data/derivatives/`.
* Ensure CRS units align with **scale** (meters vs degrees). Derivation tools auto-detect but allow overrides.
* Heavy jobs: set `GDAL_CACHEMAX=2048` (or higher) and pass `--threads ALL_CPUS`.

```
