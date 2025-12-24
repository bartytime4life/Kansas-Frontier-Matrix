---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.1"
semantic_document_id: "kfm-data-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.1"
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

- Define the **canonical home for KFM datasets and pipeline artifacts**: immutable source snapshots, intermediate transforms, normalized “processed” outputs, and machine-readable metadata required for discovery, lineage, and audits (STAC/DCAT/PROV + graph import fixtures).
- Enforce KFM’s non-negotiable ordering by placement and linkage:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Domain datasets (raw/work/processed) and evidence products used downstream | Source code (`src/`) |
| Catalog outputs: STAC Collections/Items, DCAT dataset records, PROV bundles | UI runtime assets/config (`web/`) |
| Graph ingest fixtures (CSV/Cypher) generated from processed outputs | Story Nodes (`docs/reports/story_nodes/`) |
| Deterministic, diffable outputs and integrity rules (IDs resolve; no orphan refs) | API contracts (belongs at the API boundary) |

### Audience

- **Primary:** Data engineers and contributors running ETL/catalog builds and producing governed datasets.
- **Secondary:** Maintainers/reviewers validating catalogs and provenance; curators publishing Story Nodes and Focus Mode content.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **domain pack**, **evidence artifact**, **catalog**, **provenance**, **graph ingest fixture**, **deterministic pipeline**, **redaction**, **orphan reference**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline, ordering is non-negotiable |
| v13 layout guidance (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | Canonical roots + stage homes |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Structure + required checklists |
| Schema validation (STAC/DCAT/PROV) | `schemas/` | Data/Platform | Schemas are the source-of-truth validators *(presence not confirmed in repo)* |
| ETL + catalog pipelines | `src/pipelines/` | Data Eng | Deterministic transforms; outputs land under `data/**` |
| Graph build + ontology bindings | `src/graph/` | Graph Eng | Generates/consumes `data/graph/**` fixtures |
| API boundary | `src/server/` *(v13 target; not confirmed in repo)* | API Eng | UI never reads Neo4j directly |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Must cite catalog/provenance evidence |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Directory responsibilities + placement rules documented and consistent with Master Guide
- [ ] All “recommended” paths are marked when not confirmed in repo
- [ ] Validation expectations are actionable (can be turned into CI checks)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `data/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs, catalogs, provenance, graph fixtures |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders (write into `data/**`) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts consumed downstream |
| Graph | `src/graph/` + `data/graph/` | Ontology-governed ingest + import fixtures |
| API boundary | `src/server/` *(v13 target; not confirmed in repo)* | Contracts, redaction, query services |
| UI | `web/` | React/MapLibre UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Documentation | `docs/` | Governed designs, guides, standards, ADRs |
| Schemas | `schemas/` | JSON Schemas for validation *(presence not confirmed in repo)* |
| Tests | `tests/` | Unit/integration/contract/e2e tests *(layout not confirmed in repo)* |
| Tools | `tools/` | Validation/utilities *(presence not confirmed in repo)* |
| Releases | `releases/` | Manifests/SBOMs/signed bundles *(v13 target; not confirmed in repo)* |

### Expected file tree for this sub-area

> This is the **recommended v13+ structure**. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 data/
├── 📄 README.md
│
├── 📁 stac/
│   ├── 📁 collections/                  # STAC Collections (JSON)
│   └── 📁 items/                        # STAC Items (JSON)
│
├── 📁 catalog/
│   └── 📁 dcat/                         # DCAT outputs (JSON-LD / TTL as adopted)
│
├── 📁 prov/                             # PROV bundles (per run / per dataset)
│
├── 📁 graph/
│   ├── 📁 csv/                          # import-ready CSVs (nodes/edges/etc.)
│   └── 📁 cypher/                       # optional post-import scripts / migrations
│
└── 📁 <domain>/                         # Example: hydrology, air-quality, historical
    ├── 📁 raw/                          # immutable source snapshots
    ├── 📁 work/                         # intermediate transforms (rerunnable)
    ├── 📁 processed/                    # normalized outputs used downstream
    ├── 📁 mappings/                     # dataset → STAC/DCAT/PROV mapping docs (optional)
    └── 📄 README.md                     # domain README (required)
~~~

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/<domain>/raw/` | Immutable source snapshots (append-only; do not mutate in place) | ETL ingest | ETL transforms (read-only) |
| `data/<domain>/work/` | Intermediate transforms (can be regenerated) | ETL | ETL, validation |
| `data/<domain>/processed/` | Normalized outputs for catalogs + graph ingest | ETL | Catalog build, graph build, audits |
| `data/<domain>/mappings/` | Human-readable mapping docs (crosswalks, field notes) | Data/curation | Reviewers, maintainers |
| `data/stac/**` | STAC Collections + Items | Catalog build | Graph, API, UI |
| `data/catalog/dcat/**` | DCAT dataset records | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles | ETL + catalog build | Audits, provenance graph, Focus Mode |
| `data/graph/**` | Import fixtures for Neo4j | Graph build | Neo4j loaders / migrations |

## 📦 Data & Metadata

### Data lifecycle

For each domain under `data/<domain>/`:

- `raw/` — immutable source snapshots
- `work/` — intermediate transforms (rerunnable)
- `processed/` — normalized outputs used for catalogs and graph ingest

Global evidence artifacts:

- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/` *(or `docs/data/` in older guidance; location may vary — not confirmed in repo)*
- PROV: `data/prov/` *(prefer per-run or per-dataset bundles)*
- Graph import: `data/graph/csv/` and `data/graph/cypher/`

### Domain expansion pattern

A **domain pack** is the minimum set required for a new domain to participate in the pipeline.

When adding a new domain:

1. Create:
   - `data/<domain>/raw/`
   - `data/<domain>/work/`
   - `data/<domain>/processed/`
   - `data/<domain>/README.md`
2. Ensure processed outputs can generate:
   - STAC Collection + Item(s)
   - DCAT dataset record(s)
   - PROV activity/bundle(s)
   - Graph import fixtures (if the domain is graph-ingested)
3. Add mapping documentation in **one** canonical place:
   - `data/<domain>/mappings/` (recommended for crosswalks), or
   - `docs/data/<domain>/` (documentation-first) *(not confirmed in repo)*  
   Do **not** duplicate mapping source-of-truth across both.

## 🌐 STAC, DCAT & PROV alignment

### Policy for every dataset

For each dataset or evidence product that is used downstream:

- STAC Collection + Item(s)
- DCAT mapping record
- PROV activity describing lineage
- Version/lineage links reflected in catalogs and the graph

### Identifier and linkage expectations

- Graph nodes and APIs should reference (directly or indirectly):
  - STAC Item IDs
  - DCAT dataset IDs
  - PROV activity/bundle IDs

This ensures any UI view (including Focus Mode) can resolve “what is this data?” into a traceable lineage bundle.

## 🧩 Graph ingest fixtures

### What `data/graph/**` is for

`data/graph/**` contains **import-ready artifacts** generated from `data/<domain>/processed/**` and catalog evidence:

- `csv/`: nodes and relationships exported for Neo4j import
- `cypher/`: optional post-import scripts, constraints, and migrations (if used)

### Non-negotiable constraints

- Fixtures must use **stable IDs** that match catalog/provenance identifiers wherever applicable.
- Fixtures must not introduce “orphan facts” (entities without evidence IDs).
- UI must not read Neo4j directly; all graph access is through APIs.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**
- Story Nodes may reference local assets (images, excerpts) with attribution, but the **source-of-truth evidence** remains the catalog + provenance artifacts

### Focus Mode rule (non-negotiable)

Focus Mode must only consume **provenance-linked content**. Any predictive or AI-generated content must be clearly marked, opt-in, and include uncertainty metadata.

## 🧪 Validation & CI/CD

### Minimum checks (data-facing)

- STAC/DCAT/PROV artifacts validate against schemas in `schemas/` *(presence not confirmed in repo)*
- No orphan references:
  - IDs cited by graph/API/UI resolve to catalog/provenance artifacts
- Deterministic pipelines:
  - reruns produce diffable, stable outputs
- Sensitivity/redaction rules are enforced at ingest and at API/story boundaries

### Recommended integrity checks (if tooling exists)

- Broken-link checks for STAC `links[]` and external `assets.*.href`
- Asset-size budgets for externally linked assets (avoid committing large binaries to git)
- Classification propagation checks:
  - no output is “less restricted” than any input in its lineage

*(Exact commands/tooling not confirmed in repo.)*

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

## 🧭 Context

### Background

KFM’s ability to present maps, timelines, and narratives depends on **traceable evidence**. The `data/` directory establishes where evidence artifacts live so that catalogs, graph ingest, APIs, and UI can remain provenance-linked and auditable.

### Assumptions

- Catalog and provenance artifacts (STAC/DCAT/PROV) are treated as evidence products and are validated.
- Domain staging (`raw/`, `work/`, `processed/`) is structured to support deterministic reruns.
- Some canonical documents referenced in front-matter may exist but are not included here (**not confirmed in repo**).

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- AI transformations are limited to allowed operations listed in front-matter; prohibited transforms must not be introduced.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Is DCAT canonical home `data/catalog/dcat/` or `docs/data/` for this repo? | Maintainers | TBD |
| Do we require per-domain governance docs under `data/<domain>/governance/` or under `docs/data/<domain>/`? | Governance | TBD |
| What tooling is the canonical validator for STAC/DCAT/PROV in CI? | Data/Platform | TBD |

### Future extensions

- Add per-domain “freshness gates” and classification docs (if adopted) under a single canonical location.
- Add releases packaging under `releases/` (manifests/SBOMs/signed bundles) once v13 is adopted.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `data/` README (v12/v13-aligned draft) | TBD |
| v1.0.1 | 2025-12-24 | Align to Universal doc template sections; clarify v13 target tree + “not confirmed” markers; add Context/Diagrams/open questions | TBD |

---

Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`