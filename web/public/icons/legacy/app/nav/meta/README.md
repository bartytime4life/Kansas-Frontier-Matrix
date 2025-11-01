---
title: "📜 Kansas Frontier Matrix — Legacy Navigation Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/nav/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-nav-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-nav-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Navigation Icon Metadata**
`web/public/icons/legacy/app/nav/meta/README.md`

**Purpose:** Records detailed metadata for all deprecated navigation icons from previous Kansas Frontier Matrix interface versions. Provides complete provenance, authorship, licensing, and checksum linkage under FAIR+CARE and MCP-DL v6.4.3 compliance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/nav/meta/
├── icon-nav-home-v1.json         # Metadata for Home navigation icon
├── icon-nav-explore-v1.json      # Metadata for Explore icon
├── icon-nav-map-v1.json          # Metadata for Map navigation icon
├── icon-nav-data-v1.json         # Metadata for Data catalog icon
├── icon-nav-settings-v1.json     # Metadata for Settings icon
├── icon-nav-help-v1.json         # Metadata for Help/Info icon
├── icon-nav-login-v1.json        # Metadata for Login icon
├── icon-nav-logout-v1.json       # Metadata for Logout icon
└── README.md                     # This file
```

---

## 🧩 Metadata Schema

All metadata records conform to the KFM Icon Metadata Schema (`schemas/ui/icons.schema.json`) and align with FAIR+CARE, STAC, and DCAT interoperability principles.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (e.g., `icon-nav-home-v1`) |
| `title` | string | Human-readable name for the icon |
| `category` | string | Classification path (`legacy/app/nav`) |
| `version` | string | Semantic version number of the icon asset |
| `creator` | string | Original designer or author |
| `license` | string | License type (MIT, CC-BY, or Public Domain) |
| `checksum` | string | SHA-256 hash for file verification |
| `deprecated` | string | Date of icon deprecation |
| `replaced_by` | string | ID or filename of the successor icon |
| `source_url` | string | Repository or design reference URL |
| `provenance` | string | Description of design lineage, purpose, or replacement rationale |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-nav-explore-v1",
  "title": "Explore Navigation Icon (Legacy v1)",
  "category": "legacy/app/nav",
  "version": "1.0.0",
  "creator": "KFM UI Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-839c1b27e9a1b58e34f9e5e1c7d12a8426d94c...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-nav-explore.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Used in KFM v9.0.0 navigation; replaced by v9.3.2 version optimized for accessibility and color contrast compliance."
}
```

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Validation Steps**
- ✅ Schema validation using `schemas/ui/icons.schema.json`  
- 🔐 Cross-verification with `/legacy/app/nav/checksums/` directory  
- 🧾 FAIR+CARE metadata completeness check  
- ⚖️ License and author validation  
- 🧭 Provenance mapping validation  

Reports generated in:
- `reports/self-validation/web-icons-legacy-app-nav-meta-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata records indexed and retrievable by ID. |
| **Accessible (A)** | 100% | JSON metadata openly accessible and schema-compliant. |
| **Interoperable (I)** | ≥95% | Schema aligned with STAC/DCAT interoperability standards. |
| **Reusable (R)** | 100% | Licensing and provenance enable reusability and reproducibility. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and governance integrity upheld. |

Metrics results recorded in `releases/v9.5.0/focus-telemetry.json` and integrated into Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** once archived.  
- Each metadata record must include:
  - License and creator attribution  
  - SHA-256 checksum linkage  
  - Provenance documentation  
  - Replacement reference (if applicable)  
- Modification requires **Governance Council approval** and Ledger documentation.  
- No metadata deletion permitted; records are perpetual under FAIR+CARE compliance.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Established metadata archive for legacy navigation icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum linkage and FAIR+CARE validation tracking | Governance Council |
| v9.0.0 | 2025-09-25 | Created baseline metadata structure for deprecated navigation icons | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Every Route Recorded · Every Icon Provenanced · Every Legacy Preserved.”*

</div>

