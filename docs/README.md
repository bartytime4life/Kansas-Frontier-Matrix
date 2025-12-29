---
title: "Docs — Kansas Frontier Matrix Documentation Index"
path: "docs/README.md"
version: "v1.0.5"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.5"
semantic_document_id: "kfm-docs-readme-v1.0.5"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.5"
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

This file is the **canonical entry point** for navigating `docs/` and for deciding **where new documentation belongs**.

## Quick navigation

| If you need to… | Start here… |
|---|---|
| Understand pipeline invariants + canonical roots | `docs/MASTER_GUIDE_v12.md` |
| Write/update a governed doc | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` |
| Write a Story Node / Focus Mode narrative | `docs/templates/TEMPLATE__STORY_NODE_V3.md` |
| Propose or change an API contract | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` |
| Follow governed Markdown formatting/front‑matter rules | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo; create if missing)* |
| Review ingestion + intake architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` *(not confirmed in repo; add if adopting Data Intake Design)* |
| Align work to target layout + readiness gates | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(draft reference; if adopted)* |

> **Truthfulness marker:** when this index says **not confirmed in repo**, treat it as an action item to either:
> - create the missing artifact at the canonical path, or
> - update this index to point to the real existing path.
>
> Do **not** invent replacement policies, standards, or paths elsewhere.

## 📘 Overview

### Purpose

- Provide a single entry point for navigating `docs/` (the governed documentation root).
- Direct contributors to **templates + standards** before authoring new docs.
- Keep documentation architecture-synced to the canonical system flow:

  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

- Make drift explicit and actionable:
  - If a path is referenced but missing, flag it as **not confirmed in repo** and propose the canonical home.
  - Prefer **linking** to canonical artifacts over duplicating content.

### Scope

| In Scope | Out of Scope |
|---|---|
| Where documentation lives and how it is organized | Full implementations of pipelines/services/UI |
| Template selection rules and canonical placement | Ad-hoc debugging notes (unless governed and placed appropriately) |
| Docs-to-data linkage expectations (STAC/DCAT/PROV IDs, provenance refs) | Replacing the Master Guide or rewriting the templates |
| Handling “target layout” vs legacy drift | Making up missing policies or undocumented file paths |

### Audience

- Primary: contributors authoring/maintaining governed documentation
- Secondary: engineers/reviewers working across ETL, catalogs, graph, API, UI, Story Nodes, Focus Mode

### Definitions

- Glossary link: `docs/glossary.md` *(not confirmed in repo; add if missing)*

Common terms used across docs:

- STAC / DCAT / PROV-O
- Neo4j knowledge graph
- Contract-first / contract tests
- Deterministic ETL
- Story Nodes
- Focus Mode
- Redaction / generalization
- “Not confirmed in repo”

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Docs index (this file) | `docs/README.md` | Docs | Canonical navigation + placement rules |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Docs/Core | Pipeline ordering + system inventory anchor |
| Universal Doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Story Node + Focus Mode narratives |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Draft reference; **if adopted** |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap; **not confirmed in repo** |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | **Not confirmed in repo** |
| Docs standards root | `docs/standards/` | Docs/Core | Governed standards; **some items not confirmed in repo** |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Required reference; **not confirmed in repo** |
| Ethics policy | `docs/governance/ETHICS.md` | Governance | Required reference; **not confirmed in repo** |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | Required reference; **not confirmed in repo** |
| Ingest architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Architecture/Data | **Not confirmed in repo**; align intake docs here if adopted |
| KFM 1.0 System Documentation (PDF) | `docs/architecture/KFM_1_0_SYSTEM_DOCUMENTATION.pdf` | Architecture | **Not confirmed in repo**; proposed canonical home if added |

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Internal links resolve (no broken internal references)
- [ ] “Where things go” guidance matches the Master Guide + standards, or is marked **not confirmed in repo**
- [ ] “One canonical home” guidance is consistent and unambiguous
- [ ] Validation steps are listed and reproducible
- [ ] Governance + CARE/sovereignty considerations are stated when relevant

## 🗂️ Directory Layout

### This document

- `path`: `docs/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| STAC | `data/stac/` | Collections + Items for spatiotemporal assets |
| DCAT | `data/catalog/dcat/` | Dataset/distribution discovery views |
| PROV | `data/prov/` | Lineage bundles (activities/entities/agents); run traceability |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Standards | `docs/standards/` | Governed standards + profiles *(some items not confirmed in repo)* |
| Governance | `docs/governance/` | Governance, ethics, sovereignty controls *(may be missing; do not invent alternates)* |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Repo top-levels (expected)

