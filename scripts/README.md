# Kansas-Frontier-Matrix — Scripts

Helper scripts that automate **fetch → convert → derive → validate → package → index** for the Kansas-Frontier-Matrix / Kansas Geo Timeline stack.
They are **CLI-first**, modular, reproducible, and wired into the **Makefile** and **CI**.

* **Stdlib/GDAL-first**, atomic writes, clear exit codes.
* **Idempotent** by default (skip unless forced).
* Every major artifact writes a **`.sha256`** and many emit a **JSON manifest/report**.

> Prefer running through the **Makefile** or `scripts/scripts` when possible — targets are wired and include robust fallbacks.

---

## Inventory (what connects to what)

```text
scripts/
├── fetch.py                   # Pull mixed inputs (sources, STAC Items, direct URLs) → data/raw/
├── topoview_fetch.py          # USGS TopoView API → downloads (+ optional per-map STAC Items)
├── make_cog.py                # GeoTIFF → COG (gdal_translate → rio-cogeo fallback; sidecars; manifest)
├── make_hillshade.py          # Hillshade (COG) from DEM (helper used by Makefile)
├── make_slope_aspect.py       # Slope & aspect (COG) from DEM (helper used by Makefile)
├── make_terrain_pack.py       # One-shot hillshade+slope+aspect wrapper
├── validate_cogs.py           # Parallel COG validation → JSON report (rio → gdalinfo fallback)
├── make_stac.py               # Build STAC (collections/items) from data/* → stac/
├── validate_stac.py           # Validate STAC Items/Collections/Catalogs (schema + URL/file checks)
├── validate_sources.py        # Validate data/sources/*.json (lenient), optional URL/file checks
├── patch_stac_asset.py        # Patch STAC asset fields (checksum, size; batch/filters)
├── pack_kmz.py                # Package KML + assets → KMZ (fix hrefs; strip/blank remotes; sidecars)
├── update_registry.py         # (optional) Write small provenance registry entries after builds
├── regionate_kml.py           # (optional) Regionate GeoJSON/KML → KML tree / KMZ
├── gen_sha256.sh              # (optional) Cross-platform SHA256 helper
├── scripts                    # Task runner: validate:stac, validate:sources, stac:render, fetch:topoview, doctor
└── collections/
    ├── archaeology.sh         # ETL+STAC for archaeology collection (generic)
    └── archaeology_sites.sh   # ETL+STAC+thumbs for archaeology site registers (points/polys)
```

**Makefile ↔ scripts mapping (high-level):**

| Makefile target      | Script(s) used                                       | Output(s)                                          |
| -------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| `make fetch`         | `fetch.py`                                           | `data/raw/…`, `data/raw/manifest.fetch.json`       |
| `make cogs`          | `make_cog.py`                                        | `data/cogs/**/*.tif` (COGs + `.sha256/.meta.json`) |
| `make terrain`       | `make_hillshade.py`, `make_slope_aspect.py`          | `data/cogs/hillshade,slope,aspect/*.tif`           |
| `make validate-cogs` | `validate_cogs.py`                                   | `data/validation/cog_validate.report.json`         |
| `make stac`          | `make_stac.py`, `patch_stac_asset.py`                | `stac/**` (Items/Collections/Catalog)              |
| `make stac-validate` | `validate_sources.py`, `validate_stac.py` (or `kgt`) | `data/validation/validate_stac.report.json`        |
| `make site-config`   | `kgt render-config`                                  | `web/app.config.json`                              |
| `make regionate`     | `regionate_kml.py`                                   | KML tree / KMZ                                     |
| `make arch-sites*`   | `collections/archaeology_sites.sh`                   | processed GeoJSON, STAC items, thumbs, app config  |

---

## Quick start

### 0) Doctor

```bash
scripts/scripts doctor
make env
```

### 1) Fetch mixed sources → `data/raw/`

```bash
# all sources
python scripts/fetch.py --sources data/sources --out data/raw

# or target specific files
python scripts/fetch.py data/sources/*.json stac/items/**/*.json --jobs 6 --by-domain
```

