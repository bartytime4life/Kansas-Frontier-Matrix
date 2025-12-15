---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Overview"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:readme:root:v11.2.6"
semantic_document_id: "kfm-doc-root-overview"
event_source_id: "ledger:README.md"
immutability_status: "version-pinned"

sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

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

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "README.md@v11.2.2"
---

<div align="center">

# 🌌 **Kansas Frontier Matrix (KFM v11)**
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**
### *A Kansas-scale knowledge system for environment, history, culture, AI, and time*

`README.md`

**Purpose**  
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 monorepo:  
how it’s organized, how it fits together (data → catalogs → graph → UI), and how governance keeps it reproducible and safe.

<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/A11y-WCAG_2.1_AA%2B-blueviolet" />

</div>

---

## 📘 Overview

### What KFM is

The **Kansas Frontier Matrix (KFM)** is a **state-scale, multi-domain knowledge platform** for Kansas that supports:

- **Spatiotemporal data integration** (maps, rasters, vectors, time series)
- **Evidence-led knowledge modeling** (entities, places, events, documents, datasets)
- **Reproducible pipelines** (deterministic ETL → validated outputs → versioned releases)
- **Catalog + provenance standards** (STAC / DCAT / PROV)
- **Narrative interfaces** (Story Nodes and Focus Mode on top of governed data)

KFM’s monorepo is intentionally structured so that **data, documentation, schemas, code, tests, tools, and releases** live together with traceable provenance.

### Start here

If you’re new, these are the canonical entry points:

- **System overview:** this file (`README.md`)
- **System architecture:** `ARCHITECTURE.md`
- **Contribution workflow:** `CONTRIBUTING.md`
- **Docs home:** `docs/README.md`
- **Standards:** `docs/standards/`
- **Data lifecycle:** `data/README.md`
- **Frontend app:** `web/README.md`
- **Core backend code:** `src/README.md`
- **Schemas:** `schemas/` (JSON schemas, telemetry schemas)
- **Release packets:** `releases/` (SBOMs, manifests, telemetry, attestations per version)

### Core operating model

KFM v11 is organized around a deterministic flow:

1. **ETL / pipelines** (code + configs) produce normalized artifacts
2. **Catalogs** index those artifacts (STAC + DCAT metadata)
3. **Graph layer** links semantics and provenance (Neo4j + ontology mappings)
4. **API layer** exposes queryable access (when needed; prefer file-first)
5. **UI layer** renders maps + narratives (React + MapLibre + optional 3D)
6. **Story Nodes / Focus Mode** provide governed narrative overlays
7. **CI/CD + governance** enforce safety, reproducibility, and policy compliance

### Licensing note

This README is licensed **CC-BY 4.0**. The repository includes a top-level `LICENSE` file.  
Some parts of the repository may use different licenses (e.g., **MIT for code**) as documented in-project. Always check the relevant license file and module headers before reuse.

---

## 🗂️ Directory Layout

