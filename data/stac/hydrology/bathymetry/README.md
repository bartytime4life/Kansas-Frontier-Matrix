---
title: "🗺️ Kansas Frontier Matrix — Bathymetry STAC Collection (Hydrology Domain, v11 Super-Edition)"
path: "data/stac/hydrology/bathymetry/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Sediment Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-stac-hydro-bathymetry-index-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-bathymetry-index"
semantic_document_id: "kfm-stac-hydrology-bathymetry-index"
doc_uuid: "urn:kfm:stac:hydrology:bathymetry:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🗺️ **Bathymetry STAC Collection — Hydrology Domain (v11 Super-Edition)**  
`data/stac/hydrology/bathymetry/README.md`

**Purpose:**  
Provide the **complete, authoritative technical specification** for all **bathymetry-related STAC datasets**  
in KFM’s Hydrology Domain. Defines Collection architecture, Item metadata, hydrologic semantics,  
COG raster rules, ETL lineage, DCAT/PROV ontology crosswalks, QA/QC requirements, and  
STAC → Graph → Focus Mode v3 integration.

</div>

---

# 📘 0. Overview

Bathymetry is the **foundation dataset** for:

- Sedimentation history  
- Reservoir storage-loss analysis  
- Density-current modeling  
- WID 2025 transport predictions  
- Flood-hydraulic modeling  
- Downstream geomorphic response  
- Longitudinal reservoir evolution  
- Story Node narratives  

This directory contains all **bathymetry STAC Collections & Items** for all Kansas reservoirs,  
beginning with **Tuttle Creek (1962–2024)**, and extending to **Milford, Perry, Clinton**, and statewide DEMs.

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── bathymetry/
            ├── collection.json
            └── items/
                ├── bathy-1962.json
                ├── bathy-1975.json
                ├── bathy-1993.json
                ├── bathy-2010.json
                ├── bathy-2019.json
                ├── bathy-2024.json
                ├── dod-1962-1993.json
                ├── dod-1993-2010.json
                └── dod-2010-2024.json
```

---

# 🌊 2. Bathymetric Dataset Classes

## ✔ 2.1 Original USACE Surveys  
- 1960s single-beam or digitized contour maps  
- 1975, 1993, 2010, 2019, 2024 multibeam datasets  
- Survey metadata (vessel, sonar, transducer depth, vertical datum)

## ✔ 2.2 Derived DEM Grids (COG Rasters)  
- Gridded depth rasters  
- Resolution: 1–10 m (or USACE grid standard)  
- Reprojected to EPSG:4326 or consistent CRS

## ✔ 2.3 DoD (Difference of DEMs)  
- Sediment accumulation over decades  
- Units: meters of elevation gain (positive = deposition)

## ✔ 2.4 Delta & Forebay Geometry  
- Digitized delta front  
- Forebay sediment “bullnose” footprint  
- Plume routing surfaces

## ✔ 2.5 Raster Metadata  
Each raster must include:

- `proj:*` extension  
- Vertical datum metadata  
- Pixel depth statistics  
- Processing history  
- Checksum  
- STAC asset roles: `[data, derived, overview]`

---

# 🛰️ 3. Bathymetry STAC Profile (KFM-Hydro-Bathy-v11)

Every Item in this Collection **must comply with this domain profile**.

### Required STAC fields
- `stac_version = "1.0.0"`  
- `type = "Feature"`  
- `id`  
- `collection`  
- `geometry`  
- `bbox`  
- `properties.datetime`  
- `assets`

### Required `properties` → Hydrology Profile
| Field | Description |
|-------|-------------|
| `kfm:parameter` | `bathymetry` or `dod` |
| `kfm:units` | `meters`, `meters_above_datum`, or `meters_difference` |
| `kfm:provider` | USACE KC District, KWO, etc. |
| `kfm:method` | `multibeam`, `singlebeam`, `digitized-contours`, `DoD` |
| `kfm:lineage` | ETL → interpolation → grid creation → STAC |
| `kfm:quality` | QA category |
| `kfm:crs` | CRS used pre-reprojection |
| `kfm:survey_id` | Survey metadata key |
| `kfm:processing_history` | Detailed processing steps |

### Asset requirements
COG raster assets must include:

```
roles: ["data"]
type: "image/tiff; application=geotiff; profile=cloud-optimized"
proj:epsg
proj:shape
proj:transform
checksum:sha256
```

---

# 📏 4. Reprojection & Vertical Datum Rules

## ✔ 4.1 Horizontal CRS  
USACE surveys may arrive as:

- State Plane  
- UTM  
- USACE project grids  
- Localized CRS  

**All bathymetry COGs must be reprojected to:**

**EPSG:4326** (unless otherwise required by modeling subsystems)

## ✔ 4.2 Vertical Datum  
Surveys must specify:

- NAVD88  
- NGVD29  
- Local reservoir datum  

Derived depths must track:

- `z = reservoir_elevation – bed_elevation`

---

# 🛠️ 5. ETL Pipeline — Bathymetry-Specific

Pipeline:

```
Raw Multibeam Data (.xyz / .all / .s7k)
       ↓
