---
title: "Docs — Kansas Frontier Matrix Documentation Index"
path: "docs/README.md"
version: "v1.0.3"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.3"
semantic_document_id: "kfm-docs-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.3"
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

## 📘 Overview

### Purpose

- Provide a single entry point for navigating `docs/` (the governed documentation root).
- Direct contributors to **templates + standards** before authoring new docs.
- Keep documentation architecture-synced to the canonical system flow:

  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

- Make drift explicit:
  - If a path is referenced but missing, flag it as **not confirmed in repo** and propose the canonical home.
  - Prefer **linking** to canonical artifacts over duplicating content.

### Operating principles

- **Template-first:** every governed doc conforms to one approved template.
- **One canonical home:** avoid “mystery duplicates”; link instead of copy.
- **Provenance-first:** no new narrative without sources; no new data without provenance.
- **API boundary is mandatory:** UI clients do not read Neo4j (or graph exports) directly; access is via contracted APIs.
- **Truthfulness markers:** when this doc says **not confirmed in repo**, treat it as an action item to either:
  - create the missing artifact at the canonical path, or
  - update this index to point to the real existing path.

### Read-first order

This order is “contract-first”: learn the invariants, then the authoring rules, then the domain docs.

1) `docs/MASTER_GUIDE_v12.md` — system + pipeline invariants, canonical inventory  
2) `docs/standards/` — Markdown protocol + ontology protocol + STAC/DCAT/PROV profiles  
3) `docs/templates/` — Universal / Story Node / API Contract Extension templates  
4) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — v13 target layout + readiness gates  
5) `docs/data/**` — domain modules (source/lineage/constraints)  
6) `docs/security/**` + `docs/governance/**` — safety, ethics, sovereignty controls

If a “read-first” file is missing, do not invent a replacement elsewhere — add it at the canonical path or update this list.

### Template selection quick reference

| You are writing… | Use this template | Canonical destination |
|---|---|---|
| Guides, standards, architecture docs, runbooks | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | `docs/**` |
| Story Nodes and Focus Mode narratives | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | `docs/reports/story_nodes/**` |
| API contract changes or new endpoints | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | `src/server/**` (code) + `src/server/contracts/**` (schemas, if present) + `docs/api/**` (human notes) |

### Scope

| In Scope | Out of Scope |
|---|---|
| Where documentation lives and how it is organized | Full implementations of pipelines/services/UI |
| Template selection rules and canonical placement | Ad-hoc debugging notes (unless governed and placed appropriately) |
| Docs-to-data linkage expectations (STAC/DCAT/PROV IDs, provenance refs) | Replacing the Master Guide or rewriting the templates |
| Handling “target layout” vs legacy drift | Making up missing policies or undocumented file paths |

### Audience

- Primary: contributors authoring/maintaining governed documentation
- Secondary: engineers/reviewers working in ETL, catalogs, graph, API, UI, Story Nodes, Focus Mode

### Definitions

- Glossary link: `docs/glossary.md` *(not confirmed in repo; add if missing)*

Common terms used across docs:

- STAC / DCAT / PROV-O
- Neo4j knowledge graph
- Contract tests
- Deterministic ETL
- Story Nodes
- Focus Mode
- Redaction / generalization

### Key artifacts

Status legend:

- ✅ Present (explicitly listed as present in governed design docs)
- 🟡 Placeholder (exists as an empty/placeholder artifact in governed design docs)
- ❓ Not confirmed in repo (expected, but not verified here)

| Artifact | Path / Identifier | Status | Notes |
|---|---|---|---|
| Docs index (this file) | `docs/README.md` | ✅ | Canonical navigation + placement rules |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | ✅ | Pipeline ordering + system inventory anchor |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | ✅ | Target layout + CI readiness gates |
| Universal Doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | ✅ | Default governed doc |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | ✅ | Story Node + Focus Mode narratives |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | ✅ | REST/GraphQL contract changes |
| Ontology protocol | `docs/standards/KFM_ONTology_PROTOCOL.md` | ✅ | Canonical ontology + graph constraints rules |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | ✅ | KFM DCAT constraints/mapping rules |
| STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | 🟡 | Placeholder noted in v13 materials |
| PROV profile | `docs/standards/KFM_PROV_PROFILE.md` | 🟡 | Placeholder noted in v13 materials |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | ❓ | Expected; governs Markdown conventions |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | ❓ | Expected; governs canonical roots |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | ❓ | Required governed reference (create if missing) |
| Ethics policy | `docs/governance/ETHICS.md` | ❓ | Required governed reference (create if missing) |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | ❓ | Required governed reference (create if missing) |

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Internal links resolve (no broken internal references)
- [ ] “Where things go” guidance matches Master Guide + standards, or is marked **not confirmed in repo**
- [ ] “One canonical home” rule is respected (links instead of duplicates)
- [ ] Validation steps are listed and reproducible
- [ ] Governance + CARE/sovereignty considerations are stated when relevant

## 🗂️ Directory Layout

### This document

