---
title: "⚙️ Kansas Frontier Matrix — Work Data Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.3.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-work-layer-v10.json"
governance_ref: "../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Work Data Layer**  
`data/work/README.md`

**Purpose:**  
Define the internal **Work Data Layer** of the Kansas Frontier Matrix (KFM), where **transformation, validation, AI pipelines, FAIR+CARE governance, and Streaming STAC** operations are performed.  
This layer ensures complete lineage, traceability, and ethical compliance between **raw ingestion** and **processed publication**, following **Diamond⁹ Ω / Crown∞Ω**, **FAIR+CARE**, and **MCP-DL v6.3** standards.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../docs/README.md)  
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Work%20Layer%20Certified-gold.svg)](../../docs/standards/faircare.md)  
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Aligned-2ea44f.svg)]()  
[![License: Internal](https://img.shields.io/badge/License-Internal-grey.svg)]()

</div>

---

## 📘 Overview

The **Work Data Layer** is the operational center of the KFM data lifecycle.  
It hosts **intermediate artifacts**, **transient workspace outputs**, **AI model runs**, **ethics validations**, and **schema-aligned staging data** prior to publication.

This layer bridges **raw → processed** through:

- Schema alignment  
- FAIR+CARE compliance  
- Telemetry + sustainability metrics  
- Explainability + bias auditing  
- STAC/DCAT catalog pre-generation  
- Streaming STAC promotion workflows  

### 🔧 v10.3.1 Enhancements  
- Updated telemetry endpoints for v10.3.0.  
- Harmonized work/staging directories with KFM v10 data contracts.  
- Improved lifecycle retention rules and validation gating.

---

## 🗂️ Directory Layout

~~~~~text
data/work/
├── README.md
│
├── tmp/                                   # Transient ETL/AI/validation workspace
│   ├── climate/
│   ├── hazards/
│   ├── hydrology/
│   ├── landcover/
│   ├── terrain/
│   ├── text/
│   ├── tabular/
│   └── logs/
│
├── staging/                               # Schema-aligned, audit-ready data
│   ├── tabular/
│   ├── spatial/
│   ├── metadata/
│   └── logs/
│
└── processed/                             # Pre-publication outputs awaiting release sync
    ├── climate/
    ├── hazards/
    ├── hydrology/
    ├── landcover/
    ├── tabular/
    ├── spatial/
    └── metadata/
~~~~~

---

## ⚙️ Workflow Summary

~~~~~mermaid
flowchart TD
  A["Raw Data<br/>(data/raw/*)"]
    --> B["Temporary Processing<br/>(data/work/tmp/*)"]
  B --> C["Validation + FAIR+CARE Audits<br/>(data/work/tmp/validation/)"]
  C --> D["Staging & Schema Alignment<br/>(data/work/staging/*)"]
  D --> E["Processed & Certified<br/>(data/work/processed/*)"]
  E --> F["STAC/DCAT Publication + Governance Ledger<br/>(data/stac/*)"]
~~~~~

### Lifecycle Phases

1. **Temporary (TMP)** — Cleaning, normalization, AI-supported validation.  
2. **Validation** — Schema, FAIR+CARE, checksum, explainability.  
3. **Staging** — Harmonized metadata & certification readiness.  
4. **Processed** — Certified datasets queued for release.  
5. **Publication** — Promotion to STAC/DCAT catalogs + governance ledger.

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|----------|----------------|-----------|
| **Findable** | Global STAC/DCAT indexing; manifest hashes. | @kfm-data |
| **Accessible** | Open formats preserved (CSV/GeoJSON/Parquet/GeoTIFF). | @kfm-accessibility |
| **Interoperable** | ISO 19115 + FAIR schemas. | @kfm-architecture |
| **Reusable** | Embedded checksums & lineage metadata. | @kfm-design |
| **Collective Benefit** | Supports community/tribal collaboration. | @faircare-council |
| **Authority to Control** | Council governs TMP → Processed promotions. | @kfm-governance |
| **Responsibility** | Ethical review, explainability logs. | @kfm-security |
| **Ethics** | Sensitive data masked/anonymized. | @kfm-ethics |

Governance logs:

- `data/reports/audit/data_provenance_ledger.json`  
- `data/reports/fair/data_care_assessment.json`

---

## 🧩 Example Metadata Record

~~~~~json
{
  "id": "work_layer_pipeline_hazards_v10.3.1",
  "domain": "hazards",
  "pipeline": "src/pipelines/etl/hazards_etl_pipeline.py",
  "records_processed": 23871,
  "staging_promotion": "2025-11-13T22:45:00Z",
  "checksum_sha256": "sha256:ac1b2f9e47b3a8f6d9e1a4c8b2f7e5c3a9d8e4b1c7f5a2e9d3b6a7f4c5e8b9a2",
  "validator": "@kfm-etl-ops",
  "fairstatus": "certified",
  "telemetry": {
    "energy_wh": 12.4,
    "co2_g": 16.2,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
~~~~~

---

## 🧹 Data Lifecycle Retention Policy

| Layer | Retention | Policy |
|-------|-----------|--------|
| TMP (Transient) | 7–14 days | Purged after staging promotion |
| Staging | 180 days | Retained for FAIR+CARE recertification |
| Processed (Pre-pub) | Until Release | Promoted to `data/processed/` when certified |
| Logs & Validation | 365 days | Archived for reproducibility and audits |

Automation: `work_layer_cleanup.yml`

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|--------|------:|-------------|
| Energy per ETL cycle | 21.3 Wh | @kfm-sustainability |
| Carbon Output | 26.1 gCO₂e | @kfm-security |
| Renewable Power | 100% (RE100) | @kfm-infrastructure |
| FAIR+CARE Compliance | 100% | @faircare-council |

Telemetry Source:  
```
../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧾 Internal Use Citation

```
Kansas Frontier Matrix (2025). Work Data Layer (v10.3.1).
FAIR+CARE-governed operational workspace supporting ETL, AI, validation,
and schema-aligned staging between raw ingestion and processed publication.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | @kfm-ops | Updated to v10.3; new telemetry paths; refreshed diagrams; retention policy updated. |
| v10.2.2 | 2025-11-12 | @kfm-ops | Streaming STAC updates; telemetry v2 integration; lifecycle hardening. |
| v10.0.0 | 2025-11-09 | @kfm-ops | Introduced streaming STAC, telemetry schema v10, lifecycle cleanup. |
| v9.7.0 | 2025-11-06 | @kfm-ops | Enhanced governance logs and schema references. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Data Operations × FAIR+CARE Ethics × Provenance Accountability*  
© 2025 Kansas Frontier Matrix — Internal · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Data Architecture](../ARCHITECTURE.md) · [Governance Charter](../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
