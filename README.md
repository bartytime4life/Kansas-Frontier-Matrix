---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:readme:root:v11.2.2"
semantic_document_id: "kfm-doc-root-overview"
event_source_id: "ledger:README.md"
immutability_status: "version-pinned"

sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "kfm-root-overview"
lifecycle_stage: "stable"

fair_category: "F1-A1-I2-R3"
care_label: "Mixed / Multi-Domain"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded by KFM v12 Root Overview"
---

<div align="center">

# 🌌 **Kansas Frontier Matrix (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *A State-Scale Knowledge System for Kansas — Environment, History, Culture, AI, and Time*  

`README.md`

**Purpose**  
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 — a fully-governed, reproducible, state-scale knowledge system unifying environment, history, culture, AI, and time into one coherent, semantic geospatial platform.

</div>

---

## 🗂️ Directory Layout

~~~text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root overview (this file)
├── 📄 ARCHITECTURE.md                   # High-level system & repo architecture
├── 📄 CONTRIBUTING.md                   # Contribution guidelines & workflow
│
├── 📂 .github/                          # CI/CD, security, issue/workflow config
│   ├── 📂 ISSUE_TEMPLATE/               # Issue templates
│   ├── 📂 actions/                      # Reusable composite actions
│   ├── 📂 workflows/                    # CI workflows (lint, build, tests, audits)
│   ├── 📄 ARCHITECTURE.md              # GitHub infra design
│   ├── 📄 PULL_REQUEST_TEMPLATE.md     # PR template
│   ├── 📄 README.md                    # .github overview
│   ├── 📄 SECURITY.md                  # Security policy
│   └── 📄 dependabot.yml               # Dependency update rules
│
├── 📂 data/                             # Data lifecycle & catalogs
│   ├── 📂 air-quality/                  # Air quality sources & products
│   ├── 📂 archive/                      # Archived / deprecated datasets
│   ├── 📂 checksums/                    # Hashes for data integrity
│   ├── 📂 hydrology/                    # Hydrology-related datasets & configs
│   ├── 📂 processed/                    # Canonical processed outputs
│   ├── 📂 raw/                          # Raw ingests (DVC/LFS-backed)
│   ├── 📂 reports/                      # Data QA/QC & summary reports
│   ├── 📂 stac/                         # STAC Collections & Items
│   ├── 📂 surficial-geology/            # Surficial geology products
│   ├── 📂 updates/                      # Incremental refresh payloads
│   ├── 📂 work/                         # Intermediate / working artifacts
│   ├── 📄 ARCHITECTURE.md              # Data architecture notes
│   └── 📄 README.md                    # Data tree overview
│
├── 📂 docs/                             # Human- & machine-readable documentation
│   ├── 📂 accessibility/                # A11y rules & audits
│   ├── 📂 analyses/                     # Domain analyses & case studies
│   ├── 📂 architecture/                 # System & subsystem designs
│   ├── 📂 archives/                     # Historical/archives documentation
│   ├── 📂 data/                         # Data contracts, catalogs, schemas
│   ├── 📂 design/                       # UX, UI, visual & interaction design
│   ├── 📂 governance/                   # Governance charters, processes
│   ├── 📂 graph/                        # Graph/ontology documentation
│   ├── 📂 guides/                       # How-to guides & tutorials
│   ├── 📂 history/                      # Historical context & timelines
│   ├── 📂 pipelines/                    # Pipeline specs, SOPs, runbooks
│   ├── 📂 reports/                      # Generated reports & whitepapers
│   ├── 📂 search/                       # Search/indexing behavior docs
│   ├── 📂 security/                     # Security, supply-chain, hardening
│   ├── 📂 soil/                         # Soil/terrain domain docs
│   ├── 📂 standards/                    # Protocols (KFM-MDP, FAIR+CARE, etc.)
│   ├── 📂 telemetry/                    # Telemetry & observability standards
│   ├── 📂 templates/                    # Doc & MCP templates
│   ├── 📂 workflows/                    # Human workflows & process docs
│   ├── 📄 ARCHITECTURE.md              # Docs architecture
│   ├── 📄 MASTER_GUIDE_v10.md          # Legacy v10 master guide
│   ├── 📄 MASTER_GUIDE_v11.md          # v11 master guide
│   ├── 📄 README.md                    # Docs overview
│   └── 📄 glossary.md                  # Shared terminology
│
├── 📂 mcp/                              # Master Coder Protocol assets
│   ├── 📂 experiments/                  # Experiment logs & configs
│   ├── 📂 model_cards/                  # Model cards for AI/stat models
│   ├── 📂 sops/                         # Standard operating procedures
│   ├── 📄 MCP-README.md                # MCP-specific overview
│   └── 📄 README.md                    # MCP root overview
│
├── 📂 src/                              # Backend & service code
│   ├── 📂 ai/                           # AI/ML logic & Focus Mode services
│   ├── 📂 design-tokens/                # Design tokens shared with web
│   ├── 📂 graph/                        # Neo4j schema, loaders, queries
│   ├── 📂 icons/                        # Shared icon assets
│   ├── 📂 map/                          # Map-centric backend helpers
│   ├── 📂 pipelines/                    # ETL & orchestration pipelines
│   ├── 📂 tests/                        # Backend-focused tests
│   ├── 📂 theming/                      # Theming helpers shared with web
│   ├── 📄 ARCHITECTURE.md              # Backend architecture
│   └── 📄 README.md                    # src overview
│
├── 📂 tests/                            # Cross-cutting test harnesses
│   ├── 📂 fixtures/                     # Shared test fixtures
│   ├── 📄 ARCHITECTURE.md              # Test architecture & strategy
│   └── 📄 README.md                    # tests overview
│
├── 📂 tools/                            # Tooling & maintenance utilities
│   ├── 📂 ai/                           # AI-related tools (eval, drift, etc.)
│   ├── 📂 ci/                           # CI helper scripts/tools
│   ├── 📂 cli/                          # Command-line utilities
│   ├── 📂 governance/                   # Governance automation tools
│   ├── 📂 telemetry/                    # Telemetry/metrics tools
│   ├── 📂 validation/                   # Validators (STAC/DCAT, schemas, etc.)
│   ├── 📄 ARCHITECTURE.md              # Tools architecture
│   └── 📄 README.md                    # tools overview
│
└── 🌐 web/                              # Frontend (React + MapLibre + Cesium)
    ├── 📂 public/                       # Static assets
    ├── 📂 src/                          # App code (UI, maps, Focus Mode)
    ├── 📄 ARCHITECTURE.md              # Web architecture
    └── 📄 README.md                    # web overview
