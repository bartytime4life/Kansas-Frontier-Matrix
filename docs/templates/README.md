---
title: "📄 Kansas Frontier Matrix — Documentation Templates Index"
path: "docs/templates/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-templates-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — Documentation Templates Index**
`docs/templates/README.md`

**Purpose:** Central reference for all reusable templates used throughout the Kansas Frontier Matrix (KFM) documentation ecosystem.  
Each template is **MCP v6.3** and **FAIR+CARE** compliant, ensuring every experiment, model, or workflow is documented with full reproducibility, ethical transparency, and version traceability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

All templates in this directory are designed to make **documentation-first development** frictionless and consistent.  
They ensure every KFM contributor can create compliant, machine-validated documentation files — covering experiments, AI model cards, SOPs, and governance forms.

Templates follow the **Platinum README v7.1** and **MCP v6.3** conventions and are compatible with:
- Markdown linting (`docs-lint.yml`)
- FAIR+CARE audit pipelines (`faircare-validate.yml`)
- Governance ledger integration (`reports/audit/github-workflows-ledger.json`)

---

## 🗂️ Directory Layout

```
docs/templates/
├── README.md              # This index file
├── experiment.md          # Template for research or data analysis experiments
├── model_card.md          # Template for AI/ML model documentation
└── sop.md                 # Template for standard operating procedures
```

Each file begins with a **YAML front-matter block**, includes standard section headings, and ends with a version history table and FAIR+CARE footer.

---

## 🧪 Experiment Template (`experiment.md`)

**Purpose:** Standardize experiment documentation for pipelines, AI models, and data transformations.

| Section | Description |
|----------|-------------|
| `Title & Metadata` | YAML header including version, date, and references. |
| `Objective` | Describe the research or development goal. |
| `Methodology` | Outline data, tools, and techniques used. |
| `Results` | Summarize quantitative or qualitative outcomes. |
| `Reproducibility` | Provide steps, parameters, or scripts to reproduce results. |
| `Validation` | Include FAIR+CARE or audit references. |

**Referenced By:**  
- `src/pipelines/etl/README.md`  
- `src/ai/training/README.md`  
- Governance audit logs in `reports/audit/experiments-ledger.json`

---

## 🤖 Model Card Template (`model_card.md`)

**Purpose:** Document AI/ML models to ensure explainability, governance alignment, and ethical AI practice.

| Section | Description |
|----------|-------------|
| `Metadata` | Model name, author, version, date, training dataset, license. |
| `Intended Use` | Define scope, purpose, and limitations. |
| `Architecture` | Describe model type, layers, and algorithms used. |
| `Training Details` | Include hyperparameters, dataset sources, and epochs. |
| `Evaluation Metrics` | Accuracy, precision, recall, F1, etc. |
| `Bias & Ethics` | Explain how model bias is detected and mitigated. |
| `Governance` | Link to FAIR+CARE and MCP references. |

**Validation:**  
All `model_card.md` files are validated in `faircare-validate.yml` to ensure ethical compliance.

**Used In:**  
- `src/ai/models/focus_transformer_v1/`  
- `src/ai/models/embeddings/`  
- AI Governance Ledger → `reports/audit/ai_models.json`

---

## 🧾 SOP Template (`sop.md`)

**Purpose:** Define operational procedures for reproducible data and AI workflows.

| Section | Description |
|----------|-------------|
| `Purpose` | Describe the SOP’s function within KFM. |
| `Scope` | Define boundaries of the workflow or process. |
| `Procedure` | Step-by-step task execution guide. |
| `Validation` | Include CI/CD references for automated testing. |
| `Governance` | Link to data standards and ethical review documentation. |

**Example Use Cases:**
- Data ingestion and transformation (`src/pipelines/etl/`)
- CI/CD governance setup (`.github/workflows/`)
- FAIR+CARE review processes (`docs/standards/governance/`)

---

## ⚙️ Compliance Requirements

All template-based documents must:
1. Begin with YAML front-matter including `title`, `path`, `version`, `last_updated`, and `commit_sha`.
2. Include a clear **objective**, **methods**, and **validation** section.
3. Be licensed under **CC-BY 4.0**.
4. Pass markdown and schema validation in `docs-lint.yml`.
5. Include version history and © footer.

---

## 🧮 Validation Workflows

| Workflow | Function |
|-----------|-----------|
| `docs-lint.yml` | Checks template formatting, headings, and compliance. |
| `faircare-validate.yml` | Audits model cards and experiment reports for ethical governance. |
| `telemetry-export.yml` | Logs document creation and update metadata to `focus-telemetry.json`. |

All templates and their generated documents are logged into the governance ledger under:
```
reports/audit/github-workflows-ledger.json
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created unified index for experiment, model card, and SOP templates. |
| v9.5.0 | 2025-10-20 | A. Barta | Added FAIR+CARE metadata and governance linkage. |
| v9.3.0 | 2025-08-10 | KFM Core Team | Updated SOP formatting and audit integration. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial version of KFM documentation templates. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](../README.md) · [Markdown Rules](../standards/markdown_rules.md)

</div>
