---
title: "🏺 Kansas Frontier Matrix — STAC Collection: Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/README.md"
version: "v10.4.1"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Archaeology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-archaeology-interaction-spheres-stac-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Documentation"
intent: "archaeology-interaction-spheres-stac"
semantic_document_id: "kfm:docs:analyses:archaeology:interaction-spheres:protohistoric-wichita:stac"
doc_uuid: "<uuid-placeholder>"
accessibility_compliance: "WCAG 2.1 AA (intended)"
machine_extractable: true
---

<div align="center">

# 🏺✨ **Kansas Frontier Matrix — STAC Collection: Protohistoric Wichita Interaction Sphere** ✨🏺  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/README.md`

**Purpose:**  
Define, document, and certify the **FAIR+CARE-aligned STAC Collection + Item suite** for the archaeologically significant  
**Protohistoric Wichita Interaction Sphere (ca. 1400–1700 CE)** — integrating settlement generalizations, trade corridors,  
ceramic networks, radiocarbon envelopes, paleoenvironmental variables, and ethnohistoric maps for KFM v10.

### 🏆 Certifications  
[![Diamond⁹ Ω](https://img.shields.io/badge/Diamond%E2%81%B9-Ω-blueviolet)](#)
[![Crown∞Ω](https://img.shields.io/badge/Crown-∞Ω-gold)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Verified-green)](#)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](#)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](#)

</div>

--- ✦ ---

## 🌐 Overview

The **Protohistoric Wichita Interaction Sphere** represents a dynamic cultural, environmental, and geopolitical landscape  
stretching across south-central Kansas and adjacent regions during the protohistoric period.

This STAC collection provides unified, semantic, and reproducible metadata for:

- 🧱 Generalized Wichita settlement clusters (H3 / hex grids)  
- 📡 Trade & mobility corridors (least-cost + ethnohistoric inference)  
- 🌀 Ceramic network relations (paste groups, decorations, compositional associations)  
- 🧪 Radiocarbon probability envelopes (summed PDFs)  
- 🌿 Paleoenvironmental reconstructions (hydrology, soils, fire, vegetation, climate)  
- 🗺️ Ethnohistoric cartography (Spanish, French, US, tribal sources)

Designed for **Focus Mode v2**, **Story Nodes v3**, **Neo4j ingestion**,  
and **MapLibre map layers**, this dataset is a cornerstone of the KFM archaeological analytics environment.

--- ✦ ---

## 📁 Directory Layout (DL-C Emoji Tree)

```text
protohistoric-wichita/ 🏺✨
├── metadata/ 📘
│   └── README.md 📝
│
├── provenance/ 🧬
│   └── README.md 📝
│
└── stac/ 📦🧭
    ├── collection.json 🗂️
    ├── items/ 📁🌐
    │   ├── settlements-generalized-h3.json 🧱
    │   ├── trade-corridors.json 📡
    │   ├── ceramic-network.json 🌀
    │   ├── radiocarbon-bands.json 🧪
    │   ├── paleoenvironmental-overlays.json 🌿
    │   └── ethnohistoric-cartography.json 🗺️
    └── README.md 📖 (← this file)
````

--- ✦ ---

## 🗂️ STAC Collection (`collection.json`)

### ⭐ Core Elements

* `type`: `"Collection"`
* `id`: `"protohistoric-wichita-interaction-sphere"`
* `title`, `description`: cultural & environmental scope
* `license`: `"CC-BY-4.0"` or CARE-constrained variants
* `keywords`: Wichita, Great Bend, protohistoric, archaeology
* `extent`:

  * 📍 Spatial bbox
  * ⏳ Temporal interval (OWL-Time compliant)

### 🧩 Extensions Used

* `proj:` (CRS / geometry projection info)
* `checksum:` dataset integrity
* `version:` dataset-level version control
* `scientific:` citations + DOI
* `label:` optional symbolic metadata

### 🛡️ CARE Metadata

Required for sensitive-site handling:

* `care:sensitivity_level`
* `care:governance`
* `care:notes`

--- ✦ ---

## 📄 STAC Items in `items/`

Each STAC Item inherits the collection ID and provides:

* geometry
* temporal attributes
* asset links
* dataset-specific properties

### 🧱 settlements-generalized-h3.json

Generalized settlement clusters (H3, hex grids).
Used in heat maps and cultural landscape footprints.

### 📡 trade-corridors.json

Hypothesized terrestrial corridors based on network analysis + ethnohistoric records.

### 🌀 ceramic-network.json

Node/edge metrics, ceramic types, cluster communities, spatial embedding.

### 🧪 radiocarbon-bands.json

Summed PDFs → temporal probability envelopes.

### 🌿 paleoenvironmental-overlays.json

Hydrology, soils, fire frequency, vegetation, climatic window variables.

### 🗺️ ethnohistoric-cartography.json

Digitized geometries from historic and tribal cartographic sources.

--- ✦ ---

## 🛠️ Pipeline & ETL Integration

### 🧠 ETL Flow

* STAC discovery → validation → checksum verification
* Projection normalization (EPSG:4326)
* Graph loading:

  * `Dataset`
  * `Layer`
  * `Place`
  * `Event`
  * `Network`
* CARE flags propagate into graph properties
* Multi-source provenance stored in PROV-O mappings

### 🗺️ Web UI Integration

* MapLibre layers auto-register
* Time slider sync from radiocarbon bands
* Environmental layers render as COGs or GeoJSON
* Story Node context auto-activates relevant layers

--- ✦ ---

## 📜 Story Node Integration (v3)

Story Nodes that commonly reference this dataset include:

* **proto-wichita-overview**
* **environmental-context-1500CE**
* **trade-and-ceramics**
* **corridor-systems**

Each Story Node references STAC assets via:

```yaml
relations:
  - rel: "supports"
    target: "settlements-generalized-h3"
```

Story Nodes use STAC geometry (for camera focus) and time intervals (for slider sync).

--- ✦ ---

## 🕸️ Graph Entity Mapping (Neo4j)

| STAC Element       | Neo4j Entity                    | Notes                                   |
| ------------------ | ------------------------------- | --------------------------------------- |
| Collection         | `(:Dataset)`                    | Top-level Protohistoric Wichita dataset |
| Settlements        | `(:Layer {type:'settlements'})` | Generalized sites                       |
| Corridors          | `(:Layer {type:'corridor'})`    | Mobility routes                         |
| Ceramic Network    | `(:Network)` + `(:Site)`        | Edges: `[:CERAMIC_LINK]`                |
| Radiocarbon Bands  | `(:Layer {type:'rc-band'})`     | Linked to `(:Event)`                    |
| Paleoenvironment   | `(:Layer {type:'env'})`         | Covariates                              |
| Ethnohistoric Maps | `(:Map)`                        | `[:DERIVED_FROM]` references            |
| CARE Flags         | Node/Rel props                  | Sensitivity enforcement                 |

--- ✦ ---

## 🕓 Version History

| Version | Date       | Steward         | Notes                         |
| ------- | ---------- | --------------- | ----------------------------- |
| v10.4.1 | 2025-11-17 | Lead Programmer | SEP-B edition + C-1 aesthetic |
| v10.4.0 | 2025-11-15 | Archaeology WG  | Initial STAC implementation   |

--- ✦ ---

## 👑 Footer & Certifications

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**
**FAIR+CARE Compliant · STAC 1.0.0 Validated · CIDOC CRM / OWL-Time / GeoSPARQL**
**Archaeology Data & Ethics Charter Enforced**

> After any modification, update `version`, `last_updated`, and re-run KFM CI STAC validators.

--- ✦ ---
