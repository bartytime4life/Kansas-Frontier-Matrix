---
title: "MCP Master Coder Protocol"
path: "mcp/README.md"
version: "v0.1.0-draft"
created_date: "2025-12-31"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "guide"
license: "TBD"
markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONT v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v1.0.0"
dcat_profile: "KFM-DCAT v1.0.0"
prov_profile: "KFM-PROV v1.0.0"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "Public · Low-Risk"
sensitivity: "low"
classification: "public"
jurisdiction: "Kansas"
doc_uuid: "urn:kfm:doc:mcp:readme:v0.1.0"
semantic_document_id: "kfm-mcp-readme"
event_source_id: "mcp-readme"
commit_sha: "TBD"
doc_integrity_checksum: "TBD"
ai_transformation_allowed: true
ai_generated_content: "assisted"
human_review_required: true
tags:
  - "mcp"
  - "master-coder-protocol"
  - "reproducibility"
  - "experiments"
  - "runs"
cross_refs:
  - "docs/MASTER_GUIDE_v13.md"
  - "docs/standards/KFM_MARKDOWN_FORMATTING_GUIDE.md"
  - "docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md"
---

# MCP Master Coder Protocol

## 📘 Overview

### Purpose
`mcp/` is the Kansas Frontier Matrix workspace for **protocol-driven, reproducible work**: experiments, runs, and method documentation that can be independently repeated and, when promoted, integrated into KFM’s evidence-first pipeline.

This folder is for:
- Experiment reports and protocol writeups
- Run manifests and repeatable run artifacts
- Templates to standardize experiments and SOPs
- Model cards and analysis notes that support derived data products

### Scope
In KFM terms, MCP outputs are **not “story truth.”** They are *evidence artifacts* that must be treated like any other data product:
- If an output should feed KFM UI or Story Nodes, it must go through the canonical pipeline gates.
- If it stays exploratory, it must still be reproducible and clearly labeled as non-promoted.

### Audience
- KFM contributors running analyses, OCR/NLP, geoprocessing, simulations, or QA audits
- Maintainers reviewing methods, provenance, and promotion readiness
- Researchers extending the system with new modules while preserving governance constraints

### Key invariants
- ✅ Canonical pipeline order is non-negotiable: ETL → Catalog → Knowledge Graph → API → UI → Story Nodes → Focus Mode.
- ✅ “If it’s not in the catalog, it’s not (yet) in KFM.”
- ✅ UI never reads the graph database directly; everything goes through contracted APIs.
- ✅ Any AI/analysis output that becomes part of KFM must be treated as a derived data product with provenance.

## 🗂️ Directory Layout

### Repository context
The Master Guide v13 draft uses emoji formatting for a readable, scan-friendly tree and includes `mcp/` as a first-class workspace.

    📁 repo-root/
    ├── 📁 data/                              # Domain-partitioned data lifecycle
    │   └── 📁 <domain>/                      # e.g. "hydrology/", "historical/"
    │       ├── 📁 raw/                       # Raw source data (read-only)
    │       ├── 📁 work/                      # Intermediate outputs
    │       ├── 📁 processed/                 # Final processed outputs
    │       ├── 📁 mappings/                  # Dataset ↔ STAC/DCAT/PROV mapping notes (optional)
    │       └── 📄 README.md                  # Domain runbook / notes
    ├── 📁 docs/                              # Governed docs: standards, templates, reports
    │   ├── 📄 MASTER_GUIDE_v13.md            # Canonical pipeline & structure (expected)
    │   ├── 📄 glossary.md                    # Shared definitions
    │   ├── 📁 architecture/                  # Blueprints, ADRs, diagrams
    │   ├── 📁 standards/                     # Protocols + profiles
    │   ├── 📁 templates/                     # Governing templates
    │   ├── 📁 governance/                    # ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY, review gates
    │   └── 📁 reports/                       # Story Nodes draft/published workflow
    ├── 📁 mcp/                               # Master Coder Protocol workspace
    ├── 📁 schemas/                           # STAC/DCAT/PROV/StoryNodes/UI/Telemetry schemas
    ├── 📁 src/                               # pipelines/, graph/, server/
    ├── 📁 tests/
    ├── 📁 tools/
    ├── 📁 web/
    ├── 📁 releases/
    ├── 📄 README.md
    ├── 📄 LICENSE
    ├── 📄 CITATION.cff
    ├── 📄 CHANGELOG.md
    ├── 📄 CONTRIBUTING.md
    ├── 📄 SECURITY.md
    └── 📄 docker-compose.yml

### This folder
Minimal structure expected for `mcp/` in the v13 draft layout:

    📁 mcp/
    ├── 📄 README.md                          # This file
    ├── 📁 runs/                              # Repeatable run records (timestamped)
    └── 📁 experiments/                       # Experiment reports + artifacts

Recommended additions inside `mcp/` (optional, add only if your repo uses them):
- `mcp/experiments/_templates/` for experiment report templates
- `mcp/model_cards/` for model cards tied to AI outputs
- `mcp/sops/` for step-by-step standard operating procedures

If your repo already places these elsewhere, keep one canonical home and document it here.

