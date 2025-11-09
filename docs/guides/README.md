---
title: "📚 Kansas Frontier Matrix — Guides Directory Overview"
path: "docs/guides/README.md"
version: "v10.0.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v10.0.0/telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-guides-v10.json"
governance_ref: "../standards/faircare.md"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Guides Directory Overview**
`docs/guides/README.md`

**Purpose:**  
Provide an organized, navigable index for the `docs/guides/` directory and all documentation beneath it.  
This directory houses user manuals, developer guides, FAIR+CARE governance materials, AI explainability references, and workflow documentation for **Kansas Frontier Matrix (KFM)**.  
All entries conform to **MCP-DL v6.3**, **Platinum README Template v7.1**, and **Diamond⁹ Ω / Crown∞Ω Ultimate Certification** repository documentation standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../..)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Enabled-orange)](../standards/faircare.md)
[![Status](https://img.shields.io/badge/Status-Stable_Build-brightgreen)](#)

</div>

---

## 📘 Overview

The `docs/guides/` directory serves as the **documentation hub** for both technical and governance-related topics.  
Each subdirectory beneath `guides/` provides reference materials, upgrade playbooks, integration overviews, and design documentation that support all active modules within the KFM monorepo.  
This structure ensures maintainability, ethical reproducibility, and strong cross-reference linkage between code, data, and governance systems.

---

## 🗂️ Directory Layout (for `docs/guides/` and below)

```plaintext
docs/
  guides/                    # User, developer, and governance documentation hub
  │
  ├── README.md              # This directory overview and navigation index
  │
  ├── upgrade/               # Version upgrades, inventories, readiness plans
  │   ├── README.md          # v10 upgrade overview and migration guide
  │   ├── v10-readiness.md   # Upgrade readiness & validation checklist
  │   └── v10-inventory.md   # Legacy document consolidation matrix
  │
  ├── ai/                    # Focus Mode v2, explainability, AI governance
  │   ├── README.md          # Directory index for AI-focused guides
  │   ├── explainability.md  # XAI metrics, SHAP/LIME documentation
  │   └── focus-mode-v2.md   # AI-assisted Focus Mode configuration guide
  │
  ├── workflows/             # CI/CD, automation, and validation pipelines
  │   ├── README.md          # Overview of workflows and validation logic
  │   ├── ci-cd-pipelines.md # GitHub Actions, build, and telemetry integration
  │   └── governance-ledger.md # Ledger integration and SBOM traceability
  │
  ├── governance/            # FAIR+CARE, MCP-DL, and ISO governance guides
  │   ├── README.md          # Ethical standards and compliance guide
  │   ├── faircare.md        # FAIR+CARE policy and review process
  │   └── mcp-compliance.md  # Master Coder Protocol enforcement guidelines
  │
  ├── integration/           # STAC↔DCAT, ETL, and API interoperability
  │   ├── README.md          # Integration index and overview
  │   ├── stac-dcat-bridge.md # Metadata translation guide
  │   └── api-data-flow.md   # API + data sync documentation
  │
  └── visualization/         # UX, UI, and accessibility documentation
      ├── README.md          # Visualization and interface design index
      ├── maplibre-guide.md  # MapLibre + React component integration
      └── accessibility.md   # Accessibility and color-contrast standards