~~~

Author rules:

- Each directory shown MUST have (or gain) a `README.md` with local layout and purpose.  
- New top-level directories MUST be added here with emoji + concise description.  
- All directory layouts MUST use `~~~text` fences (no nested backtick fences).

---

## 📘 Overview

The **Kansas Frontier Matrix (KFM)** is a unified, multi-layer, multi-epoch knowledge system integrating:

- 🗺️ Geospatial data (2D/3D maps, tiles, vectors, rasters, H3 cells)  
- 🧠 AI pipelines & autonomous ETL (LangGraph DAGs, CrewAI workers, MLOps)  
- 📜 Historical archives & newspapers (Kansas Memory, Chronicling America, etc.)  
- 💧 Environmental & hydrological models (climate, rivers, groundwater, drought)  
- 🏺 Archaeology & cultural landscapes (masked under CARE and sovereignty rules)  
- ⚡ Hazards & infrastructure (tornadoes, floods, wildfire, energy grids, pipelines)  
- 🌿 Ecology & land systems (grasslands, wetlands, species distributions)  
- 📖 Narrative layers (Story Nodes & Focus Mode v3)  

Everything is wired through a **Neo4j knowledge graph**, governed by:

- Ontologies: **CIDOC-CRM · GeoSPARQL · OWL-Time · PROV-O · ISO 19115**  
- Catalogs: **STAC 1.x · DCAT 3.0 · CF conventions**  
- Protocols: **KFM-MDP v11.2.2 · MCP-DL v6.3 · KFM-OP v11 · KFM-PDC v11**  
- Ethics: **FAIR+CARE · Indigenous Data Sovereignty**  

