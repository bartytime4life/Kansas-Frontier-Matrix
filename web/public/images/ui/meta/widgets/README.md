---
title: "📜 Kansas Frontier Matrix — UI Widget Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/ui/meta/widgets/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-images-ui-meta-widgets.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-images-ui-meta-widgets-validation.json"
  - "../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **UI Widget Metadata**
`web/public/images/ui/meta/widgets/README.md`

**Purpose:** Maintains metadata records for all interactive widget image assets within the Kansas Frontier Matrix web interface. Each entry provides provenance, license, checksum linkage, and accessibility compliance in accordance with FAIR+CARE governance standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Metadata Integrity](https://img.shields.io/badge/Metadata-Immutable-critical)](../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/ui/meta/widgets/
├── map-zoom-controls.json          # Metadata for map zoom control widget
├── timeline-slider.json            # Metadata for interactive timeline slider
├── chart-frame.json                # Metadata for data chart frame
├── data-legend-panel.json          # Metadata for legend display panel
├── heatmap-overlay.json            # Metadata for heatmap overlay background
└── README.md                       # This file
```

---

## 🧩 Metadata Schema

All metadata conforms to the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`) and aligns with FAIR+CARE, STAC, and DCAT interoperability standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the widget asset (e.g., `timeline-slider`). |
| `title` | string | Descriptive name of the widget image. |
| `category` | string | Directory classification (`ui/widgets`). |
| `version` | string | Semantic version number for the asset. |
| `creator` | string | Author, design system, or contributing team. |
| `license` | string | License type (MIT, CC-BY, or Public Domain). |
| `checksum` | string | SHA-256 hash ensuring asset immutability. |
| `alt_text` | string | Accessibility description for screen readers. |
| `source_url` | string | Repository or original source reference. |
| `provenance` | string | Historical lineage, design intent, or accessibility context. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "timeline-slider",
  "title": "Interactive Timeline Slider Widget",
  "category": "ui/widgets",
  "version": "2.0.0",
  "creator": "KFM Design Systems",
  "license": "MIT",
  "checksum": "sha256-3bfc9a7e24d928c4b42ea8f3f1f1d837ae79b7...",
  "alt_text": "Horizontal timeline slider control for navigating temporal data visualizations in the KFM interface.",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in v9.0.0 for temporal browsing; revised in v9.5.0 for better visual contrast and adaptive design."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Steps**
- ✅ JSON schema validation (`schemas/ui/images.schema.json`)  
- 🔐 Cross-check with `/ui/checksums/widgets/` manifests  
- ♿ Accessibility audit to confirm alt text inclusion and clarity  
- 🧾 FAIR+CARE completeness validation (license, provenance, creator)  
- ⚖️ Provenance and checksum linkage verification  

Reports stored in:
- `reports/self-validation/web-images-ui-meta-widgets-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata indexed by ID and available in open repository search. |
| **Accessible (A)** | 100% | Stored in open, machine-readable JSON format. |
| **Interoperable (I)** | ≥95% | Structured for compatibility with STAC/DCAT metadata standards. |
| **Reusable (R)** | 100% | Includes provenance, checksum, and license documentation. |
| **Ethical (CARE)** | ≥90% | Authorship, accessibility, and ethics validated in FAIR+CARE audits. |

Telemetry metrics captured in `releases/v9.5.0/focus-telemetry.json` and visualized in the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** post-validation.  
- Each must include:
  - Author and license fields  
  - SHA-256 checksum reference  
  - Alt text and provenance record  
- Modifications require **Governance Council** approval with ledger documentation.  
- Deletion of metadata prohibited under archival governance law.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added metadata and checksum linkage for all widget image assets | Design Systems Team |
| v9.3.2 | 2025-10-20 | Integrated FAIR+CARE telemetry validation and accessibility compliance | Governance Council |
| v9.0.0 | 2025-09-25 | Created foundational metadata records for interactive widget assets | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Interactivity Documented · Metadata Immutable · Provenance Certified.”*

</div>

