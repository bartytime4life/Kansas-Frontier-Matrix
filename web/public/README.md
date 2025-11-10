---
title: "🌐 Kansas Frontier Matrix — Web Public Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-v2.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Public Assets**
`web/public/README.md`

**Purpose:**  
Document the **public-facing static assets** for the KFM web application — icons, images, fonts, and PWA metadata — and define FAIR+CARE governance, accessibility, and telemetry requirements for open publication under **Master Coder Protocol v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)
[![License: MIT / CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%2F%20CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview
This directory contains **immutable, cacheable** assets supporting the KFM UI, governance dashboards, and dataset visualizations.  
All assets are **licensed**, **checksum-verified**, and **accessibility-audited**.  
Metadata is linked to provenance ledgers and release telemetry ensuring traceability, sustainability, and ethical reuse.

---

## 🗂️ Directory Layout
```
web/public/
├── README.md
│
├── icons/                  # System, data, and app iconography (SVG/PNG)
│   └── metadata.json       # Icon registry (license, checksum, a11y tags)
│
├── images/                 # UI, maps, governance, and data visuals
│   ├── ui/
│   ├── maps/
│   ├── data/
│   ├── governance/
│   ├── archive/
│   └── metadata.json       # Image registry with FAIR+CARE annotations
│
├── fonts/                  # Open-source fonts (WOFF2) + typography tokens
├── manifest.json           # PWA manifest (name, theme, icons, scope)
└── metadata.json           # Root FAIR+CARE + provenance registry for assets
```

---

## 🧩 Governance & Publication Workflow
```mermaid
flowchart TD
"Design / Data Viz Production" --> "Accessibility & FAIR+CARE Audit"
"Accessibility & FAIR+CARE Audit" --> "Checksum + License + Metadata Registration"
"Checksum + License + Metadata Registration" --> "Provenance Ledger Sync (ISO 19115 / DCAT)"
"Provenance Ledger Sync (ISO 19115 / DCAT)" --> "CI/CD Publish (Immutable, Cache-Control)"
```

1. **Audit:** Automated Lighthouse + axe accessibility scan & FAIR+CARE review  
2. **Register:** SHA-256 checksum, SPDX license, alt text added to `metadata.json`  
3. **Ledger:** Metadata & ethics details appended to governance ledger (`docs/reports/audit/`)  
4. **Publish:** Deployed via CI/CD; artifacts referenced in SBOM & manifest  

---

## 🧾 Example Asset Metadata
```json
{
  "id": "web_public_assets_v10.0.0",
  "category": "images/maps",
  "filename": "ks_topography_1890.png",
  "checksum_sha256": "ed92a2a3c4c6b1e0a71d57bfb78dfcbbd7",
  "license": "CC-BY-4.0",
  "alt_text": "Topographic map of Kansas circa 1890",
  "fairstatus": "certified",
  "a11y_reviewed": true,
  "sustainability_score": 98,
  "timestamp": "2025-11-09T18:55:00Z"
}
```

All entries must include `checksum_sha256`, `license`, and `alt_text` for verification.

---

## ⚙️ FAIR+CARE Governance Matrix
| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Asset registries searchable by checksum & ID in SBOM. | @kfm-data |
| **Accessible** | Alt text for imagery; keyboard-visible focus for icon links. | @kfm-accessibility |
| **Interoperable** | Metadata uses ISO 19115 + DCAT; JSON-LD exportable. | @kfm-architecture |
| **Reusable** | MIT/CC-BY; provenance + license in registry. | @kfm-design |
| **Collective Benefit** | Assets promote public education & research. | @faircare-council |
| **Authority to Control** | Council review for culturally sensitive images. | @kfm-governance |
| **Responsibility** | Contributors ensure inclusive, unbiased representations. | @kfm-ethics |

---

## ⚙️ Compliance & CI/CD Integration
| Workflow | Function | Artifact |
|---|---|---|
| `docs-lint.yml` | Validate Markdown/front-matter consistency | `reports/self-validation/docs/lint_summary.json` |
| `build-and-deploy.yml` | Bundle + publish web assets | `../../releases/v10.0.0/manifest.zip` |
| `telemetry-export.yml` | Aggregate sustainability & asset metrics | `../../releases/v10.0.0/focus-telemetry.json` |
| `accessibility_scan.yml` | Lighthouse/axe A11y scan per release | `reports/self-validation/web/a11y_summary.json` |

> CI/CD workflows automatically reject any asset without checksum, license, or alt text.

---

## 🌱 Sustainability & Performance Targets
| Metric | Target | Verified By |
|---|---|---|
| Avg. Image Weight | ≤ 400 KB | Build metrics |
| Render Energy | ≤ 0.04 Wh | Telemetry |
| Carbon Output | ≤ 0.05 gCO₂e | Telemetry |
| Renewable Hosting | ≥ 100% RE100 | Infra Audit |
| Lighthouse Perf | ≥ 95 | `accessibility_scan.yml` |

---

## 🧮 Telemetry & Provenance
- Asset metadata appended to `focus-telemetry.json` for version provenance.  
- Environmental and A11y scores merged into governance dashboards.  
- CI/CD publishes metrics to:  
  - `docs/reports/telemetry/build_metrics.json`  
  - `docs/reports/audit/web_public_assets.json`  

Example:
```json
{
  "asset_id": "map_kansas_1930",
  "bytes": 355432,
  "energy_wh": 0.031,
  "co2_g": 0.047,
  "a11y_score": 98,
  "timestamp": "2025-11-09T18:00:00Z"
}
```

---

## 🕰️ Version History
| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | Web Assets Team | Upgraded to v10: sustainability telemetry, ISO/DCAT export support, Lighthouse A11y CI integration. |
| v9.7.0 | 2025-11-05 | KFM Core Team | Metadata registries, telemetry schema v1, a11y requirements. |
| v9.6.0 | 2025-11-04 | KFM Core Team | Added sustainability metrics & checksum traceability. |
| v9.5.0 | 2025-11-02 | KFM Core Team | Automated FAIR+CARE asset audit pipeline. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Web Overview](../README.md) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>