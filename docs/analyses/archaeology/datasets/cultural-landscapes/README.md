---
title: "🏞️ Kansas Frontier Matrix — Cultural Landscape Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-cultural-landscapes-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-cultural-landscapes"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🏞️ **Kansas Frontier Matrix — Cultural Landscape Datasets**  
`docs/analyses/archaeology/datasets/cultural-landscapes/README.md`

**Purpose:**  
Provide a **FAIR+CARE-governed, MCP-compliant index** of all cultural landscape datasets used in the Kansas Frontier Matrix (KFM).  
These datasets support archaeological reconstruction of **settlements**, **movement**, **territories**, **resource zones**, and **cultural interaction spheres** across Kansas’ prehistoric, protohistoric, and historic eras.

Cultural landscape datasets integrate into:

- Site distribution reconstruction  
- Artifact pattern interpretation  
- Story Nodes (culture timelines)  
- Focus Mode v2 cultural narratives  
- Cesium 3D reconstructions  
- MapLibre time-aware landscape layers  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Cultural landscape datasets represent **human-environment relationships** through time, including:

- Ancient routes & mobility corridors  
- Settlement regions & hinterlands  
- Tribal territories & interaction zones  
- Cultural phases & occupation extents  
- Sacred landscapes (appropriately generalized)  
- Resource procurement areas (stone, clay, fauna)  
- Ethnohistoric pathways documented in archival sources  

Only datasets that are **public-domain**, **open-license**, or **approved through tribal review** may be included.

Restricted or culturally protected information must be:

- **Generalized using H3 (levels 5–7)**  
- **Stripped of specific sacred-site coordinates**  
- **Reviewed by FAIR+CARE + Tribal Representatives**  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/
├── README.md                          # This file
├── regions/                           # Polygons of settlement regions, tribal areas (generalized)
├── routes/                            # Ancient mobility paths, seasonal routes
├── interaction-spheres/               # Cultural zones (e.g., Great Bend aspect)
├── resource-areas/                    # Procurement zones (e.g., chert, clay)
├── stac/                              # STAC Items/Collections for all landscape layers
├── metadata/                          # DCAT, CARE, and geospatial metadata
└── provenance/                        # PROV-O lineage logs
~~~

---

## 🌄 Cultural Landscape Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Settlement Regions** | Cultural-phase habitation zones | ✅ | Must be generalized; tribal review recommended |
| **Territorial Boundaries** | Tribal, political, or cultural extents | ⚠️ | Must be generalized + approved for public display |
| **Mobility Routes** | Trails, migration paths, war/peace routes | ✅ | Based on ethnohistoric + archaeological data |
| **Interaction Spheres** | Regions of shared material culture | ✅ | E.g., Great Bend aspect |
| **Resource Procurement Areas** | Quarries, clay beds, hunting zones | ⚠️ | Sensitive ecological or sacred areas must be generalized |
| **Sacred Landscapes** | Ceremonial regions, mythic geographies | 🔴 Prohibited unless approved | Must not include coordinates or shapes without tribal consent |

Prohibited content in this directory:

- Precise ceremonial site locations  
- Burial grounds  
- Restricted tribal knowledge  
- Non-consented ethnohistorical information  

---

## 📦 Required Metadata (All Cultural Landscape Layers)

### ✔ STAC Item / Collection
Each dataset MUST include:

| Field | Description |
|---|---|
| `id` | Unique identifier |
| `bbox` | H3 generalized bounding box |
| `geometry` | Polygon/MultiPolygon only |
| `start_datetime` / `end_datetime` | Temporal extent |
| `care:sensitivity` | Cultural sensitivity classification |
| `kfm:culture_phase` | Associated culture or occupation period |
| `assets` | Links to GeoJSON/COG/tilesets |
| `proj:*` | CRS, resolution, projection metadata |
| `kfm:provenance` | Reference to PROV-O lineage file |

### ✔ DCAT 3.0 Metadata

| Field | Example |
|---|---|
| `dct:title` | "Great Bend Aspect — Cultural Landscape" |
| `dct:license` | `"CC-BY 4.0"` |
| `dcat:distribution` | GeoJSON, vector tiles, or COG |
| `dct:temporal` | OWL-Time date span |
| `dcat:keyword` | `["archaeology", "cultural-landscape"]` |

### ✔ CARE Requirements

- Clear cultural notes  
- Explicit consent provenance  
- Sensitivity classification (`general`, `generalized`, `restricted`)  
- Removal of restricted cultural knowledge  

---

## 🧪 Data Preparation Requirements

All cultural landscape datasets must:

- Use **generalized geometries** (H3 or topological simplification)  
- Include **temporal phase** or cultural period  
- Use consistent schema fields (`region_id`, `culture_phase`, `geometry`, `sources`)  
- Provide **citation list** (archaeology, ethnohistory, tribal consultation)  
- Include a **provenance log**:
  - Data sources  
  - GIS processes  
  - Simplification parameters  
  - Review notes  

---

## 🛰️ Integration Into KFM Systems

### **Knowledge Graph (Neo4j)**
Nodes:

- `CulturalRegion`
- `Route`
- `ResourceArea`
- `InteractionSphere`

Relationships:

- `OCCUPIED_DURING`
- `TRAVERSED_BY`
- `ASSOCIATED_WITH`
- `GENERALIZED_FROM`

### **Story Nodes & Focus Mode v2**
Cultural landscape layers generate:

- Cultural-phase summaries  
- Movement narratives  
- Settlement expansion sequences  
- Provenance-linked interpretations  

### **Visualization Layers**
Produced visualizations include:

- Polygon cultural-region layers  
- H3 density mosaics  
- Vector route lines  
- Cesium 3D landscape models  

All visual layers must follow:

- `visualization` standards (`docs/analyses/archaeology/visualization/README.md`)  
- `validation` rules (`docs/analyses/archaeology/validation/README.md`)

---

## 📊 Dataset Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `regions/great-bend-aspect-v2` | Interaction Sphere | `regions/` | 🟢 Active | 2025-11 | Generalized + reviewed |
| `routes/ancient-prairie-traverse-v1` | Mobility Route | `routes/` | 🟢 Active | 2025-10 | Based on open-source ethnohistory |
| `resource-areas/flint-hills-chert-v1` | Procurement Area | `resource-areas/` | 🟡 Needs Review | 2025-09 | Check ecological sensitivity |
| `regions/pawnee-territory-v1` | Territorial Region | `regions/` | 🔴 Hold | Requires tribal consultation |

---

## 🧠 Example STAC Item (Generalized Cultural Region)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "great-bend-aspect-v2",
  "bbox": [-101.8, 37.0, -95.3, 40.5],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [[[ ... ]]]
  },
  "properties": {
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "start_datetime": "1200-01-01T00:00:00Z",
    "end_datetime": "1450-01-01T00:00:00Z",
    "kfm:provenance": "provenance/great-bend-aspect-v2.json"
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

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created dataset index; added cultural governance, metadata & generalization rules; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Archaeology Dataset Team | Initial directory structure & dataset categorization |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>