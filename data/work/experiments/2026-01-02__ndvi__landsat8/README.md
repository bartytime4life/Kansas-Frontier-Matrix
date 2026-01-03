---
title: "🛰️🌿 NDVI from Landsat 8 — Experiment 2026-01-02"
path: "data/work/experiments/2026-01-02__ndvi__landsat8/README.md"
version: "v0.1.0"
last_updated: "2026-01-02"
status: "draft"
doc_kind: "Experiment README"
license: "CC-BY-4.0"

# Profile / contract versions (keep fields; use TBD vs deleting)
markdown_protocol_version: "v13"
pipeline_contract_version: "TBD"

# Governance & compliance (do not publish until these are resolved)
governance_ref: "TBD"
ethics_ref: "TBD"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "internal"
classification: "internal"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:experiments:ndvi:landsat8:2026-01-02:v0.1.0"
commit_sha: "<commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"

owners:
  - "<your-handle>"
tags:
  - ndvi
  - landsat8
  - remote-sensing
  - google-earth-engine
  - kfm
---

# 🧪 Experiment: 2026-01-02 — NDVI (Landsat 8) 🌿🛰️

| 🧷 Key | Value |
|---|---|
| Experiment folder | `data/work/experiments/2026-01-02__ndvi__landsat8/` |
| Status | 🟧 Draft (working runbook + reproducibility scaffold) |
| Primary output | NDVI raster(s) + optional field-level stats |
| Target integration | KFM NDVI ingestion → `field_health_index` + raster tiles |
| Spatial resolution | 30 m (Landsat-class) |
| Temporal cadence | ~16-day revisit window (sensor cadence; composites recommended) |

> 🧠 **Why this folder lives in `data/work/…`**  
> KFM’s data lifecycle explicitly separates `data/raw` → `data/work` → `data/processed` → `data/published`. This experiment is a *work-stage* sandbox until QA + metadata gates are passed. :contentReference[oaicite:0]{index=0}

---

## 📘 Overview

### Purpose
Create a reproducible NDVI pipeline from **Landsat 8** imagery and validate that outputs can be promoted into KFM’s production flow (raster storage + field-level table updates).

### Scope

| ✅ In scope | 🚫 Out of scope (for this experiment) |
|---|---|
| Cloud-masked Landsat 8 SR → NDVI | Multi-sensor harmonization (L5/L7/L9) |
| Composite NDVI (median / best-pixel) | Long-term climatology buildout |
| Export GeoTIFF + QC artifacts | Public release / publishing without governance checks |
| Optional zonal stats (fields) | Final API/UI deployment changes |

### Audience
- **Primary:** KFM devs + geospatial analysts building the remote-sensing pipeline  
- **Secondary:** reviewers validating governance / provenance / QA expectations

### Definitions
- **NDVI:** Normalized Difference Vegetation Index = `(NIR - RED) / (NIR + RED)`.[^ndvi_eq]
- **AOI:** Area of Interest polygon (Kansas boundary, county, watershed, or field set)
- **Composite:** single image derived from multiple scenes (e.g., median NDVI over a date window)

> ✍️ This README follows the project’s “front-matter + standardized sections” approach (keep required fields; use `TBD` rather than deleting).:contentReference[oaicite:1]{index=1}

---

## 🧠 Hypothesis / Objective

**Hypothesis:** With correct scaling + cloud/shadow masking, Landsat 8 surface reflectance can produce stable, physically plausible NDVI rasters suitable for KFM’s *field health* features and raster/tiles layer.

**Success criteria (measurable):**
1. NDVI raster values are within expected bounds `[-1, 1]` and show sensible patterns (water ≈ low/negative; vegetated crops ≈ positive).[^ndvi_range]
2. Cloud/shadow contamination is substantially reduced (visual spot checks + histogram tail reduction).
3. Exported artifacts can be promoted to `data/processed` with metadata + provenance, without bypassing pipeline ordering requirements.[^pipeline_order]

---

## 📦 Inputs

