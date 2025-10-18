<div align="center">

# 🏗️ **Kansas Frontier Matrix — System Architecture Overview**

### *“Time · Terrain · History · Knowledge Graphs”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![License: MIT \| CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-blue)](../../LICENSE)

</div>

---

## 📚 Table of Contents

- [🌾 Mission](#-mission)
- [🏛 Architectural Principles](#-architectural-principles)
- [🏗 System Diagram](#-system-diagram)
- [⚙️ Core Layers](#️-core-layers)
- [🧭 Data & File Architecture](#-data--file-architecture)
- [🧪 AI / ML Pipeline](#-ai--ml-pipeline)
- [🌐 API & Integration](#-api--integration)
- [🗽 Web Frontend](#-web-frontend)
- [🔒 Security & Provenance](#-security--provenance)
- [🧾 Change Management](#-change-management)
- [🧠 Environments & Quickstart](#-environments--quickstart)
- [🧾 Versioning & Metadata](#-versioning--metadata)
- [📚 References](#-references)

---

## 🌾 Mission

The **Kansas Frontier Matrix (KFM)** is a reproducible, open-science platform that connects Kansas’s **ecological, cultural, and historical record**.  
It fuses environmental datasets (NOAA, USGS, Daymet), historical maps & documents (KHS, treaties, archives), a **Neo4j knowledge graph** (CIDOC CRM + OWL-Time), and an **interactive React + MapLibre** frontend.

> **MCP mantra:** *Documentation-first · Reproducible · Provenanced · Auditable · Versioned.*

---

## 🏛 Architectural Principles

| Principle                      | Description                                                                 |
| :----------------------------- | :-------------------------------------------------------------------------- |
| **Documentation-First**        | Every change includes README/ADR/SOP updates and MCP metadata.              |
| **Reproducibility**            | Deterministic ETL, pinned containers, environment locks, **SHA-256**.       |
| **Open Standards**             | STAC · DCAT · CIDOC CRM · OWL-Time · GeoSPARQL · JSON-LD.                   |
| **Separation of Concerns**     | ETL/AI ↔ Graph ↔ API ↔ Web with typed contracts and schemas.                |
| **Defense-in-Depth**           | CodeQL · Trivy · signed workflows · artifact retention · audit logs.        |

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
  H --> J["API Layer<br/>FastAPI · GraphQL · REST · JSON-LD"]
  J --> F["Frontend (React + MapLibre GL)<br/>Timeline · Map · Search · AI Panels"]
  C --> K["Google Earth Exports<br/>KML / KMZ"]
%% END OF MERMAID
```

---

## ⚙️ Core Layers

### 🧬 1) ETL Pipeline
- Python (GDAL, Rasterio, Pandas) · `make fetch` · `make process` · `make stac`
- Outputs: **COG** rasters, **GeoJSON**, CSV + **STAC** descriptors
- CI gates: schema checks + checksum enforcement

### 🧠 2) AI / ML Enrichment
- OCR (Tesseract/OpenCV), NLP (spaCy + Transformers)
- Summarization (BART/T5), geocoding (GeoPy/GNIS)
- Entity linking → canonical graph IDs, confidence & provenance (PROV-O)

### 🕸 3) Knowledge Graph
- Neo4j + CIDOC CRM + OWL-Time + GeoSPARQL
- Relations: `MENTIONS`, `OCCURRED_AT`, `DERIVED_FROM`, …
- Optional RDF/JSON-LD exports

### 🔗 4) API Layer
- FastAPI + GraphQL; outputs JSON/GeoJSON/STAC/DCAT/JSON-LD
- Endpoints: `/api/events`, `/api/entities/{id}`, `/api/search`, `/api/tiles/{layer}/{z}/{x}/{y}.pbf`

### 🖥️ 5) Web Frontend
- React + Vite + MapLibre + Canvas/D3 timeline
- Map ↔ Timeline single time window; AI panel with citations
- **WCAG 2.1 AA** UI; GitHub Pages hosting

---

## 🧭 Data & File Architecture

```text
data/
  sources/     # Source manifests: license, coverage, URLs
  raw/         # Large inputs (LFS/DVC pointers)
  processed/   # GeoTIFF, GeoJSON, CSV
  stac/        # STAC Items & Collections (versioned)
```

Each dataset must ship with: **provenance metadata**, **SHA-256**, **STAC entry**, and an SOP/experiment log.

---

## 🧪 AI / ML Pipeline

| Component      | Role                               | Tools                 |
| :------------- | :---------------------------------- | :-------------------- |
| OCR            | Scan → text                         | Tesseract, OpenCV     |
| NLP            | Entity extraction                   | spaCy, Transformers   |
| Geocoding      | Place resolution                    | GeoPy, GNIS           |
| Summarization  | Abstractive/extractive summaries    | BART, T5              |
| Entity Linking | Disambiguation + graph integration  | Rules + similarity    |

> Models documented in `docs/templates/model_card.md`; training data tracked with hashes.

---

## 🌐 API & Integration

| Endpoint                      | Description                         |
| :---------------------------- | :---------------------------------- |
| `GET /api/events`            | Time & bbox filtered events         |
| `GET /api/entities/{id}`     | Entity dossier & relations          |
| `GET /api/search?q=...`      | Full-text + semantic search         |
| `GET /api/tiles/{layer}/…`   | Vector/raster tiles                 |
| `GET /stac/catalog.json`     | STAC root                           |

**Standards:** STAC 1.0 · DCAT 2.0 · JSON-LD · CIDOC CRM · OWL-Time

---

## 🗽 Web Frontend

| Subsystem     | Stack            | Highlights                                   |
| :------------ | :--------------- | :------------------------------------------- |
| Map           | MapLibre GL JS   | COG overlays, vector filters, legends        |
| Timeline      | Canvas + D3      | Smooth zoom/brush, interval filtering        |
| Panels        | React (typed)    | AI summaries, citations, entity dossiers     |
| Accessibility | WAI-ARIA + CSS   | Keyboard/SR support, AA contrast, skip-links |

---

## 🔒 Security & Provenance

| Area             | Strategy                                  |
| :--------------- | :----------------------------------------- |
| Auth             | JWT + RBAC                                 |
| Static Analysis  | **CodeQL**                                 |
| Dependency Scan  | **Trivy**                                  |
| Data Integrity   | **SHA-256** for artifacts & datasets       |
| Provenance       | PROV-O metadata + CI logs + STAC lineage   |
| Workflow Audit   | Pinned actions, branch protection, reviews |

---

## 🧾 Change Management

| Domain | Versioning                    |
| :----- | :---------------------------- |
| Code   | **SemVer**                    |
| Data   | STAC `properties.version`     |
| Docs   | MCP-DL metadata               |
| Models | `model_card.md` with history  |

**Flow:** branch → docs & manifests → `make stac-validate` → PR + CI → review/merge → version bump.

---

## 🧠 Environments & Quickstart

**Essential env vars**

```bash
# Backend
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASS=neo4j

# Web
VITE_API_URL=http://localhost:8000
VITE_MAP_STYLE_URL=/tiles/style.json
```

**Start locally**

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
pip install -r requirements.txt
cd web && pnpm install && cd ..
make fetch && make process && make stac
make serve
```

Open **http://localhost:3000** (web) · **http://localhost:7474** (Neo4j, if local).

---

## 🧾 Versioning & Metadata

| Field            | Value                                   |
| :--------------- | :--------------------------------------- |
| **Doc Version**  | `v6.3.2`                                 |
| **Release Type** | **Stable**                               |
| **Last Updated** | 2025-10-17                               |
| **Maintainers**  | @kfm-architecture · @kfm-data · @kfm-web |
| **Alignment**    | STAC · DCAT · CIDOC CRM · OWL-Time · GeoSPARQL |
| **Checksums**    | CI publishes SHA-256 sidecars for artifacts |

---

## 📚 References

- `docs/architecture/architecture.md`  
- `docs/architecture/file-architecture.md`  
- `docs/templates/model_card.md`  
- `docs/glossary.md`  
- `data/sources/*.json`  
- `data/stac/*.json`

<div align="center">

### 🏛 “Document the Frontier · Reconstruct the Past · Illuminate Connections.”

© 2025 Kansas Frontier Matrix — MIT (code) · CC-BY 4.0 (data/docs)

</div>