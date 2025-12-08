---
title: "🤝 Kansas Frontier Matrix — Contribution Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "CONTRIBUTING.md"
version: "v11.1.0"
last_updated: "2025-12-08"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"

sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/contributing-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"

status: "Active / Enforced"
doc_kind: "Governance"
intent: "contributor-workflow"
role: "governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed Dataset Classification"
sensitivity_level: "Contribution-dependent"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

provenance_chain:
  - "CONTRIBUTING.md@v10.3.1"
  - "CONTRIBUTING.md@v10.3.2"
  - "CONTRIBUTING.md@v10.4.1"
  - "CONTRIBUTING.md@v11.0.0"
  - "CONTRIBUTING.md@v11.0.1"
previous_version_hash: "<previous-sha256>"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "schemas/json/contributing-v11.schema.json"
shape_schema_ref: "schemas/shacl/contributing-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:contributing-v11.1.0"
semantic_document_id: "kfm-doc-contributing"
event_source_id: "ledger:CONTRIBUTING.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict controls"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next contributor-guideline update"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contribution Guide**  
`CONTRIBUTING.md`

**A documentation-first, FAIR+CARE-governed, reproducible workflow for contributing to the Kansas Frontier Matrix (KFM).**

[![KFM-MDP v11.2.5](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.5-informational)](docs/standards/kfm_markdown_protocol_v11.2.5.md)  
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  

</div>

---

## 📘 Overview

This guide defines how to contribute to the **Kansas Frontier Matrix (KFM v11)**, a **state-scale, FAIR+CARE-governed knowledge system for Kansas** spanning deep prehistory, historic archives, present-day environments, and speculative futures.

KFM integrates:

- 🗺️ Geospatial data (2D/3D maps, tiles, vectors, rasters, H3 cells)  
- 🧠 AI pipelines & autonomous ETL (deterministic DAGs, MCP-compliant experiments)  
- 📜 Historical archives & newspapers  
- 💧 Environmental, hydrological, and climate models  
- 🏺 Archaeology & cultural landscapes (governed via CARE & sovereignty rules)  
- ⚡ Hazards & infrastructure (tornadoes, floods, wildfire, energy grids, pipelines)  
- 🌿 Ecology & land systems (grasslands, wetlands, species distributions)  
- 📖 Narrative layers (Story Nodes & Focus Mode v3)  

All contributions must align with:

- **MCP-DL v6.3** — documentation-first engineering  
- **KFM-MDP v11.2.5** — Markdown & documentation protocol  
- **KFM-OP v11** — ontology and graph modeling  
- **KFM-PDC v11** — data contracts and validation  
- **STAC, DCAT, PROV-O, GeoSPARQL** — catalog and provenance standards  
- **FAIR+CARE & Indigenous sovereignty** — ethics and governance  

If your change cannot pass these constraints, it cannot merge.

---

## 🗂️ Directory Layout