### Remote sensing source
- **Landsat 8** imagery (30 m class) is explicitly called out in KFM as a remote sensing source for indices like NDVI, with ~16-day cadence. :contentReference[oaicite:2]{index=2}

### Required local inputs (expected)
- `data/work/experiments/2026-01-02__ndvi__landsat8/data/aoi.geojson` *(or similar)*  
- *(optional)* `data/work/field_boundaries/...` if computing zonal stats

### Assumed compute options
- **Option A:** Google Earth Engine (recommended for first pass)  
- **Option B:** Local NDVI compute from raster bands (GDAL/NumPy) for offline reproducibility[^local_ndvi]

---

## ⚙️ Method

### 1) Preprocessing (Landsat 8 SR)
**Key steps:**
1. Filter imagery by AOI + date range
2. Apply cloud + cloud-shadow mask using QA band bits
3. Apply SR scale/offset (collection-specific) before index calculation[^l8_mask_scale]

### 2) NDVI calculation
NDVI uses **NIR** and **Red** reflectance:  
\[
NDVI = \frac{NIR - RED}{NIR + RED}
\]
For **Landsat 8**, NDVI is typically computed from **band 5 (NIR)** and **band 4 (Red)**. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

### 3) Temporal compositing
Recommended for stable maps:
- **Median NDVI** over the date window (robust to outliers)
- Or a **quality mosaic** approach (best pixel) if you maintain a quality band

> Landsat-derived NDVI is commonly delivered as **16-day composites**, with cloud masking/quality flags applied. :contentReference[oaicite:5]{index=5}

### 4) Export + storage targets (KFM alignment)
KFM describes an ingestion flow where new satellite imagery is processed to NDVI and stored both as:
- field-level values (e.g., in `field_health_index`), and
- raster outputs (GeoTIFF and/or tiles) for map display. :contentReference[oaicite:6]{index=6}

---

## 🧰 Implementation

### Option A — Google Earth Engine (JS) 🛰️

> ✅ Use this as the canonical first implementation because it matches KFM’s described pipeline:  
> `get_new_satellite_image → process_image_to_NDVI → update_database → …` :contentReference[oaicite:7]{index=7}

```javascript
// ------------------------------------------------------------
// KFM Experiment: NDVI (Landsat 8) — 2026-01-02
// ------------------------------------------------------------

// 0) Parameters (edit these)
var START = '2025-06-01';
var END   = '2025-09-30';
var AOI   = /* color: #d63000 */ ee.Geometry.Polygon(
  [[[ -102.05, 40.00 ], [ -94.60, 40.00 ], [ -94.60, 36.99 ], [ -102.05, 36.99 ]]]
); // TODO: replace with real AOI (Kansas boundary / county / fields)

// 1) Landsat 8 Collection 2 Level-2 SR
var l8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');

// 2) Cloud/shadow mask using QA_PIXEL bits + scale SR reflectance
function maskL8sr(image) {
  var qa = image.select('QA_PIXEL');

  // Bits 3 and 4 are cloud shadow and cloud, respectively (per example implementation).
  var cloudShadowBitMask = (1 << 3);
  var cloudsBitMask = (1 << 4);

  var mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0)
    .and(qa.bitwiseAnd(cloudsBitMask).eq(0));

  // Apply reflectance scaling for SR bands
  var sr = image.select('SR_B.*').multiply(0.0000275).add(-0.2);

  return image.addBands(sr, null, true).updateMask(mask);
}

// 3) NDVI band
function addNDVI(image) {
  var ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('ndvi');
  return image.addBands(ndvi);
}

// 4) Build collection
var col = l8
  .filterBounds(AOI)
  .filterDate(START, END)
  .map(maskL8sr)
  .map(addNDVI);

// 5) Composite
var ndvi_median = col.select('ndvi').median().clip(AOI);

// 6) Visual sanity check
Map.centerObject(AOI, 7);
Map.addLayer(ndvi_median, {min: -1, max: 1}, 'NDVI (median)');

// 7) Export (Drive shown; replace with your KFM export target)
Export.image.toDrive({
  image: ndvi_median,
  description: 'kfm__ndvi__landsat8__median__' + START + '__' + END,
  region: AOI,
  scale: 30,
  maxPixels: 1e13
});
```

