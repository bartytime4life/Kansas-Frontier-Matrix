---
title: "🧲 Kansas Frontier Matrix — Archaeological Geophysics Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/geophysics/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-datasets-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-geophysics-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧲 **Kansas Frontier Matrix — Archaeological Geophysics Datasets**  
`docs/analyses/archaeology/datasets/geophysics/README.md`

**Purpose:**  
Provide a comprehensive, FAIR+CARE–aligned, MCP-compliant index of **archaeological geophysics datasets** in the Kansas Frontier Matrix (KFM).  
Includes **magnetometry**, **ground-penetrating radar (GPR)**, **electrical resistivity**, **LiDAR-derived archaeological features**, and **derived interpretative surfaces** used for cultural landscape reconstruction.

These datasets support:

- Non-invasive archaeological site detection  
- Cultural landscape mapping  
- Artifact and feature correlation  
- 2D + 3D visualization (MapLibre + Cesium)  
- Story Nodes & Focus Mode v2 interpretations  
- Graph-based spatial reasoning (Neo4j + GeoSPARQL)

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Archaeological geophysics datasets in KFM include:

- **Magnetometry grids** (PNG, GeoTIFF, COG)  
- **Ground-penetrating radar time-slices**  
- **Electrical resistivity transects**  
- **LiDAR-derived archaeological features** (generalized)  
- **Raster anomalies detected with AI-assisted scripts**  
- **Interpreted features** (borrow pits, palisades, house basins, earthworks)  

Only **open-access**, **public-domain**, or **explicitly permitted** datasets may be included.

Restricted datasets (raw sacred features, unreviewed tribal landscapes) **must not appear** in this directory.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/geophysics/
├── README.md                          # This file
├── raw/                               # Open-access source grids (PD-only)
├── processed/                         # Cleaned, filtered, generalized geophysics data
├── interpreted/                       # Human-verified interpretations (feature outlines)
├── stac/                              # STAC Items & Collections for geophysics datasets
├── metadata/                          # DCAT + CARE metadata files
└── provenance/                        # PROV-O lineage for geophysics datasets
~~~

---

## 🧭 Geophysics Dataset Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Magnetometry** | Magnetic field anomalies; excellent for detecting pits, ditches, structures | ✅ | Must be generalized & processed |
| **GPR** | Subsurface slices showing floors, pits, features | ⚠️ | Only publicly released slices; depth > 30 cm generalized |
| **Electrical Resistivity** | Soil moisture contrasts; reveals ditches/buildings | ✅ | PD-only datasets |
| **LiDAR Features** | DEM-derived earthworks, mounds, landscape forms | ⚠️ | Must avoid showing protected burial mounds |
| **AI-Detected Features** | ML outputs highlighting anomalies | ⚠️ | Requires validation notebook |
| **Interpretation Layers** | Human-validated features (polygons/lines) | ✅ | Must include justification and metadata |

Forbidden:

- Unapproved raw GPR volumes  
- Unprocessed sensitive LiDAR tiles  
- Any burial information or sacred features  
- Exact coordinates of protected archaeological features  

---

## 📦 Required Metadata for All Geophysics Datasets

### ✔ STAC Item Requirements

| Field | Description |
|---|---|
| `id` | Unique ID |
| `bbox` | H3 generalized bounding box |
| `geometry` | Polygon/MultiPolygon |
| `start_datetime` / `end_datetime` | Applicable if temporal context known |
| `care:sensitivity` | `generalized`, `restricted-generalized` |
| `assets` | Links to raster grids, interpretations, tilesets |
| `proj:*` | CRS, resolution, transform |
| `kfm:provenance` | PROV-O JSON file |

### ✔ DCAT Metadata Requirements

| Field | Example |
|---|---|
| `dct:title` | "North Kansas Magnetometry Survey (PD)" |
| `dcat:distribution` | COG raster tileset |
| `dct:license` | `"CC-BY 4.0"` or `"CC0"` |
| `dct:temporal` | OWL-Time interval |
| `dcat:keyword` | `["geophysics", "magnetometry", "archaeology"]` |

### ✔ CARE Requirements

- No depiction of protected sacred landscapes  
- Coordinate generalization & obfuscation mandatory  
- All interpretations require **cultural review**  
- Clear notes on cultural sensitivity levels  

---

## 🧪 Data Preparation Requirements

All datasets must:

- Be filtered, corrected, and cleaned  
- Use standardized naming conventions  
- Remove grid noise (if needed)  
- Use **H3 spatial generalization** for sensitive areas  
- Include processing logs in `provenance/`  
- Document all classification parameters  

Generalization rules:

- Never display feature-level resolution for sensitive sites  
- Earthwork locations must be blurred, offset, or polygon-generalized  
- Raster resolution must be degraded when needed (e.g., > 2 m/pixel)

---

## 🛰️ Integration Into KFM Systems

### **Knowledge Graph (Neo4j)**

Nodes:

- `GeophysicsSurvey`
- `MagnetometryGrid`
- `GPRSlice`
- `InterpretedFeature`
- `LiDARFeature`
- `LandscapeUnit`

Relationships:

- `DETECTS_FEATURE`
- `LOCATED_AT`
- `ASSOCIATED_WITH`
- `GENERALIZED_FROM`

### **Focus Mode v2**

Geophysics datasets produce:

- Interpretive overlays  
- Confidence-weighted anomaly maps  
- Explanatory summaries with provenance chips  
- Bias-mitigated descriptions  

### **Story Nodes**

Geophysics contributes to:

- Cultural reconstruction narratives  
- Archaeological feature timelines  
- Settlement explanations  

All narratives undergo **CARE tone review**.

---

## 🌄 Visualization Standards

Geophysics visual outputs must follow:

- `docs/analyses/archaeology/visualization/README.md`  
- Raster formats: **COG**, **GeoTIFF**, generalized PNG  
- Vector formats: **GeoJSON**, **Vector Tiles**  
- 3D formats: **Cesium Tilesets** for allowed features  

Every visual layer must include:

| Field | Requirement |
|---|---|
| CRS | EPSG:4326 |
| Temporal extent | OWL-Time compliant |
| Sensitivity | CARE flag |
| Provenance | PROV-O trace |
| STAC item reference | Required |

---

## 📊 Dataset Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `magnetometry/north-ks-survey-v1` | Magnetometry | `processed/` | 🟢 Active | 2025-11 | Fully generalized |
| `gpr/high-plains-slice-v2` | GPR | `processed/` | 🟡 Needs Review | 2025-09 | Validate depth range |
| `lidar/prairie-mounds-v1` | LiDAR | `interpreted/` | 🔴 Hold | Requires cultural approval |
| `interpretations/central-ks-v1` | Interpretation | `interpreted/` | 🟢 Active | 2025-11 | Review completed |

---

## 🧠 Example STAC Item (Generalized Geophysics Dataset)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "magnetometry-north-ks-v1",
  "bbox": [-101.8, 37.4, -95.8, 40.1],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[ ... ]]]
  },
  "properties": {
    "care:sensitivity": "generalized",
    "kfm:survey_type": "magnetometry",
    "kfm:provenance": "provenance/mag-north-ks-v1.json"
  },
  "assets": {
    "grid": {
      "href": "https://example.com/geophysics/mag_north_ks_v1.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created geophysics dataset index; added generalization rules + STAC/DCAT metadata requirements; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Geophysics Dataset Team | Initial conceptual structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>