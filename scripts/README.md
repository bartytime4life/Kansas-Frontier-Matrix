# Kansas-Frontier-Matrix — Scripts

Helper scripts that automate **fetch → convert → derive → validate → package → index** for the Kansas-Frontier-Matrix / Kansas Geo Timeline stack. They are **CLI-first**, modular, reproducible, and designed to slot into the **Makefile** and **CI**.

* **Stdlib-first** (GDAL/`requests` where appropriate), atomic writes, clear exit codes.
* **Idempotent** by default (skip unless forced).
* Every major artifact gets a **`.sha256`** and many write a **JSON manifest**.

---

## At-a-glance

```text
scripts/
├── fetch.py                # Fetch STAC/cat URLs → data/raw (stdlb-only, atomic, sidecars, manifest)
├── topoview_fetch.py       # USGS TopoView API (v4) → downloads + optional per-map STAC items
├── make_cogs.py            # GeoTIFF → COG (gdal_translate → rio-cogeo fallback; atomic; sidecars; manifest)
├── derive_terrain.py       # Parallel hillshade/slope/aspect (GDAL Python API → CLI fallback)
├── make_terrain_pack.py    # One-shot hillshade+slope+aspect wrapper
├── validate_cogs.py        # Parallel COG validation (rio → gdalinfo fallback) → JSON report
├── make_stac.py            # Build small STAC (collections/items) from data/cogs & vectors → stac/
├── validate_stac.py        # Validate STAC Items/Collections/Catalogs (schema + URL/file checks → report)
├── validate_sources.py     # Validate data/sources + STAC (lenient for sources; URL/file checks → report)
├── patch_stac_asset.py     # Patch STAC asset fields (checksum:size, file:size; batch/filters)
├── pack_kmz.py             # Package KML + assets → KMZ (fix hrefs; strip/blank remotes; sidecars)
└── scripts                 # Tiny task-runner (subcommands for common flows)
```

> Prefer running through the **Makefile** or `scripts/scripts` when possible — targets are wired and include robust fallbacks.

---

## Quick start

```bash
# 0) Doctor — show environment/tooling
scripts/scripts doctor

# 1) Fetch mixed sources (STAC items, catalogs, direct URLs) → data/raw
python scripts/fetch.py data/sources/*.json stac/items/**/*.json --jobs 6 --by-domain

# 2) Convert to COG (idempotent, atomic; ZSTD by default)
python scripts/make_cogs.py --inp data/processed --recursive --pattern "*.tif" \
  --out data/cogs --jobs 8 --validate

# 3) Derive terrain (hillshade/slope/aspect) in parallel
python scripts/derive_terrain.py data/cogs/dem/*.tif --products hillshade,slope,aspect \
  --cog --multidir --threads ALL_CPUS

# 4) Validate COGs (rio → gdalinfo fallback) → JSON report
python scripts/validate_cogs.py data/cogs --jobs 8 --timeout 120 \
  --report data/validation/cog_validate.report.json

# 5) Build STAC (collections/items) from COGs/vectors → stac/
python scripts/make_stac.py

# 6) Validate STAC (schema + URL/local-file checks) → CI report
python scripts/validate_stac.py stac --check-urls --check-files \
  --report data/validation/validate_stac.report.json

# 7) Regionate & package KML → KMZ (fixed hrefs; extra files)
python scripts/pack_kmz.py --kml out/regionated --out dist --strip-remote --name-from-kml
```

Or via the runner:

```bash
# validate STAC + sources (URL + file checks) into data/validation/
scripts/scripts validate:stac --check-urls --check-files
scripts/scripts validate:sources --check-urls --check-files

# render viewer config (requires kgt)
scripts/scripts stac:render --stac stac/items --out web/app.config.json

# USGS TopoView fetch (bbox/year-configured in data/sources/usgs_topoview.json)
scripts/scripts fetch:topoview --max 25 --stac-dir stac/topoview
```

---

## Script details (concise)

### `fetch.py` (stdlib-only downloader)

* **What:** Fetch mixed inputs → `data/raw/` with atomic writes and `.sha256` sidecars.
* **Understands:** STAC Items (assets), source catalogs (`endpoint[s]`, `urls`, `assets[].href`), or direct URLs.
* **Grouping:** by JSON stem (default) or `--subdir` or `--by-domain`.
* **Manifest:** `data/raw/manifest.fetch.json`.

```bash
python scripts/fetch.py data/sources/*.json stac/items/**/*.json --jobs 6 --by-domain
```

### `topoview_fetch.py`

* **What:** USGS TopoView API (v4.x) with bbox/year filters, paging, strict format/series/scale filtering.
* **Outputs:** downloads → `data/raw/topoview/`; README index + manifest; optional per-map STAC items.

```bash
python scripts/topoview_fetch.py --source data/sources/usgs_topoview.json --max 25 --stac-dir stac/topoview
```

### `make_cogs.py`

* **What:** GeoTIFF → **COG** (prefers `gdal_translate -of COG`; falls back to `rio cogeo`).
* **Defaults:** ZSTD, BLOCKSIZE=512, OVERVIEWS=AUTO, `NUM_THREADS=ALL_CPUS`; **atomic write**; `.sha256` + `.meta.json`.
* **Smart:** detect 8-bit RGB → optional `--jpeg`; auto NoData; predictor hint for ints/floats; skip/repack logic; validate optionally.

```bash
python scripts/make_cogs.py --inp data/processed --out data/cogs --recursive --validate --jobs 8
```

### `derive_terrain.py` / `make_terrain_pack.py`

