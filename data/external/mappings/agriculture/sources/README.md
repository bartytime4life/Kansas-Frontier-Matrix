# 🌾 Agriculture — External Map Sources Registry

![Domain](https://img.shields.io/badge/domain-agriculture-2e7d32?style=flat&logo=leaflet&logoColor=white)
![Scope](https://img.shields.io/badge/scope-external%20mappings-1565c0?style=flat)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-6a1b9a?style=flat)
![UI](https://img.shields.io/badge/map-MapLibre%20%2B%20(3D%20optional)-263238?style=flat)

> 📍 **Path:** `data/external/mappings/agriculture/sources/`  
> 🧭 Purpose: the **“map behind the map”** 🗺️—every agriculture layer should be traceable to a source entry here.

---

## 🎯 What this folder is

This directory is the **machine-readable registry** for agriculture-related **external** map/data sources that KFM can:

- reference 🔗
- fetch/ingest ⬇️
- attribute 📜
- validate ✅
- publish as processed datasets + catalogs 🗂️

Think of this as the **single source-of-truth for upstream origin metadata** before anything becomes a first-class dataset.

> [!IMPORTANT]
> **No big datasets live here.**  
> Put raw downloads in `data/raw/<domain>/…` (or external object storage) and keep **only metadata + fetch instructions + integrity info** here.

---

## ✅ What belongs here (and what doesn’t)

### ✅ Yes, put this here
- `source.json` / `source.yml` manifests 🧾
- provider URLs, API endpoints, WMS/WFS endpoints 🌐
- required attribution strings for UI 🏷️
- license/terms notes 📜
- checksum manifests (recommended) 🔐
- minimal “how to update” runbooks (`fetch.md`) 📌

### ❌ Don’t put this here
- large GeoTIFFs / MBTiles / shapefile zips / imagery tiles 🧱
- secrets (API keys, tokens) 🔑
- private landowner/parcel PII 🚫

---

## 🔁 How this fits KFM’s data lifecycle

```mermaid
flowchart LR
  A[External provider 🌐] --> B[This folder: source registry 🧾]
  B --> C[data/raw/agriculture/... 🧊]
  C --> D[data/work/agriculture/... 🛠️]
  D --> E[data/processed/agriculture/... ✅]
  E --> F[Boundary artifacts 🗂️\nSTAC + DCAT + PROV]
  F --> G[(Databases: PostGIS / Neo4j)]
  G --> H[API]
  H --> I[UI (MapLibre/Cesium)]
```

> [!NOTE]
> The registry entry here should eventually link to the “published artifacts” (STAC/DCAT/PROV) created after processing.

---

## 📁 Recommended layout

```text
data/external/mappings/agriculture/sources/
├─ README.md                          👈 you are here
├─ _templates/                        🧩 optional: boilerplate + examples
│  ├─ source.template.json
│  └─ source.template.yml
├─ _generated/                        🤖 optional: generated indexes (do not hand-edit)
│  └─ registry.index.json
├─ usda_nass_cdl/                     🌽 example (folder-per-source)
│  ├─ source.json                     🧾 required
│  ├─ fetch.md                        ⬇️ optional
│  ├─ checksums.sha256                🔐 recommended
│  └─ LICENSE_OR_TERMS.md             📜 optional
└─ ...more sources...                 ➕
```

> [!TIP]
> Prefer **folder-per-source** so reviews stay clean and checksums/terms stay scoped.

---

## 🧾 Source manifest contract

Each source folder must include **`source.json`** (or `source.yml`) that is:

- 🧠 **machine-readable**
- 🔍 **searchable/greppable**
- 🧱 **stable** (treat `id` like a database key)

### 🏷️ Naming conventions (recommended)

- **IDs / folders:** `snake_case` (e.g., `usda_nrcs_ssurgo`)
- **Files:** `source.json`, `fetch.md`, `checksums.sha256`
- **Dates:** ISO-8601 (`YYYY-MM-DD`)
- **Units:** always explicit (meters, acres, %, etc.)

---

## ✅ Minimal required fields

Your `source.json` must include at least:

- `id` — stable slug (snake_case)
- `domain` — `"agriculture"`
- `title`
- `description`
- `provider.name`
- `license` — SPDX if possible, otherwise `"proprietary"` + URL/notes
- `access` — how to reach the source (download/API/WMS/GEE/etc.)
- `coverage.spatial` + `coverage.temporal`
- `attribution` — safe to display in UI
- `updated_at`

> [!IMPORTANT]
> **Contract rule:** if a source is intended to ship into the platform, its metadata must be **schema-validatable** (CI-friendly). No “hand-wavy” entries.

---

## 📄 Example `source.json` (with MapLibre-friendly delivery block)

```json
{
  "id": "usda_nass_cdl",
  "domain": "agriculture",
  "kind": "external_mapping_source",
  "title": "USDA NASS Cropland Classification (Example)",
  "description": "Annual crop/landcover classification used for crop patterns and change detection.",
  "provider": {
    "name": "USDA NASS",
    "homepage": "https://example.org/provider-homepage",
    "contact": "mailto:data-contact@example.org"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "url": "https://example.org/license",
    "attribution_required": true
  },
  "attribution": "© USDA NASS (example attribution text)",
  "access": {
    "method": "http",
    "type": "download",
    "urls": [
      "https://example.org/path/to/dataset-or-index"
    ],
    "auth": {
      "required": false,
      "env_vars": []
    }
  },
  "coverage": {
    "spatial": {
      "region": "Kansas (KS), USA",
      "bbox_wgs84": [-102.051, 36.993, -94.589, 40.003]
    },
    "temporal": {
      "start": "2010-01-01",
      "end": "2025-12-31",
      "cadence": "annual"
    }
  },
  "delivery": {
    "map": {
      "supported": true,
      "maplibre_source": {
        "type": "raster",
        "tiles": [
          "https://tiles.example.org/agriculture/cdl/{z}/{x}/{y}.png"
        ],
        "tileSize": 256,
        "minzoom": 0,
        "maxzoom": 16
      }
    },
    "pipeline": {
      "plugin": "agriculture/cdl_ingest",
      "raw_target": "data/raw/agriculture/usda_nass_cdl/",
      "processed_target": "data/processed/agriculture/usda_nass_cdl/"
    },
    "catalog_links": {
      "stac_collection_id": null,
      "stac_item_ids": [],
      "dcat_dataset_id": null,
      "prov_bundle_paths": []
    }
  },
  "integrity": {
    "checksums_sha256": "checksums.sha256",
    "expected_files": null
  },
  "notes": {
    "gotchas": [
      "Keep yearly vintages versioned and time-indexed."
    ],
    "update_instructions": "See fetch.md for steps and expected file naming."
  },
  "updated_at": "2026-01-29"
}
```

---

## ➕ Adding a new source (PR checklist)

- [ ] Create folder: `data/external/mappings/agriculture/sources/<source_id>/`
- [ ] Add `source.json` (or `source.yml`)
- [ ] Add `fetch.md` if updates are non-trivial
- [ ] Add `checksums.sha256` (recommended)
- [ ] Confirm license + attribution are correct and display-safe
- [ ] If auth is required:
  - [ ] document required env vars **only** (no secrets in Git)
  - [ ] provide a redacted example (`API_KEY=...`)
- [ ] If the source will be ingested:
  - [ ] ensure a pipeline plugin exists (or is planned) under `src/pipelines/`
  - [ ] confirm raw/work/processed targets

---

## 🌱 Starter “source ideas” (turn into real folders over time)

> [!TIP]
> Keep this as a wishlist until each one has a real `source.json`.

| Idea 🧠 | Helps with 🌾 | Likely type | Typical cadence |
|---|---|---:|---|
| Crop/landcover classification | crop patterns, change detection | Raster | Annual |
| Soil survey / soil properties | suitability, erosion risk | Vector/Raster | Slow/irregular |
| Aerial imagery | field boundaries, irrigation pivots | Raster | Multi-year |
| Multispectral satellite imagery | vegetation indices, crop health proxies | Raster | Days–weeks |
| Yield/production statistics | economic & historical overlays | Tabular | Seasonal/annual |
| Drought/climate indicators | stress modeling, context layers | Raster/Tabular | Monthly |

---

## ✅ QA & sanity checks (before wiring to pipelines/UI)

- 🔎 **Spatial sanity:** bbox + CRS + resolution documented
- 🕒 **Temporal sanity:** start/end/cadence explicit
- 🧾 **Attribution:** present + short enough for UI
- 🔐 **Integrity:** checksums (or at least file counts/sizes) recorded
- 🧪 **Reproducibility:** a new contributor can re-fetch with `fetch.md`

---

## 🔐 Secrets, privacy, and “don’t commit this” rules

Never commit:
- API keys/tokens 🔑
- private landowner/parcel PII 🚫
- restricted datasets you can’t redistribute 📵

If a source is restricted, declare it **explicitly**:

```json
{
  "classification": {
    "visibility": "restricted",
    "reason": "license/PII",
    "handling": "store externally; publish only aggregated outputs"
  },
  "access": {
    "auth": { "required": true, "env_vars": ["PROVIDER_TOKEN"] }
  }
}
```

---

## 🔗 Related folders (where things go next)

- `src/pipelines/…` 🧰 — ingestion + processing code
- `data/raw/agriculture/…` 🧊 — untouched downloads (or pointers to object storage)
- `data/work/agriculture/…` 🛠️ — scratch outputs (safe to overwrite)
- `data/processed/agriculture/…` ✅ — authoritative processed datasets
- `data/stac/collections/` + `data/stac/items/` 🗂️ — STAC catalogs
- `data/catalog/dcat/` 🧾 — DCAT discovery views
- `data/prov/` 🧬 — provenance bundles (lineage)

---

## 🙋 FAQ

<details>
  <summary><strong>Why are “sources” separate from STAC/DCAT?</strong></summary>

- **Sources (this folder)** describe *upstream providers* and access patterns.
- **STAC/DCAT** describe *published outputs* KFM actually serves.
- One upstream source can produce many processed datasets over time, so we keep the upstream registry clean and reusable.

</details>

<details>
  <summary><strong>Can I put data files in here?</strong></summary>

Only if they’re **tiny** (e.g., a small lookup table under ~100KB) and clearly justified. Otherwise, use `data/raw/...` or external object storage and keep references + checksums here.

</details>