**Notes:**
- The QA-bit mask + reflectance scaling constants above are taken directly from an example Landsat 8 SR workflow, and should be treated as the baseline implementation for this experiment. :contentReference[oaicite:8]{index=8}

**Common failure mode (Earth Engine):**  
If you hit “too many pixels” errors when reducing/exporting, consider raising `maxPixels`, increasing `scale`, enabling `bestEffort`, or reducing AOI size. :contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

---

### Option B — Local NDVI (GDAL + NumPy) 🧮

Use this when:
- you’ve exported Red/NIR rasters (or downloaded scenes),
- you want offline determinism + auditability.

Example NDVI computation pattern (mask denominator=0, set NoData):​:contentReference[oaicite:11]{index=11}

```python
import numpy as np
from osgeo import gdal

ds = gdal.Open("input_multiband.tif")
red = ds.GetRasterBand(1).ReadAsArray().astype(float)
nir = ds.GetRasterBand(4).ReadAsArray()

red = np.ma.masked_where(nir + red == 0, red)
ndvi = (nir - red) / (nir + red)
ndvi = ndvi.filled(-99)  # NoData sentinel
```

> ⚠️ Band ordering varies by product. The sample above reads red=Band1 and nir=Band4 in that example dataset; confirm your Landsat export band order before running. :contentReference[oaicite:12]{index=12}

---

## 📂 Expected Folder Layout

This experiment structure is inspired by the project’s “experiments as reproducible units” convention (README + protocol + src + data + results).:contentReference[oaicite:13]{index=13}

```text
🧪 data/work/experiments/2026-01-02__ndvi__landsat8/           # experiment root (this folder)
├── 📄 README.md                                              # 👈 you are here (overview + runbook)
├── 🧾 protocol.md                                            # hypothesis → procedure → metrics → acceptance criteria
├── 🗂️ data/                                                  # inputs (AOI + optional QA geometries)
│   ├── 🗺️ aoi.geojson                                        # AOI geometry (or pointer to canonical boundary)
│   └── 🎯 field_samples.geojson                              # optional: sample polygons/points for QC spot-checks
├── 🧑‍💻 src/                                                 # implementation (Earth Engine + local tooling)
│   ├── 🌍 gee/                                               # GEE scripts (JavaScript)
│   │   └── 📜 ndvi_landsat8.js                                # Landsat 8 SR → QA mask → NDVI → composite → export
│   └── 🐍 python/                                            # Python utilities (stats + QA)
│       ├── 📊 zonal_stats.py                                 # optional: field mean NDVI + p10/p90 + CSV export
│       └── 🧪 qc_ndvi_histogram.py                            # NDVI histogram + range checks + quick plots
└── 🧱 results/                                               # produced artifacts (promotable outputs)
    ├── 🛰️ rasters/                                           # raster deliverables
    │   └── 🗺️ ndvi__landsat8__median__START__END__30m.tif      # final NDVI mosaic (30 m) for the window
    ├── 📈 tables/                                            # tabular deliverables
    │   └── 📄 field_ndvi_stats__START__END.csv                # per-field zonal stats (if enabled)
    ├── ✅ qc/                                                # QA evidence (visual + stats)
    │   ├── 📊 ndvi_histogram.png                              # distribution sanity check (tails/outliers)
    │   └── 🖼️ ndvi_preview.png                                # quicklook map image for eyeballing artifacts
    └── 🧬 logs/                                              # run records (inputs/params/hashes/timings)
        └── 🧾 run__YYYY-MM-DDTHHMMSSZ.json                    # machine-readable run manifest (repro + provenance)
```

---

## ✅ Validation Plan (QC)