QA/QC filtering (beam angle, noise, spikes)
       ↓
TIN or point-cloud → raster interpolation
       ↓
DEM generation (COG)
       ↓
DoD differencing (optional)
       ↓
STAC Item creation
       ↓
STAC validation
       ↓
Graph ingestion (Neo4j)
```

All steps must be captured in `mcp/experiments/hydrology/bathymetry/*`.

---

# 🧬 6. PROV-O, DCAT, CIDOC-CRM Crosswalk (Bathymetry)

### STAC Item → DCAT  
- `id` → `dct:identifier`  
- `assets.*.href` → `dcat:downloadURL`  
- `description` → `dct:description`  
- `extent.spatial` → `dct:spatial`  

### STAC Item → PROV  
- `prov:Entity` = DEM or DoD  
- `prov:Activity` = DEM creation process  
- `prov:Agent` = USACE / KWO / KFM  

### STAC Item → CIDOC-CRM  
- `E73 InformationObject` = bathy raster  
- `E53 Place` = reservoir polygon  
- `E7 Activity` = survey  
- `E3 ConditionState` = reservoir bed condition  

### GeoSPARQL  
- Raster footprint stored as `geo:hasGeometry`  
- DoD changes as temporal `E3 ConditionState` transitions

---

# 🧭 7. Focus Mode v3 Integration

Focus Mode uses bathymetry STAC Items for:

- Reservoir 3D visualization  
- Delta and forebay analysis  
- Sedimentation timelines  
- WID 2025 density-current simulation context  
- Flood operation scenario analysis  

Selecting **“Sedimentation History”** auto-loads:

- 1962, 1993, 2010, 2019, 2024 bathy COGs  
- DoD rasters for Δ elevation  
- Delta migration polygons  

---

# 📚 8. Story Node Integration

Story Nodes referencing bathymetry:

- **“A Reservoir Filling From the Bottom Up”**  
- **“The 2019 Flood and Forebay Transformation”**  
- **“The 2025 WID Demonstration”**

All bathymetry Items must be accessible via:

```json
{
  "rel": "uses-dataset",
  "target": "bathy-2019"
}
```

---

# 📁 9. Example STAC Item — Bathymetry (COG)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tuttle-creek-bathymetry-2019",
  "collection": "tuttle-creek-bathymetry",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2019-09-30T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:provider": "USACE Kansas City District",
    "kfm:method": "multibeam",
    "kfm:lineage": "etl/bathy2019_v3",
    "kfm:quality": "A",
    "kfm:crs": "NAVD88",
    "kfm:processing_history": "cleaning → interpolation → reprojection → COG creation"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/data/bathy_2019.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

# 📈 10. Bathymetry QA/QC Rules

### ✔ DEM Validation
- Min/max depth thresholds  
- No nodata “spikes” or void artifacts  
- Seamless shoreline transitions  
- Density-current channel preserved  
- Delta front edge sharpness maintained  

### ✔ DoD Validation
- Positive values = deposition  
- Negative values = erosion  
- Zero bias check vs reference benchmarks  

---

# 🚀 11. Expansion Roadmap

Future bathymetry STAC Items:

- Annual multibeam surveys  
- 3D point-cloud STAC Items (`.las`, `.laz`)  
- UAV photobathymetry STAC Items  
- Machine learning bathymetry interpolation datasets  
- Reservoir storage projections (2030–2100)  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of bathymetry STAC Collection index (super-edition).

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [⬅ Back to Hydrology Data Index](../../../hydrology/README.md) • [🏠 KFM Master Guide](../../../../docs/reference/kfm_v11_master_documentation.md)

