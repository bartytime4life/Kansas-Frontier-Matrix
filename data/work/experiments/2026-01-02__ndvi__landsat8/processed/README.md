---
kfm:
  artifact_type: experiment_processed_outputs
  experiment_id: 2026-01-02__ndvi__landsat8
  created: 2026-01-02
  stage: data/work/experiments/*/processed
  product: NDVI
  sensor: Landsat 8
  status: draft
---

# 🛰️🌿 NDVI (Landsat 8) — Processed Outputs

![stage](https://img.shields.io/badge/stage-work%2Fprocessed-blue)
![sensor](https://img.shields.io/badge/sensor-Landsat%208-6aa84f)
![product](https://img.shields.io/badge/product-NDVI-3d85c6)
![run](https://img.shields.io/badge/run-2026--01--02-lightgrey)
![formats](https://img.shields.io/badge/formats-GeoTIFF%20%7C%20COG%20%7C%20PNG-orange)

> ⚠️ **Work-stage artifact:** This folder contains processed outputs for an *experiment run* (not yet “published” / canonical).  
> ✅ Use for analysis + review; promote only after QC + provenance + metadata are complete.

---

## 📍 Location

`data/work/experiments/2026-01-02__ndvi__landsat8/processed/`

**Related (if present):**
- ⬆️ Experiment root: `../README.md`
- ⚙️ Run config: `../run_config.*` or `../config/`
- 📜 Logs: `../logs/`
- 🧪 Notebooks / scripts: `../src/` or `../notebooks/`

---

## 📌 TL;DR

This directory should contain:
- **NDVI raster(s)** (prefer `.cog.tif`)
- **Quicklook image(s)** (`.png`) for visual diffing
- **Stats tables** (`.csv`) for sanity checks + QA
- **Run manifest** (`run_manifest.json`) so outputs are reproducible + auditable

---

## 🧾 Run metadata (fill in & keep accurate)

| Field | Value |
|---|---|
| AOI / ROI | `TODO (name + file/path to boundary)` |
| Date range | `TODO (YYYY-MM-DD → YYYY-MM-DD)` |
| Landsat collection | `TODO (e.g., LANDSAT/LC08/C02/T1_L2)` |
| Cloud/shadow mask | `TODO (QA bits / thresholds / method)` |
| Composite method | `TODO (median / max NDVI / percentile / best-pixel)` |
| Output CRS | `TODO (EPSG:####)` |
| Pixel size | `TODO (m; Landsat typically 30 m)` |
| NoData | `TODO (value + rationale)` |
| Code commit | `TODO (git sha)` |
| Environment | `TODO (conda env / docker image / requirements hash)` |
| Runner | `TODO (@handle)` |
| Run ID | `TODO (uuid/timestamp)` |

---

## 🗂️ Folder contents

### 🌳 Expected layout (example)

```text
📦 processed/                                                           # 🧪 Experiment outputs (work-stage “processed” artifacts)
├── 📘 README.md                                                         # 👈 You are here — folder contract, QC notes, promotion rules
├── 🧾 run_manifest.json                                                 # 🔗 Run manifest — inputs → params → outputs (+ hashes/refs)
├── 🛰️🌿🗺️ ndvi__<roi>__<start>_<end>__landsat8__30m.cog.tif             # 🧱 Primary NDVI raster — Cloud-Optimized GeoTIFF (COG)
├── 🖼️ ndvi__<roi>__<start>_<end>__landsat8__30m.preview.png            # 👀 Quicklook — visual QA / PR diff / spot cloud artifacts fast
├── 📊 ndvi__<roi>__<start>_<end>__landsat8__30m.stats.csv              # 🧮 Summary stats — min/max/mean/std, pixel counts, % masked
└── 🛡️☁️ mask__<...>.tif                                                # (optional) QA mask — clouds/shadows/snow/water (if exported)
```

### 📦 Artifact inventory (update after every run)

| File / Pattern | Type | What it is | Required |
|---|---|---|---|
| `ndvi__*.tif` (prefer `*.cog.tif`) | Raster | Primary NDVI output | ✅ |
| `ndvi__*_preview.png` | Image | Quicklook / PR-friendly visualization | ✅ |
| `ndvi__*_stats.csv` | Table | Summary stats (min/max/mean/std, pixel counts, % masked) | ✅ |
| `ndvi__*_histogram.csv` | Table | Binned histogram for distribution checks | ⭕ |
| `mask__*.tif` | Raster | Cloud/shadow/snow/water mask (if exported) | ⭕ |
| `run_manifest.json` | JSON | Inputs → processing → outputs (machine-readable) | ✅ |
| `stac_item.json` | JSON | STAC Item (needed when publishing) | ⭕ |
| `prov.json` / `prov.ttl` | PROV | Lineage bundle (needed when publishing) | ⭕ |

---

## 🧮 NDVI definition & band mapping

NDVI is defined as:

\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

**Band mapping (typical for Landsat 8 Surface Reflectance in GEE):**
- **NIR:** `SR_B5`
- **Red:** `SR_B4`

Example (GEE JavaScript reference pattern):

```js
// Landsat 8 Collection 2 Tier 1 Level 2 (Surface Reflectance)
var ndvi = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterBounds(regionInt)
  .filterDate('YYYY-MM-DD', 'YYYY-MM-DD')
  // .filter(<cloud filter>)  // TODO: record exact filter
  .median()                  // TODO: record composite method
  .normalizedDifference(['SR_B5', 'SR_B4'])
  .rename('NDVI')
  .clip(regionInt);
```

> 🧠 **Sanity note:** NDVI should typically remain within `[-1, 1]` (minor float epsilon is ok).  
> If your output exceeds this range, treat it as a QA failure until explained.

---

## 🔁 Processing pipeline (conceptual)

```mermaid
flowchart LR
  A[🛰️ Landsat 8 SR] --> B[☁️ QA Mask (cloud/shadow/snow)]
  B --> C[🌿 NDVI per-scene]
  C --> D[🧩 Composite / Mosaic]
  D --> E[📦 Export GeoTIFF/COG + Preview]
  E --> F[📊 Stats + Hist + QA]
  F --> G[🧾 Manifest + (Publish: STAC/DCAT/PROV)]
```

### ✅ Minimum steps we expect were done

1. **Select inputs:** AOI + time window + dataset selection  
2. **Mask:** clouds/shadows (and optionally snow/water)  
3. **Compute NDVI**  
4. **Composite:** reduce over time (median/max/percentile/etc.)  
5. **Export:** raster(s) + quicklook(s)  
6. **Summarize:** stats + pixel counts + masked %  
7. **Record:** manifest + run metadata (and when publishing: STAC/DCAT/PROV)

<details>
<summary>🧠 Optional enhancements (only list these if the run actually used them)</summary>

- Best-available-pixel compositing (BAP)  
- Temporal smoothing / gap-filling  
- Quality band export (clear vs climatology vs smoothed, etc.)  
- Cross-sensor harmonization (e.g., L5/L7/L8/L9)  
- BRDF / terrain correction

</details>

---

## ✅ QC checklist (don’t skip)

### 🔍 Numeric + metadata checks
- [ ] NDVI range in `[-1, 1]` (or explain exceptions)
- [ ] CRS + resolution match the run metadata
- [ ] NoData correctly set (and not colliding with valid NDVI values)
- [ ] Masked % recorded (and plausible)

### 🗺️ Visual checks
- [ ] Quicklook looks correctly oriented (no flips/rotations)
- [ ] No obvious cloud contamination / striping / seams
- [ ] AOI edges align (no unexpected clipping or padding)

### 🔁 Reproducibility checks
- [ ] Code commit recorded
- [ ] Config recorded (exact parameters)
- [ ] Rerun produces identical output (or differences are explained)
- [ ] `run_manifest.json` present and complete

---

## 🧾 `run_manifest.json` (recommended schema)

> 📌 Treat this like a *mini lab-notebook entry* for the produced files.

```json
{
  "experiment_id": "2026-01-02__ndvi__landsat8",
  "generated_at": "2026-01-02T00:00:00Z",
  "aoi": {
    "name": "TODO",
    "source": "TODO (path or reference)"
  },
  "inputs": [
    {
      "source": "TODO (GEE collection / local catalog id)",
      "dataset_id": "LANDSAT/LC08/C02/T1_L2",
      "date_range": ["TODO", "TODO"],
      "filters": {
        "cloud": "TODO",
        "other": "TODO"
      }
    }
  ],
  "processing": {
    "masking": "TODO (QA bits / logic)",
    "ndvi_bands": {"nir": "SR_B5", "red": "SR_B4"},
    "composite": "TODO (median/max/percentile/etc.)"
  },
  "outputs": [
    {
      "path": "ndvi__...cog.tif",
      "role": "primary_raster",
      "sha256": "TODO",
      "nodata": "TODO",
      "crs": "TODO",
      "pixel_size_m": 30
    },
    {
      "path": "ndvi__...preview.png",
      "role": "quicklook",
      "sha256": "TODO"
    },
    {
      "path": "ndvi__...stats.csv",
      "role": "summary_stats",
      "sha256": "TODO"
    }
  ],
  "environment": {
    "code_commit": "TODO",
    "runner": "TODO",
    "container": "TODO (image digest/tag)",
    "deps": "TODO (requirements lock hash)"
  }
}
```

---

## 🗺️ Using the outputs (QGIS / GIS quick tips)

- Prefer loading `*.cog.tif` (fast overviews + streaming-friendly).
- Use a diverging ramp centered near `0.0` for interpretation.
- If doing zonal stats: store **pixel counts** and **masked %** with the results.

---

## 📤 Promotion to canonical datasets (when ready)

> 📌 If these outputs graduate beyond “experiment artifacts”, promote them to `data/processed/<domain>/...` and generate the required metadata/lineage bundles.

**Definition of Done (publish-ready):**
- [ ] QC checklist is fully green ✅
- [ ] Stable naming/versioning applied
- [ ] STAC + DCAT + PROV generated (or linked)  
- [ ] Provenance is traceable from raw → work → processed
- [ ] Peer review / second set of eyes (recommended)

---

## 🧾 Traceability matrix (mini)

| Experiment ID | Output | Code commit | Config ref | Notes |
|---|---|---|---|---|
| `2026-01-02__ndvi__landsat8` | `ndvi__*.tif` | `TODO` | `TODO` | `TODO` |

---

## 📝 Changelog

| Date | Change | By |
|---|---|---|
| 2026-01-02 | Initial processed outputs generated | `TODO` |

---

## 🔒 House rules

- 🧊 **No hand edits** to rasters: regenerate so lineage stays clean.
- 🧾 Keep the manifest + metadata accurate (they’re part of the deliverable).
- 🧱 If files are huge: follow the project’s large-file storage policy and keep pointers + checksums here.