- `path`: `docs/README.md`

### Canonical roots at a glance

~~~text
📁 <repo-root>/
├─ 📁 .github/          # CI + security + community health
├─ 📁 data/             # raw/work/processed + catalog outputs
├─ 📁 docs/             # governed documentation (this index)
├─ 📁 mcp/              # experiments, runs, model cards, SOPs
├─ 📁 schemas/          # JSON schemas (and optional shapes) for validation gates
├─ 📁 src/              # pipelines/graph/server (code)
├─ 📁 tests/            # unit + integration + contract tests
├─ 📁 tools/            # CLI utilities + validators (not canonical output homes)
├─ 📁 web/              # UI (React/map client) — code and/or build artifacts
└─ 📁 releases/         # versioned packaged outputs (if used)
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Templates | `docs/templates/` | Universal / Story Node / API Contract templates |
| Standards | `docs/standards/` | Markdown protocol + profiles (STAC/DCAT/PROV) + ontology protocol |
| Governance | `docs/governance/` | Governance, ethics, sovereignty controls |
| Architecture | `docs/architecture/` | Architecture docs, ADRs, redesign blueprints |
| Domain docs | `docs/data/` | Domain module documentation index |
| Pipelines docs | `docs/pipelines/` | ETL + catalog build docs |
| Graph docs | `docs/graph/` | Ontology + entity/edge documentation |
| API docs | `docs/api/` | Human-facing API notes (contracts live with server) |
| UI docs | `docs/web/` | UI layer registry + accessibility + audit notes |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes + assets |
| Security docs | `docs/security/` | Threat model + redaction rules + security notes |
| Telemetry docs | `docs/telemetry/` | Signals + instrumentation docs |

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed (and/or domain packs) |
| Global STAC | `data/stac/` | STAC collections + items (machine-validated) |
| Global DCAT | `data/catalog/dcat/` | DCAT datasets/distributions (machine-validated) |
| Global PROV | `data/prov/` | Lineage bundles/activities (machine-validated) |
| Graph artifacts | `data/graph/` | Import fixtures (csv/cypher as adopted) |
| Pipelines code | `src/pipelines/` | Deterministic ETL + transforms + catalog generation |
| Graph code | `src/graph/` | Ontology bindings + graph ingest/migrations/constraints |
| API boundary code | `src/server/` | Contracted API layer + policy enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schemas + contract test fixtures |
| UI code | `web/` | React + map clients + layer registry |

Legacy drift note:

- Older drafts may reference `src/api/` or `src/web/`. New work should align to canonical roots above and add explicit deprecation/migration notes when moving paths.

### Expected docs tree

~~~text
📁 docs/
├─ 📄 README.md
├─ 📄 MASTER_GUIDE_v12.md
├─ 📄 glossary.md                                   # optional; not confirmed in repo
├─ 📁 templates/
│  ├─ 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│  ├─ 📄 TEMPLATE__STORY_NODE_V3.md
│  └─ 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├─ 📁 standards/
│  ├─ 📄 KFM_MARKDOWN_WORK_PROTOCOL.md              # not confirmed in repo
│  ├─ 📄 KFM_REPO_STRUCTURE_STANDARD.md             # not confirmed in repo
│  ├─ 📄 KFM_STAC_PROFILE.md                        # placeholder noted in v13 materials
│  ├─ 📄 KFM_DCAT_PROFILE.md
│  ├─ 📄 KFM_PROV_PROFILE.md                        # placeholder noted in v13 materials
│  └─ 📄 KFM_ONTology_PROTOCOL.md
├─ 📁 governance/
│  ├─ 📄 ROOT_GOVERNANCE.md                         # not confirmed in repo
│  ├─ 📄 ETHICS.md                                  # not confirmed in repo
│  └─ 📄 SOVEREIGNTY.md                              # not confirmed in repo
├─ 📁 architecture/
│  ├─ 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│  ├─ 📄 KFM_VISION_FULL_ARCHITECTURE.md            # not confirmed in repo
│  ├─ 📄 KFM_NEXT_STAGES_BLUEPRINT.md               # not confirmed in repo
│  ├─ 📁 adr/                                       # optional
│  └─ 📁 diagrams/                                  # optional
├─ 📁 data/
│  └─ 📁 <domain>/
│     └─ 📄 README.md
├─ 📁 pipelines/
│  └─ 📁 <etl + catalog docs>/
├─ 📁 graph/
│  └─ 📁 <ontology + graph docs>/
├─ 📁 api/
│  └─ 📁 <human-facing API notes>/
├─ 📁 web/
│  └─ 📁 <UI docs: map/layer registry/a11y>/
├─ 📁 reports/
│  └─ 📁 story_nodes/
│     ├─ 📁 draft/                                  # optional; not confirmed in repo
│     ├─ 📁 published/                              # optional; not confirmed in repo
│     └─ 📁 assets/                                 # optional; not confirmed in repo
├─ 📁 telemetry/
│  └─ 📁 <signals + instrumentation docs>/
└─ 📁 security/
   └─ 📁 <redaction + threat model docs>/
