---
title: "NDVI (Derived) — Landsat 8 — 2026-01-02"
kfm:
  experiment_id: "2026-01-02__ndvi__landsat8"
  stage: "data/work (intermediate)"
  artifact: "ndvi_raster"
  sensor: "Landsat 8"
  status: "experimental"
  created: "2026-01-02"
---

# 🌿 NDVI (Derived) — Landsat 8

![stage](https://img.shields.io/badge/stage-data%2Fwork-blue)
![artifact](https://img.shields.io/badge/artifact-NDVI-brightgreen)
![sensor](https://img.shields.io/badge/sensor-Landsat%208-orange)
![format](https://img.shields.io/badge/format-GeoTIFF-lightgrey)
![status](https://img.shields.io/badge/status-experimental-yellow)

> [!IMPORTANT]
> This folder is **intermediate / experimental output** under `data/work/...` 🧪  
> Treat contents as **mutable** until promoted to `data/processed/...` with full **STAC/DCAT/PROV** metadata and lineage.

---

## 🧭 Context

- **Experiment ID:** `2026-01-02__ndvi__landsat8`
- **Path:** `data/work/experiments/2026-01-02__ndvi__landsat8/data/derived/ndvi/`
- **What this is:** derived NDVI rasters (and sidecars) computed from **Landsat 8** imagery.
- **What this is not:** a published/immutable dataset (no catalog guarantees yet).

---

## 🗂️ Folder contents

> [!NOTE]
> File names and subfolders may evolve as the experiment matures. The goal is to keep this directory **discoverable and reproducible** 🔁.

```text
📁 data/work/experiments/2026-01-02__ndvi__landsat8/
└─ 📁 data/
   └─ 📁 derived/
      └─ 📁 ndvi/
         ├─ 📄 README.md                👈 you are here
         ├─ 🗺️ *.tif                    NDVI rasters (GeoTIFF / COG recommended)
         ├─ 🧾 *.json                   Sidecar metadata (params, sources, run info) (optional)
         ├─ 📁 quicklook/               PNG/JPG previews for fast review (optional)
         ├─ 📁 stats/                   Histograms, zonal summaries, CSVs (optional)
         └─ 📁 logs/                    Pipeline logs / run reports (optional)
```

---

## 🌱 NDVI definition (what’s in the pixels)

**NDVI = (NIR − RED) / (NIR + RED)**

For **Landsat 8**, the common band mapping is:

- **RED** → Band 4 (`B4` or `SR_B4`)
- **NIR** → Band 5 (`B5` or `SR_B5`)

### Expected value conventions ✅
- **Typical range:** `[-1, 1]` (float)
- **Vegetation:** usually higher NDVI (closer to 1)
- **Bare soil / built-up:** mid/low
- **Water / clouds:** often low or masked (depends on masking rules)
- **NoData:** document explicitly in the sidecar JSON (recommended)

> [!TIP]
> If you’re unsure whether a raster is scaled/typed correctly, run a quick **min/max + histogram** check (see “Handy commands” below).

---

## 🏗️ Processing summary (how these files are produced)

This experiment generally follows a deterministic ETL mindset 🔧:

1. **Acquire imagery** (Landsat 8 scenes intersecting the ROI and time window)
2. **Mask clouds/shadows** (QA band / mask strategy)
3. **Scale reflectance** (if required by the source product)
4. **Compute NDVI** from RED + NIR
5. **Export rasters** (GeoTIFF; prefer Cloud-Optimized GeoTIFF if serving/tiling)
6. *(Optional)* **Build overviews/tiles**, and compute summary stats

<details>
<summary>🧾 Suggested sidecar metadata (strongly recommended)</summary>

Keep a JSON per output raster (or one `run_manifest.json`) that captures at least:

| Field | Example | Why it matters |
|---|---|---|
| `experiment_id` | `2026-01-02__ndvi__landsat8` | Traceability |
| `run_id` | `2026-01-02T19-04-22Z__abc1234` | Uniquely identifies a run |
| `git_commit` | `abc1234` | Reproducibility |
| `roi` | `kansas_statewide` (or a GeoJSON ref) | Spatial scope |
| `date_start` / `date_end` | `2025-06-01` / `2025-06-30` | Temporal scope |
| `landsat_collection` | `LANDSAT/LC08/C02/T1_L2` | Source definition |
| `cloud_mask` | `QA_PIXEL` | QA rules |
| `ndvi_formula` | `(nir - red)/(nir + red)` | Transparency |
| `bands` | `red=SR_B4, nir=SR_B5` | Removes ambiguity |
| `nodata` | `-9999` or `NaN` | Correct interpretation |
| `crs` / `transform` | from GeoTIFF metadata | Downstream correctness |

</details>

---

## ✅ Validation checklist (before you trust or publish)

- [ ] **Raster opens** in QGIS/ArcGIS without errors 🗺️
- [ ] **CRS and pixel size** match expectation (Landsat-native is commonly 30 m)
- [ ] **NDVI value range** looks sane (no giant spikes unless NoData/scale issue)
- [ ] **Cloud masking** behaves as intended (spot-check cloudy scenes)
- [ ] **NoData handling** is consistent across outputs
- [ ] **Stats generated** (min/max/mean/std + histogram) for quick regression testing
- [ ] **Visual sanity check**: a few random tiles/areas across ROI

> [!CAUTION]
> A classic failure mode is computing NDVI before proper scaling/masking, yielding “valid-looking” images that are numerically wrong. Always record the source product + scaling rules.

---

## 🧬 Provenance & promotion path (when this becomes “real”)

This folder is in **`data/work/`**, meaning it’s **not** the final contract boundary.

When you’re ready to promote:

- [ ] Move final outputs to: `data/processed/<domain>/ndvi/...` (or the project’s canonical processed home)
- [ ] Create/Update **STAC**:
  - `data/stac/collections/...`
  - `data/stac/items/...`
- [ ] Create/Update **DCAT** entry:
  - `data/catalog/dcat/...`
- [ ] Create/Update **PROV** lineage bundle:
  - `data/prov/...`
- [ ] Ensure links cross-reference correctly (STAC ↔ DCAT ↔ PROV) 🔗

> [!NOTE]
> If this NDVI becomes a UI-facing layer, it should be treated as a first-class “evidence artifact” with explicit provenance before graph/UI integration.

---

## 🛠️ Handy commands (inspect + sanity-check)

### Inspect metadata
```bash
gdalinfo path/to/your_ndvi.tif
```

### Quick min/max + histogram-ish stats (GDAL)
```bash
gdalinfo -stats path/to/your_ndvi.tif
```

### Make a quick PNG preview (stretch)
```bash
# Adjust -scale as needed depending on your NDVI distribution
gdal_translate -of PNG -scale -1 1 0 255 path/to/your_ndvi.tif quicklook/ndvi_preview.png
```

### Convert to Cloud-Optimized GeoTIFF (COG) (recommended)
```bash
# Requires GDAL with COG driver support
gdal_translate path/to/your_ndvi.tif path/to/your_ndvi.cog.tif \
  -of COG -co COMPRESS=DEFLATE -co RESAMPLING=NEAREST
```

---

## 🧩 Naming convention (recommended)

<details>
<summary>📛 Suggested file naming scheme</summary>

A naming pattern that stays sortable and grep-friendly:

```text
ndvi__landsat8__<roi>__<date_or_range>__<run_id>__v<semver>.tif
```

Examples:
- `ndvi__landsat8__kansas__2025-06-01_to_2025-06-30__2026-01-02T1904Z__v0.1.0.tif`
- `ndvi__landsat8__field_0123__2025-07-14__2026-01-02T1904Z__v0.1.0.tif`

</details>

---

## ⚠️ Known limitations (NDVI gotchas)

- NDVI can **saturate** in very dense vegetation (high biomass).
- Residual clouds/haze can bias NDVI if masking is imperfect ☁️
- Mixed pixels (edge of water/urban/veg) can produce misleading values.
- Comparisons across sensors/collections require careful normalization.

---

## 📚 References / related docs (in-repo)

- 📘 `docs/MASTER_GUIDE_v13.md` (pipeline + data lifecycle + catalog boundaries)
- 📐 `docs/standards/` (STAC/DCAT/PROV profiles and validation expectations)
- 🧪 Experiment report (recommended): `mcp/experiments/2026-01-02__ndvi__landsat8/` (or equivalent)

