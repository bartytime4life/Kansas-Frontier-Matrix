# 🌿 Derived Data — NDVI (Landsat 8)

![Stage](https://img.shields.io/badge/stage-work%2Fderived-blue)
![Sensor](https://img.shields.io/badge/sensor-Landsat%208-2ea44f)
![Index](https://img.shields.io/badge/index-NDVI-brightgreen)
![Format](https://img.shields.io/badge/format-GeoTIFF-orange)
![Status](https://img.shields.io/badge/status-experimental-yellow)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-6f42c1)

> 🧪 **Experiment run:** `2026-01-02__ndvi__landsat8`  
> 📍 **You are here:** `data/work/experiments/2026-01-02__ndvi__landsat8/data/derived/`  
> ⬅️ **Go up:** [`../../README.md`](../../README.md)

✅ **TL;DR**  
This folder contains **generated outputs** (derived artifacts) from the Landsat 8 → NDVI workflow: rasters, masks, summaries, and lightweight manifests/previews. It’s meant for **analysis + iteration**, not long-term publication.

---

## 🎯 Scope & folder rules

### ✅ What belongs here
- **Computed artifacts** produced by the pipeline (NDVI GeoTIFFs, masks, summary tables, previews).
- **Small metadata sidecars** that make outputs reproducible (run manifests, checksums, lightweight logs).

### 🚫 What does *not* belong here
- **Raw source data** (that lives in sibling `../raw/` or project-wide `data/raw/...`).
- **Hand-edited files** (derived artifacts should be regenerated, not tweaked).
- **“Published” datasets** meant for UI/API consumption  
  → Promote to `data/processed/...` and generate STAC/DCAT/PROV boundary artifacts (see below).

> ⚠️ **Treat `derived/` as regenerable.**  
> If you can’t reproduce it deterministically, it’s not “derived” yet — it’s “mystery.” 🕵️‍♂️

---

## 🗂️ Contents

<details>
<summary><strong>📁 Typical layout (recommended)</strong></summary>
```text
📁 derived/
├── 📄 README.md                      # 👈 you are here ✅ (scope, rules, navigation)
├── 🌿📁 ndvi/                        # NDVI rasters/composites + NDVI-specific notes
│   └── 📄 README.md                  # NDVI contract: naming, ranges, nodata, QC
├── ☁️📁 masks/                       # Cloud/shadow/valid-pixel masks + QA support rasters
│   └── 📄 README.md                  # Mask semantics (0/1 or codes) + edge cases
└── 📊📁 stats/                       # Zonal stats + summary tables (CSV/Parquet) + QA tables
    └── 📄 README.md                  # Stats schema, aggregation rules, validation checks
```

</details>

> 🧩 If your run uses a slightly different subfolder layout, that’s fine — **keep the contracts consistent** (formats + metadata + naming + provenance).

---

## 🧾 Data contract (non‑negotiable)

### 🌿 NDVI raster(s)

**NDVI definition**  
`NDVI = (NIR - RED) / (NIR + RED)`

**Landsat 8 band mapping (common convention)**  
- **RED:** Band 4  
- **NIR:** Band 5

**Required properties**
- **Format:** GeoTIFF (`.tif`)
- **Data type:** float32 (recommended)
- **Value range:** typically `[-1, 1]`
- **NoData:** explicitly set (avoid writing NaN/Inf into the GeoTIFF)
- **Geo metadata:** CRS + transform + pixel size must be present

**Recommended filename pattern**
```text
ndvi__L8__{aoi}__{date_or_range}__sr__cloudmask-{method}__v{n}.tif
```

**Examples**
```text
ndvi__L8__kansas__2026-01-02__sr__cloudmask-qa_pixel__v1.tif
ndvi__L8__aoi-012__2025-06-01_2025-06-30__sr__cloudmask-fmask__v3.tif
```

---

### ☁️ Cloud/shadow mask raster(s) (strongly recommended)

**Purpose:** exclude contaminated pixels before NDVI is computed.

**Required properties**
- **Format:** GeoTIFF (`.tif`)
- **Data type:** `uint8` recommended
- **Semantics:** must be documented (what is valid vs masked?)

**Recommended filename pattern**
```text
mask__L8__{aoi}__{date_or_range}__{method}__v{n}.tif
```

**Minimum semantic contract**
- `1` = valid pixel
- `0` = masked pixel (cloud/shadow/snow/water/etc. per your method)

<details>
<summary><strong>🧷 Optional: quality code mapping</strong></summary>

If you export a **quality band** (instead of a binary mask), include a small table here that defines codes.

Example (only if your pipeline uses a similar scheme):
- `10` clear (not smoothed)
- `11` clear (smoothed)
- `20` snow/water (not smoothed)
- `21` snow/water (smoothed)
- `30` climatology-filled (not smoothed)
- `31` climatology-filled (smoothed)

</details>

---

### 📊 Summary table(s) (optional but useful)

**Purpose:** quick stats for AOIs, dashboards, QA, and regression checks.

**Format:** CSV  
**Recommended filename pattern**
```text
ndvi_stats__{aoi}__{date_or_range}__v{n}.csv
```

**Suggested schema (extend as needed)**
| column | type | meaning |
|---|---|---|
| aoi_id | string | AOI identifier used in the experiment |
| date_start | date | start of compositing / observation window |
| date_end | date | end of window |
| ndvi_mean | float | mean NDVI (masked) |
| ndvi_median | float | median NDVI (masked) |
| ndvi_std | float | std dev NDVI (masked) |
| valid_px | int | count of valid pixels used |
| total_px | int | total pixels in AOI raster window |
| pct_valid | float | valid_px / total_px |

---

### 🧾 Manifest & integrity files (recommended)

Keep these **small** and **always commit** them (even if you don’t commit the rasters):

- `manifest/run_manifest.json`  
  Contains:
  - input collection IDs / source references
  - parameters (dates, AOI id, mask method, compositing)
  - commit hash / pipeline version
  - timestamp + runtime environment
- `manifest/checksums.sha256`  
  File hashes to detect drift/corruption.

---

## 🧠 Processing assumptions (fill these in)

> ✅ These fields turn “a file” into “a dataset.” 📦

- **AOI:** `TBD` (link or path to AOI geometry)
- **Date / window:** `TBD` (single day vs composite window)
- **Source imagery collection ID(s):** `TBD`  
- **Product level:** `TBD` (surface reflectance strongly preferred)
- **Reflectance scaling applied:** `TBD` (yes/no + how)
- **Cloud/shadow mask method:** `TBD` (QA bits / FMask / custom)
- **Compositing strategy:** `TBD` (first scene / median / max NDVI / etc.)
- **Reprojection/resampling:** `TBD` (native vs reprojected)

---

## 🔍 Quick QA / validation checklist

Run these before treating outputs as “usable” ✅

```bash
# 1) Inspect metadata + size
gdalinfo rasters/ndvi/*.tif | head -n 80

# 2) Quick stats (if rasterio/rio is installed)
rio info rasters/ndvi/*.tif
rio stats rasters/ndvi/*.tif
```

```bash
# 3) Detect NaN/Inf leakage (should be NONE in saved GeoTIFFs)
python - <<'PY'
import glob, numpy as np
import rasterio as rio

paths = sorted(glob.glob("rasters/ndvi/*.tif"))
if not paths:
    print("No NDVI rasters found under rasters/ndvi/")
    raise SystemExit(0)

for fp in paths:
    with rio.open(fp) as ds:
        a = ds.read(1, masked=True)
    bad = np.isnan(a).any() or np.isinf(a).any()
    print(fp, "❌ BAD (NaN/Inf present)" if bad else "✅ ok")
PY
```

👀 Visual sanity checks (fast, human-friendly):
- Water bodies should trend **low/negative**
- Healthy vegetation should be **high positive**
- Cloud edges should **not** produce streaky NDVI artifacts if masking is correct

---

## 🧹 Storage & git hygiene

- 🧱 GeoTIFFs can get big — prefer:
  - Git LFS, or
  - object storage (and commit only manifests + checksums + previews)
- ✅ Always commit:
  - `run_manifest.json`
  - `checksums.sha256`
  - small PNG previews (optional but helpful)

---

## 🚚 Promotion to `data/processed/` (when this becomes “real”)

When an artifact graduates from experiment output → dataset:

1. **Move outputs** into a canonical domain path  
   Example (adjust to repo convention):  
   `data/processed/remote-sensing/ndvi/landsat8/...`

2. **Generate boundary artifacts** (required for publication)
   - STAC Collection + Item(s) (assets + spatiotemporal metadata)
   - DCAT dataset entry (discoverability + license + keywords)
   - PROV bundle (inputs → processing activity → outputs)

3. **Write/Update a domain README** under `docs/data/...`  
   Include source notes, ETL summary, and maintenance expectations.

---

## 🛡️ Governance, FAIR+CARE & attribution

- ✅ Prefer **explicit assumptions + uncertainty** over false precision.
- ✅ Carry **source attribution** and licensing forward into published metadata.
- ⚠️ If outputs are used in UI/API: they must flow through governed API paths (no hard-coded direct file serving).

---

## 📝 Changelog

- **2026-01-02** — Initial derived output contract + folder README created.
