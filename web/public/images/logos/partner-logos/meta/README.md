---
title: "📜 Kansas Frontier Matrix — Partner & Institutional Logo Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/logos/partner-logos/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-images-logos-partners-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-images-logos-partners-meta-validation.json"
  - "../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Partner & Institutional Logo Metadata**
`web/public/images/logos/partner-logos/meta/README.md`

**Purpose:** Documents the metadata, provenance, and licensing information for all active partner and institutional logos within Kansas Frontier Matrix. Enables transparent FAIR+CARE-compliant governance and audit verification for all co-branded assets used on the platform.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/logos/partner-logos/meta/
├── ku-logo.json                     # Metadata for University of Kansas logo
├── kgs-logo.json                    # Metadata for Kansas Geological Survey logo
├── usgs-logo.json                   # Metadata for U.S. Geological Survey logo
├── nsf-logo.json                    # Metadata for National Science Foundation logo
├── noaa-logo.json                   # Metadata for NOAA logo
├── openai-logo.json                 # Metadata for OpenAI partner logo
└── README.md                        # This file
```

---

## 🧩 Metadata Schema

All metadata conforms to the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`) and adheres to FAIR+CARE, STAC, and DCAT interoperability standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier for the partner logo (e.g., `usgs-logo`). |
| `title` | string | Descriptive title of the partner or institution. |
| `category` | string | Directory classification (`logos/partner-logos`). |
| `version` | string | Semantic version of the logo asset. |
| `creator` | string | Partner organization or institutional creator. |
| `license` | string | License type (MIT, CC-BY, Public Domain, or Partner Agreement). |
| `checksum` | string | SHA-256 hash verifying immutability. |
| `alt_text` | string | Accessible description of the logo for screen readers. |
| `source_url` | string | Official website or documentation URL. |
| `provenance` | string | Explanation of the logo’s usage, history, and governance context. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "usgs-logo",
  "title": "U.S. Geological Survey Logo",
  "category": "logos/partner-logos",
  "version": "1.0.0",
  "creator": "U.S. Geological Survey",
  "license": "Public Domain (US Government)",
  "checksum": "sha256-51a9f8239a7b83c4cf9c2c6b293e8db29e0d92...",
  "alt_text": "U.S. Geological Survey logo featuring green and white mountain stripes with text 'USGS Science for a Changing World'.",
  "source_url": "https://www.usgs.gov/",
  "provenance": "Approved partner logo under Public Domain terms for official use on Kansas Frontier Matrix partner page."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Tasks**
- ✅ JSON schema validation (`schemas/ui/images.schema.json`)  
- 🔐 Cross-verification with `/partner-logos/checksums/` manifests  
- 🧾 FAIR+CARE completeness validation (license, creator, provenance)  
- ⚖️ License type and author verification  
- 🧭 Provenance mapping and audit trail recording  

Reports stored in:
- `reports/self-validation/web-images-logos-partners-meta-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata indexed by unique ID and accessible in JSON format. |
| **Accessible (A)** | 100% | All records available in open, machine-readable format. |
| **Interoperable (I)** | ≥95% | Schema aligned with STAC/DCAT data exchange standards. |
| **Reusable (R)** | 100% | License and provenance documentation ensures reuse compliance. |
| **Ethical (CARE)** | ≥90% | Verified authorship and FAIR+CARE audit alignment. |

Results integrated with `releases/v9.5.0/focus-telemetry.json` and the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata is **immutable** after approval to ensure archival integrity.  
- Each record must contain:
  - License and attribution  
  - SHA-256 checksum reference  
  - Provenance statement and alt text  
- Any modifications require **Governance Council approval** and ledger documentation.  
- Metadata deletion is strictly prohibited.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added full metadata archive for active partner and institutional logos | Design Systems Team |
| v9.3.2 | 2025-10-20 | Integrated FAIR+CARE telemetry and license compliance validation | Governance Council |
| v9.0.0 | 2025-09-25 | Created initial partner metadata directory with checksum cross-validation | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Integrity in Collaboration · Provenance in Partnership · Transparency in Governance.”*

</div>

