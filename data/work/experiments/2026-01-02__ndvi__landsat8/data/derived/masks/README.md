# 🧩 Derived Masks — NDVI (Landsat 8)

![experiment](https://img.shields.io/badge/experiment-2026--01--02__ndvi__landsat8-blue)
![artifact](https://img.shields.io/badge/artifact-derived%20masks-orange)
![sensor](https://img.shields.io/badge/sensor-Landsat%208-success)
![index](https://img.shields.io/badge/index-NDVI-6f42c1)
![format](https://img.shields.io/badge/format-GeoTIFF%20%7C%20COG-lightgrey)
![status](https://img.shields.io/badge/status-regeneratable-brightgreen)

> 🧠 **These files are derived artifacts.** If you delete/rebuild this folder, you should be able to regenerate it from the experiment pipeline (no hand-edits).

🔗 **Jump back:** [`../../../README.md`](../../../README.md) (experiment root)

---

## 🧭 Quick navigation

- [📌 What is this folder?](#-what-is-this-folder)
- [🗂️ Folder contract](#️-folder-contract)
- [🧾 Mask catalog](#-mask-catalog)
- [🧠 How masks are built](#-how-masks-are-built)
- [🧮 How masks are used in NDVI](#-how-masks-are-used-in-ndvi)
- [✅ QC checklist](#-qc-checklist)
- [🛠️ Quick usage (Python)](#️-quick-usage-python)
- [♻️ Regenerating masks](#️-regenerating-masks)
- [⚠️ Known limitations](#️-known-limitations)
- [🗒️ Changelog](#️-changelog)

---

## 📌 What is this folder?

This directory contains **mask rasters** used by the `2026-01-02__ndvi__landsat8` experiment to:

- 🧼 remove invalid pixels before computing or exporting NDVI (clouds, shadows, snow, water, fill/no-data, saturation)
- 📉 track quality metrics (e.g., % clear pixels vs. % cloud/shadow)
- 🧩 keep downstream analysis consistent (all rasters share the same grid as the derived NDVI product)

Typical “good pixel” definition for NDVI is:

- ✅ **clear**
- ❌ not cloud / not cirrus / not dilated cloud
- ❌ not cloud shadow
- ❌ not snow (often excluded)
- ❌ not water (often excluded)
- ❌ not saturated (QA_RADSAT)

> ⚠️ If your experiment intentionally includes snow or water for a specific analysis, document the rule change here (and bump the mask version in filenames).

---

## 🗂️ Folder contract

### 📍 Location (context)

```text
data/work/experiments/2026-01-02__ndvi__landsat8/
└── data/
    └── derived/
        ├── ndvi/          # NDVI outputs (rasters, composites, summaries)
        └── masks/         # 👈 you are here
            └── README.md
```

### 🧱 Required properties (must-haves)

All mask rasters in this folder should satisfy:

- 🧭 **Same CRS / transform / resolution / extent** as the derived NDVI raster(s)
- 🧮 **Pixel-perfect alignment** (no half-pixel drift)
- 🧊 Stored as:
  - `uint8` (recommended), where values are **0/1**, _or_
  - a **1-valued raster with NoData elsewhere** (common when exported from Earth Engine)
- 🏷️ **NoData** is set (if the format uses NoData)
- 🧷 Filenames are **stable and parseable** (see naming scheme below)

### 🏷️ Naming scheme (recommended)

Use double-underscore separators (consistent with experiment folder naming):

- **Class masks** (flags):  
  `qa_pixel__cloud.tif`, `qa_pixel__snow.tif`, `qa_pixel__water.tif`, etc.

- **Composite validity masks** (keep/drop):  
  `valid__ndvi.tif` (single “source of truth” for NDVI pixel validity)

- **Optional versioning** (highly recommended when experimenting):  
  `valid__ndvi__v01.tif`, `valid__ndvi__v02.tif`

> ✅ Rule of thumb: **class masks describe what a pixel *is***, while **valid masks describe whether we *keep* the pixel**.

---

## 🧾 Mask catalog

> This table describes the *intended* mask set. If files differ, update this catalog so the folder remains self-documenting 📚.

| Mask (file) | Type | “True” means… ✅ | Primary source |
|---|---:|---|---|
| `valid__ndvi.tif` | keep/drop | pixel is safe to use for NDVI | composite of QA masks + AOI |
| `qa_pixel__clear.tif` | class | pixel is flagged “clear” | Landsat `QA_PIXEL` |
| `qa_pixel__cloud.tif` | class | pixel is cloud | Landsat `QA_PIXEL` |
| `qa_pixel__cirrus.tif` | class | pixel has cirrus | Landsat `QA_PIXEL` |
| `qa_pixel__dilated_cloud.tif` | class | pixel is dilated cloud | Landsat `QA_PIXEL` |
| `qa_pixel__cloud_shadow.tif` | class | pixel is cloud shadow | Landsat `QA_PIXEL` |
| `qa_pixel__snow.tif` | class | pixel is snow/ice | Landsat `QA_PIXEL` |
| `qa_pixel__water.tif` | class | pixel is water | Landsat `QA_PIXEL` |
| `qa_pixel__fill.tif` | class | pixel is fill / no-data | Landsat `QA_PIXEL` |
| `qa_radsat__ok.tif` | keep/drop | pixel is *not* radiometrically saturated | Landsat `QA_RADSAT` |
| `aoi__mask.tif` | keep/drop | pixel is inside AOI (e.g., Kansas boundary / study area) | vector AOI rasterized |

### ✅ Truthiness conventions

To avoid “mask confusion” in downstream code:

- **Class masks:** `1 = present`, `0 = not present`  
  (or `1` with NoData elsewhere)
- **Validity masks:** `1 = keep`, `0 = drop`  
  (or `1` with NoData elsewhere)

> 🔍 Practical tip: when a mask is exported with NoData outside the mask, treat **NoData as False** in code unless explicitly documented otherwise.

---

## 🧠 How masks are built

### 🛰️ Landsat 8 QA_PIXEL bit reference (Collection 2 Level-2)

`QA_PIXEL` is a **bit-packed** quality band. The commonly used bits are:

| Bit | Value | Meaning |
|---:|---:|---|
| 0 | 1 | Fill |
| 1 | 2 | Dilated cloud |
| 2 | 4 | Cirrus |
| 3 | 8 | Cloud |
| 4 | 16 | Cloud shadow |
| 5 | 32 | Snow |
| 6 | 64 | Clear |
| 7 | 128 | Water |

<details>
<summary>🧩 Example logic (conceptual)</summary>

- **Clear candidate:** `clear = (QA_PIXEL & 64) != 0`
- **Cloud/shadow tests:**  
  `cloud = (QA_PIXEL & 8) != 0`  
  `shadow = (QA_PIXEL & 16) != 0`  
  `cirrus = (QA_PIXEL & 4) != 0`  
  `dilated = (QA_PIXEL & 2) != 0`
- **Often excluded from NDVI:**  
  `snow = (QA_PIXEL & 32) != 0`  
  `water = (QA_PIXEL & 128) != 0`
- **Always excluded:**  
  `fill = (QA_PIXEL & 1) != 0`

A typical NDVI-valid mask:

- `valid = clear`
- `valid &= ~fill & ~cloud & ~shadow & ~cirrus & ~dilated`
- `valid &= ~snow` (if configured)
- `valid &= ~water` (if configured)
- `valid &= radsat_ok`
- `valid &= aoi_mask`

</details>

### ☢️ QA_RADSAT (saturation)

`QA_RADSAT` flags saturated pixels. A common rule is:

- `radsat_ok = (QA_RADSAT == 0)` ✅

---

## 🧮 How masks are used in NDVI

NDVI is computed per-pixel as:

- 🌱 `NDVI = (NIR - Red) / (NIR + Red)`

For Landsat 8 surface reflectance, common band mapping is:

- 🔴 Red: `SR_B4`
- 🟣 NIR: `SR_B5`

**Mask application rule (recommended):**

- compute NDVI
- apply `valid__ndvi` so invalid pixels become NoData (or NaN)

> ✅ Always apply the *same* validity definition to both the exported NDVI raster and any zonal stats / summaries, or you’ll get mismatched results.

---

## ✅ QC checklist

Before using masks downstream:

- [ ] **Alignment:** `crs`, `transform`, `width`, `height` match NDVI rasters
- [ ] **Value sanity:** masks are binary-ish (0/1) OR “1 with NoData elsewhere”
- [ ] **Coverage sanity:** `% valid` is not ~0% or ~100% unless expected
- [ ] **Visual spot-check:** overlay masks on a quick RGB composite (clouds/shadows make sense)
- [ ] **NoData sanity:** NoData is consistent (and documented) across masks

📉 Suggested metrics to record (per scene or composite):

- `%clear`, `%cloud`, `%shadow`, `%snow`, `%water`, `%valid_ndvi`

---

## 🛠️ Quick usage (Python)

> These snippets are intentionally “boring and robust” 😄 — adjust to your pipeline conventions.

### 1) Load NDVI + a validity mask and apply it

```python
import numpy as np
import rasterio

ndvi_path = "../ndvi/ndvi.tif"
mask_path = "valid__ndvi.tif"

with rasterio.open(ndvi_path) as nd:
    ndvi = nd.read(1).astype("float32")
    nd_profile = nd.profile

with rasterio.open(mask_path) as m:
    mask = m.read(1)
    # Option A: mask is 0/1
    valid_a = mask.astype(bool)

    # Option B: mask is 1-with-nodata elsewhere (NoData means invalid)
    # valid_b = m.read_masks(1) > 0

valid = valid_a  # swap to valid_b if that matches your export style
ndvi_masked = np.where(valid, ndvi, np.nan)
```

### 2) Quick alignment assertions

```python
import rasterio

ndvi_path = "../ndvi/ndvi.tif"
mask_path = "valid__ndvi.tif"

with rasterio.open(ndvi_path) as nd, rasterio.open(mask_path) as m:
    assert nd.crs == m.crs
    assert nd.transform == m.transform
    assert (nd.width, nd.height) == (m.width, m.height)
```

### 3) Compute a “valid pixel ratio”

```python
import numpy as np
import rasterio

mask_path = "valid__ndvi.tif"

with rasterio.open(mask_path) as m:
    arr = m.read(1)
    valid = arr.astype(bool)
    ratio = valid.mean()

print(f"valid_pixel_ratio = {ratio:.3%}")
```

---

## ♻️ Regenerating masks

If you need to regenerate:

1. 🔎 Identify the **source imagery selection** used in this experiment (time window, AOI, collection ID).
2. 🧠 Re-run the pipeline step that:
   - decodes `QA_PIXEL` + `QA_RADSAT`
   - rasterizes AOI (if used)
   - builds `valid__ndvi`
3. 📌 Ensure outputs land back in this folder and update:
   - the [Mask catalog](#-mask-catalog)
   - the [Changelog](#️-changelog)
   - any version suffixes in filenames (`__v02`, etc.)

> 🧯 Avoid “manual fixes” to masks. If a rule is wrong, fix it in code and regenerate so results stay reproducible.

---

## ⚠️ Known limitations

- ☁️ **Cloud masking is imperfect** — bright surfaces, snow/ice, and urban areas can trigger false positives.
- 🕶️ Shadows can be subtle and may slip through depending on the QA method used.
- 🧊 Snow/water handling is **analysis-dependent**: some workflows exclude them for vegetation analysis (typical), but hydrology or phenology tasks may treat them differently.
- 🧬 Different compositing strategies (median/percentile/“best pixel”) can change the effective mask behavior — document the approach at the experiment root.

---

## 🗒️ Changelog

- **2026-01-03** 📝 Created folder README and defined mask contract + conventions.
- **TBD** 🔁 Update entries as masks are regenerated / versioned.

