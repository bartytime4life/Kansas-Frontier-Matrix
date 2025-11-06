---
title: "🧾 Kansas Frontier Matrix — STAC Validation Raw Reports Directory"
path: "docs/self-validation/stac/reports/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/docs-stac-reports-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — STAC Validation Raw Reports Directory**
`docs/self-validation/stac/reports/README.md`

**Purpose:** Describe the structure, purpose, and retention policy for raw STAC (SpatioTemporal Asset Catalog) validation reports generated automatically during CI/CD workflows.  
These reports are part of KFM’s reproducibility framework and are permanently archived for provenance and audit under the **Master Coder Protocol (MCP v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![Status: Immutable](https://img.shields.io/badge/Status-Immutable-blue)]()

</div>

---

## 📘 Overview

The `/reports/` directory under `docs/self-validation/stac/` contains **raw STAC validation results** produced by automated workflows.  
Each file corresponds to a specific dataset validation event and includes:
- Validation logs from **PySTAC** and **stac-validator**
- Timestamps, schema versions, and error contexts
- Dataset-level metadata for reproducibility and FAIR+CARE traceability

These raw reports are retained indefinitely to maintain a **verifiable audit trail** and support **cross-validation** with governance ledgers and release telemetry.

---

## 🗂️ Directory Layout

```
docs/self-validation/stac/reports/
├── README.md                            # This index file
├── validation_log_2025-11-05T1800Z.json # Detailed validation log
├── validation_log_2025-11-05T1815Z.json # Subsequent validation session
├── validation_log_2025-11-05T1830Z.json # Example additional session
└── archive/                             # Compressed and archived historical logs
    ├── stac_validation_v9.5.0.tar.gz
    └── stac_validation_v9.7.0.tar.gz
```

Each file contains detailed JSON objects representing one or more dataset validation sessions executed by CI/CD pipelines.

---

## 🧾 JSON Structure Example

**File:** `validation_log_2025-11-05T1800Z.json`

```json
{
  "session_id": "stac_validate_2025-11-05T1800Z",
  "schema_version": "1.0.0",
  "validator_version": "3.3.0",
  "datasets_validated": 52,
  "errors_found": 0,
  "warnings": [],
  "details": [
    {
      "path": "data/stac/items/usgs_topo_1894.json",
      "valid": true,
      "message": "Validation successful using pystac 1.9.0"
    },
    {
      "path": "data/stac/items/ks_elevation_1950.json",
      "valid": true,
      "message": "No structural or schema errors."
    }
  ],
  "timestamp": "2025-11-05T18:00:00Z",
  "duration_sec": 185
}
```

---

## 🔍 Purpose of Raw Logs

Raw STAC validation logs provide:
- **Dataset-level audit evidence** for validation events  
- **Traceability** for schema updates, validator versions, and errors  
- **Cross-verification** with FAIR+CARE reports and Governance Ledgers  
- **Performance monitoring** via validation duration and dataset count  

Each session produces:
1. Human-readable JSON report  
2. Machine-ingestible NDJSON stream (`stac_validator_results.ndjson`)  
3. Summary file (`_summary.json`) for dashboards and telemetry aggregation  

---

## ⚙️ Workflow Integration

**Source Workflow:** `.github/workflows/stac-validate.yml`

**Pipeline Summary:**
1. Validate all `data/stac/**/*.json` items with PySTAC  
2. Cross-validate with `stac-validator` CLI  
3. Aggregate session metrics into a raw report file  
4. Archive reports into versioned `.tar.gz` bundles  
5. Append ledger entry in `reports/audit/github-workflows-ledger.json`

---

## 🧮 Governance & Telemetry Cross-References

| Linked Record | Description | Location |
|----------------|-------------|-----------|
| **Governance Ledger** | Workflow execution event and metadata | `reports/audit/github-workflows-ledger.json` |
| **Telemetry Report** | Aggregated metrics and durations | `releases/v9.7.0/focus-telemetry.json` |
| **FAIR+CARE Audit** | Cross-linked compliance confirmation | `reports/fair/faircare_summary.json` |
| **SBOM Reference** | Software versions used in validation | `releases/v9.7.0/sbom.spdx.json` |

---

## 🧠 Data Retention Policy

| Policy Element | Specification |
|----------------|----------------|
| **Retention Period** | Permanent (immutable archive). |
| **Compression Policy** | Raw JSON older than one release cycle compressed into `.tar.gz`. |
| **Accessibility** | Publicly available under CC-BY 4.0 license. |
| **Verification** | Each archived log digitally signed with SHA-256 checksum. |
| **Governance Approval** | Council reviewed; included in MCP audit cycle. |

Example signature:
```bash
sha256sum validation_log_2025-11-05T1800Z.json
# Output: 7f9db06ac8b24b64b1f84711e0b9a2f511d9f1dc6c3b57cb8bb13b0af7b458ea
```

---

## ⚖️ FAIR+CARE Compliance Mapping

| Principle | Implementation |
|------------|----------------|
| **Findable** | Reports indexed by timestamp, version, and dataset ID. |
| **Accessible** | Stored in GitHub repository and linked in telemetry. |
| **Interoperable** | JSON conforms to open OGC STAC and DCAT schemas. |
| **Reusable** | Historical logs remain accessible for governance and research. |
| **CARE** | Data validated ethically under CARE review protocol. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created detailed STAC raw report index with FAIR+CARE and governance integration. |
| v9.5.0 | 2025-10-20 | A. Barta | Added data retention and checksum verification policy. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established report directory and metadata structure. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to STAC Self-Validation Index](../README.md) · [Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>****
