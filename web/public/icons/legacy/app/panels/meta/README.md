---
title: "📜 Kansas Frontier Matrix — Legacy Panel Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/legacy/app/panels/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../../releases/v9.5.0/web-icons-legacy-app-panels-meta.json"
validation_reports:
  - "../../../../../../../reports/self-validation/web-icons-legacy-app-panels-meta-validation.json"
  - "../../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Panel Icon Metadata**
`web/public/icons/legacy/app/panels/meta/README.md`

**Purpose:** Documents immutable metadata for all legacy panel interface icons within Kansas Frontier Matrix. Each record defines authorship, licensing, checksum linkage, and provenance under FAIR+CARE and MCP-DL v6.4.3 compliance standards for reproducibility and ethical stewardship.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/legacy/app/panels/meta/
├── icon-panel-info-v1.json         # Metadata for Info icon (legacy)
├── icon-panel-close-v1.json        # Metadata for Close icon (legacy)
├── icon-panel-expand-v1.json       # Metadata for Expand icon (legacy)
├── icon-panel-collapse-v1.json     # Metadata for Collapse icon (legacy)
├── icon-panel-settings-v1.json     # Metadata for Settings icon (legacy)
├── icon-panel-pin-v1.json          # Metadata for Pin icon (legacy)
├── icon-panel-unpin-v1.json        # Metadata for Unpin icon (legacy)
└── README.md                       # This file
```

---

## 🧩 Metadata Schema

All entries conform to `schemas/ui/icons.schema.json`, ensuring interoperability and compliance with FAIR+CARE and STAC metadata conventions.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (e.g., `icon-panel-expand-v1`) |
| `title` | string | Human-readable title |
| `category` | string | Classification path (`legacy/app/panels`) |
| `version` | string | Semantic version number |
| `creator` | string | Designer or author attribution |
| `license` | string | License type (MIT, CC-BY, Public Domain) |
| `checksum` | string | SHA-256 hash to ensure immutability |
| `deprecated` | string | Date of icon deprecation |
| `replaced_by` | string | Successor icon filename |
| `source_url` | string | Repository or asset link |
| `provenance` | string | Notes on design lineage, rationale for replacement, and version context |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-panel-expand-v1",
  "title": "Panel Expand Icon (Legacy v1)",
  "category": "legacy/app/panels",
  "version": "1.0.0",
  "creator": "KFM UI Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-f6b37a8d4e21f2d7c9e6f79c8e3f79ab74c9e1...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-panel-expand.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in v9.0.0; replaced in v9.3.2 to improve accessibility and adjust stroke contrast."
}
```

---

## ⚙️ Validation & Governance Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Tasks**
- ✅ JSON schema validation (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum verification crosslink with `/legacy/app/panels/checksums/`  
- 🧾 FAIR+CARE completeness validation  
- ⚖️ License and authorship consistency checks  
- 🧭 Replacement mapping integrity validation  

Audit results are stored in:
- `reports/self-validation/web-icons-legacy-app-panels-meta-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All records indexed by ID and title for global searchability. |
| **Accessible (A)** | 100% | JSON files open, readable, and schema-compliant. |
| **Interoperable (I)** | ≥95% | Metadata follows STAC/DCAT structure for export. |
| **Reusable (R)** | 100% | Provenance, license, and checksum included for reproducibility. |
| **Ethical (CARE)** | ≥90% | Authorship and transparency verified via Governance Ledger. |

Metrics recorded in `releases/v9.5.0/focus-telemetry.json` and reviewed by the Governance Council.

---

## 🧱 Governance Policies

- Metadata is **immutable post-merge**; no deletions or overwrites.  
- Each file must include:
  - Author attribution  
  - License declaration  
  - Checksum verification linkage  
  - Provenance and replacement references  
- All updates require **Governance Council** approval and Ledger record.  
- FAIR+CARE compliance verified quarterly.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added FAIR+CARE metadata schema and checksum linkage for panel icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Integrated provenance validation and telemetry metrics | Governance Council |
| v9.0.0 | 2025-09-25 | Created metadata archive for legacy panel icon collection | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Panels Recorded · Metadata Preserved · Provenance Immutable.”*

</div>
