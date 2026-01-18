# 🗂️ Data UI Components (KFM)  
`web/components/data/` 📍

<p align="center">
  <strong>Contract-first ✅ • Provenance-first 🧾 • Config-driven ⚙️</strong><br/>
  Data catalog + dataset details + provenance UI for the KFM web app.
</p>

<p align="center">
  <img alt="React" src="https://img.shields.io/badge/React-TypeScript-61DAFB?logo=react&logoColor=ffffff" />
  <img alt="Contract First" src="https://img.shields.io/badge/contract--first-enforced-2ea44f" />
  <img alt="Provenance First" src="https://img.shields.io/badge/provenance--first-no%20mystery%20layers-6f42c1" />
  <img alt="STAC/DCAT/PROV" src="https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT%20%7C%20PROV-0b7285" />
</p>

---

## 🎯 Purpose

This folder contains **data-facing UI components** that help users **discover, understand, and trust** KFM datasets:

- 🗺️ Browse & filter datasets in the **Catalog / Layer List**
- 🧩 Toggle layers (and their settings) in a transparent way
- 🧾 Display dataset **metadata**, **license**, and **source attribution**
- 🧬 Show **provenance/lineage** so users can audit “how we got here”
- 📦 Provide **download / export** affordances (where supported by the API)

> [!IMPORTANT]
> **If a dataset can’t be explained, it shouldn’t be displayed.**  
> These components exist to keep KFM “no black boxes” in the UI ✨

---

## 🧭 Non‑negotiables (KFM data trust rules)

- ✅ **Contract-first**: components should expect **typed, validated** dataset metadata (a “data contract”), not ad-hoc objects.
- 🧾 **Provenance-first**: always surface *where a dataset came from*, what license applies, and how it was processed.
- 🚫 **No “mystery layers”**: don’t introduce UI-only pseudo-datasets. If it’s not in the catalog / API, it doesn’t belong.
- ⚙️ **Config-driven UI**: avoid hard-coding Kansas-specific assumptions; read from contracts + config defaults.
- ♿ **Accessible by default**: catalog entries, controls, and panels must be keyboard/screen-reader friendly.

---

## 🧱 Where this fits in the repo

```text
web/
├─ 🧩 components/
│  ├─ 🗂️ data/                 # 👈 you are here 📌 Data-catalog UI components (cards, metadata panels, filters)
│  ├─ 🗺️ map/                  # Map UI widgets (layer list, legends, popups, basemap controls)
│  └─ 🎛️ ui/                   # Shared UI primitives (buttons, dialogs, tooltips, tabs, form controls)
├─ 🧭 views/                    # Page-level screens (MapPage, DataCatalogPage, StoryPage…) + orchestration glue
├─ 🛰️ viewers/                  # MapLibre/Cesium integrations + render pipelines (layers, picking, camera, tiles)
├─ 📚 story_nodes/              # Story content + step configs consumed by the Story UI (markdown + map actions)
└─ 🎨 styles/                   # Global CSS/tokens/themes + accessibility helpers (import order matters)

data/
├─ 📜 sources/                  # External dataset manifests + intake descriptors (what to fetch, from where, licensing)
├─ 📥 raw/                      # Downloaded source artifacts (as-received; immutable; checksums + provenance expected)
├─ 🗄️ processed/                # Cleaned/normalized outputs (GeoJSON/GeoParquet/COG/Parquet; analysis-ready)
└─ 🗂️ catalog/                  # Published metadata + lineage (STAC/DCAT records, provenance, derived product registry)
```

---

## 🔌 Inputs: what these components render

### 1) Dataset “Data Contract” 🧾  
A **metadata JSON** (the “data contract”) is the *minimum* required input for trusted UI.

It should include (at least):  
- `id`, `title`, `description`  
- `license`, `attribution` / `source`  
- `spatial` extent (bbox + CRS)  
- `temporal` range  
- `provenance` links (source URLs, processing steps, lineage IDs)

> [!TIP]
> Treat contracts like code: schema versioned, validated, and CI-gated ✅

---

### 2) Catalog standards 🗂️  
KFM aligns catalog metadata to standards so other systems (and humans) can interpret it consistently:

- 🧭 **STAC**: geospatial assets and collections  
- 🏷️ **DCAT**: dataset-level catalog entries  
- 🧬 **PROV**: lineage/provenance graphs and processing history

These components should assume:  
- contracts can be rendered directly, **and/or**
- contracts can link to STAC/DCAT/PROV records the UI can fetch and display.

---

## 🛰️ End-to-end data flow (mental model)

```mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC/DCAT/PROV Catalog]
  B --> C[Neo4j Knowledge Graph]
  C --> D[APIs (REST/GraphQL)]
  D --> E[React + Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode Q&A]
```

