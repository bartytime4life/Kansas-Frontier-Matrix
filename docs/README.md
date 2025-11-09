---
title: "📚 Kansas Frontier Matrix — Documentation Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../releases/v10.0.0/manifest.zip"
telemetry_ref: "../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-index-v1.json"
governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation Index**  
`docs/README.md`

**Purpose:**  
Provide the **central navigation hub** for all Kansas Frontier Matrix (KFM) documentation — standards, workflows, governance, AI systems, pipelines, datasets, and developer guides — maintained under **MCP-DL v6.3**, **FAIR+CARE**, and **ISO 19115** alignment.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../releases/)
</div>

---

## 📘 Overview

The **Kansas Frontier Matrix (KFM)** documentation ecosystem serves as a **living, interoperable knowledge graph**.  
Each Markdown file includes YAML front-matter enabling **automated validation**, **telemetry tracking**, and **provenance auditing**.

Aligned frameworks:
- **Master Coder Protocol (MCP-DL v6.3)**  
- **FAIR+CARE Governance**  
- **Platinum README Template v7.1**  
- **ISO 19115**, **DCAT 3.0**, and **CIDOC CRM**  

---

## 🗂️ Directory Layout

```plaintext
docs/
├── README.md                          # Central documentation index
├── glossary.md                        # Glossary of technical, governance, and domain terms
│
├── architecture/                      # Architecture, systems, and design docs
│   ├── data-architecture.md           # Data model, STAC/DCAT schemas, and ontologies
│   ├── web-ui.md                      # Frontend structure, components, accessibility
│   ├── github-architecture.md         # CI/CD and automation architecture
│   └── api-architecture.md            # API and knowledge graph integration (v10.0.0)
│
├── standards/                         # FAIR+CARE, governance, compliance, and style rules
│   ├── faircare.md                    # FAIR+CARE ethical framework
│   ├── markdown_rules.md              # Platinum README compliance rules
│   ├── markdown_guide.md              # Style guide and formatting conventions
│   ├── ui_accessibility.md            # WCAG 2.1 AA + inclusive design standards
│   ├── licensing.md                   # SPDX / CC licensing references
│   ├── data-contracts.md              # Data contract schema reference
│   ├── telemetry_standards.md         # System telemetry and sustainability metrics
│   └── governance/
│       └── ROOT-GOVERNANCE.md         # Root governance charter and oversight policies
│
├── workflows/                         # GitHub workflow documentation
│   ├── README.md                      # Workflow index
│   ├── docs-lint.yml.md               # Markdown linting & validation workflow
│   ├── faircare-validate.yml.md       # FAIR+CARE audit pipeline
│   ├── telemetry-export.yml.md        # Metrics export and energy tracking
│   ├── stac-validate.yml.md           # STAC/DCAT metadata validator
│   └── ai-train.yml.md                # AI training + governance alignment pipeline
│
├── guides/                            # Topical guidebooks (AI, Geo, Data, etc.)
│   ├── ai/README.md                   # AI & Focus Mode guide index
│   ├── geo/README.md                  # Geospatial pipelines & tooling
│   ├── data/README.md                 # Data ingestion & FAIR+CARE standards
│   ├── deployment/README.md           # CI/CD & infrastructure automation
│   ├── governance/README.md           # Oversight, ethics, and ledger integration
│   ├── integration/README.md          # STAC/DCAT ↔ API ↔ Neo4j interoperability
│   ├── sustainability/README.md       # Energy, carbon, and renewable strategy
│   ├── telemetry/README.md            # Observability and audit telemetry
│   ├── visualization/README.md        # MapLibre, timelines, UI & accessibility
│   └── workflows/README.md            # Automation & validation guides
│
├── templates/                         # Authoring and documentation templates
│   ├── model_card.md                  # AI model card template
│   ├── sop.md                         # Standard Operating Procedure template
│   ├── experiment.md                  # Experiment report template
│   └── workflow_template.md           # YAML workflow documentation template
│
└── reports/                           # Validation and audit outputs
    ├── faircare_summary.json          # FAIR+CARE audit snapshot
    ├── stac_validation.json           # STAC/DCAT validation report
    ├── governance_audit.json          # Governance compliance summary
    └── telemetry/                     # Energy, latency, and a11y metrics
        ├── docs_telemetry.json
        └── sustainability_metrics.json
```

---

## ⚙️ Workflows Documentation

The **`docs/workflows/`** directory provides annotated companions for each **GitHub Actions workflow**.  
Each document includes YAML excerpts, dependency diagrams, and governance context.