~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 standards/                          # some items not confirmed in repo
├── 📁 governance/                         # some items not confirmed in repo
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md    # draft reference; if adopted
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md     # roadmap; not confirmed in repo
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md  # not confirmed in repo
├── 📁 data/
│   └── 📁 <domain>/
└── 📁 reports/
    └── 📁 story_nodes/                    # pattern; draft/published split if defined

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/
├── 📁 ui/
└── 📁 telemetry/

📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/

📁 web/
📁 tests/
📁 tools/
📁 releases/
~~~

### Canonical homes by stage

| Stage | Canonical home | Primary artifacts |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | deterministic transforms; outputs land in `data/**` |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections, DCAT datasets, PROV bundles |
| Graph | `src/graph/` + `data/graph/` *(if used)* | ontology-governed ingest + import fixtures |
| API boundary | `src/server/` | OpenAPI/GraphQL contracts, redaction, query services |
| UI | `web/` | map layers, Focus Mode UI, citation rendering |
| Story Nodes | `docs/reports/story_nodes/` | draft/published Story Nodes + assets |
| MCP | `mcp/runs/` + `mcp/experiments/` | run logs, experiments, model cards |
| Releases | `releases/` | manifests, SBOMs, signed bundles, telemetry snapshots *(if used)* |

## 🧭 Context

### Background

KFM documentation is not just narrative — it preserves the system’s **contracts and invariants** across ETL, catalogs, graph, APIs, UI, and Story Nodes. Documentation is treated as a governed artifact, intended to be versioned, reviewed, and validated along with code and data.

### What KFM is

KFM is an open-source, geospatial + historical knowledge system that ingests heterogeneous sources, publishes governed catalogs (STAC/DCAT/PROV), builds a semantically structured Neo4j graph, and serves evidence through contracted APIs into a map + narrative UI. The system is designed so that every narrative claim can be traced to versioned evidence and every derived product has explicit lineage.

### Assumptions

- The v12 Master Guide is the current anchor for pipeline ordering and canonical roots.
- v13 redesign/vision materials are draft references and must be normalized into governed Markdown under `docs/architecture/` to avoid drift.
- If an expected file is missing, prefer creating it in the canonical location over working around it.

### Constraints and invariants

- Pipeline order is preserved:

  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

- The UI consumes graph/context through the **API boundary** only.
- Focus Mode consumes **provenance-linked** content only.
- Story content must separate **fact vs inference vs hypothesis** where applicable.
- Avoid redundant copies of schemas/standards/templates — link to canonical versions.

### Drift watchlist

Common drift patterns to correct over time:

- Missing canonical roots referenced by standards/CI (`schemas/`, `releases/`, `data/catalog/dcat/`, `data/prov/`)
- Duplicate/ambiguous homes (e.g., `src/api/` vs `src/server/`, `src/map/` vs `web/`)
- Story Node location mismatch (legacy structures vs `docs/reports/story_nodes/`)
- File-type correctness (docs vs runnable scripts)

Treat these as remediation priorities and document migrations explicitly.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `docs/**` subdirectories are present today vs target? | TBD | TBD |
| Where is the canonical glossary located, and is it complete? | TBD | TBD |
| What is the canonical API schema format mix (OpenAPI, GraphQL, both)? | TBD | TBD |
| How should v12 staging (`data/raw`/`work`/`processed`) coexist with v13 domain packs (`data/<domain>/{raw,work,processed}`)? | TBD | TBD |
| Are there legacy governance refs under `docs/standards/**` that need migration to `docs/governance/**`? | TBD | TBD |

### Future extensions

- Add an index README per major area (`docs/data/`, `docs/pipelines/`, `docs/graph/`, `docs/api/`, `docs/web/`, `docs/security/`).
- Add a docs health-check script: validate internal links and required front matter.
- Add an ADR formalizing migration from legacy staging to domain packs (if both remain in use).

## 🗺️ Diagrams

