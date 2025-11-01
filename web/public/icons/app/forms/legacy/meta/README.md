---
title: "📜 Kansas Frontier Matrix — Legacy Form & Input Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/app/forms/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-app-forms-legacy-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-app-forms-legacy-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Form & Input Icon Metadata**
`web/public/icons/app/forms/legacy/meta/README.md`

**Purpose:** Provides immutable metadata for deprecated form and input icons within the Kansas Frontier Matrix interface. Documents each asset’s authorship, licensing, and provenance, ensuring full FAIR+CARE and MCP-DL v6.4.3 compliance with reproducibility, traceability, and audit transparency.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/app/forms/legacy/meta/
├── icon-form-save-v1.json         # Metadata for save icon (legacy)
├── icon-form-edit-v1.json         # Metadata for edit icon (legacy)
├── icon-form-delete-v1.json       # Metadata for delete icon (legacy)
├── icon-form-add-v1.json          # Metadata for add icon (legacy)
├── icon-form-warning-v1.json      # Metadata for warning icon (legacy)
├── icon-form-error-v1.json        # Metadata for error icon (legacy)
└── README.md                      # This file
```

---

## 🧩 Metadata Schema

All JSON files conform to `schemas/ui/icons.schema.json`, harmonized with FAIR+CARE, STAC, and schema.org metadata conventions.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique asset identifier (e.g., `icon-form-add-v1`) |
| `title` | string | Human-readable name of icon |
| `category` | string | Directory classification path (`app/forms/legacy`) |
| `version` | string | Semantic version of asset |
| `creator` | string | Original designer or author |
| `license` | string | Asset license (MIT, CC-BY 4.0, or Public Domain) |
| `checksum` | string | SHA-256 checksum for file immutability validation |
| `deprecated` | string | Date the asset was retired |
| `replaced_by` | string | Successor icon filename |
| `source_url` | string | Repository or design asset source link |
| `provenance` | string | Summary of design lineage, usage, and replacement rationale |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-form-delete-v1",
  "title": "Form Delete Icon (Legacy v1)",
  "category": "app/forms/legacy",
  "version": "1.0.0",
  "creator": "KFM UI Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-8f74dc01b2e1a5f9d3b42abf2aa7e918f19ef3...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-form-delete.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Deployed in KFM v9.0.0 form module; replaced for modern styling and color accessibility compliance in v9.3.2."
}
```

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Steps**
- ✅ Schema compliance verification (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum linkage validation with `/legacy/checksums/`  
- 🧾 FAIR+CARE completeness audit (license, author, provenance required)  
- ⚖️ License and source verification  
- 🧭 Replacement mapping consistency checks  

Reports stored in:
- `reports/self-validation/web-icons-app-forms-legacy-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Compliance Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All records indexed in STAC-compatible JSON format. |
| **Accessible (A)** | 100% | Stored in open JSON; accessible without proprietary tools. |
| **Interoperable (I)** | ≥95% | Compliant with schema.org + STAC mapping. |
| **Reusable (R)** | 100% | Provenance, license, and checksum fields populated. |
| **Ethical (CARE)** | ≥90% | Transparency and authorship integrity enforced. |

FAIR+CARE scores and metadata metrics are published to `releases/v9.5.0/focus-telemetry.json`.

---

## 🧱 Governance Policies

- Metadata files are **immutable post-merge**.  
- Each metadata record must contain:
  - License type  
  - Creator attribution  
  - SHA-256 checksum  
  - Replacement mapping  
  - Provenance note  
- Changes require **Governance Council approval** recorded in the Ledger.  
- File removal or renaming is **strictly prohibited** to preserve historical traceability.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added full FAIR+CARE integration and telemetry-based audit for legacy form icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Linked metadata records with checksum validation | Governance Council |
| v9.0.0 | 2025-09-25 | Created legacy metadata archive for original form icon set | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Metadata Preserves History · Provenance Upholds Trust · Design Transcends Versions.”*

</div>