This folder lives in **E** (React + Map UI) and focuses on making **B (catalog)** visible + understandable.

---

## 🧩 What should live in `web/components/data/`

### ✅ Good fits
- 📚 **Catalog UI**
  - dataset list/grid
  - search + filters
  - tags (theme, time range, geometry type, sensitivity)
- 🧾 **Dataset details**
  - metadata panels
  - license + attribution blocks
  - spatial/temporal summaries
- 🧬 **Provenance UI**
  - “Source → Processing → Output” trails
  - provenance badges (“Verified”, “Derived”, “Projection”, etc.)
- 🧰 **Layer controls (UI only)**
  - layer toggle
  - opacity slider
  - time slider bindings (UI-level controls, not rendering logic)

### 🚫 Not a good fit
- 🛰️ Map rendering / tile plumbing (belongs in `web/viewers/`)
- 🔌 API clients (prefer `web/lib/`, `web/services/`, or hooks like `web/hooks/`)
- 🧪 ETL scripts or catalog generation (belongs in `scripts/` / pipelines)
- 📚 Story content (belongs in `web/story_nodes/`)

---

## 🧰 Patterns & conventions

### 1) “UI reads contracts” (no hidden coupling) 🔍
Prefer component props shaped like:

- `DatasetContract`
- `CatalogEntry`
- `ProvenanceRecord`
- `LayerConfig`

…and avoid passing raw API responses deep into the tree.

---

### 2) Always show attribution + license 🧾
Every dataset surface (card, detail view, tooltip, layer panel) should include:

- **Source / publisher**
- **License**
- (Optional) “Last updated” + “Processing step” badges

> [!NOTE]
> If the dataset is a **projection/model**, label it clearly as such (e.g., “Scenario / Projection”).

---

### 3) UI states matter (trust UX) 🧠
For any network-bound view, include:

- ⏳ Loading (skeleton/placeholder)
- 🙅 Empty state (no matches)
- ⚠️ Error state (retry + friendly error)
- 📴 Offline / cached fallback (if supported)

---

### 4) Performance guidance ⚡
Catalogs can get big.

- 🪟 Use list virtualization when rendering many dataset cards
- 🧠 Memoize heavy computed summaries (temporal bins, tag aggregation)
- 📦 Lazy-load deep provenance graphs (“click to expand”)

---

## 🧾 Example: simplified dataset contract (for UI dev)

```json
{
  "id": "usgs_historic_topo_1894",
  "title": "USGS Historical Topographic Map (Ellsworth County, 1894)",
  "description": "Digitized 1894 USGS topographic survey of Ellsworth County, Kansas.",
  "license": "Public Domain",
  "schema_version": "v3.0.0",
  "spatial": {
    "bbox": [-99.5, 38.3, -98.8, 38.9],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "1894-01-01",
    "end": "1894-12-31"
  },
  "provenance": {
    "source_url": "https://www.usgs.gov/historical-topo",
    "creator": "U.S. Geological Survey",
    "issued": "1894-03-15"
  }
}
```

---

## 🧪 PR checklist (data components)

- [ ] ✅ Renders **license + source attribution**
- [ ] ✅ Handles **missing fields** gracefully (but warns in dev)
- [ ] ✅ Has **loading/empty/error** states
- [ ] ✅ Keyboard + screen reader friendly (labels, roles, focus order)
- [ ] ✅ No Kansas-only hard-coding (reads config/contracts)
- [ ] ✅ Uses typed props (`DatasetContract`, etc.), not `any`
- [ ] ✅ “No mystery layers”: UI only renders catalog/API-backed datasets

---

## 🔗 Related docs (recommended reading)

- 📘 `docs/MASTER_GUIDE_v13.md` (contract-first + evidence-first flow)
- 🗂️ `docs/standards/KFM_STAC_PROFILE.md`
- 🏷️ `docs/standards/KFM_DCAT_PROFILE.md`
- 🧬 `docs/standards/KFM_PROV_PROFILE.md`
- 🧾 `docs/data/contracts/…` (examples + validators)

---

## 🧠 Glossary (quick)

- **STAC** 🗂️: standard metadata format for geospatial assets/collections  
- **DCAT** 🏷️: dataset catalog vocabulary  
- **PROV** 🧬: provenance/lineage model  
- **COG** 🛰️: Cloud-Optimized GeoTIFF (fast web raster access)  
- **GeoParquet** 🧱: columnar vector storage (fast + analytics-friendly)

---

<p align="center">
  <sub>🧾 Trust is a UI feature. If we can’t cite it, we shouldn’t show it.</sub>
</p>
