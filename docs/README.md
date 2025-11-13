---
title: "📚 Kansas Frontier Matrix — Documentation Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-index-v3.json"
governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation Index**  
`docs/README.md`

**Purpose:**  
Serve as the **central navigation hub** for all Kansas Frontier Matrix (KFM) documentation — standards, architecture, workflows, governance, AI systems, pipelines, datasets, analyses, security, and developer guides — maintained under **MCP-DL v6.3**, **FAIR+CARE**, and **ISO 19115** alignment.

<img alt="Docs · MCP_v6.3" src="https://img.shields.io/badge/Docs·MCP-v6.3-blue" />
<img alt="License: CC-BY 4.0" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success" />

</div>


---

## 📘 Overview

The **KFM documentation ecosystem** is a **schema-aware, telemetry-enabled knowledge graph of Markdown documents**.

Each file includes:

- YAML front-matter for **validation**, **telemetry**, and **governance**  
- Stable paths for cross-referencing between README files and code  
- FAIR+CARE metadata and governance references

Aligned frameworks:

- **Master Coder Protocol (MCP-DL v6.3)**  
- **FAIR+CARE Governance**  
- **Platinum README Template v7.1**  
- **ISO 19115**, **DCAT 3.0**, **CIDOC CRM**  

---

## 🗂️ Directory Layout

    docs/
    ├── README.md                          # Central documentation index
    ├── glossary.md                        # Glossary of technical, governance, and domain terms
    │
    ├── architecture/                      # Architecture, systems, and design docs
    │   ├── data-architecture.md           # Data model, STAC/DCAT schemas, and ontologies
    │   ├── web-ui.md                      # Frontend structure, components, accessibility
    │   ├── github-architecture.md         # CI/CD and automation architecture
    │   └── api-architecture.md            # API and knowledge graph integration
    │
    ├── standards/                         # FAIR+CARE, governance, compliance, and style rules
    │   ├── faircare.md                    # FAIR+CARE ethical framework
    │   ├── markdown_rules.md              # Platinum README & markdown rules
    │   ├── markdown_guide.md              # Style and formatting conventions
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
    ├── analyses/                          # Domain analyses (end-user science outputs)
    │   ├── README.md                      # Analyses overview & navigation
    │   ├── hydrology/                     # Drought–flood correlation & hydrology methods
    │   ├── climatology/                   # Trend, projection, and climate datasets
    │   ├── geology/                       # Stratigraphy, seismic, geomorphology
    │   ├── ecology/                       # SDM, landcover, ecosystem services
    │   └── historical/                    # Archives, treaties, cultural landscapes
    │
    ├── security/                          # Security, threat modeling, and supply chain integrity
    │   ├── README.md                      # Security overview
    │   ├── threat-model.md                # STRIDE/LINDDUN threat model & mitigations
    │   ├── secrets-policy.md              # Secrets handling, KMS/HSM, and rotation policy
    │   ├── supply-chain.md                # SBOM, SLSA, provenance, dependency governance
    │   └── vulnerability-management.md    # Reporting, triage, CVSS, patch SLAs
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

---

## 🔎 What’s New (v10.3.1)