Canonical **contributor-view** of the monorepo (align this with `README.md`):

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root system overview
├── 📄 ARCHITECTURE.md                   # High-level system & repo architecture
├── 📄 CONTRIBUTING.md                   # This contribution guide
│
├── 📁 .github/                          # CI/CD, security, governance automation
│   ├── 📁 ISSUE_TEMPLATE/               # Issue templates
│   ├── 📁 actions/                      # Composite GitHub Actions
│   ├── 📁 workflows/                    # CI workflows (tests, lint, audits, lineage)
│   ├── 📄 ARCHITECTURE.md              # CI/CD architecture
│   ├── 📄 PULL_REQUEST_TEMPLATE.md     # PR checklist (governance + tests)
│   ├── 📄 README.md                    # .github overview
│   ├── 📄 SECURITY.md                  # Security policy
│   └── 📄 dependabot.yml               # Dependency update rules
│
├── 📁 data/                             # Data lifecycle & catalogs
│   ├── 📁 sources/                      # External dataset manifests (DASC, NOAA, USGS, etc.)
│   ├── 📁 raw/                          # Raw ingests (DVC/LFS-backed)
│   ├── 📁 work/                         # Intermediate / working artifacts
│   ├── 📁 processed/                    # Canonical processed outputs
│   ├── 📁 stac/                         # STAC Collections & Items (spatiotemporal assets)
│   ├── 📁 checksums/                    # Hashes for data integrity
│   ├── 📁 reports/                      # Data QA/QC & summary reports
│   └── 📄 README.md                    # data/ overview
│
├── 📁 docs/                             # Documentation (standards, guides, reports)
│   ├── 📁 standards/                    # KFM standards (Markdown, FAIR+CARE, STAC/DCAT/PROV, etc.)
│   ├── 📁 architecture/                 # System & subsystem designs
│   ├── 📁 guides/                       # How-tos & tutorials
│   ├── 📁 governance/                   # Governance charters & decisions
│   ├── 📁 graph/                        # Ontology & graph modeling docs
│   ├── 📁 history/                      # Historical narratives & timelines
│   ├── 📁 analyses/                     # Analyses & case studies
│   ├── 📁 data/                         # Data catalogs, contracts, and schemas
│   ├── 📁 pipelines/                    # Pipeline specs & runbooks
│   ├── 📁 security/                     # Security & supply-chain docs
│   ├── 📁 telemetry/                    # Telemetry & observability standards
│   ├── 📁 templates/                    # Doc & MCP templates
│   ├── 📁 workflows/                    # Human workflows & process docs
│   ├── 📄 MASTER_GUIDE_v11.md          # v11 master guide
│   ├── 📄 README.md                    # docs/ overview
│   └── 📄 glossary.md                  # Shared terminology
│
├── 📁 mcp/                              # Master Coder Protocol assets
│   ├── 📁 experiments/                  # Experiment logs & configs
│   ├── 📁 model_cards/                  # Model cards for AI/stat models
│   ├── 📁 sops/                         # Standard operating procedures
│   ├── 📄 MCP-README.md                # MCP-specific overview
│   └── 📄 README.md                    # mcp/ overview
│
├── 📁 schemas/                          # JSON, JSON-LD, STAC, DCAT, SHACL, telemetry schemas
│   ├── 📁 json/                         # JSON schemas (docs, pipelines, Story Nodes, telemetry)
│   └── 📁 telemetry/                    # Energy, carbon, lineage, metrics schemas
│
├── 📁 src/                              # Backend, ETL, AI, graph, shared code
│   ├── 📁 pipelines/                    # ETL & orchestration (batch + streaming)
│   ├── 📁 graph/                        # Neo4j schema, loaders, queries
│   ├── 📁 ai/                           # Focus Mode, AI services, workers
│   ├── 📁 map/                          # Map-related helpers
│   ├── 📁 design-tokens/                # Shared design tokens
│   ├── 📁 theming/                      # Shared theming utilities
│   ├── 📁 tests/                        # Backend tests
│   ├── 📄 ARCHITECTURE.md              # src/ architecture
│   └── 📄 README.md                    # src/ overview
│
├── 📁 tests/                            # Cross-cutting tests
│   ├── 📁 fixtures/                     # Shared test fixtures
│   ├── 📄 ARCHITECTURE.md              # tests/ architecture
│   └── 📄 README.md                    # tests/ overview
│
├── 📁 tools/                            # Dev, governance, and validation tools
│   ├── 📁 ai/                           # AI evaluation & drift tools
│   ├── 📁 ci/                           # CI helper scripts/tools
│   ├── 📁 cli/                          # CLI utilities
│   ├── 📁 governance/                   # Governance automation
│   ├── 📁 telemetry/                    # Telemetry/metrics tools
│   ├── 📁 validation/                   # Validators (STAC/DCAT/schemas/Story Nodes)
│   ├── 📄 ARCHITECTURE.md              # tools/ architecture
│   └── 📄 README.md                    # tools/ overview
│
└── 📁 web/                              # Frontend (React + MapLibre + Cesium)
    ├── 📁 public/                       # Static assets
    ├── 📁 src/                          # Components, map/3D, Focus Mode UI
    ├── 📄 ARCHITECTURE.md              # web/ architecture
    └── 📄 README.md                    # web/ overview
~~~

**Directory layout rules (normative):**

- Every directory above **MUST** have (or gain) a `README.md` describing purpose and key files.  
- When you introduce a new top-level directory, update this tree in both `README.md` and `CONTRIBUTING.md`.  
- All directory trees in docs **MUST** use this emoji style (`📁`, `📄`, `🧾`, `🖼️`) and ASCII branches.  
- Directory trees **MUST** be fenced as `~~~text` (or ```text```), not generic code blocks.  

---

## 🧭 Context

### Contribution Types

You can contribute in several ways; all must respect FAIR+CARE, Indigenous sovereignty, and KFM governance:

