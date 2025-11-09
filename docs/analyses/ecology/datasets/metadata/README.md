---
title: "🌿 Kansas Frontier Matrix — Ecology Dataset Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/ecology/datasets/metadata/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-ecology-datasets-metadata-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Ecology Dataset Metadata Registry**
`docs/analyses/ecology/datasets/metadata/README.md`

**Purpose:**  
Maintain the **FAIR+CARE-aligned metadata registry** for all ecology-related datasets in the Kansas Frontier Matrix (KFM).  
This registry ensures transparency, reproducibility, and ethical governance of ecological data by applying **STAC/DCAT 3.0**, **ISO 19115-3**, and **FAIR+CARE v3** metadata standards.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Ecology_Metadata-orange)](../../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Registry-brightgreen)](../../../../../../releases/)
</div>

---

## 📘 Overview

The **Ecology Dataset Metadata Registry** governs how biodiversity, land cover, and ecosystem data are cataloged, validated, and made accessible in KFM.  
Each metadata record documents provenance, licensing, spatial/temporal coverage, telemetry data, and FAIR+CARE ethical compliance for datasets used across species distribution, landcover, and ecosystem modeling workflows.

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/ecology/datasets/metadata/
├── README.md                                  # This document
├── stac_catalog.json                          # STAC 1.0 catalog for ecological datasets
├── dcat_metadata.json                         # DCAT 3.0 dataset distribution records
├── faircare_validation.json                   # FAIR+CARE and ISO validation report
├── provenance_log.json                        # Provenance, lineage, and checksum registry
└── iso19115_summary.xml                       # ISO 19115-3 metadata summary for geospatial assets
```

---

## 🧩 Metadata Standards Alignment

| Standard | Purpose | Validation Source |
|-----------|----------|--------------------|
| **STAC 1.0** | Spatial-temporal cataloging of datasets | `stac_catalog.json` |
| **DCAT 3.0** | Data discovery and distribution schema | `dcat_metadata.json` |
| **ISO 19115-3** | Geospatial metadata crosswalk and CRS documentation | `iso19115_summary.xml` |
| **FAIR+CARE v3** | Ethical and sustainability compliance | `faircare_validation.json` |

---

## 📑 STAC Example — GBIF Occurrence Records

```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "gbif-ecology-kansas",
  "collection": "ecology-biodiversity",
  "properties": {
    "description": "GBIF occurrence data for Kansas species used in habitat suitability modeling.",
    "license": "CC-BY 4.0",
    "keywords": ["biodiversity", "species", "habitat", "Kansas"],
    "datetime": "2025-01-01T00:00:00Z",
    "providers": [
      {"name": "Global Biodiversity Information Facility", "roles": ["producer", "licensor"]}
    ],
    "extent": {
      "spatial": {"bbox": [[-102.05, 36.99, -94.6, 40.0]]},
      "temporal": {"interval": [["1900-01-01", "2025-01-01"]]}
    }
  },
  "assets": {
    "data": {
      "href": "https://www.gbif.org/occurrence/search?state=Kansas",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 📄 DCAT Example — MODIS NDVI Time Series

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "@type": "dcat:Dataset",
  "dct:title": "MODIS NDVI Time Series for Kansas (2000–2025)",
  "dct:identifier": "modis-ndvi-kansas-2025",
  "dct:issued": "2025-11-09",
  "dct:license": "CC-BY 4.0",
  "dcat:keyword": ["NDVI", "vegetation", "remote sensing", "Kansas"],
  "dcat:temporalResolution": "monthly",
  "dcat:spatialResolutionInMeters": 250,
  "dcat:distribution": [{
    "dcat:accessURL": "https://modis.gsfc.nasa.gov/data/",
    "dct:format": "NetCDF"
  }],
  "dcat:spatialCoverage": {
    "@type": "dct:Location",
    "locn:geometry": "{\"type\": \"Polygon\", \"coordinates\": [[[-102.05,36.99],[-94.6,36.99],[-94.6,40.0],[-102.05,40.0],[-102.05,36.99]]] }"
  }
}
```

---

## 🧮 FAIR+CARE Validation Example

```json
{
  "validation_id": "ecology-metadata-2025-11-09-0167",
  "datasets_validated": [
    "GBIF Occurrence Data",
    "MODIS NDVI",
    "EPA Ecological Health",
    "USDA PLANTS"
  ],
  "metadata_checks": {
    "stac_schema": "Pass",
    "dcat_schema": "Pass",
    "iso19115_crosswalk": "Pass",
    "faircare_integrity": "Pass"
  },
  "energy_joules": 9.4,
  "carbon_gCO2e": 0.0041,
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:15:00Z"
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | Metadata indexed via STAC/DCAT with UUIDs | `stac_catalog.json` |
| **Accessible** | Metadata and datasets available under FAIR+CARE license | FAIR+CARE Ledger |
| **Interoperable** | JSON-LD and XML formats following DCAT and ISO standards | `telemetry_schema` |
| **Reusable** | Provenance, lineage, and license metadata stored | `manifest_ref` |
| **Responsibility** | ISO 50001 telemetry ensures validation sustainability | `telemetry_ref` |
| **Ethics** | Metadata reviewed for environmental and privacy ethics | FAIR+CARE Ethics Audit |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "ecology-metadata-ledger-2025-11-09-0168",
  "component": "Ecology Dataset Metadata Registry",
  "files": [
    "stac_catalog.json",
    "dcat_metadata.json",
    "iso19115_summary.xml"
  ],
  "energy_joules": 9.4,
  "carbon_gCO2e": 0.0041,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:17:00Z"
}
```

---

## 🧠 Sustainability Metrics

| Metric | Description | Value | Target | Unit |
|---------|-------------|--------|---------|------|
| **Energy (J)** | Energy used in metadata validation | 9.4 | ≤ 15 | Joules |
| **Carbon (gCO₂e)** | CO₂ emissions during metadata validation | 0.0041 | ≤ 0.006 | gCO₂e |
| **Telemetry Coverage (%)** | FAIR+CARE trace completion | 100 | ≥ 95 | % |
| **Audit Pass Rate (%)** | FAIR+CARE validation success | 100 | 100 | % |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published ecology metadata registry with STAC/DCAT examples and FAIR+CARE audit schema. |
| v10.2.1 | 2025-11-09 | Metadata & Governance Team | Added ISO crosswalk and telemetry record integration. |
| v10.2.0 | 2025-11-09 | KFM Ecology Team | Created baseline ecology metadata documentation aligned with climatology and hydrology modules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Ecology Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

