---
title: "📜 Kansas Frontier Matrix — Licensing & Intellectual Property Standards"
path: "docs/standards/licensing.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-licensing-v1.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Licensing & Intellectual Property Standards**
`docs/standards/licensing.md`

**Purpose:** Define and enforce open-source and open-data licensing standards across the Kansas Frontier Matrix (KFM).  
Licensing ensures transparency, reproducibility, and ethical sharing of software, datasets, and documentation, in full compliance with **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** governance principles.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Active-success)]()

</div>

---

## 📘 Overview

Licensing governs how all **data, code, models, and documentation** in the Kansas Frontier Matrix may be used, shared, or redistributed.  
The KFM project follows a unified **open licensing framework** to ensure maximum accessibility while respecting cultural and ethical boundaries.

All licenses must:
- Be **SPDX-compliant**
- Be explicitly stated in metadata, manifests, or front-matter
- Be compatible with FAIR+CARE ethical principles
- Be tracked in the **SBOM (Software Bill of Materials)** and **Release Manifests**

---

## 🧱 Core Licensing Policy

| Category | Default License | Description |
|-----------|-----------------|-------------|
| **Code & Scripts** | MIT License | Allows reuse and modification with attribution. |
| **Documentation** | CC-BY 4.0 | Allows redistribution and adaptation with credit. |
| **Data & Datasets** | CC-BY 4.0 or Public Domain (US Gov Works) | Ensures free access with ethical acknowledgment. |
| **AI Models** | CC-BY-SA 4.0 | Requires derivative models to share alike under same license. |
| **Governance Records & Reports** | CC-BY 4.0 | Publicly auditable under ethical data stewardship. |

All license metadata is recorded in:
```
releases/v9.7.0/sbom.spdx.json
```

---

## 🧩 SPDX License Integration

All licenses must use standardized SPDX identifiers as defined by the [SPDX License List](https://spdx.org/licenses/).

| SPDX ID | License Name | Typical Use |
|----------|---------------|--------------|
| `MIT` | MIT License | Source code and scripts |
| `CC-BY-4.0` | Creative Commons Attribution 4.0 | Documentation, data |
| `CC-BY-SA-4.0` | Creative Commons Attribution-ShareAlike 4.0 | Models, derivative AI |
| `CC0-1.0` | Creative Commons Zero 1.0 Universal | Public domain data |
| `ODbL-1.0` | Open Database License 1.0 | Structured data collections |
| `Public Domain` | U.S. Government Works | Federal datasets, USGS, NOAA, NASA |

**Example SBOM License Entry:**
```json
{
  "name": "kfm-data-ingest",
  "version": "v9.7.0",
  "license": "MIT",
  "copyright": "© 2025 Kansas Frontier Matrix",
  "licenseFile": "LICENSE"
}
```

---

## ⚖️ Data Licensing Metadata

Every dataset manifest (`data/sources/*.json`) must include explicit licensing information to ensure reuse transparency.

| Field | Description | Example |
|--------|-------------|----------|
| `license` | SPDX-compatible license identifier | `"CC-BY-4.0"` |
| `license_text` | Short human-readable summary | `"Creative Commons Attribution 4.0 International"` |
| `provenance` | Data source or owner | `"NOAA National Centers for Environmental Information"` |
| `attribution` | Required credit text | `"Data courtesy of NOAA and the Kansas Frontier Matrix Project"` |

**Example:**
```json
{
  "id": "noaa_storms_1950_2025",
  "title": "NOAA Storm Events Archive (1950–2025)",
  "license": "Public Domain",
  "provenance": "NOAA NCEI",
  "attribution": "Public domain dataset — U.S. Government Work"
}
```

---

## 🧮 Validation & Governance Workflow

Licensing compliance is automatically verified through multiple validation pipelines:

| Workflow | Purpose | Output |
|-----------|----------|--------|
| `faircare-validate.yml` | Checks dataset manifests for license presence and validity. | `reports/fair/faircare_results.ndjson` |
| `stac-validate.yml` | Ensures STAC/DCAT metadata includes license fields. | `reports/self-validation/stac/_summary.json` |
| `docs-lint.yml` | Confirms all documentation includes a license badge and footer. | `reports/self-validation/docs/lint_summary.json` |
| `telemetry-export.yml` | Publishes license coverage metrics for dashboards. | `releases/v9.7.0/focus-telemetry.json` |

All validations append results to:
```
reports/audit/github-workflows-ledger.json
```

---

## 🧭 License Attribution Standards

KFM enforces clear and consistent attribution language across datasets and publications.

| Asset Type | Attribution Format |
|-------------|--------------------|
| **Code** | “© 2025 Kansas Frontier Matrix, released under the MIT License.” |
| **Data** | “Data courtesy of [Source]. Licensed under CC-BY 4.0.” |
| **Models** | “Trained by the Kansas Frontier Matrix AI Team under CC-BY-SA 4.0.” |
| **Documentation** | “This documentation is available under CC-BY 4.0.” |

**Example Markdown Footer:**
```markdown
**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Built under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
```

---

## 🧠 Ethical & Cultural Data Restrictions

While KFM promotes open access, certain datasets or records may carry **ethical or cultural restrictions** in accordance with CARE principles.

| Restriction Type | Condition | Handling Procedure |
|------------------|------------|--------------------|
| **Restricted** | Data contains sensitive Indigenous or cultural content. | Access requires FAIR+CARE Council approval. |
| **Conditionally Open** | Requires attribution or use limitation statement. | Add CARE note and limited license in metadata. |
| **Fully Open** | No ethical restrictions; Public Domain or CC license. | Publish directly in repository. |

**CARE Field Example (in data manifest):**
```json
"care": {
  "status": "restricted",
  "statement": "Requires approval for redistribution by KFM FAIR+CARE Council.",
  "reviewer": "FAIR+CARE Governance Board"
}
```

---

## 🧩 Integration with SBOM & Manifest Tracking

Licensing data is consolidated across all release metadata for audit and reproducibility.

| File | Description |
|------|-------------|
| `releases/v9.7.0/sbom.spdx.json` | SPDX license inventory for all dependencies and data. |
| `releases/v9.7.0/manifest.zip` | Compressed package including licensing metadata. |
| `reports/audit/release-manifest-log.json` | Immutable log of license compliance across releases. |
| `docs/reports/telemetry/governance_scorecard.json` | License coverage and FAIR compliance metrics. |

---

## 🧾 License Compliance Dashboard

The KFM Governance Dashboard visualizes:
- Percentage of datasets with valid licenses
- Frequency of open vs. restricted licenses
- CARE-restricted data categories
- Attribution completeness across assets

**Data Source:**  
`docs/reports/telemetry/governance_scorecard.json`

**Governance Score Example:**
```json
{
  "license_compliance_rate": 100,
  "care_restricted_datasets": 3,
  "open_data_ratio": 0.97,
  "timestamp": "2025-11-05T19:40:00Z"
}
```

---

## ⚖️ FAIR+CARE Alignment

| Principle | Licensing Implementation |
|------------|---------------------------|
| **Findable** | Each dataset and document includes explicit license metadata. |
| **Accessible** | All licenses are open and machine-readable. |
| **Interoperable** | SPDX identifiers ensure cross-platform standardization. |
| **Reusable** | License metadata stored in SBOM and manifest for all releases. |
| **CARE** | Restricted datasets follow ethical review protocols. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created unified licensing and IP standard with SBOM integration and FAIR+CARE mapping. |
| v9.5.0 | 2025-10-20 | A. Barta | Added CARE data restriction section and SPDX alignment. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established open license policy framework. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
