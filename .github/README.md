---
title: "🧭 Kansas Frontier Matrix (KFM) — Contributor Hub"
path: ".github/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "Repo Meta"
license: "CC-BY-4.0 (docs); see repo LICENSE for code/data (not confirmed in this bundle)"
markdown_protocol_version: "KFM-MDP v11.2.6 (ref: KFM Markdown Guide)"
pipeline_contract_version: "KFM-PPC v11.0.0 (ref: KFM Markdown Guide)"
stac_profile: "KFM-STAC v11.0.0 (ref: KFM Markdown Guide)"
dcat_profile: "KFM-DCAT v11.0.0 (ref: KFM Markdown Guide)"
prov_profile: "KFM-PROV v11.0.0 (ref: KFM Markdown Guide)"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md (path referenced in KFM Markdown Guide; confirm in repo)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"
doc_uuid: "urn:kfm:doc:github:readme:v0.1.0-draft"
semantic_document_id: "kfm-github-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:github:readme:v0.1.0-draft"
commit_sha: "<fill-at-merge>"
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

# Kansas Frontier Matrix (KFM) — Contributor Hub

KFM is an open-source geospatial–historical knowledge platform (“living atlas” of Kansas) that ingests diverse sources, publishes governed metadata catalogs, builds a semantic knowledge graph, and delivers evidence-backed narratives through APIs to an interactive map UI.

This file lives under `.github/` to help contributors and reviewers align on **the canonical pipeline, governance rules, and repo expectations**.

---

## 🔗 Start here (reading order)

1) **📄 KFM Architecture Document.pdf** — system stages, contracts, and what “must never be bypassed”  
2) **📄 Kansas Frontier Matrix – Unified Technical Plan.docx** — implementation plan and subsystem responsibilities  
3) **📄 Kansas Frontier Matrix (KFM) – Master Documentation.docx** — core principles, invariants, and cross-cutting rules  
4) **📄 KFM Markdown Guide.docx** — Markdown protocol + templates + definition-of-done for docs  
5) **📄 Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx** — GitHub workflow expectations (issues, PRs, CI)

> If any of these files move into `docs/` later, update links here. (Paths outside this bundle are **not confirmed**.)

---

## 🧩 The canonical pipeline (non‑negotiable)

All KFM work must respect the enforced sequence:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

**Why this matters:** every stage adds standardized metadata + provenance, so every derived output and narrative claim is traceable to versioned evidence.

### ✅ Hard boundaries (contracts)

- **No stage bypassing.** If you add/modify data, it must enter through ETL and be registered in catalogs before it can reach graph/UI/story layers.  
- **API is the only gateway.** The UI must never access the database/graph directly; it consumes contracted API responses only.  
- **Provenance-first publishing.** Narrative content (Story Nodes + Focus Mode) must be evidence-linked; no uncited information is displayed.

---

## 🗺️ Repo orientation (expected structure)

⚠️ The exact folder layout should be confirmed against the repo’s Master Guide.  
The tree below reflects **KFM’s documented lifecycle roots** and common subsystem separation.

    📦 repo-root/
    ├── 📁 .github/
    │   ├── 📄 README.md                      — Contributor Hub (this file)
    │   └── 📁 workflows/                     — CI / validation (confirm in repo)
    │
    ├── 📁 docs/                              — Standards, governance, templates (confirm in repo)
    │   ├── 📁 🧾 templates/                  — e.g., TEMPLATE__KFM_UNIVERSAL_DOC, TEMPLATE__STORY_NODE_V3
    │   ├── 📁 📏 standards/                  — Markdown protocol, validation rules
    │   ├── 📁 🛡️ governance/                 — Sovereignty, sensitivity, approvals
    │   └── 📁 🕸️ graph/                      — Ontology notes, mappings (confirm in repo)
    │
    ├── 📁 data/                              — Canonical lifecycle roots
    │   ├── 📁 🧊 raw/                        — Immutable originals; versioned
    │   ├── 📁 🧪 work/                       — Intermediates; reproducible
    │   ├── 📁 ✅ processed/                  — Published/derived outputs
    │   ├── 📁 🛰️ stac/                       — STAC collections/items (confirm exact path)
    │   ├── 📁 🧰 catalog/                    — DCAT metadata (confirm exact subpath)
    │   └── 📁 🔗 prov/                       — PROV lineage (confirm exact path)
    │
    ├── 📁 etl/                               — Pipelines/jobs (name/path not confirmed)
    ├── 📁 🧠 graph/                          — Neo4j loads/migrations (name/path not confirmed)
    ├── 📁 🔌 api/                            — OpenAPI/GraphQL specs + server (name/path not confirmed)
    ├── 📁 🖥️ ui/                             — React/MapLibre client (name/path not confirmed)
    └── 📁 ✍️ story-nodes/                    — Markdown narratives (name/path not confirmed)

---

## 🧑‍💻 How to contribute (workflow)

### 1) Pick the right workstream

- 🧺 **Data intake / ETL** (new source, cleaning, transforms)
- 🗂️ **Catalogs** (STAC/DCAT metadata, PROV lineage)
- 🧠 **Graph** (ontology alignment, node/edge mapping, load rules)
- 🔌 **APIs** (contracted endpoints, versioning, compatibility)
- 🖥️ **UI** (React/MapLibre layers, story rendering, accessibility)
- ✍️ **Story Nodes / Focus Mode** (governed narrative + evidence panes)

