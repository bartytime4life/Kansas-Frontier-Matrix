---
title: "🛰️ Kansas Frontier Matrix — Tuttle Creek Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/tuttle-creek/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydrology-tc-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-tuttle-creek-items-index"
semantic_document_id: "kfm-stac-hydrology-tuttle-creek-items-index"
doc_uuid: "urn:kfm:stac:hydrology:tuttle-creek:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Tuttle Creek Hydrology — STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/tuttle-creek/items/README.md`

**Purpose:**  
Provide the complete, authoritative documentation for **all STAC Items** associated with  
Tuttle Creek hydrology, sedimentation, bathymetry, WID 2025, water-quality monitoring, and  
downstream ecological datasets. Defines Item-level metadata, asset standards, ontology mapping,  
lineage rules, and integration with the KFM v11 knowledge graph and Focus Mode v3.

</div>

---

# 📘 0. Overview

This directory contains the **STAC Item files** for Tuttle Creek Lake and its associated hydrologic datasets.

Each Item represents a **single spatiotemporal data asset**, such as:

- Bathymetry DEMs  
- Time-series hydrology data (inflows/outflows)  
- Sediment cores & sediment volumes  
- WID 2025 turbidity, DO, ADCP transects  
- Downstream DO / turbidity responses  
- Ecological surveys  
- Plume propagation polygons  
- Channel morphology updates  

This README defines:

- Required metadata fields  
- Hydrology-specific `kfm:*` extensions  
- Asset rules (COG, GeoJSON, CSVW, NetCDF, MP4)  
- STAC–DCAT–CIDOC–PROV crosswalks  
- ETL → STAC → Graph ingestion  
- Validation & QA  
- Story Node and Focus Mode linkages  

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── tuttle-creek/
            ├── collection.json
            └── items/
                ├── bathymetry-1962.json
                ├── bathymetry-1993.json
                ├── bathymetry-2010.json
                ├── bathymetry-2024.json
                ├── hydrology-inflows-usgs.json
                ├── hydrology-outflows.json
                ├── wid-2025-turbidity-b1.json
                ├── wid-2025-do-b2.json
                ├── wid-2025-density-current.json
                ├── wid-2025-nutrients.json
                ├── sediment-core-locations.json
                ├── sediment-volumes-timeseries.json
                ├── delta-migration.json
                ├── downstream-do.json
                ├── downstream-turbidity.json
                ├── ecology-fish-2025.json
                └── ecology-mussels.json
