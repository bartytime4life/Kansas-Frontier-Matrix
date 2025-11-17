---
title: "🪨 Kansas Frontier Matrix — Stratigraphy Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/stratigraphy/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-stratigraphy-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-stratigraphy-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🪨 **Kansas Frontier Matrix — Stratigraphy Datasets**  
`docs/analyses/archaeology/datasets/stratigraphy/README.md`

**Purpose:**  
Define and index all **stratigraphic datasets** used in the Kansas Frontier Matrix (KFM), including soil layers, excavation profiles, depositional sequences, and chronologically calibrated stratigraphy reconstructions.  
These datasets underpin:

- Occupational phase modeling  
- Cultural layer reconstruction  
- Geoarchaeological interpretations  
- Paleoenvironmental correlation  
- Story Nodes & Focus Mode v2 contextual timelines  
- 2D/3D stratigraphic visualizations (MapLibre, Cesium)

All stratigraphy datasets must follow **FAIR+CARE**, **CIDOC-CRM**, **GeoSPARQL**, **STAC 1.0**, **DCAT 3.0**, and **MCP-DL v6.3**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Stratigraphy datasets include:

- Excavation layer descriptions (generalized)  
- Soil horizons (A/B/C horizons, loess, paleosols)  
- Cultural strata (middens, construction layers)  
- Geoarchaeological trench profiles  
- Stratigraphic cross-sections  
- Sediment chronology (age–depth models)  
- 3D stratigraphic reconstructions  

Prohibited content:

- Exact coordinates of excavation units  
- Burial strata or culturally sensitive contexts  
- Confidential site-level stratigraphic logs  

All spatial coordinates must be generalized using **H3 level 5–7**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/stratigraphy/
├── README.md                          # This file
├── profiles/                          # Generalized excavation profiles, stratigraphy logs
├── cross-sections/                    # Raster/Vector cross-sections
├── temporal-models/                   # Age-depth models & chronology
├── stac/                              # STAC Items/Collections for stratigraphy datasets
├── metadata/                          # DCAT + CARE + geological metadata
└── provenance/                        # PROV-O lineage logs
~~~

---

## 🧭 Stratigraphy Dataset Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Excavation Profiles** | Layer descriptions, soil stratigraphy | ⚠️ | Must be generalized; remove restricted units |
| **Soil Horizons** | Pedological horizons, soil types | ✅ | KGS + USDA open datasets allowed |
| **Cultural Layers** | Middens, structural layers | ⚠️ | No sensitive context allowed |
| **Geoarchaeology Profiles** | Sedimentology + depositional sequences | ✅ | PD datasets |
| **Stratigraphic Cross-Sections** | Cross-site comparisons | ✅ | Raster/vector allowed if generalized |
| **Chronology Models** | Age–depth models for layers | ✅ | Must include uncertainty bounds |

Forbidden: excavation unit coordinates, human remains data, or burial layers.

---

## 📦 Required Metadata (All Stratigraphy Datasets)

### ✔ STAC Item Requirements

| Field | Description |
|---|---|
| `id` | Unique dataset identifier |
| `bbox` | Generalized bounding box |
| `geometry` | Generalized polygons or lines |
| `start_datetime` / `end_datetime` | Phase or deposition interval |
| `care:sensitivity` | `"generalized"` or `"restricted-generalized"` |
| `assets` | Links to logs, profiles, cross-sections |
| `kfm:provenance` | Link to PROV-O log |
| `proj:*` | CRS, transform |

### ✔ DCAT 3.0 Metadata

| Field | Example |
|---|---|
| `dct:title` | "Excavation Profiles — Flint Hills" |
| `dct:license` | `"CC-BY 4.0"` |
| `dcat:distribution` | CSV, GeoJSON, PNG profiles |
| `dct:temporal` | Cultural or depositional date span |
| `dcat:keyword` | `["stratigraphy", "soil", "geoarchaeology"]` |

### ✔ CARE Cultural Safety

- Remove explicit coordinates  
- Replace excavation unit IDs with pseudonyms  
- Downsample images to avoid exposing sensitive features  
- Provide cultural notes & context warnings  

---

## 🧪 Data Preparation Requirements

All datasets must:

- Use **standard schema fields** (`layer_id`, `unit_code`, `soil_class`, `phase`, `depth_cm`, `notes`, `sources`)  
- Include **uncertainty** (σ, confidence intervals)  
- Provide full documentation of **methods & parameters**  
- Pass cultural, scientific, and metadata validation steps  
- Include visualizations in generalized form  

Generalization rules:

- Remove grid-level detail from excavation logs  
- H3 generalization for any location  
- Abstracted descriptions for culturally sensitive layers  

---

## 🛰️ Integration Into KFM Systems

### **Knowledge Graph (Neo4j)**

Nodes created:

- `StratigraphicUnit`  
- `CulturalLayer`  
- `SoilHorizon`  
- `GeoProfile`  
- `ChronologyModel`

Relationships:

- `PART_OF`  
- `OVERLIES`  
- `UNDERLIES`  
- `DATED_TO`  
- `ASSOCIATED_WITH`

### **Focus Mode v2**

- Provides explanations of depositional history  
- Links cultural phases to environmental change  
- Includes uncertainty visualization & narrative provenance  

### **Visualization Outputs**

Formats include:

- PNG/SVG profiles  
- Raster cross-sections (COG/GeoTIFF)  
- Cesium 3D layer models  
- MapLibre overlays  

All visualizations must follow the archaeology `visualization` standards.

---

## 📊 Dataset Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `profiles/flint-hills-profiles-v1` | Excavation Profiles | `profiles/` | 🟢 Active | 2025-11 | Generalized + validated |
| `soil/usda-horizons-v2` | Soil Horizons | `profiles/` | 🟢 Active | 2025-10 | Open-source; CRS standardized |
| `cross-sections/smoky-hill-v1` | Cross-Sections | `cross-sections/` | 🟡 Needs Review | 2025-09 | Requires CARE notes |
| `temporal-models/flint-hills-age-depth-v1` | Chronology Model | `temporal-models/` | 🟢 Active | 2025-11 | Uncertainty bounds included |

---

## 🧠 Example STAC Item (Stratigraphy)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "stratigraphy-flint-hills-v1",
  "bbox": [-101.3, 37.2, -95.6, 40.2],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[ /* generalized */ ]]]
  },
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "start_datetime": "1200-01-01T00:00:00Z",
    "end_datetime": "1450-01-01T00:00:00Z",
    "kfm:provenance": "provenance/stratigraphy-flint-hills-v1.json"
  },
  "assets": {
    "profiles": {
      "href": "https://example.com/stratigraphy/flint_hills_profiles_v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created stratigraphy dataset index; added metadata rules, CARE requirements, STAC/DCAT integration; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Stratigraphy Dataset Team | Initial structure and definitions |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>