<!--
Path: data/work/experiments/2026-01-02__ndvi__landsat8/data/exports/README.md
-->

# 📤 Exports — NDVI (Landsat 8) — 2026-01-02

![Status](https://img.shields.io/badge/status-work%20stage-orange)
![Experiment](https://img.shields.io/badge/experiment-2026--01--02-blue)
![Product](https://img.shields.io/badge/product-NDVI-brightgreen)
![Sensor](https://img.shields.io/badge/sensor-Landsat%208-lightgrey)
![Preferred Format](https://img.shields.io/badge/preferred-COG%20GeoTIFF-informational)

> [!IMPORTANT]
> This folder is under `data/work/…` → treat it as **reproducible, intermediate output**.
> For stable, “published” artifacts: promote to `data/processed/…` and register in the catalog (STAC/DCAT/PROV).

---

## 🧭 What is this folder?

This directory contains the *exported artifacts* produced by the experiment:

- 🧪 **Experiment ID:** `2026-01-02__ndvi__landsat8`
- 🎯 **Goal:** generate NDVI rasters (and optional summaries) from Landsat 8 imagery for a configured AOI/time window
- 📦 **Why “exports”:** this is the hand-off point between compute (e.g., Earth Engine / local processing) and downstream packaging, QA, and publishing

### NDVI quick definition 🌿

NDVI is computed as:

`NDVI = (NIR - RED) / (NIR + RED)`

For Landsat 8, NDVI typically uses **B5 = NIR** and **B4 = RED** (confirm in the experiment config for this run).

---

## 🗂️ Contents & conventions

> [!NOTE]
> Exact filenames/subfolders may vary by run configuration — the patterns below are the **contract** we aim to follow.

### Recommended layout (suggested) 🧱

```text
📁 data/work/experiments/2026-01-02__ndvi__landsat8/data/exports/
├─ 📄 README.md
├─ 📄 export_manifest.json            # required: what was exported + key metadata
├─ 📄 checksums.sha256                # required: sha256 for every exported asset
├─ 📁 raster/                         # preferred: GeoTIFF COGs
│  ├─ 🗺️ ndvi__landsat8__<aoi>__<start>--<end>__30m__<crs>__cog.tif
│  └─ 🧊 ndvi__landsat8__<aoi>__<start>--<end>__cloudmask.tif            # optional
├─ 📁 preview/                        # small “look” files for PRs / docs
│  └─ 🖼️ ndvi__landsat8__<aoi>__<start>--<end>__preview.png
├─ 📁 tables/                         # optional: summary outputs
│  └─ 📊 ndvi__landsat8__<aoi>__<start>--<end>__zonal__<unit>.csv
└─ 📁 logs/                           # optional but recommended
   ├─ 🧾 gee_tasks.log
   └─ 🧾 run_metadata.json
```

### File naming rules ✅

Use **double-underscore** separators and keep names sortable:

`<product>__<sensor>__<aoi>__<start>--<end>__<scale>__<crs>__<variant>.<ext>`

Where:

- `<product>`: `ndvi`
- `<sensor>`: `landsat8`
- `<aoi>`: short slug (e.g., `kansas`, `ks_counties`, `tile_14T`)
- `<start>--<end>`: ISO dates (`YYYY-MM-DD`)
- `<scale>`: `30m` (or actual)
- `<crs>`: `epsgXXXX` or `utm14n` (be consistent)
- `<variant>`: `cog`, `preview`, `zonal__counties`, `mask`, `qa`, etc.

**Examples (illustrative):**

- `ndvi__landsat8__kansas__2025-12-01--2026-01-02__30m__epsg32614__cog.tif`
- `ndvi__landsat8__kansas__2025-12-01--2026-01-02__30m__epsg32614__preview.png`
- `ndvi__landsat8__kansas__2025-12-01--2026-01-02__zonal__counties.csv`

---

## 🧾 Export manifest contract

### `export_manifest.json` (required)

This file is the single source of truth describing what is inside `exports/`.

Minimum fields to capture:

- `experiment_id`
- `run_id` (timestamp and/or git hash)
- `created_at` (UTC)
- `aoi` (name + geometry reference)
- `inputs` (dataset ids, processing level, filters)
- `processing` (reducers, cloud mask approach, compositing method)
- `exports[]` (one entry per file):
  - `path`
  - `type` (`raster` / `preview` / `table` / `metadata`)
  - `format`
  - `crs`, `scale`
  - `nodata`
  - `stats` (min/max/mean if available)
  - `sha256`
- `known_issues` (if any)

> [!TIP]
> Keep the manifest small and machine-readable. Put long run logs in `logs/`.

### `checksums.sha256` (required)

A flat sha256 list (compatible with `sha256sum -c`) for all exported artifacts.

---

## 🧪 QA / sanity checks

Before treating an export as “ready for downstream use”, verify:

- ✅ NDVI range makes sense (normally within `[-1, 1]`)
- ✅ CRS + scale match the run configuration (e.g., 30 m)
- ✅ No unexpected striping / seam lines in mosaics
- ✅ Cloud/shadow masking strategy recorded (and, ideally, exported as a separate mask layer)
- ✅ Nodata is explicit and consistent

<details>
<summary><strong>Quick commands (GDAL / Rasterio)</strong></summary>

```bash
# Basic inspection
gdalinfo -stats raster/ndvi__*.tif

# If you have rio-cogeo installed, validate COG compliance
rio cogeo validate raster/ndvi__*.tif

# Verify checksums
sha256sum -c checksums.sha256
```

</details>

---

## 🚀 Promoting exports to “processed” (publishing checklist)

Exports are **not considered published** until they are:

1. ✅ Stored in the canonical processed area (`data/processed/…`)
2. ✅ Registered in the project catalog (STAC/DCAT/PROV)
3. ✅ Reproducible (config + run metadata captured)
4. ✅ QA’d (basic checks pass)

### Definition of Done ✅

- [ ] COG GeoTIFF created (tiling + internal overviews + compression)
- [ ] Preview image(s) created for docs/PRs
- [ ] `export_manifest.json` present and complete
- [ ] `checksums.sha256` present and verified
- [ ] STAC item/collection created (asset HREFs point at processed files)
- [ ] DCAT record created (dataset + distributions)
- [ ] PROV record created (inputs → process → outputs)
- [ ] Any known issues captured in the manifest (or a short `KNOWN_ISSUES.md`)

---

## 🔒 Safety & governance

- 🔑 Never commit secrets (API keys, tokens, service accounts) into this folder.
- 🧾 If an export could contain sensitive location data, follow the project’s data classification rules **before** publishing.

---

## 🧯 Troubleshooting

<details>
<summary><strong>Common Earth Engine export issues</strong></summary>

- **Task stuck / fails:** check the Tasks panel + export logs; break AOI into tiles; reduce `maxPixels`.
- **Empty raster:** AOI or date filter returned no images; cloud mask too aggressive.
- **Weird NDVI values:** confirm reflectance scaling, band mapping, and masking order.
- **CRS surprises:** ensure you explicitly set projection/scale during export.
</details>