- **Code**
  - Frontend: React, MapLibre, Cesium, accessibility improvements  
  - Backend: APIs, ETL pipelines, AI services, geospatial processing  
  - Tools: CLI utilities, telemetry exporters, governance automation  

- **Documentation**
  - Standards, protocols, and governance docs under `docs/standards/`  
  - Architecture, pipeline, and Story Node guides  
  - Domain analyses: archaeology, hydrology, history, climate, etc.  

- **Data & Metadata**
  - New datasets (geology, hydrology, climate, biodiversity, archaeology, land records)  
  - STAC/DCAT metadata and PROV-O lineage records  
  - Ontology and graph mappings (CIDOC-CRM, GeoSPARQL, OWL-Time)  

- **Testing & Validation**
  - Unit, integration, and E2E tests  
  - Schema/ontology tests and validators  
  - A11y and UX tests for Story Nodes and Focus Mode  

- **Governance & Ethics**
  - CARE labels and sovereignty metadata for Indigenous and sensitive data  
  - Risk assessments, redaction strategies, and governance process docs  

All contributions must be **documentation-first**, **test-aware**, and **governance-compliant**.

### Branching & Workflow

- **Branch naming**
  - `feature/<short-description>` — new features  
  - `fix/<short-description>` — bug fixes  
  - `docs/<short-description>` — documentation changes  
  - `data/<short-description>` — data/metadata changes  

**Standard workflow:**

1. Branch from `main`.  
2. Implement changes as small, focused commits.  
3. Update docs, schemas, and tests alongside code/data.  
4. Run relevant tests locally.  
5. Open a PR, complete the template, address CI feedback.  

---

## 🧱 Architecture

KFM v11 is a **deterministic ETL → catalogs → graph → API → web** system. Contributions must preserve this separation-of-concerns:

1. **ETL & Pipelines (`src/pipelines/`, `tools/validation/`, `tools/ci/`)**  
   - Implement deterministic ETL/ELT patterns with clear configs and versioned schemas.  
   - Use config files (YAML/JSON) and avoid baking parameters directly into code.  
   - Keep runs replayable: the same config + same input data **MUST** produce the same outputs.  

2. **Catalogs & Provenance (`data/stac/`, `docs/data/`, `schemas/`)**  
   - STAC is the **source of truth** for spatiotemporal assets.  
   - DCAT describes catalogs and dataset series; PROV-O captures lineage.  
   - All new datasets must have:
     - STAC Item(s)/Collection(s)  
     - DCAT Dataset/Distribution entries  
     - PROV Entities/Activities/Agents connecting:
       - Raw sources  
       - Pipelines (ETL scripts, configs)  
       - Derived products  

3. **Graph & Semantics (`src/graph/`, `docs/graph/`)**  
   - Model entities/events/places using KFM-OP v11 (CIDOC-CRM, PROV-O, OWL-Time, GeoSPARQL).  
   - Ensure new nodes/relationships are typed, documented, and provenance-linked.  
   - Changes to the graph schema require:
     - Updated ontology docs  
     - Updated SHACL/validation shapes  
     - Migration notes and tests  

4. **APIs & Frontend (`src/`, `web/`)**  
   - APIs expose graph + STAC/DCAT-backed datasets safely.  
   - Frontend uses React + MapLibre + Cesium to surface maps, timelines, and Story Nodes.  
   - No direct DB access from `web/`: all data must flow through the API.  

If you change architecture, you **must**:

- Update relevant `ARCHITECTURE.md` files.  
- Respect module boundaries (pipelines → catalogs/graph → API → web).  
- Capture changes in CI/CD and governance docs where applicable.  

---

## 🧪 Validation & CI/CD

KFM treats **CI/CD as governance infrastructure**, not just build tooling.

### Local Setup & Baseline Checks

Basic local setup:

~~~bash
git clone https://github.com/<org>/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix

# Backend / pipelines
pip install -r requirements.txt    # or uv/poetry equivalent

# Frontend
cd web
npm install
~~~

Run baseline checks relevant to your change:

~~~bash
# Frontend
cd web
npm run lint
npm test

# Backend / pipelines
cd ..
pytest
~~~

If you modify pipelines, add small deterministic tests for core transforms (no random without fixed seeds).

### CI Expectations

CI will block merges if any of the following fail:

- Code linting (frontend/backend)  
- Markdown lint + schema validation (KFM-MDP v11.2.5)  
- STAC/DCAT/PROV/Story Node/telemetry schema checks for touched artifacts  
- Tests (unit, integration, E2E where defined)  
- FAIR+CARE / sovereignty checks for sensitive data or narratives  
- Security and supply-chain checks (SBOM, manifest, dependency scanning)  

### Pull Request Checklist

Every PR **must**:

- Be scoped and named appropriately (feature/fix/docs/data).  
- Update documentation and front-matter (`version`, `last_updated`, `path`) as needed.  
- Include or update tests where relevant.  
- Pass CI or clearly justify required changes to CI/pipeline.  

If something fails, fix it or explain *why* the check needs an update; do **not** ignore failing checks.

---

## 📦 Data & Metadata

KFM is **catalog-first**, not file-first.

### When adding or modifying datasets, you must provide:

- **Identity**
  - Title, description, keywords  
  - Source, publisher, steward, contact  

- **Licensing & Rights**
  - License (e.g. CC-BY, CC0, MIT)  
  - Access constraints (if any)  
  - CARE/sovereignty labels where relevant  

- **Spatial**
  - CRS, bounding box, resolution  
  - Vertical datum if applicable  

- **Temporal**
  - Time range and resolution  
  - Sampling frequency, known gaps  

- **Catalog & Provenance**
  - STAC Items/Collections under `data/stac/`  
  - DCAT Dataset/Distribution entries under `docs/data/` or relevant catalog docs  
  - PROV Entities/Activities/Agents connecting:
    - Raw sources  
    - Pipelines (ETL scripts, configs)  
    - Derived products  

- **Processing Description**
  - Steps, tools, parameters, and code references  
  - Links to MCP experiment logs if applicable  

### Ensuring Compatibility

- No PII/PHI or ungoverned sensitive content.  
- Licensing must be compatible with repo license and upstream terms.  
- Contracts and validators under `schemas/` and `tests/` must be updated accordingly.  

---

## ⚖ FAIR+CARE & Governance

KFM’s governance integrates FAIR, CARE, and Indigenous data sovereignty:

- **FAIR**
  - *Findable*: Stable IDs, predictable paths, indexed in STAC/DCAT catalogs.  
  - *Accessible*: Open licenses and clear access URLs.  
  - *Interoperable*: Shared ontologies (DCAT, PROV-O, GeoSPARQL, CIDOC-CRM, OWL-Time).  
  - *Reusable*: Explicit versioning, provenance, and quality indicators.  

- **CARE**
  - *Collective Benefit*: Contributions must align with community benefit, not extraction.  
  - *Authority to Control*: Respect tribal governance and sovereignty policies for cultural data.  
  - *Responsibility*: Avoid harm (e.g., revealing sensitive site locations, misrepresenting histories).  
  - *Ethics*: No speculative narratives or misrepresentations about Indigenous communities or other communities of interest.  

**Non-negotiable rules for sensitive data (especially archaeology and heritage):**

- Never commit precise coordinates for sensitive archaeological or sacred sites; apply generalization (e.g. H3, county-level) and masking per heritage standards.  
- Consult FAIR+CARE Council and relevant tribal partners for content touching on cultural heritage, sacred places, or community knowledge.  
- When in doubt, **open an issue or raise it in your PR** rather than guessing.  

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                                                        |
|---------:|------------|--------------------------------------------------------------------------------------------------------------------------------|
| v11.1.0  | 2025-12-08 | Aligned CONTRIBUTING with KFM-MDP v11.2.5; standardized `🗂️ Directory Layout` section; enforced emoji H2 registry; clarified CI/CD, STAC/DCAT/PROV/GeoSPARQL alignment, and FAIR+CARE/sovereignty rules. |
| v11.0.1  | 2025-11-27 | Updated for KFM-MDP v11.2.2, aligned with current repo layout, clarified CI, FAIR+CARE, and a11y expectations.                |
| v11.0.0  | 2025-11-18 | v11 rebuild aligned with KFM-OP v11, KFM-PDC v11, and new governance/telemetry requirements.                                  |
| v10.4.1  | 2025-11-15 | One-box-safe formatting; improved CARE/a11y guidance; stronger governance and telemetry hooks.                                |
| v10.4.0  | 2025-11-15 | Major restructuring of contributor workflow and alignment with v10.4 standards.                                               |
| v10.3.2  | 2025-11-14 | Added governance and telemetry integration details.                                                                           |
| v10.3.1  | 2025-11-13 | Initial CONTRIBUTING framework.                                                                                               |

---

[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)