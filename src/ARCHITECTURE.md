---
title: "🏛️ Kansas Frontier Matrix — Architecture Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ARCHITECTURE.md"
version: "v11.0.0"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/architecture-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-architecture-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active · Enforced"
doc_kind: "Architecture"
intent: "system-architecture-overview"
semantic_document_id: "kfm-architecture-overview"
doc_uuid: "urn:kfm:src:architecture:overview:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I2-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
---

<div align="center">

# 🏛️ **Kansas Frontier Matrix — Architecture Overview (v11 LTS · Diamond⁹ Ω / Crown∞Ω)**  
`src/ARCHITECTURE.md`

**Purpose**  
Define the canonical **system architecture** of the Kansas Frontier Matrix (KFM) v11, including data/AI pipelines, Neo4j knowledge graph schema, STAC/DCAT catalogs, Story Nodes v3, Focus Mode v3, governance, and multi-cloud deployment.  
This is the **developer source of truth** for implementing, extending, and governing KFM.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Ultimate-orange)](../docs/standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📖 1. High-Level Overview

The **Kansas Frontier Matrix (KFM)** is an open-source semantic geospatial-historical platform fusing Kansas’s historical, cultural, and environmental data into an interactive **map + timeline + knowledge graph + narrative** experience.

The v11 architecture is:

- **Layered:**  
  `data → ETL/AI pipelines → Neo4j graph → APIs → web UI → Story Nodes & Focus Mode`
- **Semantic:**  
  aligned with **CIDOC-CRM**, **OWL-Time**, **GeoSPARQL**, **schema.org**, **STAC 1.x**, **DCAT 3.0**.
- **Ethical:**  
  governed by **MCP-DL v6.3** (documentation-first) and **FAIR+CARE** (data & AI ethics) with sovereignty controls.
- **Reliable:**  
  implements **Reliable Pipelines v11** (WAL · Retry · Rollback · Idempotency · Advisory Locks).
- **Narrative-aware:**  
  treats **Story Nodes v3** and **Focus Mode v3** outputs as schema-linked, first-class graph entities.

**Goals**

1. Make all data (past, live, projected) **queryable in time and space**.  
2. Ensure every transformation and AI output is **reproducible, explainable, and provenance-rich**.  
3. Provide a **developer-friendly monorepo** with modular, integrated ETL/graph/API/web components.  
4. Enable **safe, explainable AI narratives** over the graph (Focus Mode v3 + Story Nodes v3).  

---

## 🗂️ 2. Repository Structure (v11)

```text
Kansas-Frontier-Matrix/
│
├── src/
│   ├── pipelines/            # ETL · AI · validation · governance · telemetry · remote-sensing · updater · utils
│   ├── graph/                # Neo4j schema · loaders · RDF/JSON-LD exporters
│   ├── server/               # FastAPI + GraphQL APIs
│   ├── theming/              # UI theming framework · design tokens integration
│   └── ARCHITECTURE.md       # This file
│
├── web/                      # React + MapLibre + Cesium frontend
├── data/                     # sources · raw · processed · stac · provenance · releases
├── docs/                     # standards · architecture · analyses · governance
├── schemas/                  # JSON/YAML schemas · STAC/DCAT · Story Nodes · telemetry
└── mcp/                      # MCP experiments · SOPs · model cards
```

---

## 🔄 3. Data Ingestion & Pipelines

All data flows through **Reliable Pipelines v11**, implemented on:

- **LangGraph v11 DAGs**  
- **Reliable Nodes** (WAL + Retry + Resume + Compensation)  
- **Idempotency keys + advisory locks**  
- **GE Checkpoints + OTel metrics**  
- **FAIR+CARE + sovereignty gates**

### 3.1 Data Layout

- `data/sources/` — JSON manifests describing external data sources (DCAT-like).  
- `data/raw/` — download workspace (not committed; DVC/LFS).  
- `data/processed/` — cleaned, harmonized outputs (COG · GeoJSON · Parquet · NetCDF).  
- `data/stac/` — STAC Catalog for all spatiotemporal assets.  
- `data/provenance/` — PROV-O + OpenLineage lineage bundles.  
- `data/releases/` — versioned bundles for public/archive use.

Each `data/sources/*.json` holds:

- `id`, `title`, `description`, `license` (SPDX-style)  
- `spatial` (bbox, CRS)  
- `temporal` (start/end, granularity)  
- `endpoint` (HTTP/STAC/etc.)  
- `outputs` (paths for processed artifacts)  

These manifests function as **data contracts** for ETL jobs.

---

### 3.2 Batch ETL

Batch ETL runs for historical/static datasets (NOAA archives, USGS, BLM, archives):

**Extract**

- HTTP/REST/STAC downloads  
- Retry & rate-limit logic  
- Checksum logging (sha256)  

**Transform**

- Tables → CSV/Parquet with consistent schema  
- Vectors → GeoJSON (EPSG:4326)  
- Rasters → COG GeoTIFF with overviews  
- NLP (OCR, NER, geoparsing) for text  
- Spatial/temporal normalization  

**Load**

- Artifacts → `data/processed/`  
- STAC Items/Collections → `data/stac/`  
- Neo4j graph nodes/edges via Cypher templates in `src/graph/`  

All batch pipelines are **idempotent** and **incremental**, keyed on natural identifiers.

---

### 3.3 Streaming ETL

Streaming ETL handles **near-real-time** feeds:

- River gauges, Mesonet metrics, hazard alerts…  
- Ingestion via streaming APIs, pub/sub, webhook fan-in.  
- Each event becomes:
  - a validated `Observation` node,  
  - a STAC Item (where appropriate),  
  - linked to `SensorStream`, `Place`, and relevant `Dataset`.

Streaming pipelines aim for **exactly-once** semantics where possible using:

- Idempotency keys  
- WAL + replay  
- Advisory locks for per-dataset serialization  

---

### 3.4 Predictive & Scenario ETL

Predictive ETL produces **future scenarios** (e.g. climate 2030–2100):

- Models output gridded projections / time series.  
- Each projection is STAC-published with:
  - scenario metadata (`rcp`, `ssp`),  
  - model version,  
  - uncertainty metrics.  

Predictive artifacts are clearly distinguished in:

- Metadata (`kfm:kind = "model-projection"`),  
- UI (styling and labels),  
- Focus Mode narrative (“projected”, “modeled”, etc.).

---

## 📊 4. Knowledge Graph & Ontology

KFM uses **Neo4j** as its knowledge graph store, with logical alignment to:

- **CIDOC-CRM** (cultural heritage)  
- **OWL-Time** (temporal)  
- **GeoSPARQL** (geospatial)  
- **DCAT / STAC** (datasets)  
- **schema.org** (web data)  

### 4.1 Core Node Types

- `Person` (`E21 Person`, `schema:Person`)  
- `Place` (`E53 Place`, `schema:Place`, `geo:Feature`)  
- `Event` (`E5 Event`, `schema:Event`)  
- `Document` (`E31 Document`, `schema:CreativeWork`)  
- `Dataset` (`dcat:Dataset` · STAC Collection)  
- `Observation` (time-stamped measurements)  
- `SensorStream` (observation series)  
- `StoryNode` (structured narrative)  

### 4.2 Core Relationships

- `(:Person)-[:ATTENDED]->(:Event)`  
- `(:Event)-[:OCCURRED_AT]->(:Place)`  
- `(:Document)-[:MENTIONS]->(:Place|:Person|:Event)`  
- `(:Dataset)-[:DESCRIBES]->(:Place|:Event|:Theme)`  
- `(:SensorStream)-[:LOCATED_AT]->(:Place)`  
- `(:SensorStream)-[:PRODUCED]->(:Observation)`  
- `(:Observation)-[:DERIVED_FROM]->(:Dataset)`  
- `(:StoryNode)-[:ABOUT]->(:Place|:Person|:Event|:Dataset)`  
- `(:StoryNode)-[:FOLLOWS]->(:StoryNode)`  

Graph schema and constraints are defined under `src/graph/` and enforced in CI via tests and optional graph checks.

---

## 📚 5. Story Nodes v3 — Narrative Layer

**Story Nodes v3** are structured JSON documents (see `schemas/story-node.schema.json`) that unify:

- Narrative text  
- Spatial footprints  
- Temporal intervals  
- Graph relations (links to places/events/people/datasets)  

Key fields:

- `id`, `type="story-node"`, `version`, `lang`  
- `title`, `summary`  
- `narrative` (body, format, alternates, media)  
- `spacetime` (geometry, bbox, CRS, place_labels, when{start,end,precision,original_label})  
- `relations` (`rel`, `target`, `role`)  
- Optional `stac` hints (relevant assets/collections)  

Story Nodes are:

- stored as JSON/JSON-LD,  
- represented as `(:StoryNode)` nodes in Neo4j,  
- linked via `:ABOUT`, `:FOLLOWS`, `:PART_OF`, etc.  

They support:

- map/timeline synchronization,  
- narrative sequencing,  
- Focus Mode integration,  
- FAIR+CARE & sovereignty gating for narrative content.

---

## 🧠 6. Focus Mode v3 — AI Context Engine

**Focus Mode v3** is the AI-powered lens for any entity in the graph.

Given an entity ID, Focus Mode:

1. Gathers a local subgraph (1–2 hops) and relevant Story Nodes, Documents, Observations, Datasets.  
2. Uses **Focus Transformer v3** (graph+text+metadata model) to generate:
   - a structured narrative,  
   - a list of related entities,  
   - reasoning/explainability signals.  
3. Returns **provenance-annotated** narrative: each sentence is traceably linked to underlying data.  
4. Applies **FAIR+CARE + sovereignty filters**:
   - redactions for sensitive content,  
   - careful language for historical trauma,  
   - no speculative genealogies or Indigenous-history invention.  

Focus Mode is implemented by:

- API endpoint(s) under `src/server/`  
- Graph queries under `src/graph/`  
- AI model integration under `src/pipelines/ai/`  

Explainability overlays:

- highlight which nodes/edges/documents had the most influence,  
- show SHAP/LIME-like contributions for context rankings.

---

## ☁️ 7. Deployment & Multi-Cloud

KFM v11 is deployable across:

- AWS, Azure, GCP, on-prem clusters, and hybrid configurations.  

Core services:

- Neo4j (single or multi-node cluster),  
- API (FastAPI/GraphQL),  
- Web (React SPA),  
- ETL/AI workers,  
- Storage (S3-compatible, Blob/GCS, or on-prem MinIO).  

Infra-as-code:

- Kubernetes/Helm or equivalent manifests,  
- CI pipelines to build/push images and validate deployments.

Reliability:

- WAL + idempotency + advisory locks = safe re-runs and rollbacks.  
- Telemetry (OTel) = observability across services.  
- SLOs and error budgets define gating rules for promotions.

---

## ⚖️ 8. Governance, MCP, FAIR+CARE, Sovereignty

Architecture is tied to:

- **MCP-DL v6.3** — documentation-first; experiments, SOPs, model cards.  
- **FAIR+CARE** — data/practice standards with Indigenous data sovereignty at the center.  
- **KFM-OP v11** — ontology alignment and rules.  
- **KFM-PDC v11** — data contracts for all pipeline inputs/outputs.  

All new components must:

- Provide documentation (README + diagrams)  
- Provide schema contracts  
- Integrate with provenance systems  
- Respect CARE & sovereignty policies  
- Emit telemetry for runtime & sustainability  

Governance failures **block release** in CI.

---

## 🕰️ 9. Version History (Architecture Overview)

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-24 | Upgraded to KFM-MDP v11; integrated Reliable Pipelines v11, Story Nodes v3, Focus v3, sovereignty, telemetry v11. |
| v10.4.0 | 2025-11-16 | v10.4.0 architecture; streaming ETL, Focus v2.5, Story Nodes, DCAT/STAC bridge.          |
| v10.3.x | 2025-11-14 | Deeper ETL + graph details; DCAT3 and provenance patterns.                               |
| v10.0.0 | 2025-09-01 | Major v10 restructure; predictive pipelines, Focus v2, 3D, STAC catalog baseline.        |
| ≤ v9.x  | 2023–2024  | Early designs; initial ETL/graph/visual stack; pre-MCP v6.3 and pre-FAIR+CARE formalization. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
**Diamond⁹ Ω / Crown∞Ω · FAIR+CARE · MCP-DL v6.3 · Sovereignty-Respectful · Provenance-First**  

[Back to Docs](../docs/README.md) · [Standards](../docs/standards/ROOT-STANDARDS.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>