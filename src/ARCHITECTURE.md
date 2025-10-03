<div align="center">

# 🏛 Kansas Frontier Matrix — **System Architecture**  
`src/ARCHITECTURE.md`

**⛰ Time · 🌍 Terrain · 📜 History · 🔗 Knowledge Graphs**  
_A mission-grade, open-source, reproducible spatiotemporal knowledge hub for Kansas_

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)  
[![Docs: MCP](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)  
[![License: MIT/CC-BY](https://img.shields.io/badge/license-MIT%20%7C%20CC--BY-green)](../LICENSE)

</div>

---

## 📚 Table of Contents
1. [🔭 Overview](#-overview)  
2. [🏗 System Layers](#-system-layers)  
3. [🧭 High-Level Architecture (Mermaid)](#-high-level-architecture-mermaid)  
4. [📦 Pipeline Sequence (Swimlane)](#-pipeline-sequence-swimlane)  
5. [🎨 Layer Timeline Legend](#-layer-timeline-legend)  
6. [🗂 Data Standards & Semantic Interoperability](#-data-standards--semantic-interoperability)  
7. [🔬 Reproducibility & Observability](#-reproducibility--observability)  
8. [🚀 Extending the System](#-extending-the-system)  
9. [📁 Repository & Data Layout](#-repository--data-layout)  
10. [📖 References & Further Reading](#-references--further-reading)  

---

## 🔭 Overview
Kansas Frontier Matrix (KFM) is a **multi-disciplinary, open-source spatiotemporal knowledge hub** integrating **geography, climate, archaeology, treaties, disasters, and oral histories** into a unified **map + timeline + semantic knowledge graph**.

---

## 🏗 System Layers
- **ETL / Ingestion:** normalize inputs (COG/GeoJSON), compute checksums, generate STAC items  
- **AI/ML Enrichment:** NER, geoparsing, summarization, entity linking  
- **Knowledge Graph:** semantic nodes/edges with provenance & confidence  
- **API Layer:** time/space/graph queries, dossier endpoints  
- **Frontend:** interactive timeline + map, layer toggles, story mode, KML/KMZ exports  

---

## 🧭 High-Level Architecture (Mermaid)

```mermaid
flowchart TD
    A["Sources<br/>Scans · Rasters · Vectors · Documents"] --> B["ETL Pipeline<br/>Makefile · Python · Checksums"]
    B --> C["Processed Layers<br/>COGs · GeoJSON · Parquet"]
    B --> I["AI/ML Enrichment<br/>NER · Geocoding · Summarization · Linking"]

    C --> D["STAC Catalog<br/>Collections · Items · Assets"]
    D --> H["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time"]
    I --> H

    D --> J["API Layer<br/>FastAPI · GraphQL"]
    H --> J

    J --> F["Frontend<br/>React + MapLibreGL<br/>Timeline · Search · Filters"]
    D --> F

    E["Config Build<br/>app.config.json · layers.json"] --> F
    E --> G["Google Earth Exports<br/>KML · KMZ"]
````

---

## 📦 Pipeline Sequence (Swimlane)

```mermaid
sequenceDiagram
    autonumber
    participant SRC as Source
    participant ETL as ETL
    participant STAC as STAC Catalog
    participant KG as Knowledge Graph
    participant API as API
    participant UI as Web UI

    SRC->>ETL: Provide scans/vectors/tables
    ETL->>ETL: Convert (COG/GeoJSON), reproject, checksums
    ETL->>STAC: Publish items/assets + temporal/spatial metadata
    ETL->>KG: Upsert entities + relations (provenance/confidence)
    UI->>API: /events?start=1850&end=1870&bbox=...
    API->>KG: Graph query (time + space filters)
    API-->>UI: Timeline slice + entity summaries
    UI->>STAC: Fetch COG/GeoJSON for map layers
    UI-->>User: Interactive map + timeline + AI dossier panel
```

---

## 🎨 Layer Timeline Legend

| Layer Category             | Example Dataset(s)                  | Timeline Range     | Map/Timeline Color Token | Notes                                         |
| -------------------------- | ----------------------------------- | ------------------ | ------------------------ | --------------------------------------------- |
| 🏔 **Terrain & DEMs**      | LiDAR 1m DEM, Hillshade             | 2018–2020 (modern) | `#6C757D` (gray)         | Basemap foundation, hillshade overlay         |
| 🗺 **Historic Topos**      | USGS 1894 Larned Map, 1930s Topos   | 1890–1950s         | `#8D5524` (sepia brown)  | Scanned topo sheets, tiled COGs               |
| 🧾 **Treaties & Cessions** | 1854 Treaty, Royce Cession Polygons | 1820–1870s         | `#0077B6` (deep blue)    | Polygon overlays linked to treaty docs        |
| 🌊 **Hydrology**           | Kansas River Flood 1951, Streamflow | 1850–Present       | `#0096C7` (cyan)         | River floodplains, water levels               |
| 🌾 **Land Use & Soils**    | 1937 Soil Survey, NLCD Landcover    | 1850–Present       | `#52B788` (green)        | Cropland, prairie loss, soil maps             |
| 🚂 **Infrastructure**      | 1900s Railroads, Trails             | 1850–1950s         | `#E63946` (red)          | Trails/rail lines with fade-out on disuse     |
| 🌪 **Hazards**             | Tornado Tracks, Drought Episodes    | 1950–Present       | `#F77F00` (orange)       | Tornado lines/points, FEMA disasters          |
| 🏛 **Cultural/Oral**       | Oral Histories, Site Dossiers       | Any (tagged)       | `#9D4EDD` (violet)       | Linked to knowledge graph text, not just maps |

> 🖌 **Design Note:** Colors are harmonized with timeline & legend UI for consistency. Suggested to add these tokens in `web/config/layers.json` under each layer definition.

---

## 🗂 Data Standards & Semantic Interoperability

* **Formats:** GeoJSON, Cloud-Optimized GeoTIFF, CSVW, Parquet
* **Catalog:** STAC 1.0.0 (collections/items/assets) + JSON Schema CI validation
* **Ontologies:** CIDOC CRM (heritage), OWL-Time (temporality), PeriodO (periods)
* **Linked Data:** JSON-LD export for external graph interoperability

---

## 🔬 Reproducibility & Observability

* **MCP (docs-first):** `docs/architecture.md`, `docs/sop.md`, `docs/experiment.md`, `docs/model_card.md`
* **CI/CD (GitHub Actions):** lint/tests, STAC validation, CodeQL, Trivy, container builds
* **Containers:** Docker Compose stack (ETL, API, DB, UI) with pinned versions
* **Data Integrity:** `.sha256` sidecars; DVC/Git LFS for large artifacts

---

## 🚀 Extending the System

1. Create manifest → `data/sources/{id}.json`
2. Run:

   ```bash
   make fetch && make cogs && make stac
   ```
3. Extend ETL → upsert entities/relations into Knowledge Graph
4. Add config → `web/config/layers.json` with style + popup fields
5. Update docs → `docs/sop.md` + screenshots

---

## 📁 Repository & Data Layout

```text
KansasFrontierMatrix/
├─ src/               # Python ETL + AI/ML + API code
├─ web/               # React frontend
├─ data/
│  ├─ sources/        # dataset manifests (no big binaries in git)
│  ├─ raw/            # fetched artifacts (DVC/LFS)
│  ├─ processed/      # COG, GeoJSON, CSV/Parquet outputs
│  └─ stac/           # STAC catalog (collections/items/assets)
├─ docs/              # architecture, SOPs, experiments, model cards
├─ tools/             # CLI + automation helpers
├─ tests/             # unit/integration tests for Python/JS
└─ .github/           # CI/CD workflows, PR/issue templates
```

---

## 📖 References & Further Reading

* **System Docs:** Architecture, AI Dev Guide, Web UI Design, Repo/Monorepo Design, File/Data Architecture
* **Standards:** STAC 1.0.0, CIDOC CRM, OWL-Time, PeriodO
* **Data Hubs:** USGS 3DEP, NOAA NCEI, FEMA OpenFEMA, Kansas GIS Hub, Kansas Historical Society Archives

---

> ✨ *“KFM is not just a data platform—it’s a living atlas of Kansas, built for reproducibility, discovery, and storytelling.”*

```

---

✅ With this **Layer Timeline Legend**, devs/designers now have a **style guide + temporal index** to keep UI/timeline consistent with backend data.  