* **What:** Parallel **hillshade / slope / aspect** from DEMs (COG or plain GeoTIFF). GDAL Python API → CLI fallback.
* **Nice bits:** auto scale (meters vs degrees), `--multidir`, NODATA handling, SHA sidecars, manifest.

```bash
python scripts/derive_terrain.py data/cogs/dem/*.tif --products hillshade,slope,aspect --cog --multidir
```

### `validate_cogs.py`

* **What:** Validate COG conformance quickly (`rio cogeo validate` → `gdalinfo -json` fallback).
* **Outputs:** JSON report for CI.

```bash
python scripts/validate_cogs.py data/cogs --jobs 8 --timeout 120 --report data/validation/cog_validate.report.json
```

### `make_stac.py` (STAC builder)

* **What:** Create STAC `collections` and `items` from `data/cogs/` and `data/processed/vectors/` → **`stac/`** (top-level).
* **Valid by default:** always writes bbox; sets temporal `datetime` or `start/end`; optionally copies `file:size` and `checksum:sha256` from sidecars; links `provenance` if `*.meta.json` exists.

```bash
python scripts/make_stac.py --bbox -102.05 36.99 -94.59 40.00 --interval 1800-01-01T00:00:00Z 2100-12-31T23:59:59Z
```

### `validate_stac.py` / `validate_sources.py`

* **What:** Validate **Items / Collections / Catalogs** (schema + minimal checks); optionally check http(s) URLs and local/relative `file://` hrefs. Emits CI-ready report JSON.

```bash
python scripts/validate_stac.py stac --check-urls --check-files --report data/validation/validate_stac.report.json
python scripts/validate_sources.py data/sources stac --check-urls --check-files --report data/validation/validate_sources.report.json
```

### `patch_stac_asset.py`

* **What:** Patch STAC asset fields (e.g., `checksum:sha256`, `file:size`), **batch-mode**, filters (`--role`, `--type`), dotted `--item-set` for item properties, robust sidecar parsing.

```bash
python scripts/patch_stac_asset.py stac/items/**/*.json --asset '*' --from-file-size --from-sha256-file --role data --pretty
```

### `pack_kmz.py`

* **What:** Package KML + local assets into KMZ, fix `<href>` paths, include extras, strip or blank remote refs, name from `<Document><name>` if desired. Writes `.sha256` + `.meta.json`.

```bash
python scripts/pack_kmz.py --kml out/regionated --out dist --strip-remote --name-from-kml
```

### `scripts/scripts` (task runner)

* **Subcommands:** `validate:stac`, `validate:sources`, `stac:render`, `stac:validate`, `fetch:topoview`, `doctor`.

```bash
# list
scripts/scripts list

# stac validate (URL + file checks)
scripts/scripts stac:validate
```

---

## How everything connects

* **Makefile** targets wrap these tools:

  * `make fetch` → `scripts/fetch.py`
  * `make cogs` → `scripts/make_cogs.py` (bulk)
  * `make terrain` → `scripts/derive_terrain.py` (or `make_terrain_pack.py`)
  * `make validate-cogs` → `scripts/validate_cogs.py`
  * `make stac` → `scripts/make_stac.py` (→ `stac/`)
  * `make stac-validate` → `scripts/validate_stac.py`
  * `make kmz` → `scripts/pack_kmz.py`

* **CI (GitHub Actions)**: jobs call the same scripts; JSON reports land under `data/validation/` and are uploaded as artifacts.

* **Provenance**: Most scripts write `.sha256` and either a per-artifact `.meta.json` or a run-level **manifest** (tool, args, timings, sizes, hashes).

---

## Conventions & guarantees

* **Exit codes:** `0` success; `1–2` input/env problems; `>2` processing errors.
* **Atomic writes:** outputs written as `*.part` or `*.tmp` then renamed.
* **Idempotent:** skip existing outputs when safe (unless `--force`/`--repack`/`--overwrite`).
* **Parallelism:** `--jobs`, `NUM_THREADS=ALL_CPUS` for GDAL transforms.
* **Paths:**

  * Raw downloads → `data/raw/`
  * COGs & derivatives → `data/cogs/…`
  * STAC index → **`stac/`** (top-level)
  * Validation reports → `data/validation/`

---

## Minimal deps

* **Python 3.10+**
* `requests` (for ArcGIS/topoview fetchers)
* **GIS tools** (preferred/optional): GDAL (`gdaldem`, `gdal_translate`, `gdalbuildvrt`, `gdalinfo`), `rio cogeo` (faster validation)

---

## Troubleshooting

* **COG validation failing?** Run `validate_cogs.py` with `--timeout` and inspect the JSON report. If `rio` missing, install or rely on the `gdalinfo` fallback.
* **STAC items invalid?** Use `validate_stac.py --no-strict` to see minimal structural errors; then add `--check-urls --check-files` to find broken hrefs.
* **KMZ shows red X icons?** `pack_kmz.py` fixes common `<IconStyle>/<Icon>` and Overlay hrefs. Use `--blank-remote` to keep features but clear remote hrefs, or `--strip-remote` to drop them entirely.

---

### Tips

* Keep raw downloads in `data/raw/`; convert to COGs in `data/cogs/`; viewer-friendly copies go to `data/derivatives/`.
* Ensure CRS units align with **scale** (meters vs degrees). Derivation tools auto-detect but allow overrides.
* Heavy jobs: set `GDAL_CACHEMAX=2048` (or higher) and pass `--threads ALL_CPUS`.

---
