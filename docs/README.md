---
title: "📚 docs/ — Documentation Index"
path: docs/README.md
version: v1.0.0
last_updated: 2025-12-31
status: draft
doc_kind: Guide
license: CC-BY-4.0

# KFM protocol + profile versions (confirm against repo standards if CI fails)
markdown_protocol_version: KFM-MDP v11.2.6
mcp_version: MCP-DL v6.3
ontology_protocol_version: KFM-ONTO v4.1.0
pipeline_contract_version: KFM-PPC v11.0.0
stac_profile: KFM-STAC v11.0.0
dcat_profile: KFM-DCAT v11.0.0
prov_profile: KFM-PROV v11.0.0

# Governance anchors
governance_ref: docs/governance/ROOT_GOVERNANCE.md
ethics_ref: docs/governance/ETHICS.md
sovereignty_policy: docs/governance/SOVEREIGNTY.md

# FAIR+CARE / risk
fair_category: FAIR+CARE
care_label: TBD
sensitivity: public
classification: open
jurisdiction: US-KS

# Identity + integrity
doc_uuid: urn:kfm:doc:docs:readme:v1.0.0
semantic_document_id: kfm-docs-readme-v1.0.0
event_source_id: ledger:kfm:doc:docs:readme:v1.0.0
commit_sha: TBD
doc_integrity_checksum: sha256:TBD

# AI usage policy (doc authoring / drafting helpers only)
ai_transform_permissions:
  - summarization
  - structure_extract
  - keyword_index
  - citation_assist
ai_transform_prohibited:
  - generate_policy
  - infer_sensitive_locations
  - decontextualized_narrative_claims
---

# 📚 docs/ — Documentation Index

This directory is the canonical home of **governed** Kansas Frontier Matrix (KFM) documentation.

A **governed document**:
- begins with YAML front‑matter,
- follows exactly **one approved template**,
- is compatible with KFM validation (schema + provenance + governance checks).

