---
title: "Docs — Kansas Frontier Matrix Documentation Index"
path: "docs/README.md"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.1"
semantic_document_id: "kfm-docs-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.1"
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

# Docs — Kansas Frontier Matrix Documentation Index

## 📘 Overview

### Purpose

- Provide a single entry point for navigating `docs/` (the canonical governed documentation area).
- Point contributors to the correct templates/standards before adding or changing documentation.
- Keep documentation **architecture-synced** with the system pipeline:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

### Read-first order

1) `docs/MASTER_GUIDE_v12.md` (canonical pipeline, invariants, system inventory)  
2) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (draft design: canonical subsystem homes, CI gates, repo lint rules) *(planned; not confirmed in repo)*  
3) `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` (draft: end-to-end architecture & vision) *(planned; not confirmed in repo)*  
4) `docs/templates/` (Universal, Story Node, API Contract templates)  
5) `schemas/README.md` (contract schemas registry for catalogs, Story Nodes, UI registries, telemetry)

### Scope

| In Scope | Out of Scope |
|---|---|
| Where documentation lives and how it is organized | Full implementation details of pipelines, services, or UI |
| Which templates to use for docs (Universal, Story Node, API Contract) | Debugging runtime failures / operations runbooks |
| Docs-to-data linkage expectations (STAC/DCAT/PROV identifiers, provenance references) | Replacing the Master Guide or templates |

### Audience

- Primary: contributors authoring/maintaining documentation in `docs/`
- Secondary: engineers and reviewers working in ETL, catalogs, graph, API, UI, and story layers

### Definitions

- Link: `docs/glossary.md` *(planned in v13 target tree; not confirmed in repo)*
- Terms commonly used in docs:
  - STAC, DCAT, PROV-O
  - Neo4j graph
  - Story Nodes
  - Focus Mode
  - Contract tests (API/UI)
  - Deterministic ETL (idempotent, replayable)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical roots + CI gates (draft) *(not confirmed in repo)* |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | TBD | End-to-end architecture doc (draft) *(not confirmed in repo)* |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc template |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | For narratives + Focus Mode surfacing |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | For REST/GraphQL contract changes |
| Schemas registry | `schemas/README.md` | TBD | Contract schemas for catalogs, UI registries, Story Nodes, telemetry |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | TBD | *(planned; not confirmed in repo)* |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | TBD | *(planned; not confirmed in repo)* |
| STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | TBD | *(planned; not confirmed in repo)* |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | TBD | *(planned; not confirmed in repo)* |
| PROV profile | `docs/standards/KFM_PROV_PROFILE.md` | TBD | *(planned; not confirmed in repo)* |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | required reference for governed docs *(not confirmed in repo)* |
| Ethics policy | `docs/governance/ETHICS.md` | TBD | required reference for governed docs *(not confirmed in repo)* |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | required reference for governed docs *(not confirmed in repo)* |

### Project reference library

The following documents are part of the project’s working reference set. **They are not automatically assumed to be committed into the repo.** If you choose to vendor any of them into `docs/`, ensure licensing and size constraints are reviewed.

#### Architecture, scope, and expansion references

- *Kansas Frontier Matrix: System Structure and Scope* (PDF) *(recommended home: `docs/architecture/` — not confirmed in repo)*
- *Kansas Frontier Matrix (KFM) Implementation Guide* (PDF) *(recommended home: `docs/architecture/` — not confirmed in repo)*
- *Expanding the Kansas Frontier Matrix Knowledge Base* (PDF) *(recommended home: `docs/architecture/` or `docs/research/` — not confirmed in repo)*
- *Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks* (PDF) *(recommended home: `docs/architecture/` or `docs/research/` — not confirmed in repo)*

#### Documentation authoring and UI references

- *Comprehensive Guide to Markdown in Programming and Documentation* (PDF)
- *CSS Notes for Professionals* (PDF)
- *KFM-responsive-web-design-with-html5-and-css3* (PDF)
- *KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl* (PDF)
- *DesigningVirtualWorlds* (PDF)

#### Geospatial / modeling references

- *An Introduction to Spatial Data Analysis and Visualisation in R* (PDF)
- *KFM- python-geospatial-analysis-cookbook* (PDF)
- *Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide* (PDF)

#### AI / ML / statistics references

- *KFM- AI Foundations of Computational Agents (3rd Ed)* (PDF)
- *KFM- Artificial-neural-networks-an-introduction* (PDF)
- *KFM- deep-learning-in-python-prerequisites* (PDF)
- *KFM- Data Science & Machine Learning (Mathematical & Statistical Methods)* (PDF)
- *KFM- Understanding Statistics & Experimental Design* (PDF)
- *KFM- regression-analysis-with-python* (PDF)
- *KFM- Bayesian computational methods* (PDF)
- *KFM- Data Mining Concepts & applications* (PDF)

#### Graph and data engineering references

