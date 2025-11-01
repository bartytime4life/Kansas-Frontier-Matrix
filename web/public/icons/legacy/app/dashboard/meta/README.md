---
title: "📜 Kansas Frontier Matrix — Legacy Dashboard Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/dashboard/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-dashboard-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-dashboard-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Dashboard Icon Metadata**
`web/public/icons/legacy/app/dashboard/meta/README.md`

**Purpose:** Preserves comprehensive metadata for all legacy dashboard icons used in earlier Kansas Frontier Matrix versions. Documents authorship, licensing, and provenance while ensuring checksum linkage and FAIR+CARE audit compliance under MCP-DL v6.4.3 governance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/dashboard/meta/
├── icon-dashboard-overview-v1.json       # Metadata for overview icon
├── icon-dashboard-stats-v1.json          # Metadata for statistics icon
├── icon-dashboard-alerts-v1.json         # Metadata for alerts icon
├── icon-dashboard-activity-v1.json       # Metadata for activity indicator
├── icon-dashboard-performance-v1.json    # Metadata for performance icon
├── icon-dashboard-governance-v1.json     # Metadata for governance icon
└── README.md                             # This file
```

---

## 🧩 Metadata Schema

Metadata follows `schemas/ui/icons.schema.json`, ensuring consistency, interoperability, and FAIR+CARE documentation standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier (e.g., `icon-dashboard-performance-v1`). |
| `title` | string | Descriptive name of the icon. |
| `category` | string | Classification (`legacy/app/dashboard`). |
| `version` | string | Semantic version number of the icon asset. |
| `creator` | string | Original author or design contributor. |
| `license` | string | License type (MIT, CC-BY, Public Domain, etc.). |
| `checksum` | string | SHA-256 hash ensuring asset immutability. |
| `deprecated` | string | Date icon was replaced or deprecated. |
| `replaced_by` | string | Successor icon identifier or file name. |
| `source_url` | string | Repository or origin link for asset traceability. |
| `provenance` | string | Notes on design history, lineage, or replacement rationale. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-dashboard-governance-v1",
  "title": "Dashboard Governance Icon (Legacy v1)",
  "category": "legacy/app/dashboard",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-84de7c1f9a6c5be43a55e91f9134d78abf7b2b...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-dashboard-governance.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in KFM v9.0.0; replaced in v9.3.2 for standardization with governance telemetry UI icons."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Validation Tasks**
- ✅ JSON schema conformance check (`schemas/ui/icons.schema.json`)  
- 🔐 Cross-validation with `/legacy/app/dashboard/checksums/`  
- 🧾 FAIR+CARE completeness verification  
- ⚖️ License and author verification  
- 🧭 Provenance and replacement mapping audit  

Validation results are stored in:
- `reports/self-validation/web-icons-legacy-app-dashboard-meta-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All metadata entries indexed by ID and title. |
| **Accessible (A)** | 100% | Metadata stored in open JSON schema format. |
| **Interoperable (I)** | ≥95% | Metadata aligned with STAC/DCAT for exchange. |
| **Reusable (R)** | 100% | Provenance, checksum, and license fully recorded. |
| **Ethical (CARE)** | ≥90% | Authorship and governance validated under FAIR+CARE. |

Audit metrics published to `releases/v9.5.0/focus-telemetry.json` and synchronized with the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** post-commit.  
- Modifications require **Governance Council** approval and Ledger log entry.  
- Each record must include:
  - Author and license data  
  - SHA-256 checksum  
  - Provenance statement  
  - Replacement or successor mapping  
- Deletion of legacy metadata is strictly prohibited.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Created legacy dashboard metadata archive with FAIR+CARE telemetry linkage | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added schema validation and provenance integration | Governance Council |
| v9.0.0 | 2025-09-25 | Established metadata archive structure for dashboard icon assets | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Data Visuals Remembered · Provenance in Every Dashboard.”*

</div>

