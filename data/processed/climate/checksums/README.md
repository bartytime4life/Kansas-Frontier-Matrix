---
title: "🌡️ Kansas Frontier Matrix — Climate Checksums Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/climate/checksums/README.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-processed-climate-checksums-v11.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Checksum Registry"
intent: "climate-integrity"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
provenance_chain:
  - "data/processed/climate/checksums/README.md@v10.0.0"
  - "data/contracts/data-contract-v3.json"
ontology_alignment:
  cidoc: "E30 Right"
  prov: "prov:Entity"
  dcat: "Distribution"
story_node_refs: []
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
doc_uuid: "urn:kfm:data-processed:climate:checksums"
semantic_document_id: "kfm-climate-checksums-v11"
event_source_id: "ledger:climate_checksums_v11"
immutability_status: "immutable-after-release"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "3d-context-render"
ai_transform_prohibited:
  - "content-alteration"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "active"
ttl_policy: "24 months"
sunset_policy: "Supersedes v10.0.0 after Nov 2025"
---

<div align="center">

# 🌡️ Kansas Frontier Matrix — **Climate Checksums Registry**  
`data/processed/climate/checksums/README.md`

**Purpose:**  
Provide **integrity verification, reproducibility guarantees, cryptographic provenance, and FAIR+CARE-compliant governance** for all processed **climate datasets** in the Kansas Frontier Matrix.  
This registry certifies **Q4 2025 processed climate outputs**, including gridded temps, precipitation composites, drought anomaly layers, reanalysis harmonizations, and derivative risk indicators.

[![MCP-DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue.svg)]()  
[![KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM%E2%80%91MDP_v11.0.0-purple.svg)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold.svg)]()  
[![STAC](https://img.shields.io/badge/STAC-1.0.0-green.svg)]()  
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0-blue.svg)]()  
[![Integrity Ledger](https://img.shields.io/badge/Provenance-Ledger%20Verified-grey.svg)]()

</div>

---

## 📘 Overview

This registry contains the **canonical checksum manifest** for all processed climate layers included in KFM v11.  
All checksum entries are:

- SHA-256 verified  
- Logged in the **Data Provenance Ledger**  
- Cross-linked to STAC/DCAT catalogs  
- Ethically validated under **CARE**  
- Machine-parsable for automated ETL + Focus Mode engines  
- Bound by **Data Contract v3.0.1** and **ISO 19115 lineage**  
- Included in CI/CD integrity workflows (checksum-verify.yml)

Climate domains covered:

- 📈 Temperature composites (Daymet, PRISM, reanalysis blends)  
- 🌧️ Precipitation models & radar-corrected grids  
- 🔥 Evapotranspiration + heat-index rasters  
- 🌾 Drought anomaly indicators (SPI/NDVI/Soil moisture)  
- 🧭 Climate-hazard derivatives (heatwave probabilities, freeze risk)

---

## 🗂️ Directory Layout

```text
data/processed/climate/checksums/
├── README.md                      # This file — climate checksum registry (v11)
│
├── temp_composite.sha256         # Temperature composites (Q4 2025)
├── precip_composite.sha256       # Precipitation reanalysis layers
├── drought_indicators.sha256     # SPI/soil moisture/NDVI drought metrics
├── climate_derivatives.sha256    # Hazard-linked climate derivatives
└── manifest.json                 # Consolidated STAC/DCAT-aligned checksum manifest
```

---

## 🧩 STAC/DCAT-Compatible Checksum Manifest Example

```json
{
  "id": "kfm_climate_checksums_v11",
  "type": "ChecksumCollection",
  "title": "KFM Processed Climate Checksums (v11 · Q4 2025)",
  "provenance": {
    "prov:wasGeneratedBy": "pipeline:climate_etl_v11",
    "prov:wasAssociatedWith": "agent:kfm-data-council",
    "checksum_method": "sha256"
  },
  "items": [
    {
      "id": "temp_composite_v11",
      "sha256": "3c4fb91e1870f5fc9adc01d8e3...",
      "source_asset": "../../processed/climate/temp_composite.tif",
      "last_verified": "2025-11-20T18:20:00Z"
    },
    {
      "id": "precip_composite_v11",
      "sha256": "8b12ae9bca2ebd8909fbdf110a...",
      "source_asset": "../../processed/climate/precip_composite.tif",
      "last_verified": "2025-11-20T18:20:00Z"
    }
  ]
}
```

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Checksums indexed in STAC/DCAT; semantic IDs | `@kfm-data` |
| **Accessible** | Public CC-BY ledger files | `@kfm-accessibility` |
| **Interoperable** | STAC/DCAT/ISO-compliant manifests | `@kfm-architecture` |
| **Reusable** | Full provenance + cryptographic signatures | `@kfm-design` |
| **Collective Benefit** | Ensures trustworthy open climate data | `@faircare-council` |
| **Authority to Control** | Governance ledger validation | `@kfm-governance` |
| **Responsibility** | Continuous checksum monitoring | `@kfm-security` |
| **Ethics** | CARE-reviewed climate layers | `@kfm-ethics` |

---

## ⚙️ Verification Workflow

| Stage | Workflow | Output |
|---|---|---|
| Extract + Hash | `checksum-generate.py` | `*.sha256` |
| STAC Merge | `stac-manifest-merge.py` | `manifest.json` |
| Governance Verify | `governance-ledger.yml` | Ledger signatures |
| CI Integrity Check | `checksum-verify.yml` | Pass/Fail |

Telemetry reference:  
`../../../../releases/v11.0.0/focus-telemetry.json`

---

## 📏 Sustainability Metrics

| Metric | Target | Verified By |
|---|---|---|
| Checksum Coverage | 100% | `@kfm-validation` |
| Ledger Accuracy | 100% | `@kfm-governance` |
| Energy per Hash | ≤ 3.8 Wh | `@kfm-sustainability` |

---

## 🕰️ Version History

| Version | Date | Author | Notes |
|---|---|---|---|
| v11.0.0 | 2025-11-20 | `@kfm-data` | Upgraded to MDP v11; added PROV-O lineage & STAC/DCAT manifest. |
| v10.0.0 | 2025-11-10 | `@kfm-data` | Added baseline checksum generation & ledger linking. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Integrity × Governance × Reproducibility*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[⬅ Back to Climate Data](../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md) · [Integrity Ledger](../../../reports/audit/data_provenance_ledger.json)

</div>