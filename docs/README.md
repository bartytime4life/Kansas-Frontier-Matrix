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

**Purpose:** Serve as the central navigation index for all documentation within the Kansas Frontier Matrix (KFM) monorepo — covering standards, governance, pipelines, AI systems, datasets, and developer references.  
All documents comply with **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** principles for transparency, ethics, and reproducibility.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Documentation Standards](#-documentation-standards)
- [Core Categories](#-core-categories)
  - [Architecture & Systems](#architecture--systems)
  - [Governance & Ethics](#governance--ethics)
  - [Pipelines & Data Workflows](#pipelines--data-workflows)
  - [AI & Focus Mode](#ai--focus-mode)
  - [Design & Web Interface](#design--web-interface)
- [Writing Rules & Style Guide](#-writing-rules--style-guide)
- [Validation & Compliance](#-validation--compliance)
- [Version History](#-version-history)

---

## 🌍 Overview

The **Kansas Frontier Matrix (KFM)** documentation is designed as a **living, interlinked knowledge base**.  
Every Markdown file functions both as a **human-readable document** and a **machine-parseable metadata source** for automated validation and graph integration.

All documentation follows:
- **MCP Documentation-First Protocol**
- **FAIR+CARE Data Governance**
- **Platinum README Template v7.1**
- **ISO 19115 & DCAT 3.0 metadata alignment**

---

## 🧱 Documentation Standards

KFM uses **GitHub-Flavored Markdown (GFM)** with standardized YAML front-matter metadata for every document.  
This ensures version traceability, rendering consistency, and automated indexing across the knowledge graph.

**Front-Matter Schema Example:**
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
---
```

See [📑 Markdown Rules](standards/markdown_rules.md) and [🎨 Markdown Style Guide](standards/markdown_guide.md) for formatting best practices.

---

## 🧩 Core Categories

### 🏗 Architecture & Systems

| Document | Description |
|-----------|-------------|
| [`src/ARCHITECTURE.md`](../src/ARCHITECTURE.md) | Technical blueprint for KFM’s architecture layers. |
| [`docs/architecture/data-architecture.md`](architecture/data-architecture.md) | Overview of data modeling, STAC/DCAT schema, and file structure. |
| [`docs/architecture/web-ui.md`](architecture/web-ui.md) | Frontend (React + MapLibre) interface and component design. |
| [`docs/architecture/github-architecture.md`](../.github/ARCHITECTURE.md) | CI/CD, automation, and governance pipeline documentation. |

---

### ⚖ Governance & Ethics

| Document | Description |
|-----------|-------------|
| [`docs/standards/faircare.md`](standards/faircare.md) | FAIR+CARE data governance framework. |
| [`docs/standards/governance/ROOT-GOVERNANCE.md`](standards/governance/ROOT-GOVERNANCE.md) | Root governance charter for ethical review and decision processes. |
| [`docs/standards/data-contracts.md`](standards/data-contracts.md) | Schema of FAIR-compliant data contracts for all datasets. |
| [`docs/standards/licensing.md`](standards/licensing.md) | License guidelines and SPDX references. |

---

### 🔄 Pipelines & Data Workflows

| Document | Description |
|-----------|-------------|
| [`src/pipelines/README.md`](../src/pipelines/README.md) | Overview of ETL, AI, and validation pipelines. |
| [`src/pipelines/etl/README.md`](../src/pipelines/etl/README.md) | Extract–Transform–Load process documentation. |
| [`src/pipelines/validation/README.md`](../src/pipelines/validation/README.md) | FAIR+CARE validation module. |
| [`data/processed/README.md`](../data/processed/README.md) | Processed dataset directory reference. |

---

### 🧠 AI & Focus Mode

| Document | Description |
|-----------|-------------|
| [`src/ai/README.md`](../src/ai/README.md) | Overview of AI/ML components in KFM. |
| [`src/ai/models/focus_transformer_v1/README.md`](../src/ai/models/focus_transformer_v1/README.md) | AI-powered Focus Mode engine and model documentation. |
| [`src/ai/explainability/README.md`](../src/ai/explainability/README.md) | SHAP/LIME explainability module reference. |
| [`src/ai/training/README.md`](../src/ai/training/README.md) | Model training configuration and evaluation methods. |

---

### 🎨 Design & Web Interface

| Document | Description |
|-----------|-------------|
| [`web/README.md`](../web/README.md) | Overview of KFM’s web frontend design principles. |
| [`web/public/icons/README.md`](../web/public/icons/README.md) | Iconography and accessibility guidelines. |
| [`docs/standards/ui_accessibility.md`](standards/ui_accessibility.md) | Accessibility compliance (WCAG 2.1 AA). |
| [`docs/architecture/web-ui.md`](architecture/web-ui.md) | Web interface design & interaction models. |

---

## ✏️ Writing Rules & Style Guide

All KFM documentation follows the **Markdown Styling & Rules** guides:

- [🧾 `docs/standards/markdown_rules.md`](standards/markdown_rules.md) — structural, front-matter, and layout rules  
- [🎨 `docs/standards/markdown_guide.md`](standards/markdown_guide.md) — stylistic conventions for headers, emojis, and badges  

**Formatting Highlights:**
- Use emojis in headers for visual indexing.
- Always include YAML front-matter.
- Write short paragraphs for readability.
- Include directory trees and Mermaid diagrams where applicable.
- End each document with a version history table and © footer.

---

## 🧮 Validation & Compliance

Documentation is automatically validated by **CI/CD workflows** under `.github/workflows/`:

| Workflow | Purpose |
|-----------|----------|
| `docs-lint.yml` | Ensures Markdown consistency and schema validity. |
| `stac-validate.yml` | Validates dataset catalogs referenced in docs. |
| `faircare-validate.yml` | Verifies ethical data governance references. |
| `telemetry-export.yml` | Logs doc validation telemetry to `focus-telemetry.json`. |

Validation reports are stored in:
```
reports/self-validation/docs/
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added unified documentation index with linked categories and style integration. |
| v9.5.0 | 2025-10-20 | A. Barta | Introduced markdown compliance section and telemetry links. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Expanded architecture and FAIR+CARE reference sections. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial documentation structure created. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Root README](../README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>