The monorepo’s **main branch** top-level directories and their intended roles:

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md                                  # Root overview (this file)
├── 📄 ARCHITECTURE.md                            # High-level system & repo architecture
├── 📄 CONTRIBUTING.md                            # Contribution workflow (governed)
├── 📄 LICENSE                                    # Project license file (see notes in docs)
│
├── 📁 .github/                                   # GitHub config + CI/CD
│   ├── 📁 ISSUE_TEMPLATE/                        # Issue templates
│   ├── 📁 actions/                               # Reusable composite actions
│   ├── 📁 workflows/                             # CI workflows (lint/tests/audits/build/deploy)
│   ├── 📄 ARCHITECTURE.md                        # CI/CD & GitHub infrastructure architecture
│   ├── 📄 PULL_REQUEST_TEMPLATE.md               # PR checklist (governance + tests)
│   ├── 📄 README.md                              # .github overview
│   ├── 📄 SECURITY.md                            # Security policy
│   └── 🧾 dependabot.yml                          # Dependency update configuration
│
├── 📁 data/                                      # Data lifecycle + catalogs
│   ├── 📁 air-quality/                           # Domain: air quality
│   ├── 📁 hydrology/                             # Domain: hydrology
│   ├── 📁 surficial-geology/                     # Domain: surficial geology
│   ├── 📁 raw/                                   # Raw ingested data (may be DVC/LFS-managed)
│   ├── 📁 work/                                  # Intermediate/working artifacts (staging)
│   ├── 📁 processed/                             # Certified processed outputs (production-ready)
│   ├── 📁 stac/                                  # STAC collections & items (asset metadata)
│   ├── 📁 reports/                               # QA/QC reports and summaries
│   ├── 📁 checksums/                             # Integrity hashes for artifacts
│   ├── 📁 updates/                               # Incremental refresh payloads
│   ├── 📁 archive/                               # Archived / deprecated datasets
│   ├── 📄 ARCHITECTURE.md                        # data/ architecture notes
│   └── 📄 README.md                              # data/ conventions and structure
│
├── 📁 docs/                                      # Documentation (human + machine readable)
│   ├── 📁 accessibility/                         # A11y standards and audit docs
│   ├── 📁 analyses/                              # Domain analyses and case studies
│   ├── 📁 architecture/                          # System/subsystem designs
│   ├── 📁 archives/                              # Historical archives and record docs
│   ├── 📁 data/                                  # Data contracts, catalog notes, schema docs (DCAT)
│   ├── 📁 design/                                # UX/UI and interaction design docs
│   ├── 📁 governance/                            # Governance charters, policies, processes
│   ├── 📁 graph/                                 # Graph/ontology modeling docs (Neo4j, CIDOC, etc.)
│   ├── 📁 guides/                                # How-to guides and tutorials
│   ├── 📁 history/                               # Historical context and timelines
│   ├── 📁 pipelines/                             # Pipeline specs, SOPs, runbooks
│   ├── 📁 reports/                               # Reports and whitepapers
│   ├── 📁 search/                                # Search and indexing behavior docs
│   ├── 📁 security/                              # Security and supply-chain docs
│   ├── 📁 soil/                                  # Soil domain docs
│   ├── 📁 standards/                             # Protocols and standards (KFM-MDP, governance, etc.)
│   ├── 📁 telemetry/                             # Telemetry/observability docs and standards
│   ├── 📁 templates/                             # Canonical templates (docs, SOPs, model cards)
│   ├── 📁 workflows/                             # Human workflows and process docs
│   ├── 📄 ARCHITECTURE.md                        # docs/ architecture overview
│   ├── 📄 MASTER_GUIDE_v10.md                    # Legacy v10 master guide (archival)
│   ├── 📄 MASTER_GUIDE_v11.md                    # v11 master guide (current)
│   ├── 📄 README.md                              # docs/ index
│   └── 📄 glossary.md                            # Shared glossary
│
├── 📁 mcp/                                       # Master Coder Protocol workspace
│   ├── 📁 experiments/                           # Experiment logs (timestamped; reproducible)
│   ├── 📁 model_cards/                           # Model cards (AI/ML/stat models)
│   ├── 📁 sops/                                  # Standard operating procedures
│   ├── 📄 MCP-README.md                          # MCP “bible”
│   └── 📄 README.md                              # mcp/ overview
│
├── 📁 schemas/                                   # Schema definitions
│   ├── 📁 json/                                  # JSON schemas (docs, pipelines, Story Nodes, etc.)
│   └── 📁 telemetry/                             # Telemetry schemas (energy, carbon, lineage, metrics)
│
├── 📁 src/                                       # Backend services + core logic
│   ├── 📁 ai/                                    # AI/Focus Mode logic and services
│   ├── 📁 design-tokens/                         # Design tokens shared with frontend
│   ├── 📁 graph/                                 # Neo4j schema/loaders/queries
│   ├── 📁 icons/                                 # Shared icon assets
│   ├── 📁 map/                                   # Geospatial utilities/helpers
│   ├── 📁 pipelines/                             # ETL and orchestration pipelines
│   ├── 📁 tests/                                 # Backend-local tests
│   ├── 📁 theming/                               # Theming utilities shared with frontend
│   ├── 📄 ARCHITECTURE.md                        # src/ architecture overview
│   └── 📄 README.md                              # src/ overview
│
├── 📁 tests/                                     # Cross-cutting test suites (repo-level)
│   ├── 📁 fixtures/                              # Shared fixtures/sample data
│   ├── 📄 ARCHITECTURE.md                        # Testing strategy
│   └── 📄 README.md                              # tests/ overview
│
├── 📁 tools/                                     # Tooling and utilities
│   ├── 📁 ai/                                    # AI evaluation + drift analysis tools
│   ├── 📁 ci/                                    # CI helper scripts/tools
│   ├── 📁 cli/                                   # Command-line utilities
│   ├── 📁 governance/                            # Governance automation (ledger + compliance)
│   ├── 📁 telemetry/                             # Telemetry aggregation and reporting
│   ├── 📁 validation/                            # STAC/DCAT/schema validators
│   ├── 📄 ARCHITECTURE.md                        # tools/ architecture notes
│   └── 📄 README.md                              # tools/ overview
│
├── 📁 web/                                       # Frontend web app (React + MapLibre + optional 3D)
│   ├── 📁 public/                                # Static assets
│   ├── 📁 src/                                   # Frontend source (UI, map/3D visualization)
│   ├── 📄 ARCHITECTURE.md                        # Frontend architecture
│   └── 📄 README.md                              # web/ overview
│
└── 📁 releases/                                  # Certified release artifacts + provenance
    ├── 📁 v10.2.0/                               # Example legacy release packet(s)
    ├── 📁 v10.4.0/                               # Example legacy release packet(s)
    ├── 📁 v11.0.0/                               # Example v11 release packet(s)
    └── 📁 v11.2.2/                               # Example: SBOM + manifest + system telemetry