### Pixel-level sanity checks
- [ ] NDVI range is within `[-1, 1]` (after scaling & masking).[^ndvi_range]
- [ ] Water bodies ≈ negative; bare soil ≈ near 0; healthy vegetation ≈ high positive.[^ndvi_range]
- [ ] No obvious striping / edge artifacts after compositing.

### Cloud contamination checks
- [ ] Compare NDVI mosaic with/without QA mask on a cloudy day (spot-check)
- [ ] Histogram tail check: masked composite should reduce extreme outliers

### Temporal consistency (optional)
NDVI should generally vary smoothly; abrupt drops can be cloud contamination. A simple smoothing rule used in practice is to replace a value if it drops below the mean of adjacent values by a threshold (e.g., 0.1).:contentReference[oaicite:14]{index=14}

---

## 🔗 KFM Integration Plan

KFM describes processing imagery in an incremental pipeline (process only new imagery / append new NDVI records) and storing NDVI for field analytics + map layers. :contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}

### Target outputs for promotion
- `data/processed/remote_sensing/ndvi/landsat8/...` (GeoTIFF + metadata)
- `data/catalogs/stac/...` (STAC item + assets)
- `data/catalogs/prov/...` (PROV lineage record)
- DB upsert into `field_health_index` (if field boundaries are available)

> 🚦 **Pipeline order is enforced in KFM:** ETL → STAC/DCAT/PROV → graph → API → UI → story nodes. Don’t bypass stages. :contentReference[oaicite:17]{index=17}

---

## 🧾 Run Log (fill per execution)

| Run timestamp | AOI | Date range | Collection | Composite | Mask | Export target | Notes |
|---|---|---|---|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `LANDSAT/LC08/C02/T1_L2` | `median` | `QA_PIXEL bits 3/4` | `TBD` | `TBD` |

---

## 🧱 Definition of Done (Doc + Experiment)

KFM’s “Definition of Done” for governed docs emphasizes: front-matter validity, evidence-linked claims, repeatable validation, and explicit governance/CARE handling. :contentReference[oaicite:18]{index=18}

- [ ] YAML front-matter complete & valid (no missing required fields)  
- [ ] Procedure is repeatable (exact params recorded, scripts referenced)  
- [ ] Outputs listed + paths standardized (no mystery artifacts)  
- [ ] Validation steps executed + results captured (QC images / stats)  
- [ ] Governance + sensitivity reviewed (care_label updated from `TBD`)  
- [ ] Promotion plan documented (what moves to `data/processed` + metadata)  

---

## 📚 References (project files)

- **KFM Markdown governance & pipeline ordering** :contentReference[oaicite:19]{index=19}  
- **KFM technical architecture & NDVI pipeline/storage** :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}  
- **Google Earth Engine Applications (NDVI, Landsat band mapping, composites)** :contentReference[oaicite:22]{index=22}  
- **Cloud-Based Remote Sensing with Google Earth Engine (masking/scaling patterns)** :contentReference[oaicite:23]{index=23}  
- **Geoprocessing with Python (local NDVI computation pattern)** :contentReference[oaicite:24]{index=24}  
- **Comprehensive Markdown Guide (front-matter + template conventions)** :contentReference[oaicite:25]{index=25}  

---

## Footnotes

[^ndvi_eq]: NDVI definition and Landsat 8 band mapping (band 5 = NIR, band 4 = Red). :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27}  
[^ndvi_range]: NDVI outputs typically range from −1 to 1; high green vegetation ≈ 0.8–0.9, near 0 indicates little vegetation, water trends toward −1. :contentReference[oaicite:28]{index=28}  
[^pipeline_order]: KFM pipeline ordering requirement (ETL → STAC/DCAT/PROV → graph → API → UI → story nodes). :contentReference[oaicite:29]{index=29}  
[^l8_mask_scale]: Example Landsat 8 SR workflow showing QA_PIXEL cloud/shadow masking and SR scaling constants used here as the baseline. :contentReference[oaicite:30]{index=30}  
[^local_ndvi]: Local NDVI computation example using GDAL/NumPy (mask denominator=0; fill NoData). :contentReference[oaicite:31]{index=31}

