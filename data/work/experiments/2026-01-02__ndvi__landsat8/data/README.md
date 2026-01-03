---
title: "Experiment Data — NDVI (Landsat 8)"
path: "data/work/experiments/2026-01-02__ndvi__landsat8/data/README.md"
experiment_id: "2026-01-02__ndvi__landsat8"
created: "2026-01-02"
last_updated: "2026-01-03"
doc_kind: "Data README"
stage: "work"
status: "active"
owner: "TBD"
contact: "TBD"
sensitivity: "public (verify if AOI/outputs are derived from restricted inputs)"
care_label: "Public"
license: "TBD (inherit from source + KFM policy)"
---

# 🌿 NDVI (Landsat 8) — Experiment Data

![stage](https://img.shields.io/badge/stage-data%2Fwork-informational)
![experiment](https://img.shields.io/badge/experiment-2026--01--02__ndvi__landsat8-blue)
![sensor](https://img.shields.io/badge/sensor-Landsat%208-9cf)
![index](https://img.shields.io/badge/index-NDVI-brightgreen)
![format](https://img.shields.io/badge/target%20format-COG%20GeoTIFF-lightgrey)

This folder contains the **data artifacts** (inputs, intermediates, exports, and derived rasters/tables) for the experiment:

- 🧪 **Experiment:** `2026-01-02__ndvi__landsat8`
- 🛰️ **Source:** Landsat 8 imagery (recommended: Surface Reflectance / Level-2 when available)
- 🌱 **Product:** NDVI (Normalized Difference Vegetation Index)

> [!IMPORTANT]
> This is under `data/work/...` → treat it as **rebuildable working output**.
> - ✅ OK to iterate and regenerate  
> - 🚫 Don’t treat as “published evidence” yet  
> - 📦 When stable: promote outputs to `data/processed/...` and generate **catalog + provenance** artifacts (STAC/DCAT/PROV) before wiring into graph/API/UI.

---

## 🧭 Quick navigation

- [🧾 At a glance](#-at-a-glance)
- [🗂️ Directory layout](#️-directory-layout)
- [📦 What belongs here](#-what-belongs-here)
- [📐 NDVI data contract](#-ndvi-data-contract)
- [🧼 Quality & masking](#-quality--masking)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧬 Provenance & reproducibility](#-provenance--reproducibility)
- [🔐 Governance & sensitivity](#-governance--sensitivity)
- [✅ Validation checklist](#-validation-checklist)
- [📚 Project references](#-project-references)

---

## 🧾 At a glance

| Field | Value |
|---|---|
| 📍 Location in repo | `data/work/experiments/2026-01-02__ndvi__landsat8/data/` |
| 🧪 Stage | `work` (intermediate / regenerable) |
| 🛰️ Sensor | Landsat 8 |
| 🌱 Index | NDVI |
| 🧱 Primary outputs | NDVI rasters (GeoTIFF/COG) + summary stats tables |
| 🗺️ AOI | **TBD** (see `aoi/` if present) |
| 🗓️ Time range | **TBD** (record in `metadata/run.json`) |
| 🧩 Resolution | ~30 m (unless resampled — must be documented) |
| 🌍 CRS | **Must be recorded** (keep consistent per output series) |

---

## 🗂️ Directory layout

> [!NOTE]
> This is the **recommended/target** structure for this experiment’s data subtree.  
> If your run differs, update this section so future maintainers don’t have to guess. 🙏

```text
📁 data/
├── 📁 aoi/                         # Area of interest boundaries (GeoJSON/GeoPackage)
│   ├── 📄 aoi.geojson              # (example)
│   └── 📄 aoi.readme.md            # AOI notes: source, edits, assumptions
├── 📁 inputs/                      # Any non-satellite inputs used (optional)
│   └── 📄 ...                      # e.g., field boundaries (if permitted)
├── 📁 exports/                     # Raw exports pulled from GEE or upstream tooling
│   ├── 📁 landsat8_sr/             # reflectance stacks / mosaics / QA bands
│   └── 📄 export_manifest.json     # export list + checksums
├── 📁 derived/                     # Derived products from exports
│   ├── 📁 ndvi/                    # NDVI rasters (final for this experiment)
│   ├── 📁 masks/                   # cloud/snow/water masks used (optional)
│   └── 📁 stats/                   # per-AOI summary tables (CSV/Parquet)
├── 📁 quicklooks/                  # Small PNGs for eyeballing outputs
│   └── 📄 ndvi__*.png
└── 📁 metadata/                    # Run configuration + provenance stubs
    ├── 📄 run.json                 # inputs, parameters, date range, AOI, versions
    ├── 📄 env.txt                  # environment snapshot (conda/pip, docker tag, etc.)
    ├── 📄 checksums.sha256         # file integrity checks (recommended)
    └── 📄 notes.md                 # any anomalies, TODOs, known issues
```

---

## 📦 What belongs here

### ✅ Allowed
- 🗺️ AOI geometries + notes
- 🛰️ Exported imagery stacks (SR + QA) that are *necessary* to reproduce derived NDVI
- 🌿 NDVI rasters (single-date, composited, or time-sliced)
- 📊 Derived tables (zonal stats, time-series summaries)
- 🧾 Manifests + checksums + run configuration

### 🚫 Not allowed (move elsewhere)
- “Published” final datasets meant for downstream stages → **promote to `data/processed/...`**
- Sensitive/raw private user uploads (unless explicitly approved and tagged/secured)
- One-off scratch artifacts with no provenance (put those in a personal sandbox or add metadata)

---

## 📐 NDVI data contract

### 1) NDVI definition (must be consistent within a series)
NDVI is defined as:

\[
NDVI = \frac{(NIR - RED)}{(NIR + RED)}
\]

For Landsat 8, NDVI is computed from:
- **RED:** Band 4  
- **NIR:** Band 5  

> [!TIP]
> In Google Earth Engine, this is typically computed via `normalizedDifference(['NIR','RED'])` after renaming bands, or directly from B5/B4 if you keep original band names.

### 2) Raster requirements (recommended)
| Requirement | Target |
|---|---|
| File format | GeoTIFF, preferably **Cloud Optimized GeoTIFF (COG)** 📦 |
| Data type | `float32` (preferred) |
| NODATA | Use a consistent NODATA (e.g., `-9999`) and document it |
| Value range | Generally `[-1, 1]` (flag out-of-range values) |
| Compression | Lossless (`DEFLATE` or `LZW`) |
| Overviews | Internal overviews for fast map rendering |

### 3) Sidecar metadata (strongly recommended)
For every major output asset (especially rasters), keep a sidecar JSON:

```text
derived/ndvi/<name>.tif
derived/ndvi/<name>.json
```

Suggested fields for `<name>.json`:
- `experiment_id`
- `source_collection` (e.g., Earth Engine collection ID)
- `aoi_id` + `aoi_hash`
- `date_start`, `date_end`
- `compositing_method` (median / mosaic / best-pixel / etc.)
- `masking_method` (QA_PIXEL bits, thresholds)
- `band_map` (RED, NIR)
- `crs`, `pixel_size`
- `software` (gee / python stack) + `version`
- `git_commit` (if applicable)

---

## 🧼 Quality & masking

> [!WARNING]
> NDVI without consistent masking (cloud/shadow/snow/water) will create misleading artifacts.  
> If you change masking rules, **bump the dataset version** and record it in `metadata/run.json`.

### Recommended approach
- Use the **Landsat QA band** (e.g., `QA_PIXEL`) to mask:
  - ☁️ clouds
  - 🌑 cloud shadows
  - ❄️ snow/ice
- Keep the mask output (optional) in `derived/masks/` for auditability.

<details>
<summary>🔎 Minimal “masking notes” template</summary>

Add to <code>metadata/run.json</code> or <code>metadata/notes.md</code>:

- Mask source: QA band = `QA_PIXEL`
- Masked classes: clouds, cloud shadow, snow
- Extra filters: (max cloud %), (erosion/dilation), (water handling)
- Known limitations: (thin cirrus), (scan line artifacts), (seasonal snow confusion)

</details>

---

## 🏷️ Naming conventions

### Experiment folder name
`YYYY-MM-DD__<signal>__<source>`

For this experiment:
- `2026-01-02__ndvi__landsat8`

### Output file naming (recommended)
Use **contract-style, parseable** names so automation can index them later:

```text
ndvi__landsat8__aoi-<slug>__start-YYYYMMDD__end-YYYYMMDD__comp-<method>__mask-<method>__v<semver>.tif
```

Examples:
- `ndvi__landsat8__aoi-kansas__start-20250501__end-20250531__comp-median__mask-qapixel__v0.1.0.tif`
- `ndvi__landsat8__aoi-douglas_co__start-20240701__end-20240715__comp-mosaic__mask-qapixel__v0.2.0.tif`

> [!NOTE]
> If you don’t know the AOI slug yet, use `aoi-unknown` temporarily, but fix it before promotion to `data/processed/...`.

---

## 🧬 Provenance & reproducibility

This experiment is expected to follow a **deterministic, logged pipeline**:
- Same inputs + same config ⇒ same outputs (byte-identical if feasible)
- Raw sources should never be overwritten
- Every transformation should be reproducible from captured configuration

### Minimum required provenance in `metadata/`
- `run.json` — *the* source of truth for:
  - AOI
  - date range
  - collection IDs
  - compositing method
  - mask rules
  - export scale / CRS
- `checksums.sha256` — integrity for key assets (rasters + tables)
- `env.txt` — tooling snapshot (docker tag / conda env / pip freeze)

### Promotion path (when this is no longer “just an experiment”)
When outputs are stable and intended for downstream usage:
1. 📦 Move/republish final assets to `data/processed/<domain>/...`
2. 🗺️ Create catalog artifacts (STAC/DCAT)
3. 🧾 Write PROV lineage (inputs → activities → outputs)
4. 🔌 Only then integrate with graph/API/UI

---

## 🔐 Governance & sensitivity

Even if Landsat imagery is public, **derived layers can become sensitive** depending on how they’re joined/used (e.g., private field boundaries, user-uploaded agronomic data, sensitive locations).

**Rules of thumb:**
- 🧷 If any private AOI boundaries or user data were used → treat outputs as **restricted**.
- 🧬 Never publish an output at a lower restriction level than its inputs.
- 🧽 If redaction/generalization is applied (blur coordinates, aggregate stats), document it explicitly in metadata.

> [!IMPORTANT]
> If this experiment ever mixes public NDVI with private “field-scale” data, ensure outputs are permissioned and tagged appropriately (and do not land in public folders by accident).

---

## ✅ Validation checklist

Use this checklist before calling the data “done” ✅

### File integrity
- [ ] `metadata/run.json` exists and is filled (no “TBD” for core parameters)
- [ ] Checksums exist for key outputs (`metadata/checksums.sha256`)
- [ ] No raw source is overwritten (new runs → new versioned outputs)

### Geospatial sanity
- [ ] Output CRS recorded and consistent within a series
- [ ] Pixel size recorded
- [ ] NDVI values within expected range (flag outliers)
- [ ] NODATA set and documented

### Reproducibility
- [ ] Export method documented (GEE export vs local compute)
- [ ] Masking method documented
- [ ] Environment snapshot saved (`env.txt`)

### Publication readiness (only if promoting)
- [ ] Outputs moved/copied to `data/processed/...`
- [ ] STAC/DCAT/PROV generated and validated
- [ ] Governance review completed if sensitivity changed

---

## 📚 Project references

These “project files” informed the structure and method used here (keep local copies accessible):

- 📘 **KFM Master / Markdown guide**: `MARKDOWN_GUIDE_v13.md.gdoc`
- 🧪 **Experiment protocol guidance**: `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`
- 🛰️ **Earth Engine NDVI + Landsat**:
  - `Google Earth Engine Applications.pdf`
  - `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- 🧱 **KFM architecture + NDVI usage**: `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`

---

## 🗓️ Changelog

- **2026-01-03** — Created this README (baseline contract + structure). ✍️