- *KFM- Spectral Geometry of Graphs* (PDF)
- *KFM- Scalable Data Management for Future Hardware* (PDF)
- *KFM- clean-architectures-in-python* (PDF)

#### Template source documents

- *Universal Markdown templates* (DOCX)
- *TEMPLATE__KFM_UNIVERSAL_DOC* (DOCX)
- *TEMPLATE__STORY_NODE_V3* (DOCX)
- *TEMPLATE__API_CONTRACT_EXTENSION* (DOCX)
- *KFM data Refrences* (DOCX)
- *KFM data References 2* (DOCX)
- *KFM DATA Refrences 3* (DOCX)
- *README Information* (DOCX)

> If these DOCX/PDF artifacts are being used as authoritative sources, prefer converting them into governed Markdown at their canonical `docs/**` or `schemas/**` destinations and treating the DOCX/PDF as upstream references only (to avoid drift).

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Links resolve (no broken internal references)
- [ ] Any “system rule” stated here is also reflected in governed artifacts (Master Guide / standards / blueprint), or is explicitly marked as *not confirmed in repo*
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated when relevant

## 🗂️ Directory Layout

### This document

- `path`: `docs/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Architecture | `docs/architecture/` | System architecture, ADRs, diagrams, redesign blueprints |
| Standards | `docs/standards/` | Repo standards + profiles (Markdown protocol, STAC/DCAT/PROV profiles) |
| Governance | `docs/governance/` | Governance, ethics, sovereignty controls |
| Data staging | `data/raw/`, `data/work/`, `data/processed/` | Raw inputs → intermediate artifacts → canonical processed outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC collections/items + DCAT mappings + PROV bundles |
| Graph import artifacts | `data/graph/` | Graph import CSV exports + optional post-import scripts |
| Data domains | `data/<domain>/` | Domain pack docs/governance; domain README; optional mapping notes |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build |
| API boundary | `src/server/` | API layer (contracts live here) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schema snapshots + contract tests |
| UI | `web/` | React + map clients, layer registry |
| Schemas | `schemas/` | JSON schemas, telemetry schemas |
| Tests | `tests/` | Unit + integration + contract tests |
| Tools | `tools/` | CLI utilities, validators |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| CI | `.github/` | Workflows, CI gates |
| Releases | `releases/` | Versioned packaged artifacts |

> Note: Some older docs may reference `src/api/` and/or `src/server/` simultaneously. The v13 blueprint recommends **one canonical home** at `src/server/` with explicit deprecation markers for any prior duplicates *(not confirmed in repo: migration status)*.

### Expected file tree for this sub-area

~~~text
📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
├── 📄 glossary.md                              # (planned) not confirmed in repo
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md         # (planned) source exists as PDF draft
│   ├── 📄 KFM_VISION_FULL_ARCHITECTURE.md       # (planned) source exists as PDF draft
│   ├── 📄 KFM_1_0_SYSTEM_DOCUMENTATION.pdf      # (not confirmed) consider adding the scope/system PDF here
│   ├── 📄 KFM_IMPLEMENTATION_GUIDE.pdf          # (not confirmed) consider adding implementation guide PDF here
│   ├── 📁 diagrams/
│   └── 📁 adr/
├── 📁 standards/
│   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md         # (planned) not confirmed in repo
│   ├── 📄 KFM_REPO_STRUCTURE_STANDARD.md        # (planned) not confirmed in repo
│   ├── 📄 KFM_STAC_PROFILE.md                   # (planned) not confirmed in repo
│   ├── 📄 KFM_DCAT_PROFILE.md                   # (planned) not confirmed in repo
│   └── 📄 KFM_PROV_PROFILE.md                   # (planned) not confirmed in repo
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md                    # not confirmed in repo
│   ├── 📄 ETHICS.md                             # not confirmed in repo
│   └── 📄 SOVEREIGNTY.md                        # not confirmed in repo
├── 📁 data/
│   └── 📄 <domain documentation lives here>     # optional; keep one canonical location and link
├── 📁 pipelines/
│   └── 📄 <etl + catalog documentation lives here>
├── 📁 graph/
│   └── 📄 <ontology + entity/edge documentation lives here>
├── 📁 api/
│   └── 📄 <API docs + contract notes live here> # code lives in src/server/
├── 📁 web/
│   └── 📄 <UI docs: map/layer registry/a11y/audit>
├── 📁 reports/
│   └── 📁 story_nodes/
│       ├── 📁 draft/                            # optional split; not confirmed in repo
│       ├── 📁 published/                        # optional split; not confirmed in repo
│       └── 📁 assets/                           # optional; not confirmed in repo
├── 📁 telemetry/
│   └── 📄 <signals + instrumentation docs>
└── 📁 security/
    └── 📄 <redaction + threat model docs>
~~~

## 🧭 Context

### Background

KFM documentation is not just narrative: it defines and preserves the system’s contracts and invariants across ETL, catalogs, graph, API boundary, UI, and story layers.

At the system level, KFM is intended to be an evidence-first “living atlas” that integrates diverse Kansas historical/cultural/ecological data into a unified graph, and surfaces that evidence through interactive maps, timelines, and provenance-linked Story Nodes.

### Assumptions

- This README is aligned to the **v12 Master Guide** as the current system anchor and the **v13 blueprint** as a target layout for canonical roots and CI gates.
- If a referenced path/document is missing, treat it as **not confirmed in repo** and either:
  - add it under the correct canonical location, or
  - update this README to link to the correct existing location.

### Constraints / invariants

- The pipeline order is preserved:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- The UI must consume data through the **API boundary** (no direct graph dependency).
- Focus Mode only consumes provenance-linked content (no uncited facts).
- No new public narrative without sources, no new data without provenance, and no new subsystem changes without docs + tests.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `docs/**` subdirectories are present today vs planned? | TBD | TBD |
| Where is the glossary located (or should it be created at `docs/glossary.md`)? | TBD | TBD |
| What is the repo’s canonical API schema format (OpenAPI, GraphQL, both)? | TBD | TBD |
| Which staging convention is authoritative across domains (global `data/raw|work|processed/<domain>` vs domain-local `data/<domain>/{raw,work,processed}`)? | TBD | TBD |
| Where is the authoritative governance root (e.g., `docs/governance/` vs `docs/standards/governance/`)? | TBD | TBD |

### Future extensions

- Add a docs index per major area (data, pipelines, graph, API, web, story nodes).
- Add a “docs health check” script to validate internal links and required front matter.
- Add an ADR formalizing staging conventions and canonical roots where conflicts exist.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API boundary]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Data lifecycle

- Canonical staging roots:
  - `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- Catalog + provenance outputs:
  - `data/stac/` + `data/catalog/dcat/` + `data/prov/`
- Graph import artifacts:
  - `data/graph/` (CSV exports, optional post-import Cypher)
- Optional derived evidence products:
  - `data/reports/<domain>/` (as needed; do not replace catalog outputs)

### Domain expansion pattern

- New domain packs go under `data/<domain>/...` (with governance + README + optional mapping notes).
- New domain docs go under `docs/<domain>/...` or `docs/data/<domain>/...` (**choose one canonical location and link**).
- If a domain uses domain-local staging roots (`data/<domain>/{raw,work,processed}`), the domain README must:
  - document why, and
  - link to an ADR or standard (if adopted). *(not confirmed in repo)*

### Example domain modules found in project docs

- Air Quality module (example paths; not confirmed in repo):
  - `docs/data/air-quality/README.md`
  - `data/air-quality/governance/README.md`
  - `data/raw/air-quality/` → `data/work/air-quality/` → `data/processed/air-quality/`
- Land Treaties module (example paths; not confirmed in repo):
  - `docs/data/historical/land-treaties/README.md`
  - `data/historical/land-treaties/`
- Soils SDA module (example paths; not confirmed in repo):
  - `data/soils/sda/README.md`
  - `data/raw/soils/` → `data/processed/soils/`

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

- Every new dataset must have:
  - STAC Collection + Item(s)
  - DCAT mapping (minimum title/description/license/keywords)
  - PROV activity bundle for the transform that generated it

### Versioning expectations

- New versions should link predecessor/successor relationships.
- Graph should mirror version lineage where applicable.

### Where schemas live

- STAC validation: `schemas/stac/**`
- DCAT validation: `schemas/dcat/**`
- PROV validation: `schemas/prov/**`
- Story Node validation: `schemas/story_nodes/**` *(if adopted; not confirmed in repo)*
- UI registry validation: `schemas/ui/**` *(if adopted; not confirmed in repo)*

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| API boundary | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story Nodes | schema + citations + entity refs | no unsourced narrative |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] ETL: deterministic pipeline outputs in canonical staging roots
- [ ] STAC: new collection + item schema validation
- [ ] DCAT: dataset record created/validated
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] API: contract update + tests + redaction rules
- [ ] UI: layer registry entry + access rules + a11y notes
- [ ] Story Nodes: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes must carry provenance annotations and connect to graph entities.
- Published Story Nodes must pass validation for front-matter, citations, entity references, and redaction compliance.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Story Node validation
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Repo lint expectations

- No YAML front-matter in code files
- No duplicate canonical homes without explicit deprecation markers
- No misspelled README variants (e.g., `README.me`)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Telemetry schemas | `schemas/telemetry/` | `docs/telemetry/` + CI artifacts |
| Pipeline run lineage | `data/prov/` | `data/prov/**` + release manifests (if used) |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.
- Prefer API-boundary enforcement for redaction and downstream propagation into UI/story views.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-24 | Align docs index with v12 guide + v13 blueprint; add canonical roots, CI gates, and project reference library | TBD |
| v1.0.0 | 2025-12-22 | Initial `docs/` README index | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