### 2) Convert to COG (GeoTIFF → COG)

```bash
# via Makefile
make cogs

# or direct
python scripts/make_cog.py --in data/raw --out data/cogs --jobs 8 --validate
```

### 3) Derive terrain (hillshade/slope/aspect)

```bash
# via Makefile (preferred; handles mirroring to data/derivatives/)
make terrain DEM=data/cogs/dem/ks_1m_dem_2018_2020.tif
```

### 4) Validate COGs → JSON report

```bash
make validate-cogs
# report: data/validation/cog_validate.report.json
```

### 5) Build STAC → `stac/`

```bash
make stac
```

### 6) Validate STAC (schema + URL/local-file checks)

```bash
make stac-validate
# report: data/validation/validate_stac.report.json (if validate_stac.py is present)
```

### 7) Render viewer config (requires `kgt`)

```bash
make site-config
# writes web/app.config.json
```

### 8) Optional: KML / KMZ

```bash
python scripts/pack_kmz.py --kml out/regionated --out dist --strip-remote --name-from-kml
```

---

## Collections (pipelines for grouped layers)

### Archaeology Sites (points/polygons, site registers)

**Convenience via Makefile:**

```bash
make arch-sites            # fetch→unpack→process→stac→validate→render (thumbs included)
make arch-sites-validate   # validate STAC + render (thumbs included)
make arch-sites-render     # render viewer config only (thumbs included)
```

**Direct (collection script):**

```bash
bash scripts/collections/archaeology_sites.sh deps       # check deps (GDAL, jq, kgt, python)
bash scripts/collections/archaeology_sites.sh init       # create starter data/sources/arch_sites_example.json
bash scripts/collections/archaeology_sites.sh fetch
bash scripts/collections/archaeology_sites.sh unpack
bash scripts/collections/archaeology_sites.sh process
bash scripts/collections/archaeology_sites.sh stac
bash scripts/collections/archaeology_sites.sh validate
bash scripts/collections/archaeology_sites.sh render     # renders web/app.config.json + thumbnails
bash scripts/collections/archaeology_sites.sh doctor
```

**Outputs:**

* processed GeoJSON → `data/processed/arch_sites/*.geojson`
* STAC Items → `stac/items/archaeology-sites/*.json` (parent: `stac/collections/archaeology-sites.json`)
* thumbnails (auto) → `web/assets/thumbnails/*.png` and auto-attached to STAC assets

### Archaeology (generic collection)

```bash
bash scripts/collections/archaeology.sh fetch
bash scripts/collections/archaeology.sh process
bash scripts/collections/archaeology.sh stac
bash scripts/collections/archaeology.sh validate
bash scripts/collections/archaeology.sh render
```

> `make collections-build` gracefully handles scripts that **don’t** implement `build`: it falls back to `fetch→unpack→process→stac→validate→render`.

---

## Script details

### `fetch.py`

Fetch mixed inputs → `data/raw/` with atomic writes and `.sha256` sidecars.
Understands **STAC Items**, `data/sources/*.json` (`endpoints`, `urls`, `assets[].href`), and direct URLs.
Grouping: default by JSON stem; or `--subdir`/`--by-domain`.
Manifest: `data/raw/manifest.fetch.json`.

### `topoview_fetch.py`

USGS TopoView API (v4.x) with bbox/year/scale/series filters and paging.
Outputs → `data/raw/topoview/`; README index + manifest; optional per-map **STAC Items**.

### `make_cog.py`

GeoTIFF → **COG** (prefers `gdal_translate`; falls back to `rio cogeo`).
Defaults: DEFLATE/ZSTD (repo policy), blocksize, **auto overviews**, `NUM_THREADS=ALL_CPUS`.
Atomic write, `.sha256` + `.meta.json`, skip/repack logic, optional `--validate`.

### `make_hillshade.py`, `make_slope_aspect.py`, `make_terrain_pack.py`

