---
title: "Kansas Frontier Matrix — End-to-End Data & Metadata Pipeline"
path: "docs/architecture/kfm_end_to_end_pipeline_v0.1.0.md"
version: "v0.1.0-draft"
last_updated: "2025-12-05"
release_stage: "Draft / Proposed"
lifecycle: "Active"
status: "Draft"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
governance_ref: "docs/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
ci_workflow_ref: ".github/workflows/kfm-ci.yml"
story_node_ready: true
focus_mode_ready: true
---

# Kansas Frontier Matrix — End-to-End Data & Metadata Pipeline v0.1.0

**Purpose:**  
Define the canonical end-to-end pipeline for KFM: **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode**, with clear module boundaries, metadata contracts, and CI/CD hooks. This document is the architecture backbone for how data moves from raw sources into interactive stories on the map.

---

## 📘 Overview

### 1. Scope

This document covers:

- Data and metadata flow from **external sources** into **KFM storage, catalogs, and graph**.  
- The contract between:
  - `src/pipelines/**` (ETL & enrichment),
  - `data/**` (raw → work → processed → stac),
  - `src/graph/**` (Neo4j models),
  - `src/api/**` (service layer), and
  - `src/web/**` (React + MapLibre/Cesium).  [oai_citation:0‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- Requirements for **STAC items**, **DCAT datasets**, and **PROV-O provenance** per stage.  [oai_citation:1‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  [oai_citation:2‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  [oai_citation:3‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- How Story Nodes and Focus Mode consume this pipeline.

### 2. Pipeline Summary (Conceptual)

1. **Deterministic ETL (config-driven):**  
   - Ingest raw files/feeds into `data/raw/**`.  
   - Transform & enrich into `data/work/**` and `data/processed/**`.  
   - All jobs are reproducible, seed-locked, and logged per MCP 2.0.  [oai_citation:4‡Master Coder Protocol 2.0.pdf](file-service://file-XjPWZrWdLTrVng7soAnSHp)  

2. **STAC/DCAT Catalog Layer:**  
   - For each geospatial or spatiotemporal asset, emit a **STAC Item** into `data/stac/items/**`.  [oai_citation:5‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
   - For each logical dataset (multi-asset), emit a **DCAT Dataset** description into `data/catalog/dcat/**`.  [oai_citation:6‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  

3. **Neo4j Knowledge Graph Layer:**  
   - Ingest STAC/DCAT/PROV into Neo4j as **Places, Events, Documents, Assets, Activities, Agents**.  
   - Use PROV-O and GeoSPARQL mappings for lineage and geometry.  [oai_citation:7‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  [oai_citation:8‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

4. **API Layer:**  
   - `src/api/**` exposes stable REST/GraphQL endpoints for map/timeline, Focus Mode, and Story Node queries.

5. **Frontend Layer:**  
   - `src/web/**` (React) + MapLibre + Cesium render:  
     - time-aware maps,  
     - Story Node overlays,  
     - Focus Mode entity panels.

6. **Story Nodes & Focus Mode:**  
   - Narrative chunks are generated from graph + docs, stored as Story Nodes, and surfaced in Focus Mode for interactive exploration.

### 3. Concrete Next Steps

Short-term backlog items:

- Scaffold baseline ETL pipeline config (`configs/pipelines/default_etl.yml`).  [oai_citation:9‡Comprehensive Guide to ETL Architecture, Open-Source Tools, and Best Practices.pdf](file-service://file-5sAQHp79veowmhbYy2iX5u)  
- Create initial STAC Collection + sample Items under `data/stac/collections/kansas-core.json`.  [oai_citation:10‡Implementing a Self-Hosted SpatioTemporal Asset Catalog (STAC) System.pdf](file-service://file-GxbDKAbMAJBhvkoENndVGa)  
- Implement first graph ingestion job (`src/graph/ingest/stac_to_neo4j.py`).  
- Expose `/v1/timeline` and `/v1/map/layers` in `src/api/`.  
- Wire a minimal “Story Node viewer” route in `src/web/` consuming `/v1/story_nodes`.

---

## 🗂️ Directory Layout

> **Goal:** Every artifact is findable via predictable paths and cataloged metadata.

**Core paths:**

| Path | Role |
| --- | --- |
| `data/sources/` | Source manifests (URLs, licenses, collection notes). |
| `data/raw/` | Immutable raw drops from external systems. |
| `data/work/` | Intermediate transforms, temp joins, QA outputs. |
| `data/processed/` | Ready-for-catalog datasets (clean, versioned). |
| `data/stac/collections/` | STAC Collection JSON files (dataset families). |
| `data/stac/items/` | STAC Item JSONs for individual assets/granules. |
| `data/catalog/dcat/` | DCAT Dataset/Distribution RDF (TTL/JSON-LD). |
| `data/prov/` | PROV-O provenance bundles for runs and datasets. |
| `src/pipelines/etl/` | ETL entrypoints & DAG definitions. |
| `src/pipelines/catalog/` | STAC/DCAT/PROV emitters & validators. |
| `src/graph/` | Neo4j schema, Cypher migrations, ingestion code. |
| `src/api/` | Public/internal API services (REST/GraphQL). |
| `src/web/` | React/MapLibre/Cesium frontend. |
| `docs/architecture/` | Architecture standards & diagrams (this doc). |
| `mcp/experiments/` | Reproducible experiments, model runs (MCP 2.0). |
| `.github/workflows/` | CI/CD pipelines (`kfm-ci`, docs-lint, lineage-audit).  [oai_citation:11‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

---

## 🧭 Context

- This document **extends** the public-facing Kansas Frontier Matrix overview by specifying how the pipeline is physically wired into the monorepo and metadata stack.  [oai_citation:12‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- It **reuses** patterns and datasets identified in the expansion documents (deep past, futures, archaeology) while standardizing how those data arrive and are cataloged.  [oai_citation:13‡Expanding the Kansas Frontier Matrix.pdf](file-service://file-HwRCT9vfxTnJzgqm6Tbg7s)  [oai_citation:14‡Expanding the Kansas Frontier Matrix: New Data Sources and Features.pdf](file-service://file-GS7S8zrZFtqkiW1ScN1cM3)  
- It is **governed by** KFM-MDP v11.2.4 for Markdown structure and by KFM-OP v11 for graph semantics.  [oai_citation:15‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

---

## 🧱 Architecture

### 1. Deterministic ETL Layer

**Modules & Paths**

- Code: `src/pipelines/etl/**`  
- Configs: `configs/pipelines/*.yml`  
- Data: `data/raw/**`, `data/work/**`, `data/processed/**`

**Requirements**

- All pipelines are **config-driven**, no hard-coded paths or secrets.  
- Seeds and parameters are recorded in:

  - `mcp/experiments/YYYY-MM-DD_PIPELINE-RUN-ID.md`  
  - `data/prov/run/<run-id>.ttl` (PROV-O bundle).

- ETL supports both batch and streaming where needed but must always log:

  - input datasets + versions,  
  - transforms applied,  
  - outputs and their IDs.

### 2. STAC Catalog Layer

**Modules & Paths**

- STAC generator: `src/pipelines/catalog/stac_emitter.py`  
- Storage: `data/stac/collections/**`, `data/stac/items/**`

**Key Rules**

- Each **spatiotemporal asset** (raster, vector, time series slice) becomes a STAC Item with:

  - `id`, `geometry`, `bbox`, `properties.datetime`,  
  - `assets.data.href` pointing into `data/processed` or external storage.  [oai_citation:16‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  

- Collections encode:

  - spatial/temporal extent of the dataset,  
  - license, providers, processing summaries.

- Validation:

  - All Items/Collections must pass `stac-validate` in CI before merge.  [oai_citation:17‡Implementing a Self-Hosted SpatioTemporal Asset Catalog (STAC) System.pdf](file-service://file-GxbDKAbMAJBhvkoENndVGa)  

### 3. DCAT Catalog Layer

**Modules & Paths**

- DCAT emitter: `src/pipelines/catalog/dcat_emitter.py`  
- RDF outputs: `data/catalog/dcat/**` (TTL or JSON-LD)

**Key Rules**

- Each logical dataset (e.g., “Kansas Homestead Land Patents 1862–1930”) is a **DCAT Dataset**.  [oai_citation:18‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- For each Dataset:

  - At least one **Distribution** (file or API endpoint) is defined.  
  - Dataset references its STAC Collections/Items via seeAlso / qualified relations.  
  - Versioning uses DCAT 3.0 terms (`dcat:hasVersion`, `dcat:previousVersion`) for releases.

### 4. Knowledge Graph Layer (Neo4j)

**Modules & Paths**

- Schema: `src/graph/schema/*.cypher`  
- Ingestion: `src/graph/ingest/{stac,dcat,prov}_to_neo4j.py`  
- Migrations: `src/graph/migrations/**`

**Modeling Highlights**

- Core node labels:

  - `Place`, `Event`, `Document`, `Person`, `Organization`,  
  - `Asset` (for STAC assets),  
  - `Dataset`, `Distribution`,  
  - `Activity`, `Agent` (from PROV-O).  [oai_citation:19‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- Relationships (examples):

  - `(Activity)-[:USED]->(Entity)`  
  - `(Entity)-[:WAS_GENERATED_BY]->(Activity)`  
  - `(Agent)-[:WAS_ASSOCIATED_WITH]->(Activity)`  
  - `(Place)-[:HAS_GEOMETRY]->(Geometry)` (GeoSPARQL alignment).  [oai_citation:20‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

- All STAC/DCAT/PROV entities must retain their original IDs for bidirectional traceability.

### 5. API Layer

**Modules & Paths**

- Service code: `src/api/**`  
- OpenAPI specs: `docs/api/*.yml`

**Baseline Endpoints**

- `/v1/timeline` — time-sliced events & datasets.  
- `/v1/map/layers` — layer catalog with STAC/DCAT references.  
- `/v1/story_nodes` — Story Nodes keyed by graph IDs, spatial & temporal extent.  
- `/v1/focus/{entity_id}` — Focus Mode context for a given node (Place/Event/Person).

APIs must never query Neo4j directly from the frontend; all access goes through this layer with documented contracts.

### 6. Frontend Layer

**Modules & Paths**

- React app: `src/web/app/**`  
- Map components: `src/web/components/map/**`  
- Story/Focus panels: `src/web/components/story/**`, `src/web/components/focus/**`

**Responsibilities**

- Resolve entities only through API contracts.  
- Use STAC & DCAT metadata to:

  - drive legend entries,  
  - show licensing & provenance on hover/click,  
  - animate time via timeline scrubber.

---

## 🗺️ Diagrams

> Diagrams are authoritative **only** when checked into `docs/architecture/diagrams/**` and referenced here.

Planned diagrams:

1. **High-Level Pipeline Flowchart**  
   - Shows: Source systems → ETL → STAC/DCAT/PROV → Neo4j → API → Web → Story Nodes.  
   - Stored at: `docs/architecture/diagrams/kfm_pipeline_overview.mmd`.

2. **Graph Schema Overview**  
   - Node labels & key relationships.  
   - Stored at: `docs/architecture/diagrams/kfm_graph_schema.mmd`.

3. **Catalog Integration Diagram**  
   - How STAC Items and DCAT Datasets map into the graph and APIs.

CI will run a diagram-check to ensure referenced `.mmd` files exist and render.

---

## 🧠 Story Node & Focus Mode Integration

**Story Node Contract**

Each Story Node must be representable as:

- `title`: short human-readable title.  
- `text`: 1–4 paragraphs, derived from graph + docs (no hallucinated facts).  
- `spatial_extent`: geometry or bbox (GeoJSON) matching a `Place` or asset.  
- `temporal_extent`: start/end timestamps (OWL-Time compatible).  
- `graph_links`: list of Neo4j IDs + relationship hints.

Story Node generation jobs live in:

- `src/pipelines/story_nodes/**` (batch generators),  
- `mcp/experiments/story_nodes/**` (experiments & evaluation).

Focus Mode uses:

- `/v1/focus/{entity_id}` for context,  
- `/v1/story_nodes?entity_id=...` for narrative overlays.

---

## 🧪 Validation & CI/CD

**CI Workflow:** `.github/workflows/kfm-ci.yml`  [oai_citation:21‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

Minimum checks for pipeline-related changes:

1. **Markdown & Schema Linting**

   - Validate this doc against KFM-MDP v11.2.4 JSON schema.  [oai_citation:22‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

2. **ETL Tests**

   - Unit tests in `src/pipelines/tests/**`.  
   - “Dry-run” ETL jobs on sample configs.

3. **Catalog Validation**

   - `stac-validate` for all modified Items/Collections.  [oai_citation:23‡Implementing a Self-Hosted SpatioTemporal Asset Catalog (STAC) System.pdf](file-service://file-GxbDKAbMAJBhvkoENndVGa)  
   - SHACL/SHEx validation for DCAT graph.  [oai_citation:24‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  

4. **Graph & API Tests**

   - Schema migration checks (Neo4j).  
   - API contract tests (OpenAPI-based).

5. **Lineage & Provenance Audit**

   - Ensure every new dataset has a PROV bundle in `data/prov/`.  [oai_citation:25‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

---

## 📦 Data & Metadata

**For every dataset/asset, we require:**

- Source manifest in `data/sources/*.yml`:

  - `source_uri`, `license`, `contact`, `collection_notes`.

- STAC Item(s) / Collection(s) when geospatial or temporal.  [oai_citation:26‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
- DCAT Dataset/Distribution when exposed via portal or API.  [oai_citation:27‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- PROV bundle describing:

  - which ETL run generated it,  
  - input datasets,  
  - responsible agents (people/services).  [oai_citation:28‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

All metadata must be FAIR: findable via catalogs, accessible via APIs, interoperable via standards, reusable via clear licensing.

---

## 🌐 STAC, DCAT & PROV Alignment

**Canonical mappings:**

- **STAC → Graph**

  - `Item.id` → `Asset.asset_id`  
  - `Item.geometry` → `Geometry` node with GeoSPARQL geometry literal.  [oai_citation:29‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
  - `Item.properties.datetime` → `Asset.datetime` + OWL-Time instant.  

- **DCAT → Graph**

  - `dcat:Dataset` → `Dataset` node.  [oai_citation:30‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
  - `dcat:Distribution` → `Distribution` node.  
  - `dcat:distribution` → `(:Dataset)-[:HAS_DISTRIBUTION]->(:Distribution)`  

- **PROV → Graph**

  - `prov:Entity` → `Entity`-subclass nodes (`Dataset`, `Asset`, `Document`).  
  - `prov:Activity` → `Activity` nodes connected via `:USED` and `:WAS_GENERATED_BY`.  
  - `prov:Agent` → `Agent` nodes (`Person`, `Organization`, `SoftwareAgent`).  [oai_citation:31‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

**Rule of thumb:**  
No STAC or DCAT object may enter the graph without a corresponding PROV Activity describing how it was produced.

---

## ⚖ FAIR+CARE & Governance

- All ingestion configs must record **license** and **rights**; no dataset enters `data/processed/` without explicit licensing metadata.  [oai_citation:32‡Comprehensive Open Data Sources and Tools for the Kansas Frontier-Matrix Project.pdf](file-service://file-TaFEKzoaANSnQHWuupWH38)  
- Indigenous and culturally sensitive data must be flagged via:

  - `sovereignty_policy` in front-matter (doc-level),  
  - dataset-level flags in `data/sources/*.yml`.

- Redactions must be explicit (“location generalized to county for cultural sensitivity”), not silent.  
- Governance references (must be kept up to date):

  - Root governance: `docs/governance/ROOT-GOVERNANCE.md`  
  - FAIR+CARE guidance: `docs/faircare/FAIRCARE-GUIDE.md`  
  - Indigenous data protection: `docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date | Author | Notes |
| --- | --- | --- | --- |
| v0.1.0-draft | 2025-12-05 | AI Lead Programmer (KFM) | Initial end-to-end pipeline architecture, aligned with KFM-MDP v11.2.4 and STAC/DCAT/PROV stack. |

---

**Governance & References**

- This document complies with **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2.4**.  [oai_citation:33‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- STAC integration based on **OGC STAC Community Standard — Complete Overview (for KFM Integration)**.  [oai_citation:34‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
- DCAT alignment based on **Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide**.  [oai_citation:35‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- Provenance alignment based on **Comprehensive Guide to W3C PROV-O**.  [oai_citation:36‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- Geo semantics aligned with **GeoSPARQL: Geospatial SPARQL for the Semantic Web**.  [oai_citation:37‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
