---
title: "📜 Kansas Frontier Matrix — Legacy Navigation Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/meta/nav/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-meta-nav.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-meta-nav-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Navigation Icon Metadata**
`web/public/icons/legacy/app/meta/nav/README.md`

**Purpose:** Maintains metadata records for all deprecated navigation icons within Kansas Frontier Matrix. Ensures full traceability, checksum linkage, and FAIR+CARE-compliant governance of historical UI navigation assets.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/meta/nav/
├── icon-nav-home-v1.json          # Metadata for legacy home icon
├── icon-nav-explore-v1.json       # Metadata for explore icon
├── icon-nav-map-v1.json           # Metadata for map navigation icon
├── icon-nav-data-v1.json          # Metadata for data icon
├── icon-nav-settings-v1.json      # Metadata for settings icon
├── icon-nav-help-v1.json          # Metadata for help/info icon
├── icon-nav-login-v1.json         # Metadata for login icon
├── icon-nav-logout-v1.json        # Metadata for logout icon
└── README.md                      # This file
```

---

## 🧩 Metadata Schema

All entries conform to the official KFM Icon Metadata Schema (`schemas/ui/icons.schema.json`) to ensure transparency and interoperability with FAIR+CARE and STAC standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the icon (e.g., `icon-nav-home-v1`). |
| `title` | string | Human-readable name of the icon. |
| `category` | string | Classification (`legacy/app/nav`). |
| `version` | string | Semantic version of the icon. |
| `creator` | string | Original author or design source. |
| `license` | string | License type (MIT, CC-BY, or Public Domain). |
| `checksum` | string | SHA-256 checksum linking to validation record. |
| `deprecated` | string | Date of archival or deprecation. |
| `replaced_by` | string | ID or file name of successor icon. |
| `source_url` | string | Repository or design provenance URL. |
| `provenance` | string | Historical design context, usage, and rationale for deprecation. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-nav-settings-v1",
  "title": "Navigation Settings Icon (Legacy v1)",
  "category": "legacy/app/nav",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-b38ef1928ad8bfc0c21f7aeb8230a1c7f2e27b...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-nav-settings.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Used in KFM v9.0.0 as part of early navigation suite; replaced in v9.3.2 to align with accessibility and responsive design standards."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema conformance check for all JSON files (`schemas/ui/icons.schema.json`)  
- 🔐 Cross-verification with `/legacy/app/nav/checksums/` entries  
- 🧾 FAIR+CARE completeness audit  
- ⚖️ Author and license validation  
- 🧭 Provenance and replacement chain verification  

Results stored in:
- `reports/self-validation/web-icons-legacy-app-meta-nav-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All navigation metadata records indexed and retrievable by ID. |
| **Accessible (A)** | 100% | Metadata stored in open JSON format for transparency. |
| **Interoperable (I)** | ≥95% | Schema-compliant with STAC/DCAT exchange formats. |
| **Reusable (R)** | 100% | Includes complete provenance, license, and checksum. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and archival governance enforced. |

Audit results appended to `releases/v9.5.0/focus-telemetry.json` and displayed in the Governance Ledger.

---

## 🧱 Governance Policies

- Metadata files are **immutable** post-commit.  
- All records must include:
  - Creator and license attribution  
  - SHA-256 checksum linkage  
  - Replacement and provenance information  
- Modifications require **Governance Council** approval with ledger record.  
- Metadata deletion prohibited under archival governance law.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added complete metadata archive for legacy navigation icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Linked metadata with FAIR+CARE telemetry and checksum validation | Governance Council |
| v9.0.0 | 2025-09-25 | Created foundational legacy navigation metadata repository | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Navigating History · Preserving Provenance · Ensuring Integrity.”*

</div>