```

---

# 🛰️ 2. Purpose of STAC Items

STAC Items are the **atomic metadata units** describing:

- A dataset  
- Its geometry  
- Its time coverage  
- Its associated files (assets)  
- Its provenance  
- Its relationship to hydrologic processes  

They enable:

- Search  
- Filtering  
- Map/timeline rendering  
- Dataset lineage  
- Graph ingestion  
- Story Node enrichment  
- Focus Mode v3 data-driven narratives  

---

# 📐 3. Required Metadata Fields (Strict v11 Hydrology Profile)

Each Item **must** include the following:

### ✔ Core STAC Fields
- `stac_version`
- `type = "Feature"`
- `id`
- `collection`
- `geometry`
- `bbox`
- `properties.datetime`
- `assets.*`

### ✔ Hydrology-Specific `kfm:` Extensions
| Field | Description |
|------|-------------|
| `kfm:parameter` | e.g., turbidity, inflow, DO, bathymetry |
| `kfm:units` | SI or hydrology standard |
| `kfm:site` | site identifier (A1/B2/C3, ADCP transect ID, etc.) |
| `kfm:provider` | USACE / USGS / KDHE / KWO / KFM |
| `kfm:method` | survey method, sensor type, algorithm |
| `kfm:lineage` | ETL → STAC → Graph provenance |
| `kfm:quality` | QA/QC flags |
| `kfm:project` | e.g., “WID-2025”, “Sedimentation-History” |
| `kfm:hydro_region` | “Tuttle Creek Reservoir”, “Tailwater" |

### ✔ Temporal Rules
- Use **ISO 8601**  
- Support `start_datetime` and `end_datetime` for intervals  
- Use OWL-Time precision mapping  

---

# 🧭 4. Asset Standards (Hydrology Domain)

### ✔ Allowed Asset Types
| Format | Use Case |
|--------|-----------|
| **COG** | DEMs, DoD, bathymetry |
| **GeoJSON** | ecological polygons, ADCP transects |
| **CSV/CSVW** | time-series hydrology & water quality |
| **NetCDF** | climate forcing, hydrodynamics |
| **MP4** | ADCP or WID plume videos |

### ✔ Asset Keys
Every asset MUST contain:

- `href`  
- `type`  
- `roles`  
- recommended: `title`, `description`, `checksum:sha256`

---

# 🛰️ 5. STAC Item Type Index

### **5.1 Bathymetry Items**
- bathymetry-1962.json  
- bathymetry-1993.json  
- bathymetry-2010.json  
- bathymetry-2024.json  

Represent DEM rasters (COG) and bathymetric surveys.

### **5.2 Hydrology Time-Series Items**
- hydrology-inflows-usgs.json  
- hydrology-outflows.json  

Contain CSVW time-series.

### **5.3 Sediment Items**
- sediment-core-locations.json  
- sediment-volumes-timeseries.json  
- delta-migration.json  

Represent sediment cores, sediment volumes, and delta migration geometry.

### **5.4 WID 2025 Items**
- wid-2025-turbidity-b1.json  
- wid-2025-do-b2.json  
- wid-2025-density-current.json  
- wid-2025-nutrients.json  

### **5.5 Downstream Impact Items**
- downstream-do.json  
- downstream-turbidity.json  

### **5.6 Ecology Items**
- ecology-fish-2025.json  
- ecology-mussels.json  

---

# 🧬 6. DCAT 3.0 Crosswalk

| STAC Field | DCAT Field |
|------------|------------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `assets[].href` | `dcat:downloadURL` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `keywords` | `dcat:keyword` |
| `license` | `dct:license` |

---

# 🕸️ 7. PROV-O Lineage Mapping

Each STAC Item corresponds to:

### Entities
- `prov:Entity` (dataset asset)  

### Activities
- `prov:Activity` (ETL pipeline step)  

### Agents
- `prov:Agent` (USACE, USGS, KDHE, KWO, KFM)

### Required Relationships
- `prov:wasGeneratedBy`  
- `prov:wasAttributedTo`  
- `prov:used`  

---

# 🧠 8. CIDOC-CRM & GeoSPARQL Mapping

Each Item generates:

### CIDOC-CRM entities
- `E73 InformationObject` → the dataset  
- `ObservationSeries` → for time-series  
- `E53 Place` → from geometry  
- `E7 Activity` → event/operation datasets (WID, flood, etc.)  
- `E3 ConditionState` → hydrologic/geomorphic states  

### CRM properties
- `P7_took_place_at`  
- `P70_documents`  
- `P1_is_identified_by`  

### GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

---

# 🛠️ 9. ETL → STAC → Graph Pipeline Requirements

```
Raw Inputs  
    ↓ extract  
Normalize / Reproject / Harmonize  
    ↓ transform  
Asset Production (CSVW / COG / GeoJSON / NetCDF)  
    ↓ annotate-stac  
STAC Item  
    ↓ stac-validate  
Neo4j Entity + Spatial Relationships  
```

---

# 🎯 10. Focus Mode v3 Integration

Focus Mode automatically pulls STAC Items based on:

- place  
- time  
- parameter  
- event  

Example:

Selecting **“WID 2025”** loads:

- turbidity pulses  
- DO sag monitoring  
- density-current ADCP transects  
- nutrient samples  

Selecting **“Downstream Effects”** loads:

- downstream DO Item  
- downstream turbidity Item  
- ecological datasets  

---

# 📖 11. Story Node Integration

Story Nodes reference STAC Items via:

```json
{
  "rel": "uses-dataset",
  "target": "wid-2025-turbidity-b1"
}
```

Narratives such as:

- *“A Reservoir Filling From the Bottom Up”*  
- *“Downstream of the Dam”*  
- *“The 2025 Water Injection Experiment”*  

all rely on datasets cataloged here.

---

# 🚀 12. Expansion Roadmap

Future items may include:

- Sentinel-2 turbidity rasters  
- HEC-RAS 2D hydrodynamic model outputs  
- UAV-based bathymetry reconstructions  
- CMIP6 downscaled hydroclimate projections  
- Real-time MQTT hydrology sensors  
- Longitudinal biological monitoring (annual)  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Tuttle Creek hydrology STAC Items super-index.

---

[⬅️ Back to Tuttle Creek STAC Collection](../README.md) • [🏠 Hydrology STAC Domain](../../README.md) • [📂 Data Home](../../../README.md)

