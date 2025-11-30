---
title: "🤝 Kansas Frontier Matrix — Contribution Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "CONTRIBUTING.md"
version: "v11.0.1"
last_updated: "2025-11-27"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"

sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/contributing-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

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
previous_version_hash: "<previous-sha256>"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "schemas/json/contributing-v11.schema.json"
shape_schema_ref: "schemas/shacl/contributing-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:contributing-v11.0.1"
semantic_document_id: "kfm-doc-contributing"
event_source_id: "ledger:CONTRIBUTING.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict controls"
ai_transform_permissions:
  - "summaries"
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next contributor-guideline update"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contribution Guide**  
`CONTRIBUTING.md`

**A documentation-first, FAIR+CARE-governed, reproducible workflow for contributing to the Kansas Frontier Matrix (KFM).**

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-informational)](docs/standards/kfm_markdown_protocol_v11.2.2.md)  
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  

</div>

---

## 📘 Overview

This guide defines how to contribute to the **Kansas Frontier Matrix (KFM v11)**, a **state-scale, FAIR+CARE-governed knowledge system for Kansas**.

It is aligned with:

- **MCP-DL v6.3** — documentation-first engineering  
- **KFM-MDP v11.2.2** — Markdown and documentation protocol  
- **KFM-OP v11** — ontology and graph modeling protocol  
- **KFM-PDC v11** — data contracts and validation  
- **FAIR+CARE** — data ethics and Indigenous sovereignty  
- **WCAG 2.1 AA** — accessibility baseline  

If your change cannot pass these constraints, it cannot merge.

---

## 🗂 Project Layout (Contributor View)

This is the **canonical v11 contributor view** of the repo, based on the current tree.

~~~text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root system overview
├── 🏗️ ARCHITECTURE.md                   # Repository architecture & system blueprint
├── 🤝 CONTRIBUTING.md                   # This contribution guide
│
├── ⚙️ .github/                          # CI/CD, security, and governance automation
│   ├── 📂 ISSUE_TEMPLATE/               # Issue templates
│   ├── 📂 actions/                      # Composite actions
│   ├── 📂 workflows/                    # CI workflows (tests, lint, audits)
│   ├── 📄 ARCHITECTURE.md              # CI/CD architecture
│   ├── 📄 PULL_REQUEST_TEMPLATE.md     # PR checklist (governance + tests)
│   ├── 📄 README.md                    # .github overview
│   ├── 📄 SECURITY.md                  # Security policy
│   └── 📄 dependabot.yml               # Dependency update rules
│
├── 🗃️ data/                            # Data lifecycle & catalogs
│   ├── 🌫️ air-quality/                 # Air-quality sources & products
│   ├── 🗄️ archive/                     # Archived/deprecated bundles
│   ├── ✅ checksums/                   # Hashes for integrity verification
│   ├── 💧 hydrology/                   # Hydrology datasets
│   ├── 📊 processed/                   # Canonical processed outputs
│   ├── 📥 raw/                         # Raw ingests (DVC/LFS-backed)
│   ├── 📑 reports/                     # QA/QC & data reports
│   ├── 🛰️ stac/                       # STAC Collections & Items
│   ├── 🪨 surficial-geology/           # Surficial geology data
│   ├── 🔁 updates/                     # Incremental refresh payloads
│   ├── 🧪 work/                        # Intermediate working artifacts
│   ├── 🏗️ ARCHITECTURE.md              # Data architecture
│   └── 📄 README.md                    # data/ overview
│
├── 📚 docs/                            # Documentation (standards, guides, reports)
│   ├── ♿ accessibility/               # Accessibility standards & audits
│   ├── 📊 analyses/                    # Analyses & case studies
│   ├── 🧱 architecture/                # System & subsystem designs
│   ├── 🗃️ archives/                    # Historical/archive integration docs
│   ├── 🗂️ data/                        # Data catalogs & contracts
│   ├── 🎨 design/                      # Design system & UX guidelines
│   ├── 🛡️ governance/                  # Governance charters & decisions
│   ├── 🧠 graph/                       # Ontology & graph modeling
│   ├── 📖 guides/                      # How-tos & tutorials
│   ├── 🕰️ history/                     # Historical narratives & timelines
│   ├── 🚰 pipelines/                   # Pipeline specs & runbooks
│   ├── 📑 reports/                     # Reports & whitepapers
│   ├── 🔍 search/                      # Search & discovery behavior
│   ├── 🔒 security/                    # Security & supply-chain docs
│   ├── 🌱 soil/                        # Soil/terrain domain docs
│   ├── ⚖️ standards/                   # KFM standards (Markdown, FAIR+CARE, etc.)
│   ├── 📡 telemetry/                   # Telemetry & observability standards
│   ├── 🧩 templates/                   # Templates for docs/MCP/Story Nodes
│   ├── 🔄 workflows/                   # Human processes & workflows
│   ├── 🏗️ ARCHITECTURE.md              # docs/ architecture
│   ├── 📘 MASTER_GUIDE_v10.md          # v10 master guide
│   ├── 📘 MASTER_GUIDE_v11.md          # v11 master guide
│   ├── 📄 README.md                    # docs/ overview
│   └── 📖 glossary.md                  # Shared terms
│
├── 🧬 mcp/                            # Master Coder Protocol assets
│   ├── 🔬 experiments/                # Experiment logs (inputs, configs, outputs)
│   ├── 🧾 model_cards/                # AI/ML model cards
│   ├── 📜 sops/                       # SOPs for repeatable tasks
│   ├── 📄 MCP-README.md              # MCP-specific overview
│   └── 📄 README.md                  # mcp/ overview
│
├── 🧠 src/                            # Backend, ETL, AI, graph, and shared code
│   ├── 🤖 ai/                         # Focus Mode, AI services, workers
│   ├── 🎨 design-tokens/             # Shared design tokens
│   ├── 🧩 graph/                     # Neo4j schema & loaders
│   ├── 🖼️ icons/                     # Shared icon set
│   ├── 🗺️ map/                       # Map-related helpers
│   ├── 🚰 pipelines/                 # ETL & orchestration logic
│   ├── 🧪 tests/                     # Backend tests
│   ├── 🎨 theming/                   # Shared theming utilities
│   ├── 🏗️ ARCHITECTURE.md            # src/ architecture
│   └── 📄 README.md                  # src/ overview
│
├── 🧪 tests/                         # Cross-cutting tests
│   ├── 🧱 fixtures/                  # Test fixtures
│   ├── 🏗️ ARCHITECTURE.md            # tests/ architecture
│   └── 📄 README.md                  # tests/ overview
│
├── 🛠 tools/                         # Dev, governance, and validation tools
│   ├── 🤖 ai/                        # AI evaluation & drift tools
│   ├── ⚙️ ci/                        # CI support scripts
│   ├── 💻 cli/                       # CLI utilities
│   ├── 🏛️ governance/                # Governance automation
│   ├── 📡 telemetry/                 # Telemetry collection/export tools
│   ├── ✅ validation/                # Validators for STAC/DCAT/schemas/Story Nodes
│   ├── 🏗️ ARCHITECTURE.md            # tools/ architecture
│   └── 📄 README.md                  # tools/ overview
│
└── 🌐 web/                          # Frontend (React + MapLibre + Cesium)
    ├── 📦 public/                   # Static assets
    ├── 🧩 src/                      # Components, map/3D, Focus Mode UI
    ├── 🏗️ ARCHITECTURE.md          # web/ architecture
    └── 📄 README.md                # web/ overview
