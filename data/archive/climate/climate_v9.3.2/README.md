---
title: "🌦️ Kansas Frontier Matrix — Climate Dataset v9.3.2 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/climate/climate_v9.3.2/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-ClimateExt.owl"
---

<div align="center">

# 🌦️ Kansas Frontier Matrix — **Climate Dataset v9.3.2**
`data/archive/climate/climate_v9.3.2/README.md`

**Purpose:** Immutable archived dataset of Kansas statewide climate metrics (temperature, precipitation, drought, and anomaly data) certified under FAIR+CARE v9.3.2 governance.  
Provides the foundation for environmental trend analysis, policy research, and Focus Mode AI-driven spatiotemporal reasoning.

[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Climate Dataset v9.3.2** is the official 2025 archival release of Kansas Frontier Matrix’s climate data collection.  
It merges NOAA, NCEI, NIDIS, and Kansas Mesonet datasets into unified, standardized GeoJSON layers.  
All data have passed full **FAIR+CARE** validation, checksum verification, and governance review under MCP-DL v6.3 reproducibility standards.

Key Highlights:
- Multi-decade continuous dataset (1900–2025).  
- Combines temperature, precipitation, drought indices, and anomaly layers.  
- Schema-aligned to STAC 1.0 and DCAT 3.0 metadata standards.  
- Used in Focus Mode for long-term climate visualization and analysis.

---

## 🗂️ Directory Layout

```plaintext
data/archive/climate/climate_v9.3.2/
├── README.md                          # This file — dataset overview
│
├── climate_summary_2025.geojson       # Annual temperature and precipitation summaries
├── climate_anomalies_2025.geojson     # Temperature and rainfall anomaly surfaces
├── drought_index_2025.geojson         # Palmer Drought Severity and SPI datasets
├── metadata.json                      # STAC item metadata
├── provenance_record.json             # Provenance and lineage record
├── validation_report.json             # Validation and FAIR+CARE audit summary
├── checksums.sha256                   # Integrity verification signatures
└── governance_approval.md             # FAIR+CARE Council approval record
```

---

## ⚙️ Dataset Composition

| Layer | Description | Source | Format |
|--------|--------------|---------|---------|
| `climate_summary_2025.geojson` | Mean monthly temperature and precipitation for 2025. | NOAA NCEI | GeoJSON |
| `climate_anomalies_2025.geojson` | Temperature and rainfall deviation from 20th-century averages. | NOAA CPC | GeoJSON |
| `drought_index_2025.geojson` | Palmer Drought Severity Index and SPI composites. | NOAA NIDIS, USDA | GeoJSON |

Spatial Reference: **EPSG:4326 (WGS84)**  
Temporal Coverage: **1900–2025**

---

## 🧩 Metadata Summary (STAC Item Extract)

```json
{
  "id": "climate_v9.3.2",
  "title": "Kansas Climate Summary Dataset (v9.3.2)",
  "description": "FAIR+CARE-certified integrated climate dataset for Kansas, including temperature, precipitation, and drought indices for 1900–2025.",
  "version": "v9.3.2",
  "created": "2025-10-28T15:00:00Z",
  "license": "CC-BY 4.0",
  "providers": [
    {"name": "NOAA NCEI", "role": "data-source"},
    {"name": "NIDIS", "role": "data-source"},
    {"name": "Kansas Mesonet", "role": "validator"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1900-01-01T00:00:00Z", "2025-12-31T00:00:00Z"]}
  },
  "keywords": ["climate", "precipitation", "temperature", "drought", "fair-care"]
}
```

---

## 🧠 FAIR+CARE Compliance Overview

| Principle | Implementation |
|------------|----------------|
| **Findable** | Indexed in STAC and manifest with globally unique identifier. |
| **Accessible** | Available under CC-BY 4.0; no authentication required. |
| **Interoperable** | Compliant with STAC 1.0 and DCAT 3.0 metadata structures. |
| **Reusable** | Full provenance and validation logs published alongside dataset. |
| **Collective Benefit** | Informs public climate awareness, policy, and research. |
| **Authority to Control** | Source organizations retain data ownership and attribution. |
| **Responsibility** | QA/QC and anomaly detection performed under council review. |
| **Ethics** | Sensitive data (e.g., private agricultural stations) redacted. |

All validation metrics recorded in:  
`data/reports/fair/data_care_assessment.json`

---

## 🔍 Validation & Governance Summary

| Validation Type | Status | Reference |
|------------------|---------|-----------|
| STAC Validation | ✅ Passed | `validation_report.json` |
| Schema Compliance | ✅ Passed | `schemas/climate_schema_v9.3.2.json` |
| FAIR+CARE Certification | ✅ Approved | `data/reports/fair/data_fair_summary.json` |
| Governance Sign-Off | ✅ Complete | `governance_approval.md` |

**Checksums:**  
All dataset assets verified via `checksums.sha256` and cross-listed in `releases/v9.3.2/manifest.zip`.

---

## 🧾 Provenance Record (Excerpt)

```json
{
  "dataset_id": "climate_v9.3.2",
  "source_agencies": ["NOAA NCEI", "NOAA CPC", "NIDIS"],
  "etl_pipeline": "src/pipelines/etl/climate/climate_pipeline.py",
  "compiled_by": "@kfm-etl-ops",
  "validated_by": "@kfm-data-lab",
  "archived_on": "2025-10-28T14:50:00Z",
  "checksum": "a3df91b22d87a4b44d88a0d9c07fcb17fddf1e1ac...",
  "linked_reports": {
    "stac_item": "data/stac/items/climate_v9.3.2.json",
    "audit_ledger": "data/reports/audit/data_provenance_ledger.json",
    "validation": "data/reports/validation/stac_validation_report.json"
  },
  "governance_status": "approved"
}
```

---

## ⚙️ Focus Mode Integration

This dataset powers the **Climate Focus Module**, enabling users to:
- Visualize multi-year drought trends.  
- Overlay climate anomalies with hazards or hydrological data.  
- Access AI-generated climate summaries and temporal forecasts.  

**Focus API Endpoints:**
- `/api/focus/climate?year=2025` — Fetches relevant anomaly summaries.  
- `/api/timeline/climate` — Provides event sequence for visualization.  

Telemetry recorded in `releases/v9.3.2/focus-telemetry.json`.

---

## ⚖️ Ethical Review Summary

> This dataset was reviewed by the **FAIR+CARE Council** on *2025-10-28* for compliance with open data ethics, scientific integrity, and equitable access standards.  
> Review Outcome: **Approved for permanent archival under Diamond⁹ Ω certification.**  
> No privacy, bias, or sensitive data concerns identified.

Full review notes:  
`data/reports/fair/ethics_review_summary.md`

---

## 🧾 Usage & Citation

**Access Path:**  
`data/archive/climate/climate_v9.3.2/`

**Citation Example:**
```text
Kansas Frontier Matrix (2025). Kansas Climate Dataset (v9.3.2).
FAIR+CARE-certified multi-decade climate archive integrating NOAA, NCEI, and NIDIS data.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/climate/climate_v9.3.2
License: CC-BY 4.0
```

---

## 🧾 Version Notes

- **Release v9.3.2 (2025):** Introduced temperature anomalies and drought indices aligned with FAIR+CARE standards.  
- **Enhancements:** Unified temporal coverage and improved metadata completeness.  
- **Governance:** Approved and signed by FAIR+CARE Council and @bartytime4life (Project Maintainer).  

---

<div align="center">

**Kansas Frontier Matrix** · *Climate Science × FAIR+CARE Ethics × Provenance-Based Open Data*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