### Naming conventions
- Prefer stable, sortable IDs:
  - Runs: `YYYY-MM-DD__run-####__short_slug/`
  - Experiments: `EXP-####__short_slug/` (or `YYYY-MM-DD__exp-####__short_slug/`)
- Never overwrite run outputs; create a new run ID and link provenance forward.

## 🧭 Context

KFM aims for reproducibility and traceability across all stages. MCP provides the “lab notebook” discipline for experiments and analyses:
- define the question
- document methods before running
- log parameters, environments, and results
- record limitations and next steps

This helps close the gap between architectural intent and practice by ensuring experiments are documented consistently and are promotable through KFM’s normal gates when appropriate.

## 🗺️ Diagrams

MCP is a workspace, not a bypass.

    MCP work (question → method → run → results)
                 │
                 ▼
    ETL → Catalog → Graph → API → UI → Story Nodes → Focus Mode

## 📦 Data & Metadata

### Where experiment outputs go
MCP outputs should not “float around” as ad-hoc files.
Use the data lifecycle conventions:
- Raw inputs remain immutable
- Intermediate results are in work
- Published results go to processed
- Metadata and provenance are written so results are findable and auditable

### Minimum run record
Even in exploratory work, a run should capture:
- run_id
- date/time
- objective
- code ref (commit SHA)
- inputs (paths + IDs)
- parameters (including random seeds)
- environment (tool versions)
- outputs (paths + checksums)
- promotion status (exploratory vs promoted)

If your repo has an existing run-manifest schema, use that instead of inventing a new one.

## 🌐 STAC, DCAT & PROV Alignment

If an MCP output is going to be used in KFM as a dataset:
- Register it in metadata catalogs
- Validate it
- Generate PROV lineage that links inputs → activities → outputs

Catalog records are a gate: no data enters the graph or UI without complete metadata and validation.

## 🧱 Architecture

- Heavy computation should happen in ETL or controlled pipelines, not at query time.
- Treat the API as the system boundary: analysis tools and notebooks should prefer API access patterns when feasible so access control and policy rules are consistently applied.

## 🧠 Story Node & Focus Mode Integration

MCP reports are not Story Nodes.
When an experiment is promoted into narrative use:
- Produce or reference a dataset with catalog IDs
- Ensure Story Nodes cite dataset/document IDs
- Preserve a clear boundary between evidence and narrative

## 🧪 Validation & CI/CD

Before considering an MCP artifact merge-ready:
- ✅ Documentation has complete front-matter where governed docs are required
- ✅ Links resolve
- ✅ Parameters and environment are captured
- ✅ No sensitive locations or restricted data are exposed
- ✅ If promoted: STAC/DCAT/PROV exist and validate; graph/API/UI gates are respected

## ⚖️ FAIR+CARE & Governance

- Keep derived outputs transparent and attributable.
- Do not include precise sensitive locations or culturally sensitive details unless policy permits and review gates are met.
- If any run touches restricted data, mark the run and require human review.

## 🕰️ Version History

| Version | Date       | Summary                                 | Author |
|--------:|------------|------------------------------------------|--------|
| v0.1.0-draft | 2025-12-31 | Initial MCP README with emoji layout and KFM alignment | TBD |

## 📚 Project Reference Library

The following project files form the reference base for MCP experiments, methods, and implementation notes.

### KFM architecture, contracts, and governance workflow
- Kansas Frontier Matrix (KFM) – Master Documentation.docx
- Kansas Frontier Matrix – Unified Technical Plan.docx
- KFM Architecture Document.pdf
- MARKDOWN_GUIDE_v13.md.gdoc
- KFM Markdown Guide.docx
- Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx

### MCP protocol and experiment discipline
- Scientific Method _ Research _ Master Coder Protocol Documentation.pdf
- Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf

### Modeling and simulation
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- Generalized Topology Optimization for Structural Design.pdf
- Spectral Geometry of Graphs.pdf

### Statistics and experimental design
- Understanding Statistics & Experimental Design.pdf
- Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf
- Bayesian computational methods.pdf
- regression-analysis-with-python.pdf
- graphical-data-analysis-with-r.pdf
- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf

### Data management and scalable systems
- Scalable Data Management for Future Hardware.pdf

### AI and machine learning foundations
- AI Foundations of Computational Agents 3rd Ed.pdf
- Artificial-neural-networks-an-introduction.pdf
- deep-learning-in-python-prerequisites.pdf
- Data Mining Concepts & applictions.pdf

### Geospatial data processing and cartography
- Geographic Information System Basics - geographic-information-system-basics.pdf
- geoprocessing-with-python.pdf
- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf
- making-maps-a-visual-guide-to-map-design-for-gis.pdf
- Google Earth Engine Applications.pdf
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
- Google Maps API Succinctly - google_maps_api_succinctly.pdf
- google-maps-javascript-api-cookbook.pdf

### UI, graphics, and visualization
- responsive-web-design-with-html5-and-css3.pdf
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- Computer Graphics using JAVA 2D & 3D.pdf

### Command line and workflows
- Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf

### Navigation and field reference
- Map Reading & Land Navigation