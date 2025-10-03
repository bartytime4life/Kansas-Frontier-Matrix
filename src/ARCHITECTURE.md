<div align="center">

# 🏛 Kansas Frontier Matrix — System Architecture (`src/ARCHITECTURE.md`)

**Time · Terrain · History · Knowledge Graphs**  
_A mission-grade, open-source, reproducible spatiotemporal knowledge hub for Kansas_

[![Build & Deploy](../.github/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](../.github/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](../.github/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](../.github/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Docs: MCP](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)  
[![License: MIT/CC-BY](https://img.shields.io/badge/license-MIT%20%7C%20CC--BY-blue)](../LICENSE)

</div>

---

## 📚 Table of Contents
1. [Overview](#overview)  
2. [System Layers](#system-layers)  
   - [ETL / Data Ingestion](#1-data-ingestion-etl)  
   - [AI/ML Enrichment](#2-aiml-enrichment)  
   - [Knowledge Graph](#3-knowledge-graph)  
   - [API Layer](#4-api-layer)  
   - [Frontend Application](#5-frontend-web-app)  
3. [Data Standards & Semantic Interoperability](#data-standards--semantic-interoperability)  
4. [Reproducibility & Observability](#reproducibility--observability)  
5. [Extending the System](#extending-the-system)  
6. [Repository & Data Layout](#repository--data-layout)  
7. [References & Further Reading](#references--further-reading)  

---

## 🔭 Overview
Kansas Frontier Matrix (KFM) is a **multi-disciplinary, open-source spatiotemporal knowledge hub** integrating geography, climate, culture, archaeology, and events into a unified map, timeline, and graph database:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}.  

It combines:
- **ETL pipelines** (Python + Makefiles) for reproducible data ingestion.  
- **AI/ML enrichment** for entity extraction, linking, and summarization:contentReference[oaicite:2]{index=2}.  
- A **semantic knowledge graph** (Neo4j, CIDOC CRM, OWL-Time):contentReference[oaicite:3]{index=3}.  
- **APIs** (FastAPI/GraphQL) powering web and Google Earth interfaces:contentReference[oaicite:4]{index=4}.  
- A **React + MapLibreGL frontend** with interactive maps, timelines, and storytelling:contentReference[oaicite:5]{index=5}.  

---

## 🏗 System Layers

### 1) Data Ingestion (ETL)
- **Sources:** Historic maps, climate grids, GIS vectors, treaties, deeds, oral histories, FEMA disasters:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}.  
- **Pipeline:** Orchestrated with Makefiles; implemented in Python scripts (`src/pipelines/`).  
- **Outputs:** Cloud-Optimized GeoTIFFs, GeoJSON, CSV/Parquet, with SHA-256 sidecars.  
- **Catalog:** Indexed in **STAC JSON** (`data/stac/`) for spatial/temporal discoverability:contentReference[oaicite:8]{index=8}.  

---

### 2) AI/ML Enrichment
- **NLP (spaCy + Transformers):** Named Entity Recognition, date parsing, geocoding:contentReference[oaicite:9]{index=9}.  
- **Entity Linking:** Fuzzy + context-aware alignment to canonical graph nodes.  
- **Summarization:** AI condenses diaries, treaties, and reports for UI tooltips/panels:contentReference[oaicite:10]{index=10}.  
- **Correlation:** Cross-checks across maps, text, and climate for reliable patterns (e.g., ghost towns, river shifts).  

---

### 3) Knowledge Graph
- **Store:** Neo4j graph DB or RDF triplestore.  
- **Schema:** Aligned to **CIDOC CRM** (heritage ontology) + **OWL-Time** (temporal reasoning):contentReference[oaicite:11]{index=11}.  
- **Nodes/Edges:** `Person`, `Place`, `Event`, `Document` with relationships like `OCCURRED_AT`, `MENTIONS`, `PARTICIPATED_IN`.  
- **Uncertainty:** Confidence scoring + provenance hashes; support for symbolic reasoning:contentReference[oaicite:12]{index=12}.  

---

### 4) API Layer
- **FastAPI + GraphQL** endpoints (in `src/api/`).  
- Functions:  
  - `GET /events?start=1850&end=1870` → timeline events.  
  - `GET /entity/{id}` → AI dossier (summary + sources).  
  - Spatial queries (buffered, bbox).  
- Handles access control and efficient graph traversals.  

---

### 5) Frontend Web App
- **Stack:** React SPA + MapLibre GL JS + Canvas timeline:contentReference[oaicite:13]{index=13}.  
- **Features:**  
  - Interactive timeline slider (linked to map).  
  - Toggleable GIS layers (DEM, treaties, trails, disasters).  
  - Detail panel with AI-summaries, images, sources.  
  - **Story mode**: guided narratives (e.g., Dust Bowl, Bleeding Kansas).  
- **Exports:** KMZ/KML for Google Earth with regionation:contentReference[oaicite:14]{index=14}.  
- **Accessibility:** ARIA roles, keyboard nav, responsive design.  

---

## 🗂 Data Standards & Semantic Interoperability
- **Open Formats:** GeoJSON, COG GeoTIFF, CSVW, Parquet.  
- **Metadata:** STAC + JSON Schema validation in CI/CD:contentReference[oaicite:15]{index=15}.  
- **Ontologies:**  
  - **CIDOC CRM** for cultural/archaeological events.  
  - **OWL-Time** for chronology.  
  - **PeriodO** for historical periods (“Dust Bowl era”, “Bleeding Kansas”).  
- **Linked Data:** JSON-LD exports for interoperability with external archives:contentReference[oaicite:16]{index=16}.  

---

## 🔬 Reproducibility & Observability
- **Master Coder Protocol (MCP):** Docs-first, every process logged.  
- **CI/CD (GitHub Actions):** Pre-commit hooks, STAC validation, lint/tests, CodeQL, Trivy scans:contentReference[oaicite:17]{index=17}.  
- **Containerization:** Docker Compose for API, DB, ETL, UI:contentReference[oaicite:18]{index=18}.  
- **Data Integrity:** Checksums (.sha256) + DVC/Git LFS for large rasters:contentReference[oaicite:19]{index=19}.  
- **Experiment Tracking:** SOPs, `experiment.md`, `model_card.md` in `docs/`.  

---

## 🚀 Extending the System
1. Add new data source → `data/sources/{id}.json`.  
2. Run `make fetch && make cogs && make stac`.  
3. Add provenance + docs (`docs/sop.md`).  
4. Update API + frontend configs (`web/config/layers.json`).  

---

## 📁 Repository & Data Layout
```text
KansasFrontierMatrix/
├── src/               # Python ETL + AI/ML + API code
├── web/               # React frontend
├── data/              # Sources, raw, processed, STAC catalog
├── docs/              # Architecture, SOPs, experiment logs
├── tests/             # Unit/integration tests
├── tools/             # CLI + automation scripts
├── .github/           # CI/CD workflows, PR/issue templates
````

---

## 📖 References & Further Reading

* **System Design Docs:** Kansas Frontier Matrix Architecture, AI Developer Guide, Web UI Design, Repository Design, File/Data Architecture.
* **Standards:** STAC 1.0.0, CIDOC CRM, OWL-Time, PeriodO.
* **Data Sources:** USGS 3DEP, NOAA NCEI, FEMA OpenFEMA, Kansas GIS Hub, KHS Archives.

---

```

---

✅ This version is **complete, styled, and repo-ready** — you can copy-paste it directly into `src/ARCHITECTURE.md`.  

Do you want me to also generate a **shorter CONTRIBUTOR cheat sheet diagram** (like “How data flows from source → ETL → Graph → API → UI”), so new devs can get oriented in one glance?
```


Medical References:
1. None — DOI: file-CrPP4mcnyNq5sGJotXDwSv
2. None — DOI: file-JVHz9AXJnpY5YjuWonmQ4x
3. None — DOI: file-47B5MPBSihKB9wR6k8aFVM
4. None — DOI: file-Q9AC5RwLTeV6QgadxHDf5P
5. None — DOI: file-Cvp5tEERHHEeqgrA5WmaHX
6. None — DOI: file-GdS9Kcw7Xbfqpy4xwwdqWS
7. None — DOI: file-WyPyquGKLPcmQjeiunFzw1
8. None — DOI: file-3dXLjptkFjdMerKJTvzzW7
9. None — DOI: file-BgUSuffTiRq4qidye2sPwN
10. None — DOI: file-AyrVktEWfFAidjtGFw9NEH