### System dataflow

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Neo4j Graph — src/graph (+ data/graph imports)"]
  C --> D["API boundary — src/server"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional sequence

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph contracts)

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (apply redaction rules)
  Graph-->>API: context bundle (entities + evidence refs)
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/**`
- `docs/standards/**` *(if present)*
- `docs/governance/**` *(if present)*

### Outputs

- This index file (`docs/README.md`) and any local `docs/**/README.md` indexes

### Data lifecycle

KFM supports deterministic staging and machine-validated catalogs.

Baseline staging pattern:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ optional `data/reports/` outputs)

v13 target domain-pack pattern:

- `data/<domain>/raw/` → `data/<domain>/work/` → `data/<domain>/processed/`

Global catalog outputs:

- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`
- Graph import fixtures (if used): `data/graph/`

If both baseline staging and domain packs exist, document the mapping explicitly in:
- `docs/data/<domain>/README.md` and/or an ADR under `docs/architecture/adr/`.

### Domain expansion pattern

When adding a new domain:

1) Create staging directories:
   - `data/<domain>/raw/`
   - `data/<domain>/work/`
   - `data/<domain>/processed/`

2) Ensure processed outputs can generate:
   - STAC Collection + Item(s)
   - DCAT dataset record(s)
   - PROV activity/bundle(s)

3) Create domain docs:
   - `docs/data/<domain>/README.md`

4) If domain-specific mappings exist (e.g., `data/<domain>/mappings/`), link them from the domain README.

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

Every dataset/evidence product must have:

- STAC Collection + Item(s)
- DCAT mapping (minimum title/description/license/keywords)
- PROV bundle for the activity that generated it

### Versioning expectations

- New versions link predecessor/successor relationships in catalogs.
- Graph mirrors version lineage where applicable.

### Where schemas live

*(Paths are targets; some may be not confirmed in repo.)*

- STAC validation: `schemas/stac/**`
- DCAT validation: `schemas/dcat/**`
- PROV validation: `schemas/prov/**`
- Story Node validation: `schemas/story_nodes/**`
- UI registry validation: `schemas/ui/**`
- Telemetry validation: `schemas/telemetry/**`

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story Nodes | schema + citations + entity refs | no unsourced narrative |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] ETL: deterministic pipeline outputs land in canonical staging + catalogs
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
- Published Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Story Nodes should separate:
  - facts
  - inferences
  - hypotheses

### UI integration expectations (evidence-first)

- Story Node citations and references should be **clickable** in the UI and able to surface evidence context (catalog metadata, snippets, or linked assets).
- Story Nodes should be linkable to graph entities (Place/Person/Event/Document/etc.) so the UI can surface relevant stories based on user context.

### Focus Mode rule (hard gate)

- Focus Mode only consumes provenance-linked content.
- Any predictive/suggestive content must be:
  - opt-in,
  - paired with uncertainty/confidence metadata,
  - prohibited from inferring or revealing sensitive locations.

## 🧪 Validation & CI/CD

### CI behavior contract

- Validate if present: if a canonical root exists (or changes), validate its artifacts.
- Fail if invalid: schema errors, missing links, or orphan references fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing overall CI.

### Minimum checks

