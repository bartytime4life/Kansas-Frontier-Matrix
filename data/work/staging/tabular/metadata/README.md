---
title: "🧾 Kansas Frontier Matrix — Tabular Metadata Workspace (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/staging/tabular/metadata/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-work-staging-tabular-metadata-v10.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Tabular Metadata Workspace**
`data/work/staging/tabular/metadata/README.md`

**Purpose:**  
Central workspace for managing, harmonizing, and auditing **tabular metadata** in KFM.  
Ensures alignment with **FAIR+CARE** ethics, **STAC/DCAT** schemas, and **PROV-O/ISO 19115** lineage standards under MCP-DL v6.3 governance, with **telemetry v2** integration.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../../../docs/architecture/README.md)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Metadata%20Certified-gold.svg)](../../../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Aligned-7e57c2.svg)]()
[![License: Internal](https://img.shields.io/badge/License-Internal%20Governance%20Layer-grey.svg)](../../../../../LICENSE)

</div>

---

## 📘 Overview
The **Tabular Metadata Workspace** guarantees that metadata for structured datasets is **harmonized, validated, and ethically governed** before dataset promotion or publication.  
Pipelines provide FAIR+CARE-compliant transformations and schema checks across **STAC**, **DCAT**, and **PROV-O**.

**v10 Enhancements**
- Telemetry v2 fields attached to metadata validation (energy/CO₂ & coverage).  
- JSON-LD lineage pointers for Focus Mode v2 dashboards.  
- Extended crosswalk rules for STAC↔DCAT attribute equivalence.

### Core Responsibilities
- Harmonize metadata across STAC/DCAT/PROV-O standards.  
- Conduct FAIR+CARE audits for accessibility, transparency, and reuse.  
- Validate completeness, accuracy, and governance alignment.  
- Log lineage, checksums, and certification details for provenance.  

---

## 🗂️ Directory Layout
```plaintext
data/work/staging/tabular/metadata/
├── README.md
├── tmp/
│   ├── stac_to_dcat_crosswalk.json
│   ├── provenance_mapping.json
│   ├── metadata_merge_preview.json
│   └── metadata_patch_queue.json
├── validation/
│   ├── schema_validation_summary.json
│   ├── faircare_metadata_audit.json
│   ├── stac_dcat_link_check.log
│   └── metadata_qa_summary.md
└── logs/
    ├── metadata_validation.log
    ├── governance_sync.log
    └── metadata.json
```

---

## ⚙️ Metadata Governance Workflow
```mermaid
flowchart TD
    "Normalized Tabular (staging/tabular/normalized/*)" --> "Schema Harmonization (STAC/DCAT/PROV-O)"
    "Schema Harmonization (STAC/DCAT/PROV-O)" --> "FAIR + CARE Ethical Audit"
    "FAIR + CARE Ethical Audit" --> "Validation: Schema · Linkage · Completeness"
    "Validation: Schema · Linkage · Completeness" --> "Checksum + Governance Ledger Registration"
    "Checksum + Governance Ledger Registration" --> "Promotion → Processed Metadata (data/work/processed/metadata/)"
```

### Steps
1. **Harmonization** — Align metadata with target standards.  
2. **Ethics Audit** — FAIR+CARE checks for openness & stewardship.  
3. **Validation** — Confirm structural + linkage integrity.  
4. **Governance** — Register checksums and results in provenance ledger.  
5. **Promotion** — Publish to processed metadata collections.

---

## 🧩 Example Metadata Record
```json
{
  "id": "metadata_tabular_hazards_v10.0.0",
  "linked_dataset": "data/work/staging/tabular/normalized/hazards_normalized_v10.0.0.csv",
  "schemas_tested": ["STAC 1.0", "DCAT 3.0", "PROV-O"],
  "records_total": 1482,
  "schema_validation": "passed",
  "faircare_score": 99.1,
  "checksum_verified": true,
  "telemetry": { "energy_wh": 0.5, "co2_g": 0.7, "validation_coverage_pct": 100 },
  "validator": "@kfm-metadata-lab",
  "created": "2025-11-09T23:53:00Z",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## 🧠 FAIR+CARE Governance Matrix
| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Indexed with dataset + schema version in catalogs. | `@kfm-data` |
| **Accessible** | JSON-LD + CSV artifacts for review. | `@kfm-accessibility` |
| **Interoperable** | STAC/DCAT/PROV-O/ISO 19115 harmonization. | `@kfm-architecture` |
| **Reusable** | Provenance, checksums, telemetry, and certification embedded. | `@kfm-design` |
| **Collective Benefit** | Enables ethical reuse and accountability. | `@faircare-council` |
| **Authority to Control** | Council validates metadata certification. | `@kfm-governance` |
| **Responsibility** | Engineers document schema + linkage changes. | `@kfm-security` |
| **Ethics** | Audits ensure accurate, respectful representation. | `@kfm-ethics` |

**Audit refs:**  
`data/reports/fair/data_care_assessment.json` · `data/reports/audit/data_provenance_ledger.json`

---

## ⚙️ Validation & Certification Artifacts
| Artifact                         | Description                                     | Format |
|---|---|---|
| `schema_validation_summary.json` | STAC/DCAT/PROV-O compliance check               | JSON   |
| `faircare_metadata_audit.json`   | FAIR+CARE ethics audit + scoring                | JSON   |
| `stac_dcat_link_check.log`       | Cross-schema linkage verification               | Text   |
| `metadata_qa_summary.md`         | Governance-readable QA summary                  | Markdown |
| `metadata.json`                  | Checksum, lineage, telemetry, certification refs| JSON   |

**Automation:** `metadata_staging_sync.yml`

---

## ♻️ Retention & Sustainability
| Data Type            | Retention | Policy |
|---|---:|---|
| Temporary (`tmp/`)  | 7 Days    | Purged after validation + sync. |
| Validation Reports  | 180 Days  | Retained for FAIR+CARE audits.   |
| Governance Logs     | 365 Days  | Archived for lineage tracking.   |
| Metadata Records    | Permanent | Stored in provenance ledger.     |

**Telemetry Source:**  
`../../../../../releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Internal Citation
```text
Kansas Frontier Matrix (2025). Tabular Metadata Workspace (v10.0.0).
FAIR+CARE-certified metadata harmonization and validation workspace for tabular datasets, aligned with STAC, DCAT, and PROV-O under MCP-DL v6.3 governance and telemetry v2.
```

---

## 🕰️ Version History
| Version | Date       | Author               | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | `@kfm-metadata`      | Upgraded to v10: telemetry v2 fields, JSON-LD lineage pointers, crosswalk expansion. |
| v9.7.0  | 2025-11-06 | `@kfm-metadata`      | Telemetry/schema refs aligned; QA artifacts refreshed. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Integrity × FAIR+CARE Ethics × Provenance Governance*  
© 2025 Kansas Frontier Matrix — Internal · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Tabular Staging](../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>