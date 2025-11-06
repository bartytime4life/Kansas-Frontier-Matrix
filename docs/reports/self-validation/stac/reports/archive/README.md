---
title: "🗄️ Kansas Frontier Matrix — Archived STAC & DCAT Validation Logs"
path: "docs/reports/self-validation/stac/reports/archive/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/docs-reports-stac-archive-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🗄️ **Kansas Frontier Matrix — Archived STAC & DCAT Validation Logs**
`docs/reports/self-validation/stac/reports/archive/README.md`

**Purpose:** Provide the authoritative index of archived STAC validation reports and their associated metadata, preserving data lineage and reproducibility for all Kansas Frontier Matrix (KFM) releases.  
These archives ensure permanent accessibility to historical validation sessions under **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** data governance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)
[![Status: Archived](https://img.shields.io/badge/Status-Immutable-blue)]()

</div>

---

## 📘 Overview

This `archive/` directory stores **compressed TAR archives** of past STAC and DCAT validation reports generated from KFM’s automated workflows.  
Each archive bundle corresponds to a specific release (e.g., `v9.7.0`) and contains all:
- PySTAC validation outputs  
- STAC Validator logs  
- Aggregated summaries (`_summary.json`)  
- Metadata describing validator versions, dataset counts, and schema details  
- SHA-256 checksums ensuring integrity  

These archives serve as the **long-term provenance ledger** for dataset metadata validation across all KFM versions.

---

## 🗂️ Directory Layout

```
docs/reports/self-validation/stac/reports/archive/
├── README.md                             # This file
├── stac_validation_v9.5.0.tar.gz         # Archived reports from release v9.5.0
├── stac_validation_v9.6.0.tar.gz         # Archived reports from release v9.6.0
├── stac_validation_v9.7.0.tar.gz         # Latest archive (current release)
└── metadata/                             # Associated metadata and checksums
    ├── stac_validation_v9.5.0_metadata.json
    ├── stac_validation_v9.6.0_metadata.json
    └── stac_validation_v9.7.0_metadata.json
```

---

## 🧾 Archive Metadata Schema

Each archive has an accompanying metadata JSON file located under `/metadata/`.

**Example: `stac_validation_v9.7.0_metadata.json`**
```json
{
  "release": "v9.7.0",
  "generated_on": "2025-11-05T18:15:00Z",
  "datasets_validated": 52,
  "passed": 52,
  "failed": 0,
  "validator_version": "3.3.0",
  "schema_version": "STAC 1.0.0",
  "archive_checksum": "sha256-0afebf2d93a45dc73d8d14a9955d22e49afce78e3b6b792a4ac65e8f093b6aef"
}
```

---

## ⚙️ Archive Creation Workflow

| Step | Process | Tool / Workflow |
|------|----------|-----------------|
| 1️⃣ | Validate datasets with PySTAC & STAC Validator | `.github/workflows/stac-validate.yml` |
| 2️⃣ | Aggregate results into summary and raw NDJSON logs | PySTAC / `stac-validator` |
| 3️⃣ | Package reports into `.tar.gz` archive | `tar -czf stac_validation_vX.Y.Z.tar.gz` |
| 4️⃣ | Generate SHA-256 checksum and metadata JSON | `sha256sum` utility |
| 5️⃣ | Append record to Governance Ledger | `reports/audit/github-workflows-ledger.json` |
| 6️⃣ | Reference archive in SBOM and Manifest | `releases/v9.7.0/sbom.spdx.json` |

**Automation Example (Bash):**
```bash
tar -czf stac_validation_v9.7.0.tar.gz pystac_results.json stac_validator_results.ndjson _summary.json
sha256sum stac_validation_v9.7.0.tar.gz > stac_validation_v9.7.0.sha256
```

---

## 🧠 Governance Integration

| Record | Description | File Location |
|---------|--------------|----------------|
| **Governance Ledger** | Logs archive creation events and Council approval. | `reports/audit/github-workflows-ledger.json` |
| **Release Manifest Log** | Records checksums and metadata for reproducibility. | `reports/audit/release-manifest-log.json` |
| **Telemetry Dashboard** | Displays validation history and compliance rates. | `docs/reports/telemetry/governance_scorecard.json` |

**Governance Example Entry:**
```json
{
  "event": "stac_archive_creation",
  "release": "v9.7.0",
  "datasets_validated": 52,
  "archive_file": "stac_validation_v9.7.0.tar.gz",
  "checksum": "sha256-0afebf2d93a45dc73d8d14a9955d22e49afce78e3b6b792a4ac65e8f093b6aef",
  "timestamp": "2025-11-05T18:30:00Z",
  "approved_by": "FAIR+CARE Council"
}
```

---

## 🧩 FAIR+CARE Compliance Alignment

| Principle | Archive Implementation |
|------------|------------------------|
| **Findable** | Archives indexed by release version and timestamp. |
| **Accessible** | Publicly available under CC-BY 4.0 license. |
| **Interoperable** | Metadata conforms to JSON Schema and STAC/DCAT standards. |
| **Reusable** | Fully versioned and checksum-verified for reproducibility. |
| **CARE** | Reviewed by FAIR+CARE Council for ethical and cultural sensitivity. |

---

## 🧮 Data Retention Policy

| Policy Element | Specification |
|----------------|----------------|
| **Retention Period** | Permanent archival; never deleted or replaced. |
| **Format** | `.tar.gz` + JSON metadata (UTF-8 encoded). |
| **Integrity Verification** | SHA-256 hashes validated in SBOM. |
| **Accessibility** | Published in repository and listed in release manifest. |
| **Governance Oversight** | Quarterly review by FAIR+CARE Council. |

---

## 🧾 Telemetry Integration

Archived validation data contribute to governance telemetry for performance and reproducibility metrics.

**Telemetry Example:**
```json
{
  "stac_archives": {
    "releases_tracked": 3,
    "total_datasets_validated": 156,
    "overall_compliance_rate": 99.8,
    "last_archive_created": "2025-11-05T18:15:00Z"
  }
}
```

Stored in:
```
releases/v9.7.0/focus-telemetry.json
```

---

## 🧠 Use Cases

| Use Case | Description |
|-----------|-------------|
| **Historical Audit** | Verify validation results across project versions. |
| **Governance Review** | Provide oversight for dataset compliance trends. |
| **Reproducibility Testing** | Confirm historical metadata integrity using archived logs. |
| **Public Transparency** | Enable third-party verification of FAIR+CARE adherence. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added archive index with checksum policy and FAIR+CARE governance integration. |
| v9.5.0 | 2025-10-20 | A. Barta | Implemented structured metadata schema for archived validation bundles. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established STAC/DCAT archive retention framework. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to STAC Raw Reports](../README.md) · [Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