- [ ] Markdown protocol checks for governed docs (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation:
  - [ ] STAC/DCAT/PROV
  - [ ] story node schemas (if present)
  - [ ] telemetry schemas (if present)
  - [ ] UI layer registry schemas (if present)
- [ ] Graph integrity checks (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] Security and sovereignty scanning gates (as applicable):
  - [ ] secret scan
  - [ ] PII scan
  - [ ] sensitive-location leakage checks
  - [ ] classification propagation checks (no downgrades without review)

### Local reproduction

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# 1) validate schemas
# 2) validate provenance bundles
# 3) run unit/integration tests
# 4) run doc lint / link checks
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` | catalogs/pipelines | `data/prov/**` + telemetry stores (if used) |
| `redaction_applied` | API/pipelines | `data/prov/**` + API logs (as governed) |
| `promotion_blocked` | CI/publish gate | CI artifacts + audit logs |
| `catalog_published` | catalog job | CI artifacts + release manifests (if used) |
| `focus_mode_redaction_notice_shown` | UI | UI telemetry (if present) |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for restricted locations.
- Prefer API-boundary enforcement so redaction propagates into UI + Story views.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.

## 📚 Project reference library

These documents are part of the project’s working reference set. They are not automatically assumed to be committed into the repo. If you vendor any of them into `docs/`, ensure licensing, size constraints, and governance review are completed.

Suggested canonical home if vendored: `docs/reference/` *(not confirmed in repo; create if needed)*.  
For architecture PDFs specifically, `docs/architecture/` is an acceptable canonical home.

### Available reference files in this project bundle

**Architecture, scope, planning, intake**
- `MASTER_GUIDE_v12.md.pdf` (PDF export)
- `Kansas Frontier Matrix_ System Structure and Scope.pdf`
- `Kansas Frontier Matrix (KFM) Implementation Guide.pdf`
- `Kansas Frontier Matrix (KFM) System – Visual and Functional Overview.pdf`
- `Expanding the Kansas Frontier Matrix Knowledge Base.pdf`
- `Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks.pdf`
- `Elevating the Kansas Frontier Matrix: Gaps and Proposed Enhancements.pdf`
- `Data Intake Design KFM.pdf`
- `KFM Reference Data.pdf`

**Templates and documentation authoring**
- `Universal Markdown templates.docx`
- `TEMPLATE__KFM_UNIVERSAL_DOC.md.docx`
- `TEMPLATE__STORY_NODE_V3.md.docx`
- `TEMPLATE__API_CONTRACT_EXTENSION.md.docx`
- `Comprehensive Guide to Markdown in Programming and Documentation.pdf`
- `The Comprehensive Markdown Guide.pdf`

**Web/UI and developer notes**
- `CSS Notes for Professionals - CSSNotesForProfessionals.pdf`
- `Git Notes for Professionals - GitNotesForProfessionals.pdf`
- `Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf`
- `MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `KFM-responsive-web-design-with-html5-and-css3.pdf`
- `KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `DesigningVirtualWorlds.pdf`

**Geospatial and visualization**
- `An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf`
- `graphical-data-analysis-with-r.pdf`
- `geoprocessing-with-python.pdf`
- `KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf`
- `KFM- Computer Graphics using JAVA 2D & 3D.pdf`

**Scientific modeling, AI/ML, stats**
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `KFM- AI Foundations of Computational Agents 3rd Ed.pdf`
- `KFM- Artificial-neural-networks-an-introduction.pdf`
- `KFM- deep-learning-in-python-prerequisites.pdf`
- `KFM- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`
- `KFM-regression-analysis-with-python.pdf`
- `KFM- Bayesian computational methods.pdf`
- `KFM- Data Mining Concepts & applictions.pdf`

**Graph and data engineering**
- `KFM- Spectral Geometry of Graphs.pdf`
- `KFM- Scalable Data Management for Future Hardware.pdf`

**Optimization**
- `KFM- Generalized Topology Optimization for Structural Design.pdf`

### Referenced elsewhere but not confirmed in this bundle

- `KFM 1.0 System Documentation (PDF)` *(not confirmed in repo; proposed: `docs/architecture/KFM_1_0_SYSTEM_DOCUMENTATION.pdf`)*
- `Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design (PDF)` *(not confirmed)*
- `KFM- Understanding Statistics & Experimental Design (PDF)` *(not confirmed)*
- `KFM- clean-architectures-in-python (PDF)` *(not confirmed)*
- `README Information (DOCX)` *(not confirmed)*
- `KFM data References (DOCX variants)` *(not confirmed)*

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.5 | 2025-12-29 | Re-aligned to Universal Governed Doc structure; synced repo top-level tree + canonical homes to Master Guide v12; normalized standards filenames per v12/v13 guidance; added intake architecture pointer (not confirmed in repo); rebuilt “Key artifacts” to match template columns; reconciled reference library to the project file bundle and flagged missing items explicitly | TBD |
| v1.0.4 | 2025-12-28 | Template-aligned to Universal Governed Doc sections; added quick navigation; consolidated duplicate path tables; clarified drift watchlist and file-type correctness; aligned CI gate list to Master Guide; preserved “not confirmed in repo” truthfulness markers | TBD |
| v1.0.3 | 2025-12-27 | Rebuilt docs index for contract-first navigation: clarified status legend, aligned canonical roots to Master Guide inventory, harmonized v12 staging vs v13 domain packs, and tightened “one canonical home + provenance-first” rules | TBD |
| v1.0.2 | 2025-12-26 | Align docs index to v13 target roots (domain packs + global catalogs), add template-selection guidance, and expand project reference library | TBD |
| v1.0.1 | 2025-12-24 | Align docs index with v12 guide + v13 blueprint; add canonical roots, CI gates, and project reference library | TBD |
| v1.0.0 | 2025-12-22 | Initial `docs/` README index | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`