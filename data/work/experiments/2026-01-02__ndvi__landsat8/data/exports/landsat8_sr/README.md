# 🛰️ Landsat 8 Surface Reflectance (SR) — Export Artifacts 🌿

![Sensor](https://img.shields.io/badge/Sensor-Landsat%208-0b5394)
![Product](https://img.shields.io/badge/Product-Collection%202%20%7C%20Level--2%20SR-2e7d32)
![Primary%20use](https://img.shields.io/badge/Primary%20Use-NDVI%20Inputs-6a1b9a)
![Resolution](https://img.shields.io/badge/Resolution-30m-f9a825)
![Format](https://img.shields.io/badge/Format-GeoTIFF%20%2F%20COG-f57c00)
![Folder%20type](https://img.shields.io/badge/Folder-Generated%20Export%20Artifact-616161)

> 📌 **Path:** `data/work/experiments/2026-01-02__ndvi__landsat8/data/exports/landsat8_sr/`  
> 🧪 **Experiment:** `2026-01-02__ndvi__landsat8`  
> 🧱 **Role:** “Source imagery” exports used to derive NDVI + downstream analytics (not the final NDVI product)

---

## 🧭 Navigation

- ⬅️ Back to **experiment root**: `../../..`
- ⬆️ Back to **exports index**: `..`

---

## ✅ What this folder is

This directory stores **exported Landsat 8 Surface Reflectance (SR)** imagery used as **inputs** for the NDVI experiment run dated **2026‑01‑02**.

Think of these files as the **frozen, local copy** of the “analysis-ready” imagery after cloud masking + scaling decisions were applied (or at minimum, recorded). They exist so the rest of the pipeline can be:

- **repeatable** 🔁 (same inputs → same outputs)
- **offline-friendly** 📴 (don’t depend on external services once exported)
- **auditable** 🧾 (clear provenance + QA)

> ⚠️ This folder is **generated**. Prefer re-exporting/regenerating over manual edits.

---

## 📦 What you should expect to find here

Exact filenames may vary per run, but exports typically fall into one of these shapes:

### Option A: **Single multi-band raster** (recommended)
- `landsat8_sr__<roi>__<start>__<end>__v<run>.tif` ✅

Band order is typically:
1. `SR_B2` (Blue)
2. `SR_B3` (Green)
3. `SR_B4` (Red)
4. `SR_B5` (NIR)
5. `SR_B6` (SWIR1)
6. `SR_B7` (SWIR2)
(+ optional QA/thermal bands)

### Option B: **One file per band** (acceptable)
- `landsat8_sr__<roi>__<date>__SR_B4.tif`
- `landsat8_sr__<roi>__<date>__SR_B5.tif`
- …

### Option C: **Per-scene exports**
- One export per Landsat scene ID (useful for debugging, heavier storage)

### Suggested companion files (highly recommended)
- `metadata.json` 📄 (run config + scale/offset + ROI + date window)
- `manifest.json` 🧾 (checksums, file list, versions)
- `export.log` 🪵 (export task IDs, timestamps, parameters)

---

## 🗂️ Quick folder tree (example)

```text
📁 landsat8_sr/
├─ 📄 README.md
├─ 🗺️ landsat8_sr__ks_aoi__2025-12-15__2026-01-15__v001.tif
├─ 📄 metadata.json
├─ 📄 manifest.json
└─ 📁 logs/
   └─ 📄 export_gee_tasks.log
```

---

## 🔎 Data provenance

### Canonical source (typical)
Most KFM NDVI workflows pull Landsat 8 SR from Google Earth Engine (GEE), using the **USGS Landsat 8 Level‑2, Collection 2** products.

Typical collection ID used in GEE:
- `LANDSAT/LC08/C02/T1_L2`

### Typical spatial/temporal filtering
- **ROI**: experiment AOI geometry (Kansas region / subregion)
- **Date window**: centered around the experiment date (Landsat revisit is not daily)

> 📝 If you export a *composite* (median/max/least-cloudy), record the reducer and the time window in `metadata.json`.

---

## 🎛️ Band dictionary (Landsat 8 SR)

| Band | Common name | Use in NDVI? | Notes |
|------|-------------|--------------|------|
| `SR_B2` | Blue | ❌ | haze/aerosol sensitive |
| `SR_B3` | Green | ❌ | useful for visual composites |
| `SR_B4` | **Red** | ✅ | NDVI denominator + vegetation absorption |
| `SR_B5` | **NIR** | ✅ | NDVI numerator + vegetation reflectance |
| `SR_B6` | SWIR1 | ❌ | moisture / burn / soil signals |
| `SR_B7` | SWIR2 | ❌ | moisture / burn / geology signals |

> 🌿 NDVI uses **NIR vs Red** → `SR_B5` and `SR_B4`.

---

## ☁️ Cloud/quality masking (important)

### QA intent
Landsat Level‑2 includes pixel QA bands that allow masking out:
- fill pixels
- clouds (including dilated clouds)
- cirrus
- cloud shadow
- radiometric saturation

### Common “strict” mask rule (bits 0–4 must be 0)
Mask if any of these are flagged:
- Fill
- Dilated cloud
- Cirrus
- Cloud
- Cloud shadow

Also mask radiometric saturation (`QA_RADSAT == 0`).

> ✅ If NDVI looks “peppered” or implausibly low, your cloud/shadow mask is the first thing to check.

---

## 📏 Scaling & units (don’t skip this)

Landsat Collection 2 Level‑2 SR optical bands often require **scale + offset** to convert to reflectance-like values:

- **Optical SR**: `SR * 0.0000275 + (-0.2)`

Thermal bands (if present) use a different scale/offset.

### Practical guidance
- **If exports are float reflectance** (recommended): scaling has already been applied.
- **If exports are int DN**: apply the scale/offset before computing NDVI.
- It’s okay to see some negative values *before* masking/cleanup due to the offset; mask clouds/shadows first.

---

## 🧮 How NDVI is computed (from these exports)

### Formula
\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

For Landsat 8 SR:
- `NIR = SR_B5`
- `Red = SR_B4`

---

## 🐍 Python example (rasterio + NumPy)

> Assumes a single multi-band GeoTIFF in band order: B2, B3, **B4**, **B5**, B6, B7.

```python
import numpy as np
import rasterio

src_path = "landsat8_sr__<roi>__<start>__<end>__v<run>.tif"

with rasterio.open(src_path) as src:
    red = src.read(3).astype("float32")  # SR_B4
    nir = src.read(4).astype("float32")  # SR_B5

    # If your export is NOT already scaled, uncomment:
    # red = red * 0.0000275 - 0.2
    # nir = nir * 0.0000275 - 0.2

    denom = (nir + red)
    ndvi = np.where(denom != 0, (nir - red) / denom, np.nan)

print(np.nanmin(ndvi), np.nanmax(ndvi))
```

---

## 🧰 GEE export pattern (reference snippet)

<details>
<summary><strong>Click to expand: Earth Engine masking + scaling + export skeleton</strong> 📤</summary>

```javascript
// ROI + date window come from experiment config.
var roi = /* your geometry */;
var startDate = '2025-12-15';
var endDate   = '2026-01-15';

// Mask clouds + saturation, apply scale factors.
function maskAndScaleL8L2(image) {
  var qaMask = image.select('QA_PIXEL')
    .bitwiseAnd(parseInt('11111', 2))  // bits 0-4
    .eq(0);

  var saturationMask = image.select('QA_RADSAT').eq(0);

  var optical = image.select('SR_B.')
    .multiply(0.0000275)
    .add(-0.2);

  // Optional thermal scaling if you need ST bands:
  // var thermal = image.select('ST_B.*')
  //   .multiply(0.00341802)
  //   .add(149.0);

  return image
    .addBands(optical, null, true)
    // .addBands(thermal, null, true)
    .updateMask(qaMask)
    .updateMask(saturationMask);
}

var landsat8sr = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterBounds(roi)
  .filterDate(startDate, endDate)
  .map(maskAndScaleL8L2);

// Choose a composite strategy (document which one you used!)
var composite = landsat8sr.median().clip(roi);

// Export SR bands for downstream NDVI.
Export.image.toDrive({
  image: composite.select(['SR_B2','SR_B3','SR_B4','SR_B5','SR_B6','SR_B7']),
  description: 'landsat8_sr__<roi>__' + startDate + '__' + endDate,
  region: roi,
  scale: 30,
  maxPixels: 1e13
});
```
</details>

---

## ✅ Validation checklist (fast)

Run these checks before trusting NDVI outputs:

- [ ] **CRS + pixel size** look correct (`gdalinfo <file>.tif`)
- [ ] **NoData** is set and consistent across bands
- [ ] **Band order** is known (write it down in `metadata.json`)
- [ ] **Scaling applied** (or explicitly deferred) ✅
- [ ] **NDVI range** makes sense (rough sanity: land ∈ [-1, 1], healthy veg often > 0.4)
- [ ] Visual spot-check in QGIS: do clouds/shadows look masked?

---

## 🧊 Storage & versioning notes

These rasters can be large. Recommended practices:

- Prefer **COG** for large GeoTIFFs (faster reads + cloud/web workflows)
- Use **Git LFS** or **DVC** for large binary artifacts
- Keep `metadata.json` / `manifest.json` small + human-readable
- Don’t hand-edit rasters; regenerate from source steps 🔁

---

## 🧾 “Data contract” for this directory

✅ **Allowed**
- Add/refresh exports via pipeline
- Add metadata + manifest
- Add logs and checksums

🚫 **Not allowed**
- Manually editing pixels/bands
- Renaming files without updating manifest/metadata
- Mixing multiple unrelated runs without versioning

---

## 🗒️ Changelog

- **2026‑01‑02:** Folder created for `2026-01-02__ndvi__landsat8` SR export artifacts.

