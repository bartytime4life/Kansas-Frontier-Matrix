---
title: "📚 Kansas Frontier Matrix — Documentation Index"
path: "docs/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../releases/v9.7.0/manifest.zip"
telemetry_ref: "../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-index-v1.json"
governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Documentation Index**
`docs/README.md`

**Purpose:** Provide the central navigation hub for all Kansas Frontier Matrix (KFM) documentation — standards, governance, pipelines, AI systems, datasets, and developer references — validated under **MCP v6.3** and **FAIR+CARE**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **Kansas Frontier Matrix (KFM)** documentation is a **living, interlinked knowledge base**.  
Each Markdown file is both **human-readable** and **machine-parseable** — carrying front-matter metadata used by validation and governance systems.

Aligned frameworks:
- **Master Coder Protocol (MCP v6.3)**  
- **FAIR+CARE** Data Governance  
- **Platinum README v7.1**  
- **ISO 19115** & **DCAT 3.0** metadata alignment

---

## 🗂️ Directory Layout

```
docs/
├── README.md                        # Central index (this file)
├── glossary.md                      # Glossary of technical and ethical terms
│
├── architecture/                    # System and UI design documents
│   ├── data-architecture.md         # Data modeling + STAC/DCAT schemas
│   ├── web-ui.md                    # Frontend architecture & UX
│   └── github-architecture.md       # CI/CD & governance automation
│
├── standards/                       # FAIR+CARE, governance, style, licensing
│   ├── faircare.md                  # Ethical data governance
│   ├── markdown_rules.md            # Structural rules
│   ├── markdown_guide.md            # Style guide
│   ├── ui_accessibility.md          # WCAG 2.1 AA accessibility
│   ├── licensing.md                 # SPDX / CC licensing reference
│   ├── data-contracts.md            # Dataset contracts & schemas
│   └── governance/
│       └── ROOT-GOVERNANCE.md       # Root governance charter
│
├── templates/                       # Reusable authoring templates
│   ├── model_card.md                # AI model card template
│   ├── sop.md                       # SOP template
│   └── experiment.md                # Experiment template
│
└── reports/                         # Validation & audit documentation
    ├── faircare_summary.json        # FAIR+CARE validation snapshot
    ├── stac_validation.json         # STAC/DCAT validation summary
    └── telemetry/                   # Telemetry and governance metrics
```

> All documentation references appear in the telemetry snapshot:  
> `../releases/v9.7.0/focus-telemetry.json`

---

## 🧱 Documentation Standards

Every doc uses **GitHub-Flavored Markdown (GFM)** and includes YAML front-matter for provenance and validation.

**Front-Matter Example**
```yaml
---
title: "🏗️ Kansas Frontier Matrix — System Architecture"
path: "src/ARCHITECTURE.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
telemetry_ref: "releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/system-architecture-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
```

See **[markdown_rules.md](standards/markdown_rules.md)** and **[markdown_guide.md](standards/markdown_guide.md)** for alignment details (badges order, emoji headers, table rules, mermaid limits).

---

## 🧩 Core Categories

### 🏗 Architecture & Systems

| Document | Description |
|-----------|-------------|
| [`src/ARCHITECTURE.md`](../src/ARCHITECTURE.md) | High-level system architecture. |
| [`architecture/data-architecture.md`](architecture/data-architecture.md) | Data model overview + STAC/DCAT mappings. |
| [`architecture/web-ui.md`](architecture/web-ui.md) | Web app components, a11y, and interactions. |
| [`.github/ARCHITECTURE.md`](../.github/ARCHITECTURE.md) | CI/CD automation and governance architecture. |

---

### ⚖ Governance & Ethics

| Document | Description |
|-----------|-------------|
| [`standards/faircare.md`](standards/faircare.md) | FAIR+CARE governance framework. |
| [`standards/governance/ROOT-GOVERNANCE.md`](standards/governance/ROOT-GOVERNANCE.md) | Root charter and council processes. |
| [`standards/data-contracts.md`](standards/data-contracts.md) | Dataset contracts and schema references. |
| [`standards/licensing.md`](standards/licensing.md) | SPDX/CC license guidance. |

---

### 🔄 Pipelines & Data Workflows

| Document | Description |
|-----------|-------------|
| [`../src/pipelines/README.md`](../src/pipelines/README.md) | ETL/AI/validation pipeline index. |
| [`../src/pipelines/etl/README.md`](../src/pipelines/etl/README.md) | ETL process and configs. |
| [`../src/pipelines/validation/README.md`](../src/pipelines/validation/README.md) | FAIR+CARE and STAC validation flows. |
| [`../data/processed/README.md`](../data/processed/README.md) | Processed data directory reference. |

---

### 🧠 AI & Focus Mode

| Document | Description |
|-----------|-------------|
| [`../src/ai/README.md`](../src/ai/README.md) | AI modules and orchestration. |
| [`../src/ai/models/focus_transformer_v1/README.md`](../src/ai/models/focus_transformer_v1/README.md) | Focus Mode model card. |
| [`../src/ai/explainability/README.md`](../src/ai/explainability/README.md) | SHAP/LIME and drift analysis. |
| [`../src/ai/training/README.md`](../src/ai/training/README.md) | Training configs and evaluation. |

---

### 🎨 Design & Web Interface

| Document | Description |
|-----------|-------------|
| [`../web/README.md`](../web/README.md) | Frontend architecture and patterns. |
| [`../web/public/icons/README.md`](../web/public/icons/README.md) | Iconography and a11y guidance. |
| [`standards/ui_accessibility.md`](standards/ui_accessibility.md) | WCAG 2.1 AA standards. |
| [`architecture/web-ui.md`](architecture/web-ui.md) | UI/UX diagrams and flows. |

---

## ✏️ Writing Rules & Style

- Emoji-prefixed headers (📘, 🗂️, 🧾, ⚙️, 🧩, ⚖️, 🕰️).  
- Include a Directory Layout tree in each README.  
- Mermaid: `flowchart TD|LR`, quoted labels, ≤1 diagram/section.  
- Tables: ≥3 columns, `—` for N/A, ≤100 chars width.  
- End with **Version History** and a **centered footer**.

---

## 🧮 Validation & Compliance

**Workflows:** `docs-lint.yml`, `stac-validate.yml`, `faircare-validate.yml`, `telemetry-export.yml`  
**Reports:** stored under `reports/self-validation/docs/` and summarized in telemetry.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added Directory Layout, standards refs, and telemetry linkages. |
| v9.5.0 | 2025-10-20 | A. Barta | Introduced markdown compliance and governance sections. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Expanded architecture and FAIR+CARE references. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial documentation index created. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Root README](../README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>