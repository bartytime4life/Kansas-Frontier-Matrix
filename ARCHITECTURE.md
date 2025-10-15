div align="center">

# 🏗️ **Kansas Frontier Matrix — System Architecture Overview**

### *“Time · Terrain · History · Knowledge Graphs”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![License: MIT | CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-blue)](../../LICENSE)

</div>

---

## 📚 Table of Contents
* [🌾 Mission](#🌾-mission)
* [🏛 Architectural Principles](#🏛-architectural-principles)
* [🏗 System Diagram](#🏗-system-diagram)
* [⚙️ Core Layers](#⚙️-core-layers)
* [🧭 Data & File Architecture](#🧭-data--file-architecture)
* [🧮 AI / ML Pipeline](#🧮-ai--ml-pipeline)
* [🌐 API & Integration](#🌐-api--integration)
* [🗺 Web Frontend](#🗺-web-frontend)
* [🔒 Security & Provenance](#🔒-security--provenance)
* [🧾 Change Management](#🧾-change-management)
* [📚 References](#📚-references)

---

## 🌾 Mission

The **Kansas Frontier Matrix (KFM)** connects the *ecological, cultural, and historical record of Kansas*  
through a reproducible, open-science platform. It integrates:

- Environmental & climate datasets (NOAA, USGS, Daymet)  
- Historical documents & maps (KHS, archives, treaties)  
- Semantic knowledge graph (Neo4j + CIDOC CRM)  
- Interactive frontend (React + MapLibre + D3 timeline)

Each layer of the system is built under **Master Coder Protocol (MCP)** principles:
> Documentation-first · Reproducible · Provenanced · Auditable · Versioned.

---

## 🏛 Architectural Principles

| Principle | Description |
| :-- | :-- |
| **Documentation-First** | Every component change has an accompanying doc or SOP. |
| **Reproducibility** | Deterministic ETL pipelines and checksums guarantee reproducible builds. |
| **Open Standards** | Uses STAC, DCAT, CIDOC CRM, OWL-Time, GeoSPARQL for interoperability. |
| **Version Control Everywhere** | Code (SemVer), Data (STAC), Docs (MCP-DL metadata). |
| **Auditability** | All CI pipelines log checksums, signatures, and provenance events. |

---

## 🏗 System Diagram

```mermaid
flowchart TD
  A["Sources<br/>Historical Maps · Rasters · Text Archives · APIs"]
    --> B["ETL Pipeline<br/>Python · GDAL · Makefile · Checksums"]
  B --> C["Processed Layers<br/>COG · GeoJSON · CSV"]
  B --> I["AI / ML Enrichment<br/>NER · OCR · Geocoding · Summaries"]
  C --> D["STAC Catalog<br/>Collections · Items · Assets"]
  D --> H["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time"]
  I --> H
  H --> J["API Layer<br/>FastAPI · GraphQL · REST"]
  J --> F["Frontend (React + MapLibre GL)<br/>Timeline · Map · Search · AI Panels"]
  C --> K["Google Earth Exports<br/>KML / KMZ"]
%% END OF MERMAID
````

---

## ⚙️ Core Layers

### 🧩 1. ETL Pipeline

* **Language:** Python (GDAL, Rasterio, Pandas)
* **Stages:** Extract → Transform → Load
* **Execution:** via `make fetch`, `make process`, `make stac`
* **Output:** standardized GeoJSON / COG + STAC metadata
* **Validation:** schema + checksum verification in CI

### 🧠 2. AI / ML Enrichment

* **OCR:** Tesseract, OpenCV for scanned docs
* **NLP:** spaCy + Transformers for entity extraction
* **Summarization:** BART / T5 for document abstracts
* **Entity Linking:** custom matchers aligning text entities → graph nodes
* **Outputs:** structured entities (`Person`, `Place`, `Event`, `Document`)

### 🕸 3. Knowledge Graph

* **Engine:** Neo4j
* **Schema:** CIDOC CRM + OWL-Time + DCAT
* **Relations:** `OCCURRED_AT`, `MENTIONS`, `LOCATED_IN`, `PARTICIPATED_IN`
* **Spatial Index:** GeoSPARQL / WKT geometries
* **Inference:** rule-based + confidence scoring

### 🔌 4. API Layer

* **Framework:** FastAPI + GraphQL
* **Endpoints:** `/events`, `/entities/{id}`, `/timeline`, `/search`
* **Formats:** JSON, GeoJSON, CSV, STAC, DCAT
* **Auth:** JWT + audit logging
* **OpenAPI Spec:** auto-generated `/docs` route

### 🖥 5. Web Frontend

* **Stack:** React + MapLibre GL + D3 Timeline
* **Features:**

  * Interactive map + timeline linked to knowledge graph
  * Search and AI-assistant sidebar
  * Accessibility (WCAG 2.1 AA)
* **Deployment:** GitHub Pages via `site.yml`

---

## 🧭 Data & File Architecture

| Directory         | Purpose                                            |
| :---------------- | :------------------------------------------------- |
| `data/sources/`   | JSON manifests (source configs + provenance)       |
| `data/raw/`       | Large external datasets (fetched, LFS/DVC tracked) |
| `data/processed/` | Normalized GeoJSON / COG outputs                   |
| `data/stac/`      | STAC catalog (items, collections)                  |
| `src/`            | Python ETL + AI pipelines                          |
| `web/`            | React frontend (Map + Timeline)                    |
| `docs/`           | Architecture, SOPs, standards                      |
| `.github/`        | Workflows, issue templates                         |

Each dataset must include:

* ✅ **Provenance metadata** (source URL, license)
* ✅ **SHA-256 checksum** sidecar
* ✅ **STAC JSON** with `properties.version`
* ✅ **Linked SOP or experiment record**

---

## 🧮 AI / ML Pipeline

| Component      | Role                                 | Tools / Libs                     |
| :------------- | :----------------------------------- | :------------------------------- |
| OCR            | Convert scanned images → text        | Tesseract, OpenCV                |
| NLP            | Extract names, places, events        | spaCy, Hugging Face Transformers |
| Geocoding      | Resolve locations → coordinates      | GeoPy, USGS GNIS                 |
| Summarization  | Condense large texts                 | BART, T5                         |
| Entity Linking | Connect text entities to graph nodes | Custom ML + Neo4j driver         |

> All models are documented via `docs/model_card.md`
> Training datasets are versioned with DVC + checksum logs.

---

## 🌐 API & Integration

**Endpoints**

| Route                               | Description                      |
| :---------------------------------- | :------------------------------- |
| `/api/events`                       | Query events by time & geography |
| `/api/entities/{id}`                | Retrieve linked data entity      |
| `/api/search?q=<term>`              | Text/semantic search             |
| `/api/timeline?start=<y1>&end=<y2>` | Chronological range query        |
| `/api/tiles/{layer}`                | Tile service (GeoJSON / raster)  |

**Format Compliance:**

* STAC 1.0.x
* DCAT 2.0
* JSON-LD contexts for semantic linking

**Integration Points:**

* Web frontend (MapLibre layers)
* Google Earth KML/KMZ exports
* Research APIs for AI queries

---

## 🗺 Web Frontend

| Layer             | Technology          | Purpose                             |
| :---------------- | :------------------ | :---------------------------------- |
| **UI Framework**  | React + Vite        | SPA structure                       |
| **Map Engine**    | MapLibre GL JS      | render GIS layers & time data       |
| **Timeline**      | D3 / Canvas         | spatio-temporal event visualization |
| **Accessibility** | WAI-ARIA / WCAG 2.1 | inclusive design                    |
| **Hosting**       | GitHub Pages        | static build deployment             |

**Features**

* Linked Map + Timeline views
* Layer toggles (treaties, terrain, hydrology, etc.)
* AI summary popups
* Semantic highlighting of entities

---

## 🔒 Security & Provenance

| Control                 | Mechanism                                        |
| :---------------------- | :----------------------------------------------- |
| **Authentication**      | JWT (FastAPI middleware)                         |
| **Dependency Scanning** | Trivy CI workflow                                |
| **Static Analysis**     | CodeQL                                           |
| **Data Integrity**      | SHA-256 checksums per file                       |
| **Access Control**      | Role-based permissions                           |
| **Audit Logs**          | stored for ETL + API interactions                |
| **CI/CD Governance**    | Signed actions, branch protection, version gates |

---

## 🧾 Change Management

**Versioning Policy**

* **Code:** Semantic Versioning (SemVer)
* **Data:** STAC `properties.version`
* **Docs:** MCP-DL metadata header
* **Models:** Model Card revisions

**Workflow**

1. Create feature branch → `feature/<short-name>`
2. Update documentation → `/docs/` + `/data/sources/`
3. Validate STAC → `make stac-validate`
4. Open PR using Feature Request template
5. CI checks (unit, schema, security)
6. Merge → version bump → changelog update

---

## 📚 References

* [`File and Data Architecture`](../file-and-data-architecture.md)
* [`Monorepo Repository Design`](../kansas-frontier-matrix-monorepo-repository-design.pdf)
* [`GIS Archive & Deeds Integration`](../kansas-frontier-matrix-gis-archive--deeds-data-integration-guide.pdf)
* [`Web UI Design`](../kansas-frontier-matrix-web-ui-design-document.pdf)
* [`MCP Documentation`](../scientific-method--research--master-coder-protocol-documentation.pdf)

---

<div align="center">

### 🏛 “Document the Frontier · Reconstruct the Past · Illuminate Connections.”

© 2025 Kansas Frontier Matrix — MIT (code) · CC-BY 4.0 (data)

</div>
```
