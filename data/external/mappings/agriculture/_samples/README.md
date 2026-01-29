# 🌾 Agriculture Mapping Samples

![KFM](https://img.shields.io/badge/KFM-v13-2b6cb0)
![Mapping](https://img.shields.io/badge/type-mapping__samples-6b46c1)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-1f9d55)
![Scope](https://img.shields.io/badge/scope-external%2Fagriculture-0ea5e9)

> **What this is:** A small, copy/paste-ready library of **mapping examples** 🧩 for bringing **agriculture-related external datasets** into the KFM pipeline—cleanly, reproducibly, and with required metadata + provenance.

---

## ✅ What belongs in `_samples/`

Use this folder to store **example mapping packs** that demonstrate how an agriculture dataset *should* be:

- 🗺️ described (dataset + assets)
- 🧾 cataloged (STAC/DCAT)
- 🧬 traced (PROV lineage)
- 🎛️ exposed (UI layer intent: MapLibre tiles vs GeoJSON overlays)

Think of each sample as a **starter kit** for a new dataset ingestion.

---

## 🧭 Where this fits in KFM

KFM treats “mappings” as **documentation/config artifacts** that connect datasets → catalogs → downstream layers. In the repository layout, each domain can include a `mappings/` folder for **Dataset → STAC/DCAT/PROV mapping docs**. :contentReference[oaicite:0]{index=0}

This folder is specifically:

📁 `data/` → 📁 `external/` → 📁 `mappings/` → 📁 `agriculture/` → 📁 `_samples/`

---

## 📁 Suggested sample-pack layout

Each sample pack should be **self-contained** and readable in isolation:

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 🌾 agriculture/
         └─ 📁 _samples/                               🧪 worked examples (templates + fixtures)
            ├─ 📄 README.md                             📘 how to use samples + how to add new ones
            └─ 📁 <sample_id>/                          🏷️ one sample bundle (self-contained)
               ├─ 🧩 mapping.yml                         ✅ sample mapping pack (fields/params/outputs)
               ├─ 🛰️ stac.collection.sample.json         🧩 sample STAC Collection (reference structure)
               ├─ 🛰️ stac.item.sample.json               📦 sample STAC Item (reference structure)
               ├─ 🗂️ dcat.dataset.sample.jsonld          🧾 sample DCAT Dataset (JSON-LD discovery record)
               ├─ 🧬 prov.bundle.sample.jsonld           🧾 sample PROV bundle (lineage + receipts)
               ├─ 📄 notes.md                            📝 sample-specific guidance + assumptions
               └─ 📁 fixtures/                           ◻️ optional: tiny example files/schemas/screenshots
```

**Rule of thumb:** samples should stay **small**, and focus on demonstrating *structure + correctness*, not “shipping the full dataset.”

---

## 🌾 Sample themes we want covered (starter ideas)

Agriculture mapping in KFM often touches:

- 🧱 **Soils** (e.g., soil polygons / classifications)
- 🌽 **Crop type & land cover** (raster classifications)
- 📈 **Yield & production stats** (tabular + spatial joins)
- 💧 **Irrigation / water use indicators**
- 🌿 **Crop health signals** (NDVI and related vegetation indices)

Example agriculture records that matter historically and analytically include soil maps, crop yield statistics, and land ownership/land-use records. 

Remote sensing adds common derived products such as crop classification, yield prediction, crop stress detection, and irrigation identification. 

---

## 🧩 Minimal `mapping.yml` template

This is a **human-first** template meant to be easy to review. Keep it deterministic and machine-friendly.

```yaml
# mapping.yml (sample)
dataset:
  id: external.agriculture.<dataset_slug>
  title: "<Human-readable dataset title>"
  description: "<What is it? what does it measure? why is it useful?>"
  license: "<SPDX or plain-text license name>"
  publisher: "<agency/org>"
  keywords: ["agriculture", "soils", "crop", "kansas"]
  version: "0.1.0"

source:
  method: "api|download|gee"
  homepage: "<source landing page>"
  access:
    type: "http|s3|wms|wfs|gee|other"
    url: "<endpoint or download URL>"
  citation: "<preferred citation string>"

coverage:
  spatial:
    aoi: "<reference to AOI geometry or KC bounding box>"
    crs: "EPSG:4326"
  temporal:
    start: "YYYY-MM-DD"
    end: "YYYY-MM-DD"

outputs:
  processed_assets:
    - id: "<asset_id>"
      type: "vector|raster|table"
      format: "gpkg|geojson|cog|parquet|csv"
      path_hint: "data/processed/agriculture/<...>"   # hint only; real outputs belong in canonical locations

catalog:
  stac:
    collection_id: "external-agriculture-<dataset_slug>"
    item_id_pattern: "<dataset_slug>__{year}__{aoi}"
  dcat:
    dataset_uri: "urn:kfm:dataset:external.agriculture.<dataset_slug>"
  prov:
    activity_id: "urn:kfm:activity:ingest.external.agriculture.<dataset_slug>"

ui:
  delivery: "tiles|geojson"
  layer_name: "<Map UI label>"
  style_hint:
    # keep this simple; the real MapLibre style lives in web/ or a governed style registry
    type: "fill|line|circle|raster"
    notes: "<symbology notes>"

governance:
  classification: "public|restricted|sensitive"
  pii: false
  sovereignty_review_required: false
```

---

## 🧪 How to use a sample mapping pack

1) **Copy** the sample folder to a new dataset mapping location (same level as `_samples/`).

2) Update:
- dataset identifiers ✅
- license & citation ✅
- spatial/temporal coverage ✅
- asset definitions ✅
- UI intent ✅

3) Ensure your pipeline produces:
- processed outputs (canonical staging)
- STAC Collection + Items
- DCAT dataset entry
- PROV lineage bundle

> KFM requires published datasets to produce STAC/DCAT/PROV boundary artifacts before downstream stages consume them. :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

---

## 🧱 Sample pack checklist

### Metadata completeness ✅
- [ ] STAC Item(s) reference actual assets and include spatial/temporal metadata  
- [ ] DCAT entry includes **title, description, license, keywords, distribution links**  
- [ ] PROV bundle links **raw → work → processed** and records activity + agents  

(These are enforced as cross-layer expectations.) :contentReference[oaicite:5]{index=5}

### Pipeline correctness 🔁
- [ ] Deterministic + idempotent (re-run yields same outputs)
- [ ] No interactive/manual steps in official pipelines
- [ ] Inputs read from raw; outputs written to processed; catalogs updated

:contentReference[oaicite:6]{index=6}

### Repo hygiene 🧼
- [ ] Samples stay small; don’t commit multi-GB raw datasets here
- [ ] Prefer stable APIs/services for huge sources where appropriate (e.g., Earth Engine style workflows)

KFM design explicitly favors leveraging external services to avoid bloating the repo while staying up-to-date. :contentReference[oaicite:7]{index=7}

### Safety + governance 🛡️
- [ ] No secrets, API keys, or credentials
- [ ] No PII or sensitive location leakage
- [ ] Classification is not downgraded accidentally

CI-level scans and governance checks are expected to catch violations. :contentReference[oaicite:8]{index=8}

---

## 🧠 Notes for agriculture-derived layers (remote sensing)

If your sample demonstrates a derived raster product (NDVI trend, crop type classification, irrigation proxy, etc.), treat it like a **first-class evidence artifact**:

- store outputs in processed
- catalog in STAC/DCAT
- trace in PROV with algorithm + parameters

:contentReference[oaicite:9]{index=9}

A common pattern for crop mapping is time-series classification (e.g., Landsat) and using labeled data (e.g., Cropland Data Layer) for training/validation. 

---

## 📚 References used to design this README (project files)

> These are the project sources that informed structure, governance, and agriculture scope.

- **KFM Master Guide v13 (Markdown Guide)** — contract-first, pipeline ordering, STAC/DCAT/PROV requirements  
  <!-- :contentReference[oaicite:11]{index=11} -->

- **KFM Comprehensive Technical Blueprint (PDF)** — deterministic pipelines, external services strategy, UI mapping delivery notes  
  <!-- :contentReference[oaicite:12]{index=12} -->

- **Geospatial Mapping Hub Design (KFM)** — agriculture as soil/crop/yield/land-use evidence domain  
  <!-- :contentReference[oaicite:13]{index=13} -->

- **Cloud-Based Remote Sensing with Google Earth Engine** — agriculture remote sensing use-cases and workflows  
  <!-- :contentReference[oaicite:14]{index=14} -->