> If you are looking for the repo overview, go to the root `README.md`. This file is specifically for navigating **docs/**.

---

## 🚀 Start here

- 📘 **Master Guide (v13)** — `docs/MASTER_GUIDE_v13.md`
  - Canonical pipeline ordering, invariants, and “where things live.”
- 🧱 **Architecture & Roadmaps** — `docs/architecture/`
- 📜 **Standards & Profiles** — `docs/standards/`
- 🧩 **Templates** — `docs/templates/`
- ⚖️ **Governance & Review Gates** — `docs/governance/`
- 🗺️ **Story Nodes** — `docs/reports/story_nodes/`
- 🧰 **Domain Modules / Runbooks** — `docs/data/<domain>/README.md`

---

## 🧭 KFM pipeline ordering

KFM is a deterministic, contract-first pipeline: every stage consumes formal artifacts from the previous stage.

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph (references back to catalogs)"]
  G --> H["API Layer (contracts + redaction)"]
  H --> I["Map UI — React · MapLibre · (optional) Cesium"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked context bundle)"]
~~~

### ✅ Non‑negotiable invariants (quick list)

- **Pipeline ordering is absolute**: ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.
- **API boundary**: the UI must never query Neo4j directly; it must use the governed API.
- **Provenance first**: datasets and derived evidence must be cataloged (STAC/DCAT/PROV) before graph/UI/story use.
- **Deterministic ETL**: idempotent, config-driven, fully logged; stable IDs/hashes.
- **Evidence-first narrative**: Story Nodes / Focus Mode require citations to cataloged sources; AI text must be clearly labeled and evidence-linked.
- **Sovereignty/classification propagation**: outputs cannot be less restricted than inputs.

---

## 🗂️ docs/ folder map

~~~text
📁 docs/
├── 📄 README.md                      ← you are here
├── 📄 MASTER_GUIDE_v13.md            ← repo source-of-truth (pipeline + invariants)
├── 📁 architecture/                  ← blueprints, long-form architecture, roadmaps
├── 📁 standards/                     ← STAC/DCAT/PROV + ontology + markdown protocols
├── 📁 templates/                     ← governed doc templates (Universal/Story/API)
├── 📁 governance/                    ← review gates, ethics, sovereignty, policy refs
├── 📁 data/                          ← domain modules (each has its own README)
│   └── 📁 <domain>/
│       └── 📄 README.md              ← sources + ETL runbook + domain caveats
├── 📁 reports/                       ← outputs, audits, QA, derived analyses
│   └── 📁 story_nodes/
│       ├── 📁 templates/             ← story node helpers (if used)
│       ├── 📁 draft/                 ← WIP narratives (not public)
│       └── 📁 published/             ← released narratives
│           └── 📁 <story_slug>/
│               ├── 📄 story.md
│               └── 📁 assets/
└── 📄 glossary.md                    ← shared terms (if present)
~~~

---

## ✍️ Writing docs in KFM

### 1) Pick exactly one template

Use **exactly one** template, based on what you’re authoring:

- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`  
  For most governed docs (plans, standards, design notes, runbooks, reports).
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`  
  For narrative content destined for Story Nodes / Focus Mode.
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`  
  For adding/changing API endpoints/contracts.

### 2) Fill the YAML front matter completely

- `path:` must match the file location.
- Keep protocol/profile versions aligned with the repo’s standards (update if CI expects different versions).
- Provide stable IDs:
  - `doc_uuid`
  - `semantic_document_id`
  - `event_source_id`
- Do **not** ship with missing governance anchors if the doc has sovereignty/ethics implications.

### 3) Make evidence linkable (and machine-checkable)

Prefer referencing cataloged artifacts rather than raw URLs:
- STAC IDs (collections/items) for geospatial assets
- DCAT dataset IDs for discovery/distributions
- PROV bundles for lineage (raw → work → processed)

If your doc describes a process, include:
- inputs/outputs,
- validation steps,
- where provenance is written,
- expected stable IDs/hashes.

### 4) Domain docs are runbooks (not essays)

When adding a new domain:
- put a concise runbook at `docs/data/<new-domain>/README.md`
- document:
  - sources + licensing
  - ETL steps
  - known limitations / uncertainty
  - governance notes (sensitivity/classification)
  - links to STAC/DCAT/PROV records

---

## 📦 Data & metadata locations (for dataset-facing docs)

Docs that describe or cite datasets should align with the canonical layout:

- `data/raw/<domain>/` → immutable source inputs
- `data/work/<domain>/` → intermediate transforms
- `data/processed/<domain>/` → published / derived outputs

Catalogs / boundary artifacts:
- `data/stac/` → STAC collections/items
- `data/catalog/dcat/` → DCAT datasets (JSON-LD)
- `data/prov/` → PROV lineage bundles

These “boundary artifacts” are required before data is considered fully published.

---

## 🔁 CI / contribution expectations

KFM expects automated validation gates on contributions, including (examples):
- YAML front-matter completeness & validity
- schema validation for STAC/DCAT/PROV and contracts
- provenance completeness checks
- security scans (secrets/sensitive info)

If CI fails, do not “work around” it—update the doc to align with the relevant standard/profile.

---

## 📚 Reference library (non-normative)

The repo root `library/` directory holds PDFs/DOCX used for background rigor. These references **do not override** governed KFM contracts, templates, standards, or governance.

### Suggested library organization

- `library/kfm-core/` — project source documents (technical plan, master docs, architecture, repo ops)
- `library/gis/` — GIS, cartography, geoprocessing, remote sensing
- `library/data-science/` — statistics, regression, Bayesian methods, data mining
- `library/ml-ai/` — neural nets, deep learning, computational agents
- `library/web-ui/` — web design + rendering (WebGL), map APIs
- `library/systems-graphs/` — scalable data mgmt, graph theory/geometry
- `library/shell-devops/` — CLI/bash workflow references

### Reference files currently in the project set (expected under `library/`)

**KFM core (project-facing)**
- Kansas Frontier Matrix – Unified Technical Plan.docx
- Kansas Frontier Matrix (KFM) – Master Documentation.docx
- KFM Architecture Document.pdf
- Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx
- KFM Markdown Guide.docx

**Modeling / simulation / engineering**
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- Generalized Topology Optimization for Structural Design.pdf

**Data science / statistics**
- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf
- regression-analysis-with-python.pdf
- Understanding Statistics & Experimental Design.pdf
- Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf
- Bayesian computational methods.pdf
- graphical-data-analysis-with-r.pdf
- Data Mining Concepts & applictions.pdf

**ML / AI**
- deep-learning-in-python-prerequisites.pdf
- Artificial-neural-networks-an-introduction.pdf
- AI Foundations of Computational Agents 3rd Ed.pdf

**GIS / mapping / remote sensing**
- Geographic Information System Basics - geographic-information-system-basics.pdf
- geoprocessing-with-python.pdf
- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf
- making-maps-a-visual-guide-to-map-design-for-gis.pdf
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
- Google Earth Engine Applications.pdf
- Google Maps API Succinctly - google_maps_api_succinctly.pdf
- google-maps-javascript-api-cookbook.pdf

**Web / visualization**
- responsive-web-design-with-html5-and-css3.pdf
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- Computer Graphics using JAVA 2D & 3D.pdf

**Systems / graphs / scalability**
- Scalable Data Management for Future Hardware.pdf
- Spectral Geometry of Graphs.pdf

**Shell / developer workflow**
- Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf
- clean-architectures-in-python.pdf

> If any file listed above is missing in a given checkout, treat this as the *intended* library contents and reconcile against the actual `library/` directory.

---

## ✅ Definition of done for docs

A doc in `docs/` is considered “done” when:
- YAML front‑matter is complete and valid (template + profiles).
- Any process described has repeatable validation steps.
- Governance/FAIR+CARE/sovereignty implications are stated when relevant.
- Narrative claims (Story Nodes) are evidence-linked to cataloged sources.

---