~~~

## 🧭 Context

### Background

KFM documentation is not just narrative — it preserves the system’s **contracts and invariants** across ETL, catalogs, graph, APIs, UI, and Story Nodes. Documentation is treated as a governed artifact, intended to be versioned, reviewed, and validated along with code and data.

### Assumptions

- The v12 Master Guide is the current anchor for pipeline ordering and canonical roots.
- v13 redesign/vision materials may evolve and should be normalized into governed Markdown under `docs/architecture/` to avoid drift.
- If an expected file is missing, prefer creating it in the canonical location over working around it.

### Constraints and invariants

- Pipeline order is preserved:

  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

- The UI consumes graph/context through the **API boundary** only.
- Focus Mode consumes **provenance-linked** content only.
- Avoid redundant copies of schemas/standards/templates — link to canonical versions.

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
- Published Story Nodes should validate for:
  - front matter
  - citations and evidence references
  - entity references
  - redaction compliance

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### CI behavior contract

- Validate if present: if a canonical root exists (or changes), validate its artifacts.
- Fail if invalid: schema errors, missing links, or orphan references fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing overall CI.

### Minimum checks

- [ ] Markdown protocol checks for governed docs
- [ ] Schema validation (STAC/DCAT/PROV, Story Nodes, UI registries, telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests (`src/server/contracts/**` if present)
- [ ] UI registry checks (layer registry schema)
- [ ] Link integrity checks for docs (if tooling exists)
- [ ] Security and sovereignty checks (as applicable)

### Local reproduction

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# 1) validate schemas
# 2) validate provenance bundles
# 3) run unit/integration tests
# 4) run doc lint / link checks
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

- Document redaction/generalization rules for restricted locations.
- Prefer API-boundary enforcement so redaction propagates into UI + Story views.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.

## 📚 Project reference library

These documents are part of the project’s working reference set. They are not automatically assumed to be committed into the repo. If you vendor any of them into `docs/`, ensure licensing, size constraints, and governance review are completed.

### Architecture, scope, planning, and expansion references

- MASTER_GUIDE_v12 (PDF export)
- Kansas Frontier Matrix — v13 Redesign Blueprint (PDF)
- Kansas Frontier Matrix: System Structure and Scope (PDF)
- Kansas Frontier Matrix (KFM) Implementation Guide (PDF)
- Expanding the Kansas Frontier Matrix Knowledge Base (PDF)
- Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks (PDF)
- Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design (PDF)

### Documentation authoring and UI references

- Comprehensive Guide to Markdown in Programming and Documentation (PDF)
- Universal Markdown templates (DOCX)
- CSS Notes for Professionals (PDF)
- KFM-responsive-web-design-with-html5-and-css3 (PDF)
- KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl (PDF)
- DesigningVirtualWorlds (PDF)
- KFM- Computer Graphics using JAVA 2D & 3D (PDF)

### Geospatial and modeling references

- An Introduction to Spatial Data Analysis and Visualisation in R (PDF)
- KFM- python-geospatial-analysis-cookbook (PDF)
- Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide (PDF)
- KFM- Generalized Topology Optimization for Structural Design (PDF)

### AI, ML, and statistics references

- KFM- AI Foundations of Computational Agents (3rd Ed) (PDF)
- KFM- Artificial-neural-networks-an-introduction (PDF)
- KFM- deep-learning-in-python-prerequisites (PDF)
- KFM- Data Science & Machine Learning (Mathematical & Statistical Methods) (PDF)
- KFM- Understanding Statistics & Experimental Design (PDF)
- KFM- regression-analysis-with-python (PDF)
- KFM- Bayesian computational methods (PDF)
- KFM- Data Mining Concepts & applications (PDF)

### Graph and data engineering references

- KFM- Spectral Geometry of Graphs (PDF)
- KFM- Scalable Data Management for Future Hardware (PDF)
- KFM- clean-architectures-in-python (PDF)

### Template and draft source documents

- TEMPLATE__KFM_UNIVERSAL_DOC (DOCX)
- TEMPLATE__STORY_NODE_V3 (DOCX)
- TEMPLATE__API_CONTRACT_EXTENSION (DOCX)
- KFM Reference Data (PDF)
- KFM data References (DOCX variants)
- README Information (DOCX)

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.3 | 2025-12-27 | Rebuilt docs index for contract-first navigation: clarified status legend, aligned canonical roots to Master Guide inventory, harmonized v12 staging vs v13 domain packs, and tightened “one canonical home + provenance-first” rules | TBD |
| v1.0.2 | 2025-12-26 | Align docs index to v13 target roots (domain packs + global catalogs), add template-selection guidance, and expand project reference library | TBD |
| v1.0.1 | 2025-12-24 | Align docs index with v12 guide + v13 blueprint; add canonical roots, CI gates, and project reference library | TBD |
| v1.0.0 | 2025-12-22 | Initial `docs/` README index | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
