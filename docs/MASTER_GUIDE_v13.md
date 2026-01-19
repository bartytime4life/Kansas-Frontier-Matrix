---
title: "📘 KFM Master Guide v13 — Kansas Frontier Matrix (Canonical System Guide)"
path: "docs/MASTER_GUIDE_v13.md"
version: "v13.0.1"
last_updated: "2026-01-19"
status: "active"
doc_kind: "Master Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
security_ref: "docs/governance/SECURITY.md"
contributing_ref: "CONTRIBUTING.md"
code_of_conduct_ref: "CODE_OF_CONDUCT.md"

# helpful cross-refs (recommended)
blueprint_ref: "docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md"
markdown_work_protocol_ref: "docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md"
library_manifest_ref: "docs/library/MANIFEST.yml"

fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
---

<a id="top"></a>

# 📘 KFM Master Guide v13 🧭🌾🗺️  
**Kansas Frontier Matrix (KFM)** is a provenance-first “living atlas of Kansas” — turning **maps, datasets, documents, and models** into an **auditable, queryable, mappable knowledge system** where citations and metadata are first-class (no black boxes).  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

![KFM](https://img.shields.io/badge/KFM-v13%20Master%20Guide-1f6feb)
![MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-8957e5)
![ONTO](https://img.shields.io/badge/KFM--ONTO-v4.1.0-6f42c1)
![Catalog](https://img.shields.io/badge/evidence%20spine-STAC%20%2B%20DCAT%20%2B%20PROV-0aa3a3)
![Governance](https://img.shields.io/badge/FAIR%2BCARE-governed-2ea043)
![Graph](https://img.shields.io/badge/knowledge--graph-Neo4j-00b894)
![Spatial](https://img.shields.io/badge/spatial-PostGIS-336791)
![API](https://img.shields.io/badge/APIs-REST%20%7C%20GraphQL-8250df)
![UI](https://img.shields.io/badge/UI-React%20%7C%20MapLibre%20%7C%20Cesium-f97316)
![Policy](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20Conftest-black)
![SupplyChain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20SLSA%20%2B%20Sigstore-111827)

> [!IMPORTANT]
> This file is the canonical **“Start Here”** for KFM’s architecture, workflows, standards, and golden paths.  
> If anything contradicts this guide, treat it as a governance event.

---

## 🧭 Quick Jump
- 🚀 [Start Here](#-start-here)
- 🔒 [Non‑Negotiables (KFM Rules)](#-nonnegotiables-kfm-rules)
- 🧱 [System Architecture](#-system-architecture)
- 🗂️ [Repository Map (v13)](#️-repository-map-v13)
- 🛰️ [The Evidence Spine (Pipeline)](#️-the-evidence-spine-pipeline)
- 📥 [Data Intake (Raw → Governed)](#-data-intake-raw--governed)
- 🧠 [Graph, Ontology, Semantics](#-graph-ontology-semantics)
- 🔌 [APIs & Contracts](#-apis--contracts)
- 🗺️ [UI & Story Nodes](#️-ui--story-nodes)
- 🤖 [Focus Mode (AI System)](#-focus-mode-ai-system)
- 🧑‍⚖️ [Governance, Ethics, Sovereignty](#️-governance-ethics-sovereignty)
- 🔐 [Security, Policy, Supply Chain](#-security-policy-supply-chain)
- ✅ [Validation & CI/CD](#-validation--cicd)
- 🧪 [Roadmap & Future Proposals](#-roadmap--future-proposals)
- 📚 [Reference Shelf (Project Library)](#-reference-shelf-project-library)
- 🧾 [Appendices (Checklists)](#-appendices-checklists)

---

## 🚀 Start Here

### ✅ What KFM is (in one breath)
KFM is an open-source geospatial + historical knowledge hub that publishes governed catalogs (**STAC/DCAT/PROV**), builds a **Neo4j knowledge graph**, and serves evidence via **contracted APIs** into a **map‑first UI** with narrative Story Nodes and an evidence‑bound AI assistant.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧬 The canonical ordering (non‑negotiable)
**ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → UI → Story Nodes → Focus Mode** (no leapfrogging).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧰 Golden Paths (pick your role)
<details>
<summary><b>🧑‍🔬 Data Contributor (first dataset → live layer)</b></summary>

1) 📚 Read governance + sensitivity policy (`docs/governance/*`)  
2) 📦 Add a small, bounded dataset (one county / one period)  
3) 🧾 Write a **data contract** (source, license, spatial/temporal extent, processing steps) — enforced by validators  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
4) 🛰️ Emit catalogs: **STAC Item/Collection + DCAT Dataset + PROV run** (linked together)  [oai_citation:4‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
5) ✅ Run validations (schemas, links, hashes, policy pack)  
6) 🕸️ Register graph nodes/edges (datasets/assets/activities)  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
7) 🗺️ Publish a layer (tiles / GeoJSON / PMTiles, depending on use)  
</details>

<details>
<summary><b>🎬 Story Author (story node → map narrative)</b></summary>

1) 🧾 Pick an evidence bundle (datasets + docs)  
2) 🧭 Define the “claim/question” + uncertainty statement  
3) 🗺️ Author Story Node linking map views + timeline + citations  
4) ✅ Validate story schema + governance checks  
5) 🚢 Publish (Story Nodes are governed content, not blog posts)  
</details>

<details>
<summary><b>🧑‍💻 UI/Frontend (feature → provenance-visible UX)</b></summary>

1) 🗺️ Build on MapLibre (2D) + Cesium (3D), timeline, and narrative UI  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
2) ⛓️ Always surface provenance (“Layer Info” + proposed “Layer Provenance” panel)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
3) 📱 Keep mobile/offline in mind (PWA + offline packs)  [oai_citation:8‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
</details>

<details>
<summary><b>🤖 AI/Focus Mode (RAG → cited answers)</b></summary>

1) 🔎 Parse intent/entities → retrieve from Neo4j + search index → generate answer with citations → governance check  [oai_citation:9‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
2) 🧾 If it can’t be grounded in KFM evidence, it refuses or marks uncertainty  [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
3) 🛡️ Enforce policy at runtime (OPA allow/deny)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
</details>

---

## 🔒 Non‑Negotiables (KFM Rules)

> [!NOTE]
> These are engineering constraints (not “best practices”). They protect trust, provenance, and sovereignty.

1. ⛓ **No mystery layers** — unsourced/ad‑hoc data doesn’t enter the official catalog.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
2. 🧾 **Contract‑first** — every dataset has a metadata contract (source/license/spatiotemporal/steps) enforced by validators.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
3. 🛰️ **Catalog triplet required** — STAC + DCAT + PROV are the minimum publishable spine outputs.  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
4. 🧬 **Provenance never breaks** — exports, stories, and AI answers carry lineage forward.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
5. 🧑‍⚖️ **FAIR+CARE + sovereignty** — sensitive/cultural data is classified and handled with authority-to-control patterns.  [oai_citation:16‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
6. 🛡️ **Policy‑as‑code** — governance is machine‑enforced (OPA + Conftest), not vibes.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
7. 🔐 **Supply‑chain integrity** — SBOM + SLSA attestations + transparency logs for automated outputs.  [oai_citation:18‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
8. 🌱 **Sustainability is governed** — energy/carbon accountability can gate costly compute.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

## 🧱 System Architecture

KFM is designed in modular layers to integrate heterogeneous historical + geospatial data into a cohesive research tool.  [oai_citation:20‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### 🧩 Layers (conceptual)
- 🧠 **Domain**: Places, Events, Datasets, Observations, Story Nodes
- 🧪 **Services**: ingest → validate → catalog → graph → publish → narrate
- 🔌 **Adapters**: contracts ↔ domain, PostGIS, Neo4j, search index
- 🏗️ **Infra**: object storage, tile serving, CI/CD, policy engine

### 🗺️ Why two “truth stores”?
- 🗺️ **PostGIS** for spatial query + tiles + heavy geometry ops  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🕸️ **Neo4j** for semantic relationships, narrative traversal, and multi-hop context for retrieval  [oai_citation:22‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

## 🗂️ Repository Map (v13)

> v13 standardizes where subsystems live (one canonical home each) and reorganizes Story Nodes under governed paths.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

```text
🏠 Kansas-Frontier-Matrix/
├─ 📁 data/                         # raw/work/processed + catalogs (STAC/DCAT/PROV)
│  ├─ 📁 raw/                       # immutable drops (append-only)
│  ├─ 📁 work/                      # scratch + sims + staging (governed by policy)
│  ├─ 📁 processed/                 # normalized outputs (GeoParquet/COG/etc.)
│  ├─ 📁 catalog/                   # materialized STAC/DCAT/PROV outputs
│  └─ 📁 graph/                     # CSV imports / snapshots for Neo4j
│
├─ 📁 docs/                         # governed docs (this file lives here)
│  ├─ 📁 architecture/              # blueprints, ADRs
│  ├─ 📁 governance/                # FAIR+CARE, ethics, sovereignty, security
│  ├─ 📁 reports/story_nodes/        # narrative content (draft vs published)
│  └─ 📁 library/                   # reference manifest(s) for project shelf
│
├─ 📁 schemas/                      # JSON Schemas for catalogs, story nodes, UI config, telemetry
├─ 📁 src/
│  ├─ 📁 server/                    # API service implementation + contracts boundary
│  ├─ 📁 pipelines/                 # ETL/model runs (idempotent)
│  └─ 📁 graph/                     # ontology bindings + ingest tooling
│
├─ 📁 web/                          # React UI (MapLibre + Cesium), Focus Mode UI
├─ 📁 tools/                        # validators, policy pack, schema lints
├─ 📁 mcp/                          # experiments, eval logs, model cards
├─ 📁 tests/                        # unit/integration/e2e
└─ 📁 .github/                      # workflows, security gates
```

---

## 🛰️ The Evidence Spine (Pipeline)

### 🧬 “Spine” diagram
```mermaid
flowchart LR
  A[📥 ETL / Ingest] --> B[🛰️ STAC Items & Collections]
  A --> C[🗂️ DCAT Datasets]
  A --> D[🧬 PROV Runs]
  B --> E[🕸️ Neo4j Graph Build]
  C --> E
  D --> E
  E --> F[🔌 APIs (REST/OpenAPI + GraphQL)]
  F --> G[🗺️ UI (Map Explorer + Timeline + Stories)]
  G --> H[🤖 Focus Mode (Cited RAG Answers)]
```

### 📦 The catalog triplet (minimum publishable output)
KFM links STAC/DCAT/PROV so discovery metadata, technical asset metadata, and lineage travel together.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

- 🛰️ **STAC** answers “what/where/when/files?”  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🗂️ **DCAT** answers “publisher/license/access/citation?”  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🧬 **PROV** answers “how produced, from what inputs, by whom/what agent?”  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

## 📥 Data Intake (Raw → Governed)

### 🧠 Intake philosophy
Data intake is “provenance-first”: every piece of data enters with where it came from, how it was obtained, and how it can be reproduced.  [oai_citation:28‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🧾 Data contracts (contract-first)
Every dataset has an associated metadata JSON (“data contract”) with required fields (source/license/spatiotemporal/processing steps) enforced by validators.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

**Example contract shape (illustrative):**
- `id`, `title`, `description`
- `license`
- `spatial` (bbox, CRS)
- `temporal` (start/end)
- `provenance` (source URL, creator/issued, processing steps)
- `faircare` (collective benefit, authority-to-control, responsibility, ethics)  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🔁 Streaming/real-time fits the same spine
KFM treats streaming as many small datasets over time, still requiring provenance and classification enforcement.  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

Concrete example: river gauge data is queried from PostGIS, displayed in UI with source attribution from DCAT, and Focus Mode logs the specific reading used in PROV.  [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### ♻️ Rollback & incident response
Because data changes flow through Git and catalog outputs, reversions can undo ingestion; sensitive-data incidents require rapid classification flip + removal + post-mortem + new policy rules.  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 🧠 Graph, Ontology, Semantics

### 🕸️ Why Neo4j matters
The graph stores relationships across people↔places↔events↔datasets, enabling semantic traversal and multi-hop retrieval.  [oai_citation:34‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧭 Ontology alignment (directional)
Focus Mode and graph modeling reference established ontologies (e.g., CIDOC‑CRM for history, OWL‑Time for temporal data) for consistent semantics.  [oai_citation:35‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧹 Graph QA + anti-hallucination boundary
If something isn’t in the graph/docs, Focus Mode can be constrained to refuse rather than fabricate, reducing hallucination risk.  [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

---

## 🔌 APIs & Contracts

### 🔒 Contracted boundary
KFM separates UI/back-end via well-defined REST + GraphQL endpoints, letting the UI evolve without altering core data logic.  [oai_citation:37‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

### 🧱 PostGIS outbound patterns
PostGIS powers interactive maps (filters, bounding boxes, tiles, aggregates); vector tiles can be served using SQL templates (e.g., `ST_AsMVT`) behind API endpoints.  [oai_citation:38‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 🗺️ UI & Story Nodes

### 🖥️ UI pillars
KFM’s UI combines 2D/3D maps, timeline navigation, story narratives, and AI assistance in one cohesive platform.  [oai_citation:39‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

**Core UI modules (high level):**
- 🗺️ 2D Map Viewer + 🧊 3D Globe/Terrain (MapLibre + Cesium)
- ⏳ Timeline & temporal navigation
- 🎬 Story Nodes (interactive narratives)
- 🔎 Search & discovery, layer management, popups
- 🤖 Focus Mode with citations + explainability
- 🤝 Collaboration features, mobile + offline, AR extensions  [oai_citation:40‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

### ⛓️ “Map behind the map” (provenance UX)
Users can inspect layer provenance via Layer Info (source/license/how prepared), with a proposed Layer Provenance panel listing active layers and citations.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 📱 Offline + PWA direction
A PWA approach enables installable behavior and offline caching; offline “packs” bundle tiles + stories for field/museum/classroom use.  [oai_citation:42‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🧠 Community & collaboration (UI and beyond)
KFM plans in-UI annotations/comments, contribution pathways, and community quality signals (upvotes/flags) to support a living atlas.  [oai_citation:44‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

---

## 🤖 Focus Mode (AI System)

### 🧠 How Focus Mode works (traceable RAG)
Focus Mode follows a strict pipeline: parse → retrieve → generate (with embedded citations) → governance check → deliver with sources.  [oai_citation:45‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧾 Must-cite + must-refuse
Every AI answer includes citations to specific datasets/docs/entities; if it can’t be derived, it refuses or signals uncertainty.  [oai_citation:46‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🔎 Retrieval mechanisms
Hybrid retrieval draws from:
- full-text/semantic search index for documents  [oai_citation:47‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- Neo4j graph queries for linked context  [oai_citation:48‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- PostGIS for spatial/time-based queries (fast indices)  [oai_citation:49‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧭 Explainability & audit surfaces
Focus Mode includes explainability hooks (audit panel/attributions) and highlights governance flags (e.g., sensitive data notices).  [oai_citation:50‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 📓 Immutable governance ledger (AI)
KFM tracks AI outputs and compliance metadata in an append-only ledger for post-hoc auditing.  [oai_citation:51‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

## 🧑‍⚖️ Governance, Ethics, Sovereignty

### 🧭 FAIR+CARE is enforced, not optional
KFM enforces FAIR via mandatory metadata/provenance and respects CARE by designating sensitive data and requiring appropriate authority and review.  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🪶 Cultural protocols & differential access (directional)
Models like Mukurtu (TK labels/cultural protocols) inspire fine-grained access controls and context tagging for community-contributed or culturally sensitive materials.  [oai_citation:53‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 🗺️ Sensitivity-aware mapping (geo-obfuscation)
For vulnerable sites/species/cultural locations, KFM can generalize coordinates and gate access while preserving provenance.  [oai_citation:54‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

---

## 🔐 Security, Policy, Supply Chain

### 🧾 Policy Pack (OPA + Conftest)
Governance rules are encoded as versioned Rego policies and evaluated in CI; policies cover metadata requirements, sensitivity rules, citation coverage, and more.  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🛡️ Runtime policy enforcement
OPA can intercept runtime actions (e.g., allow/deny an AI answer or sensitive dataset access), and policies can be updated without redeploying the whole system.  [oai_citation:56‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧰 Supply-chain provenance
The Watcher → Planner → Executor pipeline ties into supply-chain integrity: SBOMs, SLSA attestations, and Sigstore transparency logging for automated PR outputs.  [oai_citation:57‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

### 🌱 Sustainability + compute governance
KFM tracks energy/carbon footprint and can require approval for expensive computations (governed compute).  [oai_citation:58‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

## ✅ Validation & CI/CD

### 🧪 CI ethos
CI blocks merges when checks fail; quality gates include tests, schema validation, policy checks, and security scanning.  [oai_citation:59‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🧠 Watcher → Planner → Executor (W‑P‑E)
Agents refuse to prepare or promote changes that violate FAIR/CARE or security policies; the Executor won’t promote a PR without proof of redaction/approval when sensitive content is involved.  [oai_citation:60‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

### ✅ What must be validated (minimum)
- 🧾 Contracts (dataset/story/ui schemas)
- 🛰️ STAC correctness + links
- 🗂️ DCAT fields (license, access URLs, identifiers)
- 🧬 PROV integrity (agents, activities, entities, hashes)
- 🔗 Cross-links across STAC ↔ DCAT ↔ PROV ↔ Graph
- 🛡️ Policy Pack (OPA/Conftest)

---

## 🧪 Roadmap & Future Proposals

> KFM v13 prioritizes **thin vertical slices** end-to-end (one dataset → catalogs → graph → API → UI → story → cited answers).  [oai_citation:61‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

### 🧭 Near-term (practical)
- 📄 Bulk document ingestion (OCR → entity extraction → graph linking)  [oai_citation:62‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 📱 PWA + offline data packs for field/classroom use  [oai_citation:63‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🧾 Layer provenance surfaces everywhere (layer info → provenance panel)  [oai_citation:64‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🌌 Medium/Long-term (frontier)
- 🧊 4D / temporal simulation + “digital twin” style exploration (time as a first-class dimension)  [oai_citation:65‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 📱 AR overlays for place-based Kansas history and environmental context  [oai_citation:66‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🤝 Crowdsourced verification systems (OSM-style QA + peer review)  [oai_citation:67‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧩 Citizen-science microtask consensus (Zooniverse-style multi-rater aggregation)  [oai_citation:68‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧠 “Query co-pilot” for natural language GIS questions (human-in-the-loop, evidence-based)  [oai_citation:69‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

---

## 📚 Reference Shelf (Project Library)

> This shelf lists the **project’s internal reference documents** (design, architecture, guides, compendiums).  
> Some items are PDF portfolios and must be opened in a compatible PDF viewer to access their embedded documents.  [oai_citation:70‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)

### 🧭 Core KFM system docs
- 📘 **Comprehensive Technical Documentation** — mission, principles, “no black box” ethos  [oai_citation:71‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 🧱 **Comprehensive Architecture, Features, and Design** — UI transparency, offline packs, governance summary  [oai_citation:72‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:73‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 📥 **Data Intake – Technical & Design Guide** — STAC/DCAT/PROV integration + streaming examples  [oai_citation:74‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:75‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🗺️ **Comprehensive UI System Overview** — UI modules, offline/AR/collaboration roadmap  [oai_citation:76‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🤖 **AI System Overview** — RAG flow, governance checks, citations, OPA runtime hooks  [oai_citation:77‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:78‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🌟 **Latest Ideas & Future Proposals** — W‑P‑E governance + supply chain attestation direction  [oai_citation:79‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

### 🧾 Docs & Markdown standards
- 🧾 **MARKDOWN_GUIDE_v13** — canonical pipeline ordering + v13 directory layout + doc DoD  [oai_citation:80‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- ✍️ **Comprehensive Markdown Guide (docx)** — Mermaid + Math + collapsible sections patterns  [oai_citation:81‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  

### 🧠 Innovation & community patterns
- 💡 **Innovative Concepts to Evolve KFM** — 4D twins, AR storytelling, crowdsourced QA, cultural protocols  [oai_citation:82‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:83‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:84‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 🧰 Compendium portfolios (embedded libraries)
- 🧠 **AI Concepts & more** (PDF portfolio)  [oai_citation:85‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- 🗺️ **Maps / GoogleMaps / Virtual Worlds / Archaeology / WebGL** (PDF portfolio)  [oai_citation:86‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🧑‍💻 **Various Programming Languages & Resources** (PDF portfolio)  [oai_citation:87‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- 🗄️ **Data Management / Architectures / Bayesian Methods / Ideas** (PDF portfolio)  [oai_citation:88‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  

### 📚 Extra supporting references already in-repo
- 🧭 **Open-Source Geospatial Historical Mapping Hub Design** (architecture concept)  [oai_citation:89‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
- 🧼 **Data Mining Concepts & Applications** (data quality + cleansing framing)  [oai_citation:90‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- 🐍 **Python Geospatial Analysis Cookbook** (practical GIS recipes + PostGIS patterns)  [oai_citation:91‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  

---

## 🧾 Appendices (Checklists)

### 🧾 Appendix A — Dataset Promotion Checklist ✅
- [ ] 📥 Source captured (manifest + license + access notes)
- [ ] 🔒 Sensitivity classified (public/internal/restricted)
- [ ] 🧾 Data contract completed + validated  [oai_citation:92‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- [ ] 🧹 Normalized to standard format (GeoParquet/COG/etc.)
- [ ] 🛰️ STAC Item/Collection created + linked
- [ ] 🗂️ DCAT Dataset created (publisher/license/access URLs)
- [ ] 🧬 PROV run created (inputs/code version/params/outputs)
- [ ] ✅ Validation passes (schemas + link checks + hashes + policy pack)
- [ ] 🕸️ Graph registered (nodes + relationships)
- [ ] 🗺️ UI layer published (tiles + styling)
- [ ] 🎬 Story Node optional (curated narrative + uncertainty + citations)

### 🎬 Appendix B — Story Node Checklist
- [ ] 🎯 Clear claim/question
- [ ] 🧾 Evidence list (datasets + documents)
- [ ] 🗺️ Map views defined (camera, layers, filters, timeline)
- [ ] 🧬 Provenance links included
- [ ] ⚠️ Uncertainty stated
- [ ] 🧑‍⚖️ Governance checks (sensitivity + sovereignty)
- [ ] ✅ Validate story schema + links

### 🤖 Appendix C — Focus Mode Answer Checklist
- [ ] 🔎 Retrieval logged (what sources were used)
- [ ] 🧾 All factual claims have citations  [oai_citation:93‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- [ ] 🛡️ Governance/policy check passed (OPA allow/deny)  [oai_citation:94‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- [ ] 🧬 PROV/ledger record written (answer + source set)  [oai_citation:95‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- [ ] ⚠️ Uncertainty is explicit where evidence is weak

### 🧾 Appendix D — Doc “Definition of Done” (for governed docs)
- [ ] Front-matter complete + valid
- [ ] Claims link to datasets/schemas/source references where applicable
- [ ] Validation steps listed and repeatable
- [ ] Governance/FAIR+CARE/sovereignty considerations stated  [oai_citation:96‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

---

## 🔗 Footer Navigation
- ⬆️ Back to Top: [↑](#top)
- 🧑‍⚖️ Governance Root: `docs/governance/ROOT_GOVERNANCE.md`
- 🤝 Contributing: `CONTRIBUTING.md`
- 🧾 Markdown Work Protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`