---
title: "📜 Kansas Frontier Matrix — Legacy Data Domain Icon Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/data/legacy/meta/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../../../releases/v9.5.0/web-icons-data-legacy-meta.json"
validation_reports:
  - "../../../../../../reports/self-validation/web-icons-data-legacy-meta-validation.json"
  - "../../../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 Kansas Frontier Matrix — **Legacy Data Domain Icon Metadata**
`web/public/icons/data/legacy/meta/README.md`

**Purpose:** Documents metadata for all deprecated data domain icons across Kansas Frontier Matrix (e.g., climate, hazards, treaties, hydrology, archaeology). Provides immutable records for provenance, authorship, and FAIR+CARE compliance under MCP-DL v6.4.3 documentation governance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../../../docs/standards/governance/LEDGER.md)
[![Archive Provenance](https://img.shields.io/badge/Archive-Metadata%20Immutable-critical)](../../../../../../reports/audit/web-icons-faircare.json)

</div>

---

## 📁 Directory Layout

```
web/public/icons/data/legacy/meta/
├── icon-data-climate-v1.json          # Metadata for climate dataset icon
├── icon-data-hazards-v1.json          # Metadata for hazard dataset icon
├── icon-data-treaties-v1.json         # Metadata for treaty dataset icon
├── icon-data-hydrology-v1.json        # Metadata for hydrology dataset icon
├── icon-data-archaeology-v1.json      # Metadata for archaeology dataset icon
├── icon-data-culture-v1.json          # Metadata for culture dataset icon
└── README.md                          # This file
```

---

## 🧩 Metadata Schema

All metadata records conform to the KFM Icon Metadata Schema (`schemas/ui/icons.schema.json`) and align with FAIR+CARE, STAC, and DCAT interoperability principles.

| Field | Type | Description |
|--------|------|-------------|
| `id` | string | Unique asset identifier (e.g., `icon-data-hydrology-v1`) |
| `title` | string | Descriptive name of the icon |
| `category` | string | Classification path (`data/legacy`) |
| `version` | string | Semantic version number |
| `creator` | string | Designer or author |
| `license` | string | Legal license type (MIT / CC-BY / Public Domain) |
| `checksum` | string | SHA-256 hash for immutability verification |
| `deprecated` | string | Date when icon was deprecated |
| `replaced_by` | string | Successor icon file name |
| `source_url` | string | Repository or reference URL |
| `provenance` | string | Summary of design history and replacement rationale |

---

## 🧾 Example Metadata Record

```json
{
  "id": "icon-data-treaties-v1",
  "title": "Treaties Dataset Icon (Legacy v1)",
  "category": "data/legacy",
  "version": "1.0.0",
  "creator": "KFM Design Systems (Historical)",
  "license": "MIT",
  "checksum": "sha256-7c41e9e27bf33d2ac128f09dc4a1e715c9a94f...",
  "deprecated": "2025-09-25",
  "replaced_by": "icon-data-treaties.svg",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Introduced in v9.0.0 as core treaty dataset visual; replaced in v9.3.2 for improved clarity and accessibility compliance."
}
```

---

## ⚙️ Validation & Audit Workflow

**Workflow:** `.github/workflows/icon-meta-validate.yml`

**Automated Tasks**
- ✅ JSON schema compliance check (`schemas/ui/icons.schema.json`)  
- 🔐 Cross-verification with `/legacy/checksums/` hashes  
- 🧾 FAIR+CARE metadata completeness validation  
- ⚖️ License and author verification  
- 🧭 Provenance mapping and replacement validation  

Audit results are stored in:
- `reports/self-validation/web-icons-data-legacy-meta-validation.json`
- `reports/audit/web-icons-faircare.json`

---

## 🔍 FAIR+CARE Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **Findable (F)** | 100% | All metadata indexed and discoverable by ID. |
| **Accessible (A)** | 100% | Open JSON schema, easily parsed and reused. |
| **Interoperable (I)** | ≥95% | Conforms to STAC/DCAT schema compatibility. |
| **Reusable (R)** | 100% | Provenance, license, and creator recorded. |
| **Ethical (CARE)** | ≥90% | Authorship transparency and immutability enforcement. |

Results contribute to `releases/v9.5.0/focus-telemetry.json` for governance analytics.

---

## 🧱 Governance Policies

- Metadata files are **immutable** once committed.  
- Any modification requires Governance Council approval and Ledger entry.  
- Each record must include:
  - License  
  - Creator  
  - SHA-256 checksum  
  - Replacement mapping  
  - Provenance summary  
- Metadata deletions or renaming are strictly **prohibited** to preserve historical traceability.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Introduced schema-aligned metadata and telemetry for legacy dataset icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added checksum linkage and FAIR+CARE governance validation | Governance Council |
| v9.0.0 | 2025-09-25 | Created metadata archive for original data domain icon set | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Every Dataset Has a Symbol · Every Symbol Has a Story · Every Story Has Provenance.”*

</div>