~~~

Directory layout rules (repo-wide):

- All directory trees in KFM docs MUST be fenced as `~~~text`.
- Top-level additions MUST be reflected here and in the relevant architectural docs.
- Each major directory SHOULD contain a `README.md` describing purpose and local layout.

---

## 🧭 Context

### Who this repository is for

KFM is designed to support:

- **Researchers** who need reproducible spatiotemporal datasets and traceable provenance
- **Public-facing storytelling** that remains evidence-led and policy compliant
- **Maintainers** who need CI-enforced governance, schemas, and release discipline
- **Developers** building geospatial UI + knowledge graph features under strict contracts

### Branch model (high level)

- `main` is the **stable, governed** branch used for releases.
- `develop` is the **integration** branch where changes are tested before promotion to `main`.
- CI runs on both branches, and promotion follows a **dev → staging → production** model (staging as an environment concept, not necessarily a long-lived git branch).

### Release discipline

The `releases/` directory contains **versioned release packets** (one folder per release). A release packet commonly includes:

- **SBOM** (e.g., `sbom.spdx.json`)
- **Manifest** (e.g., `manifest.zip`)
- **Telemetry** (e.g., `system-telemetry.json`)
- **Attestation/signature artifacts** (when present)

This makes releases verifiable and replayable.

---

## 🧱 Architecture

### System layers

KFM v11 is organized as a set of layers that communicate through **files, catalogs, and governed APIs**:

1. **Data layer** (`data/`)
   - Domain inputs and outputs, staged through `raw/ → work/ → processed/`.
   - Integrity and audit artifacts: `checksums/`, `reports/`, `updates/`.

2. **Pipeline layer** (`src/pipelines/`, `docs/pipelines/`, `tools/validation/`)
   - Deterministic ETL and quality gates.
   - Validators enforce schema correctness and governance constraints before promotion.

3. **Catalog layer** (`data/stac/`, `docs/data/`)
   - STAC collections/items index spatiotemporal assets.
   - DCAT-aligned documentation describes dataset-level identity, licensing, and distributions.

4. **Semantic graph layer** (`src/graph/`, `docs/graph/`)
   - Neo4j schema + loaders + query patterns (ontology-aligned).
   - Links entities (people/places/events/docs/datasets) with provenance relationships.

5. **Experience layer** (`web/`, `docs/design/`, `docs/accessibility/`)
   - React UI using MapLibre for map-first experiences.
   - Optional/roadmapped 3D expansion (where supported), kept behind contracts.

6. **Governance + CI/CD** (`.github/`, `docs/standards/`, `tools/governance/`)
   - Enforces markdown protocol, schema validity, security scanning, and policy compliance.

### High-level pipeline flow

~~~mermaid
flowchart LR
  A[Raw inputs<br/>data/raw] --> B[Normalize + validate<br/>data/work]
  B --> C[Certify outputs<br/>data/processed]
  C --> D[Catalog<br/>data/stac + docs/data]
  D --> E[Graph ingest<br/>src/graph]
  E --> F[UI consumption<br/>web]
  C --> G[Release packet<br/>releases/vX.Y.Z]
  B -->|fails checks| H[Quarantine / review<br/>governance workflow]
~~~

---

## 📦 Data & Metadata

### Data stages (normative)

- `data/raw/` — raw ingests (may be managed via DVC/LFS or external stores)
- `data/work/` — intermediate artifacts, normalization, staging outputs
- `data/processed/` — **certified** outputs used by catalogs, graph ingest, and UI
- `data/updates/` — incremental refresh payloads
- `data/reports/` — QA/QC summaries
- `data/checksums/` — integrity hashes to detect corruption/tampering
- `data/archive/` — deprecated/retired artifacts retained for traceability

