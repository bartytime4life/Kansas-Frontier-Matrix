---
title: "📜 Kansas Frontier Matrix — Legacy Dashboard Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/app/dashboard/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-app-dashboard-legacy-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-app-dashboard-legacy-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Dashboard Icon Metadata**
`web/public/icons/app/dashboard/legacy/meta/README.md`

**Purpose:** Documents metadata for all deprecated dashboard icons used across historical Kansas Frontier Matrix interface releases. Preserves authorship, licensing, and provenance under FAIR+CARE and MCP-DL v6.4.3 standards for full design transparency and reproducibility.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/app/dashboard/legacy/meta/
├── icon-dashboard-overview-v1.json       # Metadata for original dashboard overview icon
├── icon-dashboard-stats-v1.json          # Metadata for early statistical summary icon
├── icon-dashboard-alerts-v1.json         # Metadata for alerts/notifications icon
├── icon-dashboard-performance-v1.json    # Metadata for performance metrics icon
├── icon-dashboard-activity-v1.json       # Metadata for historical activity indicator
└── README.md                             # This file
```

---

## 🧩 Metadata Schema

Each metadata JSON record adheres to `schemas/ui/icons.schema.json` and aligns with FAIR+CARE documentation principles.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (e.g., `icon-dashboard-stats-v1`) |
| `title` | string | Human-readable icon name |
| `category` | string | Directory classification (`app/dashboard/legacy`) |
| `version` | string | Semantic version number of the legacy asset |
| `creator` | string | Designer or team responsible for creation |
| `license` | string | License type (MIT, CC-BY, or Public Domain) |
| `checksum` | string | SHA-256 hash ensuring file immutability |
| `deprecated` | string | Date of icon deprecation |
| `replaced_by` | string | ID or filename of current successor icon |
| `source_url` | string | Link to repository or original asset |
| `provenance` | string | Historical note describing lineage, design context, and replacement rationale |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-dashboard-alerts-v1",
  "title": "Dashboard Alerts Icon (Legacy v1)",
  "category": "app/dashboard/legacy",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-8ba31f7a1b73f4a92decb5b1e0f2b92f1a7d1e6...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-dashboard-alerts.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in v9.0.0 dashboard suite; retired in v9.3.2 to improve visibility and color contrast for WCAG 2.2 AA compliance."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Checks**
- ✅ JSON schema conformance validation (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum cross-verification with `/legacy/checksums/` directory  
- 🧾 FAIR+CARE completeness audit (all required metadata fields present)  
- ⚖️ License & provenance consistency check  
- 📜 Replacement mapping validation (each deprecated icon must specify successor)  

Results stored in:
- `reports/self-validation/web-icons-app-dashboard-legacy-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All legacy records indexed and discoverable by ID. |
| **Accessible (A)** | 100% | Open JSON schema compliant; no proprietary formats. |
| **Interoperable (I)** | ≥95% | STAC-compatible schema structure and metadata fields. |
| **Reusable (R)** | 100% | Provenance, license, and creator fields documented. |
| **CARE (Ethical)** | ≥90% | Ensures attribution transparency and immutability enforcement. |

Telemetry results integrated into `releases/v9.5.0/focus-telemetry.json`.

---

## 🧱 Governance Policies

- All legacy metadata files are **immutable once merged**.  
- Modifications require **formal approval** via the Design Systems Governance Council.  
- Each record must include:
  - License type  
  - Creator/author  
  - SHA-256 checksum  
  - Replacement mapping  
  - Provenance statement  
- Deletion of files is **prohibited** to maintain full provenance traceability.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Standardized legacy dashboard metadata schema & FAIR+CARE validation | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum linkage and telemetry-based governance integration | Governance Council |
| v9.0.0 | 2025-09-25 | Created initial legacy dashboard metadata records for historical UI elements | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Metadata is Memory · Provenance is Integrity · Transparency is Design.”*

</div>

