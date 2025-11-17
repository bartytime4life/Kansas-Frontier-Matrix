---
title: "🌾 Kansas Frontier Matrix — Monorepo Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v10.4.0"
last_updated: "2025-11-16"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/root-readme-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Monorepo Overview**  
`README.md`

**Purpose:**  
Serve as the authoritative, MCP-governed root documentation for the Kansas Frontier Matrix (KFM) v10.4 monorepo — defining vision, architecture, quickstart, contributor workflows, metadata compliance, FAIR+CARE ethics, and system-wide governance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](docs/)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-green)](docs/standards/faircare.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Data License: CC-BY 4.0](https://img.shields.io/badge/Data%20License-CC--BY%204.0-lightgrey)](LICENSE)
[![Build Status](https://img.shields.io/badge/CI-Passing-brightgreen)](.github/workflows)
[![STAC Validated](https://img.shields.io/badge/STAC-Validated-orange)](data/stac/)
[![Semantic Version](https://img.shields.io/badge/Version-v10.4.0-blue)]()

</div>

---

## 📑 Table of Contents
- [📘 Overview](#-overview)
- [✨ Core Features](#-core-features)
- [🏗 Architecture](#-architecture)
- [🧭 Repository Structure](#-repository-structure)
- [🚀 Quickstart](#-quickstart)
- [🧪 Usage Examples](#-usage-examples)
- [🌐 Data Sources](#-data-sources)
- [🛰 External API Integrations](#-external-api-integrations)
- [🛡 FAIR+CARE Ethical Model](#-faircare-ethical-model)
- [🧵 Metadata & STAC/DCAT Compliance](#-metadata--stacdcat-compliance)
- [🧑‍💻 Developer Workflow](#-developer-workflow)
- [🤝 Contribution Guidelines](#-contribution-guidelines)
- [📚 References & Acknowledgements](#-references--acknowledgements)

---

## 📘 Overview
The **Kansas Frontier Matrix (KFM)** is a *semantic, geospatial, AI-augmented knowledge system* integrating:

- Kansas history  
- Tribal histories and cultural archives  
- Environmental and climate data  
- Geological & hydrological layers  
- Predictive simulations (2030–2100)  
- AI-powered narratives (Focus Mode v2 + Story Nodes v3)  

KFM v10.4 transforms the state’s past, present, and projected future into a **living data atlas**, navigable through:

- 🌎 **MapLibre 2D/3D spatial interface**  
- 🕰 **Temporal timeline with OWL-Time semantics**  
- 🧠 **AI Focus Mode v2 (context engine + ethical summarization)**  
- 🕸 **CIDOC CRM–aligned knowledge graph**  

---

## ✨ Core Features
- 🗺 **Interactive 2D/3D time-aware map** (MapLibre + Cesium)
- 🕰 **Semantic timeline** (OWL-Time, multi-era)
- 🧠 **Focus Mode v2** — dual-encoder transformer generating contextual, CARE-filtered summaries
- 🧾 **Story Nodes v3** — structured narrative units (JSON schema)
- 🕸 **Knowledge graph (Neo4j)** — CIDOC CRM + GeoSPARQL + PROV-O
- 📦 **STAC v1.0 + DCAT 3.0 metadata catalogs**
- 📚 **FAIR+CARE governed dataset ingestion**
- ⛓ **Predictive ETL** — allows future projections as first-class temporal data
- 🪶 **Indigenous data sovereignty protections (CARE-A, CARE-E)**
- 🧬 **AI explainability** — SHAP/LIME overlays in Focus Mode
- 🚀 **Containerized full stack** — FastAPI, React, Neo4j, pipelines
- 🔍 **Semantic + full-text search**
- 🧪 **Sanitized, reproducible pipelines (MCP v6.3)**

---

## 🏗 Architecture

### 🌐 High-Level Diagram

```mermaid
flowchart LR
    subgraph ExternalData[External Data Sources]
        NOAA[(NOAA Climate)]
        USGS[(USGS Geospatial)]
        DPLA[(Digital Archives)]
        Tribal[(Tribal Records)]
        FEMA[(FEMA Disasters)]
        GBIF[(Biodiversity Data)]
    end

    ExternalData --> ETL[ETL + AI Pipeline]
    ETL --> OCR[OCR]
    ETL --> NER[NER]
    ETL --> Geocoding[Geocoding]
    ETL --> ML[ML]
    ETL --> PredictiveModels[Predictive Models]

    ETL --> Graph[Neo4j Knowledge Graph]
    Graph --> API[FastAPI / GraphQL API]
    API --> Frontend[React + MapLibre + Cesium]

    API <-- Telemetry[Telemetry v3]
```

## 🧭 Repository Structure

```plaintext
Kansas-Frontier-Matrix/
├── src/
│   ├── pipelines/etl/
│   ├── ai/models/focus_transformer_v2/
│   ├── api/
│   ├── graph/
│   └── telemetry/
├── web/
│   ├── src/components/
│   ├── src/features/map/
│   ├── src/features/timeline/
│   └── src/features/story/
├── data/
│   ├── sources/        # DCAT v3.0 source manifests
│   ├── raw/            # DVC-tracked raw data
│   ├── processed/      # GeoJSON, COGs, Parquet
│   └── stac/           # STAC v1.0 catalog
├── docs/
│   ├── architecture/
│   ├── standards/
│   ├── templates/
│   └── workflows/
├── scripts/
├── tools/
└── tests/
```

---

## 🚀 Quickstart

### 🔧 Using Docker (Recommended)

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
docker-compose up --build
```

Backend → [http://localhost:8000](http://localhost:8000)
Frontend → [http://localhost:3000](http://localhost:3000)

### 🖥 Manual Setup

```bash
make setup
make data
make build
make serve
```

---

## 🧪 Usage Examples

### 📍 Explore the map

1. Move the timeline slider.
2. Map layers auto-filter by temporal extent.
3. Click a feature → opens a Story Node or Focus summary.

### 🧠 Call Focus Mode API

```bash
GET /api/focus/fort_larned
```

### 📦 Load a STAC Item

```bash
GET /api/stac/items/usgs_topo_1894
```

### 🕸 Query Graph

```graphql
{
  events(during:"1854") {
    id
    label
    locatedAt { name }
  }
}
```

---

## 🌐 Data Sources

KFM integrates 200+ open datasets, including:

* **NOAA Climate / Storm Events**
* **USGS EarthExplorer / NHD / LiDAR**
* **Kansas DASC GIS Portal**
* **Kansas Historical Society (KHS)**
* **Library of Congress (Chronicling America)**
* **BLM Land Patents**
* **Tribal Lands & Treaties (Native Land Digital, LandMark)**
* **GBIF Biodiversity Records**
* **Mesonet (KSU)**
* **FEMA Declarations**

All datasets comply with DCAT 3.0, STAC 1.0, and FAIR+CARE metadata requirements.

---

## 🛰 External API Integrations

* **NOAA CDO API**
* **USGS API (Water, Topo, Earthquakes)**
* **FEMA OpenAPI**
* **GBIF Occurrence API**
* **Mesonet API**
* **DPLA + Chronicling America**
* **OpenStreetMap / Nominatim**
* **GeoNames / GNIS**

---

## 🛡 FAIR+CARE Ethical Model

KFM v10.4 enforces:

* CARE-A: **Authority to Control**
* CARE-E: **Ethics of data use**
* CARE-C: **Collective Benefit**
* FAIR-F: **Findable**
* FAIR-A: **Accessible**
* FAIR-I: **Interoperable**
* FAIR-R: **Reusable**

All AI outputs (Focus Mode v2, summaries, patterns) undergo:

* Bias scoring
* Drift detection
* Sentiment safety checks
* Indigenous sovereignty filters
* Provenance chaining (PROV-O)

---

## 🧵 Metadata & STAC/DCAT Compliance

Every dataset includes:

* Spatial extent (bbox)
* Temporal extent (ISO-8601)
* License (SPDX)
* Provenance (PROV-O)
* Lineage chain
* CARE metadata
* STAC Item + DCAT Dataset pairing
* Checksums (SHA-256)

CI rejects any dataset missing required metadata.

---

## 🧑‍💻 Developer Workflow

### Standard Commands

```bash
make lint
make validate
make test
make data
make serve
```

### MCP v6.3 Workflow

1. Write docs first (templates in `docs/templates/`).
2. Add data → create DCAT manifest → STAC entries.
3. Update graph schema if needed.
4. Implement code.
5. Add tests.
6. Run full validation suite.
7. Submit PR → Governance review → Merge.

---

## 🤝 Contribution Guidelines

Follow:

* `CONTRIBUTING.md`
* `docs/standards/markdown_rules.md`
* `docs/standards/data-contracts.md`
* `docs/standards/faircare.md`

All PRs must pass:

* Docs lint
* STAC/DCAT validation
* Telemetry export
* FAIR+CARE audit
* Security scans
* Full test suite

---

## 📚 References & Acknowledgements

Thanks to:

* Kansas Historical Society
* USGS, NOAA, FEMA, DPLA
* Kansas DASC
* Tribal Nations and CARE partners
* Open-source communities (Neo4j, MapLibre, Cesium, spaCy, PyTorch)

<div align="center">

**Kansas Frontier Matrix v10.4 — “Where Kansas’s past and future converge in a living data matrix.”**
Built with 🕰 history, 🌎 geospatial precision, 🧠 AI assistance, and ❤️ community collaboration.

</div>