~~~

When in doubt, place files where they align with this layout and **update this tree** if a new top-level area is introduced.

---

## 🧱 Contribution Types

You can contribute in several ways:

- **Code**
  - Frontend: React, MapLibre, Cesium, accessibility improvements  
  - Backend: FastAPI/GraphQL, ETL, AI services  
  - Pipelines: LangGraph DAGs, data contracts, validation hooks  
  - Tools: CLI, telemetry, governance, validation  

- **Documentation**
  - Standards, protocols, and governance docs  
  - Architecture, pipeline, and Story Node guides  
  - Analyses, reports, and narrative explanations  

- **Data & Metadata**
  - New datasets and derived products  
  - STAC/DCAT metadata and PROV-O lineage  
  - Ontology/graph mappings and constraints  

- **Testing & Validation**
  - Unit, integration, and E2E tests  
  - Schema/ontology tests and validators  
  - A11y and usability tests  

- **Governance & Ethics**
  - CARE labels and sovereignty metadata  
  - Risk assessments and redaction strategies  
  - Governance process documentation  

All contributions must be **documentation-first**, **test-aware**, and **governance-compliant**.

---

## 🛠 Setup & Local Development

### 1. Fork and clone

~~~bash
git clone https://github.com/<org>/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
~~~

### 2. Install dependencies (examples)

~~~bash
# Frontend
cd web
npm install

# Backend / pipelines
cd ..
pip install -r requirements.txt  # or uv/poetry equivalent
~~~

### 3. Run basic checks

~~~bash
# Frontend
cd web
npm run lint
npm test

# Backend
cd ..
pytest
~~~

Refer to `ARCHITECTURE.md` and `docs/architecture/` for precise environment details.

---

## 🌿 Branching & Workflow

### Branch naming

