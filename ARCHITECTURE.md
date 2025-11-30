---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Full v10.x → v11.x compatibility"
commit_sha: "<latest-commit-hash>"

signature_ref: "releases/v11.2.2/signature.sig"
attestation_ref: "releases/v11.2.2/slsa-attestation.json"
sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/root-architecture-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High Governance · Requires Full Provenance · Auto-Masked Sensitive Data"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "repository-architecture"
category: "System Architecture · Repository Design · Global Dataflow"
sensitivity: "General (non-sensitive, but applies masking to protected datasets)"
prov_profile: "PROV-O Core + KFM Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"

ontology_ref:
  - "docs/graph/ontology/core-entities.md"
  - "docs/graph/ontology/cidoc-crm-mapping.md"
  - "docs/graph/ontology/spatial-temporal-patterns.md"

metadata_profiles:
  - "schemas/stac/kfm-stac-v11.json"
  - "schemas/dcat/kfm-dcat-v11.json"
  - "schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "KFM Multi-Cloud Mesh (AWS + GCP + On-Prem)"
  graph_engine: "Neo4j Enterprise v5.x Cluster"
  api_stack: "FastAPI + GraphQL Gateway (GovHooks v4)"
  frontend_stack: "React · MapLibre · Cesium · Vite Build"
  lineage_bus: "OpenLineage v2.5"
  reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"
  agents: "LangGraph Autonomous Updater v11"

fair_category: "F1-A1-I1-R1"
sensitivity_level: "Low"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "schemas/json/root-architecture-v11.schema.json"
shape_schema_ref: "schemas/shacl/root-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:architecture:repository:v11.2.2"
semantic_document_id: "kfm-repository-architecture"
event_source_id: "ledger:ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified architectural claims"
  - "modifying normative requirements"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major architecture and repository redesign"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix**  
## **Repository Architecture & System Blueprint (v11 LTS)**  
`ARCHITECTURE.md`  

[📘 Docs – MCP v6.3](docs/README.md) · [⚖️ FAIR+CARE](docs/standards/faircare/FAIRCARE-GUIDE.md) · [📜 License: MIT](LICENSE) · [📦 SBOM](releases/v11.2.2/sbom.spdx.json) · [📊 Telemetry](releases/v11.2.2/focus-telemetry.json)

</div>

---

## 📘 Overview

The **Kansas Frontier Matrix (KFM v11)** is a monorepo that implements a **state-scale, FAIR+CARE-governed knowledge system for Kansas**. It integrates:

- 🗺️ Geospatial layers (2D/3D maps, rasters, vectors, H3)  
- 💧 Environmental & hydrological chronologies  
- 🌿 Ecology & land systems  
- 🏺 Archaeology & cultural landscapes (masked and generalized)  
- 📜 Historic archives, newspapers, and documents  
- ⚡ Hazards & infrastructure (storms, floods, drought, wildfire, energy)  
- 🧠 AI-assisted ETL, predictive modeling, and narrative generation  
- 📖 Story Nodes & Focus Mode v3 narrative overlays  

This document describes **how the repository is structured**, **how data flows end-to-end**, and **how CI/CD, governance, and runtime components fit together**.

---

## 🗂️ Directory Layout

The layout below is **grounded in the current repository** (two levels deep where applicable) and is the canonical v11 architecture view.

