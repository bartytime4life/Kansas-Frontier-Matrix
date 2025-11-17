---
title: "🏺 Kansas Frontier Matrix — Archaeology Dataset Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-datasets-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Index"
intent: "archaeology-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Dataset Index**  
`docs/analyses/archaeology/datasets/README.md`

**Purpose:**  
Provide a FAIR+CARE–aligned, MCP-compliant index of all archaeological datasets integrated into the Kansas Frontier Matrix (KFM).  
Datasets span **prehistoric, protohistoric, and historic** periods and include **site gazetteers, artifact inventories, stratigraphic data, geophysical surveys, environmental samples**, and **cultural landscape maps**.

This index ensures consistent documentation, provenance, ethical handling of sensitive cultural information, and compatibility with **Story Nodes**, **Focus Mode**, **Neo4j graph ingestion**, and **STAC/DCAT metadata standards**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This directory contains all **archaeological datasets**, metadata manifests, and prepared derivatives used in KFM’s:

- **Archaeology Analysis Pipeline**
- **Cultural Landscape Reconstruction**
- **Prehistoric + Historic Timeline Layers**
- **AI-assisted Focus Mode (v2)**  
- **Story Node generation**  
- **Geo-temporal visualizations (MapLibre + Cesium)**  

Each dataset must include:

- **STAC Item or Collection**
- **DCAT metadata**
- **CARE attributes** (consent, sensitivity classification, cultural rules)
- **Checksum & provenance chain**
- **Spatial extent, temporal coverage, and CRS specification**

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/
├── README.md                       # This file
├── site-gazetteers/                # GNIS + academic site lists + tribal heritage mappings
├── artifact-inventories/           # Itemized artifact datasets (public-domain only)
├── stratigraphy/                   # Stratigraphic logs, soil layers, profiles
├── paleoenvironment/               # Pollen, charcoal, fauna, eco-samples (open datasets)
├── geophysics/                     # Magnetometry, GPR, LiDAR-derived features
├── cultural-landscapes/            # Ancient trails, settlements, mound distributions
├── stac/                           # STAC Items/Collections for all archaeology data
└── metadata/                       # DCAT + CARE metadata, provenance logs
~~~

---

## 🧭 Dataset Categories & Descriptions

| Category | Description | Examples | Notes |
|---|---|---|---|
| **Site Gazetteers** | Tabular or spatial datasets listing known archaeological sites | GNIS feature lists, academic site identifiers | Sensitive coordinates generalized via **H3 mosaic** per CARE |
| **Artifact Inventories** | Public-domain artifact counts, lithics, ceramics | WSU open-access catalogs, museum PD datasets | No restricted or provenance-sensitive items included |
| **Stratigraphy** | Soil horizons, excavation layer logs | KGS open soil layers, USDA soil pits | Used for reconstructing occupational phases |
| **Paleoenvironment** | Environmental proxies | Pollen cores, lake stratigraphy, fauna | Tied into climate + ecosystem timelines |
| **Geophysics** | Non-invasive survey datasets | Magnetometry PNGs/GeoTIFFs, GPR slices | Generalized for H3 grid privacy |
| **Cultural Landscapes** | Settlement distributions, ancient roads, territorial extents | Great Bend aspect distributions, protohistoric routes | Includes tribal requests for generalized boundaries |

---

## 🌐 External Data Sources (Open Access Only)

| Source | Domain | URL | Notes |
|---|---|---|---|
| **Open Context** | Global archaeological datasets | https://opencontext.org | CC-BY, structured JSON-LD |
| **ADS (UK Archaeology Data Service)** | Surveys & archives | https://archaeologydataservice.ac.uk | Select datasets relevant for comparative analysis |
| **Kansas Historical Society – Kansas Memory** | Photos, artifacts, documents | https://kansasmemory.org | Only PD/licensed materials included |
| **USGS / KGS** | Soil, stratigraphy, geologic data | https://kgs.ku.edu | Basis for landscape reconstructions |
| **Smithsonian Open Access** | Digitized artifacts | https://si.edu/openaccess | CC0 / CC-BY datasets only |

_All restricted, tribal, or culturally-sensitive datasets must go through FAIR+CARE review before ingestion._

---

## 🧩 Metadata & STAC Requirements

Each dataset must include:

| Requirement | Standard | Status |
|---|---|---|
| **Spatial Extent** | GeoJSON / bbox | Required |
| **Temporal Coverage** | OWL-Time (`start`, `end`, `precision`) | Required |
| **CRS** | EPSG:4326 default | Required |
| **Checksum** | SHA-256 | Required |
| **Provenance** | PROV-O (`wasDerivedFrom`) | Required |
| **CARE Flags** | Sensitivity, consent, cultural notes | Required |
| **STAC Item** | `stac_version: 1.0.0` | Required |
| **DCAT Dataset** | `dct:title`, `dct:license`, `dcat:distribution` | Required |

Example STAC snippet:

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "archaeology-site-gazetteer-v1",
  "bbox": [-102.0, 37.0, -94.6, 40.0],
  "properties": {
    "datetime": null,
    "kfm:temporal": "multi-period",
    "care:sensitivity": "generalized"
  },
  "assets": {
    "data": {
      "href": "https://example.com/site-gazetteer.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

---

## ⚖️ FAIR+CARE Cultural Responsibility

Archaeological datasets **must** adhere to:

- **CARE Principles** (Collective Benefit, Authority to Control, Responsibility, Ethics)  
- **Tribal consultation requirements**  
- **H3 generalization** for any culturally sensitive coordinates  
- **Ethical narrative framing** in Focus Mode + Story Nodes

Forbidden inclusions:

- Exact coordinates for sacred sites  
- Restricted tribal heritage records  
- Provenance-uncertain artifacts  
- Human remains or sensitive burial records  

---

## 📊 Dataset Status Tracking

| Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `site-gazetteers/statewide-v1` | Sites | 🟢 Active | 2025-11 | Coordinates generalized |
| `stratigraphy/flint-hills-v2` | Soil/Stratigraphy | 🟢 Active | 2025-10 | STAC + DCAT validated |
| `paleoenvironment/charcoal-cores-v1` | Eco | 🟡 Needs Review | 2025-09 | Add CARE consent info |
| `artifact-catalogs/ks-museum-v1` | Artifacts | 🟢 Active | 2025-11 | Public-domain verified |

---

## 🧠 How Datasets Integrate Into KFM

Archaeology datasets feed into:

- **Neo4j Knowledge Graph**  
  - Nodes: `Site`, `Artifact`, `Culture`, `OccupationPhase`, `StratLayer`, `Landscape`  
  - Relationships: `OCCURRED_IN`, `BELONGS_TO`, `ASSOCIATED_WITH`, `LOCATED_AT`

- **Story Nodes**  
  - Time-anchored site narratives  
  - Cultural-landscape evolution sequences  

- **Focus Mode v2**  
  - AI summaries with cultural safety filters  
  - Provenance chips and inclusivity scoring  

- **Map Layers**  
  - Site density heatmaps  
  - Cultural region polygons  
  - Stratigraphic layers  
  - LiDAR-derived mound features  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | FAIR+CARE + Archaeology Working Group | Added dataset index, STAC/DCAT requirements, cultural safety guidance; fixed all box-breaker issues |
| v10.0.0 | 2025-11-10 | Archaeology Group | Initial dataset structure proposal |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Analysis](../README.md)

</div>