### 2) Use the correct template

From **KFM Markdown Guide.docx**, canonical templates are referenced as:

- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`

If these template files are missing in the repo, treat that as a **blocker** and open a standardization issue.

### 3) PR checklist (minimum)

Before requesting review, ensure:

- ✅ Your change respects: **ETL → Catalogs → Graph → API → UI → Story → Focus**  
- ✅ New/updated datasets have **STAC + DCAT + PROV** artifacts (or an explicit, reviewed exception)  
- ✅ Identifiers are **stable** (don’t silently rename IDs; version them)  
- ✅ Outputs are **deterministic & reproducible** (reruns yield same results on same inputs)  
- ✅ Docs follow the **KFM Markdown Guide** and are evidence-linked where required  
- ✅ Sensitivity/sovereignty handling is reviewed when applicable  
- ✅ CI checks pass (lint, schema validation, tests — see below)

---

## 🧪 Validation gates (what CI should enforce)

> Exact workflows depend on the repo’s `.github/workflows/` configuration (not confirmed in this bundle).

Recommended automated checks:

- 📏 **Markdown**: formatting, internal link integrity, required front matter (if governed docs)
- 🛰️ **STAC**: schema validation + KFM-STAC profile constraints
- 🧰 **DCAT**: schema validation + KFM-DCAT profile constraints
- 🔗 **PROV**: lineage completeness (raw → work → processed → catalog → graph)
- 🧠 **Graph**: ontology mapping integrity + migration safety
- 🔌 **API**: OpenAPI/GraphQL contract tests + backward compatibility checks
- 🖥️ **UI**: basic smoke checks + layer registry/schema validation (if applicable)
- 🛡️ **Security**: secret scanning + sensitive content checks

---

## 🛡️ Governance, sovereignty, and safety expectations

KFM is built to be **FAIR + CARE** and **provenance-first**:

- **FAIR**: metadata makes data findable, accessible, interoperable, reusable  
- **CARE**: community authority + ethics; sensitive/Indigenous data handled on their terms  
- **Sovereignty filters**: apply sensitivity classification and access rules before content reaches users  
- **No “AI narrative truth.”** If AI/ML generates derived outputs, they are treated as **derived data products**:
  - must go through **ETL → Catalogs → Graph** like everything else  
  - must record model identity/version + parameters + timestamps in lineage metadata  
  - must carry uncertainty/confidence semantics (define what confidence means)

If a change touches governance policy text: **draft a proposal and flag “requires governance review.”**

---

## 📚 Project file bundle (included here)

These files are referenced throughout KFM work. **Core system docs** come first; everything else is supplemental guidance and must not override KFM contracts.

### 🧭 Core KFM documents

- 📄 **KFM Architecture Document.pdf** — canonical pipeline + subsystem contracts  
- 📄 **Kansas Frontier Matrix – Unified Technical Plan.docx** — implementation plan  
- 📄 **Kansas Frontier Matrix (KFM) – Master Documentation.docx** — master principles + rules  
- 📄 **KFM Markdown Guide.docx** — Markdown protocol + templates + DoD  
- 📄 **Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx** — GitHub + CI norms

### 🧠 AI / ML / data mining

- 📄 **AI Foundations of Computational Agents 3rd Ed.pdf**  
- 📄 **Artificial-neural-networks-an-introduction.pdf**  
- 📄 **deep-learning-in-python-prerequisites.pdf**  
- 📄 **Data Mining Concepts & applictions.pdf**  
- 📄 **Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf**

### 📊 Statistics, inference, regression

- 📄 **Bayesian computational methods.pdf**  
- 📄 **Understanding Statistics & Experimental Design.pdf**  
- 📄 **Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf**  
- 📄 **regression-analysis-with-python.pdf**  
- 📄 **graphical-data-analysis-with-r.pdf**

### 🗺️ GIS, geoprocessing, mapping, remote sensing

- 📄 **Geographic Information System Basics - geographic-information-system-basics.pdf**  
- 📄 **geoprocessing-with-python.pdf**  
- 📄 **python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf**  
- 📄 **making-maps-a-visual-guide-to-map-design-for-gis.pdf**  
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**  
- 📄 **Google Earth Engine Applications.pdf**  
- 📄 **Google Maps API Succinctly - google_maps_api_succinctly.pdf**  
- 📄 **google-maps-javascript-api-cookbook.pdf**  
- 📄 **Map Reading & Land Navigation** *(file type/path not confirmed in this bundle)*

### 🕸️ Web, UI, and visualization

- 📄 **responsive-web-design-with-html5-and-css3.pdf**  
- 📄 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**  
- 📄 **Computer Graphics using JAVA 2D & 3D.pdf**

### 🧩 Architecture, data systems, graphs, optimization, dev productivity

- 📄 **clean-architectures-in-python.pdf**  
- 📄 **Scalable Data Management for Future Hardware.pdf**  
- 📄 **Spectral Geometry of Graphs.pdf**  
- 📄 **Generalized Topology Optimization for Structural Design.pdf**  
- 📄 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**  
- 📄 **Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf**

---

## 🧭 Need help?

- Use **Issues** for bugs/tasks and **Pull Requests** for changes.
- If you’re unsure where something belongs in the pipeline, open an issue tagged: **question / architecture / governance** (labels not confirmed).

KFM’s north star: **every claim traceable, every dataset versioned, every workflow reproducible.**