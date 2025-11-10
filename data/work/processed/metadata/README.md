---
title: "🧾 Kansas Frontier Matrix — Processed Metadata Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/processed/metadata/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-work-processed-metadata-v10.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Processed Metadata Layer**
`data/work/processed/metadata/README.md`

**Purpose:**  
Central repository for **FAIR+CARE-certified metadata collections** documenting all finalized datasets in KFM.  
Maintains validated, provenance-linked metadata aligned with **STAC**, **DCAT**, **PROV-O**, and **ISO 19115** for transparent, interoperable governance, with **telemetry v2** and **Streaming STAC** references.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../../docs/architecture/README.md)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Metadata%20Certified-gold.svg)](../../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Aligned-7e57c2.svg)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../../LICENSE)

</div>

---

## 📘 Overview
The **Processed Metadata Layer** provides authoritative metadata collections for **FAIR+CARE-validated** KFM datasets.  
Each record captures **provenance**, **schema lineage**, **ethics certification**, and **catalog registration**, ensuring global interoperability and traceability.

**v10 Enhancements**
- Telemetry v2 fields (energy/CO₂, validation coverage) bundled with certification.  
- Streaming STAC cross-links for datasets with ongoing updates.  
- Expanded JSON-LD governance certificates for Focus Mode v2.

### Core Objectives
- Store final, validated metadata harmonized across STAC/DCAT/PROV-O.  
- Register FAIR+CARE certifications and checksum verifications.  
- Link metadata collections to processed outputs in `data/work/processed/*/`.  
- Publish catalog-ready metadata for open access.

---

## 🗂️ Directory Layout
```plaintext
data/work/processed/metadata/
├── README.md
├── stac_collection.json                  # STAC 1.0 collection manifest (processed datasets)
├── provenance_manifest.json              # PROV-O lineage + governance ledger mapping
├── governance_certification.json         # FAIR+CARE audit & ethics certification (JSON-LD)
├── metadata_summary.csv                  # Dataset → metadata index (human-readable)
└── metadata.json                         # Provenance + checksum record for metadata layer
```

---

## ⚙️ Metadata Processing Workflow
```mermaid
flowchart TD
    "FAIR+CARE Validated Datasets (data/work/processed/*)" --> "STAC/DCAT Metadata Harmonization"
    "STAC/DCAT Metadata Harmonization" --> "FAIR+CARE Certification + Provenance Registration"
    "FAIR+CARE Certification + Provenance Registration" --> "Checksum & Governance Verification"
    "Checksum & Governance Verification" --> "Catalog Synchronization + Publication"
```

### Steps
1. **Extraction** — Generate metadata from processed datasets.  
2. **Harmonization** — Align with STAC/DCAT/PROV-O profiles.  
3. **Certification** — Record FAIR+CARE validation & council approval.  
4. **Verification** — Verify checksums & governance hashes.  
5. **Publication** — Link to STAC collections & governance ledgers.

---

## 🧩 Example Metadata Record
```json
{
  "id": "metadata_processed_hazards_v10.0.0",
  "dataset_ref": "data/work/processed/hazards/hazards_composite_v10.0.0.geojson",
  "schemas": ["STAC 1.0.0", "DCAT 3.0", "PROV-O"],
  "fairstatus": "certified",
  "checksum_sha256": "sha256:d8a4e1b3f7a9c6e2b3a7d8c4e5f2b9d3e4a1f6c8b7e2a9c5d3f4a7b6c9e5d1f3",
  "validator": "@kfm-metadata-lab",
  "license": "CC-BY 4.0",
  "created": "2025-11-09T23:45:00Z",
  "telemetry": {
    "energy_wh": 0.9,
    "co2_g": 1.2,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## 🧠 FAIR+CARE Metadata Governance Matrix
| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | STAC/DCAT indexing with dataset links & IDs. | `@kfm-data` |
| **Accessible** | JSON-LD & CSV exports for public use. | `@kfm-accessibility` |
| **Interoperable** | Conforms to STAC/DCAT/PROV-O & ISO 19115. | `@kfm-architecture` |
| **Reusable** | Provenance, checksums, & certification included. | `@kfm-design` |
| **Collective Benefit** | Ethical, transparent access to Kansas research data. | `@faircare-council` |
| **Authority to Control** | Council governs metadata certification. | `@kfm-governance` |
| **Responsibility** | Validators sustain consistency across collections. | `@kfm-security` |
| **Ethics** | Reviewed for inclusivity & cultural sensitivity. | `@kfm-ethics` |

**FAIR+CARE references:**  
`data/reports/fair/data_care_assessment.json` · `data/reports/audit/data_provenance_ledger.json`

---

## ⚙️ Validation & Certification Artifacts
| Artifact                    | Description                                   | Format |
|---|---|---|
| `stac_collection.json`     | STAC collection for processed datasets.       | JSON   |
| `provenance_manifest.json` | PROV-O lineage + governance references.       | JSON   |
| `governance_certification.json` | FAIR+CARE ethics certification outcomes. | JSON   |
| `metadata_summary.csv`     | Index of dataset metadata (human-readable).   | CSV    |
| `metadata.json`            | Provenance + checksum record for the layer.   | JSON   |

Automation: `metadata_processed_sync.yml`.

---

## 📊 Processed Metadata Summary (v10.0.0)
| Dataset                 | Standards             | FAIR+CARE | License  |
|---|---|---|---|
| Hazards Composite      | STAC/DCAT/PROV-O      | ✅        | CC-BY 4.0 |
| Climate Summary        | STAC/DCAT             | ✅        | CC-BY 4.0 |
| Hydrology Summary      | DCAT/PROV-O           | ✅        | CC-BY 4.0 |
| Landcover Classification| STAC/DCAT            | ✅        | CC-BY 4.0 |
| Tabular Aggregates     | DCAT 3.0              | ✅        | CC-BY 4.0 |

---

## ♻️ Retention & Sustainability
| Data Type            | Retention | Policy |
|---|---:|---|
| Processed Metadata  | Permanent | Authoritative catalog record. |
| FAIR+CARE Certs     | Permanent | Governance continuity.        |
| Provenance Records  | Permanent | Immutable & ledger-logged.    |
| Validation Reports  | 365 Days  | Reproducibility reviews.      |

**Telemetry:** `../../../../releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation
```text
Kansas Frontier Matrix (2025). Processed Metadata Layer (v10.0.0).
FAIR+CARE-certified metadata repository harmonizing STAC, DCAT, and PROV-O standards for all processed KFM datasets.
Checksum-verified, governance-certified, and openly accessible for reproducible research and ethical stewardship.
```

---

## 🕰️ Version History
| Version | Date       | Author             | Summary |
|---|---|---|---|
| v10.0.0  | 2025-11-09 | `@kfm-metadata`    | Upgraded to v10: telemetry v2 bundling, Streaming STAC cross-links, JSON-LD governance certificates. |
| v9.7.0   | 2025-11-06 | `@kfm-metadata`    | Telemetry/schema refs aligned; examples & matrices refreshed. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Transparency × FAIR+CARE Ethics × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Work → Processed](../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>