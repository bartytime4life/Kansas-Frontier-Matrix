---
title: "📜 Kansas Frontier Matrix — Legacy Flag & Regional Marker Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/flags/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-icons-flags-legacy-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-icons-flags-legacy-meta-validation.json"
  - "../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Flag & Regional Marker Icon Metadata**
`web/public/icons/flags/legacy/meta/README.md`

**Purpose:** Stores and governs immutable metadata for all legacy flag and regional marker icons within the Kansas Frontier Matrix. These records document provenance, licensing, cultural permissions, and FAIR+CARE compliance to ensure ethical and traceable use of heritage and jurisdictional symbols.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/flags/legacy/meta/
├── icon-flag-usa-v1.json             # Metadata for early USA flag icon
├── icon-flag-kansas-v1.json          # Metadata for Kansas state flag icon
├── icon-flag-osage-v1.json           # Metadata for Osage Nation flag icon
├── icon-flag-kaw-v1.json             # Metadata for Kaw Nation (Kanza) flag
├── icon-flag-tribal-generic-v1.json  # Metadata for generic tribal flag
├── icon-flag-historical-v1.json      # Metadata for historical or treaty-era banner
└── README.md                         # This file
```

---

## 🧩 Metadata Schema

Each JSON file conforms to `schemas/ui/icons.schema.json`, ensuring interoperability with FAIR+CARE and STAC standards for cultural, historical, and geospatial metadata.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the icon (e.g., `icon-flag-osage-v1`). |
| `title` | string | Descriptive name of the flag or marker. |
| `category` | string | Logical grouping path (`flags/legacy`). |
| `version` | string | Semantic version of the icon asset. |
| `creator` | string | Author or cultural source responsible for design. |
| `license` | string | Legal license (MIT, CC-BY, Public Domain, or tribal permission note). |
| `checksum` | string | SHA-256 hash verifying immutability. |
| `deprecated` | string | Date when the icon was replaced. |
| `replaced_by` | string | Successor icon filename or identifier. |
| `source_url` | string | Link to authoritative design source (repository, archive, or tribal office). |
| `provenance` | string | Description of origin, purpose, and design context. |
| `cultural_permission_ref` | string | Reference or documentation of cultural permissions if applicable. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-flag-kaw-v1",
  "title": "Kanza (Kaw) Nation Flag (Legacy v1)",
  "category": "flags/legacy",
  "version": "1.0.0",
  "creator": "KFM Cultural Design Team",
  "license": "CC-BY 4.0",
  "checksum": "sha256-d71c1f0a91852b1a02bb4fd93210ceaf4b1f54...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-flag-kaw.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "cultural_permission_ref": "https://www.kawnation.com/?page_id=110",
  "provenance": "Used in v9.0.0 to represent Kaw Nation boundaries; replaced in v9.3.2 with updated proportion and verified cultural permission."
}
```

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Tasks**
- ✅ Schema validation (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum linkage verification with `/legacy/checksums/`  
- 🧾 FAIR+CARE completeness validation (license, provenance, author)  
- ⚖️ Cultural permissions verification and license audit  
- 🧭 Replacement mapping integrity check  

Reports stored in:
- `reports/self-validation/web-icons-flags-legacy-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All legacy metadata indexed by ID and title. |
| **Accessible (A)** | 100% | JSON files are open, machine-readable, and publicly auditable. |
| **Interoperable (I)** | ≥95% | Metadata aligned with STAC/DCAT standards for cultural datasets. |
| **Reusable (R)** | 100% | Provenance, license, and permissions are fully documented. |
| **Ethical (CARE)** | ≥90% | Ensures representation consent and authorship transparency. |

All results are aggregated in `releases/v9.5.0/focus-telemetry.json` for governance review.

---

## 🧱 Governance & Cultural Policies

- All metadata entries are **immutable post-merge**.  
- Any modifications require **Governance Council** and **Cultural Liaison** approval.  
- Each metadata record must include:
  - License type  
  - Creator attribution  
  - SHA-256 checksum  
  - Provenance explanation  
  - Cultural permission reference (if applicable)  
- Deletions are prohibited; historical data must remain traceable for audit reproducibility.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Implemented cultural permission verification and FAIR+CARE telemetry linkage | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum crosslinking and schema validation for heritage icons | Governance Council |
| v9.0.0 | 2025-09-25 | Created foundational metadata archive for legacy flag icons | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Flags of Heritage · Icons of Memory · Provenance in Perpetuity.”*

</div>

