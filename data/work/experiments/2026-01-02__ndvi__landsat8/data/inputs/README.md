# 📥 Inputs — `2026-01-02__ndvi__landsat8`

![KFM](https://img.shields.io/badge/KFM-living_atlas-blue)
![Experiment](https://img.shields.io/badge/experiment-data%2Fwork%2Fexperiments-informational)
![Index](https://img.shields.io/badge/index-NDVI-success)
![Sensor](https://img.shields.io/badge/sensor-Landsat%208-9cf)
![Reproducibility](https://img.shields.io/badge/pipeline-deterministic-important)

> [!IMPORTANT]
> This folder is the **immutable input snapshot** for this experiment run.  
> If an input changes (AOI, date range, cloud mask rule, scene list, scaling, etc.), **do not edit in place** — make a new experiment folder (new date/id) and re-run.

---

<details>
  <summary>🧭 Quick navigation</summary>

- [🎯 What belongs here](#-what-belongs-here)
- [✅ Minimum required inputs](#-minimum-required-inputs)
- [🗂️ Suggested layout](#️-suggested-layout)
- [🛰️ Landsat 8 NDVI expectations](#️-landsat-8-ndvi-expectations)
- [🧾 Input contract](#-input-contract)
- [🔐 Integrity & provenance](#-integrity--provenance)
- [✅ Validation checklist](#-validation-checklist)
- [📚 Evidence anchors](#-evidence-anchors)

</details>

---

## 🎯 What belongs here

This directory contains **only the upstream artifacts** required to reproduce the NDVI outputs for the experiment:

- 🗺️ **AOI boundary** (geometry used to filter/clip imagery)
- ⚙️ **Run configuration** (time range, cloud thresholds, compositing method, scaling rules)
- 🛰️ **Scene/asset selectors** (scene IDs, STAC item JSONs, or GEE collection + filters)
- 🧼 **Masking helpers** (cloud/QA rule notes, optional masks)
- 🔐 **Checksums + manifest** (so we can prove “same inputs → same outputs”)

KFM’s broader workflow expects **deterministic, config-driven transformations** and **explicit lineage** across raw → work → processed stages. This folder is how we “freeze” inputs for replayable runs. ✅:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## ✅ Minimum required inputs

| Item | File (recommended) | Required | Notes |
|---|---|:--:|---|
| AOI geometry | `aoi.geojson` | ✅ | Polygon/MultiPolygon. Prefer EPSG:4326 for portability. |
| Run parameters | `params.yaml` | ✅ | Date range, cloud rule, NDVI method, output scale, etc. |
| Scene selector | `landsat8/scenes.csv` **or** `landsat8/stac_items/` **or** `landsat8/gee.json` | ✅ | Choose the mode that matches the pipeline you’re running. |
| Manifest | `inputs.manifest.json` | ✅ | Declares every input artifact + role + checksum. |
| Checksums | `checksums.sha256` | ✅ | SHA-256 for all non-generated input files in this folder. |

> [!TIP]
> If you’re unsure what the pipeline expects, start with:
> - `aoi.geojson`
> - `params.yaml`
> - `landsat8/gee.json` (GEE collection + filters)
> - `inputs.manifest.json`
> - `checksums.sha256`

---

## 🗂️ Suggested layout

```text
📁 data/work/experiments/2026-01-02__ndvi__landsat8/
└─ 📁 data/
   └─ 📁 inputs/
      ├─ 📄 README.md                         👈 you are here
      ├─ 🗺️ aoi.geojson                        (required)
      ├─ ⚙️ params.yaml                        (required)
      ├─ 📁 landsat8/
      │  ├─ 📄 gee.json                        (one option)
      │  ├─ 📄 scenes.csv                      (alternate option)
      │  └─ 📁 stac_items/                     (alternate option)
      │     ├─ 🧾 item_01.json
      │     └─ 🧾 item_02.json
      ├─ 🧾 inputs.manifest.json               (required)
      └─ 🔐 checksums.sha256                   (required)
```

---

## 🛰️ Landsat 8 NDVI expectations

### NDVI definition (the “math contract”)
NDVI is computed from **surface reflectance** as:

\[
NDVI = \frac{\rho_{NIR} - \rho_{RED}}{\rho_{NIR} + \rho_{RED}}
\]

For **Landsat 8 OLI**, use:
- **Red**: Band 4
- **NIR**: Band 5:contentReference[oaicite:2]{index=2}

### Quality / cloud masking
Prefer **surface reflectance** products that ship with **quality flags** and/or cloud masks, then filter to “good pixels” (cloud/shadow/snow masked out) before compositing or exporting.:contentReference[oaicite:3]{index=3}

### If using Google Earth Engine (GEE)
A common Landsat 8 Level-2 collection used in GEE is:
- `LANDSAT/LC08/C02/T1_L2`:contentReference[oaicite:4]{index=4}

…and you typically apply scale factors to convert SR bands to reflectance.:contentReference[oaicite:5]{index=5}

---

## 🧾 Input contract

### `params.yaml` (recommended schema)
Use this as a starting point:

```yaml
experiment:
  id: "2026-01-02__ndvi__landsat8"
  title: "NDVI from Landsat 8 (OLI) surface reflectance"
  description: "Compute NDVI over AOI for defined date range; produce reproducible outputs."

aoi:
  file: "aoi.geojson"
  crs: "EPSG:4326"

time:
  start: "YYYY-MM-DD"
  end: "YYYY-MM-DD"

landsat8:
  mode: "gee"              # gee | scenes_csv | stac_items
  collection: "LANDSAT/LC08/C02/T1_L2"   # if mode=gee
  cloud_cover_max: 20       # percent (if applicable)
  apply_scale_factors: true # required for Collection 2 L2 SR in many workflows
  mask:
    enabled: true
    strategy: "qa_pixel"    # qa_pixel | cfmask | custom
    notes: "Describe bits/classes used."

ndvi:
  method: "nir_red_ratio"
  bands:
    red: "B4"               # or SR_B4 depending on pipeline
    nir: "B5"               # or SR_B5 depending on pipeline
  nodata: -9999

export:
  target_crs: "EPSG:XXXX"   # optional: match AOI or target tiling CRS
  pixel_size_m: 30
  format: "COG"             # GeoTIFF/COG recommended for rasters
```

> [!NOTE]
> If you’re processing locally (GeoTIFFs), the NDVI operation is the same math, but make sure you preserve **NoData handling** and do computations in float to avoid integer truncation.:contentReference[oaicite:6]{index=6}

---

## 🔐 Integrity & provenance

### 1) `checksums.sha256`
Store a checksum for every non-generated input file in this folder.

Example:

```bash
# from data/inputs/
sha256sum aoi.geojson params.yaml inputs.manifest.json landsat8/* >> checksums.sha256
```

### 2) `inputs.manifest.json`
This is the human+machine readable declaration of what “the inputs” actually were.

Example:

```json
{
  "experiment_id": "2026-01-02__ndvi__landsat8",
  "generated_at_utc": "2026-01-02T00:00:00Z",
  "inputs": [
    {"path": "aoi.geojson", "role": "aoi", "sha256": "..." },
    {"path": "params.yaml", "role": "config", "sha256": "..." },
    {"path": "landsat8/gee.json", "role": "scene_selector", "sha256": "..." }
  ],
  "upstream": {
    "platform": "landsat-8",
    "notes": "Surface reflectance + QA mask; NDVI derived from red & NIR."
  }
}
```

### 3) “Promotion” rule (work → processed)
This experiment lives under `data/work/…` (intermediate). When promoting any derived product to “published” status, KFM expects catalog + lineage artifacts (STAC/DCAT/PROV) and end-to-end provenance linking **raw → work → processed**.:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

---

## ✅ Validation checklist

Before running the pipeline:

- [ ] `aoi.geojson` loads cleanly (valid geometry, correct CRS)
- [ ] `params.yaml` matches intended experiment settings (time range, mask rule, bands)
- [ ] Scene selector is unambiguous (`mode` matches provided files)
- [ ] Cloud/QA masking strategy is documented (even if it’s “use default QA_PIXEL”)
- [ ] `inputs.manifest.json` exists and lists **every** input artifact
- [ ] `checksums.sha256` exists and includes every file listed in the manifest
- [ ] Inputs are treated as immutable (if something changes → new experiment folder)

> [!WARNING]
> Never store secrets (tokens, service account keys) in this folder. Use environment variables or a secret manager.

---

## 📚 Evidence anchors

<details>
  <summary>Project docs & technical anchors used to write this README</summary>

- KFM contract-first + deterministic pipeline principles:contentReference[oaicite:9]{index=9}
- KFM domain expansion pattern: raw/ → work/ → processed/ + canonical catalogs (STAC/DCAT/PROV):contentReference[oaicite:10]{index=10}
- PROV expectation: link raw inputs → intermediate work → processed outputs:contentReference[oaicite:11]{index=11}
- NDVI method and Landsat 8 band mapping (Red=B4, NIR=B5) + emphasis on SR + quality flags:contentReference[oaicite:12]{index=12}
- GEE Landsat 8 Collection 2 Level 2 example (`LANDSAT/LC08/C02/T1_L2`) + scale-factor application pattern:contentReference[oaicite:13]{index=13}
- Local raster NDVI computation note (math + nodata handling):contentReference[oaicite:14]{index=14}

</details>

