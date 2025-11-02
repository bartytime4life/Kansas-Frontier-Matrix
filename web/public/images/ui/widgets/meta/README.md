---
title: "📜 Kansas Frontier Matrix — UI Widget Image Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/ui/widgets/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-images-ui-widgets-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-images-ui-widgets-meta-validation.json"
  - "../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **UI Widget Image Metadata**
`web/public/images/ui/widgets/meta/README.md`

**Purpose:** Contains metadata for all interactive widget image assets in the Kansas Frontier Matrix web interface. Each entry includes provenance, licensing, and checksum linkage, ensuring verifiable FAIR+CARE compliance and reproducible UI design governance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Metadata Integrity](https://img.shields.io/badge/Metadata-Immutable-critical)](../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/ui/widgets/meta/
├── map-zoom-controls.json          # Metadata for map zoom control widget
├── timeline-slider.json            # Metadata for timeline slider widget
├── chart-frame.json                # Metadata for chart frame overlay
├── data-legend-panel.json          # Metadata for data legend widget
├── heatmap-overlay.json            # Metadata for heatmap overlay background
└── README.md                       # This file
```

---

## 🧩 Metadata Schema

All metadata conforms to the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`) and complies with FAIR+CARE, STAC, and DCAT interoperability standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the widget asset (e.g., `timeline-slider`). |
| `title` | string | Human-readable name of the widget image. |
| `category` | string | Directory classification (`ui/widgets`). |
| `version` | string | Semantic version number for the asset. |
| `creator` | string | Author, designer, or team responsible for creation. |
| `license` | string | License type (MIT, CC-BY, Public Domain). |
| `checksum` | string | SHA-256 hash verifying file integrity. |
| `alt_text` | string | Accessibility description of the widget image. |
| `source_url` | string | Repository or source reference for the asset. |
| `provenance` | string | Historical or contextual notes explaining design purpose, revisions, or usage. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "data-legend-panel",
  "title": "Data Legend Panel Widget",
  "category": "ui/widgets",
  "version": "1.4.0",
  "creator": "KFM Design Systems",
  "license": "MIT",
  "checksum": "sha256-2fbb6d1ae34241bc9a84b17f93dc49ac8cb221...",
  "alt_text": "Interactive data legend displaying map layers and color keys.",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in v9.2.0 for map visualizations; updated in v9.5.0 for adaptive layout and improved color contrast compliance."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema validation (`schemas/ui/images.schema.json`)  
- 🔐 Cross-verification with `/ui/widgets/checksums/` manifests  
- 🧾 FAIR+CARE completeness validation (license, provenance, checksum linkage)  
- ♿ Accessibility audit for alt text and descriptive content  
- ⚖️ License verification and authorship validation  

Audit results stored in:
- `reports/self-validation/web-images-ui-widgets-meta-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata indexed by unique ID and searchable within repository. |
| **Accessible (A)** | 100% | JSON metadata stored in open, machine-readable format. |
| **Interoperable (I)** | ≥95% | Schema structured for STAC/DCAT compliance. |
| **Reusable (R)** | 100% | License, checksum, and provenance recorded for reuse. |
| **Ethical (CARE)** | ≥90% | Verified authorship and ethical design documentation under FAIR+CARE audits. |

Metrics aggregated in `releases/v9.5.0/focus-telemetry.json` and visualized in the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable post-validation** to preserve provenance.  
- Each record must include:
  - License and creator attribution  
  - SHA-256 checksum linkage  
  - Accessibility description (`alt_text`)  
  - Provenance and usage notes  
- Modifications require **Governance Council** approval and recorded ledger entry.  
- Metadata deletion prohibited under FAIR+CARE archival governance.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Created comprehensive metadata governance for all widget image assets | Design Systems Team |
| v9.3.2 | 2025-10-20 | Integrated FAIR+CARE audit telemetry and accessibility validation | Governance Council |
| v9.0.0 | 2025-09-25 | Established widget image metadata structure for interactive visualization assets | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Interactivity Preserved · Metadata Verified · Provenance Immutable.”*

</div>

