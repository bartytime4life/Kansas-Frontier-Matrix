---
title: "📚 Kansas Frontier Matrix — Master Guide v10 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/MASTER_GUIDE_v10.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/master-guide-v1.json"
governance_ref: "./standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — MASTER GUIDE v10**  
**The Complete System Bible — Architecture · Data · AI · UX · Governance**  
`docs/MASTER_GUIDE_v10.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose:**  
Serve as the **definitive, canonical reference** for the Kansas Frontier Matrix (KFM) v10+.  
Every subsystem, layer, workflow, and governance rule is defined here.  
**This file governs v10+.**

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-System%20Certified-gold.svg)](standards/faircare.md)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success.svg)]()

</div>

---

## 📘 Overview

The **Kansas Frontier Matrix (KFM)** is a unified, semantic, geospatial–temporal system reconstructing **Kansas through time** — historically, ecologically, hydrologically, and culturally.

KFM integrates:

- Hydrology, climate, drought/flood indices, hazards  
- Land cover, terrain, soils, geology, geomorphology  
- Treaties, homesteads, land patents, ownership, plats  
- Census, crop records, wildlife, insects, pests  
- Archaeological data, diaries, newspapers, letters, archives  
- AI-powered narratives, explainability, and Focus Mode entity-centric views  

Powered by:

- Python ETL pipelines + LangGraph orchestrated agents  
- STAC 1.0 / DCAT 3.0 metadata  
- Neo4j knowledge graph with CIDOC CRM + GeoSPARQL + OWL-Time  
- React + MapLibre + Cesium 3D front-end  
- FAIR+CARE governance + telemetry + validation gates  

---

## 📁 Directory Layout (Authoritative)

~~~~~text
KansasFrontierMatrix/
├── src/
│   ├── ai/                     # AI models, Focus Mode, explainability
│   ├── api/                    # FastAPI / GraphQL services
│   ├── graph/                  # Neo4j schema, queries, migrations
│   ├── pipelines/              # ETL, ingestion, validation
│   └── ARCHITECTURE.md         # Source system architecture
│
├── data/
│   ├── raw/                    # Unaltered sources
│   ├── work/                   # tmp + staging + work/processed
│   ├── processed/              # Published datasets
│   ├── stac/                   # STAC Collections & Items
│   ├── contracts/              # Data contracts (JSON)
│   └── ARCHITECTURE.md         # Data architecture spec
│
├── docs/
│   ├── standards/              # Markdown rules, FAIR+CARE, governance
│   ├── analyses/               # Domain-specific analyses
│   ├── reports/                # Validation, audit, telemetry
│   ├── guides/                 # Guides (data governance, self-validation, FAIR)
│   ├── accessibility/          # A11y standards & patterns
│   ├── governance/             # Governance docs (if present)
│   └── MASTER_GUIDE_v10.md     # This master guide
│
├── web/
│   ├── public/                 # Static assets
│   ├── src/                    # React + MapLibre + Cesium client
│   └── README.md
│
├── .github/
│   ├── workflows/              # CI/CD workflows
│   └── README.md               # CI/automation overview
│
├── releases/                   # Manifests, SBOMs, telemetry per version
└── Makefile
~~~~~

---

## 🧩 System Overview

~~~~~mermaid
flowchart TD
  A["Raw Data Sources"] --> B["ETL Pipelines"]
  B --> C["Validation & Self-Validation Gates"]
  C --> D["Data Work / Processed Layers"]
  D --> E["STAC/DCAT Metadata Layer"]
  E --> F["Neo4j Knowledge Graph"]
  F --> G["API Layer (FastAPI / GraphQL)"]
  G --> H["Web Client (React · MapLibre · Cesium)"]
  H --> I["Focus Mode AI Engine"]
  I --> F
~~~~~

---

## 🗺️ Data Architecture

### 3.1 Raw → Processed Pipeline

- `data/raw/` — untouched source files (NOAA, USGS, KHS, etc.)  
- `data/work/` — normalization, cleaning, staging, AI validation  
- `data/processed/` — final, certified tables/GeoJSON/Parquet/COG  
- `data/stac/` — STAC Collections & Items describing assets  
- `data/archive/` — immutable historical releases & manifests  

### 3.2 Dataset Families

- **Hydrology:** USGS NWIS, NHD, WBD, streamflow  
- **Climate:** NOAA, PRISM, Daymet, drought indices  
- **Hazards:** storms, floods, fires, tornadoes, disasters  
- **Land Cover & Terrain:** NLCD, LiDAR, elevation models  
- **Agriculture & Demography:** crops, census, land use  
- **Treaties & Land:** Royce polygons, BLM patents, deeds, homesteads  
- **Archaeology & History:** sites, surveys, diaries, newspapers  
- **Ecology & Biodiversity:** wildlife, insects, pests, eBird/GBIF  

---

## 🏗️ ETL Pipelines

Each ETL pipeline:

- Emits OpenTelemetry traces (run_id, dataset_id, rows, etc.)  
- Uses structured logging (Loki-compatible)  
- Produces Prometheus metrics (rows processed, failures, latencies)  
- Runs **self-validation** (schema + FAIR+CARE + checksums)  
- Blocks writes on validation failure (gated ETL)  
- Stamps provenance (lineage, source refs, timestamps)

### ETL Lifecycle

1. **Fetch** — download / query external APIs or archives  
2. **Normalize** — clean, reshape, unit/CRS conversions  
3. **Geoprocess** — reproject, clip, derive, union/diff  
4. **Temporal Alignment** — OWL-Time-based intervals  
5. **Validation** — schema, FAIR+CARE, checksum, AI audits  
6. **STAC Indexing** — create/update STAC Items/Collections  
7. **Graph Hydration** — load key entities and relations into Neo4j  

---

## 📦 Metadata Governance (STAC + DCAT + FAIR+CARE)

### 5.1 STAC

Each geospatial asset is described by a STAC Item with:

- `geometry`, `bbox`, `datetime`/temporal range  
- `assets` (COGs, GeoJSON, Parquet, NetCDF, docs)  
- `links` (collections, related, derived-from)  
- KFM properties:
  - `kfm:provenance`  
  - `kfm:ethics` (care_label, sensitivity, sovereignty_notes)  
  - `kfm:lineage` (source_ids, pipeline_ids)  

### 5.2 DCAT

Each dataset → DCAT Dataset with:

- `dct:title`, `dct:description`  
- `dct:creator`, `dct:license`  
- `dct:temporal`, `dct:spatial`  
- `dcat:distribution` with STAC asset links  

FAIR+CARE metadata is enforced by `faircare-validate.yml`.

---

## 🧠 Neo4j Knowledge Graph (CIDOC CRM + GeoSPARQL + OWL-Time)

### 6.1 Major Classes

- **CIDOC CRM**  
  - `E53 Place`, `E4 Period`, `E5 Event`, `E7 Activity`  
  - `E52 Time-Span`, `E18 Physical Thing`, `E28 Conceptual Object`  

- **KFM Extensions**  
  - `KFM:HydrologicalUnit`  
  - `KFM:ClimateBoundary`  
  - `KFM:TreatyBoundary`  
  - `KFM:HistoricalActor`  
  - `KFM:EcologicalIndicator`  
  - `KFM:DocumentReference`

### 6.2 Example Relations

- `(Person)-[:ATTENDED]->(Event)`  
- `(Event)-[:LOCATED_AT]->(Place)`  
- `(Document)-[:MENTIONS]->(Place|Event|Person)`  
- `(Dataset)-[:COVERS]->(Place)`  
- `(StoryNode)-[:NARRATES]->(Event|Place|Person)`  

---

## 🔌 API Layer (FastAPI / GraphQL)

Key endpoints (representative):

- `/stac/*` — STAC browsing and search  
- `/graph/query` — graph queries (Cypher-based)  
- `/timeseries/*` — climate, hydrology, hazards time series  
- `/layers/*` — map layers and metadata  
- `/focus/ask` — natural-language Focus Mode queries  
- `/focus/embeddings` — embedding search + similarity  
- `/focus/narrative` — AI narrative generation  

AuthN/AuthZ: OAuth2/OIDC + RBAC for sensitive content.

---

## 🌐 Web Client (React + MapLibre + Cesium)

### 8.1 Primary UX Features

- Multi-year **timeline** with dynamic filters  
- 2D (MapLibre) + 3D (Cesium) visualization  
- Layer browser + feature inspector  
- Focus Mode sidebar + Story Node cards  
- Keyboard-accessible, WCAG 2.1 AA-compliant UI  

### 8.2 UI Structure

- `components/` — Map, Timeline, Panels, Legends  
- `hooks/` — data fetching, caching, state sync  
- `state/` — global app state (e.g., Zustand or Redux)  
- `assets/` — icons, sprites, color tokens  

---

## 🔥 Focus Mode AI Engine

### 9.1 Inputs

- Neo4j graph nodes  
- STAC/DCAT metadata  
- Full-text archives (diaries, news, reports)  
- Time series & raster summaries  

### 9.2 Capabilities

- Entity-centric Q&A  
- Narrative synthesis across datasets  
- Spatial–temporal reasoning  
- NER, linking, summarization  
- Multi-dataset correlation & hypothesis surfacing  
- Explainability (SHAP overlays, rationale traces)  

---

## 🎛️ Telemetry, Observability, Alerts

### OpenTelemetry

Each ETL/Focus/API call emits traces with:

- `run_id`, `dataset_id`, `span_id`, `latency_ms`  
- `validator_pass`, `rows_processed`, `bytes_processed`  

### Metrics (Prometheus)

- `etl_rows_processed_total`  
- `etl_failures_total`  
- `web_request_latency_ms`  
- `focus_tokens_used_total`  

### Logging (Loki)

- Structured JSON logs, correlated via `run_id`  

### Alerts

- High error rate  
- Validator failures  
- Performance regressions  
- Security anomalies  

---

## 🧪 Data Validation (Self-Validation + Great Expectations)

Validation stack:

- Self-validation gates (schema + FAIR+CARE + checksum)  
- Great Expectations-like suites for:
  - schema  
  - spatial validity  
  - temporal validity  
  - value ranges  
  - missingness  
  - entity consistency  

**If validation fails → downstream writes are blocked.**

---

## 🔒 Security & Privacy

- Signed manifests + SBOM for every release  
- SLSA provenance for critical workflows  
- API key rotation policies  
- PII scrubbing on ingest  
- Read-only graph for public views  
- Network isolation for heavy ETL workloads  

---

## 🔄 Versioning & Releases

### Semantic Versioning

- **MAJOR** — architectural or ontology-breaking changes  
- **MINOR** — new features, analyses, or datasets  
- **PATCH** — bug fixes / minor improvements  

### Release Bundle Contents

- `manifest.zip` — asset listing + checksums  
- `sbom.spdx.json` — dependency SBOM  
- STAC root catalog snapshot  
- Graph snapshot (optional)  
- AI model fingerprints & metrics  
- `focus-telemetry.json` — telemetry & governance  

---

## 📈 Analyses & Workflows

Examples:

- **Hydrology:** drought–flood correlation, watershed change, flow anomalies  
- **Ecology:** species distributions, pest ranges, habitat fragmentation  
- **Historical:** treaty boundary evolution, settlement patterns, land tenure timelines  
- **Remote Sensing:** change detection, NDVI/NDMI trends, LiDAR terrain reconstruction  

Each analysis documents:

- Data sources  
- Methods  
- Validation & uncertainty  
- Story Nodes + visualizations  

---

## 🧱 Architecture Deep Dive

### 15.1 API ↔ Graph Interface

~~~~~mermaid
flowchart TD
  A["FastAPI Resolver"] --> B["Cypher Template Builder"]
  B --> C["Neo4j Driver"]
  C --> D["Graph Store"]
  D --> A
~~~~~

### 15.2 Focus Mode AI Feedback Loop

~~~~~mermaid
flowchart TD
  A["User Query"] --> B["Embedding Search"]
  B --> C["Graph Lookup"]
  C --> D["Context Synthesis"]
  D --> E["LLM Narrative"]
  E --> F["UI Story Nodes"]
  F --> A
~~~~~

---

## 📚 MCP-DL v6.3 Compliance

The Master Coder Protocol requires:

- Mandatory YAML front-matter for all docs  
- One-box Markdown outputs, validated structure  
- Standardized directory layout sections  
- Correct Mermaid usage (flowchart LR/TD, quoted labels)  
- Telemetry references and governance links  
- CI-enforced Markdown rules (`docs-lint.yml`)  

This master guide is the reference for MCP-DL compliance decisions.

---

## 🧰 Development Standards

### Commits

- `feat:`, `fix:`, `docs:`, `chore:`, `data:`, `graph:`, `ci:`, `security:`  

### Branching

- `feature/*`, `analysis/*`, `dataset/*`, `fix/*`  

### PR Requirements

- Documentation updated  
- Data contracts present & validated  
- CI/validation green  
- Governance checklist completed  

---

## 🚀 v10 Core Principles

- **Everything is temporal**  
- **Everything is spatial**  
- **Everything has provenance**  
- **Everything is queryable**  
- **Everything is FAIR+CARE**  
- **Everything is validated**  
- **Everything is observable**  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | KFM Core Team | Master guide aligned to v10.3; diagrams fixed; telemetry & governance references updated. |
| v10.2.2 | 2025-11-13 | KFM Core Team | Expanded architecture coverage; added Focus Mode and telemetry sections. |

---

<div align="center">

**Kansas Frontier Matrix — MASTER GUIDE v10**  
*Architecture · Data · AI · UX · Governance*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Docs Index](README.md) · [System Architecture](../src/ARCHITECTURE.md) · [Data Governance](guides/data-governance/README.md)

</div>