---

## 🧱 Architecture

KFM v11 is structured as a deterministic, provenance-rich stack:

1. **Data & Storage**  
   - `data/` with raw → work → processed → releases, plus STAC, checksums, and provenance.  

2. **Pipelines & AI**  
   - `src/pipelines/` + `tools/ci/`, `tools/validation/` implementing LangGraph DAG ETL, schema checks, and OpenLineage emission.  

3. **Graph & Semantics**  
   - `src/graph/` and `docs/graph/` define Neo4j schema, CIDOC-CRM/GeoSPARQL mappings, and PROV-O integration.  

4. **APIs & Services**  
   - `src/` server components expose FastAPI/GraphQL endpoints for map layers, graph queries, and Focus Mode.  

5. **Frontend Experience**  
   - `web/` hosts React + MapLibre + Cesium apps, with shared design tokens and theming from `src/design-tokens/` and `src/theming/`.  

6. **Governance & CI/CD**  
   - `.github/` workflows and `tools/governance/` enforce security, FAIR+CARE, STAC/DCAT validity, and markdown protocol compliance.  

All layers are **replayable** and **lineage-tracked** via PROV-O and telemetry.

---

## 📦 Data & Metadata

KFM data is cataloged and governed as follows:

- **STAC** in `data/stac/` for spatiotemporal assets (rasters, vectors, tiles).  
- **DCAT** in `docs/data/` and `data/releases/` for dataset-level metadata.  
- **PROV-O** in `data/provenance/` for dataset, pipeline, and model lineage.  
- **Checksums** in `data/checksums/` for integrity verification.  

Every production dataset MUST declare:

- Identity: title, description, version, license, steward.  
- Spatial: CRS, bbox, resolution, vertical datum (if applicable).  
- Temporal: `datetime` or interval, sampling frequency, known gaps.  
- Lineage: sources, processing steps, parameters, and code references.  
- FAIR+CARE & sovereignty attributes where culturally or ecologically sensitive.

---

## 🧠 Story Node & Focus Mode Integration

KFM v11 uses **Story Nodes** (v3 schema) and **Focus Mode** as a core narrative layer:

- Story Nodes live in JSON and bind:
  - `spacetime.geometry` (points, polygons, H3 cells)  
  - `spacetime.when` (instant or interval)  
  - narrative text  
  - links to graph entities (places, events, datasets, documents)  

- Focus Mode v3:
  - Accepts a focus target (entity, dataset, Story Node).  
  - Retrieves the two-hop neighborhood from Neo4j, plus STAC/DCAT links.  
  - Generates strictly data-grounded narratives under governance rules.  

Sensitive archaeological or cultural content is generalized (H3) or suppressed according to:

- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/heritage/` (dynamic H3 generalization and masking)  
- `docs/governance/` sovereignty policies  

---

## ⚖ FAIR+CARE & Governance

KFM operates under explicit governance:

- **FAIR+CARE Council** — data ethics, Indigenous data sovereignty, community benefit.  
- **Architecture Board** — technical decisions, performance, and reliability.  
- **Data & Heritage Working Groups** — domain expertise and risk review.  
- **AI Safety & Narrative Governance Board** — AI behavior, Focus Mode, Story Nodes.  

CI/CD workflows enforce:

- Markdown protocol (KFM-MDP v11.2.2)  
- Schema validity (STAC, DCAT, JSON-LD, Story Node, telemetry)  
- FAIR+CARE & sovereignty checks (especially for archaeology and archives)  
- Security & supply-chain constraints (SBOMs, dependency scanning)  

Nothing ships to `data/releases/` without passing these gates.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                             |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Expanded two-level directory layout, aligned with current repo, tightened architecture & governance integration.    |
| v11.1.2 | 2025-11-27 | Previous v11 root overview with initial digital twin framing and multi-domain scope.                               |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