- `feature/<short-description>` — new features  
- `fix/<short-description>` — bug fixes  
- `docs/<short-description>` — documentation-focused changes  
- `data/<short-description>` — data/metadata changes  

### Workflow (simplified)

1. Create a branch from `main`.  
2. Implement changes with small, focused commits.  
3. Update docs, schemas, and tests alongside code.  
4. Run relevant tests and validations.  
5. Open a PR, complete the template, and request review.  

---

## 📥 Pull Request Checklist

Every PR must:

- Target the correct branch and be appropriately scoped.  
- Update relevant documentation (including YAML front-matter dates/versions).  
- Include or update tests where appropriate.  
- Pass CI:

  - Code linting (frontend/backend)  
  - Markdown linting and schema checks  
  - Unit/integration/E2E tests (where defined)  
  - STAC/DCAT/Story Node/telemetry schema validation (if touched)  
  - FAIR+CARE and sovereignty checks for data/narrative changes  
  - Security checks and SBOM/manifest verification when needed  

If something fails, fix it or explain why the check needs to be updated.

---

## ⚖ FAIR+CARE & Sovereignty

Key rules:

- **Never commit precise coordinates** of sensitive archaeological or sacred sites.  
- Use **H3 generalization and masking** as documented in `docs/standards/heritage/` for heritage-related data.  
- Avoid speculative or sensational narratives about Indigenous communities; follow documented sources and governance guidance.  
- When working with any content tied to Indigenous knowledge or sensitive cultural materials, coordinate with the **FAIR+CARE Council** and respect sovereignty policies.  

If you are not sure whether something is sensitive, raise a question in an issue or PR before proceeding.

---

## 🗃 Data & Metadata Contributions

When adding or modifying datasets:

- Provide:

  - Title, description, keywords  
  - Source, publisher, contact  
  - License and usage terms  
  - Spatial extent (bbox, CRS, vertical datum if applicable)  
  - Temporal extent (range and resolution)  
  - STAC Items/Collections for spatial assets  
  - DCAT dataset records  
  - CARE labels, sovereignty flags, and any restrictions  
  - Processing description (steps, tools, parameters)  

- Ensure:

  - Licensing is compatible with KFM’s use (MIT/CC-BY for code/docs).  
  - No PII/PHI or ungoverned sensitive content is introduced.  
  - Data contracts and validators are updated under `schemas/` and `tests/`.  

---

## 🧪 Testing & Validation

Run tests appropriate to the scope of your change:

- **Code:** unit, integration, and (where available) E2E tests.  
- **Schemas:** JSON, JSON-LD, STAC, DCAT, Story Node v3, telemetry.  
- **Docs:** markdown lint, front-matter validation, heading order checks.  
- **A11y:** automated accessibility linting and manual keyboard checks.  

Introduce new tests if your area has no coverage yet—especially for new standards, schemas, or governance rules.

---

## ♿ Accessibility Requirements

All UI work must meet **WCAG 2.1 AA**:

- Full keyboard accessibility and visible focus states  
- Sufficient color contrast and non-color-only cues  
- Semantic HTML structure with appropriate ARIA labels  
- Descriptive alt text for images and icons  
- Respect for `prefers-reduced-motion`  

Document any known limitations or intentional exceptions in the PR and tag accessibility reviewers when appropriate.

---

## 📐 Documentation Standards

All new or updated docs must follow **KFM-MDP v11.2.2**:

- YAML front-matter at the top (no blank lines before `---`).  
- Single H1 in a centered title block.  
- Emojis in H2 headings where appropriate.  
- Directory trees inside `~~~text` fences.  
- Proper heading hierarchy (no jumps from H2 to H4).  
- Three-link footer for governed docs.  

When in doubt, copy an existing v11-compliant doc from `docs/standards/` and adapt.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.0.1 | 2025-11-27 | Updated for KFM-MDP v11.2.2, aligned with current repo layout, clarified CI, FAIR+CARE, and a11y expectations. |
| v11.0.0 | 2025-11-18 | v11 rebuild aligned with KFM-OP v11, KFM-PDC v11, and new governance/telemetry requirements.          |
| v10.4.1 | 2025-11-15 | One-box-safe formatting; improved CARE/a11y guidance; stronger governance and telemetry hooks.        |
| v10.4.0 | 2025-11-15 | Major restructuring of contributor workflow and alignment with v10.4 standards.                       |
| v10.3.2 | 2025-11-14 | Added governance and telemetry integration details.                                                   |
| v10.3.1 | 2025-11-13 | Initial CONTRIBUTING framework.                                                                       |

---

[🏠 Root README](README.md) · [🏗 Architecture](ARCHITECTURE.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)
