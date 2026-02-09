# Kansas Frontier Matrix (KFM)

> **A provenance-first geospatial knowledge system for Kansas.**  
> KFM integrates maps, data, historical narratives, and AI-assisted analysis using a governed  
> **“pipeline → catalogs → databases → API → UI”** architecture so every map, story, and answer is traceable to sources.

[![CI](https://img.shields.io/badge/CI-passing-brightgreen)](#ci--quality-gates) <!-- replace with real badge -->
[![License](https://img.shields.io/badge/License-see%20LICENSE-blue)](#license)
[![Cite](https://img.shields.io/badge/Cite-CITATION.cff-informational)](#citation)

---

## Start here

### Canonical documentation (governed)

- **Master guide (architecture + governance source of truth):** `docs/MASTER_GUIDE_v13.md`
- **Markdown rules (governed docs standard):** `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- **AI assistance rules (governed usage + disclosure):** `docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md`
- **PR checklist (CI expectations + gates):** `docs/ci/checklists/PR_CHECKLIST.md`
- **Reference library (project reading + citations index):** `docs/reference/REFERENCE_LIBRARY.md`

> [!NOTE]
> If any path differs in this repo, update **either** the README **or** the Master Guide so there is one source of truth.

---

## What KFM is

KFM is designed as a **trustworthy, auditable geospatial + historical knowledge system**:

- **Pipeline-first:** raw sources are transformed deterministically into processed datasets.
- **Catalog-first:** every published dataset produces **STAC + DCAT + PROV** records before it becomes visible in the UI.
- **Governed delivery:** the UI and external clients access data **only through the API “trust membrane”** (never by querying databases directly).
- **Narratives as artifacts:** Story Nodes are versioned, machine-ingestible Markdown narratives with evidence linkages.
- **Focus Mode:** a read-only experience that presents Story Nodes with map/timeline context and only provenance-linked content.

### What KFM is not

- Not a “direct DB query” app: clients do not bypass the API layer.
- Not a free-form wiki: documentation and narratives are governed artifacts with templates, validation, and review gates.
- Not “best-effort provenance”: missing lineage/metadata fails closed.

---

## Core principles

### Provenance-first (“the map behind the map”)

Every user-facing output (layer, story, chart, AI answer) must be traceable to sources via catalogs and lineage logs.

### Deterministic truth path (fail-closed)

Data must flow through the canonical stages **with no shortcuts**:

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- plus catalog outputs: `data/stac/`, `data/catalog/dcat/`, `data/prov/`

If required metadata or provenance is missing, the item is not publishable.

### Trust membrane

> [!IMPORTANT]
> **Frontend (React/MapLibre) and external clients never access databases directly.**  
> **Backend core logic never bypasses repository interfaces to talk directly to storage.**  
> All access routes through governed contracts (API + policy checks).

### Contract-first interfaces

APIs, schemas, and templates are first-class versioned artifacts. Breaking changes require explicit versioning and compatibility review.

### FAIR + CARE

KFM aims to be **Findable, Accessible, Interoperable, Reusable** while also honoring **Collective Benefit, Authority to Control, Responsibility, Ethics**—especially for sensitive or sovereignty-relevant content.

---

## Architecture overview

KFM follows a **Clean Architecture** layering model:

| Layer | Responsibility | Examples |
|---|---|---|
| **Domain** | Pure entities & core concepts, no DB/UI code | `LandParcel`, `HistoricalEvent`, `StoryNode` |
| **Use Case / Service** | Business workflows, policies, orchestration | ingestion, validation, timeline generation |
| **Integration / Interface** | Ports + adapters (interfaces for storage/APIs) | repository interfaces, API presenters |
| **Infrastructure** | Concrete tech implementations | PostGIS, Neo4j, FastAPI, React/MapLibre, CI/CD |

---

## End-to-end system flow

```mermaid
flowchart LR
  subgraph Ingestion["📥 Ingestion & ETL"]
    raw["data/raw (immutable sources)"] --> work["data/work (intermediate)"]
    work --> processed["data/processed (final outputs)"]
    processed --> stac["data/stac (STAC collections/items)"]
    processed --> dcat["data/catalog/dcat (DCAT JSON-LD)"]
    processed --> prov["data/prov (W3C PROV lineage)"]
  end

  stac --> storage["Storage: PostGIS + Neo4j (+ optional search index)"]
  dcat --> storage
  prov --> storage

  storage --> api["FastAPI API (REST + optional GraphQL)"]
  api --> ui["React UI (MapLibre · optional Cesium)"]
  ui --> story["Story Nodes + Focus Mode"]