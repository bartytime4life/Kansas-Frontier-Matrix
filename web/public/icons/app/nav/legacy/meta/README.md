---
title: "📜 Kansas Frontier Matrix — Legacy Navigation Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/app/nav/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-icons-app-nav-legacy-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-icons-app-nav-legacy-meta-validation.json"
  - "../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Navigation Icon Metadata**
`web/public/icons/app/nav/legacy/meta/README.md`

**Purpose:** Documents historical metadata records for all deprecated or superseded navigation icons. Ensures lineage, authorship, and licensing remain traceable for every version under FAIR+CARE and MCP-DL governance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/app/nav/legacy/meta/
├── icon-nav-home-v1.json          # Metadata for original home icon
├── icon-nav-explore-v1.json       # Metadata for early explore/timeline icon
├── icon-nav-map-v1.json           # Metadata for early map navigation icon
├── icon-nav-settings-v1.json      # Metadata for v1 settings cog
├── icon-nav-help-v1.json          # Metadata for v1 help/info icon
└── README.md                      # This file
```

---

## 🧩 Metadata Schema Overview

Each JSON file follows the **KFM Icon Metadata Schema** (`schemas/ui/icons.schema.json`), aligned with STAC and FAIR+CARE governance requirements.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique icon identifier (`icon-nav-home-v1`) |
| `title` | string | Human-readable name of the icon |
| `category` | string | Directory classification (`app/nav/legacy`) |
| `version` | string | Semantic version of icon release |
| `creator` | string | Original designer or author |
| `license` | string | Legal license type (MIT / CC-BY 4.0 / Public Domain) |
| `checksum` | string | SHA-256 hash of the file for immutability tracking |
| `deprecated` | string (date) | Date the icon was deprecated |
| `replaced_by` | string | Successor icon filename |
| `source_url` | string | Repository or asset source |
| `provenance` | string | Description of design lineage and purpose |

All metadata is stored as JSON to support automation, provenance audits, and AI-driven knowledge graph ingestion.

---

## 🧾 Example Legacy Metadata Record

```json
{
  "id": "icon-nav-map-v1",
  "title": "Navigation Map Icon (Legacy v1)",
  "category": "app/nav/legacy",
  "version": "1.0.0",
  "creator": "KFM UI/UX Design Systems",
  "license": "MIT",
  "checksum": "sha256-72e8f1dba2039a51d0348ea5e3dd79a9a71329...",
  "deprecated": "2025-09-30",
  "replaced_by": "icon-nav-map.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "First-generation navigation icon used in v9.0.0 UI release. Replaced for improved accessibility and resolution."
}
```

---

## ⚙️ CI/CD Validation Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

### Automated Validations
- ✅ Schema compliance (icons.schema.json)  
- 🔐 Checksum alignment with `/legacy/checksums/` directory  
- 🧾 FAIR+CARE metadata completeness  
- ⚖️ License and provenance validation  
- 📅 Deprecation record cross-check with Governance Ledger  

Results stored in:
- `reports/self-validation/web-icons-app-nav-legacy-meta-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Compliance Metrics

| Metric | Description | Threshold |
|--------|-------------|------------|
| **F (Findable)** | All records indexed by ID and STAC-compatible JSON | 100% |
| **A (Accessible)** | Metadata stored in open JSON schema | 100% |
| **I (Interoperable)** | Conforms to STAC + schema.org mappings | ≥95% |
| **R (Reusable)** | Proper licensing and provenance tags | 100% |
| **CARE (Ethics)** | Provenance integrity and author transparency | ≥90% |

Compliance results are aggregated into `releases/v9.5.0/focus-telemetry.json`.

---

## 🧱 Governance Policies

- Metadata files are **immutable** once committed.  
- All modifications require approval from the **Design Systems Governance Council**.  
- Each JSON must include:
  - Explicit license
  - Creator attribution
  - SHA-256 checksum
  - Replacement mapping  
- Removal of records is **prohibited**; only new superseding records may be added.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Standardized legacy metadata schema and automated validation | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added STAC-aligned export and checksum linkage | Governance Council |
| v9.0.0 | 2025-09-25 | Created initial metadata archive for deprecated icons | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Every Record Remembered · Every Asset Accounted · Every Change Traceable.”*

</div>

