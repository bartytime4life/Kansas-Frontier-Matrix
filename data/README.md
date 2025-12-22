---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
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
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:readme:v1.0.0"
semantic_document_id: "kfm-data-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# `data/` — KFM data directory

## 📘 Overview

### Purpose

The `data/` directory is the **canonical home for KFM datasets and pipeline artifacts**: immutable source snapshots, intermediate transforms, normalized “processed” outputs, and the machine-readable metadata that makes those outputs discoverable and auditable (STAC/DCAT/PROV, graph import fixtures).

This directory exists to support KFM’s canonical pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### What belongs here

- **Domain datasets** (organized per domain pack): raw / work / processed
- **Catalog outputs**:
  - STAC collections + items
  - DCAT dataset records
  - PROV lineage bundles
- **Graph ingest fixtures** (CSV + Cypher) used by loaders/migrations (generated from processed data)

### What does not belong here

- Source code (belongs under `src/`)
- API contracts (belongs under the API boundary)
- UI runtime assets/config (belongs under `web/`)
- Narrative Story Nodes (belongs under `docs/reports/story_nodes/`)

## 🗂️ Directory Layout

### This document

- `path`: `data/README.md` (must match front-matter)

### Target layout (v13+)

~~~text
📁 data/
├── 📄 README.md
│
├── 📁 <domain>/
│   ├── 📁 raw/                 # immutable source snapshots
│   ├── 📁 work/                # intermediate transforms (rerunnable)
│   └── 📁 processed/           # normalized outputs used downstream
│
├── 📁 stac/
│   ├── 📁 collections/         # STAC Collections (JSON)
│   └── 📁 items/               # STAC Items (JSON)
│
├── 📁 catalog/
│   └── 📁 dcat/                # DCAT Dataset records (JSON-LD / TTL as adopted)
│
├── 📁 prov/                    # PROV bundles (JSON-LD / TTL as adopted)
│
└── 📁 graph/
    ├── 📁 csv/                 # import-ready CSVs (nodes/edges/etc.)
    └── 📁 cypher/              # Cypher loaders/migrations (if used)
~~~

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/<domain>/raw/` | Immutable source snapshots | ETL ingest | ETL transforms (read-only) |
| `data/<domain>/work/` | Intermediate transforms (can be regenerated) | ETL | ETL, validation |
| `data/<domain>/processed/` | Normalized outputs for catalogs + graph ingest | ETL | Catalog build, graph build |
| `data/stac/**` | STAC Collections + Items | Catalog build | Graph, API, UI |
| `data/catalog/dcat/**` | DCAT dataset records | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles | ETL + catalog build | Audits, provenance graph, Focus Mode |
| `data/graph/**` | Import fixtures for Neo4j | Graph build | Neo4j loaders / migrations |

## 📦 Data & Metadata

### Data lifecycle

For each domain under `data/<domain>/`:

- `raw/` — immutable source snapshots
- `work/` — intermediate transforms
- `processed/` — normalized outputs used for catalogs and graph ingest

Global metadata outputs:

- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`
- Graph import: `data/graph/csv/` and `data/graph/cypher/`

### Domain expansion pattern

A “domain pack” is the minimum set required for a new domain to participate in the pipeline.

When adding a new domain:

1. Create `data/<domain>/raw/`, `data/<domain>/work/`, `data/<domain>/processed/`
2. Ensure the domain’s processed outputs can generate:
   - STAC Collection + Item(s)
   - DCAT dataset record(s)
   - PROV activity/bundle(s)
   - Graph import fixtures (if the domain is graph-ingested)
3. Add domain documentation under `docs/data/<domain>/` (canonical location may vary by repo; choose one and link it from here)

## 🌐 STAC, DCAT & PROV alignment

### Policy for every dataset

For each dataset or evidence product:

- STAC Collection + Item(s)
- DCAT mapping record
- PROV activity describing lineage
- Version lineage links reflected in catalogs and the graph

### Identifier and linkage expectations

- Graph nodes and APIs should reference:
  - STAC Item IDs
  - DCAT dataset ID
  - PROV activity ID

This ensures any UI view (including Focus Mode) can resolve “what is this data?” into a traceable lineage bundle.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**
- Story Nodes may reference local assets (images, excerpts) with attribution, but the **source-of-truth evidence** remains the catalog + provenance artifacts

### Focus Mode rule (non-negotiable)

Focus Mode must only consume **provenance-linked content**. Any predictive or AI-generated content must be clearly marked, opt-in, and include uncertainty metadata.

## 🧪 Validation & CI/CD

### Minimum checks (data-facing)

- STAC/DCAT/PROV artifacts validate against schemas in `schemas/`
- No orphan references (IDs cited by graph/API/UI resolve to catalog/provenance artifacts)
- Deterministic pipelines: reruns produce diffable, stable outputs
- Sensitivity/redaction rules are enforced at ingest and at API/story boundaries

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New external data sources
- New sensitive layers (protected locations / culturally sensitive knowledge)
- New AI narrative behaviors that could surface unsourced claims
- New public-facing endpoints that expose data directly

### Sovereignty safety

Any restricted locations or culturally sensitive knowledge must be protected by:

- geometry generalization where required,
- API-level redaction,
- Story Node asset review gates.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `data/` README (v12/v13-aligned) | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
