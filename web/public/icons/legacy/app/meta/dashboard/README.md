---
title: "📜 Kansas Frontier Matrix — Legacy Dashboard Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/meta/dashboard/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-meta-dashboard.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-meta-dashboard-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Dashboard Icon Metadata**
`web/public/icons/legacy/app/meta/dashboard/README.md`

**Purpose:** Archives metadata for all deprecated dashboard icons from previous Kansas Frontier Matrix interface versions. Captures full provenance, authorship, checksum linkage, and FAIR+CARE-compliant validation for transparency and reproducibility.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/meta/dashboard/
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

All metadata records adhere to the official **KFM Icon Metadata Schema** (`schemas/ui/icons.schema.json`) and conform to FAIR+CARE, STAC, and DCAT interoperability standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (e.g., `icon-dashboard-performance-v1`) |
| `title` | string | Human-readable name for the icon. |
| `category` | string | Directory classification (`legacy/app/dashboard`). |
| `version` | string | Semantic version of the icon asset. |
| `creator` | string | Author or original design source. |
| `license` | string | License type (MIT, CC-BY, Public Domain). |
| `checksum` | string | SHA-256 hash ensuring immutability. |
| `deprecated` | string | Date the icon was deprecated. |
| `replaced_by` | string | Successor icon filename or ID. |
| `source_url` | string | Repository or design reference link. |
| `provenance` | string | Historical context and reason for replacement. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-dashboard-overview-v1",
  "title": "Dashboard Overview Icon (Legacy v1)",
  "category": "legacy/app/dashboard",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-1b5f83ce70f48ea7b90cfa1a58324783db78b9...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-dashboard-overview.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Originally used in v9.0.0 for dashboard summary cards; replaced in v9.3.2 with updated layout and color accessibility improvements."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema conformance (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum verification linkage (`/legacy/app/dashboard/checksums/`)  
- 🧾 FAIR+CARE completeness validation  
- ⚖️ License and author attribution verification  
- 🧭 Provenance chain and replacement reference validation  

Results recorded in:
- `reports/self-validation/web-icons-legacy-app-meta-dashboard-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata records indexed by unique ID and title. |
| **Accessible (A)** | 100% | JSON metadata stored in open, human-readable schema. |
| **Interoperable (I)** | ≥95% | Schema aligns with STAC/DCAT metadata exchange standards. |
| **Reusable (R)** | 100% | Metadata includes full provenance, license, and checksum. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and audit governance maintained. |

Audit metrics appended to `releases/v9.5.0/focus-telemetry.json` and visualized in the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable post-commit**.  
- Every entry must include:
  - License and author information  
  - SHA-256 checksum linkage  
  - Replacement mapping  
  - Provenance rationale  
- All changes require **Governance Council approval** and ledger documentation.  
- Metadata deletions are **strictly prohibited** to preserve audit history.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Established metadata archive for legacy dashboard icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum cross-link and FAIR+CARE audit integration | Governance Council |
| v9.0.0 | 2025-09-25 | Created dashboard metadata structure for historical UI provenance | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Every Dashboard Documented · Every Metric Provenanced · Every Record Immutable.”*

</div>