| Workflow | Description |
|-----------|-------------|
| `docs-lint.yml.md` | Lints Markdown files for MCP-DL and Platinum README compliance. |
| `faircare-validate.yml.md` | Runs FAIR+CARE audits and ethical metadata checks. |
| `telemetry-export.yml.md` | Aggregates build metrics, energy use, and latency. |
| `stac-validate.yml.md` | Validates STAC/DCAT interoperability. |
| `ai-train.yml.md` | AI model training and ethical registry workflow. |

These documents enable **traceable CI/CD governance**, ensuring all automations meet FAIR+CARE certification requirements.

---

## 🧱 Documentation Standards

All Markdown files include **front-matter metadata**, badges, emojis, and validation hooks.

**Front-Matter Example**
```yaml
---
title: "🏗️ Kansas Frontier Matrix — System Architecture"
path: "src/ARCHITECTURE.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.0.0/sbom.spdx.json"
manifest_ref: "releases/v10.0.0/manifest.zip"
telemetry_ref: "releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/system-architecture-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
```

See **[`standards/markdown_rules.md`](standards/markdown_rules.md)** for rules and emoji hierarchy.

---

## 🧩 Core Documentation Sections

### 🏗 Architecture & Systems

| Document | Description |
|-----------|-------------|
| [`architecture/data-architecture.md`](architecture/data-architecture.md) | Data modeling, STAC/DCAT mapping, ontology. |
| [`architecture/web-ui.md`](architecture/web-ui.md) | Web UI, components, and timeline integration. |
| [`architecture/github-architecture.md`](architecture/github-architecture.md) | CI/CD & governance automation architecture. |
| [`architecture/api-architecture.md`](architecture/api-architecture.md) | Backend and Neo4j integration overview. |

---

### ⚖ Governance & Ethics

| Document | Description |
|-----------|-------------|
| [`standards/faircare.md`](standards/faircare.md) | FAIR+CARE ethical governance charter. |
| [`standards/data-contracts.md`](standards/data-contracts.md) | Dataset schema and validation contract reference. |
| [`standards/governance/ROOT-GOVERNANCE.md`](standards/governance/ROOT-GOVERNANCE.md) | Root governance policies. |
| [`standards/ui_accessibility.md`](standards/ui_accessibility.md) | Accessibility and inclusivity standards. |

---

### 🔄 Pipelines & Workflows

| Document | Description |
|-----------|-------------|
| [`../src/pipelines/README.md`](../src/pipelines/README.md) | Data and AI workflow orchestration. |
| [`../src/pipelines/etl/README.md`](../src/pipelines/etl/README.md) | ETL ingest pipelines. |
| [`workflows/README.md`](workflows/README.md) | GitHub CI/CD and governance workflows. |
| [`../src/pipelines/validation/README.md`](../src/pipelines/validation/README.md) | Validation and FAIR+CARE certification processes. |

---

### 🧠 AI & Focus Mode

| Document | Description |
|-----------|-------------|
| [`../src/ai/README.md`](../src/ai/README.md) | AI systems and explainability pipeline. |
| [`../src/ai/models/focus_transformer_v1/README.md`](../src/ai/models/focus_transformer_v1/README.md) | Focus Mode model documentation. |
| [`../src/ai/explainability/README.md`](../src/ai/explainability/README.md) | AI explainability and bias tracking. |

---

### 🎨 Design & Web Interface

| Document | Description |
|-----------|-------------|
| [`../web/README.md`](../web/README.md) | Frontend design and structure. |
| [`../web/public/icons/README.md`](../web/public/icons/README.md) | Iconography and accessibility guidance. |
| [`standards/ui_accessibility.md`](standards/ui_accessibility.md) | WCAG compliance and accessibility rules. |

---

## 🧮 Validation & CI/CD Compliance

**Primary Workflows:**  
- `docs-lint.yml` – Documentation and YAML validation.  
- `faircare-validate.yml` – Ethical compliance and governance.  
- `telemetry-export.yml` – Performance and sustainability metrics.  

**Reports:**  
Stored under `reports/self-validation/docs/` and surfaced in `focus-telemetry.json`.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-09 | `@kfm-docs` | Upgraded index to v10; added comprehensive guides (AI, Geo, Data, Deployment, Governance, Integration, Sustainability, Telemetry, Visualization, Workflows). |
| v9.9.0 | 2025-11-08 | `@kfm-docs` | Added `workflows/` documentation set and updated architecture categories. |
| v9.7.0 | 2025-11-05 | `@kfm-core` | Standardized telemetry schema and governance refs. |
| v9.5.0 | 2025-10-20 | `@kfm-core` | Integrated FAIR+CARE metadata validation hooks. |
| v9.0.0 | 2025-06-01 | `@kfm-core` | Initial documentation index established. |

---

<div align="center">

**Kansas Frontier Matrix Documentation**  
*Governed Knowledge × FAIR+CARE Certification × Sustainable Transparency*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Root README](../README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>
