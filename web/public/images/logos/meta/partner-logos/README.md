---
title: "📜 Kansas Frontier Matrix — Partner & Institutional Logo Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/images/logos/meta/partner-logos/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-images-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-images-logos-meta-partners.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-images-logos-meta-partners-validation.json"
  - "../../../../../../../reports/audit/web-images-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Partner & Institutional Logo Metadata**
`web/public/images/logos/meta/partner-logos/README.md`

**Purpose:** Manages detailed metadata for all active partner and institutional logos displayed within Kansas Frontier Matrix. Ensures each logo’s provenance, license, checksum, and accessibility compliance are verifiable under FAIR+CARE and MCP-DL v6.4.3 governance standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Metadata Integrity](https://img.shields.io/badge/Metadata-Immutable-critical)](../../../../../../../reports/audit/web-images-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/images/logos/meta/partner-logos/
├── ku-logo.json                     # Metadata for University of Kansas logo
├── kgs-logo.json                    # Metadata for Kansas Geological Survey logo
├── nsf-logo.json                    # Metadata for National Science Foundation logo
├── usgs-logo.json                   # Metadata for U.S. Geological Survey logo
├── noaa-logo.json                   # Metadata for NOAA collaboration logo
├── openai-logo.json                 # Metadata for OpenAI partnership logo
└── README.md                        # This file
```

---

## 🧩 Metadata Schema

All metadata conforms to the **KFM Image Metadata Schema** (`schemas/ui/images.schema.json`), which aligns with FAIR+CARE, STAC, and DCAT interoperability standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier (e.g., `noaa-logo`). |
| `title` | string | Descriptive title for the logo asset. |
| `category` | string | Directory classification (`logos/meta/partner-logos`). |
| `version` | string | Semantic version of the logo asset. |
| `creator` | string | Partner organization or contributing institution. |
| `license` | string | License (MIT, CC-BY, Public Domain, or Partner Agreement). |
| `checksum` | string | SHA-256 hash linking to the integrity manifest. |
| `alt_text` | string | Accessibility text for assistive technologies. |
| `source_url` | string | Official URL for organization or logo source. |
| `provenance` | string | Historical or contextual background of the asset. |

---

## 🧾 Example Metadata Record

```json
{
  "id": "noaa-logo",
  "title": "National Oceanic and Atmospheric Administration Logo",
  "category": "logos/meta/partner-logos",
  "version": "2.0.0",
  "creator": "National Oceanic and Atmospheric Administration (NOAA)",
  "license": "Public Domain (U.S. Government)",
  "checksum": "sha256-982ac75a3fef94a15b3efc4b7a2b04a93d1e91...",
  "alt_text": "NOAA circular logo showing a stylized seabird above ocean waves in blue and white.",
  "source_url": "https://www.noaa.gov/",
  "provenance": "Updated NOAA collaboration logo adopted in v9.5.0 after branding refresh; replaces legacy NOAA v1 logo archived in /logos/archive/partner-logos/."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/image-meta-validate.yml`

**Automated Validation Tasks**
- ✅ Schema conformance check (`schemas/ui/images.schema.json`)  
- 🔐 Cross-verification with `/logos/checksums/partner-logos/` manifests  
- 🧾 FAIR+CARE completeness validation (license, creator, provenance)  
- ⚖️ License compliance and authorship verification  
- 🧭 Provenance and replacement mapping validation  

Reports recorded in:
- `reports/self-validation/web-images-logos-meta-partners-validation.json`
- `reports/audit/web-images-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | Metadata indexed and searchable by ID and title. |
| **Accessible (A)** | 100% | Stored in open, machine-readable JSON format. |
| **Interoperable (I)** | ≥95% | Compatible with STAC/DCAT schema structures. |
| **Reusable (R)** | 100% | Fully documented provenance and licensing. |
| **Ethical (CARE)** | ≥90% | Authorship and ethical partnership validation. |

Telemetry results integrated with `releases/v9.5.0/focus-telemetry.json` and displayed on the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** post-approval.  
- Each file must include:
  - License and creator attribution  
  - SHA-256 checksum linkage  
  - Provenance and accessibility text  
- All modifications require **Governance Council** approval with ledger recording.  
- Metadata deletions are strictly prohibited under archival governance rules.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Established metadata directory for partner and institutional logos with FAIR+CARE governance integration | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum linkage and license validation under FAIR+CARE framework | Governance Council |
| v9.0.0 | 2025-09-25 | Created initial metadata repository for institutional partnerships | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Integrity in Partnership · Transparency in Governance · Provenance in Design.”*

</div>

