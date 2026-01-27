<div align="center">

# 🧭 Kansas Frontier Matrix (KFM)

**Open-source geospatial + historical mapping hub for Kansas — from raw sources ➜ governed datasets ➜ interactive 2D/3D maps ➜ evidence-backed answers.**[^kfm_system]

<p>
  <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix"><img alt="Repo" src="https://img.shields.io/badge/GitHub-Kansas--Frontier--Matrix-181717?style=for-the-badge&logo=github"></a>
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="Stars" src="https://img.shields.io/github/stars/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="Issues" src="https://img.shields.io/github/issues/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
</p>

**Quick links:**  
[🚀 Quickstart](#-quickstart) · [🗺️ Features](#️-features) · [🏗️ Architecture](#️-architecture-at-a-glance) · [📦 Repo layout](#-repo-layout) · [🤖 Focus Mode AI](#-focus-mode-ai-local-first-but-governed) · [🤝 Contributing](#-contributing) · [📚 Project library](#-project-library)

</div>

---

## 🔎 What is KFM?

KFM is a **pipeline → catalog → database → API → UI** system designed to turn raw historical + geospatial sources into **traceable** map layers and narrative experiences — with an emphasis on *provenance-first* data and governed AI assistance.[^kfm_system]

> [!IMPORTANT]
> KFM is designed to **fail closed**: if policy/permission is uncertain, access is denied by default.[^fail_closed]

---

## 🗺️ Features

### ✅ What you can do (today + near-term)

- **Ingest & normalize** raw sources (rasters, vectors, tables) into cleaned “processed” artifacts.[^kfm_flow]
- **Publish a catalog** using standards-friendly outputs (STAC / DCAT + explicit provenance logs) so people can trust what they’re seeing.[^stac_dcat_prov]
- **Explore Kansas in 2D & 3D** with modern web mapping (MapLibre) + optional 3D globe/terrain (Cesium).[^tech_stack]
- **Use “story maps”**: narrative Markdown + a choreography script that drives map state (camera, layers, timeline).[^story_format]
- **Ask questions** in *Focus Mode* and get responses that remain constrained by governance (even with a local model).[^focus_mode][^local_model_governance]
- **Export & interop**: common geospatial outputs (GeoJSON, KML/KMZ, etc.) for sharing and downstream analysis.[^exports]

### 🧬 Project principles

- **Metadata is not optional.** A dataset isn’t “in” until it has a dataset card + machine-readable metadata.[^stac_dcat_prov][^metadata_standards]
- **Cartography is communication.** We design maps with essentials like legend/scale/credits, and we explicitly track coordinate/projection context.[^map_elements][^coords_proj]
- **Provenance over vibes.** Every claim should be traceable to a source, a dataset artifact, or a script run.[^kfm_system][^doc_governance]

---

## 🚀 Quickstart

### ✅ Recommended: Docker Compose

```bash
# from the repo root
docker compose up --build
```

Then open:

- 🖥️ **Web UI**: `http://localhost:3000`  
- 🧠 **API**: `http://localhost:8000`  
- 📘 **Swagger / OpenAPI docs**: `http://localhost:8000/docs`  
- 🕸️ **Neo4j Browser**: `http://localhost:7474`  

If ports conflict, change mappings in `docker-compose.yml` and restart.[^docker_compose]

---

### 🧰 Local dev (manual) — for contributors

<details>
<summary><b>Backend (FastAPI)</b></summary>

KFM’s backend follows a clean-ish separation: routers validate inputs, call service logic, and enforce governance checks in one place.[^fastapi_arch]

Typical flow:

```bash
# (example)
python -m venv .venv
source .venv/bin/activate
pip install -r api/requirements.txt

uvicorn api.main:app --reload --port 8000
```

- API endpoints are defined via routers; FastAPI dependency injection can provide DB sessions/repositories.[^fastapi_arch]
- GraphQL can be mounted optionally (if enabled) for nested queries.[^fastapi_arch]

</details>

<details>
<summary><b>Frontend (React + MapLibre + optional Cesium)</b></summary>

```bash
# (example)
cd web
npm install
npm run dev
```

The UI stack described in the design docs centers on MapLibre for 2D, with Cesium as an optional 3D viewer.[^tech_stack]

</details>

<details>
<summary><b>Datastores (PostGIS + Neo4j)</b></summary>

- PostGIS stores spatial primitives + queryable layers (parcels, boundaries, overlays).
- Neo4j stores relationships (events ↔ people ↔ places) for story graphs and “relatedness.”[^tech_stack]

If you’re scripting PostGIS access from Python, a common pattern is `psycopg2` + geometry libraries.[^py_postgis_recipe]

</details>

---

## 🍳 Usage recipes

### 1) Explore the API surface

- Open `http://localhost:8000/docs` (Swagger UI).[^docker_compose]
- Use it to try endpoints and inspect request/response models.[^fastapi_arch]

### 2) Add a new dataset the “KFM way” (raw ➜ processed ➜ catalog)

At minimum, a pipeline contribution should produce:

- **STAC** (Item/Collection depending on dataset shape)
- **DCAT** dataset record
- **Provenance log** (W3C PROV-style or compatible lineage record)[^stac_dcat_prov]

> [!TIP]
> CI is expected to reject contributions that don’t include the required documentation + metadata. The intent is: **no data enters KFM without documentation.**[^stac_dcat_prov]

### 3) Run Focus Mode AI with a local model (Ollama)

<details>
<summary><b>Install + run Ollama</b></summary>

Ollama runs open-source models locally (macOS/Windows/Linux).[^ollama_overview]

```bash
# Linux install (per Ollama guide)
curl -fsSL https://ollama.com/install.sh | sh

# pull and run a model
ollama pull llama3.2
ollama run llama3.2

# server mode (if needed)
ollama serve
```

</details>

> [!IMPORTANT]
> A local model **does not bypass** governance. Focus Mode still applies policy checks and logging, and can sandbox or reject sensitive requests.[^local_model_governance]

### 4) Build a “story map” (narrative + choreography)

A typical story is:
- a **Markdown narrative** (with citations), and  
- a **script** that maps sections/scroll positions to map actions (center/zoom/layers/timeline).[^story_format]

This enables guided narratives like “Dust Bowl in Kansas” where the UI transitions as the reader scrolls.[^story_format]

---

## 🏗️ Architecture at a glance

### Data + map lifecycle

```mermaid
flowchart LR
  A[📥 Raw sources\n(data/raw)] --> B[🧼 Processing pipelines\n(pipelines/*)]
  B --> C[📦 Processed artifacts\n(data/processed)]
  C --> D[🗂️ Catalog + metadata\nSTAC/DCAT\n(data/stac, data/catalog)]
  C --> E[🧾 Provenance logs\n(data/provenance)]
  D --> F[(🗄️ Datastores\nPostGIS / Neo4j)]
  F --> G[🔌 API\nFastAPI]
  G --> H[🗺️ UI\nReact + MapLibre\n(+ Cesium optional)]
  G --> I[🤖 Focus Mode\n(governed AI)]
```

KFM is explicitly described as pipeline–catalog–database–API–UI, with a strong emphasis on traceability and provenance.[^kfm_system]

---

## 📦 Repo layout

A practical “mental map” of the repo (adjust to match your current structure):

```text
📦 Kansas-Frontier-Matrix/
├─ 🧠 api/                  # FastAPI backend (routers, services, repos)
├─ 🖥️ web/                  # React UI (MapLibre + optional Cesium)
├─ 🧰 pipelines/             # ETL + validation + exporters
├─ 🗃️ data/
│  ├─ 📥 raw/               # Immutable inputs (as obtained)
│  ├─ 🧼 processed/          # Cleaned/normalized outputs
│  ├─ 🧾 provenance/         # Lineage logs (W3C PROV-style or compatible)
│  ├─ 🗂️ stac/               # STAC Items/Collections
│  └─ 🧾 catalog/            # DCAT/other catalog records (if separated)
├─ 📚 docs/                 # Architecture, governance, guides
├─ 🛡️ policy/               # Governance rules (OPA/Rego, etc.)
└─ 🧩 .github/              # Community health, templates, workflows
```

This monorepo structure is consistent with the documented project layout expectations and staging outputs (raw/processed/STAC/PROV).[^repo_layout]

---

## 🧭 Cartography, coordinates, and “don’t lie with maps”

### Minimum map essentials (UI + exports)

When presenting a map (especially in stories), aim to include:

- Title / explanatory text  
- Legend  
- Scale  
- Direction indicator  
- Border  
- Sources & credits (including projection/coordinate system)  
- Projection + coordinate system metadata[^map_elements]

### Metadata standards & interoperability

Good GIS data should carry explicit metadata: identification, quality, spatial organization, spatial reference (projection/coordinate system), attributes, distribution/use policy, temporal info, and citation guidance.[^metadata_standards]

### Coordinate systems you will bump into

Expect a mix of:
- **Geographic coordinates (lat/long)**
- **UTM**
- **State Plane Coordinate System (SPCS)**[^coords_proj]

And when reading grids: “**read right and up**” for easting/northing — it’s a foundational convention for consistent referencing.[^grid_reading]

> [!CAUTION]
> Many spatial operations require projected coordinates in meters. Using lat/long degrees (e.g., EPSG:4326) can break distance/area logic.[^meters_not_degrees]

---

## 🧊 3D / 4D GIS and time

KFM’s design supports time-aware and 3D-aware narratives. In 3D GIS practice, representing data across **multiple scales** and **multiple times** is central — and often requires clear acquisition routines and data organization.[^arch3d_multitemporal][^arch3d_multiscale]

---

## 📊 Analytics and QA

Exploratory visualizations (histograms, scatterplots, scatterplot matrices, etc.) are powerful for revealing structure and patterns — and should be paired with statistical checks when needed.[^r_graphics]

---

## 🤖 Focus Mode AI: local-first, but governed

Focus Mode is designed as a constrained workflow: it bundles relevant context, applies policies, and provides traceable, grounded responses rather than unbounded chat.[^focus_mode]

If you choose local inference, KFM’s design emphasizes that the governance layer remains in control and can restrict/deny access where necessary.[^local_model_governance]

---

## 🧼 Data quality, validation, and “messy data reality”

Data quality failures (incorrect/inconsistent records) can distort analysis. KFM pipelines are expected to validate and log what they did, and contributors should treat cleaning and preparation as first-class work.[^data_quality][^stac_dcat_prov]

---

## 🤝 Contributing

### How to contribute effectively

- **Document-first:** write/update the dataset card and citations as you build the pipeline output.[^doc_governance]
- **Reproducible methods:** treat pipeline runs like experiments (inputs, method, outputs).[^master_coder]
- **Keep docs synced:** if code changes, update docs in the same PR.[^master_coder]

### PR checklist (suggested)

- [ ] Data placed under `data/raw/<domain>/...` with source notes  
- [ ] Pipeline produces `data/processed/...` outputs  
- [ ] STAC/DCAT + provenance artifacts generated and linked[^stac_dcat_prov]  
- [ ] Map/story content includes citations and credits[^story_format][^doc_governance]  
- [ ] Tests / validations updated (or added) where applicable[^master_coder]

### Sensitive / culturally restricted data

If a dataset or story involves sensitive locations, consider redaction or aggregation, and label sensitivity explicitly (e.g., a `care_label` or equivalent governance metadata).[^doc_governance]

---

## 📚 Project library

These files actively inform KFM’s architecture, implementation patterns, and writing standards:

- **Kansas Frontier Matrix – Comprehensive Technical Blueprint** (architecture + governance + pipelines + UI + AI)[^kfm_system]  
- **Open-Source Geospatial Historical Mapping Hub Design** (data layers, sources, export goals, UI stack)[^tech_stack][^exports]  
- **Ollama guide** (local LLM workflow and commands)[^ollama_overview]  
- **Making Maps (GIS cartographic design)** (map elements, metadata, interoperability, copyright)[^map_elements][^metadata_standards]  
- **Map Reading & Land Navigation** (grid conventions + coordinate reading)[^grid_reading]  
- **Archaeological 3D GIS** (multi-temporal, multi-scale 3D/4D representation concepts)[^arch3d_multitemporal]  
- **Graphical Data Analysis with R** (EDA and visualization mindset)[^r_graphics]  
- **Python Geospatial Analysis Cookbook** (projection gotchas; PostGIS + GDAL patterns)[^meters_not_degrees][^py_postgis_recipe]  
- **Scientific Method / Master Coder Protocol** (reproducibility + coding standards + CI mindset)[^master_coder]  

> [!NOTE]
> Additional project PDFs (e.g., **Programming Resources**, **GIS Mapping/Geocomputation Python**, **USGS projections**) are great candidates to place under `docs/library/` and reference from dataset cards and story sources.

---

## 📜 Notice & licensing

- Respect source licensing and attribution. Map *data* may be reusable even when map *representation* is copyrighted — document both carefully.[^metadata_standards]
- See `LICENSE` for code licensing (and dataset cards for data licensing).

---

## 🧾 Sources (footnotes)

[^kfm_system]: KFM is described as a **“pipeline–catalog–database–API–UI system”** and explicitly **“provenance-first”**, emphasizing traceable layers and explainable answers. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^kfm_flow]: KFM’s core pipeline sequence is presented as **Raw → Processed → Catalog/Provenance → Database → API → UI**. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^docker_compose]: Docker Compose quickstart + default local ports: UI `:3000`, API `:8000` with `/docs`, and Neo4j `:7474` (and port-conflict note). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^fail_closed]: Governance principle: **fail closed** (deny access when uncertain). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^focus_mode]: Focus Mode described as a constrained workflow that builds context bundles and operates under governance (not “uncontrolled chat”). [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^local_model_governance]: Local model support (Ollama) still enforces the same policy checks/logging and can sandbox or deny sensitive requests; local inference does not bypass governance. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^ollama_overview]: Ollama overview: local LLM platform using llama.cpp, cross-platform support, and general positioning as an open-source local runner.
[^exports]: Data sharing/export goals (e.g., KML/KMZ and other common formats) as part of the hub’s interoperability aims.
[^tech_stack]: UI/stack concepts include MapLibre GL JS for 2D, CesiumJS for 3D, with PostGIS/Neo4j in the backend design layer discussion. [oai_citation:6‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^repo_layout]: Expected monorepo organization (data layers, pipelines, API, UI, docs) and a structured layout for consistent contributions. [oai_citation:7‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH) [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^stac_dcat_prov]: Pipeline contract: produce STAC/DCAT records and a provenance log; CI rejects missing documentation; “no data enters without documentation.” [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^map_elements]: Map design essentials include scale, explanatory text, legend, directional indicator, border, sources/credits, and explicitly listing projection/coordinate system details. [oai_citation:10‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^metadata_standards]: GIS metadata categories (including spatial reference, temporal info, distribution/use policy, citation info), FGDC standards mention, interoperability definition, and copyright notes about representation vs facts/data. [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
[^coords_proj]: Coordinate system overview (lat/long vs UTM vs State Plane), and the role of datums/ellipsoids in spatial reference context. [oai_citation:12‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^grid_reading]: Grid coordinate rule of thumb: **“read right and up”** (easting then northing) and MGRS basics for consistent referencing.
[^meters_not_degrees]: Projection warning: some operations require projected units in meters; using EPSG:4326 degrees can break calculations and rasterization assumptions. [oai_citation:13‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^arch3d_multitemporal]: 3D GIS practice emphasizes **multi-temporal** approaches and the challenge of modeling changing landscapes over time in GIS representations. [oai_citation:14‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^arch3d_multiscale]: 3D GIS representations often require **multi-scale** (macro/meso/micro) consistency and careful acquisition routines for coherent modeling. [oai_citation:15‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^r_graphics]: EDA framing: graphics can reveal structure/patterns (histograms/scatterplots/etc.) and should be paired with statistical methods where appropriate.
[^data_quality]: Data quality warning: incorrect/inconsistent data can distort analysis; data preparation/cleaning is critical in data workflows. [oai_citation:16‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
[^fastapi_arch]: FastAPI architecture notes: routers validate inputs, call service logic, use DI for DB sessions, and apply governance checks; optional GraphQL mounting is discussed. [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^py_postgis_recipe]: Example patterns for Python + PostGIS access (psycopg2 connectivity and geospatial data handling appear in recipe-style form). [oai_citation:18‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^master_coder]: Scientific-method and reproducibility expectations (protocols, data collection, analysis, results traceability) plus environment setup/versioning guidance. [oai_citation:19‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^doc_governance]: Documentation governance guidance: doc templates + Definition of Done checklists, explicit citations, and sensitivity labels (e.g., `care_label`) for restricted content handling. [oai_citation:21‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) [oai_citation:22‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^story_format]: Story format: narrative Markdown with citations plus a choreography script mapping narrative sections to map state (center/zoom/layers/timeline). [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)