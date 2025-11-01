---
title: "📜 Kansas Frontier Matrix — Legacy Certification & Governance Badge Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/badges/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-icons-badges-legacy-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-icons-badges-legacy-meta-validation.json"
  - "../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Certification & Governance Badge Metadata**
`web/public/icons/badges/legacy/meta/README.md`

**Purpose:** Documents immutable metadata for all legacy certification and governance badges in Kansas Frontier Matrix. Preserves authorship, licensing, provenance, and validation lineage under FAIR+CARE and MCP-DL v6.4.3 governance protocols for full traceability.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/badges/legacy/meta/
├── icon-badge-faircare-v1.json          # Metadata for legacy FAIR+CARE badge
├── icon-badge-diamond9-v1.json          # Metadata for legacy Diamond⁹ badge
├── icon-badge-crowninfinity-v1.json     # Metadata for legacy Crown∞Ω badge
├── icon-badge-mcpdl-v1.json             # Metadata for early MCP-DL compliance badge
├── icon-badge-iso27001-v1.json          # Metadata for legacy ISO 27001 compliance icon
├── icon-badge-accessibility-v1.json     # Metadata for early accessibility certification
├── icon-badge-audit-v1.json             # Metadata for deprecated audit validation badge
└── README.md                            # This file
```

---

## 🧩 Metadata Schema

All metadata records adhere to the **KFM Icon Metadata Schema** (`schemas/ui/icons.schema.json`), aligned with FAIR+CARE, STAC, and DCAT interoperability frameworks.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier (e.g., `icon-badge-faircare-v1`) |
| `title` | string | Human-readable title of the badge |
| `category` | string | Directory classification (`badges/legacy`) |
| `version` | string | Semantic version of the badge asset |
| `creator` | string | Author, council, or certifying organization |
| `license` | string | License type (MIT, CC-BY, ISO-proprietary, Public Domain) |
| `checksum` | string | SHA-256 hash ensuring immutability |
| `deprecated` | string | Date of archival or deprecation |
| `replaced_by` | string | Current badge ID or successor asset |
| `source_url` | string | Link to source or standard authority |
| `provenance` | string | Historical context or reasoning for retirement |
| `certification_ref` | string | Reference to certification or standard authority (e.g., ISO, FAIR, MCP-DL) |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-badge-faircare-v1",
  "title": "FAIR+CARE Certification Badge (Legacy v1)",
  "category": "badges/legacy",
  "version": "1.0.0",
  "creator": "KFM Governance Design Systems",
  "license": "CC-BY 4.0",
  "checksum": "sha256-82d4af1e9b345a6729ad27b65c84a11cd8ff9f...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-badge-faircare.svg",
  "source_url": "https://fairsharing.org/",
  "certification_ref": "https://go-fair.org/fair-principles/",
  "provenance": "Introduced in v9.0.0; replaced in v9.3.2 to align with updated FAIR+CARE compliance standards and improved accessibility."
}
```

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Tasks**
- ✅ JSON schema validation (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum cross-verification with `/legacy/checksums/` manifests  
- 🧾 FAIR+CARE metadata completeness validation  
- ⚖️ Certification and licensing verification  
- 🧭 Provenance replacement mapping validation  

Reports stored in:
- `reports/self-validation/web-icons-badges-legacy-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All legacy metadata indexed by ID and title. |
| **Accessible (A)** | 100% | JSON schema open for machine and human access. |
| **Interoperable (I)** | ≥95% | STAC/DCAT compliant for certification data exchange. |
| **Reusable (R)** | 100% | Provenance and licensing recorded for reuse and verification. |
| **Ethical (CARE)** | ≥90% | Ensures ethical representation of certification ownership. |

FAIR+CARE metrics logged in `releases/v9.5.0/focus-telemetry.json` and reviewed quarterly by the Governance Council.

---

## 🧱 Governance Policies

- Metadata records are **immutable** once archived.  
- Each record must include:
  - License  
  - Creator attribution  
  - SHA-256 checksum  
  - Certification reference  
  - Provenance description  
- Changes require **Governance Council** approval with ledger entry.  
- No deletions allowed; legacy data must remain permanently verifiable.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added checksum cross-validation and certification reference fields for badges | Design Systems Team |
| v9.3.2 | 2025-10-20 | Introduced FAIR+CARE validation and telemetry logging for legacy badges | Governance Council |
| v9.0.0 | 2025-09-25 | Created metadata archive for initial certification and governance badges | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Certifications Remembered · Provenance Preserved · Integrity Certified.”*

</div>