~~~text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root overview
├── 🏗️ ARCHITECTURE.md                   # Repository & system architecture (this file)
├── 📄 CONTRIBUTING.md                   # Contribution workflow and rules
│
├── ⚙️ .github/                          # CI/CD, issues, and repo automation
│   ├── 📂 ISSUE_TEMPLATE/               # GitHub issue templates
│   ├── 📂 actions/                      # Composite actions (shared CI logic)
│   ├── 📂 workflows/                    # CI workflows (tests, lint, build, audits)
│   ├── 📄 ARCHITECTURE.md              # GitHub infra architecture
│   ├── 📄 PULL_REQUEST_TEMPLATE.md     # PR template including governance checklist
│   ├── 📄 README.md                    # .github overview
│   ├── 📄 SECURITY.md                  # Security policy and disclosure process
│   └── 📄 dependabot.yml               # Automated dependency updates
│
├── 🗃️ data/                            # Data lifecycle & catalogs
│   ├── 🌫️ air-quality/                 # Air quality datasets and configs
│   ├── 🗄️ archive/                     # Archived/deprecated data bundles
│   ├── ✅ checksums/                   # Hashes for integrity verification
│   ├── 💧 hydrology/                   # Hydrology-related data & subcatalogs
│   ├── 📊 processed/                   # Canonical processed outputs
│   ├── 📥 raw/                         # Raw ingests (DVC/LFS-backed, not committed directly)
│   ├── 📑 reports/                     # QA/QC, validation, and summary reports
│   ├── 🛰️ stac/                       # STAC Collections & Items (KFM-STAC v11)
│   ├── 🪨 surficial-geology/           # Surficial geology datasets
│   ├── 🔁 updates/                     # Incremental refresh payloads & deltas
│   ├── 🧪 work/                        # Intermediate working artifacts
│   ├── 🏗️ ARCHITECTURE.md              # Data architecture details
│   └── 📄 README.md                    # data/ overview
│
├── 📚 docs/                            # Documentation (user, developer, governance)
│   ├── ♿ accessibility/               # A11y guidelines, audits, and reports
│   ├── 📊 analyses/                    # Analytic writeups, case studies
│   ├── 🧱 architecture/                # Deep dives into subsystems & patterns
│   ├── 🗃️ archives/                    # Guidance on archival sources & integration
│   ├── 🗂️ data/                        # Data catalogs, DCAT, contracts, and schemas
│   ├── 🎨 design/                      # UX, UI, design systems, visual language
│   ├── 🛡️ governance/                  # Councils, processes, decision logs
│   ├── 🧠 graph/                       # Ontology, schema, and graph modeling docs
│   ├── 📖 guides/                      # How-tos, tutorials, onboarding guides
│   ├── 🕰️ history/                     # Historical narratives and timelines
│   ├── 🚰 pipelines/                   # Pipeline specs, diagrams, and SOP links
│   ├── 📑 reports/                     # Strategic or research reports
│   ├── 🔍 search/                      # Search/indexing/knowledge-discovery docs
│   ├── 🔒 security/                    # Security hardening and supply-chain docs
│   ├── 🌱 soil/                        # Soil/terrain/geomorphology domain docs
│   ├── ⚖️ standards/                   # Protocols (Markdown, STAC, DCAT, FAIR+CARE, etc.)
│   ├── 📡 telemetry/                   # Telemetry, metrics, and observability standards
│   ├── 🧩 templates/                   # Doc, MCP, Story Node, and pipeline templates
│   ├── 🔄 workflows/                   # Human workflows (runbooks, reviews)
│   ├── 🏗️ ARCHITECTURE.md              # Docs architecture
│   ├── 📘 MASTER_GUIDE_v10.md          # v10 master guide
│   ├── 📘 MASTER_GUIDE_v11.md          # v11 master guide
│   ├── 📄 README.md                    # docs/ overview
│   └── 📖 glossary.md                  # Cross-project glossary
│
├── 🧬 mcp/                            # Master Coder Protocol (documentation-first)
│   ├── 🔬 experiments/                # Experiment logs (ETL, AI, modeling)
│   ├── 🧾 model_cards/                # Model cards for AI/statistical models
│   ├── 📜 sops/                       # Standard operating procedures
│   ├── 📄 MCP-README.md              # MCP-specific overview
│   └── 📄 README.md                  # mcp/ overview
│
├── 🧠 src/                            # Backend/ETL/AI/graph code
│   ├── 🤖 ai/                         # AI services, Focus logic, model runners
│   ├── 🎨 design-tokens/             # Design tokens shared with web
│   ├── 🧩 graph/                     # Neo4j schema, loaders, queries
│   ├── 🖼️ icons/                     # Shared icon assets
│   ├── 🗺️ map/                       # Map-related backend helpers
│   ├── 🚰 pipelines/                 # ETL, transformation, orchestration code
│   ├── 🧪 tests/                     # Backend-focused tests
│   ├── 🎨 theming/                   # Theming logic shared with frontend
│   ├── 🏗️ ARCHITECTURE.md            # Backend architecture
│   └── 📄 README.md                  # src/ overview
│
├── 🧪 tests/                         # Cross-cutting tests
│   ├── 🧱 fixtures/                  # Shared test fixtures
│   ├── 🏗️ ARCHITECTURE.md            # Testing strategy & architecture
│   └── 📄 README.md                  # tests/ overview
│
├── 🛠 tools/                         # Utility scripts and operational tools
│   ├── 🤖 ai/                        # AI evaluation, bias/drift check tools
│   ├── ⚙️ ci/                        # CI helper scripts
│   ├── 💻 cli/                       # Command-line tooling
│   ├── 🏛️ governance/                # Governance automation tools
│   ├── 📡 telemetry/                 # Telemetry collection & export tools
│   ├── ✅ validation/                # Validators for STAC/DCAT/schemas/Story Nodes
│   ├── 🏗️ ARCHITECTURE.md            # tools/ architecture
│   └── 📄 README.md                  # tools/ overview
│
└── 🌐 web/                          # Frontend (React + MapLibre + Cesium)
    ├── 📦 public/                   # Static assets
    ├── 🧩 src/                      # App code: pages, map/3D, Focus Mode UI
    ├── 🏗️ ARCHITECTURE.md          # Web/front-end architecture
    └── 📄 README.md                # web/ overview
~~~

Author note: any new top-level or key second-level directory MUST be added here, with a short comment and emoji.

---

## 🧱 Architecture

KFM v11 follows a **layered system architecture**:

1. **Data Layer (data/)**  
   - Manages the lifecycle from raw → work → processed → releases.  
   - Uses STAC/DCAT/PROV-O to expose datasets as cataloged, provenance-rich entities.  

