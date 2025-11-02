---
title: "📜 Kansas Frontier Matrix — Archived Partner Logo Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/logos/partner-logos/archive/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-images-logos-partners-archive-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-images-logos-partners-archive-meta-validation.json"
  - "../../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Archived Partner Logo Metadata**
`web/public/images/logos/partner-logos/archive/meta/README.md`

**Purpose:** Documents metadata for all retired or superseded partner and institutional logos once featured in Kansas Frontier Matrix collaborations. Ensures checksum linkage, license retention, provenance history, and FAIR+CARE-compliant transparency for every archived asset.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/logos/partner-logos/archive/meta/
├── ku-logo-v1.json                # Metadata for University of Kansas legacy logo
├── kgs-logo-v1.json               # Metadata for Kansas Geological Survey legacy logo
├── nsf-logo-v1.json               # Metadata for National Science Foundation logo
├── noaa-logo-v1.json              # Metadata for NOAA collaboration logo
├── openai-logo-v1.json            # Metadata for OpenAI research partner logo
└── README.md                      # This file
```

---

## 🧩 Metadata Schema

All metadata records comply with the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`), ensuring FAIR+CARE interoperability and archival transparency.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the logo (e.g., `nsf-logo-v1`). |
| `title` | string | Descriptive name for the archived logo. |
| `category` | string | Directory classification (`logos/partner-logos/archive`). |
| `version` | string | Semantic version identifier. |
| `creator` | string | Original author, institution, or agency. |
| `license` | string | License type (MIT, CC-BY, Public Domain, or Partner Agreement). |
| `checksum` | string | SHA-256 hash ensuring integrity. |
| `deprecated` | string | Date the logo was retired or replaced. |
| `replaced_by` | string | Identifier or filename of the successor logo. |
| `source_url` | string | Official source or documentation URL. |
| `alt_text` | string | Accessibility description of the logo’s visual appearance. |
| `provenance` | string | Summary of logo’s historical use and retirement rationale. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "noaa-logo-v1",
  "title": "NOAA Collaboration Logo (Legacy v1)",
  "category": "logos/partner-logos/archive",
  "version": "1.0.0",
  "creator": "National Oceanic and Atmospheric Administration (NOAA)",
  "license": "Public Domain (U.S. Government)",
  "checksum": "sha256-36cb15a7c23e89fa95b47bdf1c14ad9e90fa1a...",
  "deprecated": "2025-09-25",
  "replaced_by": "noaa-logo.svg",
  "source_url": "https://www.noaa.gov/",
  "alt_text": "Legacy NOAA logo with circular blue design featuring seabird and waves.",
  "provenance": "Used in KFM partnership displays between v9.0.0 and v9.3.2; replaced to align with NOAA’s official 2025 rebrand."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema conformance validation (`schemas/ui/images.schema.json`)  
- 🔐 Cross-verification with `/archive/checksums/` directory  
- 🧾 FAIR+CARE completeness audit (license, attribution, provenance)  
- ⚖️ License and creator verification  
- 🧭 Provenance and replacement mapping review  

Audit results recorded in:
- `reports/self-validation/web-images-logos-partners-archive-meta-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All metadata entries indexed and searchable by ID. |
| **Accessible (A)** | 100% | Metadata stored in open, human-readable JSON format. |
| **Interoperable (I)** | ≥95% | Conforms to STAC/DCAT exchange and archival data structures. |
| **Reusable (R)** | 100% | Includes license, provenance, and checksum for reuse assurance. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and ethical usage validated under FAIR+CARE audits. |

All results are integrated into the **Governance Ledger Dashboard** via telemetry (`releases/v9.5.0/focus-telemetry.json`).

---

## 🧱 Governance Policies

- Metadata files are **immutable post-approval** and subject to Governance Council oversight.  
- Each file must contain:
  - License, creator, and checksum references  
  - Provenance and successor linkage  
  - Accessibility description (`alt_text`)  
- Modifications require Governance Council approval and a recorded ledger event.  
- Metadata deletions are **strictly prohibited** for audit preservation.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Introduced full metadata governance for archived partner logos | Design Systems Team |
| v9.3.2 | 2025-10-20 | Linked metadata schema validation with FAIR+CARE telemetry | Governance Council |
| v9.0.0 | 2025-09-25 | Created foundational archive for institutional logo metadata | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Partnerships Remembered · Metadata Preserved · Integrity Eternal.”*

</div>