COG derivatives from DEMs: **hillshade**, **slope**, **aspect**.
Auto unit scaling (meters vs degrees), `--multidir`, NODATA handling, sidecars + manifest.
Used by `make terrain` (with GDAL fallbacks if helpers not present).

### `validate_cogs.py`

Validate COG conformance (`rio cogeo validate` → `gdalinfo -json` fallback).
Outputs: `data/validation/cog_validate.report.json` (CI-ready).

### `make_stac.py`

Create **STAC** Collections & Items from `data/cogs/` + `data/processed/` → `stac/`.
Writes bbox/footprint, temporal properties, and (when sidecars exist) `file:size` + `checksum:sha256`.
Links provenance; supports **collection parents** (e.g., `archaeology-sites`).

### `validate_stac.py` / `validate_sources.py`

Validate **Items / Collections / Catalogs** (schema + minimal checks).
Optional `--check-urls` / `--check-files` for http(s) and local/relative `href`s.
Emit CI-ready reports under `data/validation/`.

### `patch_stac_asset.py`

Patch STAC assets (`checksum:sha256`, `file:size`) via batch filters (`--role`, `--type`, `--glob`), or one-off.
Makefile’s `stac` target auto-patches DEM if a `.sha256` sidecar is present.

### `pack_kmz.py`

KML → KMZ (fix `<href>`, add local assets, strip/blank remotes, name from `<Document><name>`).
Writes `.sha256` + `.meta.json`.

### `scripts` (task runner)

Subcommands:

* `validate:stac` (→ `data/validation/`)
* `validate:sources` (→ `data/validation/`)
* `stac:render` (→ `web/app.config.json`)
* `stac:validate` (schema + links)
* `fetch:topoview`
* `doctor`

---

## STAC → Viewer (kgt)

* **Build** STAC: `make stac`
* **Validate**: `make stac-validate`
* **Render** viewer config (MapLibre): `make site-config`
* **Archaeology Sites**: thumbnails auto-rendered & attached on `render` step (`archaeology_sites.sh`), then included in the viewer.

> If you don’t ship a Jinja template, the Makefile falls back to rendering directly from Items.

---

## Provenance & reports

* Sidecars: `*.sha256`, `*.meta.json` for major artifacts (COGs/derivatives/KMZ).
* Run-level manifests & reports:

  * `data/raw/manifest.fetch.json`
  * `data/validation/cog_validate.report.json`
  * `data/validation/validate_stac.report.json` (when enabled)

---

## Conventions & guarantees

* **Exit codes**: `0` success; `1–2` input/env problems; `>2` processing errors.
* **Atomic writes**: write to `*.part`/`*.tmp`, rename on success.
* **Idempotent**: skip existing outputs unless `--force`/`--repack`/`--overwrite`.
* **Parallelism**: `--jobs`; GDAL `NUM_THREADS=ALL_CPUS` where available.
* **Paths**:

  * Raw downloads → `data/raw/`
  * COGs & derivatives → `data/cogs/…` and `data/derivatives/`
  * STAC index → `stac/`
  * Validation reports → `data/validation/`
  * Thumbnails → `web/assets/thumbnails/`

---

## Troubleshooting

* **Missing GDAL/`kgt`/`jq`**: use `scripts/collections/archaeology_sites.sh deps` or `make env` to verify.
* **No Jinja template** for `site-config`: Makefile now renders directly from STAC Items as fallback.
* **STAC Items without parent**: ensure `stac/collections/<collection>.json` exists (e.g., `archaeology-sites.json`).
* **DEM patching skipped**: put a `.sha256` next to the DEM COG (or run `make dem-checksum`) so `make stac` can auto-patch.

---

### Examples (copy-paste)

```bash
# Full terrain → STAC → viewer cycle
make terrain
make stac
make stac-validate
make site-config

# Archaeology sites (all-in)
make arch-sites

# Validate & render only
make arch-sites-validate
```

This README now mirrors your Makefile and collection scripts, with correct names (`make_cog.py`, `make_hillshade.py`, `make_slope_aspect.py`) and connected flows (thumbnails, collections, kgt).
