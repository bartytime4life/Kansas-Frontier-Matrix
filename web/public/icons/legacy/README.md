---
title: "🕰 Kansas Frontier Matrix — Global Legacy Icon Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../releases/v9.5.0/web-icons-legacy.meta.json"
validation_reports:
  - "../../../../reports/self-validation/web-icons-legacy-validation.json"
  - "../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🕰 Kansas Frontier Matrix — **Global Legacy Icon Archive**
`web/public/icons/legacy/README.md`

**Purpose:** Serves as the centralized archival repository for *all deprecated, superseded, or retired* icons across the Kansas Frontier Matrix system. Ensures full provenance, licensing transparency, checksum integrity, and FAIR+CARE-compliant immutability under MCP-DL v6.4.3 governance standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../docs/standards/governance/LEDGER.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Immutable-critical)](../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/
├── app/                 # Application-specific legacy icons (UI, panels, nav)
├── data/                # Data domain legacy icons (datasets, hazards, treaties)
├── system/              # System and governance legacy icons
├── social/              # Communication and collaboration legacy icons
├── flags/               # Regional, tribal, and national marker archives
├── badges/              # Certification and audit badge legacy archive
├── checksums/           # Global SHA-256 integrity manifests
├── meta/                # Aggregated legacy metadata JSON files
└── README.md            # This file
```

---

## 🧩 Governance Purpose

This directory consolidates **all legacy visual assets** across the KFM platform.  
It exists to ensure historical fidelity, transparency, and reproducibility in visual governance.

**Core Principles**
- 🔐 **Integrity:** Each archived file carries a verified SHA-256 checksum.  
- 🧾 **Provenance:** All legacy assets include documented metadata (creator, license, replacement, checksum).  
- ♿ **Accessibility Preservation:** Historical accessibility data retained for compliance validation.  
- 🧭 **FAIR+CARE Governance:** All archives adhere to ethical stewardship and open documentation standards.  

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-archive-validate.yml`

**Automated Tasks**
- ✅ Validate all metadata using `schemas/ui/icons.schema.json`  
- 🔐 Verify SHA-256 checksums against `/checksums/` manifests  
- 🧾 Run FAIR+CARE compliance audits  
- ⚖️ Cross-reference metadata with replacement mappings  
- 📜 Update telemetry logs and governance dashboards  

Reports stored in:
- `reports/self-validation/web-icons-legacy-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🧾 Example Legacy Metadata Record

```json
{
  "id": "icon-nav-home-v1",
  "title": "Home Navigation Icon (Legacy v1)",
  "category": "app/nav/legacy",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-51adfbe612f92f7aa8f0d81eac3f2b02ed1c9e...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-nav-home.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Used in KFM v9.0.0 UI; replaced by new accessible variant in v9.3.2."
}
```

---

## 🔒 Archive & Compliance Policy

| Policy | Description | Enforcement |
|--------|-------------|--------------|
| **Immutable Archive** | No legacy files may be altered or deleted. | Protected branches and governance review. |
| **Checksum Enforcement** | Every legacy SVG includes verified SHA-256 hash. | CI/CD validation and audit checks. |
| **Replacement Mapping** | All deprecated assets must specify successor. | Schema validation required. |
| **License & Attribution** | Each record declares author and licensing source. | FAIR+CARE audit enforcement. |
| **Cultural & Ethical Stewardship** | Icons of cultural significance include permission or attribution documentation. | FAIR+CARE ethical review. |

---

## 📊 Telemetry & FAIR+CARE Metrics

Telemetry data (logged in `releases/v9.5.0/focus-telemetry.json`) tracks:
- ✅ Total legacy icons archived  
- 📜 Metadata completeness rate  
- 🔐 Checksum verification success  
- ♿ Accessibility regression comparison  
- 💠 FAIR+CARE ethical compliance index  

All telemetry outputs feed directly into the **Governance Ledger Dashboard** for quarterly audit review.

---

## 🧱 Directory Integration

This directory connects all legacy branches:
- `app/` — Application UI components (navigation, timeline, panels).  
- `data/` — Dataset-based icons (climate, hydrology, hazards).  
- `system/` — Governance, audit, and validation icons.  
- `social/` — Collaboration and outreach channels.  
- `flags/` — Regional and cultural iconography.  
- `badges/` — Certification and compliance insignia.  

Each subdirectory has its own:
- `/checksums/` — for SHA-256 verification.  
- `/meta/` — for metadata archival.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Unified all legacy icon archives under central governance structure | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum linkage, FAIR+CARE telemetry, and accessibility records | Governance Council |
| v9.0.0 | 2025-09-25 | Established global legacy archive for all historical icon families | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Every Icon Tells a Story · Every Version Holds a Record · Every Record Remains Immutable.”*

</div>

