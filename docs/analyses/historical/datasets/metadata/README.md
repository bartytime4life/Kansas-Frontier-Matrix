---
title: "🏺 Kansas Frontier Matrix — Historical Dataset Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/historical/datasets/metadata/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-historical-datasets-metadata-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Historical Dataset Metadata Registry**
`docs/analyses/historical/datasets/metadata/README.md`

**Purpose:**  
Provide a centralized **metadata registry** for all historical archives, documents, maps, and demographic datasets within the Kansas Frontier Matrix (KFM).  
This registry ensures interoperability, provenance, and ethical stewardship of cultural data through compliance with **FAIR+CARE**, **CIDOC CRM (ISO 21127)**, and **STAC/DCAT 3.0** standards.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Historical_Metadata-orange)](../../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Registry-brightgreen)](../../../../../../releases/)
</div>

---

## 📘 Overview

The **Historical Metadata Registry** organizes and validates metadata for archival and historical datasets used in KFM.  
Each metadata record captures dataset lineage, temporal and spatial coverage, licensing, digitization provenance, and FAIR+CARE ethical compliance.  
This registry supports integration of archival knowledge with environmental and demographic data through the **CIDOC CRM** ontology.

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/historical/datasets/metadata/
├── README.md                                  # This document
├── stac_catalog.json                          # STAC catalog of historical datasets
├── dcat_metadata.json                         # DCAT 3.0 metadata for dataset distribution
├── faircare_validation.json                   # FAIR+CARE validation and ethics report
├── provenance_log.json                        # Provenance and checksum registry
└── iso19115_summary.xml                       # ISO 19115-3 metadata crosswalk
```

---

## 🧩 Metadata Standards Alignment

| Standard | Purpose | Validation Source |
|-----------|----------|--------------------|
| **STAC 1.0** | Spatio-temporal catalog for historical datasets | `stac_catalog.json` |
| **DCAT 3.0** | Dataset discovery and distribution schema | `dcat_metadata.json` |
| **ISO 19115-3** | Geospatial metadata alignment | `iso19115_summary.xml` |
| **CIDOC CRM (ISO 21127)** | Cultural heritage data provenance | `provenance_log.json` |
| **FAIR+CARE v3** | Ethics and sustainability governance | `faircare_validation.json` |

---

## 📑 STAC Example — Kansas Treaty Archives

```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "khs-treaty-archives-1850-1890",
  "collection": "historical-archives-kansas",
  "properties": {
    "description": "Digitized treaty and territorial archives from the Kansas Historical Society (1850–1890).",
    "license": "Public Domain",
    "keywords": ["treaty", "land", "indigenous", "archives", "Kansas"],
    "datetime": "2025-11-09T00:00:00Z",
    "providers": [
      {"name": "Kansas Historical Society", "roles": ["producer", "licensor"]}
    ],
    "extent": {
      "spatial": {"bbox": [[-102.05, 36.99, -94.6, 40.0]]},
      "temporal": {"interval": [["1850-01-01", "1890-12-31"]]}
    }
  },
  "assets": {
    "data": {
      "href": "https://kshs.org/archives/treaties",
      "type": "application/pdf",
      "roles": ["data"]
    }
  }
}
```

---

## 📄 DCAT Example — Chronicling America OCR Text Corpus

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "@type": "dcat:Dataset",
  "dct:title": "Chronicling America — Kansas Newspaper Archive (1870–1950)",
  "dct:identifier": "loc-chroniclingamerica-ks",
  "dct:issued": "2025-11-09",
  "dct:license": "Public Domain",
  "dcat:keyword": ["newspapers", "OCR", "Kansas", "history"],
  "dcat:temporalResolution": "annual",
  "dcat:distribution": [{
    "dcat:accessURL": "https://chroniclingamerica.loc.gov/",
    "dct:format": "application/json"
  }],
  "dcat:spatialCoverage": {
    "@type": "dct:Location",
    "locn:geometry": "{\"type\":\"Polygon\",\"coordinates\":[[[-102.05,36.99],[-94.6,36.99],[-94.6,40.0],[-102.05,40.0],[-102.05,36.99]]]}"
  }
}
```

---

## 🧮 FAIR+CARE Validation Example

```json
{
  "validation_id": "historical-metadata-2025-11-09-0187",
  "datasets_validated": [
    "KHS Treaty Archives",
    "LOC Sanborn Maps",
    "NARA Census Data",
    "Chronicling America Texts"
  ],
  "metadata_checks": {
    "stac_schema": "Pass",
    "dcat_schema": "Pass",
    "iso19115_crosswalk": "Pass",
    "cidoc_crm_alignment": "Pass",
    "faircare_integrity": "Pass"
  },
  "energy_joules": 9.3,
  "carbon_gCO2e": 0.0040,
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T18:15:00Z"
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | Indexed through STAC/DCAT with CIDOC CRM crosswalk | `stac_catalog.json` |
| **Accessible** | Metadata publicly accessible under CC-BY/Public Domain | FAIR+CARE Ledger |
| **Interoperable** | JSON-LD, XML, and CIDOC CRM ontologies | `telemetry_schema` |
| **Reusable** | Provenance and checksum logs embedded | `manifest_ref` |
| **Responsibility** | ISO 50001 telemetry ensures sustainability tracking | `telemetry_ref` |
| **Ethics** | Metadata reviewed for Indigenous and cultural sensitivity | FAIR+CARE Ethics Audit |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "historical-metadata-ledger-2025-11-09-0188",
  "component": "Historical Dataset Metadata Registry",
  "files": [
    "stac_catalog.json",
    "dcat_metadata.json",
    "iso19115_summary.xml"
  ],
  "energy_joules": 9.3,
  "carbon_gCO2e": 0.0040,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T18:17:00Z"
}
```

---

## 🧠 Sustainability Metrics

| Metric | Description | Value | Target | Unit |
|---------|-------------|--------|---------|------|
| **Energy (J)** | Energy used for metadata validation | 9.3 | ≤ 15 | Joules |
| **Carbon (gCO₂e)** | CO₂ emissions per validation | 0.0040 | ≤ 0.006 | gCO₂e |
| **Telemetry Coverage (%)** | FAIR+CARE trace completeness | 100 | ≥ 95 | % |
| **Audit Pass Rate (%)** | FAIR+CARE validation compliance | 100 | 100 | % |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published historical metadata registry with CIDOC CRM and STAC/DCAT examples. |
| v10.2.1 | 2025-11-09 | Metadata & Humanities Group | Added ISO 19115 crosswalk and FAIR+CARE governance schema. |
| v10.2.0 | 2025-11-09 | KFM Humanities Team | Created baseline historical metadata registry aligned with ecology and geology standards. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Historical Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

