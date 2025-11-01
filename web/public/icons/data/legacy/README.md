---
title: "🕰 Kansas Frontier Matrix — Legacy Data Domain Icons (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/data/legacy/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../releases/v9.5.0/web-icons-data-legacy.meta.json"
validation_reports:
  - "../../../../../reports/self-validation/web-icons-data-legacy-validation.json"
  - "../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🕰 Kansas Frontier Matrix — **Legacy Data Domain Icons**
`web/public/icons/data/legacy/README.md`

**Purpose:** Archives deprecated or superseded data domain icons representing KFM datasets (climate, hazards, treaties, hydrology, etc.). Preserves metadata, checksums, and provenance to maintain historical traceability under FAIR+CARE and MCP-DL v6.4.3 governance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../docs/standards/governance/LEDGER.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Immutable-critical)](../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/data/legacy/
├── icon-data-climate-v1.svg          # Legacy climate dataset icon
├── icon-data-hazards-v1.svg          # Deprecated natural hazards icon
├── icon-data-treaties-v1.svg         # Early treaties and boundary dataset icon
├── icon-data-hydrology-v1.svg        # Original hydrology dataset icon
├── icon-data-archaeology-v1.svg      # Early archaeology dataset icon
├── icon-data-culture-v1.svg          # Original cultural dataset icon
├── checksums/                        # SHA-256 hash manifests
├── meta/                             # Historical metadata JSON records
└── README.md                         # This file
```

---

## 🧩 Governance Purpose

This directory functions as a **permanent archive** of early KFM dataset iconography.  
Icons are preserved for provenance, checksum verification, and design reproducibility.

**Core Objectives**
- 🔐 **Integrity:** Maintain immutable archive of historical data icons.  
- 🧾 **Traceability:** Document visual and functional evolution between releases.  
- ♿ **Accessibility Regression Tracking:** Ensure prior versions remain referenceable for compliance testing.  
- 🧭 **Provenance:** Record creation context, dataset linkage, and designer attribution.

All legacy icons fall under the **Immutable Archive Policy**, forbidding modification or deletion.

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-data-hydrology-v1",
  "title": "Hydrology Dataset Icon (Legacy v1)",
  "category": "data/legacy",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-1db97e29a876cf5e8b7b0d41d64b02b3f991b1...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-data-hydrology.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Original hydrology dataset icon used in v9.0.0; replaced in v9.3.2 for improved line weight and accessibility contrast."
}
```

---

## ⚙️ Validation & Audit Framework

**Workflow:** `.github/workflows/icon-archive-validate.yml`

**Automated Validation Includes**
- ✅ JSON metadata schema compliance (`schemas/ui/icons.schema.json`)  
- 🔐 Checksum integrity verification (`/legacy/checksums/`)  
- 🧾 FAIR+CARE metadata completeness audit  
- ⚖️ License and creator validation  
- 🧭 Provenance linkage cross-check  

Reports stored in:
- `reports/self-validation/web-icons-data-legacy-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔒 Archive Compliance Policies

| Policy | Description | Enforcement |
|--------|-------------|--------------|
| **Immutable Archive** | Legacy dataset icons cannot be modified or deleted. | Protected branch; CI enforcement. |
| **Checksum Verification** | All icons must have `.sha256` files verified quarterly. | Enforced by CI/CD workflows. |
| **Metadata Requirements** | License, author, provenance, checksum, and replacement fields are mandatory. | Schema validation enforcement. |
| **Accessibility Recordkeeping** | Historical accessibility data preserved in FAIR+CARE audit reports. | Recorded in Governance Ledger. |

---

## 📊 Telemetry & FAIR+CARE Metrics

Legacy data icon metrics (stored in `releases/v9.5.0/focus-telemetry.json`) track:
- ✅ Verified checksum rate  
- 🧾 Metadata completeness percentage  
- ♿ Accessibility regression compliance  
- 🧭 Provenance linkage integrity  
- 📊 FAIR+CARE compliance index  

All results are automatically synchronized with the **Governance Ledger**.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Introduced immutable legacy data icon archive and telemetry linkage | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added metadata schema cross-validation and checksum framework | Governance Council |
| v9.0.0 | 2025-09-25 | Established data icon legacy structure for historical dataset assets | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Data Icons Remembered · Provenance Retained · Integrity Immutable.”*

</div>