- Aligned all references to **v10.3.0** release artifacts (SBOM, manifest, telemetry).  
- Ensured **analyses/** and **security/** sections are present in the directory map and cross-linked from topical guides.  
- Updated **badges** and **telemetry_schema** to the current docs index schema.  

---

## ⚙️ Workflows Documentation

The **`docs/workflows/`** directory provides annotated companions for each **GitHub Actions workflow**.

| Workflow Doc                    | Description                                               |
|---------------------------------|-----------------------------------------------------------|
| `docs-lint.yml.md`             | Lints Markdown + YAML against MCP and Platinum rules.    |
| `faircare-validate.yml.md`     | Runs FAIR+CARE audits and ethical metadata checks.        |
| `telemetry-export.yml.md`      | Aggregates build metrics, energy use, and latency.        |
| `stac-validate.yml.md`         | Validates STAC/DCAT metadata and linkage.                 |
| `ai-train.yml.md`              | AI model training, registry, and governance alignment.    |

These documents make CI/CD flows **transparent and auditable**.

---

## 🧱 Documentation Standards (Front-Matter)

All docs include front-matter with references to:

- SBOM, manifests, telemetry refs  
- Governance and data contracts  
- Telemetry schemas for automated validation  

Example front-matter pattern:

    ---
    title: "🏗️ Kansas Frontier Matrix — System Architecture"
    path: "src/ARCHITECTURE.md"
    version: "v10.3.1"
    last_updated: "2025-11-13"
    review_cycle: "Quarterly / FAIR+CARE Council"
    commit_sha: "<latest-commit-hash>"
    sbom_ref: "releases/v10.3.0/sbom.spdx.json"
    manifest_ref: "releases/v10.3.0/manifest.zip"
    telemetry_ref: "releases/v10.3.0/focus-telemetry.json"
    telemetry_schema: "schemas/telemetry/system-architecture-v1.json"
    governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
    license: "CC-BY 4.0"
    mcp_version: "MCP-DL v6.3"
    ---

See `standards/markdown_rules.md` for granular rules.

---

## 🧩 Core Documentation Sections

### 🏗 Architecture & Systems

| Document                                            | Description                                      |
|-----------------------------------------------------|--------------------------------------------------|
| `architecture/data-architecture.md`                | Data model, STAC/DCAT schemas, and ontologies.  |
| `architecture/web-ui.md`                           | Frontend structure, components, accessibility.  |
| `architecture/github-architecture.md`              | CI/CD & workflow automation architecture.       |
| `architecture/api-architecture.md`                 | API / Neo4j integration and query design.       |

---

### ⚖ Governance & Ethics

| Document                                             | Description                                    |
|------------------------------------------------------|------------------------------------------------|
| `standards/faircare.md`                              | FAIR+CARE ethical governance framework.       |
| `standards/data-contracts.md`                        | Dataset contracts and schema expectations.    |
| `standards/ui_accessibility.md`                      | UI accessibility and inclusive design rules.  |
| `standards/governance/ROOT-GOVERNANCE.md`            | Root governance charter and oversight.        |

---

### 🔄 Pipelines & Workflows

| Document                                      | Description                               |
|-----------------------------------------------|-------------------------------------------|
| `../src/pipelines/README.md`                  | Pipeline architecture and modules.       |
| `../src/pipelines/etl/README.md`              | ETL ingestion and transform details.     |
| `../src/pipelines/validation/README.md`       | Validation, FAIR+CARE certification.     |
| `workflows/README.md`                         | CI/CD workflows and governance flows.    |

---

### 🧠 AI & Focus Mode

| Document                                                 | Description                             |
|----------------------------------------------------------|-----------------------------------------|
| `../src/ai/README.md`                                    | AI systems, models, and governance.     |
| `../src/ai/models/focus_transformer_v2/README.md`        | Focus Transformer v2 model card.        |
| `../src/ai/explainability/README.md`                     | Explainability pipelines + metrics.     |

---

### 🎨 Design, Web Interface & Accessibility

| Document                                   | Description                              |
|--------------------------------------------|------------------------------------------|
| `../web/README.md`                         | Web platform overview.                   |
| `../web/ARCHITECTURE.md`                  | Web architecture & component flows.      |
| `../web/public/README.md`                 | Public assets, icons, and infographics.  |
| `standards/ui_accessibility.md`           | Formal accessibility standard.           |

---

### 🔐 Security

| Document                                   | Description                                  |
|--------------------------------------------|----------------------------------------------|
| `security/README.md`                       | Security posture and responsibilities.       |
| `security/threat-model.md`                 | Threat modeling (STRIDE/LINDDUN).            |
| `security/secrets-policy.md`               | Secrets, KMS, and rotation policies.         |
| `security/supply-chain.md`                 | SBOM, SLSA, provenance, dependency policies. |
| `security/vulnerability-management.md`     | Reporting, triage, remediation SLAs.         |

---

## 🧮 Validation & CI/CD Compliance

Documentation is validated by:

- `docs-lint.yml` — front-matter, headings, link correctness  
- `faircare-validate.yml` — ethical and governance metadata checks  
- `telemetry-export.yml` — ensures docs metrics are recorded in telemetry  

Primary reports:

- `../reports/self-validation/docs/lint_summary.json`  
- `../reports/fair/docs_summary.json` (if present)  
- `../releases/v10.3.0/focus-telemetry.json` (docs section)

---

## 🕰️ Version History

| Version  | Date       | Author        | Summary                                                                          |
|----------|------------|---------------|----------------------------------------------------------------------------------|
| v10.3.1  | 2025-11-13 | @kfm-docs     | Updated to v10.3 release paths; ensured analyses & security dirs in layout map. |
| v10.2.3  | 2025-11-09 | @kfm-docs     | Added analyses/ and security/ sections; refreshed metadata and cross-links.     |
| v10.2.2  | 2025-11-09 | @kfm-docs     | Aligned to v10.2; updated schemas and governance refs.                          |
| v10.0.0  | 2025-11-09 | @kfm-docs     | Upgraded to v10; added AI, Geo, Data, Deployment, Governance, Integration, etc. |
| v9.9.0   | 2025-11-08 | @kfm-docs     | Added workflows/ documentation set and updated architecture categories.         |
| v9.7.0   | 2025-11-05 | @kfm-core     | Standardized telemetry schema and governance references.                        |
| v9.5.0   | 2025-10-20 | @kfm-core     | Integrated FAIR+CARE metadata validation hooks.                                  |
| v9.0.0   | 2025-06-01 | @kfm-core     | Initial documentation index established.                                         |

---

<div align="center">

**Kansas Frontier Matrix Documentation**  
*Governed Knowledge × FAIR+CARE Certification × Sustainable Transparency*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Root README](../README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>