---
title: "📜 Kansas Frontier Matrix — Archived Partner Logo Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/logos/archive/partner-logos/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-images-logos-archive-partners-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-images-logos-archive-partners-meta-validation.json"
  - "../../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Archived Partner Logo Metadata**
`web/public/images/logos/archive/partner-logos/meta/README.md`

**Purpose:** Stores metadata for all deprecated or retired partner and institutional logos used in Kansas Frontier Matrix. Each record documents license, provenance, checksum linkage, and FAIR+CARE-compliant governance alignment for transparent archival stewardship.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/logos/archive/partner-logos/meta/
├── ku-logo-v1.json                   # Metadata for University of Kansas legacy logo
├── kgs-logo-v1.json                  # Metadata for Kansas Geological Survey legacy logo
├── nsf-logo-v1.json                  # Metadata for National Science Foundation legacy logo
├── usgs-logo-v1.json                 # Metadata for U.S. Geological Survey legacy logo
├── noaa-logo-v1.json                 # Metadata for NOAA legacy logo
├── openai-logo-v1.json               # Metadata for OpenAI partnership logo (retired)
└── README.md                         # This file
```

---

## 🧩 Metadata Schema

All metadata follows the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`), ensuring transparency and interoperability under FAIR+CARE and STAC/DCAT archival models.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the logo (e.g., `usgs-logo-v1`). |
| `title` | string | Human-readable name of the logo. |
| `category` | string | Directory classification (`logos/archive/partner-logos`). |
| `version` | string | Semantic version of the archived asset. |
| `creator` | string | Author, agency, or institutional owner. |
| `license` | string | License type (MIT, CC-BY, Public Domain, Partner Agreement). |
| `checksum` | string | SHA-256 hash ensuring immutability and file integrity. |
| `deprecated` | string | Date the logo was retired or replaced. |
| `replaced_by` | string | Reference to updated logo filename or ID. |
| `source_url` | string | Official organization or publication URL. |
| `alt_text` | string | Accessibility description for screen readers. |
| `provenance` | string | Description of logo’s historical use, retirement reason, and replacement context. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "usgs-logo-v1",
  "title": "U.S. Geological Survey Logo (Legacy v1)",
  "category": "logos/archive/partner-logos",
  "version": "1.0.0",
  "creator": "U.S. Geological Survey",
  "license": "Public Domain (U.S. Government)",
  "checksum": "sha256-37b9a2de51e4e83c72a1d4a8d13bfe92a5b12f...",
  "deprecated": "2025-09-25",
  "replaced_by": "usgs-logo.svg",
  "source_url": "https://www.usgs.gov/",
  "alt_text": "Legacy USGS logo with green striped mountains and text reading 'USGS Science for a Changing World'.",
  "provenance": "Used in Kansas Frontier Matrix partnership materials between 2023–2025. Retired in v9.5.0 following official USGS brand update."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema conformance (`schemas/ui/images.schema.json`)  
- 🔐 Cross-verification with `/archive/partner-logos/checksums/` directory  
- 🧾 FAIR+CARE completeness check (license, attribution, provenance)  
- ⚖️ Author and institution verification  
- 🧭 Provenance and replacement mapping validation  

Reports are stored in:
- `reports/self-validation/web-images-logos-archive-partners-meta-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All metadata entries indexed and searchable by ID. |
| **Accessible (A)** | 100% | JSON metadata stored in open, machine-readable format. |
| **Interoperable (I)** | ≥95% | Conforms to STAC/DCAT data interoperability standards. |
| **Reusable (R)** | 100% | License, provenance, and checksum included for safe reuse. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and ethical representation validated via audits. |

Metrics published in `releases/v9.5.0/focus-telemetry.json` and visualized on the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** post-merge and protected via Governance Council oversight.  
- Each record must include:
  - License and creator information  
  - SHA-256 checksum  
  - Provenance, replacement, and accessibility details  
- Edits require **Governance Council approval** and ledger entry.  
- Metadata deletion is prohibited under archival governance standards.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Established immutable metadata framework for archived partner logos | Design Systems Team |
| v9.3.2 | 2025-10-20 | Integrated metadata validation with FAIR+CARE telemetry | Governance Council |
| v9.0.0 | 2025-09-25 | Created archival metadata structure for institutional and partner branding | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Partnerships Preserved · Metadata Immutable · Provenance Documented.”*

</div>