2. **Pipeline & AI Layer (src/pipelines/, src/ai/, tools/)**  
   - Pipelines defined as LangGraph DAGs with explicit configs and contracts.  
   - AI agents (LangGraph Autonomous Updater v11) orchestrate governed refresh cycles.  
   - Reliable Pipelines v11 provide WAL, retries, rollbacks, and hotfix paths.  

3. **Knowledge Graph Layer (src/graph/, docs/graph/)**  
   - Neo4j schema aligned with CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O, and KFM-OP v11.  
   - Graph is the semantic backbone linking places, events, datasets, Story Nodes, and agents.  

4. **API & Service Layer (src/server/, future service subdirs)**  
   - FastAPI + GraphQL Gateway (GovHooks v4) exposes privileged, governed access.  
   - GovHooks enforce permissions, CARE masking, lineage logging, and auditability.  

5. **Frontend Layer (web/, src/design-tokens/, src/theming/)**  
   - React + MapLibre + Cesium provide 2D/3D visualization, timelines, and Focus Mode v3 UI.  
   - Shared design tokens and theming ensure consistent styling across clients.  

6. **Governance & CI/CD Layer (.github/, tools/governance/, docs/governance/)**  
   - CI workflows perform linting, schema validation, FAIR+CARE checks, security audits, and telemetry export.  
   - Governance docs and tools codify council decisions and enforcement rules.

---

## 📦 Data & Metadata

The repository enforces **metadata-first data management**:

- STAC (KFM-STAC v11) profiles describe geospatial assets in `data/stac/`.  
- DCAT (KFM-DCAT v11) profiles define dataset-level records in `docs/data/` and `data/releases/`.  
- JSON-LD contexts and SHACL shapes define machine-readable structures.  
- PROV-O and OpenLineage capture lineage at design-time and runtime.

Every production dataset MUST:

- Conform to its **data contract** (KFM-PDC v11.0).  
- Include spatial and temporal extents, CRS, vertical datum, and units.  
- Declare license, steward, FAIR+CARE category, sovereignty flags, and masking policies.  

---

## 🧠 Story Node & Focus Mode Integration

Architecture is explicitly designed to support:

- **Story Nodes v3** — JSON objects binding:
  - `spacetime.geometry` (GeoJSON/H3)  
  - `spacetime.when` (OWL-Time-aligned instants/intervals)  
  - narrative text  
  - links to graph entities (Place, Event, Dataset, Document, Agent)  

- **Focus Mode v3** — UI and service layer that:
  - Accepts a focus target (graph entity or Story Node).  
  - Pulls a two-hop neighborhood from Neo4j plus relevant STAC/DCAT entries.  
  - Generates narratives under strict AI transform permissions and governance.  

The repository organizes all related code and docs so that narratives are **reproducible, explainable, and grounded in the graph and catalogs**.

---

## 🧪 Validation & CI/CD

CI/CD (`.github/workflows/kfm-ci.yml`) enforces:

- `docs-lint-v11` — Markdown rules (KFM-MDP v11.2.2) and accessibility basics.  
- `schema-lint-v11` — JSON/JSON-LD/STAC/DCAT/Story Node/telemetry schema validation.  
- `lineage-audit-v11` — Ensures coverage of PROV-O/OpenLineage events for pipelines.  
- `governance-audit-v11` — FAIR+CARE, sovereignty, and license checks.  

No change may reach production branches unless:

- Code + docs are consistent.  
- Data contracts are satisfied.  
- FAIR+CARE and sovereignty constraints are respected.  
- Telemetry, SBOM, and manifests are updated for the release.

---

## ⚖ FAIR+CARE & Governance

This architecture document itself is a **governed plan (prov:Plan, E29 Design or Procedure)**:

- FAIR+CARE is embedded via metadata, directories, and CI checks.  
- Indigenous rights and sovereignty are enforced via the sovereignty policy and masking/aggregation behaviors baked into ETL and frontend layers.  
- High-risk content (e.g., archaeological site locations) is always passed through **H3 aggregation + CARE filters** before public exposure.  

Governance bodies (FAIR+CARE Council, Architecture Board, AI Safety Board) use this document as the **authoritative map** for:

- Approving new subsystems.  
- Evaluating risk and compliance.  
- Auditing lineage and telemetry.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                              |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Aligned with root README directory tree, enforced KFM-MDP v11.2.2 headings, clarified CI/governance integration.    |
| v11.1.1 | 2025-11-27 | Refined runtime, validation, and provenance profiles; strengthened FAIR+CARE hooks in CI.                           |
| v11.1.0 | 2025-11-27 | Updated for KFM-STAC/DCAT v11 and ontology alignment; documented repository responsibilities by layer.              |
| v11.0.1 | 2025-11-23 | Expanded runtime description (LangGraph + OpenLineage + reliability engine); clarified monorepo layout philosophy.  |
| v11.0.0 | 2025-11-19 | Established v11 LTS repository architecture; defined dataflow, graph role, and governance integration.             |

---

<div align="center">

🏗️ **Kansas Frontier Matrix — Repository Architecture (v11.2.2)**  
Documentation-First · FAIR+CARE · Provenance-Aware  

[⬅️ Root Overview](README.md) · [📚 Docs Home](docs/README.md) · [🛡️ Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
