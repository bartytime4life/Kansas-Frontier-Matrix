---
title: "🗂️ Kansas Frontier Matrix — Archaeology STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stac-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Catalog"
intent: "archaeology-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Archaeology STAC Catalog**  
`docs/analyses/archaeology/datasets/stac/README.md`

**Purpose:**  
Provide the **canonical STAC (SpatioTemporal Asset Catalog) index** for all archaeological datasets in the Kansas Frontier Matrix (KFM).  
This catalog ensures machine-discoverability, FAIR+CARE metadata completeness, reproducibility, cultural safety, and alignment with **STAC 1.0**, **DCAT 3.0**, **CIDOC-CRM**, **GeoSPARQL**, and **MCP-DL v6.3**.

STAC Items and Collections within this directory represent the authoritative metadata and access points for:

- Site Gazetteers  
- Artifact Inventories  
- Paleoenvironmental Datasets  
- Geophysical Survey Grids  
- Cultural Landscape Models  
- Derived Analytical Products  
- AI-Assisted Archaeology Outputs  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This directory houses **all STAC Items and Collections** describing archaeological datasets within the KFM ecosystem.

Each STAC entry must meet:

- **STAC 1.0.0 core specification**
- **Projection (`proj`) extension**
- **Scientific extension** (`sci:`)
- **Versioning extension** (`version:`)
- **Checksum extension**  
- **CARE metadata extension (`care:`)**  
- **KFM custom extensions** (`kfm:*` for archaeology domain attributes)

This ensures datasets are:

- Fully traceable  
- Ethically governed  
- Machine-readable  
- Compatible with KFM map layers, ETL pipelines, and Focus Mode v2  
- Indexable via static STAC browsing + future STAC API integration  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/stac/
├── README.md                           # This file
├── collections/                        # STAC Collections: grouped datasets
├── items/                              # Individual STAC Items
├── schemas/                            # JSON Schemas for STAC validation
└── examples/                           # Sample STAC items & annotated examples
~~~

---

## 🔖 STAC Collections (Required)

Each archaeological subdomain must have a STAC **Collection**, placed under `collections/`.

| Collection Name | Purpose | Example File |
|---|---|---|
| **Site Gazetteers** | Generalized archaeological site lists | `collections/site-gazetteers.json` |
| **Artifact Inventories** | Public-domain artifact datasets | `collections/artifact-inventories.json` |
| **Cultural Landscapes** | Regions, routes, interaction spheres | `collections/cultural-landscapes.json` |
| **Geophysics Surveys** | Magnetometry, GPR, LiDAR | `collections/geophysics.json` |
| **Paleoenvironment** | Pollen, charcoal, dendrochronology | `collections/paleoenvironment.json` |

Collections must include:

- Temporal extent  
- Spatial extent  
- License  
- Provider  
- Keywords  
- Version history  
- CARE sensitivity summary  
- Linkage to STAC Items  

---

## 📦 STAC Item Requirements (All Archaeology Datasets)

Every STAC Item in `items/` must include:

### **Core Fields**

| Field | Requirement |
|---|---|
| `id` | Unique, stable identifier |
| `type` | `"Feature"` |
| `bbox` | Spatial bounding box (generalized if needed) |
| `geometry` | Only generalized polygons or multipoints |
| `stac_version` | `"1.0.0"` |
| `properties.datetime` | Null or start time |
| `properties.start_datetime/end_datetime` | OWL-Time coverage |
| `assets` | Valid links to data files |
| `links` | `collection`, `parent`, `root` |

### **Required Extensions**

| Extension | Purpose |
|---|---|
| `proj` | CRS & raster metadata |
| `version` | Dataset versioning |
| `checksum` | SHA-256 verification |
| `scientific` (`sci:`) | Citation + DOI + scientific metadata |
| `kfm:` | Custom KFM archaeology metadata |
| `care:` | Cultural sensitivity metadata |

### **KFM Archaeology Extension Fields (`kfm:*`)**

| Field | Example |
|---|---|
| `kfm:culture_phase` | `"Late Prehistoric"` |
| `kfm:site_type` | `"village"` |
| `kfm:datatype` | `"magnetometry-grid"` |
| `kfm:source` | `"Kansas Geological Survey"` |
| `kfm:provenance` | Path to PROV-O file |

### **CARE Metadata Fields (`care:`)**

Required for all archaeological datasets:

| Field | Allowed Values |
|---|---|
| `care:sensitivity` | `general`, `generalized`, `restricted` |
| `care:notes` | Text description |
| `care:review` | `"tribal"`, `"faircare"`, `"none-required"` |

---

## 🌍 Spatial/Temporal Requirements

| Component | Requirement |
|---|---|
| **CRS** | EPSG:4326 unless justified |
| **Geometry** | Generalized via H3 or simplified polygon |
| **Temporal Extent** | OWL-Time |
| **Sensitivity** | Coordinate precision must align with CARE classification |

Sensitive datasets must be generalized:

- **H3 Level 5–7**  
- Topological simplification for polygons  
- Removal of fine-grained features  

---

## 🔗 Example STAC Item (Archaeology — Generalized)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-cultural-landscape-great-bend-v2",
  "bbox": [-101.5, 37.5, -96.0, 39.5],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[ /* generalized */ ]]]
  },
  "properties": {
    "start_datetime": "1200-01-01T00:00:00Z",
    "end_datetime": "1450-01-01T00:00:00Z",
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/great-bend-v2.json"
  },
  "assets": {
    "data": {
      "href": "https://example.com/cultural_landscapes/great_bend_aspect_v2.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🧪 Validation Requirements

All STAC items must pass:

- **STAC JSON schema validation**  
- **KFM Archaeology Extension schema validation**  
- **CARE sensitivity validation**  
- **Checksum verification**  
- **DCAT crosswalk check**  
- **Spatial/Temporal alignment**  
- **Provenance completeness**  

Validation workflows are in:

- `docs/analyses/archaeology/validation/`  
- `.github/workflows/stac-validate.yml`

---

## 📊 STAC Catalog Index

| Category | Collection | Examples |
|---|---|---|
| **Site Gazetteers** | `collections/site-gazetteers.json` | `items/site-gazetteer-v1.json` |
| **Artifact Inventories** | `collections/artifacts.json` | `items/artifacts-flint-hills-v1.json` |
| **Cultural Landscapes** | `collections/cultural-landscapes.json` | `items/great-bend-aspect-v2.json` |
| **Geophysics** | `collections/geophysics.json` | `items/magnetometry-north-ks-v1.json` |
| **Paleoenvironment** | `collections/paleoenvironment.json` | `items/pollen-flint-hills-v1.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created STAC catalog framework; added KFM archaeology extensions; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Archaeology Metadata Team | Initial structure & baseline STAC requirements |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>