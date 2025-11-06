---
title: "🧾 Kansas Frontier Matrix — Raw STAC & DCAT Validation Report Logs"
path: "docs/reports/self-validation/stac/reports/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/docs-reports-stac-raw-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Raw STAC & DCAT Validation Report Logs**
`docs/reports/self-validation/stac/reports/README.md`

**Purpose:** Document the directory of raw STAC validation logs and archived data produced by automated CI/CD validation workflows.  
These reports serve as immutable audit artifacts under the **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** governance standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)
[![Status: Immutable](https://img.shields.io/badge/Status-Archived-blue)]()

</div>

---

## 📘 Overview

The `/reports/` directory stores **raw STAC validation logs**, providing granular traceability for each dataset validation session.  
These logs support **reproducibility**, **governance auditing**, and **data lineage tracking** within Kansas Frontier Matrix (KFM).

Each file documents:
- Validation timestamp and validator version  
- Dataset paths and outcomes  
- Validation errors and warnings  
- Duration and schema information  
- SHA-256 checksum for data integrity  

All reports are immutable once generated and versioned by release cycle.

---

## 🗂️ Directory Layout

```
docs/reports/self-validation/stac/reports/
├── README.md                              # This index file
├── validation_log_2025-11-05T1800Z.json   # Latest validation session log
├── validation_log_2025-11-05T1830Z.json   # Next session log
└── archive/                               # Compressed historical logs
    ├── stac_validation_v9.5.0.tar.gz
    ├── stac_validation_v9.6.0.tar.gz
    └── stac_validation_v9.7.0.tar.gz
```

---

## 🧾 Log File Schema

Each validation log (`validation_log_<timestamp>.json`) follows the structure below:

```json
{
  "session_id": "stac_validate_2025-11-05T1800Z",
  "version": "v9.7.0",
  "schema_version": "1.0.0",
  "validator_version": "3.3.0",
  "datasets_validated": 52,
  "passed": 52,
  "failed": 0,
  "duration_sec": 185,
  "errors": [],
  "details": [
    {
      "path": "data/stac/items/usgs_topo_1894.json",
      "valid": true,
      "message": "Validation successful using pystac 1.9.0"
    },
    {
      "path": "data/stac/items/ks_elevation_1950.json",
      "valid": true,
      "message": "No schema errors found."
    }
  ],
  "timestamp": "2025-11-05T18:00:00Z",
  "checksum": "sha256-1f3b7c5d8e7b9a2e7e1cf34a90a9d30d5c5a4c6f0a2d66e9f1e3c5bdf7e0f1d9"
}
```

---

## 🧩 Archive Metadata Schema

Each `.tar.gz` archive in `/archive/` includes a metadata file that records contextual information about its creation.

**Example:** `stac_validation_v9.7.0_metadata.json`

```json
{
  "release": "v9.7.0",
  "generated_on": "2025-11-05T18:15:00Z",
  "datasets_validated": 52,
  "validator_version": "3.3.0",
  "schema_version": "STAC 1.0.0",
  "archive_checksum": "sha256-0afebf2d93a45dc73d8d14a9955d22e49afce78e3b6b792a4ac65e8f093b6aef"
}
```

---

## ⚙️ Generation Workflow

**Workflow:** `.github/workflows/stac-validate.yml`

### Steps
1. Validate datasets using PySTAC and STAC Validator.
2. Write session results to `validation_log_<timestamp>.json`.
3. Append validation event to `reports/audit/github-workflows-ledger.json`.
4. Package all session logs into `.tar.gz` archives per release.
5. Generate a checksum for each archive and store it in `sbom.spdx.json`.

---

## 🧠 Governance & Telemetry Linkage

| System | Function | Path |
|---------|-----------|------|
| **Governance Ledger** | Logs validation runs and approvals. | `reports/audit/github-workflows-ledger.json` |
| **FAIR+CARE Summary** | Cross-links validation to ethical data compliance. | `reports/fair/faircare_summary.json` |
| **Telemetry Dashboard** | Displays validation duration and pass rates. | `docs/reports/telemetry/governance_scorecard.json` |

**Ledger Example:**
```json
{
  "event": "stac_validation_archive",
  "release": "v9.7.0",
  "archive_file": "stac_validation_v9.7.0.tar.gz",
  "datasets_validated": 52,
  "timestamp": "2025-11-05T18:30:00Z",
  "approved_by": "FAIR+CARE Council"
}
```

---

## 🧮 FAIR+CARE Compliance Mapping

| Principle | Implementation |
|------------|----------------|
| **Findable** | Validation logs indexed by version and timestamp. |
| **Accessible** | Publicly stored and licensed under CC-BY 4.0. |
| **Interoperable** | JSON format aligns with STAC/DCAT/FAIR metadata schema. |
| **Reusable** | Immutable logs archived per release for reproducibility. |
| **CARE** | Audited for ethical and community data implications. |

---

## 🧾 Data Retention & Access Policy

| Policy Element | Specification |
|----------------|----------------|
| **Retention Period** | Permanent archival per release. |
| **Format** | JSON / TAR.GZ (UTF-8 encoded). |
| **Checksum** | Verified via `sbom.spdx.json`. |
| **License** | CC-BY 4.0 (open-access). |
| **Governance Review** | Quarterly validation by FAIR+CARE Council. |

---

## 🧩 Use Cases

| Use Case | Description |
|-----------|-------------|
| **Audit Verification** | Confirms that all STAC items were validated and archived. |
| **Metadata Provenance** | Verifies dataset lineage and schema compliance. |
| **Dashboard Integration** | Provides raw data for governance telemetry visualization. |
| **Public Transparency** | Demonstrates FAIR+CARE compliance to external reviewers. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created raw STAC/DCAT validation report index and archival metadata structure. |
| v9.5.0 | 2025-10-20 | A. Barta | Added checksum verification and governance audit linkage. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established raw validation report directory. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Immutable validation artifacts governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to STAC Validation Summary](../README.md) · [Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