### Catalog expectations

KFM treats metadata as a first-class product:

- **STAC** for spatiotemporal assets: vectors, rasters, COGs, tiles, time series
- **DCAT** for dataset-level identity, governance, and distribution metadata
- **PROV-O** for lineage: where it came from, how it was transformed, who approved it

### Promotion gates (expected behavior)

Before a dataset is promoted from `work` → `processed`, the pipeline SHOULD ensure:

- Schema compliance (required fields, CRS correctness, metadata completeness)
- Checksums recorded
- Governance constraints applied (including scanning for sensitive information and restricted content)
- Output artifacts are consistent with catalog requirements (STAC/DCAT fields, licensing, steward)

After promotion, outputs are considered trusted inputs for releases and UI.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (asset-level indexing)

KFM uses STAC to represent **spatiotemporal assets** (raster, vector, tiles, time series):

- `data/stac/` contains STAC Collections and Items describing assets in `data/processed/`
- Each STAC Item SHOULD link to one or more assets (e.g., GeoJSON, GeoTIFF/COG, tiles)
- Temporal indexing enables time navigation in the UI and analysis tooling

### DCAT (dataset-level description)

KFM uses DCAT-aligned documentation to describe datasets at a higher level:

- dataset identity (title, description, steward)
- licensing and distribution links
- update cadence and temporal/spatial coverage

### PROV-O (lineage)

KFM uses PROV-O semantics to describe:

- input sources → transformation activities → output entities
- agents (councils, maintainers, CI) responsible for approvals and validations
- release packets as immutable snapshots tying code + data + telemetry together

---

## 🧠 Story Node & Focus Mode Integration

KFM supports narrative layers that remain **data-grounded**:

- **Story Nodes**: structured narrative artifacts that point to entities, datasets, and spatiotemporal extents
- **Focus Mode**: a governed “lens” that assembles evidence from catalogs and the graph into summaries

Governance expectations:

- Narratives MUST remain evidence-led (no fabrication).
- Sensitive content (especially cultural/heritage data) MUST respect sovereignty policy constraints.
- The UI MUST access the graph through APIs/contracts (no direct graph access from the frontend).

Where to look:

- Story Node docs and patterns: `docs/` (Story Node directories vary by domain)
- Templates: `docs/templates/` and MCP templates under `mcp/`

---

## 🧪 Validation & CI/CD

### What CI checks aim to guarantee

KFM CI is designed to keep the repo:

- **Buildable** (frontend and core tooling)
- **Schema-valid** (JSON schemas, telemetry schemas, STAC/DCAT consistency)
- **Governed** (FAIR+CARE checks and policy enforcement)
- **Secure** (dependency scanning, security policy compliance)
- **Reproducible** (release artifacts and telemetry tracked per version)

CI lives under:

- `.github/workflows/` — workflows (lint, tests, audits, build/deploy)
- `.github/actions/` — reusable composite actions
- `tools/ci/` — helper scripts (where present)
- `tools/validation/` — validators for catalogs and schemas

### Release verification checklist (high level)

A release packet under `releases/vX.Y.Z/` SHOULD include:

- SBOM (SPDX JSON)
- Manifest of outputs
- System telemetry snapshot
- (Optional) signatures/attestations when enabled

This README currently references the **v11.2.2** packet for stable anchors; update refs when the next certified release packet is published.

---

## ⚖ FAIR+CARE & Governance

KFM is governed to reduce harm and ensure long-term reusability:

- **FAIR**: findable identifiers, accessible documentation, interoperable standards, reusable licensing
- **CARE**: collective benefit, authority to control, responsibility, ethics—especially for culturally sensitive data

Key governance anchors:

- Governance charter: `docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE guidance: `docs/standards/faircare/FAIRCARE-GUIDE.md`
- Sovereignty policy: `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

Operationally, governance means:

- Sensitive coordinates and protected site details MUST be masked/generalized.
- Datasets and narratives may require additional review pathways.
- CI is treated as a governance gate, not just a convenience.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Rebuilt root README to reflect the current monorepo main-tree layout (including `schemas/` and `releases/`), expanded architecture description, clarified data lifecycle + release packet discipline, aligned formatting with KFM-MDP v11.2.6. |
| v11.2.2     | 2025-11-28 | Prior root overview baseline and initial main-tree directory layout. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0 (docs)  
See `LICENSE` for repository licensing details.

[📚 Docs Home](docs/README.md) · [📏 Standards](docs/standards/) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>