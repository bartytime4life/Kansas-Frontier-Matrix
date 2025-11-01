---
title: "📜 Kansas Frontier Matrix — Legacy Form & Input Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/forms/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-forms-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-forms-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Form & Input Icon Metadata**
`web/public/icons/legacy/app/forms/meta/README.md`

**Purpose:** Stores immutable metadata records for all deprecated form and input icons used in earlier Kansas Frontier Matrix releases. Preserves authorship, licensing, checksum linkage, and provenance under FAIR+CARE and MCP-DL v6.4.3 governance frameworks.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/forms/meta/
├── icon-form-save-v1.json          # Metadata for legacy save icon
├── icon-form-edit-v1.json          # Metadata for legacy edit icon
├── icon-form-delete-v1.json        # Metadata for legacy delete icon
├── icon-form-add-v1.json           # Metadata for legacy add icon
├── icon-form-warning-v1.json       # Metadata for legacy warning icon
├── icon-form-error-v1.json         # Metadata for legacy error icon
├── icon-form-confirm-v1.json       # Metadata for legacy confirm icon
├── icon-form-cancel-v1.json        # Metadata for legacy cancel icon
└── README.md                       # This file
```

---

## 🧩 Metadata Schema

Each metadata record complies with `schemas/ui/icons.schema.json`, ensuring interoperability with FAIR+CARE, STAC, and DCAT standards.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (e.g., `icon-form-delete-v1`) |
| `title` | string | Human-readable title for the icon |
| `category` | string | Classification path (`legacy/app/forms`) |
| `version` | string | Semantic version of the icon asset |
| `creator` | string | Original designer or team attribution |
| `license` | string | License type (MIT, CC-BY, or Public Domain) |
| `checksum` | string | SHA-256 hash to ensure immutability |
| `deprecated` | string | Date of icon deprecation |
| `replaced_by` | string | Successor icon filename or ID |
| `source_url` | string | Repository or asset link |
| `provenance` | string | Description of design lineage, rationale, and accessibility updates |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-form-add-v1",
  "title": "Form Add Icon (Legacy v1)",
  "category": "legacy/app/forms",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-59bca17e6c3a47fb87efad7bde9235f27c7aa3...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-form-add.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Deployed in v9.0.0; replaced in v9.3.2 with standardized stroke width and improved color accessibility."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Validation Steps**
- ✅ JSON schema conformance check (`schemas/ui/icons.schema.json`)  
- 🔐 Cross-verification with `/legacy/app/forms/checksums/` manifests  
- 🧾 FAIR+CARE completeness validation  
- ⚖️ License and authorship verification  
- 🧭 Provenance and replacement mapping audit  

Audit results are stored in:
- `reports/self-validation/web-icons-legacy-app-forms-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All metadata indexed by ID and title. |
| **Accessible (A)** | 100% | JSON files publicly accessible and schema-compliant. |
| **Interoperable (I)** | ≥95% | Metadata aligned with STAC/DCAT standards for export. |
| **Reusable (R)** | 100% | License and provenance documented for reuse. |
| **Ethical (CARE)** | ≥90% | Authorship and transparency verified under FAIR+CARE audits. |

All metrics are aggregated into `releases/v9.5.0/focus-telemetry.json` and tracked via the Governance Ledger dashboard.

---

## 🧱 Governance Policies

- Metadata files are **immutable** once published.  
- Each file must include:
  - Author attribution  
  - License declaration  
  - SHA-256 checksum reference  
  - Provenance description and replacement linkage  
- All modifications require **Governance Council** approval and ledger documentation.  
- Metadata deletion is strictly prohibited under FAIR+CARE archival policy.  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Established legacy form metadata archive with checksum and provenance tracking | Design Systems Team |
| v9.3.2 | 2025-10-20 | Linked metadata to FAIR+CARE audits and accessibility telemetry | Governance Council |
| v9.0.0 | 2025-09-25 | Created metadata directory for legacy form icon collection | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Integrity in Every Input · Provenance in Every Field.”*

</div>

